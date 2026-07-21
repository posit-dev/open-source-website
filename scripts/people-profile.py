#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "requests>=2.31.0",
# ]
# ///

"""
Create or update a person profile in content/people/.

Each profile is a directory content/people/<id>/ containing an _index.md file
(YAML frontmatter + markdown body) and an image file referenced by the
frontmatter's `image` key. The --image argument accepts either a local file
path (copied in, keeping its name) or an http(s) URL (downloaded and saved as
<id>.<ext>, with the extension derived from the response's Content-Type).

For a new profile, --name and --image are required. If the profile already
exists, every argument other than --id is optional and only the values that are
explicitly provided are updated. Pass the literal value DELETE to clear a field
(e.g. --role DELETE removes the role; --github DELETE empties the handle).
"""

import argparse
import mimetypes
import shutil
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests
import yaml
from rich.console import Console

console = Console(stderr=True)

# Repo layout: this script lives in scripts/, content is a sibling directory.
REPO_ROOT = Path(__file__).resolve().parent.parent
PEOPLE_DIR = REPO_ROOT / "content" / "people"
SOFTWARE_DIR = REPO_ROOT / "content" / "software"

DEFAULT_AFFILIATION = "Posit, PBC"

# Sentinel value: passing this as a flag value clears the field. Always-present
# fields (social keys, affiliation) are reset to "", optional fields (role,
# software) are removed entirely.
DELETE = "DELETE"

# Social keys as they appear in _index.md, alphabetically ordered.
SOCIAL_KEYS = [
    "bluesky",
    "github",
    "linkedin",
    "mastodon",
    "orcid",
    "website",
    "youtube",
]

# Top-level frontmatter keys in canonical order.
TOP_LEVEL_ORDER = ["title", "image", "role", "affiliation", "social", "software"]


class NoAliasYamlDumper(yaml.SafeDumper):
    """YAML dumper that disables anchors and aliases."""

    def ignore_aliases(self, data):
        return True


class QuotedStr(str):
    """A string that should be emitted as a double-quoted YAML scalar."""


def _quoted_str_representer(dumper: yaml.Dumper, data: str) -> yaml.Node:
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style='"')


NoAliasYamlDumper.add_representer(QuotedStr, _quoted_str_representer)


def quote_values(data: Any) -> Any:
    """Recursively wrap string values (not mapping keys) as double-quoted scalars."""
    if isinstance(data, dict):
        return {key: quote_values(value) for key, value in data.items()}
    if isinstance(data, list):
        return [quote_values(item) for item in data]
    if isinstance(data, str):
        return QuotedStr(data)
    return data


def parse_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    """
    Parse YAML frontmatter from markdown content.

    Returns:
        tuple: (frontmatter_dict, body)
    """
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

    yaml_section = "\n".join(lines[1:end_idx])

    try:
        frontmatter = yaml.safe_load(yaml_section) or {}
    except yaml.YAMLError as e:
        console.print(f"[bold red]Error:[/] Failed to parse YAML frontmatter: {e}")
        sys.exit(1)

    # Body is everything after the closing fence; drop a single leading blank line.
    body = "\n".join(lines[end_idx + 1 :])
    if body.startswith("\n"):
        body = body[1:]

    return frontmatter, body


def order_frontmatter(frontmatter: dict[str, Any]) -> dict[str, Any]:
    """Return frontmatter with keys in canonical order (unknown keys kept at end)."""
    ordered: dict[str, Any] = {}
    for key in TOP_LEVEL_ORDER:
        if key in frontmatter:
            value = frontmatter[key]
            if key == "social" and isinstance(value, dict):
                value = {k: value.get(k, "") for k in SOCIAL_KEYS}
            ordered[key] = value
    # Preserve any keys we don't explicitly know about.
    for key, value in frontmatter.items():
        if key not in ordered:
            ordered[key] = value
    return ordered


def format_document(frontmatter: dict[str, Any], body: str) -> str:
    """Serialize frontmatter + body back into an _index.md document."""
    ordered = quote_values(order_frontmatter(frontmatter))

    yaml_str = yaml.dump(
        ordered,
        Dumper=NoAliasYamlDumper,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        indent=2,
    ).strip()

    body = body.rstrip("\n")
    if body:
        return f"---\n{yaml_str}\n---\n\n{body}\n"
    return f"---\n{yaml_str}\n---\n"


def parse_software(raw: str) -> list[str]:
    """Split a comma-separated software string into a cleaned list of slugs."""
    return [slug.strip() for slug in raw.split(",") if slug.strip()]


def validate_software(slugs: list[str]) -> None:
    """Warn (do not fail) for software slugs without a matching content directory."""
    for slug in slugs:
        if not (SOFTWARE_DIR / slug).is_dir():
            console.print(
                f"[yellow]Warning:[/] software slug '{slug}' has no directory "
                f"at content/software/{slug}"
            )


def build_frontmatter(
    args: argparse.Namespace,
    existing: dict[str, Any] | None,
    image_filename: str | None,
) -> dict[str, Any]:
    """Merge provided arguments onto existing frontmatter (or build from scratch)."""
    is_new = existing is None
    frontmatter: dict[str, Any] = dict(existing) if existing else {}

    if args.name is not None:
        frontmatter["title"] = args.name

    if image_filename is not None:
        frontmatter["image"] = image_filename

    if args.role == DELETE:
        frontmatter.pop("role", None)
    elif args.role is not None:
        frontmatter["role"] = args.role

    if args.affiliation == DELETE:
        frontmatter["affiliation"] = ""
    elif args.affiliation is not None:
        frontmatter["affiliation"] = args.affiliation
    elif is_new:
        frontmatter["affiliation"] = DEFAULT_AFFILIATION

    # Social block: keep all seven keys present, defaulting to "".
    social = dict(frontmatter.get("social") or {})
    for key in SOCIAL_KEYS:
        value = getattr(args, key)
        if value == DELETE:
            social[key] = ""
        elif value is not None:
            social[key] = value
        else:
            social.setdefault(key, "")
    frontmatter["social"] = {k: social.get(k, "") for k in SOCIAL_KEYS}

    if args.software == DELETE:
        frontmatter.pop("software", None)
    elif args.software is not None:
        slugs = parse_software(args.software)
        validate_software(slugs)
        if slugs:
            frontmatter["software"] = slugs
        else:
            frontmatter.pop("software", None)

    return frontmatter


# Preferred extensions for common image MIME types (matches repo conventions).
MIME_EXTENSIONS = {
    "image/jpeg": ".jpg",
    "image/jpg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
    "image/gif": ".gif",
    "image/svg+xml": ".svg",
}


def is_url(value: str) -> bool:
    """Return True if the value looks like an http(s) URL."""
    parsed = urlparse(value)
    return parsed.scheme in ("http", "https")


def extension_from_content_type(content_type: str) -> str | None:
    """Map a Content-Type header value to a preferred file extension."""
    mime = content_type.split(";")[0].strip().lower()
    if mime in MIME_EXTENSIONS:
        return MIME_EXTENSIONS[mime]
    return mimetypes.guess_extension(mime) if mime else None


def resolve_image(image: str, profile_id: str, dest_dir: Path, dry_run: bool) -> str:
    """
    Place the image in the profile directory and return its final filename.

    A local path is copied in, keeping its original filename. A URL is
    downloaded and saved as <profile_id>.<ext>, where the extension is derived
    from the response's Content-Type (falling back to the URL path suffix).
    """
    if is_url(image):
        return download_image(image, profile_id, dest_dir, dry_run)
    return copy_image(image, dest_dir, dry_run)


def copy_image(source: str, dest_dir: Path, dry_run: bool) -> str:
    """Copy a local image into the profile directory; return its filename."""
    src = Path(source)
    if not src.is_file():
        console.print(f"[bold red]Error:[/] image file not found: {src}")
        sys.exit(1)

    dest = dest_dir / src.name
    if src.resolve() == dest.resolve():
        console.print(f"[dim]Image already in place: {dest.name}[/]")
        return src.name

    if dry_run:
        console.print(f"[cyan]Would copy image[/] {src} -> {dest}")
        return src.name

    shutil.copy2(src, dest)
    console.print(f"[green]Copied image[/] {src.name} -> {dest}")
    return src.name


def download_image(url: str, profile_id: str, dest_dir: Path, dry_run: bool) -> str:
    """Download an image from a URL to <profile_id>.<ext>; return its filename."""
    try:
        if dry_run:
            # HEAD is enough to inspect the Content-Type without transferring the body.
            response = requests.head(url, timeout=10, allow_redirects=True)
            response.raise_for_status()
            content = None
        else:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            content = response.content
    except requests.RequestException as e:
        console.print(f"[bold red]Error:[/] failed to download image from {url}: {e}")
        sys.exit(1)

    ext = extension_from_content_type(response.headers.get("Content-Type", ""))
    if ext is None:
        # Fall back to the extension in the URL path.
        url_suffix = Path(urlparse(url).path).suffix
        ext = url_suffix if url_suffix else None
    if ext is None:
        console.print(
            f"[bold red]Error:[/] could not determine image extension for {url} "
            f"(Content-Type: {response.headers.get('Content-Type', 'unknown')})"
        )
        sys.exit(1)

    filename = f"{profile_id}{ext}"
    dest = dest_dir / filename

    if dry_run:
        console.print(f"[cyan]Would download image[/] {url} -> {dest}")
        return filename

    dest.write_bytes(content)
    console.print(f"[green]Downloaded image[/] {url} -> {dest}")
    return filename


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create or update a person profile in content/people/.",
        epilog="Pass the literal value DELETE to clear a field (e.g. --role DELETE).",
    )
    parser.add_argument("--id", required=True, help="Directory name under content/people/")
    parser.add_argument("--name", help="Full name (required for new profiles)")
    parser.add_argument(
        "--image",
        help="Image to use (required for new profiles). A local path is copied "
        "in; an http(s) URL is downloaded to <id>.<ext>.",
    )
    parser.add_argument("--role", help="Role/title")
    parser.add_argument(
        "--affiliation",
        help=f'Affiliation (defaults to "{DEFAULT_AFFILIATION}" for new profiles)',
    )
    parser.add_argument("--github", help="GitHub username")
    parser.add_argument("--linkedin", help="LinkedIn username")
    parser.add_argument("--website", help="Website URL")
    parser.add_argument("--bluesky", help="Bluesky handle")
    parser.add_argument(
        "--mastodon",
        help="Mastodon profile URL (used verbatim as the link href, "
        "e.g. https://fosstodon.org/@user)",
    )
    parser.add_argument("--orcid", help="ORCID identifier")
    parser.add_argument(
        "--youtube",
        help="YouTube handle or path (prefixed with https://youtube.com/, "
        "e.g. @user or c/Channel)",
    )
    parser.add_argument("--software", help="Comma-separated software slugs")
    parser.add_argument(
        "--body",
        help='Markdown body (multi-line string). Use "-" to read from STDIN.',
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing files or copying images",
    )
    args = parser.parse_args()

    # Reject ids that aren't a single safe path segment, so the tool can never
    # write outside content/people/ (e.g. --id ../software/foo).
    if args.id != Path(args.id).name or args.id in ("", ".", ".."):
        console.print(
            f"[bold red]Error:[/] --id must be a single directory name, "
            f"got '{args.id}'."
        )
        sys.exit(1)

    # A body of "-" means read the markdown body from STDIN.
    if args.body == "-":
        args.body = sys.stdin.read()

    profile_dir = PEOPLE_DIR / args.id
    index_path = profile_dir / "_index.md"
    is_new = not index_path.exists()

    if is_new:
        missing = [name for name, val in (("--name", args.name), ("--image", args.image)) if val is None]
        if missing:
            console.print(
                f"[bold red]Error:[/] {', '.join(missing)} required when creating a "
                f"new profile ('{args.id}' does not exist yet)."
            )
            sys.exit(1)
        existing_fm: dict[str, Any] | None = None
        body = args.body if args.body is not None else ""
        action = "Created"
    else:
        content = index_path.read_text(encoding="utf-8")
        existing_fm, existing_body = parse_frontmatter(content)
        body = args.body if args.body is not None else existing_body
        action = "Updated"

    # Handle directory + image first, since a downloaded URL's final filename
    # (and extension) is only known after the request completes.
    image_filename: str | None = None
    if args.image is not None:
        if not profile_dir.exists() and not args.dry_run:
            profile_dir.mkdir(parents=True)
            console.print(f"[green]Created directory[/] {profile_dir}")
        elif not profile_dir.exists():
            console.print(f"[cyan]Would create directory[/] {profile_dir}")
        image_filename = resolve_image(args.image, args.id, profile_dir, args.dry_run)

    frontmatter = build_frontmatter(args, existing_fm, image_filename)
    document = format_document(frontmatter, body)

    if args.dry_run:
        console.print(f"\n[cyan]Would write[/] {index_path}:\n")
        console.print(document)
        return

    index_path.write_text(document, encoding="utf-8")
    console.print(f"[bold green]{action}[/] {index_path}")


if __name__ == "__main__":
    main()
