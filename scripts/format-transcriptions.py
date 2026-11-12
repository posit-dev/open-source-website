#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "anthropic>=0.40.0",
#   "python-dotenv>=1.0.0",
# ]
# ///

"""
Format VTT transcription files into HTML fragments using the Anthropic API.

For each subdirectory under content/resources/videos/, newest first:
- Skip if transcription.txt already exists (unless --force).
- Skip if _index.md frontmatter has transcribe: false.
- Skip if transcription.vtt does not exist.
- For long videos (> 90 min), split the VTT into chunks and process each
  segment separately, then concatenate the results.
- Repair the data-t timestamps: the model copies the cue text verbatim but
  often gets the seconds wrong, so each <a> is matched back to its VTT cue.
- Validate the HTML: only <h3>, <p>, <a data-t>, and <blockquote>; every
  data-t within the video; at least 90% of the spoken words present; and a
  response that hit the max_tokens limit is rejected. Invalid output is
  never written.
- Inject <a href="..."> links for known people and software.

Requires ANTHROPIC_API_KEY in the environment or .env. The model can be set
with --model or $TRANSCRIPT_MODEL.

Exit codes: 0 = success, 1 = fatal, 2 = partial (some videos failed).
"""

from __future__ import annotations

import argparse
import asyncio
import html as html_lib
import logging
import os
import re
import sys
import time
import tomllib
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Awaitable, Callable

sys.path.insert(0, str(Path(__file__).resolve().parent))

import videolib  # noqa: E402

log = logging.getLogger("format-transcriptions")

DEFAULT_MODEL = "claude-sonnet-4-6"
# Long transcripts hit the output token limit or get condensed by the model:
# before chunking at 20 minutes, 84-93% of the 45-90 minute videos lost more
# than 10% of their words. 15-minute chunks behave like short videos.
CHUNK_DURATION_S = 900  # 15 min per chunk (default)
LONG_VIDEO_THRESHOLD_S = 1_200  # 20 min — chunk automatically

ALLOWED_TAGS = {"h3", "p", "a", "blockquote"}
# Share of the VTT's words that must appear in the HTML (outside pull quotes).
MIN_COVERAGE = 0.90
# data-t values beyond the end of the video: a warning beyond the slack, an
# error beyond max(TOLERANCE_S, TOLERANCE_RATIO * duration). The model's
# timestamp arithmetic is often off by tens of seconds (median 44 s in the
# existing transcripts), which is annoying but not worth throwing away.
DATA_T_SLACK_S = 5
DATA_T_TOLERANCE_S = 60
DATA_T_TOLERANCE_RATIO = 0.10

# Estimated USD per million (input, output) tokens, matched by model prefix.
PRICES_PER_MTOK = {
    "claude-sonnet": (3.0, 15.0),
    "claude-haiku": (1.0, 5.0),
}

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
# Prompt helpers
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
        header_parts.append(f"Technologies mentioned: {', '.join(str(s) for s in software)}")
    if description:
        header_parts.append(f"Description: {description[:600]}")

    header = "\n".join(header_parts)
    return f"{header}\n\n---\n\n{vtt_content}" if header else vtt_content


def build_chunk_system(segment_index: int, total_segments: int) -> str:
    return (
        PROMPT.rstrip()
        + "\n\n## Segment context\n"
        + f"This is segment {segment_index + 1} of {total_segments}.\n"
        + "Start each paragraph cleanly — do not begin mid-sentence.\n"
        + "End each paragraph cleanly — do not leave a sentence dangling.\n"
    )


def split_vtt_into_chunks(vtt_content: str, chunk_duration: int) -> list[tuple[str, int]]:
    cues = videolib.parse_vtt(vtt_content)
    chunks: list[tuple[str, int]] = []
    seg_start = 0.0
    seg_cues: list[videolib.Cue] = []

    for start, end, text in cues:
        if seg_cues and (start - seg_start) >= chunk_duration:
            chunks.append((videolib.render_vtt(seg_cues), int(seg_start)))
            seg_start = start
            seg_cues = []
        seg_cues.append((start, end, text))

    if seg_cues:
        chunks.append((videolib.render_vtt(seg_cues), int(seg_start)))

    return chunks


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


class FormatError(Exception):
    def __init__(self, reason: str, detail: str):
        super().__init__(detail)
        self.reason = reason


def strip_markdown_fence(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-z]*\n?", "", text)
        text = re.sub(r"\n?```$", "", text.strip())
    return text.strip()


WORD_RE = re.compile(r"[\w']+")


def word_counts(text: str) -> Counter:
    return Counter(w.lower().strip("'") for w in WORD_RE.findall(text))


def html_to_text(html: str, *, drop_blockquotes: bool = True) -> str:
    if drop_blockquotes:
        html = re.sub(r"<blockquote\b.*?</blockquote>", " ", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<h3\b.*?</h3>", " ", html, flags=re.DOTALL | re.IGNORECASE)
    return html_lib.unescape(re.sub(r"<[^>]+>", " ", html))


def coverage(cues: list[videolib.Cue], html: str) -> float:
    """Share of the spoken words (with multiplicity) found in the HTML prose."""
    spoken = word_counts(" ".join(text for _, _, text in cues))
    total = sum(spoken.values())
    if not total:
        return 1.0
    written = word_counts(html_to_text(html))
    return sum(min(n, written[w]) for w, n in spoken.items()) / total


def validate_html(html: str, cues: list[videolib.Cue], duration: int) -> dict[str, Any]:
    """Raise FormatError when the model output can't be used; return metrics."""
    if not html.lstrip().startswith("<"):
        raise FormatError("not_html", f"Response does not start with '<': {html[:80]!r}")

    tags = {t.lower() for t in re.findall(r"</?\s*([a-zA-Z][a-zA-Z0-9]*)", html)}
    disallowed = sorted(tags - ALLOWED_TAGS)
    if disallowed:
        raise FormatError("disallowed_tag", f"Disallowed elements: {', '.join(disallowed)}")

    for m in re.finditer(r"<(h3|p|blockquote)(\s[^>]*)?>", html, flags=re.IGNORECASE):
        if m.group(2) and m.group(2).strip():
            raise FormatError("disallowed_attribute", f"Attributes on <{m.group(1)}>: {m.group(2).strip()}")

    end = max([duration] + [end for _, end, _ in cues])
    max_t = 0
    anchors = 0
    for m in re.finditer(r"<a(\s[^>]*)?>", html, flags=re.IGNORECASE):
        attrs = (m.group(1) or "").strip()
        am = re.fullmatch(r'data-t="(\d+)"', attrs)
        if not am:
            raise FormatError("disallowed_attribute", f"Bad <a> attributes: {attrs!r}")
        max_t = max(max_t, int(am.group(1)))
        anchors += 1

    warnings: list[str] = []
    overshoot = max_t - end
    if overshoot > max(DATA_T_TOLERANCE_S, DATA_T_TOLERANCE_RATIO * end):
        raise FormatError("bad_timestamp", f'data-t="{max_t}" is {overshoot:.0f}s beyond the end of the video ({end:.0f}s)')
    if overshoot > DATA_T_SLACK_S:
        warnings.append(f"timestamp_overshoot: data-t=\"{max_t}\" is {overshoot:.0f}s beyond the end of the video")

    if "<p>" not in html and "<blockquote>" not in html:
        raise FormatError("no_paragraphs", "Response contains no <p> or <blockquote> elements")

    cov = coverage(cues, html)
    if cov < MIN_COVERAGE:
        raise FormatError("low_coverage", f"Only {cov:.1%} of the spoken words are in the HTML (minimum {MIN_COVERAGE:.0%})")
    return {"coverage": round(cov, 4), "anchors": anchors, "warnings": warnings or None}


# ---------------------------------------------------------------------------
# Timestamp repair
# ---------------------------------------------------------------------------

# How far ahead (in words) to look for the next anchor's text in the VTT.
REPAIR_WINDOW_WORDS = 800
# Words of an anchor used to find it in the VTT.
REPAIR_KEY_WORDS = 4

ANCHOR_RE = re.compile(r'<a data-t="(\d+)">(.*?)</a>', flags=re.DOTALL)
BLOCKQUOTE_RE = re.compile(r"(<blockquote\b.*?</blockquote>)", flags=re.DOTALL | re.IGNORECASE)


def _norm_words(text: str) -> list[str]:
    return [w.lower().strip("'") for w in WORD_RE.findall(html_lib.unescape(re.sub(r"<[^>]+>", " ", text)))]


def repair_timestamps(html: str, cues: list[videolib.Cue]) -> tuple[str, dict[str, int]]:
    """Set every ``data-t`` to the start of the VTT cue its text comes from.

    The model copies the cue text verbatim but often gets the seconds wrong
    (in the existing transcripts typically by 5-20 s, sometimes by minutes).
    Walk the anchors in document order and find each one's first words in
    the VTT, searching forward from the previous match. Anchors that can't
    be found keep the model's value. Pull quotes reuse the value of the
    matching prose anchor. Consecutive anchors with the same original value
    (split by inject_links) stay together.
    """
    words: list[tuple[str, int]] = []  # (word, cue start in whole seconds)
    for start, _end, text in cues:
        words.extend((w, int(start)) for w in _norm_words(text))
    vocab = [w for w, _ in words]

    def find(key: list[str], pos: int) -> int | None:
        limit = min(len(vocab) - len(key) + 1, pos + REPAIR_WINDOW_WORDS)
        for i in range(pos, max(pos, limit)):
            if vocab[i] == key[0] and vocab[i : i + len(key)] == key:
                return i
        return None

    stats = {"anchors": 0, "matched": 0, "changed": 0, "unmatched": 0}
    by_text: dict[str, int] = {}
    pos = 0
    prev: tuple[int, int] | None = None  # (original, repaired)

    def repair_prose(m: re.Match) -> str:
        nonlocal pos, prev
        original, inner = int(m.group(1)), m.group(2)
        stats["anchors"] += 1
        ws = _norm_words(inner)
        new = original
        found = None
        # Skip a leading word or two in case the model corrected it
        # (e.g. "Korto" -> "Quarto").
        for skip in (0, 1, 2):
            key = ws[skip : skip + REPAIR_KEY_WORDS]
            if not key:
                break
            i = find(key, pos)
            if i is not None:
                pos = i + len(ws) - skip
                found = words[i][1]
                break
        if found is not None:
            stats["matched"] += 1
            new = found
        else:
            stats["unmatched"] += 1
            if prev is not None and prev[0] == original:
                new = prev[1]  # a piece of an anchor that inject_links split
            elif words:
                # Keep the model's value, but not beyond the last cue.
                # (Clamping to the neighbours was measured to make things
                # worse: one wrong match then drags the next anchors along.)
                new = min(original, words[-1][1])
        prev = (original, new)
        if new != original:
            stats["changed"] += 1
        by_text.setdefault(" ".join(ws), new)
        return f'<a data-t="{new}">{inner}</a>'

    def repair_quote(m: re.Match) -> str:
        new = by_text.get(" ".join(_norm_words(m.group(2))), int(m.group(1)))
        return f'<a data-t="{new}">{m.group(2)}</a>'

    parts = BLOCKQUOTE_RE.split(html)
    parts = [p if i % 2 else ANCHOR_RE.sub(repair_prose, p) for i, p in enumerate(parts)]
    parts = [ANCHOR_RE.sub(repair_quote, p) if i % 2 else p for i, p in enumerate(parts)]
    return "".join(parts), stats


def unlink_entities(html: str) -> str:
    """Undo inject_links, so a published transcript can be validated again."""
    return re.sub(r'<a href="[^"]*">(.*?)</a>', r"\1", html, flags=re.DOTALL)


def check_existing(video_dir: Path) -> tuple[bool, str | None, str | None]:
    """Validate a published transcription.txt: ``(ok, reason, detail)``."""
    fm = videolib.read_frontmatter(video_dir / "_index.md")
    duration = int((fm.get("external") or {}).get("duration") or 0)
    cues = videolib.parse_vtt((video_dir / "transcription.vtt").read_text(encoding="utf-8"))
    html = unlink_entities((video_dir / "transcription.txt").read_text(encoding="utf-8"))
    try:
        validate_html(html, cues, duration)
    except FormatError as e:
        return False, e.reason, str(e)
    return True, None, None


# ---------------------------------------------------------------------------
# API
# ---------------------------------------------------------------------------


def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float | None:
    for prefix, (price_in, price_out) in PRICES_PER_MTOK.items():
        if model.startswith(prefix):
            return round((input_tokens * price_in + output_tokens * price_out) / 1_000_000, 4)
    return None


async def call_api(
    client: Any,
    user_message: str,
    *,
    model: str,
    max_tokens: int,
    rate_limiter: videolib.RateLimiter,
    label: str,
    system: str = PROMPT,
    sleep: Callable[[float], Awaitable[Any]] = asyncio.sleep,
) -> tuple[str, dict[str, Any]]:
    """Return ``(html, usage)``; raise FormatError if the output was cut off."""

    async def call():
        await rate_limiter.wait()
        return await client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user_message}],
        )

    t0 = time.monotonic()
    response = await videolib.retry_async(call, label=label, logger=log, sleep=sleep)
    usage = {
        "input_tokens": getattr(response.usage, "input_tokens", 0),
        "output_tokens": getattr(response.usage, "output_tokens", 0),
        "stop_reason": response.stop_reason,
        "request_id": getattr(response, "_request_id", None),
        "latency_s": round(time.monotonic() - t0, 1),
    }
    log.info(
        "%s: %s responded in %.1fs (%d in / %d out tokens, stop_reason=%s, request_id=%s)",
        label,
        model,
        usage["latency_s"],
        usage["input_tokens"],
        usage["output_tokens"],
        usage["stop_reason"],
        usage["request_id"],
    )
    if response.stop_reason == "max_tokens":
        raise FormatError(
            "truncated",
            f"Response hit max_tokens={max_tokens} after {usage['output_tokens']} tokens "
            f"(request_id={usage['request_id']}); try a smaller --chunk-duration",
        )
    text = "".join(getattr(block, "text", "") for block in response.content)
    return strip_markdown_fence(text), usage


# ---------------------------------------------------------------------------
# Entity linking
# ---------------------------------------------------------------------------


def build_entity_dicts(repo_root: Path) -> tuple[dict[str, str], dict[str, str]]:
    ignore_file = repo_root / "data" / "software-match-ignore.toml"
    ignored: set[str] = set()
    if ignore_file.exists():
        data = tomllib.loads(ignore_file.read_text(encoding="utf-8"))
        ignored = set(data.get("names", []))

    people: dict[str, str] = {}
    people_dir = repo_root / "content" / "people"
    if people_dir.exists():
        for d in sorted(people_dir.iterdir()):
            if not d.is_dir():
                continue
            fm = videolib.read_frontmatter(d / "_index.md")
            title = (fm.get("title") or "").strip()
            if title:
                people[title] = f"/people/{d.name}/"

    software: dict[str, str] = {}
    software_dir = repo_root / "content" / "software"
    if software_dir.exists():
        for d in sorted(software_dir.iterdir()):
            if not d.is_dir() or d.name in ignored:
                continue
            fm = videolib.read_frontmatter(d / "_index.md")
            override = (fm.get("override") or {}).get("title")
            title = (override or fm.get("title") or "").strip()
            if title:
                software[title] = f"/software/{d.name}/"

    return people, software


def _inject_into_text(text: str, entities: list[tuple[str, str, bool]], linked: set[str]) -> str:
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
    content: str, attrs: str, entities: list[tuple[str, str, bool]], linked: set[str]
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


def inject_links(html: str, people: dict[str, str], software: dict[str, str]) -> str:
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
# Per-video processing
# ---------------------------------------------------------------------------


@dataclass
class Context:
    client: Any
    args: argparse.Namespace
    semaphore: asyncio.Semaphore
    rate_limiter: videolib.RateLimiter
    people: dict[str, str]
    software: dict[str, str]
    sleep: Callable[[float], Awaitable[Any]]


def select_videos(
    dirs: list[Path],
    summary: videolib.RunSummary,
    *,
    force: bool,
    limit: int | None,
    reformat_invalid: bool = False,
) -> list[Path]:
    selected: list[Path] = []
    deferred: list[str] = []
    for d in dirs:
        fm = videolib.read_frontmatter(d / "_index.md")
        if fm.get("transcribe", True) is False:
            summary.tally("excluded")
            continue
        if not (d / "transcription.vtt").exists():
            summary.tally("no_vtt")
            continue
        if (d / "transcription.txt").exists() and not force:
            if not reformat_invalid:
                summary.tally("already_formatted")
                continue
            ok, reason, _ = check_existing(d)
            if ok:
                summary.tally("already_formatted")
                continue
            log.info("%s: existing transcript is invalid (%s); reformatting", d.name, reason)
        if limit is not None and len(selected) >= limit:
            deferred.append(d.name)
            continue
        selected.append(d)
    if deferred:
        summary.tally("deferred", len(deferred))
        summary.extra["deferred"] = deferred
        log.info("Deferred %d videos to a later run (--limit)", len(deferred))
    return selected


async def process_video(video_dir: Path, ctx: Context) -> dict[str, Any]:
    async with ctx.semaphore:
        args = ctx.args
        fm = videolib.read_frontmatter(video_dir / "_index.md")
        external = fm.get("external") or {}
        video_id = videolib.youtube_id(external.get("url"))
        label = f"{video_dir.name} ({video_id})"
        duration = int(external.get("duration") or 0)
        item: dict[str, Any] = {"slug": video_dir.name, "video_id": video_id, "duration_s": duration, "model": args.model}
        html: str | None = None
        try:
            vtt_content = (video_dir / "transcription.vtt").read_text(encoding="utf-8")
            cues = videolib.parse_vtt(vtt_content)
            if not cues:
                raise FormatError("empty_vtt", "transcription.vtt has no cues")

            if duration > LONG_VIDEO_THRESHOLD_S:
                chunks = split_vtt_into_chunks(vtt_content, args.chunk_duration)
            else:
                chunks = [(vtt_content, 0)]
            item["chunks"] = len(chunks)
            log.info("%s: formatting %d cues in %d chunk(s)", label, len(cues), len(chunks))

            # Chunks are independent, so request them concurrently (the rate
            # limiter still spaces out the requests).
            results = await asyncio.gather(
                *(
                    call_api(
                        ctx.client,
                        build_user_message(chunk_vtt, fm),
                        model=args.model,
                        max_tokens=args.max_tokens,
                        rate_limiter=ctx.rate_limiter,
                        label=f"{label} chunk {i + 1}/{len(chunks)}" if len(chunks) > 1 else label,
                        system=build_chunk_system(i, len(chunks)) if len(chunks) > 1 else PROMPT,
                        sleep=ctx.sleep,
                    )
                    for i, (chunk_vtt, _seg_start) in enumerate(chunks)
                )
            )
            parts = [html_part for html_part, _ in results]
            usages = [usage for _, usage in results]
            html = "\n<!-- segment separator -->\n".join(parts)
            if len(chunks) > 1:
                # Which chunk lost words, if any: useful when coverage is low.
                item["chunk_coverage"] = [
                    round(coverage(videolib.parse_vtt(chunk_vtt), part), 3)
                    for (chunk_vtt, _), part in zip(chunks, parts)
                ]
                log.info("%s: coverage per chunk: %s", label, ", ".join(f"{c:.1%}" for c in item["chunk_coverage"]))

            item["input_tokens"] = sum(u["input_tokens"] for u in usages)
            item["output_tokens"] = sum(u["output_tokens"] for u in usages)
            item["request_ids"] = [u["request_id"] for u in usages if u["request_id"]] or None
            item["estimated_cost_usd"] = estimate_cost(args.model, item["input_tokens"], item["output_tokens"])

            html, repair = repair_timestamps(html, cues)
            item["timestamps_repaired"] = repair["changed"]
            item["timestamps_unmatched"] = repair["unmatched"]
            log.info(
                "%s: repaired %d of %d timestamps (%d anchors not found in the VTT)",
                label,
                repair["changed"],
                repair["anchors"],
                repair["unmatched"],
            )
            metrics = validate_html(html, cues, duration)
            item.update(metrics)
            for w in metrics["warnings"] or []:
                log.warning("%s: %s", label, w)
            html = inject_links(html, ctx.people, ctx.software)
            videolib.atomic_write_text(video_dir / "transcription.txt", html)
        except FormatError as e:
            log.error("%s: %s: %s", label, e.reason, e)
            if args.rejected_dir and html is not None:
                args.rejected_dir.mkdir(parents=True, exist_ok=True)
                rejected = args.rejected_dir / f"{video_dir.name}.html"
                videolib.atomic_write_text(rejected, html)
                item["rejected_output"] = str(rejected)
                log.info("%s: saved the rejected output to %s", label, rejected)
            return {**item, "status": "error", "reason": e.reason, "detail": str(e)}
        except Exception as e:  # noqa: BLE001 - every failure goes in the summary
            log.exception("%s: formatting failed", label)
            return {**item, "status": "error", "reason": "api_error", "detail": videolib.describe_api_error(e)}

        log.info(
            "%s: wrote transcription.txt (%d anchors, %.1f%% coverage%s)",
            label,
            item["anchors"],
            item["coverage"] * 100,
            f", ~${item['estimated_cost_usd']:.3f}" if item["estimated_cost_usd"] is not None else "",
        )
        return {**item, "status": "formatted"}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def run_check_existing(dirs: list[Path], summary: videolib.RunSummary) -> None:
    """Report published transcripts that fail validation (no API calls)."""
    for d in dirs:
        if not ((d / "transcription.txt").exists() and (d / "transcription.vtt").exists()):
            continue
        ok, reason, detail = check_existing(d)
        if ok:
            summary.tally("valid")
        else:
            summary.add("invalid", slug=d.name, reason=reason, detail=detail)
            log.warning("Invalid: %s: %s: %s", d.name, reason, detail)
    invalid = summary.by_status("invalid")
    reasons: dict[str, int] = {}
    for i in invalid:
        reasons[i["reason"]] = reasons.get(i["reason"], 0) + 1
    summary.extra["invalid_by_reason"] = reasons
    log.info(
        "%d of %d transcripts are invalid %s; reformat them with --reformat-invalid",
        len(invalid),
        len(invalid) + summary.tallies.get("valid", 0),
        reasons,
    )


def run_repair_timestamps(dirs: list[Path], summary: videolib.RunSummary, *, dry_run: bool) -> None:
    """Fix the data-t values of published transcripts (no API calls)."""
    for d in dirs:
        txt, vtt = d / "transcription.txt", d / "transcription.vtt"
        if not (txt.exists() and vtt.exists()):
            continue
        cues = videolib.parse_vtt(vtt.read_text(encoding="utf-8"))
        if not cues:
            summary.tally("no_cues")
            continue
        html = txt.read_text(encoding="utf-8")
        repaired, stats = repair_timestamps(html, cues)
        if repaired == html:
            summary.tally("timestamps_ok")
            continue
        if not dry_run:
            videolib.atomic_write_text(txt, repaired)
        summary.add("timestamps_repaired", slug=d.name, **stats)
        log.info(
            "%s: %s %d of %d timestamps (%d anchors not found in the VTT)",
            d.name,
            "would repair" if dry_run else "repaired",
            stats["changed"],
            stats["anchors"],
            stats["unmatched"],
        )


def build_client(project_root: Path) -> Any:
    import anthropic
    from dotenv import load_dotenv

    load_dotenv(project_root / ".env")
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY not set in .env or environment")
    return anthropic.AsyncAnthropic(api_key=api_key, max_retries=0)  # we retry ourselves, with logging


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Format VTT transcriptions into HTML using the Anthropic API")
    parser.add_argument("--jobs", type=int, default=5, metavar="N", help="parallel formatting jobs (default: 5)")
    parser.add_argument("--force", action="store_true", help="overwrite existing transcription.txt files")
    parser.add_argument("--video", metavar="NAME", help="process only this video directory (name, prefix, or path)")
    parser.add_argument("--limit", type=int, metavar="N", help="format at most N videos (newest first)")
    parser.add_argument(
        "--model",
        default=os.getenv("TRANSCRIPT_MODEL") or DEFAULT_MODEL,
        metavar="ID",
        help=f"Anthropic model ID (default: $TRANSCRIPT_MODEL or {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--max-tokens", type=int, default=16384, metavar="N", help="max output tokens per API call (default: 16384)"
    )
    parser.add_argument(
        "--chunk-duration",
        type=int,
        default=CHUNK_DURATION_S,
        metavar="SECS",
        help=f"VTT seconds per chunk for long videos (default: {CHUNK_DURATION_S})",
    )
    parser.add_argument(
        "--reformat-invalid",
        action="store_true",
        help="also reformat existing transcripts that fail validation (see --check-existing)",
    )
    parser.add_argument(
        "--check-existing",
        action="store_true",
        help="only validate existing transcription.txt files and report the invalid ones (no API calls)",
    )
    parser.add_argument(
        "--repair-timestamps",
        action="store_true",
        help="only fix the data-t values of existing transcription.txt files from their VTT (no API calls)",
    )
    parser.add_argument(
        "--rejected-dir",
        type=Path,
        metavar="DIR",
        help="save model output that fails validation to DIR/<slug>.html, for debugging",
    )
    parser.add_argument("--dry-run", action="store_true", help="list what would be formatted")
    videolib.add_common_args(parser)
    return parser.parse_args(argv)


def main(
    argv: list[str] | None = None,
    client: Any = None,
    sleep: Callable[[float], Awaitable[Any]] = asyncio.sleep,
    min_request_interval: float = 1.0,
) -> int:
    args = parse_args(argv)
    videolib.setup_logging("format-transcriptions", args.verbose)
    summary = videolib.RunSummary("format-transcriptions")
    summary.extra.update(model=args.model, dry_run=args.dry_run, limit=args.limit)
    videos_dir = args.project_root / "content" / "resources" / "videos"

    def body() -> None:
        nonlocal client
        summary.environment = videolib.log_environment(log, packages=["anthropic"])
        if not videos_dir.exists():
            summary.fatal = f"Videos directory not found: {videos_dir}"
            return
        people, software = build_entity_dicts(args.project_root)
        log.info("Model: %s; loaded %d people and %d software entries for linking", args.model, len(people), len(software))

        dirs = [videolib.resolve_video_dir(args.video, videos_dir)] if args.video else videolib.video_dirs(videos_dir)
        if args.check_existing:
            run_check_existing(dirs, summary)
            return
        if args.repair_timestamps:
            run_repair_timestamps(dirs, summary, dry_run=args.dry_run)
            return
        selected = select_videos(
            dirs, summary, force=args.force, limit=args.limit, reformat_invalid=args.reformat_invalid
        )
        log.info("Selected %d of %d video directories (--jobs %d)", len(selected), len(dirs), args.jobs)
        if args.dry_run:
            for d in selected:
                log.info("Would format %s", d.name)
                summary.add("would_format", slug=d.name)
            return
        if not selected:
            return
        if client is None:
            client = build_client(args.project_root)

        ctx = Context(
            client=client,
            args=args,
            semaphore=asyncio.Semaphore(args.jobs),
            rate_limiter=videolib.RateLimiter(min_interval=min_request_interval),
            people=people,
            software=software,
            sleep=sleep,
        )

        async def go() -> list[dict[str, Any]]:
            return await asyncio.gather(*(process_video(d, ctx) for d in selected))

        for result in asyncio.run(go()):
            summary.add(result.pop("status"), **result)

        formatted = summary.by_status("formatted", "error")
        costs = [i.get("estimated_cost_usd") for i in formatted if i.get("estimated_cost_usd") is not None]
        summary.extra["estimated_cost_usd"] = round(sum(costs), 3)
        summary.extra["input_tokens"] = sum(i.get("input_tokens", 0) for i in formatted)
        summary.extra["output_tokens"] = sum(i.get("output_tokens", 0) for i in formatted)
        log.info(
            "Formatted %d videos (%d in / %d out tokens, ~$%.2f)",
            len(summary.by_status("formatted")),
            summary.extra["input_tokens"],
            summary.extra["output_tokens"],
            summary.extra["estimated_cost_usd"],
        )

    return videolib.run_main(summary, log, args.summary_json, body)


if __name__ == "__main__":
    sys.exit(main())
