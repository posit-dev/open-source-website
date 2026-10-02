#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pyyaml>=6.0",
#     "rich>=13.0.0",
# ]
# ///
"""
Validate cheat sheet bundles in content/resources/cheatsheets/.

Checks per cheat sheet:
- `by` is `posit` or `community`; a PDF whose footer says "Posit Software,
  PBC" must have `by: posit`
- files referenced by download_url, thumbnails, image, translations, and
  source_files exist in the bundle
- translation labels are unique
- `languages` is present (empty only for language-agnostic sheets)
- `software` values exist under content/software/
- source files (*.key, *.pptx, *.ai) are stored as Git LFS pointers
- tagged PDFs stay tagged (compare with --old-repo)

Exits with status 1 if any errors are found.

Usage:
    scripts/validate-cheatsheets.py [--old-repo ~/repos/rstudio/cheatsheets] [slug ...]
"""

import argparse
import subprocess
import sys
from pathlib import Path

import yaml
from rich.console import Console

console = Console(stderr=True, width=200)

PROJECT_ROOT = Path(__file__).parent.parent
CONTENT_DIR = PROJECT_ROOT / "content" / "resources" / "cheatsheets"
SOFTWARE_DIR = PROJECT_ROOT / "content" / "software"
LFS_SUFFIXES = {".key", ".pptx", ".ai"}


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    return yaml.safe_load(text.split("---", 2)[1]) or {}


def pdf_text(path: Path) -> str:
    return subprocess.run(["pdftotext", "-q", "-l", "2", str(path), "-"],
                          capture_output=True, text=True).stdout


def is_tagged(path: Path) -> bool:
    info = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True).stdout
    return any(l.startswith("Tagged:") and l.split()[-1] == "yes" for l in info.splitlines())


def lfs_files() -> set[str]:
    out = subprocess.run(["git", "lfs", "ls-files", "--name-only"], cwd=PROJECT_ROOT,
                         capture_output=True, text=True).stdout
    return set(out.split())


def tracked_files() -> set[str]:
    out = subprocess.run(["git", "ls-files", str(CONTENT_DIR)], cwd=PROJECT_ROOT,
                         capture_output=True, text=True).stdout
    return set(out.split("\n"))


def validate(directory: Path, old_repo: Path | None, lfs: set[str], tracked: set[str]) -> list[str]:
    errors: list[str] = []
    fm = front_matter(directory / "_index.md")

    by = fm.get("by")
    if by not in ("posit", "community"):
        errors.append(f"by: must be posit or community (got {by!r})")

    def exists(name: str, what: str) -> None:
        if name and not (directory / name).exists():
            errors.append(f"{what} not found: {name}")

    exists(fm.get("download_url"), "download_url")
    exists(fm.get("image"), "image")
    for thumb in fm.get("thumbnails") or []:
        exists(thumb, "thumbnail")

    pdf = directory / fm["download_url"] if fm.get("download_url") else None
    if pdf and pdf.exists() and by != "posit" and "Posit Software, PBC" in pdf_text(pdf):
        errors.append("PDF footer says Posit Software, PBC but by is not posit")

    labels = []
    for t in fm.get("translations") or []:
        if "file" not in t:
            errors.append(f"translation in legacy format: {t}")
            continue
        labels.append(t.get("language"))
        exists(t["file"], "translation")
        if t.get("source") and not str(t["source"]).startswith("http"):
            exists(t["source"], "translation source")
    duplicates = {l for l in labels if labels.count(l) > 1}
    if duplicates:
        errors.append(f"duplicate translation labels: {', '.join(sorted(duplicates))}")

    for s in fm.get("source_files") or []:
        if "file" in s:
            exists(s["file"], "source file")
        elif "url" not in s:
            errors.append(f"source_files entry needs file or url: {s}")

    if "languages" not in fm:
        errors.append("languages missing")

    for sw in fm.get("software") or []:
        if not (SOFTWARE_DIR / sw).is_dir():
            errors.append(f"software not found in content/software/: {sw}")

    for f in directory.rglob("*"):
        if f.suffix.lower() in LFS_SUFFIXES:
            rel = str(f.relative_to(PROJECT_ROOT))
            if rel in tracked and rel not in lfs:
                errors.append(f"not stored in Git LFS: {f.name}")

    if old_repo:
        for f in directory.glob("*.pdf"):
            matches = list(old_repo.glob(f.name)) + list(old_repo.glob(f"translations/*/{f.name}"))
            if matches and is_tagged(matches[0]) and not is_tagged(f):
                errors.append(f"lost PDF tags: {f.name}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate cheat sheet bundles.")
    parser.add_argument("slugs", nargs="*", help="Cheat sheets to check (default: all)")
    parser.add_argument("--old-repo", type=Path, help="Local clone of rstudio/cheatsheets (enables tag check)")
    args = parser.parse_args()

    dirs = [CONTENT_DIR / s for s in args.slugs] if args.slugs else sorted(
        d for d in CONTENT_DIR.iterdir() if (d / "_index.md").exists())
    lfs, tracked = lfs_files(), tracked_files()
    old_repo = args.old_repo.expanduser() if args.old_repo else None
    total = 0
    for d in dirs:
        errors = validate(d, old_repo, lfs, tracked)
        total += len(errors)
        for e in errors:
            console.print(f"[red]✗[/] {d.name}: {e}")
    console.print(f"{len(dirs)} cheat sheets checked, {total} problem(s)")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
