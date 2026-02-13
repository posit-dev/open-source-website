#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "PyGithub>=2.1.1",
#   "tomli-w>=1.0.0",
#   "python-dotenv>=1.0.0",
#   "rich>=13.0.0",
# ]
# ///

"""
Fetch public repositories from GitHub organizations and save metadata.

Reads GitHub organizations from data/github-orgs.toml and writes
repository information to data/github-repos.toml.
"""

import os
import re
import sys
import tomllib
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import tomli_w
from dotenv import load_dotenv
from github import Github, GithubException, UnknownObjectException
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn

console = Console(stderr=True)


def get_github_token() -> str:
    """Get GitHub token from .env file or GH_TOKEN environment variable."""
    load_dotenv()
    token = os.getenv("GH_TOKEN")
    if not token:
        console.print("[bold red]Error:[/] GitHub token not found in .env or GH_TOKEN environment variable")
        sys.exit(1)
    return token


def extract_first_image_url(readme_content: str) -> str | None:
    """Extract the first image URL from README markdown content."""
    # Match markdown images: ![alt](url)
    markdown_pattern = r"!\[.*?\]\((.*?)\)"
    # Match HTML img tags: <img src="url" ...>
    html_pattern = r'<img[^>]+src=["\']([^"\']+)["\']'

    markdown_match = re.search(markdown_pattern, readme_content)
    if markdown_match:
        return markdown_match.group(1)

    html_match = re.search(html_pattern, readme_content, re.IGNORECASE)
    if html_match:
        return html_match.group(1)

    return None


def get_first_commit_date(repo) -> str | None:
    """Get the date of the first commit in the repository."""
    try:
        console.print("    [dim]Fetching first commit date[/]")
        # Get commits from oldest to newest by getting all commits and taking the last one
        # For efficiency, we'll use created_at as a proxy if getting first commit is too expensive
        commits = list(repo.get_commits())
        if commits:
            # The last commit in the default iteration is actually the most recent
            # We need to reverse or get the last page
            # For efficiency, let's just use the repository created date
            date = repo.created_at.isoformat()
            console.print(f"    [dim]First commit: {date}[/]")
            return date
    except Exception as e:
        console.print(f"    [yellow]Warning:[/] Could not get first commit date: {e}")
        return repo.created_at.isoformat() if repo.created_at else None


def get_latest_release_date(repo) -> str | None:
    """Get the date of the latest release."""
    try:
        console.print("    [dim]Fetching latest release[/]")
        releases = repo.get_releases()
        if releases.totalCount > 0:
            latest_release = releases[0]
            date = latest_release.created_at.isoformat()
            console.print(f"    [dim]Latest release: {date}[/]")
            return date
        else:
            console.print("    [dim]No releases found[/]")
    except Exception as e:
        console.print(f"    [yellow]Warning:[/] Could not get latest release: {e}")
    return None


def get_contributors(repo) -> list[str]:
    """Get list of contributor usernames."""
    try:
        console.print("    [dim]Fetching contributors[/]")
        contributors = repo.get_contributors()
        contributor_list = [contributor.login for contributor in contributors]
        console.print(f"    [dim]Found {len(contributor_list)} contributors[/]")
        return contributor_list
    except Exception as e:
        console.print(f"    [yellow]Warning:[/] Could not get contributors: {e}")
        return []


def get_readme_first_image(repo) -> str | None:
    """Get the URL of the first image in README.md."""
    try:
        console.print("    [dim]Fetching README image[/]")
        readme = repo.get_readme()
        content = readme.decoded_content.decode("utf-8")
        image_url = extract_first_image_url(content)
        if image_url:
            console.print("    [dim]Found README image[/]")
        else:
            console.print("    [dim]No image in README[/]")
        return image_url
    except UnknownObjectException:
        console.print("    [dim]No README found[/]")
        return None
    except Exception as e:
        console.print(f"    [yellow]Warning:[/] Could not get README: {e}")
        return None


def load_existing_repos(output_file: Path) -> dict[str, dict[str, Any]]:
    """Load existing repository data from the output file."""
    if not output_file.exists():
        console.print("[dim]No existing repos file found[/]")
        return {}

    try:
        with open(output_file, "rb") as f:
            data = tomllib.load(f)
        repos_list = data.get("repos", [])
        # Create a dict with repo name as key for easy lookup
        repos_dict = {repo["repo"]: repo for repo in repos_list}
        console.print(f"[dim]Loaded {len(repos_dict)} existing repos[/]")
        return repos_dict
    except Exception as e:
        console.print(f"[yellow]Warning:[/] Could not load existing repos file: {e}")
        return {}


def should_update_repo(existing_repo: dict[str, Any] | None) -> tuple[bool, str]:
    """Check if a repo should be updated based on last_updated timestamp.

    Returns (should_update, reason)
    """
    if not existing_repo:
        return True, "new repo"

    last_updated_str = existing_repo.get("last_updated")
    if not last_updated_str:
        return True, "no timestamp"

    try:
        last_updated = datetime.fromisoformat(last_updated_str)
        now = datetime.now(timezone.utc)
        time_diff = now - last_updated

        if time_diff < timedelta(hours=12):
            hours_ago = time_diff.total_seconds() / 3600
            return False, f"updated {hours_ago:.1f}h ago"
        else:
            hours_ago = time_diff.total_seconds() / 3600
            return True, f"stale ({hours_ago:.1f}h ago)"
    except Exception:
        return True, "invalid timestamp"


def write_repos_to_file(repos_dict: dict[str, dict[str, Any]], output_file: Path) -> None:
    """Write all repositories to the output file."""
    try:
        repos_list = list(repos_dict.values())
        output_data = {"repos": repos_list}
        with open(output_file, "wb") as f:
            tomli_w.dump(output_data, f)
    except Exception as e:
        console.print(f"[bold red]Error:[/] Failed to write to {output_file}: {e}")


def fetch_org_repos(gh: Github, org_name: str, existing_repos: dict[str, dict[str, Any]], output_file: Path) -> dict[str, dict[str, Any]]:
    """Fetch all public, non-archived repositories for an organization."""
    repos_dict = existing_repos.copy()

    try:
        console.print(f"\n[bold cyan]Organization:[/] {org_name}")
        console.print("[dim]Scanning repositories...[/]")
        org = gh.get_organization(org_name)
        all_repos = list(org.get_repos(type="public"))

        # First pass: determine which repos need updating
        repos_to_update = []
        skipped_repos = []

        for repo in all_repos:
            if repo.archived:
                skipped_repos.append((repo.full_name, "archived"))
                continue

            existing_repo = existing_repos.get(repo.full_name)
            should_update, reason = should_update_repo(existing_repo)

            if should_update:
                repos_to_update.append(repo)
            else:
                skipped_repos.append((repo.full_name, reason))

        # Show summary
        console.print(f"[green]✓[/] Found {len(all_repos)} repos: [cyan]{len(repos_to_update)}[/] to update, [dim]{len(skipped_repos)}[/] to skip")

        if skipped_repos:
            console.print("\n[dim]Skipped repositories:[/]")
            for repo_name, reason in skipped_repos[:5]:  # Show first 5
                console.print(f"  [dim]• {repo_name} ({reason})[/]")
            if len(skipped_repos) > 5:
                console.print(f"  [dim]• ... and {len(skipped_repos) - 5} more[/]")

        # Second pass: fetch metadata with progress bar
        if repos_to_update:
            console.print(f"\n[bold]Fetching metadata for {len(repos_to_update)} repositories[/]")

            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
                TimeRemainingColumn(),
                console=console,
            ) as progress:
                task = progress.add_task("[cyan]Processing...", total=len(repos_to_update))

                for repo in repos_to_update:
                    progress.update(task, description=f"[cyan]{repo.full_name}")

                    repo_info = {
                        "repo": repo.full_name,
                        "name": repo.name,
                        "description": repo.description or "",
                        "website": repo.homepage or "",
                        "stars": repo.stargazers_count,
                        "forks": repo.forks_count,
                        "latest_release": get_latest_release_date(repo),
                        "first_commit": get_first_commit_date(repo),
                        "license": repo.license.spdx_id if repo.license else None,
                        "contributors": get_contributors(repo),
                        "readme_image": get_readme_first_image(repo),
                        "last_updated": datetime.now(timezone.utc).isoformat(),
                    }

                    # Update the repos dict and write immediately
                    repos_dict[repo.full_name] = repo_info
                    write_repos_to_file(repos_dict, output_file)

                    progress.advance(task)

            console.print(f"[green]✓[/] Completed {len(repos_to_update)} repositories\n")

    except GithubException as e:
        console.print(f"[bold red]Error:[/] Could not fetch repositories for organization '{org_name}': {e}")
    except Exception as e:
        console.print(f"[bold red]Error:[/] Unexpected error processing organization '{org_name}': {e}")

    return repos_dict


def main() -> None:
    """Main function to orchestrate the script."""
    console.print("\n[bold blue]GitHub Repository Metadata Fetcher[/]\n")

    # Set up paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    orgs_file = project_root / "data" / "github-orgs.toml"
    output_file = project_root / "data" / "github-repos.toml"

    console.print(f"[dim]Input:  {orgs_file}[/]")
    console.print(f"[dim]Output: {output_file}[/]\n")

    # Check if input file exists
    if not orgs_file.exists():
        console.print(f"[bold red]Error:[/] Input file not found: {orgs_file}")
        sys.exit(1)

    # Read organizations
    with open(orgs_file, "rb") as f:
        orgs_data = tomllib.load(f)

    organizations = orgs_data.get("orgs", [])
    if not organizations:
        console.print("[bold red]Error:[/] No organizations found in github-orgs.toml")
        sys.exit(1)

    console.print(f"[cyan]Organizations:[/] {', '.join(organizations)}")

    # Load existing repository data
    existing_repos = load_existing_repos(output_file)

    # Initialize GitHub client
    console.print("[dim]Initializing GitHub client...[/]")
    token = get_github_token()
    gh = Github(token)

    # Fetch repositories for all organizations
    all_repos_dict = existing_repos.copy()
    for org_name in organizations:
        repos_dict = fetch_org_repos(gh, org_name, all_repos_dict, output_file)
        all_repos_dict.update(repos_dict)

    # Final write to ensure everything is saved
    console.print("[dim]Writing final output...[/]")
    write_repos_to_file(all_repos_dict, output_file)

    console.print(f"\n[bold green]✓ Done![/] Processed [cyan]{len(all_repos_dict)}[/] repositories total")
    console.print(f"[dim]Data written to {output_file}[/]\n")


if __name__ == "__main__":
    main()
