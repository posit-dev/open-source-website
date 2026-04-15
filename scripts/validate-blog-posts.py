#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
# ]
# ///

"""Validate blog post frontmatter and placement.

Checks that posts have required metadata, use valid taxonomy values,
and are correctly placed in the content directory.

Usage:
  scripts/validate-blog-posts.py                     # check all posts
  scripts/validate-blog-posts.py content/blog/x/index.md  # check specific posts
  scripts/validate-blog-posts.py --strict             # treat warnings as errors
"""

import argparse
import datetime
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from rich.console import Console

console = Console(stderr=True)

REQUIRED_FIELDS = [
    "title",
    "date",
    "people",
    "description",
    "image",
    "image-alt",
    "topics",
]

COMMON_LANGUAGES = ["R", "Python", "Julia"]

FORBIDDEN_FIELDS = {
    "categories": "`topics`",
}


@dataclass
class Issue:
    file: Path
    message: str
    level: str  # "error" or "warning"


@dataclass
class ValidationContext:
    project_root: Path
    valid_topics: list[str] = field(default_factory=list)
    valid_software: set[str] = field(default_factory=set)
    valid_people_slugs: set[str] = field(default_factory=set)


def parse_frontmatter(content: str) -> dict[str, Any] | None:
    """Parse YAML frontmatter from markdown content. Returns None on failure."""
    lines = content.split("\n")

    if not lines or lines[0].strip() != "---":
        return None

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        return None

    yaml_section = "\n".join(lines[1:end_idx])
    try:
        return yaml.safe_load(yaml_section) or {}
    except yaml.YAMLError:
        return None


def build_context(project_root: Path) -> ValidationContext:
    """Load valid taxonomy values from the project."""
    ctx = ValidationContext(project_root=project_root)

    # Topics from data/topics.yaml
    topics_file = project_root / "data" / "topics.yaml"
    if topics_file.exists():
        ctx.valid_topics = yaml.safe_load(topics_file.read_text()) or []

    # Software folder names
    software_dir = project_root / "content" / "software"
    if software_dir.exists():
        ctx.valid_software = {
            d.name for d in software_dir.iterdir() if d.is_dir()
        }

    # People folder names
    people_dir = project_root / "content" / "people"
    if people_dir.exists():
        ctx.valid_people_slugs = {
            d.name for d in people_dir.iterdir() if d.is_dir()
        }

    return ctx


def slugify(name: str) -> str:
    """Convert a person's name to a directory slug, matching Hugo's behavior."""
    # Hugo preserves Unicode (accents, etc.) — only lowercase and replace
    # non-alphanumeric characters (including Unicode letters) with hyphens.
    return re.sub(r"[^\w]+", "-", name.lower(), flags=re.UNICODE).strip("-")


def is_ported(fm: dict) -> bool:
    return "ported_from" in fm


def is_port_complete(fm: dict) -> bool:
    return fm.get("port_status") in ("complete", "review")


def severity(fm: dict) -> str:
    """Return 'error' for new posts and completed ports, 'warning' for in-progress ports."""
    if not is_ported(fm):
        return "error"
    if is_port_complete(fm):
        return "error"
    return "warning"


# --- Individual checks ---


def check_placement(
    post_path: Path, fm: dict, ctx: ValidationContext
) -> list[Issue]:
    blog_dir = ctx.project_root / "content" / "blog"
    rel = post_path.parent.relative_to(blog_dir)
    depth = len(rel.parts)
    if depth > 1 and not is_ported(fm):
        return [
            Issue(
                post_path,
                f"Post must be at top level of `content/blog/`, not nested in `{rel}`.",
                "error",
            )
        ]
    return []


def check_required_fields(
    post_path: Path, fm: dict, ctx: ValidationContext
) -> list[Issue]:
    issues = []
    sev = severity(fm)
    for field_name in REQUIRED_FIELDS:
        if field_name not in fm or fm[field_name] is None:
            issues.append(
                Issue(post_path, f"`{field_name}` is required but missing.", sev)
            )
    return issues


def check_forbidden_fields(
    post_path: Path, fm: dict, ctx: ValidationContext
) -> list[Issue]:
    issues = []
    for field_name, replacement in FORBIDDEN_FIELDS.items():
        if field_name in fm:
            issues.append(
                Issue(
                    post_path,
                    f"`{field_name}` must not be used. Did you mean {replacement}?",
                    "error",
                )
            )
    return issues


def check_date_format(
    post_path: Path, fm: dict, ctx: ValidationContext
) -> list[Issue]:
    date_val = fm.get("date")
    if date_val is None:
        return []  # handled by required fields check

    sev = severity(fm)

    # yaml.safe_load may parse dates into date/datetime objects
    if isinstance(date_val, datetime.date) and not isinstance(
        date_val, datetime.datetime
    ):
        return []  # plain date object — valid

    if isinstance(date_val, datetime.datetime):
        return [
            Issue(
                post_path,
                f"`date` must be YYYY-MM-DD, not a timestamp. Found: `{date_val}`.",
                sev,
            )
        ]

    if isinstance(date_val, str):
        try:
            datetime.date.fromisoformat(date_val)
            return []
        except ValueError:
            pass
        return [
            Issue(
                post_path,
                f"`date` must be YYYY-MM-DD, not `{date_val}`.",
                sev,
            )
        ]

    return [
        Issue(
            post_path,
            f"`date` must be a string, not {type(date_val).__name__}.",
            sev,
        )
    ]


def check_topics(
    post_path: Path, fm: dict, ctx: ValidationContext
) -> list[Issue]:
    topics = fm.get("topics")
    if not topics:
        return []  # handled by required fields

    if isinstance(topics, str):
        topics = [topics]

    if not isinstance(topics, list):
        return [Issue(post_path, "`topics` must be a list or string.", "error")]

    issues = []
    sev = severity(fm)
    for t in topics:
        if t not in ctx.valid_topics:
            valid_str = ", ".join(ctx.valid_topics)
            issues.append(
                Issue(
                    post_path,
                    f"`{t}` is not a valid topic. Must be one of: {valid_str}.",
                    sev,
                )
            )
    return issues


def check_software(
    post_path: Path, fm: dict, ctx: ValidationContext
) -> list[Issue]:
    software = fm.get("software")
    if not software:
        return [
            Issue(
                post_path,
                "`software` is missing. Use folder names from `content/software/`.",
                "warning",
            )
        ]

    if isinstance(software, str):
        software = [software]

    if not isinstance(software, list):
        return [Issue(post_path, "`software` must be a list or string.", "error")]

    issues = []
    sev = severity(fm)
    for s in software:
        if s not in ctx.valid_software:
            issues.append(
                Issue(
                    post_path,
                    f"Can't find software `{s}`. No matching folder in `content/software/`.",
                    sev,
                )
            )
    return issues


def check_people(
    post_path: Path, fm: dict, ctx: ValidationContext
) -> list[Issue]:
    people = fm.get("people")
    if not people:
        return []

    if isinstance(people, str):
        people = [people]

    if not isinstance(people, list):
        return [Issue(post_path, "`people` must be a list or string.", "error")]

    issues = []
    for person in people:
        if not isinstance(person, str):
            continue
        if "team" in person.lower():
            issues.append(
                Issue(
                    post_path,
                    f"`{person}` looks like a team name. Use individual names instead.",
                    "warning",
                )
            )
        slug = slugify(person)
        if slug and slug not in ctx.valid_people_slugs:
            issues.append(
                Issue(
                    post_path,
                    f"Can't find people page for `{person}` (expected `content/people/{slug}/`).",
                    "warning",
                )
            )
    return issues


def check_image_exists(
    post_path: Path, fm: dict, ctx: ValidationContext
) -> list[Issue]:
    image = fm.get("image")
    if not image or not isinstance(image, str):
        return []

    if image.startswith("http://") or image.startswith("https://"):
        return []

    image_path = post_path.parent / image
    if not image_path.exists():
        return [
            Issue(
                post_path,
                f"Can't find image `{image}`.",
                "error",
            )
        ]
    return []


def check_languages(
    post_path: Path, fm: dict, ctx: ValidationContext
) -> list[Issue]:
    languages = fm.get("languages")
    if not languages:
        options = ", ".join(COMMON_LANGUAGES)
        return [
            Issue(
                post_path,
                f"`languages` is missing. Common values: {options}.",
                "warning",
            )
        ]
    return []


ALL_CHECKS = [
    check_placement,
    check_required_fields,
    check_forbidden_fields,
    check_date_format,
    check_topics,
    check_software,
    check_people,
    check_languages,
    check_image_exists,
]


def collect_posts(
    project_root: Path, explicit_files: list[str]
) -> list[Path]:
    """Collect post files to validate."""
    if explicit_files:
        return [Path(f).resolve() for f in explicit_files]

    blog_dir = project_root / "content" / "blog"
    posts = sorted(blog_dir.rglob("index.md"))
    # Filter out non-post files
    return [p for p in posts if p.name == "index.md"]


def display_issues(all_issues: list[Issue], strict: bool) -> tuple[int, int]:
    """Display issues grouped by file. Returns (error_count, warning_count)."""
    errors = 0
    warnings = 0

    by_file: dict[Path, list[Issue]] = {}
    for issue in all_issues:
        by_file.setdefault(issue.file, []).append(issue)

    for file_path, issues in by_file.items():
        console.print(f"\n[bold]{file_path}[/bold]")
        for issue in issues:
            if issue.level == "error":
                errors += 1
                console.print(f"  [bold red]ERROR[/]  {issue.message}")
            else:
                warnings += 1
                console.print(f"  [yellow]WARN[/]   {issue.message}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate blog post frontmatter and placement."
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Specific index.md files to check (default: all posts)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors",
    )
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    ctx = build_context(project_root)

    posts = collect_posts(project_root, args.files)
    if not posts:
        console.print("[yellow]No blog posts found to validate.[/]")
        return 0

    all_issues: list[Issue] = []

    for post_path in posts:
        content = post_path.read_text()
        fm = parse_frontmatter(content)
        if fm is None:
            all_issues.append(
                Issue(post_path, "Can't parse YAML frontmatter.", "error")
            )
            continue

        for check in ALL_CHECKS:
            all_issues.extend(check(post_path, fm, ctx))

    errors, warnings = display_issues(all_issues, args.strict)

    console.print()
    total = len(posts)
    if errors == 0 and warnings == 0:
        console.print(f"[green]All {total} posts passed validation.[/]")
        return 0

    parts = [f"{total} files checked"]
    if errors:
        parts.append(f"[bold red]{errors} errors[/]")
    if warnings:
        parts.append(f"[yellow]{warnings} warnings[/]")
    console.print(f"Summary: {', '.join(parts)}")

    if errors > 0 or (args.strict and warnings > 0):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
