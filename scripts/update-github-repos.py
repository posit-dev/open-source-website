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

import argparse
import os
import re
import sys
import tomllib
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import tomli_w
from dotenv import load_dotenv
from github import Auth, Github, GithubException, UnknownObjectException
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
    """Extract the first non-badge image URL from README."""
    # Match HTML img tags: <img src="url" ...> or <img ... src="url" ...>
    html_pattern = r'<img[^>]+src=["\']([^"\']+)["\']'

    for match in re.finditer(html_pattern, readme_content, re.IGNORECASE):
        url = match.group(1)
        # Skip badge images
        if "badge.svg" not in url.lower():
            return url

    return None


def format_value(value: Any, max_len: int = 40) -> str:
    """Format a value for display, truncating if needed."""
    if isinstance(value, list):
        value_str = ", ".join(str(v) for v in value)
    else:
        value_str = str(value)

    if len(value_str) > max_len:
        return value_str[:max_len - 3] + "..."
    return value_str


def get_first_commit_date(repo, repo_name: str, max_name_len: int, out_console: Console = console) -> str | None:
    """Get the date of the first commit in the repository."""
    repo_name_padded = repo_name.rjust(max_name_len)
    try:
        # Use repo creation date as a proxy for first commit
        if repo.created_at:
            date = repo.created_at.isoformat()
            out_console.print(f"[dim][{repo_name_padded}] first_commit: {date}[/]")
            return date
    except Exception as e:
        out_console.print(f"[yellow][{repo_name_padded}] Warning: Could not get creation date: {e}[/]")
    return None


def get_release_info(repo, repo_name: str, max_name_len: int, out_console: Console = console) -> tuple[str | None, int]:
    """Get the date of the latest release and total release count.

    Returns (latest_release_date, release_count)
    """
    repo_name_padded = repo_name.rjust(max_name_len)
    try:
        releases = repo.get_releases()
        count = releases.totalCount
        if count > 0:
            latest_release = releases[0]
            date = latest_release.created_at.isoformat()
            out_console.print(f"[dim][{repo_name_padded}] latest_release: {date}[/]")
            out_console.print(f"[dim][{repo_name_padded}] releases: {count}[/]")
            return date, count
        else:
            out_console.print(f"[dim][{repo_name_padded}] latest_release: None[/]")
            out_console.print(f"[dim][{repo_name_padded}] releases: 0[/]")
            return None, 0
    except Exception as e:
        out_console.print(f"[yellow][{repo_name_padded}] Warning: Could not get releases: {e}[/]")
        return None, 0


def get_contributors(repo, repo_name: str, max_name_len: int, out_console: Console = console) -> list[str]:
    """Get list of contributor usernames."""
    repo_name_padded = repo_name.rjust(max_name_len)
    try:
        contributors = repo.get_contributors()
        contributor_list = [contributor.login for contributor in contributors]
        out_console.print(f"[dim][{repo_name_padded}] contributors: {format_value(contributor_list)}[/]")
        return contributor_list
    except Exception as e:
        out_console.print(f"[yellow][{repo_name_padded}] Warning: Could not get contributors: {e}[/]")
        return []


def get_readme_first_image(repo, repo_name: str, max_name_len: int, out_console: Console = console) -> str | None:
    """Get the URL of the first non-badge image in README.md."""
    repo_name_padded = repo_name.rjust(max_name_len)
    try:
        readme = repo.get_readme()
        content = readme.decoded_content.decode("utf-8")
        image_url = extract_first_image_url(content)
        if image_url:
            out_console.print(f"[dim][{repo_name_padded}] readme_image: {format_value(image_url)}[/]")
        else:
            out_console.print(f"[dim][{repo_name_padded}] readme_image: None[/]")
        return image_url
    except UnknownObjectException:
        out_console.print(f"[dim][{repo_name_padded}] readme_image: None (no README)[/]")
        return None
    except Exception as e:
        out_console.print(f"[yellow][{repo_name_padded}] Warning: Could not get README: {e}[/]")
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
        # Filter out None values from each repo (TOML doesn't support None)
        repos_list = [
            {key: value for key, value in repo.items() if value is not None}
            for repo in repos_dict.values()
        ]
        output_data = {"repos": repos_list}
        with open(output_file, "wb") as f:
            tomli_w.dump(output_data, f)
    except Exception as e:
        console.print(f"[bold red]Error:[/] Failed to write to {output_file}: {e}")


def fetch_org_repos(gh: Github, org_name: str, existing_repos: dict[str, dict[str, Any]], output_file: Path, keys_to_update: set[str] | None = None, force: bool = False) -> dict[str, dict[str, Any]]:
    """Fetch all public, non-archived repositories for an organization."""
    repos_dict = existing_repos.copy()

    # Available keys that can be fetched
    FETCHABLE_KEYS = {"stars", "forks", "latest_release", "releases", "first_commit", "license", "contributors", "readme_image", "description", "website", "name", "language"}

    # If no keys specified, fetch all
    if keys_to_update is None:
        keys_to_update = FETCHABLE_KEYS
    else:
        # Validate keys
        invalid_keys = keys_to_update - FETCHABLE_KEYS
        if invalid_keys:
            console.print(f"[yellow]Warning:[/] Invalid keys: {', '.join(invalid_keys)}")
            console.print(f"[yellow]Valid keys are:[/] {', '.join(sorted(FETCHABLE_KEYS))}")
            keys_to_update = keys_to_update & FETCHABLE_KEYS

    try:
        console.print(f"\n[bold cyan]Organization:[/] {org_name}")
        if keys_to_update != FETCHABLE_KEYS:
            console.print(f"[cyan]Updating keys:[/] {', '.join(sorted(keys_to_update))}")
        if force:
            console.print("[yellow]Force mode:[/] Ignoring last_updated timestamps")
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

            # Skip timestamp check if force flag is set
            if force:
                repos_to_update.append(repo)
            else:
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

            # Find the maximum repo name length for right-alignment
            max_repo_name_len = max(len(repo.full_name) for repo in repos_to_update)

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

                    # Start with existing data or base structure
                    existing_data = existing_repos.get(repo.full_name, {})
                    repo_info = existing_data.copy() if existing_data else {}

                    # Always update repo identifier and timestamp
                    repo_info["repo"] = repo.full_name

                    # Format repo name with right-alignment
                    repo_name_padded = repo.full_name.rjust(max_repo_name_len)

                    # Print repo URL first for easy navigation
                    progress.console.print(f"[dim][{repo_name_padded}] url: https://github.com/{repo.full_name}[/]")

                    # Update only requested keys
                    if "name" in keys_to_update:
                        repo_info["name"] = repo.name
                        progress.console.print(f"[dim][{repo_name_padded}] name: {format_value(repo.name)}[/]")
                    if "description" in keys_to_update:
                        repo_info["description"] = repo.description or ""
                        progress.console.print(f"[dim][{repo_name_padded}] description: {format_value(repo.description or '')}[/]")
                    if "website" in keys_to_update:
                        repo_info["website"] = repo.homepage or ""
                        progress.console.print(f"[dim][{repo_name_padded}] website: {format_value(repo.homepage or '')}[/]")
                    if "stars" in keys_to_update:
                        repo_info["stars"] = repo.stargazers_count
                        progress.console.print(f"[dim][{repo_name_padded}] stars: {repo.stargazers_count}[/]")
                    if "forks" in keys_to_update:
                        repo_info["forks"] = repo.forks_count
                        progress.console.print(f"[dim][{repo_name_padded}] forks: {repo.forks_count}[/]")
                    if "license" in keys_to_update:
                        repo_info["license"] = repo.license.spdx_id if repo.license else None
                        progress.console.print(f"[dim][{repo_name_padded}] license: {repo_info['license']}[/]")
                    if "language" in keys_to_update:
                        repo_info["language"] = repo.language
                        progress.console.print(f"[dim][{repo_name_padded}] language: {repo.language}[/]")
                    # Fetch release info if either latest_release or releases count is requested
                    if "latest_release" in keys_to_update or "releases" in keys_to_update:
                        latest_release, release_count = get_release_info(repo, repo.full_name, max_repo_name_len, progress.console)
                        if "latest_release" in keys_to_update:
                            repo_info["latest_release"] = latest_release
                        if "releases" in keys_to_update:
                            repo_info["releases"] = release_count
                    if "first_commit" in keys_to_update:
                        repo_info["first_commit"] = get_first_commit_date(repo, repo.full_name, max_repo_name_len, progress.console)
                    if "contributors" in keys_to_update:
                        repo_info["contributors"] = get_contributors(repo, repo.full_name, max_repo_name_len, progress.console)
                    if "readme_image" in keys_to_update:
                        repo_info["readme_image"] = get_readme_first_image(repo, repo.full_name, max_repo_name_len, progress.console)

                    repo_info["last_updated"] = datetime.now(timezone.utc).isoformat()

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
    # Define basic keys that require no additional API calls
    BASIC_KEYS = {"name", "description", "website", "stars", "forks", "license", "first_commit", "language"}

    parser = argparse.ArgumentParser(
        description="Fetch public repositories from GitHub organizations and save metadata."
    )
    parser.add_argument(
        "--keys",
        type=str,
        help="Comma-separated list of keys to update (e.g., 'stars,forks,contributors'). Use 'basic' to update all keys that require no additional API calls. If not specified, all keys are updated.",
    )
    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Force update all repositories, ignoring the last_updated timestamp.",
    )
    args = parser.parse_args()

    # Parse keys argument
    keys_to_update = None
    if args.keys:
        if args.keys.strip().lower() == "basic":
            keys_to_update = BASIC_KEYS
        else:
            keys_to_update = {key.strip() for key in args.keys.split(",")}

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
    auth = Auth.Token(token)
    gh = Github(auth=auth)

    # Check rate limit
    remaining, limit = gh.rate_limiting
    reset_time = gh.rate_limiting_resettime
    reset_dt = datetime.fromtimestamp(reset_time, tz=timezone.utc)
    console.print(f"[cyan]Rate limit:[/] {remaining}/{limit} remaining (resets at {reset_dt.strftime('%H:%M:%S')})")

    # Fetch repositories for all organizations
    all_repos_dict = existing_repos.copy()
    for org_name in organizations:
        repos_dict = fetch_org_repos(gh, org_name, all_repos_dict, output_file, keys_to_update, args.force)
        all_repos_dict.update(repos_dict)

    # Final write to ensure everything is saved
    console.print("[dim]Writing final output...[/]")
    write_repos_to_file(all_repos_dict, output_file)

    # Show final rate limit status
    remaining, limit = gh.rate_limiting
    console.print(f"[cyan]Rate limit:[/] {remaining}/{limit} remaining")

    console.print(f"\n[bold green]✓ Done![/] Processed [cyan]{len(all_repos_dict)}[/] repositories total")
    console.print(f"[dim]Data written to {output_file}[/]\n")


if __name__ == "__main__":
    main()
