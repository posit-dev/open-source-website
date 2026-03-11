#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "pyyaml>=6.0",
#   "colorthief>=0.2.1",
#   "rich>=13.0.0",
# ]
# ///

"""
Extract dominant colors from software logos and add them to frontmatter.

For each software project with a raster or SVG image, extracts colors
(via ColorThief for raster, XML/CSS parsing for SVG), filters out
achromatic colors, and inserts a `color` field into the YAML frontmatter
directly after the `image:` line.
"""

import colorsys
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml
from colorthief import ColorThief
from rich.console import Console
from rich.table import Table

console = Console(stderr=True)


def parse_frontmatter(content: str) -> tuple[dict | None, str]:
    """Parse YAML frontmatter from markdown content.

    Returns (frontmatter_dict, yaml_section) or (None, "") on failure.
    """
    lines = content.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, ""

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        return None, ""

    yaml_section = "\n".join(lines[1:end_idx])
    try:
        frontmatter = yaml.safe_load(yaml_section) or {}
    except yaml.YAMLError:
        return None, ""

    return frontmatter, yaml_section


def rgb_to_hex(r: int, g: int, b: int) -> str:
    return f"#{r:02X}{g:02X}{b:02X}"


def is_chromatic(r: int, g: int, b: int) -> bool:
    """Return True if the color is sufficiently chromatic (not too gray/white/black)."""
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
    if s < 0.20:
        return False
    if v < 0.15:
        return False
    if v > 0.95 and s < 0.10:
        return False
    return True


def extract_color(image_path: Path) -> str | None:
    """Extract the first chromatic color from an image palette."""
    try:
        ct = ColorThief(str(image_path))
        palette = ct.get_palette(color_count=8, quality=1)
    except Exception:
        return None

    for r, g, b in palette:
        if is_chromatic(r, g, b):
            return rgb_to_hex(r, g, b)

    return None


def parse_hex_color(s: str) -> tuple[int, int, int] | None:
    """Parse a hex color string like '#RRGGBB' or '#RGB' to (R, G, B)."""
    s = s.strip().lstrip("#")
    if len(s) == 3:
        s = s[0] * 2 + s[1] * 2 + s[2] * 2
    if len(s) != 6:
        return None
    try:
        return int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16)
    except ValueError:
        return None


def parse_rgb_func(s: str) -> tuple[int, int, int] | None:
    """Parse 'rgb(R, G, B)' to (R, G, B)."""
    m = re.match(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", s.strip())
    if not m:
        return None
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def parse_color_value(s: str) -> tuple[int, int, int] | None:
    """Parse a CSS/SVG color value (hex or rgb()) to (R, G, B)."""
    s = s.strip()
    if s.startswith("#"):
        return parse_hex_color(s)
    if s.startswith("rgb("):
        return parse_rgb_func(s)
    return None


# Regex for hex colors and rgb() in CSS style blocks
_CSS_COLOR_RE = re.compile(
    r"(?:fill|stroke|stop-color)\s*:\s*"
    r"(#[0-9a-fA-F]{3,6}|rgb\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\))"
)

SVG_NS = "{http://www.w3.org/2000/svg}"


def extract_color_from_svg(image_path: Path) -> str | None:
    """Extract the first chromatic color from an SVG by parsing XML and CSS."""
    try:
        tree = ET.parse(image_path)
    except ET.ParseError:
        return None

    root = tree.getroot()
    colors: list[tuple[int, int, int]] = []

    # 1) Extract colors from <style> blocks (CSS classes)
    for style_el in root.iter(f"{SVG_NS}style"):
        if style_el.text:
            for m in _CSS_COLOR_RE.finditer(style_el.text):
                rgb = parse_color_value(m.group(1))
                if rgb:
                    colors.append(rgb)
    # Also try without namespace (some SVGs omit it)
    for style_el in root.iter("style"):
        if style_el.text:
            for m in _CSS_COLOR_RE.finditer(style_el.text):
                rgb = parse_color_value(m.group(1))
                if rgb:
                    colors.append(rgb)

    # 2) Extract direct fill/stroke attributes from elements
    for el in root.iter():
        for attr in ("fill", "stroke"):
            val = el.get(attr, "")
            if val and not val.startswith("url(") and val != "none":
                rgb = parse_color_value(val)
                if rgb:
                    colors.append(rgb)

    # 3) Extract gradient stop-color attributes
    for stop in root.iter(f"{SVG_NS}stop"):
        sc = stop.get("stop-color", "")
        if sc:
            rgb = parse_color_value(sc)
            if rgb:
                colors.append(rgb)
    for stop in root.iter("stop"):
        sc = stop.get("stop-color", "")
        if sc:
            rgb = parse_color_value(sc)
            if rgb:
                colors.append(rgb)

    # Deduplicate while preserving order
    seen = set()
    unique: list[tuple[int, int, int]] = []
    for c in colors:
        if c not in seen:
            seen.add(c)
            unique.append(c)

    # Return first chromatic color
    for r, g, b in unique:
        if is_chromatic(r, g, b):
            return rgb_to_hex(r, g, b)

    return None


def insert_color_after_image(content: str, hex_color: str) -> str:
    """Insert a `color:` line directly after the `image:` line in raw file text."""
    lines = content.split("\n")
    result = []
    for line in lines:
        result.append(line)
        if line.startswith("image:"):
            result.append(f'color: "{hex_color}"')
    return "\n".join(result)


def main() -> None:
    console.print("\n[bold blue]Software Color Extractor[/]\n")

    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    software_dir = project_root / "content" / "software"

    index_files = sorted(software_dir.glob("*/_index.md"))
    console.print(f"[dim]Found {len(index_files)} software directories[/]\n")

    table = Table(title="Color Extraction Results")
    table.add_column("Project", style="cyan")
    table.add_column("Image")
    table.add_column("Color")
    table.add_column("Status")

    added = 0
    skipped = 0
    no_color = 0

    for index_file in index_files:
        name = index_file.parent.name
        content = index_file.read_text(encoding="utf-8")
        frontmatter, _ = parse_frontmatter(content)

        if frontmatter is None:
            table.add_row(name, "-", "-", "[dim]skipped (no frontmatter)[/]")
            skipped += 1
            continue

        if "color" in frontmatter:
            table.add_row(name, "-", frontmatter["color"], "[dim]skipped (has color)[/]")
            skipped += 1
            continue

        image = frontmatter.get("image")
        if not image:
            table.add_row(name, "-", "-", "[dim]skipped (no image)[/]")
            skipped += 1
            continue

        image_path = index_file.parent / image
        if not image_path.exists():
            table.add_row(name, image, "-", "[dim]skipped (file missing)[/]")
            skipped += 1
            continue

        if str(image).endswith(".svg"):
            hex_color = extract_color_from_svg(image_path)
        else:
            hex_color = extract_color(image_path)
        if hex_color is None:
            table.add_row(name, image, "-", "[yellow]no suitable color[/]")
            no_color += 1
            continue

        new_content = insert_color_after_image(content, hex_color)
        index_file.write_text(new_content, encoding="utf-8")

        swatch = f"[on {hex_color}]  [/]"
        table.add_row(name, image, f"{swatch} {hex_color}", "[green]added[/]")
        added += 1

    console.print(table)
    console.print(f"\n[bold]Summary:[/]")
    console.print(f"  [green]✓[/] Added:           {added}")
    console.print(f"  [dim]○[/] Skipped:          {skipped}")
    console.print(f"  [yellow]○[/] No suitable color: {no_color}")
    console.print(f"\n[bold green]✓ Done![/]\n")


if __name__ == "__main__":
    main()
