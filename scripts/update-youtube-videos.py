#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "google-api-python-client>=2.100.0",
#   "tomli-w>=1.0.0",
#   "python-dotenv>=1.0.0",
#   "rich>=13.0.0",
# ]
# ///

"""
Fetch video metadata from YouTube channels and playlists.

Reads channel names and playlist IDs from data/youtube.toml,
fetches metadata via the YouTube Data API v3, and writes
video information to data/videos.toml.
"""

import argparse
import os
import re
import sys
import tomllib
import unicodedata
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import tomli_w
from dotenv import load_dotenv
from googleapiclient.discovery import build
from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeRemainingColumn,
)

console = Console(stderr=True)

THUMBNAIL_PREFERENCE = ["maxres", "high", "standard", "medium", "default"]


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text


def parse_iso8601_duration(duration: str) -> int:
    match = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", duration)
    if not match:
        return 0
    hours = int(match.group(1) or 0)
    minutes = int(match.group(2) or 0)
    seconds = int(match.group(3) or 0)
    return hours * 3600 + minutes * 60 + seconds


def get_api_key() -> str:
    load_dotenv()
    key = os.getenv("YOUTUBE_API_KEY")
    if not key:
        console.print(
            "[bold red]Error:[/] YOUTUBE_API_KEY not found in .env or environment"
        )
        sys.exit(1)
    return key


def load_youtube_config(config_path: Path) -> dict[str, list[str]]:
    if not config_path.exists():
        console.print(f"[bold red]Error:[/] Config file not found: {config_path}")
        sys.exit(1)
    with open(config_path, "rb") as f:
        data = tomllib.load(f)
    return {
        "channels": data.get("channels", []),
        "playlists": data.get("playlists", []),
        "videos": data.get("videos", []),
    }


def load_existing_videos(output_path: Path) -> dict[str, dict[str, Any]]:
    if not output_path.exists():
        return {}
    try:
        with open(output_path, "rb") as f:
            data = tomllib.load(f)
        return {v["url"]: v for v in data.get("videos", [])}
    except Exception as e:
        console.print(f"[yellow]Warning:[/] Could not load existing videos: {e}")
        return {}


def deduplicate_videos(
    videos: dict[str, dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    """Remove slug collisions, keeping the entry with the more recent last_updated."""
    seen: dict[str, str] = {}  # slug -> url
    result: dict[str, dict[str, Any]] = {}
    for url, video in videos.items():
        slug = video.get("slug", "")
        if slug not in seen:
            seen[slug] = url
            result[url] = video
        else:
            prev_url = seen[slug]
            prev = result[prev_url]
            if video.get("last_updated", "") > prev.get("last_updated", ""):
                del result[prev_url]
                seen[slug] = url
                result[url] = video
                console.print(
                    f"  [yellow]Warning:[/] Duplicate slug '{slug}': "
                    f"replaced {prev_url} with {url}"
                )
            else:
                console.print(
                    f"  [yellow]Warning:[/] Duplicate slug '{slug}': "
                    f"kept {prev_url}, discarded {url}"
                )
    return result


def write_videos(videos: dict[str, dict[str, Any]], output_path: Path) -> None:
    videos_list = [
        {k: v for k, v in video.items() if v is not None} for video in videos.values()
    ]
    with open(output_path, "wb") as f:
        tomli_w.dump({"videos": videos_list}, f)


def should_update_video(existing: dict[str, Any] | None, force: bool) -> bool:
    if force or not existing:
        return True
    last_updated_str = existing.get("last_updated")
    if not last_updated_str:
        return True
    try:
        last_updated = datetime.fromisoformat(last_updated_str)
        return (datetime.now(timezone.utc) - last_updated) >= timedelta(hours=12)
    except Exception:
        return True


def resolve_channel_uploads(youtube: Any, channel_name: str) -> tuple[str, str] | None:
    for params in [
        {"forUsername": channel_name},
        {"forHandle": f"@{channel_name}"},
    ]:
        try:
            resp = (
                youtube.channels()
                .list(part="contentDetails,snippet", **params)
                .execute()
            )
            if resp.get("items"):
                item = resp["items"][0]
                uploads_id = item["contentDetails"]["relatedPlaylists"]["uploads"]
                title = item["snippet"]["title"]
                console.print(
                    f"  [green]\u2713[/] Resolved uploads playlist: {uploads_id}"
                )
                return uploads_id, title
        except Exception as e:
            console.print(f"  [yellow]Warning:[/] API error for {params}: {e}")
    console.print(
        f"  [bold red]Error:[/] Could not resolve channel '{channel_name}', skipping"
    )
    return None


def fetch_playlist_video_ids(youtube: Any, playlist_id: str) -> list[str]:
    video_ids: list[str] = []
    request = youtube.playlistItems().list(
        part="contentDetails", playlistId=playlist_id, maxResults=50
    )
    while request:
        response = request.execute()
        for item in response.get("items", []):
            vid = item["contentDetails"]["videoId"]
            video_ids.append(vid)
        request = youtube.playlistItems().list_next(request, response)
    return video_ids


def fetch_video_metadata(youtube: Any, video_ids: list[str]) -> list[dict]:
    items: list[dict] = []
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i : i + 50]
        resp = (
            youtube.videos()
            .list(part="snippet,contentDetails,statistics", id=",".join(batch))
            .execute()
        )
        items.extend(resp.get("items", []))
    return items


def best_thumbnail(thumbnails: dict) -> str:
    for key in THUMBNAIL_PREFERENCE:
        if key in thumbnails:
            return thumbnails[key]["url"]
    return ""


def transform_video(item: dict, channel: str, playlist: str) -> dict[str, Any]:
    snippet = item.get("snippet", {})
    content = item.get("contentDetails", {})
    stats = item.get("statistics", {})
    title = snippet.get("title", "")
    date = snippet.get("publishedAt", "")
    date_prefix = date[:10] if len(date) >= 10 else ""
    slug = f"{date_prefix}_{slugify(title)}" if date_prefix else slugify(title)
    return {
        "url": f"https://www.youtube.com/watch?v={item['id']}",
        "title": title,
        "slug": slug,
        "date": date,
        "description": snippet.get("description", ""),
        "duration": parse_iso8601_duration(content.get("duration", "")),
        "channel": channel or snippet.get("channelTitle", ""),
        "playlist": playlist,
        "tags": snippet.get("tags", []),
        "view_count": int(stats.get("viewCount", 0)),
        "like_count": int(stats.get("likeCount", 0)),
        "comment_count": int(stats.get("commentCount", 0)),
        "thumbnail": best_thumbnail(snippet.get("thumbnails", {})),
        "language": snippet.get("defaultAudioLanguage", ""),
        "has_captions": content.get("caption") == "true",
        "definition": content.get("definition", ""),
        "publish": True,
        "last_updated": datetime.now(timezone.utc).isoformat(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch video metadata from YouTube channels and playlists."
    )
    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Force update all videos, ignoring last_updated timestamps.",
    )
    args = parser.parse_args()

    console.print("\n[bold blue]YouTube Video Metadata Fetcher[/]\n")

    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    config_path = project_root / "data" / "youtube.toml"
    output_path = project_root / "data" / "videos.toml"

    console.print(f"[dim]Config: {config_path}[/]")
    console.print(f"[dim]Output: {output_path}[/]\n")

    config = load_youtube_config(config_path)
    channels = config["channels"]
    playlists = config["playlists"]
    individual_videos = config["videos"]

    console.print(f"[cyan]Channels:[/]  {', '.join(channels) or '(none)'}")
    console.print(f"[cyan]Playlists:[/] {', '.join(playlists) or '(none)'}")
    console.print(f"[cyan]Videos:[/]    {', '.join(individual_videos) or '(none)'}")

    if args.force:
        console.print("[yellow]Force mode:[/] Ignoring last_updated timestamps")

    existing_videos = load_existing_videos(output_path)
    if existing_videos:
        console.print(f"[dim]Loaded {len(existing_videos)} existing videos[/]")

    api_key = get_api_key()
    youtube = build("youtube", "v3", developerKey=api_key)

    # video_id -> (channel, playlist)
    video_context: dict[str, tuple[str, str]] = {}
    quota_used = 0

    # Phase 2 + 3: Resolve channels and collect video IDs
    for channel_name in channels:
        console.print(f"\n[bold]Channel: {channel_name}[/]")
        result = resolve_channel_uploads(youtube, channel_name)
        quota_used += 1
        if not result:
            continue
        uploads_id, channel_title = result
        video_ids = fetch_playlist_video_ids(youtube, uploads_id)
        quota_used += (len(video_ids) // 50) + 1
        console.print(f"  [green]\u2713[/] Found {len(video_ids)} videos")
        for vid in video_ids:
            if vid not in video_context:
                video_context[vid] = (channel_title, "")

    for playlist_id in playlists:
        console.print(f"\n[bold]Playlist: {playlist_id}[/]")
        try:
            video_ids = fetch_playlist_video_ids(youtube, playlist_id)
            quota_used += (len(video_ids) // 50) + 1
            console.print(f"  [green]\u2713[/] Found {len(video_ids)} videos")
            for vid in video_ids:
                video_context[vid] = (video_context.get(vid, ("", ""))[0], playlist_id)
        except Exception as e:
            console.print(f"  [bold red]Error:[/] Could not fetch playlist: {e}")

    if individual_videos:
        console.print(f"\n[bold]Individual videos: {len(individual_videos)}[/]")
        for vid in individual_videos:
            if vid not in video_context:
                video_context[vid] = ("", "")
                console.print(f"  [green]\u2713[/] Added {vid}")
            else:
                console.print(f"  [dim]○[/] Already tracked: {vid}")

    console.print(f"\n[cyan]Total unique videos:[/] {len(video_context)}")

    # Phase 4 + 5: Fetch metadata, deduplicate, merge
    ids_to_fetch = []
    counters = {"new": 0, "updated": 0, "skipped": 0, "errors": 0}

    for vid, (channel, playlist) in video_context.items():
        url = f"https://www.youtube.com/watch?v={vid}"
        existing = existing_videos.get(url)
        if should_update_video(existing, args.force):
            ids_to_fetch.append(vid)
        else:
            counters["skipped"] += 1

    if not ids_to_fetch:
        console.print("\n[dim]All videos are up to date, nothing to fetch.[/]")
    else:
        console.print(
            f"\n[bold]Fetching metadata for {len(ids_to_fetch)} videos[/]"
            f" [dim]({counters['skipped']} skipped as fresh)[/]"
        )

        all_videos = dict(existing_videos)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeRemainingColumn(),
            console=console,
        ) as progress:
            task = progress.add_task("[cyan]Fetching...", total=len(ids_to_fetch))

            for i in range(0, len(ids_to_fetch), 50):
                batch = ids_to_fetch[i : i + 50]
                items = fetch_video_metadata(youtube, batch)
                quota_used += 1

                fetched_ids = {item["id"] for item in items}
                for vid in batch:
                    if vid not in fetched_ids:
                        console.print(
                            f"  [yellow]Warning:[/] Video {vid} not returned by API (private/deleted?)"
                        )
                        counters["errors"] += 1

                for item in items:
                    vid = item["id"]
                    channel, playlist = video_context[vid]
                    url = f"https://www.youtube.com/watch?v={vid}"
                    existing = all_videos.get(url)
                    video = transform_video(item, channel, playlist)
                    if existing and existing.get("publish") is False:
                        video["publish"] = False
                    all_videos[url] = video
                    if existing:
                        counters["updated"] += 1
                    else:
                        counters["new"] += 1

                write_videos(all_videos, output_path)
                progress.advance(task, len(batch))

        existing_videos = all_videos

    # Write final state (includes skipped videos preserved from existing data)
    existing_videos = deduplicate_videos(existing_videos)
    write_videos(existing_videos, output_path)

    # Phase 6: Summary report
    total = len(existing_videos)
    console.print(
        f"\n[bold green]\u2713 Done![/] {total} videos written to {output_path}"
    )
    console.print(
        f"  New: {counters['new']} | Updated: {counters['updated']}"
        f" | Skipped: {counters['skipped']} | Errors: {counters['errors']}"
    )
    console.print(f"  API quota used: ~{quota_used} units\n")


if __name__ == "__main__":
    main()
