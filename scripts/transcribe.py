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

For each subdirectory that contains an audio file but no transcription.json,
downloads the audio, optionally compresses it to fit the 25 MB API limit, and
transcribes it using the OpenAI gpt-4o-transcribe-diarize model. The result is
written as transcription.json. Requires OPENAI_API_KEY in .env.
"""

import json
import os
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
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
)

console = Console(stderr=True)

MAX_BYTES = 25 * 1024 * 1024
COMPRESSION_BITRATES = ["64k", "48k", "32k", "24k", "16k"]


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

    size_mb = src.stat().st_size / 1024 / 1024
    console.print(f"  [yellow]Compressing {src.name} ({size_mb:.1f} MB)…[/]")

    for bitrate in COMPRESSION_BITRATES:
        tmp = Path(tempfile.mktemp(suffix=".opus"))
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i",
                str(src),
                "-c:a",
                "libopus",
                "-b:a",
                bitrate,
                str(tmp),
            ],
            check=True,
            capture_output=True,
        )
        if tmp.stat().st_size <= MAX_BYTES:
            return tmp, True
        tmp.unlink(missing_ok=True)

    raise RuntimeError(
        f"Could not compress {src.name} below 25 MB even at {COMPRESSION_BITRATES[-1]}"
    )


def transcribe_audio(
    audio_file: Path,
    speaker_names: list[str],
    client: openai.OpenAI,
) -> dict[str, Any]:
    with open(audio_file, "rb") as f:
        kwargs: dict[str, Any] = {
            "model": "gpt-4o-transcribe-diarize",
            "file": f,
            "response_format": "diarized_json",
            "chunking_strategy": "auto",
        }
        if speaker_names:
            kwargs["known_speaker_names"] = speaker_names
        result = client.audio.transcriptions.create(**kwargs)
    return result.model_dump()


def process_video(video_dir: Path, client: openai.OpenAI) -> str:
    try:
        audio_file = find_audio_file(video_dir)
        if audio_file is None:
            return "no_audio"

        transcription_file = video_dir / "transcription.json"
        if transcription_file.exists():
            return "skipped"

        index_file = video_dir / "_index.md"
        frontmatter = (
            parse_frontmatter(index_file.read_text(encoding="utf-8"))
            if index_file.exists()
            else {}
        )

        speaker_names = frontmatter.get("people", []) or []

        audio_path, is_temp = compress_audio(audio_file)
        try:
            data = transcribe_audio(audio_path, speaker_names, client)
        finally:
            if is_temp:
                audio_path.unlink(missing_ok=True)

        transcription_file.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        return "transcribed"

    except Exception as e:
        console.print(f"  [red]✗[/] {video_dir.name}: {e}")
        return "error"


def main() -> None:
    console.print("\n[bold blue]Video Transcriber[/]\n")

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        console.print("[bold red]Error:[/] OPENAI_API_KEY not set in .env")
        sys.exit(1)

    client = openai.OpenAI(api_key=api_key)

    videos_dir = Path(__file__).parent.parent / "content" / "resources" / "videos"
    if not videos_dir.exists():
        console.print(f"[bold red]Error:[/] Videos directory not found: {videos_dir}")
        sys.exit(1)

    dirs = sorted(d for d in videos_dir.iterdir() if d.is_dir())
    console.print(f"[dim]Found {len(dirs)} video directories[/]\n")

    transcribed = skipped = no_audio = errors = 0

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Transcribing...", total=len(dirs))

        for video_dir in dirs:
            progress.update(task, description=f"[cyan]{video_dir.name}")
            result = process_video(video_dir, client)

            if result == "transcribed":
                console.print(f"  [green]✓[/] {video_dir.name}")
                transcribed += 1
            elif result == "skipped":
                skipped += 1
            elif result == "no_audio":
                no_audio += 1
            elif result == "error":
                errors += 1

            progress.advance(task)

    console.print("\n[bold]Summary:[/]")
    console.print(f"  [green]✓[/] Transcribed: {transcribed}")
    console.print(f"  [dim]○[/] Skipped:     {skipped}")
    console.print(f"  [dim]○[/] No audio:    {no_audio}")
    if errors:
        console.print(f"  [red]✗[/] Errors:      {errors}")

    console.print("\n[bold green]✓ Done![/]\n")


if __name__ == "__main__":
    main()
