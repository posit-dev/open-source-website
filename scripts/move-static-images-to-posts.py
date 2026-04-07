#!/usr/bin/env python3
"""
Move images from static/ into their post directories and update references.

Handles these root-relative path patterns:
  /blog-images/<filename>         → static/blog-images/<filename>
  /blog/images/<filename>         → static/blog/images/<filename>
  /assets/img/<filename>          → static/assets/img/<filename>
  /post/<path>/<filename>         → static/post/<path>/<filename>
"""

import re
import shutil
import sys
from pathlib import Path

BLOG_DIR = Path("content/blog/rstudio")
STATIC_DIR = Path("static")

# Map root-relative prefix → static subdirectory
STATIC_PREFIXES = [
    ("/blog-images/", STATIC_DIR / "blog-images"),
    ("/blog/images/", STATIC_DIR / "blog" / "images"),
    ("/assets/img/", STATIC_DIR / "assets" / "img"),
    ("/post/", STATIC_DIR / "post"),
]

# Regex to find root-relative image paths in src= or markdown ![]()
IMAGE_PATTERN = re.compile(
    r'(?:src=["\'](/(?:blog-images|blog/images|assets/img|post)/[^"\'>\s)]+)["\']'
    r'|!\[[^\]]*\]\((/(?:blog-images|blog/images|assets/img|post)/[^)\s]+)\))'
)


def find_static_source(img_path: str) -> Path | None:
    """Given a root-relative path like /blog-images/foo.png, find it in static/."""
    for prefix, static_subdir in STATIC_PREFIXES:
        if img_path.startswith(prefix):
            rel = img_path[len(prefix):]
            candidate = static_subdir / rel
            if candidate.exists():
                return candidate
    return None


def process_file(src_file: Path, post_dir: Path, dry_run: bool = False) -> int:
    """Process a single source file, moving images and updating paths. Returns count of fixes."""
    content = src_file.read_text(encoding="utf-8")
    new_content = content
    fixes = 0

    for match in IMAGE_PATTERN.finditer(content):
        img_path = match.group(1) or match.group(2)
        static_src = find_static_source(img_path)

        if static_src is None:
            print(f"  WARN: static source not found for {img_path} in {src_file}", file=sys.stderr)
            continue

        # Determine filename (preserve subdirectory structure after the prefix for /post/)
        for prefix, _ in STATIC_PREFIXES:
            if img_path.startswith(prefix):
                rel_within_prefix = img_path[len(prefix):]
                break

        dest = post_dir / rel_within_prefix
        new_ref = rel_within_prefix  # relative reference to use in the file

        if not dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            if not dest.exists():
                shutil.copy2(static_src, dest)

        # Replace in content: both src="..." and ![](...) forms
        old_src_attr = f'src="{img_path}"'
        new_src_attr = f'src="{new_ref}"'
        old_src_attr2 = f"src='{img_path}'"
        new_src_attr2 = f"src='{new_ref}'"
        # Markdown form: could be ](/path) or (]/path ) etc
        old_md = f"]({img_path})"
        new_md = f"]({new_ref})"
        old_md_attrs = f"({img_path})"
        new_md_attrs = f"({new_ref})"

        before = new_content
        new_content = new_content.replace(old_src_attr, new_src_attr)
        new_content = new_content.replace(old_src_attr2, new_src_attr2)
        new_content = new_content.replace(old_md, new_md)
        new_content = new_content.replace(old_md_attrs, new_md_attrs)

        if new_content != before:
            fixes += 1
            action = "DRY RUN" if dry_run else "FIXED"
            print(f"  {action}: {img_path} → {new_ref}")

    if not dry_run and new_content != content:
        src_file.write_text(new_content, encoding="utf-8")

    return fixes


def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("DRY RUN — no files will be modified\n")

    total_fixes = 0
    extensions = {".md", ".html", ".Rmd", ".Rmarkdown"}

    for post_dir in sorted(BLOG_DIR.iterdir()):
        if not post_dir.is_dir():
            continue

        post_fixes = 0
        for src_file in post_dir.iterdir():
            if src_file.suffix in extensions:
                fixes = process_file(src_file, post_dir, dry_run=dry_run)
                post_fixes += fixes

        if post_fixes:
            print(f"{post_dir.name}: {post_fixes} image(s) moved")
            total_fixes += post_fixes

    print(f"\nTotal: {total_fixes} image reference(s) updated")

    if not dry_run:
        print("\nNow remove the static directories if all images were moved:")
        print("  rm -rf static/blog-images static/blog/images static/assets/img static/post")


if __name__ == "__main__":
    main()
