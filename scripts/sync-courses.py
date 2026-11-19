#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "requests>=2.28.0",
# ]
# ///

"""
Sync courses and learning paths from Posit Academy into content/resources/courses/.

The source of truth is the "All Courses" catalog page on academy.posit.co
(https://academy.posit.co/page/all-courses), read through the Skilljar API.
Hidden items, separators, and templates are skipped.

For each course or learning path, creates or updates a directory named after
its Academy slug containing an _index.md and the promo image. Synced values
live in the `external` block; adjust the top-level values with include,
exclude, and override blocks, which are preserved. The page body is the
Academy long description, minus call-to-action buttons, and is overwritten on
every sync.

Directories are matched to Academy items by `external.id`, so a changed slug
renames the directory, and an item that is no longer listed is deleted.
Directories without `external.id` are never touched.

Requires the SKILLJAR_API_KEY environment variable.

Usage:
    ./scripts/sync-courses.py            # Sync and write changes
    ./scripts/sync-courses.py --dry-run  # Show what would change
"""

import argparse
import os
import re
import shutil
import sys
import tomllib
from pathlib import Path
from typing import Any

import requests
import yaml
from rich.console import Console

console = Console(stderr=True)

API_BASE = "https://api.skilljar.com/v1"
DOMAIN = "academy.posit.co"
CATALOG_PAGE_SLUG = "all-courses"
SKIP_TITLE_PREFIXES = ("[separator]", "[template]")

# Top-level keys derived from `external` that include/exclude/override can adjust.
MERGED_KEYS = ["title", "description", "software", "duration"]


# ---------------------------------------------------------------------------
# Shared utilities (mirrored from sync-videos.py)
# ---------------------------------------------------------------------------


class NoAliasYamlDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def parse_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    lines = content.split("\n")

    if not lines or lines[0].strip() != "---":
        return {}, content

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        return {}, content

    try:
        frontmatter = yaml.safe_load("\n".join(lines[1:end_idx])) or {}
    except yaml.YAMLError as e:
        console.print(f"[yellow]Warning:[/] Failed to parse YAML: {e}")
        return {}, content

    return frontmatter, "\n".join(lines[end_idx + 1 :])


def sort_dict_with_keys_at_end(data: Any, keys_at_end: list[str]) -> Any:
    if isinstance(data, dict):
        regular_keys = sorted(k for k in data if k not in keys_at_end)
        end_keys = [k for k in keys_at_end if k in data]
        return {
            k: sort_dict_with_keys_at_end(data[k], keys_at_end)
            for k in regular_keys + end_keys
        }
    elif isinstance(data, list):
        return [sort_dict_with_keys_at_end(item, keys_at_end) for item in data]
    else:
        return data


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

    lines = []
    for line in yaml_str.split("\n"):
        key_name = line.split(":")[0] if line and not line.startswith(" ") else ""
        if key_name in keys_at_end and lines and lines[-1] != "":
            lines.append("")
        if key_name == "external":
            line = f"{line}  # updated automatically, do not edit"
        lines.append(line)

    return "\n".join(lines).strip()


def render_index(frontmatter: dict[str, Any], body: str) -> str:
    body = f"\n{body}\n" if body else ""
    return f"---\n{format_frontmatter(frontmatter)}\n---\n{body}"


def compute_top_level_keys(
    external: dict[str, Any],
    include: dict[str, Any],
    exclude: dict[str, Any],
    override: dict[str, Any],
) -> dict[str, Any]:
    result = {}

    for key in MERGED_KEYS:
        value = external.get(key)

        if isinstance(include.get(key), list):
            value = list(value) if isinstance(value, list) else []
            value.extend(include[key])
            seen: set = set()
            value = [x for x in value if not (x in seen or seen.add(x))]

        if isinstance(value, list) and isinstance(exclude.get(key), list):
            value = [x for x in value if x not in exclude[key]]

        if key in override:
            value = override[key]

        if value is not None:
            result[key] = value

    return result


# ---------------------------------------------------------------------------
# Skilljar API
# ---------------------------------------------------------------------------


class Skilljar:
    def __init__(self, api_key: str):
        self.session = requests.Session()
        self.session.auth = (api_key, "")

    def get(self, path: str) -> dict[str, Any]:
        response = self.session.get(f"{API_BASE}/{path}", timeout=30)
        response.raise_for_status()
        return response.json()

    def get_all(self, path: str) -> list[dict[str, Any]]:
        results = []
        url: str | None = f"{API_BASE}/{path}?page_size=100"
        while url:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            data = response.json()
            results.extend(data["results"])
            url = data.get("next")
        return results


def clean_html(html: str) -> str:
    html = html.replace("\r\n", "\n").replace("\r", "\n")
    # Drop call-to-action buttons (e.g. "Download the One Pager"), which Academy
    # writes as a paragraph holding a single link. The page links to Academy instead.
    html = re.sub(r"<p>\s*<a\b[^>]*>.*?</a>\s*</p>\n?", "", html, flags=re.DOTALL)
    return html.strip()


def skip_reason(title: str, hidden: bool) -> str | None:
    if hidden:
        return "hidden"
    if title.strip().lower().startswith(SKIP_TITLE_PREFIXES):
        return "separator or template"
    return None


def fetch_catalog(api: Skilljar) -> list[dict[str, Any]]:
    """Return the courses and learning paths on the All Courses page, in order."""
    domain = f"domains/{DOMAIN}"

    pages = api.get_all(f"{domain}/catalog-pages")
    page = next((p for p in pages if p["slug"] == CATALOG_PAGE_SLUG), None)
    if page is None:
        raise RuntimeError(f"Catalog page '{CATALOG_PAGE_SLUG}' not found")

    page_items = api.get_all(f"{domain}/catalog-pages/{page['id']}/classic-page-items")
    published_courses = {p["id"]: p for p in api.get_all(f"{domain}/published-courses")}
    courses = {c["id"]: c for c in api.get_all("courses")}

    items = []
    for page_item in sorted(page_items, key=lambda i: i["order"]):
        if page_item["type"] == "PUBLISHED_COURSE":
            published = published_courses.get(page_item["item_published_course_id"])
            if published is None:
                console.print(f"  [yellow]Warning:[/] Unknown published course {page_item['item_published_course_id']}")
                continue
            course = courses.get(published["course"]["id"], {})
            title = course.get("title") or published["course"]["title"]
            reason = skip_reason(title, published["hidden"])
            if reason:
                console.print(f"  [dim]○ Skipped {title} ({reason})[/]")
                continue
            items.append({
                "id": published["id"],
                "kind": "course",
                "slug": published["slug"],
                "title": title,
                "description": course.get("short_description", ""),
                "body": clean_html(course.get("long_description_html", "")),
                "url": published["course_url"],
                "image_url": course.get("promo_image_url", ""),
                "duration": course.get("course_time") or course.get("manual_course_time") or "",
                "labels": course.get("labels", []),
                "created_at": course.get("created_at", ""),
                "modified_at": course.get("modified_at", ""),
            })

        elif page_item["type"] == "PUBLISHED_PATH":
            path_id = page_item["item_published_path_id"]
            published = api.get(f"{domain}/published-paths/{path_id}")
            path = published["path"]
            reason = skip_reason(path["title"], published["hidden"])
            if reason:
                console.print(f"  [dim]○ Skipped {path['title']} ({reason})[/]")
                continue
            path_items = api.get_all(f"{domain}/published-paths/{path_id}/path-items")
            items.append({
                "id": published["id"],
                "kind": "learning path",
                "slug": published["slug"],
                "title": path["title"],
                "description": path.get("short_description", ""),
                "body": clean_html(path.get("long_description_html", "")),
                "url": published["path_url"],
                "image_url": path.get("promo_image_url", ""),
                "path_courses": [
                    i["published_course"]["slug"]
                    for i in sorted(path_items, key=lambda i: i["order"])
                    if i.get("published_course")
                ],
                "created_at": published.get("created_at", ""),
                "modified_at": published.get("modified_at", ""),
            })

        else:
            console.print(f"  [dim]○ Skipped catalog item of type {page_item['type']}[/]")

    for order, item in enumerate(items, start=1):
        item["order"] = order

    # Only link path members that are themselves synced.
    synced_slugs = {i["slug"] for i in items}
    for item in items:
        if "path_courses" in item:
            item["path_courses"] = [s for s in item["path_courses"] if s in synced_slugs]

    return items


# ---------------------------------------------------------------------------
# Software detection
# ---------------------------------------------------------------------------


def load_software_titles(software_dir: Path, ignore_toml: Path) -> dict[str, str]:
    ignore: set[str] = set()
    if ignore_toml.exists():
        with open(ignore_toml, "rb") as f:
            ignore = set(tomllib.load(f).get("names", []))

    titles = {}
    for index_file in sorted(software_dir.glob("*/_index.md")):
        slug = index_file.parent.name
        if slug in ignore:
            continue
        frontmatter, _ = parse_frontmatter(index_file.read_text(encoding="utf-8"))
        title = str(frontmatter.get("title", "")).strip()
        if title:
            titles[slug] = title
    return titles


def detect_software(item: dict[str, Any], software_titles: dict[str, str]) -> list[str]:
    # Match on display titles but return slugs, since Hugo builds
    # /software/<term>/ from the stored value.
    text = f"{item['title']} {item['description']} {item['body']}"
    text = re.sub(r"<[^>]+>", " ", text)
    return [
        slug
        for slug, title in software_titles.items()
        if re.search(r"(?<!\w)" + re.escape(title) + r"(?!\w)", text, flags=re.IGNORECASE)
    ]


# ---------------------------------------------------------------------------
# Building pages
# ---------------------------------------------------------------------------


def image_filename(url: str) -> str:
    suffix = Path(url.split("?")[0]).suffix.lower() or ".png"
    return f"image{suffix}"


def build_external(item: dict[str, Any], software: list[str]) -> dict[str, Any]:
    external = {
        "id": item["id"],
        "kind": item["kind"],
        "slug": item["slug"],
        "title": item["title"],
        "description": item["description"],
        "url": item["url"],
        "image_url": item["image_url"],
        "order": item["order"],
        "created_at": item["created_at"],
        "modified_at": item["modified_at"],
    }
    if item.get("duration"):
        external["duration"] = item["duration"]
    if item.get("labels"):
        external["labels"] = item["labels"]
    if "path_courses" in item:
        external["courses"] = item["path_courses"]
    if software:
        external["software"] = software
    return external


def build_frontmatter(
    item: dict[str, Any], existing: dict[str, Any], software: list[str]
) -> dict[str, Any]:
    frontmatter = dict(existing)
    external = build_external(item, software)
    frontmatter["external"] = external

    include = frontmatter.get("include", {}) or {}
    exclude = frontmatter.get("exclude", {}) or {}
    override = frontmatter.get("override", {}) or {}
    top_level = compute_top_level_keys(external, include, exclude, override)

    frontmatter["title"] = top_level.get("title", item["title"])
    frontmatter["description"] = top_level.get("description", item["description"])
    frontmatter["resource_type"] = "course"
    frontmatter["course_type"] = item["kind"]
    frontmatter["date"] = str(override.get("date", item["created_at"]))[:10]
    frontmatter["software"] = top_level.get("software", [])
    frontmatter["academy_url"] = item["url"]
    frontmatter["weight"] = item["order"]
    if top_level.get("duration"):
        frontmatter["duration"] = top_level["duration"]
    else:
        frontmatter.pop("duration", None)
    if "path_courses" in item:
        frontmatter["courses"] = item["path_courses"]
    else:
        frontmatter.pop("courses", None)
    if item["image_url"]:
        frontmatter["image"] = image_filename(item["image_url"])
    else:
        frontmatter.pop("image", None)

    return frontmatter


def describe_changes(
    old: dict[str, Any], new: dict[str, Any], old_body: str, new_body: str
) -> list[str]:
    def short(value: Any) -> str:
        text = str(value).replace("\n", " ")
        return text if len(text) <= 60 else text[:57] + "..."

    changes = []
    for key in sorted(set(old) | set(new)):
        if key == "external":
            continue
        if old.get(key) != new.get(key):
            changes.append(f"{key}: [red]{short(old.get(key, '—'))}[/] → [green]{short(new.get(key, '—'))}[/]")

    # Skip external keys mirrored at the top level, which are reported above.
    mirrored = {*MERGED_KEYS, "slug", "order", "url", "courses", "modified_at"}
    old_ext, new_ext = old.get("external", {}) or {}, new.get("external", {}) or {}
    for key in sorted(set(old_ext) | set(new_ext)):
        if key in mirrored or old_ext.get(key) == new_ext.get(key):
            continue
        changes.append(f"external.{key}: [red]{short(old_ext.get(key, '—'))}[/] → [green]{short(new_ext.get(key, '—'))}[/]")

    if old_body.strip() != new_body.strip():
        changes.append("body (long description)")

    return changes


def download_image(url: str, dest: Path) -> None:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    dest.write_bytes(response.content)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def load_existing(courses_dir: Path) -> tuple[dict[str, Path], list[Path]]:
    """Map Academy ids to existing directories, and list unmanaged directories."""
    managed: dict[str, Path] = {}
    unmanaged = []
    for index_file in sorted(courses_dir.glob("*/_index.md")):
        frontmatter, _ = parse_frontmatter(index_file.read_text(encoding="utf-8"))
        academy_id = (frontmatter.get("external") or {}).get("id")
        if academy_id:
            managed[academy_id] = index_file.parent
        else:
            unmanaged.append(index_file.parent)
    return managed, unmanaged


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--dry-run", action="store_true", help="show changes without writing anything")
    args = parser.parse_args()

    console.print("\n[bold blue]Posit Academy Course Syncer[/]")
    if args.dry_run:
        console.print("[yellow]Dry run: no files will be written[/]")

    api_key = os.environ.get("SKILLJAR_API_KEY")
    if not api_key:
        console.print("[bold red]Error:[/] SKILLJAR_API_KEY is not set")
        sys.exit(1)

    root = Path(__file__).resolve().parent.parent
    courses_dir = root / "content" / "resources" / "courses"
    software_titles = load_software_titles(
        root / "content" / "software", root / "data" / "software-match-ignore.toml"
    )

    console.print(f"\n[bold]Fetching catalog from {DOMAIN}/page/{CATALOG_PAGE_SLUG}[/]")
    try:
        items = fetch_catalog(Skilljar(api_key))
    except (requests.RequestException, RuntimeError, KeyError) as e:
        console.print(f"[bold red]Error:[/] Failed to fetch catalog: {e}")
        sys.exit(1)

    # Never wipe the section because of an API hiccup.
    if not items:
        console.print("[bold red]Error:[/] Catalog is empty; refusing to sync")
        sys.exit(1)

    n_paths = sum(1 for i in items if i["kind"] == "learning path")
    console.print(f"  Found {len(items) - n_paths} courses and {n_paths} learning paths")

    managed, unmanaged = load_existing(courses_dir) if courses_dir.exists() else ({}, [])
    counts = {"created": 0, "updated": 0, "renamed": 0, "deleted": 0, "unchanged": 0, "errors": 0}

    console.print("\n[bold]Syncing[/]")
    for item in items:
        slug = item["slug"]
        label = f"{item['title']} [dim]({slug}, {item['kind']})[/]"
        try:
            item_dir = courses_dir / slug
            old_dir = managed.get(item["id"])

            if old_dir and old_dir != item_dir:
                if item_dir.exists():
                    raise RuntimeError(f"cannot rename {old_dir.name}: {slug} already exists")
                console.print(f"  [magenta]⇢ Renamed[/] {label}: {old_dir.name} → {slug}")
                counts["renamed"] += 1
                if not args.dry_run:
                    old_dir.rename(item_dir)
                else:
                    item_dir = old_dir  # read the old files below

            index_file = item_dir / "_index.md"
            is_new = not index_file.exists()
            if is_new:
                existing, old_body = {}, ""
            else:
                existing, old_body = parse_frontmatter(index_file.read_text(encoding="utf-8"))

            frontmatter = build_frontmatter(item, existing, detect_software(item, software_titles))
            new_content = render_index(frontmatter, item["body"])

            image = frontmatter.get("image")
            old_image_url = (existing.get("external") or {}).get("image_url")
            needs_image = bool(image) and (
                is_new or old_image_url != item["image_url"] or not (item_dir / image).exists()
            )
            needs_index = is_new or index_file.read_text(encoding="utf-8") != new_content

            if is_new:
                console.print(f"  [green]✓ Created[/] {label}")
                counts["created"] += 1
            elif needs_index or needs_image:
                console.print(f"  [cyan]↑ Updated[/] {label}")
                for change in describe_changes(existing, frontmatter, old_body, item["body"]):
                    console.print(f"      {change}")
                if needs_image and not needs_index:
                    console.print("      image file missing")
                counts["updated"] += 1
            else:
                counts["unchanged"] += 1
                continue

            if args.dry_run:
                continue

            item_dir.mkdir(parents=True, exist_ok=True)
            if needs_image:
                # Remove a stale image with a different extension.
                old_image = existing.get("image")
                if old_image and old_image != image and (item_dir / old_image).exists():
                    (item_dir / old_image).unlink()
                download_image(item["image_url"], item_dir / image)
            index_file.write_text(new_content, encoding="utf-8")

        except Exception as e:
            console.print(f"  [bold red]✗ Error[/] {label}: {e}")
            counts["errors"] += 1

    synced_ids = {i["id"] for i in items}
    for academy_id, item_dir in managed.items():
        if academy_id in synced_ids:
            continue
        frontmatter, _ = parse_frontmatter((item_dir / "_index.md").read_text(encoding="utf-8"))
        console.print(f"  [red]✗ Deleted[/] {frontmatter.get('title', '')} [dim]({item_dir.name})[/]")
        counts["deleted"] += 1
        if not args.dry_run:
            shutil.rmtree(item_dir)

    for item_dir in unmanaged:
        console.print(f"  [yellow]Warning:[/] {item_dir.name} has no external.id; left untouched")

    console.print("\n[bold]Summary:[/]")
    console.print(f"  [green]✓[/] Created:   {counts['created']}")
    console.print(f"  [cyan]↑[/] Updated:   {counts['updated']}")
    console.print(f"  [magenta]⇢[/] Renamed:   {counts['renamed']}")
    console.print(f"  [red]✗[/] Deleted:   {counts['deleted']}")
    console.print(f"  [dim]○[/] Unchanged: {counts['unchanged']}")
    if counts["errors"]:
        console.print(f"  [bold red]![/] Errors:    {counts['errors']}")
        sys.exit(1)

    console.print(f"\n[bold green]✓ Done{' (dry run)' if args.dry_run else ''}![/]\n")


if __name__ == "__main__":
    main()
