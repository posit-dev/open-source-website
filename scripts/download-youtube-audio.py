#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "yt-dlp>=2025.0",
# ]
# ///

"""
Download audio from YouTube videos listed under content/resources/videos/.

For each subdirectory, reads external.url from _index.md frontmatter and
downloads the audio as audio.mp3 using yt-dlp. Directories that already
contain audio.mp3 are skipped.
"""

import sys
from pathlib import Path
from typing import Any

import yaml
import yt_dlp
from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
)

console = Console(stderr=True)


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


def get_video_url(video_dir: Path) -> str | None:
    index_file = video_dir / "_index.md"
    if not index_file.exists():
        return None
    frontmatter = parse_frontmatter(index_file.read_text(encoding="utf-8"))
    return frontmatter.get("external", {}).get("url")


def download_audio(url: str, dest_dir: Path) -> None:
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": str(dest_dir / "audio.%(ext)s"),
        "no_playlist": True,
        "quiet": True,
        "no_warnings": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main() -> None:
    console.print("\n[bold blue]YouTube Audio Downloader[/]\n")

    videos_dir = Path(__file__).parent.parent / "content" / "resources" / "videos"

    if not videos_dir.exists():
        console.print(f"[bold red]Error:[/] Videos directory not found: {videos_dir}")
        sys.exit(1)

    dirs = sorted(d for d in videos_dir.iterdir() if d.is_dir())
    console.print(f"[dim]Found {len(dirs)} video directories[/]\n")

    downloaded = skipped = errors = no_url = 0

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Downloading...", total=len(dirs))

        for video_dir in dirs:
            progress.update(task, description=f"[cyan]{video_dir.name}")

            if any(video_dir.glob("audio.*")):
                skipped += 1
                progress.advance(task)
                continue

            url = get_video_url(video_dir)
            if not url:
                no_url += 1
                progress.advance(task)
                continue

            try:
                download_audio(url, video_dir)
                console.print(f"  [green]✓[/] {video_dir.name}")
                downloaded += 1
            except Exception as e:
                console.print(f"  [red]✗[/] {video_dir.name}: {e}")
                errors += 1

            progress.advance(task)

    console.print("\n[bold]Summary:[/]")
    console.print(f"  [green]✓[/] Downloaded: {downloaded}")
    console.print(f"  [dim]○[/] Skipped:    {skipped}")
    console.print(f"  [dim]○[/] No URL:     {no_url}")
    if errors:
        console.print(f"  [red]✗[/] Errors:    {errors}")

    console.print("\n[bold green]✓ Done![/]\n")


if __name__ == "__main__":
    main()
