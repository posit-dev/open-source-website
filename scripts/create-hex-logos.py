#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "rich>=13.0.0",
# ]
# ///

"""
Create hex-placeholder logos for all software projects missing an image.

Iterates over content/software/*/​_index.md, skips any that already have an
image: field, and calls scripts/create-hex-logo.py with a randomly chosen color.
"""

import random
import re
import subprocess
import sys
from pathlib import Path

from rich.console import Console

console = Console(stderr=True)

COLORS = [
    "#447099",
    "#404041",
    "#d44000",
    "#ee6331",
    "#e7b10a",
    "#72994e",
    "#419599",
    "#9a4665",
]


def has_image_field(index_file: Path) -> bool:
    """Check whether the frontmatter already contains an image: field."""
    for line in index_file.read_text(encoding="utf-8").splitlines():
        if line.rstrip() == "---":
            continue
        if re.match(r"^image:", line):
            return True
        # Stop at end of frontmatter
        if line.rstrip() == "---":
            break
    return False


def main() -> None:
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    software_dir = project_root / "content" / "software"
    hex_logo_script = script_dir / "create-hex-logo.py"

    console.print("\n[bold blue]Batch Hex Logo Creator[/]\n")

    # Collect software directories missing an image
    missing = []
    for index_file in sorted(software_dir.glob("*/_index.md")):
        if not has_image_field(index_file):
            missing.append(index_file.parent.name)

    if not missing:
        console.print("[green]All software projects already have an image.[/]\n")
        return

    console.print(f"[cyan]Found {len(missing)} software projects without an image[/]\n")

    created = 0
    failed = 0

    for name in missing:
        color = random.choice(COLORS)
        result = subprocess.run(
            [sys.executable, str(hex_logo_script), "--software", name, "--color", color],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            console.print(f"  [green]✓[/] {name} → {color}")
            created += 1
        else:
            console.print(f"  [red]✗[/] {name}: {result.stderr.strip()}")
            failed += 1

    console.print(f"\n[bold]Summary:[/]")
    console.print(f"  [green]✓[/] Created: {created}")
    if failed:
        console.print(f"  [red]✗[/] Failed:  {failed}")
    console.print(f"\n[bold green]✓ Done![/]\n")

    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
