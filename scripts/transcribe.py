#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "openai>=2.0.0",
#   "python-dotenv>=1.0.0",
# ]
# ///


"""
Transcribe audio files found under content/resources/videos/.

For each subdirectory that contains an audio file but no transcription.vtt,
optionally compresses it to fit the 25 MB API limit, and transcribes it using
the OpenAI whisper-1 model. The result is written as transcription.vtt.
Requires OPENAI_API_KEY in .env.

Runs up to --jobs transcriptions in parallel (default 5) with at least 1 second
between API requests and exponential backoff on rate-limit / server errors.
"""

import argparse
import asyncio
import os
import random
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
    TextColumn,
    TimeElapsedColumn,
)

console = Console(stderr=True, log_time_format="[%Y-%m-%d %H:%M:%S]", log_path=False)

MAX_BYTES = 25 * 1024 * 1024
COMPRESSION_BITRATES = ["64k", "48k", "32k", "24k", "16k"]
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


def compress_audio(src: Path) -> tuple[Path, bool]:
    if src.stat().st_size <= MAX_BYTES:
        return src, False

    for bitrate in COMPRESSION_BITRATES:
        tmp = Path(tempfile.mktemp(suffix=".mp3"))
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(src), "-c:a", "libmp3lame", "-b:a", bitrate, str(tmp)],
            check=True,
            capture_output=True,
        )
        if tmp.stat().st_size <= MAX_BYTES:
            return tmp, True
        tmp.unlink(missing_ok=True)

    raise RuntimeError(
        f"Could not compress {src.name} below 25 MB even at {COMPRESSION_BITRATES[-1]}"
    )


def build_prompt(frontmatter: dict[str, Any]) -> str:
    parts = []
    title = frontmatter.get("title", "")
    if title:
        parts.append(title)
    software = frontmatter.get("software", []) or []
    parts.extend(software)
    return ", ".join(parts)


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
            console.log(f"{name}  [yellow]retry {attempt + 1}/{MAX_RETRIES} in {delay:.1f}s[/]")
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
    task_id: Any,
) -> str:
    async with semaphore:
        name = video_dir.name
        try:
            audio_file = find_audio_file(video_dir)
            if audio_file is None:
                console.log(f"{name}  [dim]no audio file[/]")
                return "no_audio"

            transcription_file = video_dir / "transcription.vtt"
            if transcription_file.exists():
                console.log(f"{name}  [dim]already transcribed[/]")
                return "skipped"

            index_file = video_dir / "_index.md"
            frontmatter = (
                parse_frontmatter(index_file.read_text(encoding="utf-8"))
                if index_file.exists()
                else {}
            )
            prompt = build_prompt(frontmatter)

            if audio_file.stat().st_size > MAX_BYTES:
                size_mb = audio_file.stat().st_size / 1024 / 1024
                console.log(f"{name}  [yellow]compressing ({size_mb:.1f} MB)[/]")

            audio_path, is_temp = await asyncio.to_thread(compress_audio, audio_file)
            try:
                console.log(f"{name}  [cyan]transcribing[/]")
                data = await transcribe_audio(audio_path, prompt, name, client, rate_limiter)
            finally:
                if is_temp:
                    audio_path.unlink(missing_ok=True)

            transcription_file.write_text(data, encoding="utf-8")
            console.log(f"{name}  [green]done[/]")
            return "transcribed"

        except Exception as e:
            console.log(f"{name}  [red]error:[/] {e}")
            return "error"
        finally:
            progress.advance(task_id)


async def main_async(jobs: int) -> None:
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
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task_id = progress.add_task("[cyan]Transcribing...", total=len(dirs))

        results: list[str] = await asyncio.gather(
            *[
                process_video_async(d, client, semaphore, rate_limiter, progress, task_id)
                for d in dirs
            ]
        )

    transcribed = results.count("transcribed")
    skipped = results.count("skipped")
    no_audio = results.count("no_audio")
    errors = results.count("error")

    console.print("\n[bold]Summary:[/]")
    console.print(f"  [green]✓[/] Transcribed: {transcribed}")
    console.print(f"  [dim]○[/] Skipped:     {skipped}")
    console.print(f"  [dim]○[/] No audio:    {no_audio}")
    if errors:
        console.print(f"  [red]✗[/] Errors:      {errors}")

    console.print("\n[bold green]✓ Done![/]\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Transcribe video audio files using OpenAI Whisper"
    )
    parser.add_argument(
        "--jobs",
        type=int,
        default=5,
        metavar="N",
        help="number of parallel transcription jobs (default: 5)",
    )
    args = parser.parse_args()
    asyncio.run(main_async(args.jobs))


if __name__ == "__main__":
    main()
