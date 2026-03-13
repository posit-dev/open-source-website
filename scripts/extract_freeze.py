#!/usr/bin/env python3
"""
Extract rendered markdown from Quarto freeze files.

Usage:
    python scripts/extract_freeze.py <post-name>

Example:
    python scripts/extract_freeze.py pointblank-intro
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path


def extract_freeze(post_path: str, base_dir: Path = Path(".")):
    """Extract markdown from a freeze file and convert to hugo-md format.

    Args:
        post_path: Path to post relative to content/posts/ (e.g., "pointblank-intro"
                   or "plotnine/2024/11/version-0.14.0")
        base_dir: Base directory of the Hugo site
    """

    # Freeze file location: _freeze/<path>/index/execute-results/html.json
    freeze_path = base_dir / "_freeze" / post_path / "index" / "execute-results" / "html.json"

    if not freeze_path.exists():
        print(f"Error: Freeze file not found at: {freeze_path}")
        sys.exit(1)

    post_dir = base_dir / "content" / "posts" / post_path
    temp_md = post_dir / "index.md"
    final_md = post_dir / "index.md"
    commonmark_md = post_dir / "index-commonmark.md"

    # Check post directory exists
    if not post_dir.exists():
        print(f"Error: Post directory not found: {post_dir}")
        sys.exit(1)

    # Load freeze file
    print(f"Reading freeze file: {freeze_path}")
    with open(freeze_path) as f:
        data = json.load(f)

    markdown = data["result"]["markdown"]
    supporting = data["result"].get("supporting", [])
    includes = data["result"].get("includes", {})

    # Write extracted markdown to index.md
    with open(temp_md, "w") as f:
        f.write(markdown)
    print(f"Extracted markdown: {len(markdown):,} characters")

    # Run quarto to convert to hugo-md format
    print("Converting to hugo-md format...")
    result = subprocess.run(
        ["quarto", "render", "index.md", "--to", "hugo-md"],
        cwd=post_dir,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Error running quarto: {result.stderr}")
        sys.exit(1)

    # Clean up: remove temp file, rename output
    temp_md.unlink()
    if commonmark_md.exists():
        commonmark_md.rename(final_md)
        print(f"Created: {final_md}")
    else:
        print(f"Error: Expected output file not found: {commonmark_md}")
        sys.exit(1)

    # Copy supporting files (e.g., figure-html/) from freeze directory
    if supporting:
        freeze_parent = freeze_path.parent.parent  # Go up from execute-results/html.json
        for support_name in supporting:
            # Supporting files are referenced as "index_files" but stored without that prefix
            # e.g., "figure-html" in freeze becomes "index_files/figure-html" in post
            if support_name == "index_files":
                # Look for figure-html, libs, etc. in freeze directory
                for subdir in ["figure-html", "libs"]:
                    src = freeze_parent / subdir
                    if src.exists():
                        dest = post_dir / "index_files" / subdir
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        if dest.exists():
                            shutil.rmtree(dest)
                        shutil.copytree(src, dest)
                        print(f"Copied: {src} -> {dest}")
            else:
                # Copy other supporting files directly
                src = freeze_parent / support_name
                if src.exists():
                    dest = post_dir / support_name
                    if src.is_dir():
                        if dest.exists():
                            shutil.rmtree(dest)
                        shutil.copytree(src, dest)
                    else:
                        shutil.copy2(src, dest)
                    print(f"Copied: {src} -> {dest}")

    if includes:
        print(f"Includes: {list(includes.keys())}")
        print("  (These scripts may need to be added to the page)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    post_name = sys.argv[1]
    extract_freeze(post_name)
