#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "openai>=2.0.0",
#   "python-dotenv>=1.0.0",
#   "yt-dlp>=2025.0",
# ]
# ///

"""
Download audio from YouTube and transcribe it with OpenAI Whisper.

Processes video directories under content/resources/videos/, newest first,
that don't have a transcription.vtt yet. Skips videos with
`transcribe: false` in their frontmatter and videos without a duration
(live streams and premieres that haven't happened yet).

For each video:
- Download the audio with yt-dlp into a temporary directory (an audio.*
  file already in the video directory is used instead, and deleted after a
  successful transcription).
- If the audio exceeds the 25 MB API limit, split it at silences, transcribe
  each chunk, and merge the VTT output with corrected timestamps.
- Check the result (at least one cue; a warning if it ends well before the
  video does) and write transcription.vtt.

YouTube may block downloads from datacenter IPs (such as GitHub Actions
runners). Download errors are classified (bot_check, po_token, http_403, ...)
and logged with yt-dlp's full output. After three blocked downloads in a row
the remaining downloads are skipped, so we don't make matters worse.

Requires OPENAI_API_KEY in the environment or .env, ffmpeg/ffprobe, and a
JavaScript runtime for yt-dlp (Deno).

Exit codes: 0 = success, 1 = fatal, 2 = partial (some videos failed).
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Awaitable, Callable

sys.path.insert(0, str(Path(__file__).resolve().parent))

import videolib  # noqa: E402

log = logging.getLogger("transcribe")

MAX_BYTES = 25 * 1024 * 1024
WHISPER_MODEL = "whisper-1"
WHISPER_USD_PER_MINUTE = 0.006

# Download failures that mean YouTube is blocking us, not this one video.
BLOCKING_REASONS = {"bot_check", "po_token", "http_429"}
BREAKER_THRESHOLD = 3
# Download failures worth one more try.
RETRY_REASONS = {"network", "http_403"}
DOWNLOAD_RETRY_DELAY = 5.0
# Warn when the transcript ends before this fraction of the video.
TRUNCATION_RATIO = 0.9
# Whisper sometimes returns a long run of cues without words (just ".")
# for part of the audio. A chunk with a stretch this long is retried once;
# a transcript that still has one is rejected.
MAX_WORDLESS_S = 120
# Aim chunks at this share of the API limit: bitrates vary, and a chunk
# that ends up just over the limit gets split again into a tiny piece.
CHUNK_TARGET_RATIO = 0.9
MAX_STDERR_CHARS = 4000


# ---------------------------------------------------------------------------
# Selecting videos
# ---------------------------------------------------------------------------


@dataclass
class Candidate:
    dir: Path
    url: str
    duration: int
    frontmatter: dict[str, Any] = field(default_factory=dict)

    @property
    def slug(self) -> str:
        return self.dir.name

    @property
    def video_id(self) -> str | None:
        return videolib.youtube_id(self.url)


def select_videos(
    dirs: list[Path],
    summary: videolib.RunSummary,
    *,
    limit: int | None = None,
    max_audio_minutes: float | None = None,
) -> list[Candidate]:
    """Pick the videos to transcribe this run, in the given order.

    ``limit`` caps the number of videos and ``max_audio_minutes`` the total
    duration (a single video longer than the budget is still taken if it is
    the first one, so it doesn't block the queue forever).
    """
    selected: list[Candidate] = []
    minutes = 0.0
    deferred: list[str] = []

    for d in dirs:
        if (d / "transcription.vtt").exists():
            summary.tally("already_transcribed")
            continue
        index = d / "_index.md"
        if not index.exists():
            summary.add("skipped", slug=d.name, reason="no_index")
            continue
        fm = videolib.read_frontmatter(index)
        if fm.get("transcribe", True) is False:
            summary.tally("excluded")
            continue
        external = fm.get("external") or {}
        url = external.get("url")
        if not url:
            summary.add("skipped", slug=d.name, reason="no_url")
            log.warning("Skipping %s: no external.url", d.name)
            continue
        duration = int(external.get("duration") or 0)
        if duration <= 0:
            summary.add("skipped", slug=d.name, video_id=videolib.youtube_id(url), reason="no_duration")
            log.info("Skipping %s: no duration (live stream or premiere?)", d.name)
            continue

        over_limit = limit is not None and len(selected) >= limit
        over_budget = (
            max_audio_minutes is not None
            and selected
            and minutes + duration / 60 > max_audio_minutes
        )
        if over_limit or over_budget:
            deferred.append(d.name)
            continue
        selected.append(Candidate(d, url, duration, fm))
        minutes += duration / 60

    if deferred:
        summary.tally("deferred", len(deferred))
        summary.extra["deferred"] = deferred
        log.info("Deferred %d videos to a later run (--limit / --max-audio-minutes)", len(deferred))
    summary.extra["selected_audio_minutes"] = round(minutes, 1)
    return selected


# ---------------------------------------------------------------------------
# Downloading
# ---------------------------------------------------------------------------

# Ordered: the first matching pattern wins.
YTDLP_ERROR_PATTERNS: list[tuple[str, str]] = [
    ("age_restricted", r"confirm your age|age[- ]restricted|inappropriate for some users"),
    ("bot_check", r"confirm you(?:'|’)?re not a bot|Sign in to confirm you|not a bot"),
    ("po_token", r"PO Token|po_token|GVS PO"),
    ("members_only", r"members[- ]only|Join this channel"),
    ("private", r"Private video|video is private"),
    ("live_or_upcoming", r"live event will begin|Premieres in|This live event|is not available until|is_upcoming"),
    ("js_runtime", r"JavaScript runtime|JS runtime|challenge solv|n challenge|Signature extraction failed"),
    ("unavailable", r"Video unavailable|video is not available|has been removed|This video is no longer available|account associated with this video has been terminated"),
    ("http_403", r"HTTP Error 403|403: Forbidden|status code 403"),
    ("http_429", r"HTTP Error 429|Too Many Requests"),
    ("format_unavailable", r"Requested format is not available|No video formats found"),
    (
        "network",
        r"timed out|Connection reset|Temporary failure in name resolution|Network is unreachable"
        r"|Remote end closed|IncompleteRead|Connection refused|getaddrinfo failed|SSL",
    ),
]


# Warnings that explain a vague ERROR line ("Requested format is not
# available", "HTTP Error 403") better than the error itself.
HINT_REASONS = ("bot_check", "po_token", "js_runtime")
VAGUE_REASONS = ("unknown", "format_unavailable", "http_403")


def _match(text: str, reasons: tuple[str, ...] | None = None) -> str:
    for reason, pattern in YTDLP_ERROR_PATTERNS:
        if (reasons is None or reason in reasons) and re.search(pattern, text, flags=re.IGNORECASE):
            return reason
    return "unknown"


def classify_ytdlp_error(output: str) -> str:
    """Classify a failed yt-dlp run from its output.

    The ERROR lines decide; when they're vague, warnings such as "GVS PO
    Token which was not provided" or "No supported JavaScript runtime" are
    used instead.
    """
    error_lines = "\n".join(line for line in output.splitlines() if "ERROR" in line)
    reason = _match(error_lines or output)
    if reason in VAGUE_REASONS:
        hint = _match(output, HINT_REASONS)
        if hint != "unknown":
            return hint
    return reason


def last_error_line(output: str) -> str:
    """The most useful single line of yt-dlp output: the last ERROR line."""
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    errors = [line for line in lines if "ERROR" in line]
    return (errors or lines or ["(no output)"])[-1]


class DownloadError(Exception):
    def __init__(self, reason: str, stderr: str, attempts: int = 1):
        super().__init__(last_error_line(stderr))
        self.reason = reason
        self.stderr = stderr
        self.attempts = attempts


class CircuitBreaker:
    """Trips after ``threshold`` blocked downloads in a row."""

    def __init__(self, threshold: int = BREAKER_THRESHOLD):
        self.threshold = threshold
        self.consecutive = 0
        self.tripped = False

    def record(self, reason: str | None) -> None:
        if reason in BLOCKING_REASONS:
            self.consecutive += 1
            if self.consecutive >= self.threshold and not self.tripped:
                self.tripped = True
                log.error(
                    "%d downloads in a row were blocked by YouTube (%s); "
                    "skipping the remaining downloads this run",
                    self.consecutive,
                    reason,
                )
        else:
            self.consecutive = 0


def build_ytdlp_cmd(
    url: str, dest_dir: Path, browser: str | None, cookies: Path | None, verbose: bool = False
) -> list[str]:
    cmd = [
        sys.executable,
        "-m",
        "yt_dlp",
        "--remote-components",
        "ejs:github",
        "--format",
        "bestaudio/best",
        "--output",
        str(dest_dir / "audio.%(ext)s"),
        "--no-playlist",
        "--no-progress",
        # --verbose shows the JS runtime, PO token providers, and clients used.
        "--verbose" if verbose else "--quiet",
    ]
    if browser:
        cmd += ["--cookies-from-browser", browser]
    if cookies:
        cmd += ["--cookies", str(cookies)]
    cmd.append(url)
    return cmd


def find_audio_file(directory: Path) -> Path | None:
    for f in sorted(directory.glob("audio.*")):
        if f.suffix not in (".part", ".ytdl"):
            return f
    return None


def download_audio(
    url: str,
    dest_dir: Path,
    *,
    browser: str | None,
    cookies: Path | None,
    run: Callable[..., subprocess.CompletedProcess],
    label: str,
) -> Path:
    cmd = build_ytdlp_cmd(url, dest_dir, browser, cookies, verbose=log.isEnabledFor(logging.DEBUG))
    log.debug("%s: running %s", label, " ".join(cmd))
    result = run(cmd, capture_output=True, text=True)
    output = "\n".join(s for s in (result.stderr, result.stdout) if s and s.strip())
    if result.returncode != 0:
        raise DownloadError(classify_ytdlp_error(output), output)
    for line in output.splitlines():
        log.debug("%s: yt-dlp: %s", label, line)
    audio = find_audio_file(dest_dir)
    if audio is None:
        raise DownloadError("no_file", output or "yt-dlp succeeded but wrote no audio file")
    return audio


async def download_with_retry(
    candidate: Candidate,
    dest_dir: Path,
    args: argparse.Namespace,
    run: Callable[..., subprocess.CompletedProcess],
    sleep: Callable[[float], Awaitable[Any]],
) -> Path:
    label = f"{candidate.slug} ({candidate.video_id})"
    for attempt in (1, 2):
        try:
            return await asyncio.to_thread(
                download_audio,
                candidate.url,
                dest_dir,
                browser=args.cookies_from_browser,
                cookies=args.cookies,
                run=run,
                label=label,
            )
        except DownloadError as e:
            e.attempts = attempt
            if attempt == 1 and e.reason in RETRY_REASONS:
                log.warning("%s: download failed (%s: %s); retrying in %.0fs", label, e.reason, e, DOWNLOAD_RETRY_DELAY)
                await sleep(DOWNLOAD_RETRY_DELAY)
                continue
            raise
    raise AssertionError("unreachable")


# ---------------------------------------------------------------------------
# Splitting large audio files
# ---------------------------------------------------------------------------


def get_audio_duration(src: Path) -> float:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(src)],
        capture_output=True,
        text=True,
        check=True,
    )
    return float(result.stdout.strip())


def detect_silence(src: Path, noise_db: float = -30, min_duration: float = 0.5) -> list[float]:
    result = subprocess.run(
        ["ffmpeg", "-i", str(src), "-af", f"silencedetect=noise={noise_db}dB:d={min_duration}", "-f", "null", "-"],
        capture_output=True,
        text=True,
    )
    starts: list[float] = []
    ends: list[float] = []
    for line in result.stderr.splitlines():
        if m := re.search(r"silence_start:\s*([\d.]+)", line):
            starts.append(float(m.group(1)))
        elif m := re.search(r"silence_end:\s*([\d.]+)", line):
            ends.append(float(m.group(1)))
    return [(s + e) / 2 for s, e in zip(starts, ends)]


def compute_chunk_boundaries(
    duration: float,
    file_size: int,
    silence_points: list[float],
    max_bytes: int = MAX_BYTES,
) -> list[tuple[float, float]]:
    max_chunk_secs = CHUNK_TARGET_RATIO * max_bytes / (file_size / duration)
    boundaries: list[tuple[float, float]] = []
    start = 0.0
    while start < duration:
        ideal_end = min(start + max_chunk_secs, duration)
        if ideal_end >= duration:
            boundaries.append((start, duration))
            break
        candidates = [t for t in silence_points if start < t <= ideal_end]
        cut = max(candidates) if candidates else ideal_end
        boundaries.append((start, cut))
        start = cut
    return boundaries


def split_at_silence(
    src: Path, work_dir: Path, _offset: float = 0.0, max_bytes: int = MAX_BYTES
) -> list[tuple[Path, float]]:
    """Split ``src`` into chunks under ``max_bytes``; return (path, offset) pairs."""
    duration = get_audio_duration(src)
    silence = detect_silence(src)
    boundaries = compute_chunk_boundaries(duration, src.stat().st_size, silence, max_bytes)
    log.debug("Splitting %s (%.0fs) at %s", src.name, duration, [round(e) for _, e in boundaries])
    chunks: list[tuple[Path, float]] = []
    for start, end in boundaries:
        fd, name = tempfile.mkstemp(suffix=src.suffix, prefix="chunk-", dir=work_dir)
        os.close(fd)
        tmp = Path(name)
        subprocess.run(
            ["ffmpeg", "-y", "-ss", str(start), "-i", str(src), "-t", str(end - start), "-c", "copy", str(tmp)],
            check=True,
            capture_output=True,
        )
        if tmp.stat().st_size > max_bytes and end - start > 1:
            chunks.extend(split_at_silence(tmp, work_dir, _offset=_offset + start, max_bytes=max_bytes))
            tmp.unlink(missing_ok=True)
        else:
            chunks.append((tmp, _offset + start))
    return chunks


# ---------------------------------------------------------------------------
# Transcribing
# ---------------------------------------------------------------------------


def merge_vtt(parts: list[tuple[str, float]]) -> str:
    cues = [
        (start + offset, end + offset, text)
        for vtt_content, offset in parts
        for start, end, text in videolib.parse_vtt(vtt_content)
    ]
    return videolib.render_vtt(cues)


def build_prompt(frontmatter: dict[str, Any]) -> str:
    parts = []
    title = frontmatter.get("title", "")
    if title:
        parts.append(str(title))
    parts.extend(str(s) for s in frontmatter.get("software", []) or [])
    return ", ".join(parts)


class TranscriptError(Exception):
    def __init__(self, reason: str, detail: str):
        super().__init__(detail)
        self.reason = reason


def longest_wordless_stretch(cues: list[videolib.Cue]) -> tuple[float, float]:
    """``(seconds, start)`` of the longest run of consecutive cues without words."""
    longest, longest_start = 0.0, 0.0
    run_start = None
    for start, end, text in cues:
        if re.search(r"\w", text):
            run_start = None
            continue
        if run_start is None:
            run_start = start
        if end - run_start > longest:
            longest, longest_start = end - run_start, run_start
    return longest, longest_start


def check_transcript(vtt: str, duration: int) -> tuple[list[videolib.Cue], list[str]]:
    """Return ``(cues, warnings)``; raise TranscriptError if unusable."""
    cues = videolib.parse_vtt(vtt)
    if not cues:
        raise TranscriptError("empty_transcript", f"Whisper returned no cues ({len(vtt)} characters)")
    stretch, at = longest_wordless_stretch(cues)
    if stretch > MAX_WORDLESS_S:
        raise TranscriptError(
            "degenerate_transcript",
            f"{stretch:.0f}s of cues without words from {videolib.format_vtt_timestamp(at)[:8]}",
        )
    warnings = []
    last_end = cues[-1][1]
    if duration > 0 and last_end < TRUNCATION_RATIO * duration:
        warnings.append(
            f"suspect_truncated: last cue ends at {videolib.format_vtt_timestamp(last_end)} "
            f"of {videolib.format_vtt_timestamp(duration)}"
        )
    return cues, warnings


async def transcribe_file(
    client: Any,
    audio_file: Path,
    prompt: str,
    *,
    label: str,
    rate_limiter: videolib.RateLimiter,
    sleep: Callable[[float], Awaitable[Any]],
) -> str:
    kwargs: dict[str, Any] = {"model": WHISPER_MODEL, "response_format": "vtt"}
    if prompt:
        kwargs["prompt"] = prompt

    async def call() -> str:
        await rate_limiter.wait()
        with open(audio_file, "rb") as f:
            return await client.audio.transcriptions.create(file=f, **kwargs)

    return await videolib.retry_async(call, label=label, logger=log, sleep=sleep)


@dataclass
class Context:
    client: Any
    args: argparse.Namespace
    semaphore: asyncio.Semaphore
    rate_limiter: videolib.RateLimiter
    breaker: CircuitBreaker
    run: Callable[..., subprocess.CompletedProcess]
    sleep: Callable[[float], Awaitable[Any]]
    max_bytes: int = MAX_BYTES


async def process_video(c: Candidate, ctx: Context) -> dict[str, Any]:
    async with ctx.semaphore:
        label = f"{c.slug} ({c.video_id})"
        item: dict[str, Any] = {"slug": c.slug, "video_id": c.video_id, "duration_s": c.duration}
        if ctx.breaker.tripped:
            log.info("%s: skipped, downloads are blocked this run", label)
            return {**item, "status": "skipped", "reason": "download_blocked"}

        timings: dict[str, float] = {}
        item["timings"] = timings
        legacy_audio = find_audio_file(c.dir)
        try:
            with tempfile.TemporaryDirectory(prefix="transcribe-") as tmp:
                work_dir = Path(tmp)
                if legacy_audio:
                    audio = legacy_audio
                    log.info("%s: using existing %s", label, audio.name)
                else:
                    log.info("%s: downloading audio (%s)", label, videolib.format_vtt_timestamp(c.duration)[:8])
                    t0 = time.monotonic()
                    try:
                        audio = await download_with_retry(c, work_dir, ctx.args, ctx.run, ctx.sleep)
                    except DownloadError as e:
                        ctx.breaker.record(e.reason)
                        log.error("%s: download failed: %s: %s", label, e.reason, e)
                        for line in e.stderr.splitlines():
                            log.error("%s:   yt-dlp: %s", label, line)
                        return {
                            **item,
                            "status": "error",
                            "reason": e.reason,
                            "stage": "download",
                            "detail": str(e),
                            "attempts": e.attempts,
                            "stderr": e.stderr[-MAX_STDERR_CHARS:],
                        }
                    ctx.breaker.record(None)
                    timings["download_s"] = round(time.monotonic() - t0, 1)

                size = audio.stat().st_size
                item["audio_bytes"] = size
                item["audio_format"] = audio.suffix.lstrip(".")
                log.info(
                    "%s: audio %s, %.1f MB%s",
                    label,
                    item["audio_format"],
                    size / 1024 / 1024,
                    f" in {timings['download_s']}s" if "download_s" in timings else "",
                )

                if size > ctx.max_bytes:
                    t0 = time.monotonic()
                    chunks = await asyncio.to_thread(split_at_silence, audio, work_dir, 0.0, ctx.max_bytes)
                    timings["split_s"] = round(time.monotonic() - t0, 1)
                    log.info("%s: split into %d chunks at %s", label, len(chunks), ", ".join(f"{o:.0f}s" for _, o in chunks))
                else:
                    chunks = [(audio, 0.0)]
                item["chunks"] = len(chunks)

                prompt = build_prompt(c.frontmatter)
                parts: list[tuple[str, float]] = []
                t0 = time.monotonic()
                for i, (chunk, offset) in enumerate(chunks, start=1):
                    chunk_label = f"{label} chunk {i}/{len(chunks)}" if len(chunks) > 1 else label
                    tc = time.monotonic()
                    for attempt in (1, 2):
                        vtt = await transcribe_file(
                            ctx.client, chunk, prompt, label=chunk_label, rate_limiter=ctx.rate_limiter, sleep=ctx.sleep
                        )
                        stretch, at = longest_wordless_stretch(videolib.parse_vtt(vtt))
                        if stretch <= MAX_WORDLESS_S:
                            break
                        log.warning(
                            "%s: Whisper returned %.0fs of cues without words from %s (attempt %d/2)%s",
                            chunk_label,
                            stretch,
                            videolib.format_vtt_timestamp(at + offset)[:8],
                            attempt,
                            "; retrying" if attempt == 1 else "",
                        )
                        item["whisper_retries"] = item.get("whisper_retries", 0) + (attempt == 1)
                    log.info(
                        "%s: transcribed %.1f MB (offset %.0fs) in %.1fs",
                        chunk_label,
                        chunk.stat().st_size / 1024 / 1024,
                        offset,
                        time.monotonic() - tc,
                    )
                    parts.append((vtt, offset))
                timings["transcribe_s"] = round(time.monotonic() - t0, 1)

                data = parts[0][0] if len(parts) == 1 else merge_vtt(parts)
                cues, warnings = check_transcript(data, c.duration)
                for w in warnings:
                    log.warning("%s: %s", label, w)
                videolib.atomic_write_text(c.dir / "transcription.vtt", data)
                if legacy_audio:
                    legacy_audio.unlink(missing_ok=True)
        except TranscriptError as e:
            log.error("%s: %s: %s", label, e.reason, e)
            return {**item, "status": "error", "reason": e.reason, "stage": "check", "detail": str(e)}
        except Exception as e:  # noqa: BLE001 - every failure goes in the summary
            log.exception("%s: transcription failed", label)
            return {
                **item,
                "status": "error",
                "reason": "transcription_failed",
                "stage": "transcribe",
                "detail": videolib.describe_api_error(e),
            }

        cost = round(c.duration / 60 * WHISPER_USD_PER_MINUTE, 4)
        log.info(
            "%s: wrote transcription.vtt (%d cues, last at %s, ~$%.3f)",
            label,
            len(cues),
            videolib.format_vtt_timestamp(cues[-1][1])[:8],
            cost,
        )
        return {
            **item,
            "status": "transcribed",
            "cues": len(cues),
            "estimated_cost_usd": cost,
            "warnings": warnings or None,
        }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def build_client(project_root: Path) -> Any:
    import openai
    from dotenv import load_dotenv

    load_dotenv(project_root / ".env")
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set in .env or environment")
    return openai.AsyncOpenAI(api_key=api_key, max_retries=0)  # we retry ourselves, with logging


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download and transcribe video audio with OpenAI Whisper")
    parser.add_argument("--jobs", type=int, default=5, metavar="N", help="parallel jobs (default: 5)")
    parser.add_argument("--limit", type=int, metavar="N", help="transcribe at most N videos (newest first)")
    parser.add_argument(
        "--max-audio-minutes", type=float, metavar="M", help="stop selecting videos after M minutes of audio"
    )
    parser.add_argument("--video", metavar="NAME", help="only this video directory (name, prefix, or path)")
    parser.add_argument(
        "--cookies-from-browser",
        metavar="BROWSER",
        help="browser to read YouTube cookies from for yt-dlp (e.g. chrome, firefox, safari)",
    )
    parser.add_argument("--cookies", type=Path, metavar="FILE", help="cookies.txt file for yt-dlp")
    parser.add_argument("--dry-run", action="store_true", help="list what would be transcribed")
    videolib.add_common_args(parser)
    return parser.parse_args(argv)


def main(
    argv: list[str] | None = None,
    client: Any = None,
    run: Callable[..., subprocess.CompletedProcess] = subprocess.run,
    sleep: Callable[[float], Awaitable[Any]] = asyncio.sleep,
    max_bytes: int = MAX_BYTES,
    min_request_interval: float = 1.0,
) -> int:
    args = parse_args(argv)
    videolib.setup_logging("transcribe", args.verbose)
    summary = videolib.RunSummary("transcribe")
    summary.extra.update(dry_run=args.dry_run, limit=args.limit, max_audio_minutes=args.max_audio_minutes)
    videos_dir = args.project_root / "content" / "resources" / "videos"

    def body() -> None:
        nonlocal client
        summary.environment = videolib.log_environment(
            log, packages=["yt-dlp", "yt-dlp-ejs", "openai", "bgutil-ytdlp-pot-provider"], tools=["deno", "node", "ffmpeg", "ffprobe"]
        )
        if not videos_dir.exists():
            summary.fatal = f"Videos directory not found: {videos_dir}"
            return
        if not args.dry_run:
            missing = [t for t in ("ffmpeg", "ffprobe") if not shutil.which(t)]
            if missing:
                summary.fatal = f"Required tools not found: {', '.join(missing)}"
                return
            if not (shutil.which("deno") or shutil.which("node")):
                log.warning("No JavaScript runtime (deno or node) found; YouTube downloads will probably fail")

        dirs = [videolib.resolve_video_dir(args.video, videos_dir)] if args.video else videolib.video_dirs(videos_dir)
        candidates = select_videos(dirs, summary, limit=args.limit, max_audio_minutes=args.max_audio_minutes)
        log.info(
            "Selected %d of %d video directories (%.0f minutes of audio, --jobs %d)",
            len(candidates),
            len(dirs),
            summary.extra["selected_audio_minutes"],
            args.jobs,
        )
        if args.dry_run:
            for c in candidates:
                log.info("Would transcribe %s (%s, %ds)", c.slug, c.video_id, c.duration)
                summary.add("would_transcribe", slug=c.slug, video_id=c.video_id, duration_s=c.duration)
            return
        if not candidates:
            return
        if client is None:
            client = build_client(args.project_root)

        ctx = Context(
            client=client,
            args=args,
            semaphore=asyncio.Semaphore(args.jobs),
            rate_limiter=videolib.RateLimiter(min_interval=min_request_interval),
            breaker=CircuitBreaker(),
            run=run,
            sleep=sleep,
            max_bytes=max_bytes,
        )

        async def go() -> list[dict[str, Any]]:
            return await asyncio.gather(*(process_video(c, ctx) for c in candidates))

        for result in asyncio.run(go()):
            summary.add(result.pop("status"), **result)

        transcribed = summary.by_status("transcribed")
        summary.extra["breaker_tripped"] = ctx.breaker.tripped
        summary.extra["estimated_cost_usd"] = round(sum(i["estimated_cost_usd"] for i in transcribed), 3)
        summary.extra["transcribed_audio_minutes"] = round(sum(i["duration_s"] for i in transcribed) / 60, 1)
        log.info(
            "Transcribed %d videos (%.0f minutes, ~$%.2f)",
            len(transcribed),
            summary.extra["transcribed_audio_minutes"],
            summary.extra["estimated_cost_usd"],
        )

    return videolib.run_main(summary, log, args.summary_json, body)


if __name__ == "__main__":
    sys.exit(main())
