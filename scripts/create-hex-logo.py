#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "rich>=13.0.0",
# ]
# ///

"""
Create a colored hex-placeholder logo for a software project.

Copies static/images/hex-placeholder.svg with a custom fill color
and updates the project's frontmatter accordingly.
"""

import argparse
import re
import sys
from pathlib import Path

from rich.console import Console

console = Console(stderr=True)


def normalize_color(raw: str) -> str:
    """Normalize a hex color string to #RRGGBB format."""
    color = raw.strip().lstrip("#")

    # Expand 3-char shorthand to 6-char
    if len(color) == 3 and all(c in "0123456789abcdefABCDEF" for c in color):
        color = "".join(c * 2 for c in color)

    if len(color) != 6 or not all(c in "0123456789abcdefABCDEF" for c in color):
        console.print(f"[bold red]Error:[/] Invalid hex color: {raw}")
        sys.exit(1)

    return f"#{color.upper()}"


def update_frontmatter(index_file: Path, color: str) -> list[str]:
    """Update frontmatter in _index.md with image and color fields.

    Returns a list of actions taken.
    """
    text = index_file.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    actions = []

    # Find the first and second --- delimiters
    fence_indices = [i for i, line in enumerate(lines) if line.rstrip() == "---"]
    if len(fence_indices) < 2:
        console.print(f"[bold red]Error:[/] Could not parse frontmatter in {index_file}")
        sys.exit(1)

    first_fence = fence_indices[0]
    second_fence = fence_indices[1]
    frontmatter_lines = lines[first_fence + 1 : second_fence]

    has_image = any(re.match(r"^image:", line) for line in frontmatter_lines)
    has_color = any(re.match(r"^color:", line) for line in frontmatter_lines)

    if has_image:
        console.print(
            f"[yellow]Warning:[/] image field already exists in {index_file.name}, "
            "skipping image update"
        )
        if not has_color:
            # Insert color after the image line
            image_idx = next(
                i
                for i, line in enumerate(lines[first_fence + 1 : second_fence])
                if re.match(r"^image:", line)
            ) + first_fence + 1
            color_line = f'color: "{color}"\n'
            lines.insert(image_idx + 1, color_line)
            actions.append(f'Inserted color: "{color}"')
    else:
        # Insert image and color after the first ---
        image_line = "image: logo.svg\n"
        color_line = f'color: "{color}"\n'
        lines.insert(first_fence + 1, color_line)
        lines.insert(first_fence + 1, image_line)
        actions.append("Inserted image: logo.svg")
        actions.append(f'Inserted color: "{color}"')

    if has_color and not actions:
        console.print(
            f"[yellow]Warning:[/] color field already exists in {index_file.name}, "
            "skipping color update"
        )

    if actions:
        index_file.write_text("".join(lines), encoding="utf-8")

    return actions


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a colored hex-placeholder logo for a software project."
    )
    parser.add_argument(
        "--software",
        required=True,
        help="Software directory name (e.g. 'actions')",
    )
    parser.add_argument(
        "--color",
        required=True,
        help="Hex color (e.g. '#4388C6' or '4388C6')",
    )
    args = parser.parse_args()

    color = normalize_color(args.color)

    # Resolve paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    software_dir = project_root / "content" / "software" / args.software
    index_file = software_dir / "_index.md"
    placeholder_svg = project_root / "static" / "images" / "hex-placeholder.svg"
    output_svg = software_dir / "logo.svg"

    console.print(f"\n[bold blue]Hex Logo Creator[/]\n")

    # Validate software directory
    if not index_file.exists():
        console.print(
            f"[bold red]Error:[/] Software not found: {index_file}"
        )
        sys.exit(1)

    # Read placeholder SVG
    if not placeholder_svg.exists():
        console.print(
            f"[bold red]Error:[/] Placeholder SVG not found: {placeholder_svg}"
        )
        sys.exit(1)

    svg_content = placeholder_svg.read_text(encoding="utf-8")

    # Replace fill color
    svg_content = svg_content.replace('fill="#666666"', f'fill="{color}"')

    # Write output SVG
    output_svg.write_text(svg_content, encoding="utf-8")
    console.print(f"  [green]✓[/] Created {output_svg.relative_to(project_root)}")

    # Update frontmatter
    actions = update_frontmatter(index_file, color)
    for action in actions:
        console.print(f"  [green]✓[/] {action} in {index_file.relative_to(project_root)}")

    if not actions:
        console.print(f"  [dim]○[/] No frontmatter changes needed")

    console.print(f"\n[bold green]✓ Done![/]\n")


if __name__ == "__main__":
    main()
