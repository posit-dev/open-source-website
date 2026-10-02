#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pyyaml>=6.0",
#     "rich>=13.0.0",
# ]
# ///
"""
Migrate cheat sheets from a local clone of rstudio/cheatsheets.

For each cheat sheet in scripts/cheatsheet-migration.yaml this builds (or
updates) content/resources/cheatsheets/<slug>/:

- copies the English PDF, translation PDFs, and source files (Keynote,
  PowerPoint, ... — stored in Git LFS, see .gitattributes),
- compresses the PDFs with compress-cheatsheet-pdf.py,
- regenerates the page thumbnails with create-cheatsheet-thumbnails.py,
- writes the markdown body: keeps the existing one, ports the old site's
  HTML version (from Quarto's freeze cache, so R output is included), or
  uses the summary from the manifest,
- writes the front matter (by, people, translations, source_files, ...).

Usage:
    scripts/migrate-cheatsheet.py --old-repo ~/repos/rstudio/cheatsheets tidyr purrr
    scripts/migrate-cheatsheet.py --old-repo ~/repos/rstudio/cheatsheets --all
"""

import argparse
import json
import re
import shutil
import textwrap
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any

import yaml
from rich.console import Console

console = Console(stderr=True, width=200)

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
CONTENT_DIR = PROJECT_ROOT / "content" / "resources" / "cheatsheets"
MANIFEST = SCRIPT_DIR / "cheatsheet-migration.yaml"
REPO_URL = "https://github.com/posit-dev/open-source-website"

# Front matter keys in output order; any other existing keys follow
KEY_ORDER = [
    "title", "image", "color", "resource_type", "by", "date", "description",
    "download_url", "people", "thumbnails", "software", "languages",
    "source_files", "translations",
]


# --------------------------------------------------------------------------
# Front matter
# --------------------------------------------------------------------------

def read_index(path: Path) -> tuple[dict[str, Any], str]:
    if not path.exists():
        return {}, ""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    _, fm, body = text.split("---", 2)
    return yaml.safe_load(fm) or {}, body.lstrip("\n")


def write_index(path: Path, fm: dict[str, Any], body: str) -> None:
    ordered = {k: fm[k] for k in KEY_ORDER if k in fm and fm[k] not in (None, [], "")}
    ordered.update({k: v for k, v in fm.items() if k not in ordered and v not in (None, [], "")})
    yaml_text = yaml.dump(ordered, allow_unicode=True, sort_keys=False, width=1000).strip()
    body = body.strip()
    path.write_text(f"---\n{yaml_text}\n---\n" + (f"\n{body}\n" if body else ""), encoding="utf-8")


# --------------------------------------------------------------------------
# Porting the old site's HTML version (Quarto freeze markdown → Hugo markdown)
# --------------------------------------------------------------------------

CALLOUT_LABELS = {"note": "Note", "tip": "Tip", "important": "Important",
                  "caution": "Caution", "warning": "Warning"}
FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})\s*(.*)$")
DIV_OPEN_RE = re.compile(r"^\s*(:{3,})\s*(\{.*\}|[\w-]+)\s*$")
DIV_CLOSE_RE = re.compile(r"^\s*:{3,}\s*$")


def convert_fence_info(info: str) -> str:
    """```{.r .cell-code} → ```r, ```{.yaml filename="x"} → ```yaml {filename="x"}"""
    info = info.strip()
    if not info.startswith("{"):
        return info
    inner = info.strip("{}").strip()
    if inner.startswith("{"):  # ```{{r}} (literal chunk syntax in examples)
        return "markdown"
    lang = ""
    m = re.match(r"\.([\w+-]+)", inner)
    if m:
        lang = m.group(1)
    elif re.match(r"^[\w+-]+$", inner):
        lang = inner
    attrs = re.findall(r'(filename)="([^"]*)"', inner)
    attr_text = " ".join(f'{k}="{v}"' for k, v in attrs)
    if lang == "default":
        lang = "text"
    return f"{lang} {{{attr_text}}}" if attr_text else lang


def parse_div_attrs(spec: str) -> tuple[set[str], dict[str, str]]:
    spec = spec.strip()
    if not spec.startswith("{"):
        return {spec}, {}
    inner = spec.strip("{}")
    classes = set(re.findall(r"\.([\w-]+)", inner))
    attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', inner))
    for k, v in re.findall(r'([\w-]+)=([^\s"}]+)', inner):
        attrs.setdefault(k, v)
    return classes, attrs


def escape_shortcodes(text: str) -> str:
    # Quarto escapes shortcodes in examples as {{{< x >}}}; Hugo needs {{</* x */>}}
    text = re.sub(r"\{\{\{<\s*(.*?)\s*>\}\}\}", r"{{</* \1 */>}}", text)
    text = re.sub(r"\{\{<(?!/\*)\s*(.*?)\s*>\}\}", r"{{</* \1 */>}}", text)
    return text


def clean_inline(line: str, images: set[str]) -> str:
    # Images with Quarto attributes; fig-alt becomes the alt text
    def img(m: re.Match) -> str:
        alt, src, attrs = m.group(1), m.group(2), m.group(3) or ""
        fig_alt = re.search(r'fig-alt="([^"]*)"', attrs)
        if fig_alt and not alt:
            alt = fig_alt.group(1)
        if src.startswith("images/"):
            images.add(src)
        return f"![{alt}]({src})"
    line = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)(\{[^}]*\})?", img, line)
    for src in re.findall(r'<img[^>]+src="(images/[^"]+)"', line):
        images.add(src)
    # Bracketed spans [text]{.class} → text (but not links)
    line = re.sub(r"(?<!\])\[([^\[\]]+)\]\{[^}]*\}", r"\1", line)
    # Heading attributes only Quarto understands
    line = re.sub(r"^(#{1,6} .*?)\s*\{aria-hidden=\"true\"\}\s*$", r"\1", line)
    return line


def heading_anchor(title: str) -> str:
    """Goldmark's default heading ID: lowercase, spaces to dashes, drop punctuation."""
    anchor = re.sub(r"[^\w\- ]", "", title.lower()).strip()
    return re.sub(r"\s", "-", anchor)


def link_implicit_headings(text: str) -> str:
    """Pandoc links [Heading text] to that heading; make the link explicit."""
    headings = {m.group(1).strip() for m in re.finditer(r"^#{1,6}\s+(.*?)\s*$", text, flags=re.M)}
    def repl(m: re.Match) -> str:
        label = m.group(1)
        return f"[{label}](#{heading_anchor(label)})" if label in headings else m.group(0)
    parts = re.split(r"(```.*?```|`[^`]*`)", text, flags=re.S)  # leave code alone
    return "".join(p if i % 2 else re.sub(r"(?<![!\]\\])\[([^\]\[]+)\](?![(\[{:])", repl, p)
                   for i, p in enumerate(parts))


GRID_BORDER_RE = re.compile(r"^(\s*)\+[-=:+]+\+\s*$")


def grid_table_to_html(lines: list[str], indent: str, caption: str) -> list[str]:
    """Convert a Pandoc grid table to an HTML table with markdown cell content."""
    border = lines[0][len(indent):].rstrip()
    cuts = [i for i, ch in enumerate(border) if ch == "+"]
    rows: list[tuple[bool, list[str]]] = []  # (is_header, cells)
    current: list[str] = []
    header_done = False
    for line in lines[1:]:
        body = line[len(indent):].rstrip()
        if GRID_BORDER_RE.match(line):
            if current:
                cells = []
                for a, b in zip(cuts, cuts[1:]):
                    cell = "\n".join(r[a + 1:b].rstrip() for r in current)
                    cells.append(textwrap.dedent(cell).strip("\n"))
                is_header = "=" in body and not header_done
                header_done = header_done or is_header
                if any(cells):
                    rows.append((is_header, cells))
            current = []
        else:
            current.append(body.ljust(cuts[-1] + 1))
    out = ["<table>"]
    if caption:
        out.append(f"<caption>{caption}</caption>")
    for is_header, cells in rows:
        tag = "th" if is_header else "td"
        out.append("<tr>")
        for cell in cells:
            out += [f"<{tag}>", "", cell, "", f"</{tag}>"] if cell else [f"<{tag}></{tag}>"]
        out.append("</tr>")
    out.append("</table>")
    return [indent + l if l else "" for l in out]


def convert_grid_tables(md: str) -> str:
    lines = md.split("\n")
    out: list[str] = []
    fence = None
    i = 0
    while i < len(lines):
        line = lines[i]
        m = FENCE_RE.match(line)
        if m and (fence is None or line.strip().startswith(fence)):
            fence = None if fence else m.group(2)
        mb = GRID_BORDER_RE.match(line)
        if fence is None and mb and i + 1 < len(lines) and lines[i + 1].lstrip().startswith("|"):
            indent = mb.group(1)
            j = i + 1
            while j < len(lines) and lines[j].lstrip()[:1] in ("|", "+"):
                j += 1
            table = lines[i:j]
            k = j
            while k < len(lines) and not lines[k].strip():
                k += 1
            caption = ""
            if k < len(lines) and lines[k].lstrip().startswith(": "):
                caption = lines[k].strip()[2:]
                j = k + 1
            out += grid_table_to_html(table, indent, caption)
            i = j
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def port_freeze_markdown(md: str) -> tuple[str, set[str]]:
    """Convert Quarto's knitted markdown into Hugo-flavored markdown."""
    if md.startswith("---"):
        md = md.split("---", 2)[2]
    md = convert_grid_tables(md)
    lines = md.split("\n")
    out: list[str] = []
    images: set[str] = set()
    stack: list[dict[str, Any]] = []  # open fenced divs
    fence: str | None = None  # open code fence marker
    raw_html: list[str] | None = None

    def emit(line: str) -> None:
        for frame in reversed(stack):
            if frame.get("drop"):
                return
        out.append(line)

    i = 0
    while i < len(lines):
        line = lines[i]
        m = FENCE_RE.match(line)
        if fence is None and m and not DIV_OPEN_RE.match(line):
            indent, marker, info = m.groups()
            if info.strip() == "{=html}":
                raw_html = []
                fence = marker
                i += 1
                continue
            fence = marker
            emit(f"{indent}{marker}{convert_fence_info(info)}")
            i += 1
            continue
        if fence is not None:
            if line.strip().startswith(fence) and line.strip().strip(fence[0]) == "":
                if raw_html is not None:
                    content = "\n".join(raw_html).strip()
                    if content and not re.fullmatch(r"<!--.*?-->", content, flags=re.S):
                        for raw in raw_html:
                            emit(raw)
                    raw_html = None
                else:
                    emit(line)
                fence = None
            elif raw_html is not None:
                raw_html.append(line)
            else:
                emit(line)
            i += 1
            continue

        mo = DIV_OPEN_RE.match(line)
        if mo:
            classes, attrs = parse_div_attrs(mo.group(2))
            frame: dict[str, Any] = {"classes": classes}
            callout = next((c[len("callout-"):] for c in classes if c.startswith("callout-")), None)
            # Margin cell with the old site's logo, PDF link, and translation list
            if "column-margin" in classes and "cell" in classes:
                frame["drop"] = True
            elif callout in CALLOUT_LABELS:
                title = attrs.get("title", "")
                # Callouts use a leading heading as their title
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                hm = re.match(r"^#{1,6}\s+(.*?)\s*(\{[^}]*\})?\s*$", lines[j]) if j < len(lines) else None
                if hm:
                    title = hm.group(1)
                    i = j  # skip the heading line
                if attrs.get("collapse") == "true":
                    frame["close"] = ["", "</details>"]
                    emit("<details>")
                    emit(f"<summary>{title or CALLOUT_LABELS[callout]}</summary>")
                    emit("")
                else:
                    label = CALLOUT_LABELS[callout]
                    emit(f'<div class="callout callout-{callout}" role="note" aria-label="{label}">')
                    if title:
                        emit(f'<div class="callout-header"><span class="callout-title">{title}</span></div>')
                    emit('<div class="callout-body">')
                    emit("")
                    frame["close"] = ["", "</div>", "</div>"]
            stack.append(frame)
            i += 1
            continue
        if DIV_CLOSE_RE.match(line) and stack:
            frame = stack.pop()
            for closing in frame.get("close", []):
                emit(closing)
            i += 1
            continue

        if re.fullmatch(r"\s*<!--\s*PAGE \d+\s*-->\s*", line):
            i += 1
            continue
        emit(clean_inline(line, images))
        i += 1

    text = link_implicit_headings("\n".join(out))
    text = escape_shortcodes(text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    # Only copy images the ported text still references
    images = set(re.findall(r"\]\((images/[^)\s]+)\)", text)) | set(re.findall(r'src="(images/[^"]+)"', text))
    return text, images


def clean_existing_body(body: str) -> str:
    """Remove Quarto chunk options that leaked into earlier ports."""
    lines = [l for l in body.split("\n") if not re.match(r"^\s*#\|", l)]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines))


# --------------------------------------------------------------------------
# Files
# --------------------------------------------------------------------------

def copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".DS_Store", "*.aux", "*.log"))
    else:
        shutil.copyfile(src, dst)


def compress(pdfs: list[Path]) -> None:
    if pdfs:
        subprocess.run([str(SCRIPT_DIR / "compress-cheatsheet-pdf.py"), *map(str, pdfs)],
                       check=False)


def make_thumbnails(pdf: Path, directory: Path) -> list[str]:
    for old in directory.glob("page-*.png"):
        old.unlink()
    subprocess.run([str(SCRIPT_DIR / "create-cheatsheet-thumbnails.py"), "--pdf", str(pdf)],
                   check=True, capture_output=True)
    pages = sorted(directory.glob("page-*.png"), key=lambda p: int(re.search(r"\d+", p.stem).group()))
    return [p.name for p in pages]


def source_entry(slug: str, rel: str, fmt: str, is_dir: bool) -> dict[str, str]:
    name = Path(rel).name
    if is_dir:
        return {"url": f"{REPO_URL}/tree/main/content/resources/cheatsheets/{slug}/source/{name}",
                "format": fmt}
    return {"file": name, "format": fmt}


# --------------------------------------------------------------------------
# Migration
# --------------------------------------------------------------------------

def migrate(slug: str, entry: dict[str, Any], old_repo: Path, summaries: dict[str, Any],
            skip_pdf_work: bool = False) -> None:
    directory = CONTENT_DIR / slug
    directory.mkdir(parents=True, exist_ok=True)
    index = directory / "_index.md"
    fm, body = read_index(index)
    is_new = not fm
    extra = summaries.get(slug, {})
    pdfs_to_compress: list[Path] = []

    # English PDF (keeps its old file name)
    pdf_path: Path | None = None
    if entry.get("old"):
        src = old_repo / entry.get("old_pdf", f"{entry['old']}.pdf")
        pdf_path = directory / src.name
        if not skip_pdf_work:
            if fm.get("download_url") and fm["download_url"] != src.name:
                (directory / fm["download_url"]).unlink(missing_ok=True)
            copy(src, pdf_path)
            pdfs_to_compress.append(pdf_path)
        fm["download_url"] = src.name
    elif fm.get("download_url"):
        pdf_path = directory / fm["download_url"]

    # Translations
    translations = []
    keep_files = set()
    for t in entry.get("translations", []):
        src = old_repo / t["file"]
        dst = directory / src.name
        keep_files.add(src.name)
        if not skip_pdf_work:
            copy(src, dst)
            pdfs_to_compress.append(dst)
        item = {"language": t["language"], "lang": t["lang"], "file": src.name}
        for k in ("edition", "updated", "added", "people"):
            if t.get(k):
                item[k] = t[k]
        if isinstance(t.get("source"), list):  # several files, e.g. one SVG per page
            stem = Path(t["file"]).stem
            for f in t["source"]:
                copy(old_repo / f, directory / "source" / stem / Path(f).name)
            item["source"] = f"{REPO_URL}/tree/main/content/resources/cheatsheets/{slug}/source/{stem}"
        elif t.get("source"):
            s = old_repo / t["source"]
            if s.is_dir():
                copy(s, directory / "source" / s.name)
                item["source"] = f"{REPO_URL}/tree/main/content/resources/cheatsheets/{slug}/source/{s.name}"
            else:
                # Name it after the translation (base-r.pptx in chinese/ → base-r_zh.pptx)
                name = f"{Path(t['file']).stem}{s.suffix}"
                copy(s, directory / name)
                item["source"] = name
        translations.append(item)
    # Remove translation PDFs that belong elsewhere (e.g. shiny-python_es.pdf on shiny)
    for old in fm.get("translations") or []:
        for f in (old.values() if "file" not in old else [old["file"]]):
            if f not in keep_files and f != fm.get("download_url"):
                (directory / f).unlink(missing_ok=True)

    # Source files
    source_files = []
    for s in entry.get("sources", []):
        src = old_repo / s["path"]
        if s.get("dir"):
            copy(src, directory / "source" / src.name)
        else:
            copy(src, directory / src.name)
        source_files.append(source_entry(slug, s["path"], s["format"], bool(s.get("dir"))))
    source_files += [dict(l) for l in entry.get("source_links", [])]
    if slug == "polars":
        source_files = [{"file": "polars-cheatsheet.ai", "format": "Illustrator"}]

    if pdfs_to_compress:
        compress(pdfs_to_compress)

    # Thumbnails (also rewrites `thumbnails:` in an existing _index.md)
    if pdf_path and not skip_pdf_work and entry.get("old"):
        if not index.exists():
            index.write_text("---\ntitle: placeholder\n---\n", encoding="utf-8")
        fm["thumbnails"] = make_thumbnails(pdf_path, directory)

    # Body
    mode = entry.get("body", "keep")
    if mode == "port":
        freeze = old_repo / "_freeze" / "html" / entry["old"] / "execute-results" / "html.json"
        md = json.loads(freeze.read_text(encoding="utf-8"))["result"]["markdown"]
        body, images = port_freeze_markdown(md)
        for img in sorted(images):
            copy(old_repo / "html" / img, directory / img)
    elif mode == "summary":
        body = extra.get("summary") or entry.get("summary") or body
    else:
        body = clean_existing_body(body)

    # Front matter
    fm["title"] = fm.get("title") if not is_new and fm.get("title") != "placeholder" else (
        extra.get("title") or entry.get("title") or slug)
    if is_new and extra.get("title"):
        fm["title"] = extra["title"]
    fm.setdefault("image", "page-1.png")
    fm["resource_type"] = "cheatsheet"
    fm["by"] = entry["by"]
    updated = entry.get("updated")
    new_date = f"{updated}-01" if updated else date.today().isoformat()
    old_date = str(fm.get("date", ""))
    fm["date"] = max(old_date, new_date) if old_date and not is_new else new_date
    if extra.get("description") or entry.get("description"):
        fm["description"] = extra.get("description") or entry["description"]
    fm["people"] = entry.get("people") or fm.get("people")
    if entry.get("software"):
        fm["software"] = entry["software"]
    if entry.get("languages"):
        fm["languages"] = entry["languages"]
    fm["source_files"] = source_files or fm.get("source_files")
    fm["translations"] = translations
    fm.pop("source_url", None)
    write_index(index, fm, body)
    console.print(f"[green]✓[/] {slug}: {len(translations)} translations, {len(source_files)} sources, body={mode}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Migrate cheat sheets from rstudio/cheatsheets.")
    parser.add_argument("slugs", nargs="*", help="Cheat sheet slugs (keys in the manifest)")
    parser.add_argument("--all", action="store_true", help="Migrate every cheat sheet in the manifest")
    parser.add_argument("--old-repo", type=Path, required=True, help="Local clone of rstudio/cheatsheets")
    parser.add_argument("--summaries", type=Path, action="append", default=[],
                        help="YAML file(s) with title/description/summary per slug (overrides manifest)")
    parser.add_argument("--skip-pdf-work", action="store_true",
                        help="Don't copy/compress PDFs or regenerate thumbnails (front matter and body only)")
    args = parser.parse_args()

    manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))["sheets"]
    summaries: dict[str, Any] = {}
    for f in args.summaries:
        summaries.update(yaml.safe_load(f.read_text(encoding="utf-8")) or {})
    slugs = list(manifest) if args.all else args.slugs
    unknown = [s for s in slugs if s not in manifest]
    if unknown:
        parser.error(f"not in manifest: {', '.join(unknown)}")
    for slug in slugs:
        migrate(slug, manifest[slug], args.old_repo.expanduser(), summaries, args.skip_pdf_work)


if __name__ == "__main__":
    main()
