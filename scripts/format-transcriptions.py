#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "anthropic>=0.40.0",
#   "python-dotenv>=1.0.0",
#   "tomli>=2.0.0; python_version < '3.11'",
# ]
# ///

"""
Format VTT transcription files into HTML fragments using the Anthropic API.

For each subdirectory under content/resources/videos/:
- Skip if transcription.txt already exists (unless --force).
- Skip if _index.md frontmatter has transcribe: false.
- Skip if transcription.vtt does not exist.
- For long videos (> 90 min), split the VTT into chunks and process each
  segment separately, then concatenate the results.
- After the API call, inject <a href="..."> links for known people and software.
"""

import argparse
import asyncio
import os
import random
import re
import sys
from pathlib import Path
from typing import Any

import anthropic
import yaml
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TaskID,
    TextColumn,
    TimeElapsedColumn,
)

try:
    import tomllib
except ImportError:
    import tomli as tomllib  # type: ignore[no-redef]

console = Console(stderr=True)

MAX_RETRIES = 5
BASE_BACKOFF = 1.0
CHUNK_DURATION_S = 1_800  # 30 min per chunk (default)
LONG_VIDEO_THRESHOLD_S = 5_400  # 90 min — chunk automatically

PROMPT = """\
You convert WebVTT transcription files into clean HTML fragments for video pages.

## Your role
You receive a WebVTT file, optionally preceded by metadata about the video.
You return an HTML fragment — nothing else.

## Strict output rules
- Output ONLY the HTML fragment. No explanations, no Markdown fences
  (no ```html), no prose before or after the HTML.
- Use ONLY these four element types: <h3>  <p>  <a>  <blockquote>
- Do NOT include <html>, <head>, <body>, <div>, <span>, <h1>, <h2>, <h4>–<h6>,
  or any other element.
- Do NOT add class, id, style, or any attribute other than data-t on <a>.

## Timestamps → data-t attribute
Every <a> element MUST have a data-t attribute set to the start timestamp of
that VTT cue expressed in WHOLE SECONDS (floor, not round).

Conversion formula:  data-t = HH*3600 + MM*60 + SS  (discard milliseconds)

  00:00:00.000  →  data-t="0"
  00:01:30.500  →  data-t="90"
  00:04:46.999  →  data-t="286"
  01:02:03.100  →  data-t="3723"

## Text — keep it verbatim
Do NOT paraphrase, correct grammar, fix spelling, or improve wording.
Copy the spoken words exactly as they appear in the VTT, including filler
words ("um", "uh", "sort of", "you know") and false starts.

## Correcting technology-name mishearings
The metadata lists technologies used in this video. If a word is clearly a
phonetic mishearing of one of those technology names, silently correct it.

  "Korto" or "Corto"  →  Quarto   (if Quarto is listed)
  "R Studio"          →  RStudio  (if RStudio is listed)

Only correct when you are confident. Leave all other words verbatim.

## Combining multi-cue sentences
A sentence in the VTT often spans several consecutive cues.
Join them into a single sentence; each cue becomes its own <a> element.
Put a single space between consecutive <a> elements within a sentence.

## Paragraphs
Wrap sentences in <p> elements.  Start a NEW paragraph when ANY of these
conditions holds:
  - There is a timestamp gap larger than roughly 5 seconds between cues.
  - The topic changes.
  - The speaker changes (panels, Q&A, multi-person sessions).
  - The paragraph would exceed roughly 5–7 sentences.

## Section headings
You may group related paragraphs under an <h3> heading.
Rules:
  - Use sentence casing (e.g. "Setting up the environment", not "Setting Up
    The Environment").
  - Keep headings short — a few words to a short phrase.
  - Only add a heading when a clear topic shift justifies it.
  - Do NOT start a heading at the very beginning of the document; the first
    content should be a <p> or <blockquote>.
  - Do NOT add headings so frequently that every paragraph gets one.

## Blockquotes
Identify 0–3 memorable, insightful, or surprising quotes.
For each quote, keep the sentence(s) in their paragraph AND add a <blockquote>
immediately after that paragraph repeating the exact same <a> elements.
The blockquote is a pull quote — it duplicates text that also appears in prose.
Rules:
  - At most one quote per 10 minutes of video.
  - Space them evenly throughout the document.
  - Keep the quote verbatim.
  - If no quote stands out, omit blockquotes entirely — that is fine.

## Examples

### ✗ WRONG — text was modified
VTT:  I was kind of unsure about this approach
HTML: <a data-t="120">I was somewhat uncertain about this method</a>
WHY:  The wording was changed. Keep it verbatim.

### ✗ WRONG — data-t used minutes instead of seconds
VTT:  00:02:05.500 --> 00:02:10.000
      some text
HTML: <a data-t="2">some text</a>
WHY:  2 min 5 sec = 125 seconds; correct value is data-t="125".

### ✗ WRONG — text not wrapped in <p>
HTML: <a data-t="0">Hello everyone.</a> <a data-t="5">Today we talk about R.</a>
WHY:  Every sentence must live inside a <p> element.

### ✗ WRONG — disallowed elements
HTML: <h2>Introduction</h2><p>...</p>
WHY:  Only <h3>, <p>, <a>, <blockquote> are allowed.

### ✗ WRONG — blockquote without <a> elements
HTML: <blockquote>The best code is reproducible code.</blockquote>
WHY:  Text in blockquotes must also be wrapped in <a data-t="..."> elements.

### ✗ WRONG — blockquote removes text from paragraph
HTML:
  <p><a data-t="320">Now I want to shift gears and talk about testing.</a></p>

  <blockquote><a data-t="335">The best Shiny app is one you're not afraid to change.</a></blockquote>
WHY:  The quoted sentence must also remain in a <p> in the prose flow.
      The blockquote duplicates it — it does not replace it.

### ✗ WRONG — heading at the very start of the document
HTML: <h3>Introduction</h3><p><a data-t="0">Hello everyone.</a></p>
WHY:  Do not open with a heading; start with a <p>.

### ✗ WRONG — heading casing
HTML: <h3>Setting Up The Environment</h3>
WHY:  Use sentence casing: <h3>Setting up the environment</h3>

### ✓ CORRECT — multi-cue sentence, single paragraph
VTT:
  00:01:30.000 --> 00:01:35.000
  Today I want to talk about

  00:01:35.000 --> 00:01:40.000
  reproducible research with Quarto.

  00:01:41.000 --> 00:01:46.000
  It has changed how I work.

HTML:
  <p><a data-t="90">Today I want to talk about</a> <a data-t="95">reproducible research with Quarto.</a> <a data-t="101">It has changed how I work.</a></p>

### ✓ CORRECT — paragraph break on topic change + blockquote (pull quote)
HTML:
  <p><a data-t="300">So that covers the basics of reactive programming.</a></p>

  <p><a data-t="320">Now I want to shift gears and talk about testing.</a> <a data-t="324">Testing Shiny apps used to be really hard.</a> <a data-t="328">But shinytest2 has changed that.</a> <a data-t="335">The best Shiny app is one you're not afraid to change, and tests give you that confidence.</a></p>

  <blockquote><a data-t="335">The best Shiny app is one you're not afraid to change, and tests give you that confidence.</a></blockquote>

  <p><a data-t="342">Let me show you a simple example.</a></p>

### ✓ CORRECT — gap-based paragraph break (8-second gap between cues)
HTML:
  <p><a data-t="305">And that's how you configure the layout.</a></p>

  <p><a data-t="318">Alright, let's move on to deployment.</a></p>

### ✓ CORRECT — section heading on clear topic shift
HTML:
  <p><a data-t="540">And that wraps up our overview of the data pipeline.</a></p>

  <h3>Building the Shiny dashboard</h3>

  <p><a data-t="558">Now let's actually build the app.</a> <a data-t="562">I'll start with a minimal ui definition.</a></p>
"""


# ---------------------------------------------------------------------------
# Helpers copied from transcribe.py
# ---------------------------------------------------------------------------


def parse_frontmatter(content: str) -> dict[str, Any]:
    lines = content.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}
    end_idx = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end_idx is None:
        return {}
    try:
        return yaml.safe_load("\n".join(lines[1:end_idx])) or {}
    except yaml.YAMLError:
        return {}


def parse_vtt_timestamp(ts: str) -> float:
    parts = ts.strip().split(":")
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])
    return int(parts[0]) * 60 + float(parts[1])


def format_vtt_timestamp(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}"


def parse_vtt(content: str) -> list[tuple[float, float, str]]:
    cues: list[tuple[float, float, str]] = []
    for block in re.split(r"\n{2,}", content.strip()):
        lines = block.strip().splitlines()
        arrow = next((i for i, line in enumerate(lines) if "-->" in line), None)
        if arrow is None:
            continue
        m = re.match(r"([\d:.]+)\s+-->\s+([\d:.]+)", lines[arrow])
        if not m:
            continue
        start = parse_vtt_timestamp(m.group(1))
        end = parse_vtt_timestamp(m.group(2))
        text = "\n".join(lines[arrow + 1 :]).strip()
        if text:
            cues.append((start, end, text))
    return cues


class RateLimiter:
    def __init__(self, min_interval: float = 1.0) -> None:
        self._lock = asyncio.Lock()
        self._last: float = 0.0
        self._interval = min_interval

    async def wait(self) -> None:
        async with self._lock:
            loop = asyncio.get_running_loop()
            elapsed = loop.time() - self._last
            if elapsed < self._interval:
                await asyncio.sleep(self._interval - elapsed)
            self._last = asyncio.get_running_loop().time()


# ---------------------------------------------------------------------------
# Phase 1 — Prompt helpers
# ---------------------------------------------------------------------------


def build_user_message(vtt_content: str, frontmatter: dict[str, Any]) -> str:
    title = frontmatter.get("title", "")
    description = (frontmatter.get("description") or "").strip()
    software = frontmatter.get("software") or []
    people = frontmatter.get("people") or []

    header_parts: list[str] = []
    if title:
        header_parts.append(f"Video title: {title}")
    if people:
        header_parts.append(f"People featured: {', '.join(str(p) for p in people)}")
    if software:
        header_parts.append(
            f"Technologies mentioned: {', '.join(str(s) for s in software)}"
        )
    if description:
        header_parts.append(f"Description: {description[:600]}")

    header = "\n".join(header_parts)
    return f"{header}\n\n---\n\n{vtt_content}" if header else vtt_content


# ---------------------------------------------------------------------------
# Phase 2 — Core script
# ---------------------------------------------------------------------------


def strip_markdown_fence(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-z]*\n?", "", text)
        text = re.sub(r"\n?```$", "", text.strip())
    return text.strip()


def validate_html(html: str) -> None:
    if not html.lstrip().startswith("<"):
        raise ValueError("Response does not start with '<' — not HTML")
    for bad in ("<html", "<body", "<head", "<div", "<span", "<h1", "<h2"):
        if bad in html:
            raise ValueError(f"Response contains disallowed element: {bad}")
    if "<p>" not in html and "<blockquote>" not in html:
        raise ValueError("Response contains no <p> or <blockquote> elements")


async def call_api(
    client: anthropic.AsyncAnthropic,
    user_message: str,
    model: str,
    max_tokens: int,
    rate_limiter: RateLimiter,
    name: str,
    system: str = PROMPT,
) -> str:
    for attempt in range(MAX_RETRIES):
        if attempt > 0:
            delay = BASE_BACKOFF * (2 ** (attempt - 1)) + random.uniform(0, 1)
            console.print(
                f"  [yellow]↻[/] {name}  retry {attempt + 1}/{MAX_RETRIES} in {delay:.1f}s"
            )
            await asyncio.sleep(delay)

        await rate_limiter.wait()
        try:
            response = await client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=0,
                system=system,
                messages=[{"role": "user", "content": user_message}],
            )
            return response.content[0].text
        except anthropic.RateLimitError:
            if attempt == MAX_RETRIES - 1:
                raise
        except anthropic.APIStatusError as e:
            if e.status_code < 500 or attempt == MAX_RETRIES - 1:
                raise

    raise RuntimeError("Exceeded max retries")


def resolve_video_dir(name_or_path: str, videos_dir: Path) -> Path:
    p = Path(name_or_path)
    if p.is_absolute() and p.is_dir():
        return p
    candidate = videos_dir / name_or_path
    if candidate.is_dir():
        return candidate
    matches = [
        d
        for d in videos_dir.iterdir()
        if d.is_dir() and d.name.startswith(name_or_path)
    ]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        listed = "\n  ".join(m.name for m in sorted(matches))
        raise ValueError(f"Ambiguous --video value, matches:\n  {listed}")
    raise ValueError(f"Video directory not found: {name_or_path}")


async def process_video_async(
    video_dir: Path,
    client: anthropic.AsyncAnthropic,
    semaphore: asyncio.Semaphore,
    rate_limiter: RateLimiter,
    progress: Progress,
    overall_task: TaskID,
    args: argparse.Namespace,
    people: dict[str, str],
    software: dict[str, str],
) -> str:
    async with semaphore:
        name = video_dir.name
        job_task = progress.add_task(f"[dim]{name}", total=None)
        try:
            html_file = video_dir / "transcription.txt"
            vtt_file = video_dir / "transcription.vtt"
            index_file = video_dir / "_index.md"

            if html_file.exists() and not args.force:
                return "skipped"

            frontmatter = (
                parse_frontmatter(index_file.read_text(encoding="utf-8"))
                if index_file.exists()
                else {}
            )

            if frontmatter.get("transcribe", True) is False:
                return "excluded"

            if not vtt_file.exists():
                return "no_vtt"

            vtt_content = vtt_file.read_text(encoding="utf-8")
            duration = (frontmatter.get("external") or {}).get("duration", 0)

            if duration > LONG_VIDEO_THRESHOLD_S:
                progress.update(job_task, description=f"[cyan]{name}  chunking")
                html = await format_chunked(
                    vtt_content,
                    frontmatter,
                    client,
                    rate_limiter,
                    args,
                    name,
                    progress,
                    job_task,
                )
            else:
                user_message = build_user_message(vtt_content, frontmatter)
                progress.update(job_task, description=f"[cyan]{name}  formatting")
                raw = await call_api(
                    client,
                    user_message,
                    args.model,
                    args.max_tokens,
                    rate_limiter,
                    name,
                )
                html = strip_markdown_fence(raw)

            validate_html(html)
            html = inject_links(html, people, software)
            html_file.write_text(html, encoding="utf-8")
            return "formatted"

        except Exception as e:
            console.print(f"  [red]✗[/] {name}: {e}")
            return "error"
        finally:
            progress.remove_task(job_task)
            progress.advance(overall_task)


# ---------------------------------------------------------------------------
# Phase 3 — Chunked processing
# ---------------------------------------------------------------------------


def _render_vtt(cues: list[tuple[float, float, str]]) -> str:
    lines = ["WEBVTT", ""]
    for start, end, text in cues:
        lines.append(f"{format_vtt_timestamp(start)} --> {format_vtt_timestamp(end)}")
        lines.append(text)
        lines.append("")
    return "\n".join(lines)


def split_vtt_into_chunks(
    vtt_content: str, chunk_duration: int
) -> list[tuple[str, int]]:
    cues = parse_vtt(vtt_content)
    chunks: list[tuple[str, int]] = []
    seg_start = 0.0
    seg_cues: list[tuple[float, float, str]] = []

    for start, end, text in cues:
        if seg_cues and (start - seg_start) >= chunk_duration:
            chunks.append((_render_vtt(seg_cues), int(seg_start)))
            seg_start = start
            seg_cues = []
        seg_cues.append((start, end, text))

    if seg_cues:
        chunks.append((_render_vtt(seg_cues), int(seg_start)))

    return chunks


def build_chunk_system(segment_index: int, total_segments: int) -> str:
    return (
        PROMPT.rstrip()
        + "\n\n## Segment context\n"
        + f"This is segment {segment_index + 1} of {total_segments}.\n"
        + "Start each paragraph cleanly — do not begin mid-sentence.\n"
        + "End each paragraph cleanly — do not leave a sentence dangling.\n"
    )


async def format_chunked(
    vtt_content: str,
    frontmatter: dict[str, Any],
    client: anthropic.AsyncAnthropic,
    rate_limiter: RateLimiter,
    args: argparse.Namespace,
    name: str,
    progress: Progress,
    job_task: TaskID,
) -> str:
    chunks = split_vtt_into_chunks(vtt_content, args.chunk_duration)
    total = len(chunks)
    html_parts: list[str] = []

    for i, (chunk_vtt, _seg_start) in enumerate(chunks):
        progress.update(job_task, description=f"[cyan]{name}  chunk {i + 1}/{total}")
        user_message = build_user_message(chunk_vtt, frontmatter)
        chunk_system = build_chunk_system(i, total)
        raw = await call_api(
            client,
            user_message,
            args.model,
            args.max_tokens,
            rate_limiter,
            name,
            system=chunk_system,
        )
        html_parts.append(strip_markdown_fence(raw))

    return "\n<!-- segment separator -->\n".join(html_parts)


# ---------------------------------------------------------------------------
# Phase 4 — Entity linking
# ---------------------------------------------------------------------------


def build_entity_dicts(
    repo_root: Path,
) -> tuple[dict[str, str], dict[str, str]]:
    ignore_file = repo_root / "data" / "software-match-ignore.toml"
    ignored: set[str] = set()
    if ignore_file.exists():
        data = tomllib.loads(ignore_file.read_text(encoding="utf-8"))
        ignored = set(data.get("names", []))

    people: dict[str, str] = {}
    people_dir = repo_root / "content" / "people"
    if people_dir.exists():
        for d in people_dir.iterdir():
            if not d.is_dir():
                continue
            index = d / "_index.md"
            if not index.exists():
                continue
            fm = parse_frontmatter(index.read_text(encoding="utf-8"))
            title = (fm.get("title") or "").strip()
            if title:
                people[title] = f"/people/{d.name}/"

    software: dict[str, str] = {}
    software_dir = repo_root / "content" / "software"
    if software_dir.exists():
        for d in software_dir.iterdir():
            if not d.is_dir() or d.name in ignored:
                continue
            index = d / "_index.md"
            if not index.exists():
                continue
            fm = parse_frontmatter(index.read_text(encoding="utf-8"))
            override = (fm.get("override") or {}).get("title")
            title = (override or fm.get("title") or "").strip()
            if title:
                software[title] = f"/software/{d.name}/"

    return people, software


def _inject_into_text(
    text: str,
    entities: list[tuple[str, str, bool]],
    linked: set[str],
) -> str:
    for name, url, is_software in entities:
        if name in linked:
            continue
        flags = re.IGNORECASE if is_software else 0
        pattern = r"\b" + re.escape(name) + r"\b"
        if re.search(pattern, text, flags=flags):
            linked.add(name)
            text = re.sub(
                pattern,
                lambda m, u=url: f'<a href="{u}">{m.group(0)}</a>',
                text,
                count=1,
                flags=flags,
            )
    return text


def _inject_into_anchor(
    content: str,
    attrs: str,
    entities: list[tuple[str, str, bool]],
    linked: set[str],
) -> str:
    for name, url, is_software in entities:
        if name in linked:
            continue
        flags = re.IGNORECASE if is_software else 0
        pattern = r"\b" + re.escape(name) + r"\b"
        mo = re.search(pattern, content, flags=flags)
        if mo:
            linked.add(name)
            before = content[: mo.start()]
            match_text = mo.group(0)
            after = content[mo.end() :]
            pieces: list[str] = []
            if before:
                pieces.append(f"<a{attrs}>{before}</a>")
            pieces.append(f'<a href="{url}">{match_text}</a>')
            if after:
                pieces.append(f"<a{attrs}>{after}</a>")
            return "".join(pieces)
    return f"<a{attrs}>{content}</a>"


def inject_links(
    html: str,
    people: dict[str, str],
    software: dict[str, str],
) -> str:
    linked: set[str] = set()

    entities: list[tuple[str, str, bool]] = sorted(
        [(name, url, False) for name, url in people.items()]
        + [(name, url, True) for name, url in software.items()],
        key=lambda x: -len(x[0]),
    )

    parts = re.split(r"(<a\b[^>]*>.*?</a>)", html, flags=re.DOTALL)

    result: list[str] = []
    for part in parts:
        m = re.match(r"<a(\b[^>]*)>(.*?)</a>", part, flags=re.DOTALL)
        if m:
            attrs, content = m.group(1), m.group(2)
            result.append(_inject_into_anchor(content, attrs, entities, linked))
        else:
            result.append(_inject_into_text(part, entities, linked))

    return "".join(result)


# ---------------------------------------------------------------------------
# Entry points
# ---------------------------------------------------------------------------


async def main_async(args: argparse.Namespace) -> None:
    console.print("\n[bold blue]Transcription Formatter[/]\n")

    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        console.print("[bold red]Error:[/] ANTHROPIC_API_KEY not set in .env")
        sys.exit(1)

    client = anthropic.AsyncAnthropic(api_key=api_key)
    repo_root = Path(__file__).parent.parent
    videos_dir = repo_root / "content" / "resources" / "videos"

    if not videos_dir.exists():
        console.print(f"[bold red]Error:[/] Videos directory not found: {videos_dir}")
        sys.exit(1)

    people, software = build_entity_dicts(repo_root)
    console.print(
        f"[dim]Loaded {len(people)} people and {len(software)} software entries[/]"
    )

    if args.video:
        dirs = [resolve_video_dir(args.video, videos_dir)]
    else:
        dirs = sorted(d for d in videos_dir.iterdir() if d.is_dir())

    console.print(
        f"[dim]Found {len(dirs)} director(ies) to process (--jobs {args.jobs})[/]\n"
    )

    semaphore = asyncio.Semaphore(args.jobs)
    rate_limiter = RateLimiter(min_interval=1.0)

    with Progress(
        SpinnerColumn(),
        TextColumn("{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        overall_task = progress.add_task("[bold cyan]Formatting", total=len(dirs))
        results: list[str] = await asyncio.gather(
            *[
                process_video_async(
                    d,
                    client,
                    semaphore,
                    rate_limiter,
                    progress,
                    overall_task,
                    args,
                    people,
                    software,
                )
                for d in dirs
            ]
        )

    formatted = results.count("formatted")
    skipped = results.count("skipped")
    excluded = results.count("excluded")
    no_vtt = results.count("no_vtt")
    errors = results.count("error")

    console.print("\n[bold]Summary:[/]")
    console.print(f"  [green]✓[/] Formatted: {formatted}")
    console.print(f"  [dim]○[/] Skipped:   {skipped}")
    console.print(f"  [dim]○[/] Excluded:  {excluded}")
    console.print(f"  [dim]○[/] No VTT:    {no_vtt}")
    if errors:
        console.print(f"  [red]✗[/] Errors:    {errors}")
    console.print("\n[bold green]✓ Done![/]\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Format VTT transcriptions into HTML using the Anthropic API"
    )
    parser.add_argument(
        "--jobs",
        type=int,
        default=5,
        metavar="N",
        help="parallel formatting jobs (default: 5)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="overwrite existing transcription.txt files",
    )
    parser.add_argument(
        "--video",
        metavar="NAME",
        help="process only this video directory (name or path)",
    )
    parser.add_argument(
        "--model", default="claude-sonnet-4-6", metavar="ID", help="Anthropic model ID"
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=16384,
        metavar="N",
        help="max output tokens per API call (default: 16384)",
    )
    parser.add_argument(
        "--chunk-duration",
        type=int,
        default=CHUNK_DURATION_S,
        metavar="SECS",
        help=f"VTT seconds per chunk for long videos (default: {CHUNK_DURATION_S})",
    )
    args = parser.parse_args()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
