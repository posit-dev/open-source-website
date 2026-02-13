#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "rich>=13.0.0",
# ]
# ///

"""
Create new software directories from GitHub repository data.

Reads data/github-repos.toml and creates a directory structure for each
repository that doesn't already exist in content/software/.
"""

import argparse
import sys
import tomllib
from pathlib import Path

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.table import Table

console = Console(stderr=True)


def load_github_repos(repos_file: Path) -> list[dict]:
    """Load repository data from TOML file."""
    if not repos_file.exists():
        console.print(f"[bold red]Error:[/] Repos file not found: {repos_file}")
        sys.exit(1)

    try:
        with open(repos_file, 'rb') as f:
            data = tomllib.load(f)
        repos_list = data.get('repos', [])
        console.print(f"[dim]Loaded {len(repos_list)} repositories from {repos_file.name}[/]")
        return repos_list
    except Exception as e:
        console.print(f"[bold red]Error:[/] Failed to load repos file: {e}")
        sys.exit(1)


def get_software_name(repo_data: dict) -> str | None:
    """Get the software name from repo data, converted to lowercase."""
    name = repo_data.get('name')
    return name.lower() if name else None


def create_software_directory(
    software_dir: Path,
    repo_name: str,
    github_repo: str,
    dry_run: bool
) -> tuple[bool, str]:
    """
    Create a software directory with _index.md file.

    Returns:
        tuple: (created, message)
    """
    target_dir = software_dir / repo_name

    if target_dir.exists():
        return False, "already exists"

    if dry_run:
        return True, "would create (dry-run)"

    try:
        # Create directory
        target_dir.mkdir(parents=True, exist_ok=True)

        # Create _index.md with minimal frontmatter
        index_file = target_dir / "_index.md"
        content = f"""---
github: {github_repo}
---
"""
        index_file.write_text(content, encoding='utf-8')

        return True, "created"

    except Exception as e:
        return False, f"error: {e}"


def main() -> None:
    """Main function to orchestrate the script."""
    parser = argparse.ArgumentParser(
        description="Create new software directories from GitHub repository data."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without actually creating files",
    )
    parser.add_argument(
        "--minimal-stars",
        type=int,
        default=100,
        help="Minimum number of stars required to create a directory (default: 100)",
    )
    args = parser.parse_args()

    console.print("\n[bold blue]Software Directory Creator[/]\n")

    if args.dry_run:
        console.print("[yellow]DRY RUN MODE - No files will be created[/]\n")

    console.print(f"[dim]Minimum stars: {args.minimal_stars}[/]\n")

    # Set up paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    software_dir = project_root / "content" / "software"
    repos_file = project_root / "data" / "github-repos.toml"

    console.print(f"[dim]Software directory: {software_dir}[/]")
    console.print(f"[dim]GitHub repos data:  {repos_file}[/]\n")

    # Check if software directory exists
    if not software_dir.exists():
        console.print(f"[bold red]Error:[/] Software directory not found: {software_dir}")
        sys.exit(1)

    # Load repository data
    repos_list = load_github_repos(repos_file)

    # Process repositories
    created_count = 0
    skipped_count = 0
    error_count = 0

    results = []

    console.print(f"[cyan]Processing {len(repos_list)} repositories[/]\n")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Processing...", total=len(repos_list))

        for repo_data in repos_list:
            software_name = get_software_name(repo_data)
            github_repo = repo_data.get('repo', 'unknown')

            progress.update(task, description=f"[cyan]{github_repo}")

            if not software_name:
                results.append((github_repo, "skipped", "no name field", None))
                skipped_count += 1
                progress.advance(task)
                continue

            # Skip repos with less than minimal stars
            stars = repo_data.get('stars', 0)
            if stars < args.minimal_stars:
                results.append((github_repo, "skipped", f"too few stars ({stars} < {args.minimal_stars})", None))
                skipped_count += 1
                progress.advance(task)
                continue

            created, message = create_software_directory(
                software_dir,
                software_name,
                github_repo,
                args.dry_run
            )

            if created:
                results.append((github_repo, "created", message, software_name))
                created_count += 1
            elif "already exists" in message:
                results.append((github_repo, "skipped", message, software_name))
                skipped_count += 1
            else:
                results.append((github_repo, "error", message, software_name))
                error_count += 1

            progress.advance(task)

    # Display results table
    console.print("\n[bold]Results:[/]\n")

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Repository", style="dim", no_wrap=True)
    table.add_column("Directory", style="cyan", no_wrap=True)
    table.add_column("Status", style="")
    table.add_column("Message", style="dim")

    # Limit table output if too many rows
    if len(results) > 20:
        console.print("[dim]Showing interesting results (created/errors + first skipped)[/]\n")
        # Show only created and errors, plus first few skipped
        filtered = [r for r in results if r[1] in ("created", "error")]
        remaining = max(0, 20 - len(filtered))
        filtered.extend([r for r in results if r[1] == "skipped"][:remaining])

        for github_repo, status, message, directory in filtered:
            if status == "created":
                status_str = "[green]✓ Created[/]"
            elif status == "error":
                status_str = "[red]✗ Error[/]"
            else:
                status_str = "[dim]○ Skipped[/]"
            dir_name = directory if directory else "-"
            table.add_row(github_repo, dir_name, status_str, message)
    else:
        # Show all results sorted by status
        for github_repo, status, message, directory in sorted(results, key=lambda x: (x[1] != "created", x[1] != "error", x[0])):
            if status == "created":
                status_str = "[green]✓ Created[/]"
            elif status == "error":
                status_str = "[red]✗ Error[/]"
            else:
                status_str = "[dim]○ Skipped[/]"
            dir_name = directory if directory else "-"
            table.add_row(github_repo, dir_name, status_str, message)

    console.print(table)

    # Summary
    console.print("\n[bold]Summary:[/]")
    console.print(f"  [green]✓[/] Created:  {created_count}")
    console.print(f"  [dim]○[/] Skipped:  {skipped_count}")
    if error_count > 0:
        console.print(f"  [red]✗[/] Errors:   {error_count}")

    if args.dry_run:
        console.print("\n[yellow]DRY RUN - No changes were made[/]")

    console.print("\n[bold green]✓ Done![/]\n")

    if error_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
