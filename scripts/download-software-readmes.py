#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "rich",
#   "python-dotenv",
# ]
# ///
"""
Download README files from GitHub for all software entries.

For each _index.md under content/software/, extracts the GitHub repo from the
frontmatter and fetches the README using the GitHub API, storing it in the
same directory.

By default, skips directories that already have a readme file. Use --force
to overwrite existing files.

Authentication:
  Set GH_TOKEN in .env file or environment variable for higher rate limits:
  - Unauthenticated: 60 requests/hour
  - Authenticated: 5,000 requests/hour

  # In .env file:
  GH_TOKEN=your_token_here

  # Or as environment variable:
  export GH_TOKEN=your_token_here

Usage:
  ./scripts/download-software-readmes.py           # Skip existing files
  ./scripts/download-software-readmes.py --force   # Overwrite existing files
"""

import subprocess
import sys
import os
import argparse
from pathlib import Path
import json
import base64
import time

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.table import Table
from rich import print as rprint
from dotenv import load_dotenv

console = Console()


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown file."""
    if not content.startswith('---'):
        return {}

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}

    frontmatter = parts[1].strip()
    result = {}

    # Simple YAML parser for github field
    for line in frontmatter.split('\n'):
        if line.startswith('github:'):
            result['github'] = line.split(':', 1)[1].strip()
            break

    return result


def fetch_readme_api(owner: str, repo: str, token: str | None = None) -> tuple[str | None, str]:
    """
    Fetch README content using GitHub API.

    Returns (content, error_message)
    """
    api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    # Build curl command with optional authentication
    curl_cmd = ['curl', '-s', '-H', 'Accept: application/vnd.github.v3+json']

    if token:
        curl_cmd.extend(['-H', f'Authorization: Bearer {token}'])

    curl_cmd.append(api_url)

    # Call GitHub API
    try:
        result = subprocess.run(
            curl_cmd,
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            return None, f"curl failed: {result.stderr}"

        # Parse JSON response
        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError as e:
            return None, f"Invalid JSON response: {e}"

        # Check for API errors
        if 'message' in data and 'content' not in data:
            return None, f"API error: {data.get('message', 'Unknown error')}"

        # Extract and decode content
        if 'content' not in data:
            return None, "No content field in API response"

        try:
            content = base64.b64decode(data['content']).decode('utf-8')
            return content, ""
        except Exception as e:
            return None, f"Failed to decode content: {e}"

    except subprocess.TimeoutExpired:
        return None, "Request timeout"
    except Exception as e:
        return None, f"Unexpected error: {e}"


def process_software_dir(software_dir: Path, token: str | None = None, force: bool = False) -> dict:
    """
    Process a single software directory.

    Returns dict with status information.
    """
    index_file = software_dir / "_index.md"

    if not index_file.exists():
        return {'status': 'skip', 'reason': 'no _index.md'}

    # Check if readme already exists
    readme_file = software_dir / "readme"
    if readme_file.exists() and not force:
        return {'status': 'skip', 'reason': 'readme exists (use --force to overwrite)'}

    # Read and parse frontmatter
    try:
        content = index_file.read_text()
    except Exception as e:
        return {'status': 'error', 'reason': f'failed to read file: {e}'}

    frontmatter = parse_frontmatter(content)
    github_repo = frontmatter.get('github')

    if not github_repo:
        return {'status': 'skip', 'reason': 'no github field'}

    # Parse owner/repo
    parts = github_repo.split('/')
    if len(parts) != 2:
        return {'status': 'error', 'reason': f'invalid github format: {github_repo}'}

    owner, repo = parts

    # Fetch README
    readme_content, error = fetch_readme_api(owner, repo, token)

    if error:
        return {'status': 'error', 'reason': error, 'repo': github_repo}

    # Save README (no extension)
    readme_file = software_dir / "readme"
    try:
        readme_file.write_text(readme_content)
        return {'status': 'success', 'repo': github_repo, 'file': str(readme_file)}
    except Exception as e:
        return {'status': 'error', 'reason': f'failed to write file: {e}', 'repo': github_repo}


def main():
    """Main entry point."""
    # Parse arguments
    parser = argparse.ArgumentParser(
        description='Download README files from GitHub for all software entries.'
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Overwrite existing readme files'
    )
    args = parser.parse_args()

    # Load from .env file (if it exists)
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    dotenv_path = repo_root / ".env"

    load_dotenv(dotenv_path)

    # Check for GitHub token (GH_TOKEN)
    github_token = os.environ.get('GH_TOKEN')

    token_source = None
    if github_token:
        if dotenv_path.exists():
            # Check if token is actually from .env by re-reading it
            with open(dotenv_path) as f:
                if 'GH_TOKEN' in f.read():
                    token_source = ".env file"
                else:
                    token_source = "environment variable"
        else:
            token_source = "environment variable"

        console.print(f"[green]✓[/green] Using authenticated requests (GH_TOKEN from {token_source})")
        console.print("[dim]  Rate limit: 5,000 requests/hour[/dim]")
    else:
        console.print("[yellow]⚠[/yellow] Using unauthenticated requests")
        console.print("[dim]  Rate limit: 60 requests/hour[/dim]")
        console.print("[dim]  Tip: Set GH_TOKEN in .env file or environment variable for higher limits[/dim]")

    # Find content/software directory
    software_base = repo_root / "content" / "software"

    if not software_base.exists():
        console.print(f"[red]Error:[/red] {software_base} does not exist")
        sys.exit(1)

    # Find all software directories
    software_dirs = sorted([d for d in software_base.iterdir() if d.is_dir()])

    if args.force:
        console.print("[yellow]⚠[/yellow] Force mode enabled - will overwrite existing readme files\n")

    console.print(f"[bold cyan]Found {len(software_dirs)} software directories[/bold cyan]\n")

    # Process each directory with progress bar
    success_count = 0
    skip_count = 0
    error_count = 0
    errors = []

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console
    ) as progress:

        task = progress.add_task("[cyan]Downloading READMEs...", total=len(software_dirs))

        for software_dir in software_dirs:
            name = software_dir.name
            progress.update(task, description=f"[cyan]Processing {name}...")

            result = process_software_dir(software_dir, github_token, args.force)

            if result['status'] == 'success':
                success_count += 1
                console.print(f"  [green]✓[/green] {name:30} → {result['repo']}")
            elif result['status'] == 'skip':
                skip_count += 1
                console.print(f"  [yellow]⊘[/yellow] {name:30} [dim]{result['reason']}[/dim]")
            else:  # error
                error_count += 1
                repo_info = result.get('repo', 'unknown')
                console.print(f"  [red]✗[/red] {name:30} [red]{result['reason']}[/red]")
                errors.append({'name': name, 'repo': repo_info, 'reason': result['reason']})

            progress.advance(task)

            # Rate limiting: be nice to GitHub API
            if result['status'] == 'success':
                time.sleep(0.5)

    # Summary table
    console.print()
    table = Table(title="Summary", show_header=True, header_style="bold magenta")
    table.add_column("Status", style="cyan", width=12)
    table.add_column("Count", justify="right", style="green")

    table.add_row("Success", f"[green]{success_count}[/green]")
    table.add_row("Skipped", f"[yellow]{skip_count}[/yellow]")
    table.add_row("Errors", f"[red]{error_count}[/red]")
    table.add_row("Total", f"[bold]{len(software_dirs)}[/bold]")

    console.print(table)

    # Show errors if any
    if errors:
        console.print("\n[bold red]Errors:[/bold red]")
        error_table = Table(show_header=True, header_style="bold red")
        error_table.add_column("Name", style="cyan")
        error_table.add_column("Repo", style="yellow")
        error_table.add_column("Reason", style="red")

        for error in errors:
            error_table.add_row(error['name'], error['repo'], error['reason'])

        console.print(error_table)


if __name__ == '__main__':
    main()
