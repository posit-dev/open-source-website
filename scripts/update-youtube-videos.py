#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-api-python-client>=2.100.0",
#   "tomli-w>=1.0.0",
#   "python-dotenv>=1.0.0",
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
# ]
# ///

"""
Fetch video metadata from YouTube channels and playlists.

Reads channel names, playlist IDs, and individual video IDs from
data/youtube.toml, fetches metadata via the YouTube Data API v3, and writes
it to data/videos.toml.

Every run fetches metadata for all tracked videos (~40 quota units), but a
video's entry, including its `last_updated` timestamp, only changes when one
of its fields actually changed. View, like, and comment counts change all
the time, so they're only refreshed with --refresh-stats (the nightly
workflow does this once a week); new videos always get them.

Videos that disappear from YouTube are reported but never removed.

Requires YOUTUBE_API_KEY in the environment or .env.

Exit codes: 0 = success, 1 = fatal (nothing written), 2 = partial (a channel
or playlist could not be fetched; everything else was written).
"""

from __future__ import annotations

import argparse
import logging
import os
import re
import sys
import tomllib
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import tomli_w

sys.path.insert(0, str(Path(__file__).resolve().parent))

import videolib  # noqa: E402

log = logging.getLogger("update-youtube-videos")

THUMBNAIL_PREFERENCE = ["maxres", "high", "standard", "medium", "default"]

# Fields that change constantly; only refreshed with --refresh-stats.
STATS_FIELDS = ("view_count", "like_count", "comment_count")
# Bookkeeping fields that never count as a change by themselves.
VOLATILE_FIELDS = ("last_updated",)

API_RETRIES = 3


class FatalError(Exception):
    """Something is wrong enough that videos.toml must not be written."""


# ---------------------------------------------------------------------------
# Pure helpers
# ---------------------------------------------------------------------------


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text


def parse_iso8601_duration(duration: str) -> int:
    match = re.fullmatch(r"P(?:(\d+)D)?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?)?", duration or "")
    if not match:
        return 0
    days, hours, minutes, seconds = (int(g or 0) for g in match.groups())
    return days * 86400 + hours * 3600 + minutes * 60 + seconds


def best_thumbnail(thumbnails: dict) -> str:
    for key in THUMBNAIL_PREFERENCE:
        if key in thumbnails:
            return thumbnails[key]["url"]
    return ""


def transform_video(item: dict, channel: str, playlist: str, now: str) -> dict[str, Any]:
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
        "last_updated": now,
    }


def merge_video(
    existing: dict[str, Any] | None,
    fetched: dict[str, Any],
    *,
    refresh_stats: bool,
    now: str,
) -> tuple[dict[str, Any], list[str], list[str]]:
    """Merge freshly fetched metadata into the stored entry.

    Returns ``(video, changed_fields, changed_stats)``. ``last_updated`` only
    moves when a field changed. Without ``refresh_stats`` the stored counts
    are kept. ``publish = false`` and any keys this script doesn't produce
    (added by hand) are preserved.
    """
    if existing is None:
        return {**fetched, "last_updated": now}, [], []

    merged = dict(fetched)
    for key, value in existing.items():
        merged.setdefault(key, value)
    if existing.get("publish") is False:
        merged["publish"] = False
    if not refresh_stats:
        for f in STATS_FIELDS:
            if f in existing:
                merged[f] = existing[f]

    keys = [k for k in merged if k not in VOLATILE_FIELDS]
    changed = [k for k in keys if k not in STATS_FIELDS and merged.get(k) != existing.get(k)]
    changed_stats = [k for k in keys if k in STATS_FIELDS and merged.get(k) != existing.get(k)]

    if changed or changed_stats:
        merged["last_updated"] = now
    else:
        merged["last_updated"] = existing.get("last_updated", now)
    return merged, changed, changed_stats


def deduplicate_videos(
    videos: dict[str, dict[str, Any]],
    existing_urls: set[str],
) -> tuple[dict[str, dict[str, Any]], list[dict[str, str]]]:
    """Resolve slug collisions deterministically.

    Two videos with the same title on the same day get the same slug. Prefer
    the entry already in videos.toml (so the winner doesn't flip from night
    to night), then the later publish time, then the URL.
    """

    def rank(url: str) -> tuple:
        v = videos[url]
        return (url in existing_urls, v.get("date", ""), url)

    winners: dict[str, str] = {}
    for url, video in videos.items():
        slug = video.get("slug", "")
        if slug not in winners or rank(url) > rank(winners[slug]):
            winners[slug] = url

    keep = set(winners.values())
    result = {url: v for url, v in videos.items() if url in keep}
    discarded = [
        {"url": url, "slug": v.get("slug", ""), "kept": winners[v.get("slug", "")]}
        for url, v in videos.items()
        if url not in keep
    ]
    return result, discarded


def render_videos(videos: dict[str, dict[str, Any]]) -> str:
    videos_list = [{k: v for k, v in video.items() if v is not None} for video in videos.values()]
    return tomli_w.dumps({"videos": videos_list})


# ---------------------------------------------------------------------------
# Files
# ---------------------------------------------------------------------------


def load_youtube_config(config_path: Path) -> dict[str, list[str]]:
    if not config_path.exists():
        raise FatalError(f"Config file not found: {config_path}")
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
    except tomllib.TOMLDecodeError as e:
        # Never continue with an empty list: that would wipe the file.
        raise FatalError(f"Could not parse {output_path}: {e}") from e
    return {v["url"]: v for v in data.get("videos", [])}


# ---------------------------------------------------------------------------
# YouTube API
# ---------------------------------------------------------------------------


class Quota:
    """Rough quota bookkeeping: list calls cost 1 unit each."""

    def __init__(self) -> None:
        self.calls: dict[str, int] = {}

    def add(self, call: str, units: int = 1) -> None:
        self.calls[call] = self.calls.get(call, 0) + units

    @property
    def total(self) -> int:
        return sum(self.calls.values())


def resolve_channel_uploads(youtube: Any, channel_name: str, quota: Quota) -> tuple[str, str] | None:
    for params in [{"forUsername": channel_name}, {"forHandle": f"@{channel_name}"}]:
        quota.add("channels.list")
        resp = (
            youtube.channels()
            .list(part="contentDetails,snippet", **params)
            .execute(num_retries=API_RETRIES)
        )
        if resp.get("items"):
            item = resp["items"][0]
            uploads_id = item["contentDetails"]["relatedPlaylists"]["uploads"]
            title = item["snippet"]["title"]
            log.info("  Resolved channel %r (%s) to uploads playlist %s", channel_name, title, uploads_id)
            return uploads_id, title
        log.debug("  No channel found for %s", params)
    return None


def fetch_playlist_video_ids(youtube: Any, playlist_id: str, quota: Quota) -> list[str]:
    video_ids: list[str] = []
    request = youtube.playlistItems().list(
        part="contentDetails", playlistId=playlist_id, maxResults=50
    )
    while request:
        quota.add("playlistItems.list")
        response = request.execute(num_retries=API_RETRIES)
        for item in response.get("items", []):
            video_ids.append(item["contentDetails"]["videoId"])
        request = youtube.playlistItems().list_next(request, response)
    return video_ids


def fetch_video_metadata(youtube: Any, video_ids: list[str], quota: Quota) -> list[dict]:
    items: list[dict] = []
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i : i + 50]
        quota.add("videos.list")
        resp = (
            youtube.videos()
            .list(part="snippet,contentDetails,statistics", id=",".join(batch))
            .execute(num_retries=API_RETRIES)
        )
        items.extend(resp.get("items", []))
        log.debug("  Fetched metadata batch %d (%d videos)", i // 50 + 1, len(batch))
    return items


def collect_video_ids(
    youtube: Any,
    config: dict[str, list[str]],
    quota: Quota,
    summary: videolib.RunSummary,
) -> dict[str, tuple[str, str]]:
    """Map video id -> (channel title, playlist id) over all sources.

    A source that fails is recorded as an error; if every channel and
    playlist fails, something is wrong globally (API key, quota, network).
    """
    video_context: dict[str, tuple[str, str]] = {}
    sources = len(config["channels"]) + len(config["playlists"])
    failed = 0

    for channel_name in config["channels"]:
        log.info("Channel %s", channel_name)
        try:
            resolved = resolve_channel_uploads(youtube, channel_name, quota)
            if not resolved:
                raise LookupError(f"channel {channel_name!r} not found by username or handle")
            uploads_id, channel_title = resolved
            ids = fetch_playlist_video_ids(youtube, uploads_id, quota)
        except Exception as e:  # noqa: BLE001 - recorded and reported
            failed += 1
            log.error("  Could not fetch channel %s: %s", channel_name, e)
            summary.add("error", reason="source_failed", source=f"channel:{channel_name}", detail=str(e))
            continue
        log.info("  Found %d videos", len(ids))
        for vid in ids:
            video_context.setdefault(vid, (channel_title, ""))

    for playlist_id in config["playlists"]:
        log.info("Playlist %s", playlist_id)
        try:
            ids = fetch_playlist_video_ids(youtube, playlist_id, quota)
        except Exception as e:  # noqa: BLE001 - recorded and reported
            failed += 1
            log.error("  Could not fetch playlist %s: %s", playlist_id, e)
            summary.add("error", reason="source_failed", source=f"playlist:{playlist_id}", detail=str(e))
            continue
        log.info("  Found %d videos", len(ids))
        for vid in ids:
            video_context[vid] = (video_context.get(vid, ("", ""))[0], playlist_id)

    if sources and failed == sources:
        raise FatalError(f"All {sources} channels and playlists failed; check the API key and quota")

    if config["videos"]:
        log.info("Individual videos: %d", len(config["videos"]))
        for vid in config["videos"]:
            if vid in video_context:
                log.debug("  Already tracked: %s", vid)
            else:
                video_context[vid] = ("", "")
                log.info("  Added %s", vid)

    return video_context


# ---------------------------------------------------------------------------
# Core
# ---------------------------------------------------------------------------


def update_videos(
    youtube: Any,
    config: dict[str, list[str]],
    existing: dict[str, dict[str, Any]],
    *,
    refresh_stats: bool,
    summary: videolib.RunSummary,
    now: str | None = None,
) -> dict[str, dict[str, Any]]:
    """Return the new contents of videos.toml, recording results in ``summary``."""
    now = now or datetime.now(timezone.utc).isoformat()
    quota = Quota()

    video_context = collect_video_ids(youtube, config, quota, summary)
    log.info("Total unique videos in sources: %d", len(video_context))

    log.info("Fetching metadata for %d videos", len(video_context))
    items = fetch_video_metadata(youtube, list(video_context), quota)
    fetched_ids = {item["id"] for item in items}

    # Start from the stored order so the file diff stays minimal; new videos
    # are appended.
    videos: dict[str, dict[str, Any]] = dict(existing)
    results: dict[str, dict[str, Any]] = {}  # url -> summary fields

    for item in items:
        vid = item["id"]
        channel, playlist = video_context[vid]
        fetched = transform_video(item, channel, playlist, now)
        url = fetched["url"]
        old = existing.get(url)
        video, changed, changed_stats = merge_video(old, fetched, refresh_stats=refresh_stats, now=now)
        videos[url] = video

        if old is None:
            results[url] = {"status": "new", "slug": video["slug"], "title": video["title"]}
            log.info("New: %s (%s) %r", video["slug"], vid, video["title"])
        elif changed:
            result = {"status": "changed", "slug": video["slug"], "changed_fields": changed}
            if "slug" in changed:
                result["old_slug"] = old.get("slug")
            results[url] = result
            log.info("Changed: %s (%s): %s", video["slug"], vid, ", ".join(changed))
            for f in changed:
                log.debug("  %s: %r -> %r", f, old.get(f), video.get(f))
        elif changed_stats:
            results[url] = {"status": "stats_refreshed"}
        else:
            results[url] = {"status": "unchanged"}

    for vid in video_context:
        if vid not in fetched_ids:
            url = f"https://www.youtube.com/watch?v={vid}"
            stored = existing.get(url, {})
            results[url] = {"status": "unavailable", "slug": stored.get("slug")}
            log.warning("Unavailable: %s is listed but not returned by the API (private or deleted?)", vid)

    source_urls = {f"https://www.youtube.com/watch?v={vid}" for vid in video_context}
    for url, stored in existing.items():
        if url not in source_urls:
            results[url] = {"status": "missing", "slug": stored.get("slug"), "title": stored.get("title")}
            log.warning(
                "Missing: %s (%s) is in videos.toml but no longer in any channel or playlist",
                stored.get("slug"),
                videolib.youtube_id(url),
            )

    videos, discarded = deduplicate_videos(videos, set(existing))
    for d in discarded:
        results[d["url"]] = {"status": "duplicate_slug", "slug": d["slug"], "kept": d["kept"]}
        log.warning("Duplicate slug %s: kept %s, skipped %s", d["slug"], d["kept"], d["url"])

    for url, result in results.items():
        status = result.pop("status")
        if status in ("unchanged", "stats_refreshed"):
            summary.tally(status)
        else:
            summary.add(status, url=url, video_id=videolib.youtube_id(url), **result)

    summary.extra["quota_used"] = quota.total
    summary.extra["quota_calls"] = quota.calls
    summary.extra["videos_in_sources"] = len(video_context)
    log.info("API quota used: ~%d units (%s)", quota.total, quota.calls)
    return videos


def build_youtube_client(project_root: Path) -> Any:
    from dotenv import load_dotenv
    from googleapiclient.discovery import build

    load_dotenv(project_root / ".env")
    key = os.getenv("YOUTUBE_API_KEY")
    if not key:
        raise FatalError("YOUTUBE_API_KEY not found in .env or environment")
    return build("youtube", "v3", developerKey=key, cache_discovery=False)


def main(argv: list[str] | None = None, youtube: Any = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().split("\n\n")[0])
    parser.add_argument(
        "--refresh-stats",
        action="store_true",
        help="also update view, like, and comment counts of existing videos",
    )
    parser.add_argument("--force", "-f", action="store_true", help="alias for --refresh-stats")
    parser.add_argument("--dry-run", action="store_true", help="show what would change; write nothing")
    videolib.add_common_args(parser)
    args = parser.parse_args(argv)
    refresh_stats = args.refresh_stats or args.force

    videolib.setup_logging("update-youtube-videos", args.verbose)
    summary = videolib.RunSummary("update-youtube-videos")
    summary.extra.update(refresh_stats=refresh_stats, dry_run=args.dry_run)

    config_path = args.project_root / "data" / "youtube.toml"
    output_path = args.project_root / "data" / "videos.toml"

    def body() -> None:
        nonlocal youtube
        summary.environment = videolib.log_environment(
            log, packages=["google-api-python-client", "tomli-w"]
        )
        try:
            config = load_youtube_config(config_path)
            log.info("Config: %s", config_path)
            for kind in ("channels", "playlists", "videos"):
                log.info("  %s: %s", kind, ", ".join(config[kind]) or "(none)")
            log.info("Stats: %s", "refreshing" if refresh_stats else "keeping stored counts")

            existing = load_existing_videos(output_path)
            log.info("Loaded %d existing videos from %s", len(existing), output_path)

            if youtube is None:
                youtube = build_youtube_client(args.project_root)

            videos = update_videos(
                youtube, config, existing, refresh_stats=refresh_stats, summary=summary
            )
        except FatalError as e:
            summary.fatal = str(e)
            log.error("%s", e)
            return

        new_text = render_videos(videos)
        old_text = output_path.read_text(encoding="utf-8") if output_path.exists() else None
        if new_text == old_text:
            log.info("%s is unchanged (%d videos)", output_path, len(videos))
        elif args.dry_run:
            log.info("Dry run: would write %d videos to %s", len(videos), output_path)
        else:
            videolib.atomic_write_text(output_path, new_text)
            log.info("Wrote %d videos to %s", len(videos), output_path)
        summary.extra["written"] = new_text != old_text and not args.dry_run

    return videolib.run_main(summary, log, args.summary_json, body)


if __name__ == "__main__":
    sys.exit(main())
