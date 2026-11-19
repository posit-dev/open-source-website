#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "requests>=2.28.0",
# ]
# ///

"""
Sync video entries from data/videos.toml into content/resources/videos/.

For each video with publish=true, creates or updates a directory named after
its slug containing an _index.md with YAML frontmatter and a thumbnail.jpg.
People and software mentioned in the title or description are auto-detected
and can be adjusted with include/exclude/override blocks in the _index.md.
When a video's slug changes (e.g., because its title changed), the existing
directory is renamed, or merged into the new one, and references are updated.

Files are only written when their content changes, so a run without changes
on YouTube leaves the working tree untouched. The thumbnail is downloaded
again when its URL changes.

Exit codes: 0 = success, 1 = fatal (nothing written), 2 = partial (some
videos failed; the rest was written).
"""

from __future__ import annotations

import argparse
import logging
import re
import shutil
import sys
import time
import tomllib
from pathlib import Path
from typing import Any, Callable

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

import videolib  # noqa: E402

log = logging.getLogger("sync-videos")

THUMBNAIL_ATTEMPTS = 2

parse_frontmatter = videolib.split_frontmatter


# ---------------------------------------------------------------------------
# Frontmatter formatting (mirrored from update-software-frontmatter.py; the
# output must stay byte-for-byte stable, or every page shows up as changed)
# ---------------------------------------------------------------------------


class NoAliasYamlDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def sort_dict_with_keys_at_end(data: Any, keys_at_end: list[str]) -> Any:
    if isinstance(data, dict):
        regular_keys = []
        end_keys_present = []

        for key in data.keys():
            if key in keys_at_end:
                end_keys_present.append(key)
            else:
                regular_keys.append(key)

        regular_keys.sort()
        end_keys_ordered = [key for key in keys_at_end if key in end_keys_present]

        sorted_dict = {}
        for key in regular_keys + end_keys_ordered:
            sorted_dict[key] = sort_dict_with_keys_at_end(data[key], keys_at_end)

        return sorted_dict
    elif isinstance(data, list):
        return [sort_dict_with_keys_at_end(item, keys_at_end) for item in data]
    else:
        return data


def add_blank_lines_before_keys(yaml_str: str, keys: list[str]) -> str:
    lines = yaml_str.split("\n")
    result = []

    for i, line in enumerate(lines):
        if line and not line.startswith(" "):
            key_name = line.split(":")[0] if ":" in line else ""
            if key_name in keys:
                if i > 0 and result and result[-1] != "":
                    result.append("")
        result.append(line)

    return "\n".join(result)


def add_comment_after_key(yaml_str: str, key: str, comment: str) -> str:
    lines = yaml_str.split("\n")
    result = []

    for line in lines:
        if line and not line.startswith(" "):
            key_name = line.split(":")[0] if ":" in line else ""
            if key_name == key:
                result.append(f"{line}  # {comment}")
                continue
        result.append(line)

    return "\n".join(result)


def format_frontmatter(frontmatter: dict[str, Any]) -> str:
    keys_at_end = ["include", "exclude", "override", "external"]
    sorted_frontmatter = sort_dict_with_keys_at_end(frontmatter, keys_at_end)

    yaml_str = yaml.dump(
        sorted_frontmatter,
        Dumper=NoAliasYamlDumper,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        indent=2,
        width=float("inf"),
    )

    yaml_str = add_blank_lines_before_keys(yaml_str, keys_at_end)
    yaml_str = add_comment_after_key(yaml_str, "external", "updated automatically, do not edit")

    return yaml_str.strip()


def render_index(frontmatter: dict[str, Any], remaining_content: str) -> str:
    return f"---\n{format_frontmatter(frontmatter)}\n---\n{remaining_content}"


def write_frontmatter(file_path: Path, frontmatter: dict[str, Any], remaining_content: str) -> None:
    videolib.atomic_write_text(file_path, render_index(frontmatter, remaining_content))


def compute_top_level_keys(
    external: dict[str, Any],
    include: dict[str, Any],
    exclude: dict[str, Any],
    override: dict[str, Any],
) -> dict[str, Any]:
    result = {}
    keys_to_process = ["title", "people", "software", "description", "tags"]

    for key in keys_to_process:
        value = external.get(key)

        if key in include:
            include_items = include.get(key, [])
            if isinstance(include_items, list):
                if not isinstance(value, list):
                    value = []
                value = list(value)
                value.extend(include_items)
                seen: set = set()
                value = [x for x in value if not (x in seen or seen.add(x))]

        if isinstance(value, list) and key in exclude:
            exclude_items = exclude.get(key, [])
            if isinstance(exclude_items, list):
                value = [x for x in value if x not in exclude_items]

        if key in override:
            value = override[key]

        if value is not None:
            result[key] = value

    return result


def changed_keys(old: dict[str, Any], new: dict[str, Any]) -> list[str]:
    """Top-level keys that differ, with ``external.<key>`` for the synced block."""
    changes = []
    for key in sorted(set(old) | set(new)):
        if key == "external":
            old_ext = old.get("external") or {}
            new_ext = new.get("external") or {}
            changes += [
                f"external.{k}"
                for k in sorted(set(old_ext) | set(new_ext))
                if old_ext.get(k) != new_ext.get(k)
            ]
        elif old.get(key) != new.get(key):
            changes.append(key)
    return changes


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------


def load_videos(videos_toml: Path) -> list[dict[str, Any]]:
    with open(videos_toml, "rb") as f:
        data = tomllib.load(f)
    return data.get("videos", [])


def load_titles_by_slug(directory: Path, ignore_slugs: set[str] | None = None) -> dict[str, str]:
    titles = {}
    for index_file in sorted(directory.glob("*/_index.md")):
        slug = index_file.parent.name
        if ignore_slugs and slug in ignore_slugs:
            continue
        frontmatter, _, _ = parse_frontmatter(index_file.read_text(encoding="utf-8"))
        title = str(frontmatter.get("title", "")).strip()
        if title:
            titles[slug] = title
    return titles


def load_software_match_ignore(ignore_toml: Path) -> set[str]:
    if not ignore_toml.exists():
        return set()
    with open(ignore_toml, "rb") as f:
        data = tomllib.load(f)
    return set(data.get("names", []))


def should_process(video: dict[str, Any]) -> tuple[bool, str]:
    if video.get("publish") is False:
        return False, "publish=false"
    return True, "ok"


# ---------------------------------------------------------------------------
# People and software detection
# ---------------------------------------------------------------------------


def find_matches(text: str, names: list[str]) -> list[str]:
    matched = []
    for name in names:
        pattern = r"(?<!\w)" + re.escape(name) + r"(?!\w)"
        if re.search(pattern, text, flags=re.IGNORECASE):
            matched.append(name)
    return matched


def detect_people(video: dict[str, Any], people_names: list[str]) -> list[str]:
    combined = video.get("title", "") + " " + video.get("description", "")
    return find_matches(combined, people_names)


def detect_software(video: dict[str, Any], software_titles: dict[str, str]) -> list[str]:
    # Match on display titles but return slugs, since Hugo builds
    # /software/<term>/ from the stored value.
    combined = video.get("title", "") + " " + video.get("description", "")
    return [slug for slug, title in software_titles.items() if find_matches(combined, [title])]


# ---------------------------------------------------------------------------
# Building external
# ---------------------------------------------------------------------------

EXTERNAL_FIELDS = [
    "url",
    "title",
    "date",
    "description",
    "duration",
    "channel",
    "playlist",
    "tags",
    "view_count",
    "like_count",
    "comment_count",
    "thumbnail",
    "language",
    "has_captions",
    "definition",
    "last_updated",
]


def build_external(
    video: dict[str, Any],
    detected_people: list[str],
    detected_software: list[str],
) -> dict[str, Any]:
    external: dict[str, Any] = {
        f: video[f] for f in EXTERNAL_FIELDS if f in video and video[f] is not None
    }
    if "tags" in external and isinstance(external["tags"], list):
        external["tags"] = [
            re.sub(r"[#?/]", "", t) for t in external["tags"] if re.sub(r"[#?/]", "", t)
        ]
    if detected_people:
        external["people"] = detected_people
    if detected_software:
        external["software"] = detected_software
    return external


def build_frontmatter(
    video: dict[str, Any],
    frontmatter: dict[str, Any],
    people_names: list[str],
    software_titles: dict[str, str],
) -> dict[str, Any]:
    """Return the new frontmatter for ``video``, given the current one."""
    frontmatter = dict(frontmatter)
    external = build_external(
        video, detect_people(video, people_names), detect_software(video, software_titles)
    )
    frontmatter["external"] = external

    include = frontmatter.get("include", {})
    exclude = frontmatter.get("exclude", {})
    override = frontmatter.get("override", {})
    top_level = compute_top_level_keys(external, include, exclude, override)

    if "date" in override:
        date_str = str(override["date"])[:10]
    else:
        date_str = str(video["date"])[:10]

    frontmatter["title"] = top_level.get("title", video["title"])
    frontmatter["resource_type"] = "video"
    frontmatter["date"] = date_str
    frontmatter["description"] = top_level.get("description", video["description"])
    frontmatter["people"] = top_level.get("people", [])
    frontmatter["software"] = top_level.get("software", [])
    frontmatter["tags"] = top_level.get("tags", [])
    frontmatter["image"] = "thumbnail.jpg"
    if "resources" not in frontmatter:
        frontmatter["resources"] = []
    return frontmatter


# ---------------------------------------------------------------------------
# Renamed videos
# ---------------------------------------------------------------------------


def merge_video_dirs(old_dir: Path, new_dir: Path) -> list[str]:
    """Move files and manual blocks the new directory lacks; remove the old one.

    Returns the names of the files that were moved.
    """
    moved = []
    for item in sorted(old_dir.iterdir()):
        if item.name != "_index.md" and not (new_dir / item.name).exists():
            shutil.move(str(item), new_dir / item.name)
            moved.append(item.name)

    old_frontmatter, _, _ = parse_frontmatter((old_dir / "_index.md").read_text(encoding="utf-8"))
    new_index = new_dir / "_index.md"
    new_frontmatter, _, remaining_content = parse_frontmatter(new_index.read_text(encoding="utf-8"))
    merged = False
    for key in ["include", "exclude", "override", "resources"]:
        if old_frontmatter.get(key) and not new_frontmatter.get(key):
            new_frontmatter[key] = old_frontmatter[key]
            merged = True
    if merged:
        write_frontmatter(new_index, new_frontmatter, remaining_content)

    shutil.rmtree(old_dir)
    return moved


def update_video_references(content_dir: Path, old_slug: str, new_slug: str) -> list[Path]:
    pattern = re.compile(r"videos/" + re.escape(old_slug) + r"(?![\w-])")
    updated = []
    for md_file in sorted(content_dir.rglob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        new_text = pattern.sub(f"videos/{new_slug}", text)
        if new_text != text:
            videolib.atomic_write_text(md_file, new_text)
            updated.append(md_file)
    return updated


def handle_renamed_videos(
    videos: list[dict[str, Any]],
    videos_dir: Path,
    content_dir: Path,
    summary: videolib.RunSummary,
    *,
    dry_run: bool = False,
) -> None:
    # Slugs are derived from YouTube titles, so a title change produces a new
    # slug. Match directories to videos by URL and move or merge stale ones.
    slug_by_url = {v["url"]: v["slug"] for v in videos if "url" in v}
    current_slugs = set(slug_by_url.values())

    for index_file in sorted(videos_dir.glob("*/_index.md")):
        old_dir = index_file.parent
        old_slug = old_dir.name
        if old_slug in current_slugs:
            continue

        frontmatter, _, _ = parse_frontmatter(index_file.read_text(encoding="utf-8"))
        url = (frontmatter.get("external") or {}).get("url")
        new_slug = slug_by_url.get(url)
        if not new_slug:
            log.warning("Orphan: %s is not in videos.toml (or not published); leaving it as is", old_slug)
            summary.add("orphan", slug=old_slug, url=url, video_id=videolib.youtube_id(url))
            continue

        new_dir = videos_dir / new_slug
        action = "merged" if new_dir.exists() else "renamed"
        log.info("%s %s -> %s (%s)", "Merging" if action == "merged" else "Renaming", old_slug, new_slug, videolib.youtube_id(url))
        if dry_run:
            summary.add("renamed", action=action, old_slug=old_slug, slug=new_slug, url=url, video_id=videolib.youtube_id(url), dry_run=True)
            continue

        moved = None
        if action == "merged":
            moved = merge_video_dirs(old_dir, new_dir)
            log.info("  Moved files: %s", ", ".join(moved) or "(none)")
        else:
            old_dir.rename(new_dir)

        updated = update_video_references(content_dir, old_slug, new_slug)
        for md_file in updated:
            log.info("  Updated reference in %s", md_file.relative_to(content_dir.parent))
        summary.add(
            "renamed",
            action=action,
            old_slug=old_slug,
            slug=new_slug,
            url=url,
            video_id=videolib.youtube_id(url),
            moved_files=moved,
            updated_references=[str(p.relative_to(content_dir.parent)) for p in updated],
        )


# ---------------------------------------------------------------------------
# Thumbnail download
# ---------------------------------------------------------------------------


def download_thumbnail(
    url: str,
    dest: Path,
    http_get: Callable[..., Any],
    *,
    attempts: int = THUMBNAIL_ATTEMPTS,
    retry_delay: float = 2.0,
) -> None:
    """Download ``url`` to ``dest`` atomically; raise after ``attempts`` tries."""
    for attempt in range(1, attempts + 1):
        try:
            response = http_get(url, timeout=15)
            response.raise_for_status()
            videolib.atomic_write_bytes(dest, response.content)
            return
        except Exception as e:
            if attempt == attempts:
                raise
            log.warning("  Thumbnail download failed (attempt %d/%d): %s; retrying", attempt, attempts, e)
            time.sleep(retry_delay)


# ---------------------------------------------------------------------------
# Per-video processing
# ---------------------------------------------------------------------------


def process_video(
    video: dict[str, Any],
    videos_dir: Path,
    people_names: list[str],
    software_titles: dict[str, str],
    *,
    http_get: Callable[..., Any],
    dry_run: bool = False,
    retry_delay: float = 2.0,
) -> dict[str, Any]:
    """Create or update one video directory; return a summary item."""
    slug = video["slug"]
    video_dir = videos_dir / slug
    index_file = video_dir / "_index.md"
    is_new = not index_file.exists()

    if is_new:
        old_frontmatter: dict[str, Any] = {}
        remaining_content = "\n"
        old_text = None
    else:
        old_text = index_file.read_text(encoding="utf-8")
        old_frontmatter, _, remaining_content = parse_frontmatter(old_text)

    frontmatter = build_frontmatter(video, old_frontmatter, people_names, software_titles)
    new_text = render_index(frontmatter, remaining_content)

    result: dict[str, Any] = {"slug": slug, "url": video.get("url"), "video_id": videolib.youtube_id(video.get("url"))}
    if is_new:
        result["status"] = "created"
        result["title"] = frontmatter["title"]
    elif new_text != old_text:
        result["status"] = "updated"
        result["changes"] = changed_keys(old_frontmatter, frontmatter)
    else:
        result["status"] = "unchanged"

    if new_text != old_text and not dry_run:
        video_dir.mkdir(parents=True, exist_ok=True)
        videolib.atomic_write_text(index_file, new_text)

    thumbnail = video_dir / "thumbnail.jpg"
    old_thumbnail_url = (old_frontmatter.get("external") or {}).get("thumbnail")
    thumbnail_url = video.get("thumbnail")
    if thumbnail_url and (not thumbnail.exists() or (old_thumbnail_url and old_thumbnail_url != thumbnail_url)):
        reason = "missing" if not thumbnail.exists() else "url changed"
        if dry_run:
            result["thumbnail"] = f"would download ({reason})"
        else:
            try:
                video_dir.mkdir(parents=True, exist_ok=True)
                download_thumbnail(thumbnail_url, thumbnail, http_get, retry_delay=retry_delay)
                result["thumbnail"] = f"downloaded ({reason})"
                log.debug("  Downloaded thumbnail for %s (%s)", slug, reason)
            except Exception as e:  # noqa: BLE001 - recorded as an item error
                result["status"] = "error"
                result["reason"] = "thumbnail_failed"
                result["detail"] = f"{type(e).__name__}: {e} ({thumbnail_url})"
    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None, http_get: Callable[..., Any] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().split("\n\n")[0])
    parser.add_argument("--dry-run", action="store_true", help="show what would change; write nothing")
    videolib.add_common_args(parser)
    args = parser.parse_args(argv)

    videolib.setup_logging("sync-videos", args.verbose)
    summary = videolib.RunSummary("sync-videos")
    summary.extra["dry_run"] = args.dry_run

    root = args.project_root
    videos_toml = root / "data" / "videos.toml"
    videos_dir = root / "content" / "resources" / "videos"
    people_dir = root / "content" / "people"
    software_dir = root / "content" / "software"
    ignore_toml = root / "data" / "software-match-ignore.toml"

    def body() -> None:
        nonlocal http_get
        summary.environment = videolib.log_environment(log, packages=["pyyaml", "requests"])
        for path, label in [
            (videos_toml, "videos TOML"),
            (people_dir, "people directory"),
            (software_dir, "software directory"),
        ]:
            if not path.exists():
                summary.fatal = f"{label} not found: {path}"
                return
        if http_get is None:
            import requests

            http_get = requests.get

        all_videos = load_videos(videos_toml)
        people_names = list(load_titles_by_slug(people_dir).values())
        ignore_slugs = load_software_match_ignore(ignore_toml)
        software_titles = load_titles_by_slug(software_dir, ignore_slugs=ignore_slugs)
        log.info(
            "Loaded %d videos, %d people, %d software entries (%d ignored)",
            len(all_videos),
            len(people_names),
            len(software_titles),
            len(ignore_slugs),
        )

        published = [v for v in all_videos if should_process(v)[0]]
        summary.tally("unpublished", len(all_videos) - len(published))

        videos_dir.mkdir(parents=True, exist_ok=True)
        handle_renamed_videos(published, videos_dir, root / "content", summary, dry_run=args.dry_run)

        with videolib.make_progress() as progress:
            task = progress.add_task("Syncing", total=len(published))
            for video in published:
                progress.update(task, description=video.get("slug", "?"))
                try:
                    result = process_video(
                        video, videos_dir, people_names, software_titles, http_get=http_get, dry_run=args.dry_run
                    )
                except Exception as e:  # noqa: BLE001 - recorded as an item error
                    log.exception("Failed to process %s", video.get("slug", "?"))
                    result = {
                        "status": "error",
                        "slug": video.get("slug"),
                        "video_id": videolib.youtube_id(video.get("url")),
                        "reason": "exception",
                        "detail": f"{type(e).__name__}: {e}",
                    }
                status = result.pop("status")
                if status == "created":
                    log.info("Created %s (%s)", result["slug"], result["video_id"])
                elif status == "updated":
                    log.info("Updated %s (%s): %s", result["slug"], result["video_id"], ", ".join(result["changes"]))
                elif status == "error":
                    log.error("Error %s (%s): %s", result["slug"], result.get("video_id"), result.get("detail"))
                if "thumbnail" in result:
                    log.info("  Thumbnail %s: %s", result["slug"], result["thumbnail"])

                if status == "unchanged" and "thumbnail" not in result:
                    summary.tally("unchanged")
                else:
                    summary.add(status, **result)
                progress.advance(task)

    return videolib.run_main(summary, log, args.summary_json, body)


if __name__ == "__main__":
    sys.exit(main())
