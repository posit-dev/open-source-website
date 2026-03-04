#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "openai>=2.0.0",
#   "python-dotenv>=1.0.0",
#   "yt-dlp>=2025.0",
# ]
# ///


"""
Download audio from YouTube and transcribe it for each video under
content/resources/videos/.

For each subdirectory:
- If transcription.vtt already exists, skip.
- If no audio file exists, download it from external.url in _index.md using
  yt-dlp (pass --cookies-from-browser BROWSER if authentication is needed).
- If the audio exceeds the 25 MB API limit, split into chunks at silence
  boundaries, transcribe each chunk, and merge the VTT output with corrected
  timestamps.
- Delete the audio file after a successful transcription.

Requires OPENAI_API_KEY in .env.
Runs up to --jobs transcriptions in parallel (default 5) with at least 1 second
between API requests and exponential backoff on rate-limit / server errors.
"""

import argparse
import asyncio
import os
import random
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

import openai
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

console = Console(stderr=True)

MAX_BYTES = 25 * 1024 * 1024
MAX_RETRIES = 5
BASE_BACKOFF = 1.0


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


def find_audio_file(video_dir: Path) -> Path | None:
    for f in video_dir.glob("audio.*"):
        if f.suffix != ".part":
            return f
    return None


def get_video_url(video_dir: Path) -> str | None:
    index_file = video_dir / "_index.md"
    if not index_file.exists():
        return None
    frontmatter = parse_frontmatter(index_file.read_text(encoding="utf-8"))
    return frontmatter.get("external", {}).get("url")


def download_audio(url: str, dest_dir: Path, browser: str | None) -> None:
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
        "--quiet",
        "--no-warnings",
    ]
    if browser:
        cmd += ["--cookies-from-browser", browser]
    cmd.append(url)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())


def build_prompt(frontmatter: dict[str, Any]) -> str:
    parts = []
    title = frontmatter.get("title", "")
    if title:
        parts.append(title)
    software = frontmatter.get("software", []) or []
    parts.extend(software)
    return ", ".join(parts)


def get_audio_duration(src: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(src),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return float(result.stdout.strip())


def detect_silence(
    src: Path, noise_db: float = -30, min_duration: float = 0.5
) -> list[float]:
    result = subprocess.run(
        [
            "ffmpeg",
            "-i",
            str(src),
            "-af",
            f"silencedetect=noise={noise_db}dB:d={min_duration}",
            "-f",
            "null",
            "-",
        ],
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
) -> list[tuple[float, float]]:
    max_chunk_secs = MAX_BYTES / (file_size / duration)
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


def split_at_silence(src: Path, _offset: float = 0.0) -> list[tuple[Path, float]]:
    duration = get_audio_duration(src)
    silence = detect_silence(src)
    boundaries = compute_chunk_boundaries(duration, src.stat().st_size, silence)
    chunks: list[tuple[Path, float]] = []
    for start, end in boundaries:
        tmp = Path(tempfile.mktemp(suffix=src.suffix))
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-ss",
                str(start),
                "-i",
                str(src),
                "-t",
                str(end - start),
                "-c",
                "copy",
                str(tmp),
            ],
            check=True,
            capture_output=True,
        )
        if tmp.stat().st_size > MAX_BYTES:
            sub_chunks = split_at_silence(tmp, _offset=_offset + start)
            tmp.unlink(missing_ok=True)
            chunks.extend(sub_chunks)
        else:
            chunks.append((tmp, _offset + start))
    return chunks


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


def merge_vtt(parts: list[tuple[str, float]]) -> str:
    lines = ["WEBVTT", ""]
    for vtt_content, offset in parts:
        for start, end, text in parse_vtt(vtt_content):
            lines.append(
                f"{format_vtt_timestamp(start + offset)} --> "
                f"{format_vtt_timestamp(end + offset)}"
            )
            lines.append(text)
            lines.append("")
    return "\n".join(lines)


class RateLimiter:
    """Ensures at least `min_interval` seconds between API requests."""

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


async def transcribe_audio(
    audio_file: Path,
    prompt: str,
    name: str,
    client: openai.AsyncOpenAI,
    rate_limiter: RateLimiter,
) -> str:
    kwargs: dict[str, Any] = {
        "model": "whisper-1",
        "response_format": "vtt",
    }
    if prompt:
        kwargs["prompt"] = prompt

    for attempt in range(MAX_RETRIES):
        if attempt > 0:
            delay = BASE_BACKOFF * (2 ** (attempt - 1)) + random.uniform(0, 1)
            console.print(
                f"  [yellow]↻[/] {name}  retry {attempt + 1}/{MAX_RETRIES} in {delay:.1f}s"
            )
            await asyncio.sleep(delay)

        await rate_limiter.wait()
        try:
            with open(audio_file, "rb") as f:
                return await client.audio.transcriptions.create(file=f, **kwargs)
        except openai.RateLimitError:
            if attempt == MAX_RETRIES - 1:
                raise
        except openai.APIStatusError as e:
            if e.status_code < 500 or attempt == MAX_RETRIES - 1:
                raise

    raise RuntimeError("Exceeded max retries")


async def process_video_async(
    video_dir: Path,
    client: openai.AsyncOpenAI,
    semaphore: asyncio.Semaphore,
    rate_limiter: RateLimiter,
    progress: Progress,
    overall_task: TaskID,
    browser: str | None,
) -> str:
    async with semaphore:
        name = video_dir.name
        job_task = progress.add_task(f"[dim]{name}", total=None)
        try:
            transcription_file = video_dir / "transcription.vtt"
            if transcription_file.exists():
                return "skipped"

            audio_file = find_audio_file(video_dir)

            if audio_file is None:
                url = get_video_url(video_dir)
                if not url:
                    return "no_url"
                progress.update(job_task, description=f"[cyan]{name}  downloading")
                await asyncio.to_thread(download_audio, url, video_dir, browser)
                audio_file = find_audio_file(video_dir)
                if audio_file is None:
                    raise RuntimeError("Download succeeded but audio file not found")

            index_file = video_dir / "_index.md"
            frontmatter = (
                parse_frontmatter(index_file.read_text(encoding="utf-8"))
                if index_file.exists()
                else {}
            )
            prompt = build_prompt(frontmatter)

            if audio_file.stat().st_size > MAX_BYTES:
                size_mb = audio_file.stat().st_size / 1024 / 1024
                progress.update(
                    job_task,
                    description=f"[yellow]{name}  chunking audio ({size_mb:.1f} MB)",
                )
                chunks: list[tuple[Path, float]] = await asyncio.to_thread(
                    split_at_silence, audio_file
                )
                is_temp = True
            else:
                chunks = [(audio_file, 0.0)]
                is_temp = False

            try:
                vtt_parts: list[tuple[str, float]] = []
                total_chunks = len(chunks)
                for i, (chunk_path, offset) in enumerate(chunks):
                    label = f" {i + 1}/{total_chunks}" if total_chunks > 1 else ""
                    progress.update(
                        job_task, description=f"[cyan]{name}  transcribing{label}"
                    )
                    vtt = await transcribe_audio(
                        chunk_path, prompt, name, client, rate_limiter
                    )
                    vtt_parts.append((vtt, offset))
            finally:
                if is_temp:
                    for chunk_path, _ in chunks:
                        chunk_path.unlink(missing_ok=True)

            if len(vtt_parts) == 1:
                data = vtt_parts[0][0]
            else:
                progress.update(
                    job_task, description=f"[cyan]{name}  merging transcript"
                )
                data = merge_vtt(vtt_parts)
            transcription_file.write_text(data, encoding="utf-8")
            audio_file.unlink()
            return "transcribed"

        except Exception as e:
            console.print(f"  [red]✗[/] {name}: {e}")
            return "error"
        finally:
            progress.remove_task(job_task)
            progress.advance(overall_task)


async def main_async(jobs: int, browser: str | None) -> None:
    console.print("\n[bold blue]Video Transcriber[/]\n")

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        console.print("[bold red]Error:[/] OPENAI_API_KEY not set in .env")
        sys.exit(1)

    client = openai.AsyncOpenAI(api_key=api_key)

    videos_dir = Path(__file__).parent.parent / "content" / "resources" / "videos"
    if not videos_dir.exists():
        console.print(f"[bold red]Error:[/] Videos directory not found: {videos_dir}")
        sys.exit(1)

    dirs = sorted(d for d in videos_dir.iterdir() if d.is_dir())
    console.print(f"[dim]Found {len(dirs)} video directories (--jobs {jobs})[/]\n")

    semaphore = asyncio.Semaphore(jobs)
    rate_limiter = RateLimiter(min_interval=1.0)

    with Progress(
        SpinnerColumn(),
        TextColumn("{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        overall_task = progress.add_task("[bold cyan]Transcribing", total=len(dirs))

        results: list[str] = await asyncio.gather(
            *[
                process_video_async(
                    d, client, semaphore, rate_limiter, progress, overall_task, browser
                )
                for d in dirs
            ]
        )

    transcribed = results.count("transcribed")
    skipped = results.count("skipped")
    no_url = results.count("no_url")
    errors = results.count("error")

    console.print("\n[bold]Summary:[/]")
    console.print(f"  [green]✓[/] Transcribed: {transcribed}")
    console.print(f"  [dim]○[/] Skipped:     {skipped}")
    console.print(f"  [dim]○[/] No URL:      {no_url}")
    if errors:
        console.print(f"  [red]✗[/] Errors:      {errors}")

    console.print("\n[bold green]✓ Done![/]\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download and transcribe video audio files using OpenAI Whisper"
    )
    parser.add_argument(
        "--jobs",
        type=int,
        default=5,
        metavar="N",
        help="number of parallel transcription jobs (default: 5)",
    )
    parser.add_argument(
        "--cookies-from-browser",
        metavar="BROWSER",
        help="browser to read cookies from for yt-dlp (e.g. chrome, firefox, safari)",
    )
    args = parser.parse_args()
    asyncio.run(main_async(args.jobs, args.cookies_from_browser))


if __name__ == "__main__":
    main()
