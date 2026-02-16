#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "rich>=13.0.0",
#   "pyyaml>=6.0",
# ]
# ///
"""Summarize software README files using Claude CLI.

This script loops over all directories in content/software/, reads their readme files,
uses Claude CLI to generate summaries, and updates the body of _index.md files while
preserving frontmatter.
"""

import argparse
from pathlib import Path

from rich.console import Console

# Prompt for Claude CLI to generate summaries
PROMPT = """Summarize this README for developers and data scientists. Write exactly two paragraphs:

Paragraph 1: One or two clear, direct sentences explaining what this package does. Focus on its core purpose and primary use case.

Paragraph 2: Two to three sentences covering what makes this package valuable - its key features, what problems it solves, or what makes it different from alternatives. Keep it factual and technical, not marketing-focused. Use short, simple sentences.

Do not include headers, titles, installation instructions, or badges. Just write the summary paragraphs as plain text."""


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Summarize software README files using Claude CLI"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing summaries",
    )
    args = parser.parse_args()

    console = Console()
    console.print("[bold cyan]Software README Summarization Script[/bold cyan]")
    console.print()

    # Find content/software directory
    software_base = Path("content/software")
    if not software_base.exists():
        console.print("[bold red]Error: content/software directory not found[/bold red]")
        return 1

    # Find all software directories
    directories = sorted([d for d in software_base.iterdir() if d.is_dir()])
    console.print(f"Found {len(directories)} software directories")
    console.print()

    if args.dry_run:
        console.print("[yellow]DRY RUN MODE - No changes will be made[/yellow]")
        console.print()

    return 0


if __name__ == "__main__":
    exit(main())
