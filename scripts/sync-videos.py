#!/usr/bin/env -S uv run
# /// script
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
"""

import re
import sys
import tomllib
from pathlib import Path
from typing import Any

import requests
import yaml
from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
)

console = Console(stderr=True)


# ---------------------------------------------------------------------------
# Shared utilities (mirrored from update-software-frontmatter.py)
# ---------------------------------------------------------------------------


class NoAliasYamlDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def parse_frontmatter(content: str) -> tuple[dict[str, Any], str, str]:
    lines = content.split("\n")

    if not lines or lines[0].strip() != "---":
        return {}, "", content

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        return {}, "", content

    yaml_lines = lines[1:end_idx]
    yaml_section = "\n".join(yaml_lines)

    try:
        frontmatter = yaml.safe_load(yaml_section) or {}
    except yaml.YAMLError as e:
        console.print(f"[yellow]Warning:[/] Failed to parse YAML: {e}")
        return {}, "", content

    remaining_content = "\n".join(lines[end_idx + 1 :])
    return frontmatter, yaml_section, remaining_content


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
    yaml_str = add_comment_after_key(
        yaml_str, "external", "updated automatically, do not edit"
    )

    return yaml_str.strip()


def write_frontmatter(
    file_path: Path, frontmatter: dict[str, Any], remaining_content: str
) -> None:
    yaml_content = format_frontmatter(frontmatter)
    new_content = f"---\n{yaml_content}\n---\n{remaining_content}"
    file_path.write_text(new_content, encoding="utf-8")


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


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------


def load_videos(videos_toml: Path) -> list[dict[str, Any]]:
    with open(videos_toml, "rb") as f:
        data = tomllib.load(f)
    return data.get("videos", [])


def load_names(directory: Path, ignore_slugs: set[str] | None = None) -> list[str]:
    names = []
    for index_file in sorted(directory.glob("*/_index.md")):
        slug = index_file.parent.name
        if ignore_slugs and slug in ignore_slugs:
            continue
        content = index_file.read_text(encoding="utf-8")
        frontmatter, _, _ = parse_frontmatter(content)
        title = frontmatter.get("title", "").strip()
        if title:
            names.append(title)
    return names


def load_software_match_ignore(ignore_toml: Path) -> set[str]:
    if not ignore_toml.exists():
        return set()
    with open(ignore_toml, "rb") as f:
        data = tomllib.load(f)
    return set(data.get("names", []))


# ---------------------------------------------------------------------------
# Filtering
# ---------------------------------------------------------------------------


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


def detect_software(video: dict[str, Any], software_names: list[str]) -> list[str]:
    combined = video.get("title", "") + " " + video.get("description", "")
    return find_matches(combined, software_names)


# ---------------------------------------------------------------------------
# Building external
# ---------------------------------------------------------------------------


def build_external(
    video: dict[str, Any],
    detected_people: list[str],
    detected_software: list[str],
) -> dict[str, Any]:
    fields = [
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
    external: dict[str, Any] = {
        f: video[f] for f in fields if f in video and video[f] is not None
    }
    if "tags" in external and isinstance(external["tags"], list):
        external["tags"] = [re.sub(r"[#?/]", "", t) for t in external["tags"] if re.sub(r"[#?/]", "", t)]
    if detected_people:
        external["people"] = detected_people
    if detected_software:
        external["software"] = detected_software
    return external


# ---------------------------------------------------------------------------
# Thumbnail download
# ---------------------------------------------------------------------------


def download_thumbnail(url: str, dest_dir: Path) -> bool:
    dest = dest_dir / "thumbnail.jpg"
    if dest.exists():
        return False

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        dest.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        console.print(f"  [yellow]Warning:[/] Could not download thumbnail: {e}")
        return False


# ---------------------------------------------------------------------------
# Per-video processing
# ---------------------------------------------------------------------------


def process_video(
    video: dict[str, Any],
    videos_dir: Path,
    people_names: list[str],
    software_names: list[str],
) -> str:
    try:
        slug = video["slug"]
        video_dir = videos_dir / slug
        index_file = video_dir / "_index.md"
        is_new = not video_dir.exists()

        if is_new:
            video_dir.mkdir(parents=True, exist_ok=True)
            frontmatter: dict[str, Any] = {}
            remaining_content = "\n"
        else:
            content = index_file.read_text(encoding="utf-8")
            frontmatter, _, remaining_content = parse_frontmatter(content)

        detected_people = detect_people(video, people_names)
        detected_software = detect_software(video, software_names)

        external = build_external(video, detected_people, detected_software)
        frontmatter["external"] = external

        include = frontmatter.get("include", {})
        exclude = frontmatter.get("exclude", {})
        override = frontmatter.get("override", {})

        top_level = compute_top_level_keys(external, include, exclude, override)

        date_val = video["date"]
        date_str = str(date_val)[:10]

        frontmatter["title"] = top_level.get("title", video["title"])
        frontmatter["resource_type"] = "video"
        frontmatter["date"] = date_str
        frontmatter["description"] = top_level.get("description", video["description"])
        frontmatter["people"] = top_level.get("people", [])
        frontmatter["software"] = top_level.get("software", [])
        frontmatter["tags"] = top_level.get("tags", [])
        if "resources" not in frontmatter:
            frontmatter["resources"] = []

        write_frontmatter(index_file, frontmatter, remaining_content)
        download_thumbnail(video["thumbnail"], video_dir)

        return "created" if is_new else "updated"

    except Exception as e:
        console.print(
            f"  [bold red]Error:[/] Failed to process {video.get('slug', '?')}: {e}"
        )
        return "error"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    console.print("\n[bold blue]Video Syncer[/]\n")

    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    videos_toml = project_root / "data" / "videos.toml"
    videos_dir = project_root / "content" / "resources" / "videos"
    people_dir = project_root / "content" / "people"
    software_dir = project_root / "content" / "software"
    ignore_toml = project_root / "data" / "software-match-ignore.toml"

    for path, label in [
        (videos_toml, "videos TOML"),
        (people_dir, "people directory"),
        (software_dir, "software directory"),
    ]:
        if not path.exists():
            console.print(f"[bold red]Error:[/] {label} not found: {path}")
            sys.exit(1)

    all_videos = load_videos(videos_toml)
    people_names = load_names(people_dir)
    ignore_slugs = load_software_match_ignore(ignore_toml)
    software_names = load_names(software_dir, ignore_slugs=ignore_slugs)

    console.print(
        f"[dim]Loaded {len(all_videos)} videos, "
        f"{len(people_names)} people, "
        f"{len(software_names)} software entries "
        f"({len(ignore_slugs)} ignored)[/]\n"
    )

    videos_dir.mkdir(parents=True, exist_ok=True)

    created = updated = skipped = errors = 0

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Syncing...", total=len(all_videos))

        for video in all_videos:
            slug = video.get("slug", "?")
            progress.update(task, description=f"[cyan]{slug}")

            ok, _ = should_process(video)
            if not ok:
                skipped += 1
                progress.advance(task)
                continue

            result = process_video(video, videos_dir, people_names, software_names)
            if result == "created":
                console.print(f"  [green]✓[/] Created {slug}")
                created += 1
            elif result == "updated":
                console.print(f"  [cyan]↑[/] Updated {slug}")
                updated += 1
            elif result == "error":
                errors += 1

            progress.advance(task)

    console.print("\n[bold]Summary:[/]")
    console.print(f"  [green]✓[/] Created: {created}")
    console.print(f"  [cyan]↑[/] Updated: {updated}")
    console.print(f"  [dim]○[/] Skipped: {skipped}")
    if errors:
        console.print(f"  [red]✗[/] Errors:  {errors}")
        sys.exit(1)

    console.print("\n[bold green]✓ Done![/]\n")


if __name__ == "__main__":
    main()
