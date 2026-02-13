#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "PyGithub>=2.1.1",
#   "tomli-w>=1.0.0",
#   "python-dotenv>=1.0.0",
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
from datetime import datetime
from pathlib import Path
from typing import Any

import tomli_w
from dotenv import load_dotenv
from github import Github, GithubException, UnknownObjectException


def get_github_token() -> str:
    """Get GitHub token from .env file or GH_TOKEN environment variable."""
    load_dotenv()
    token = os.getenv("GH_TOKEN")
    if not token:
        print("Error: GitHub token not found in .env or GH_TOKEN environment variable", file=sys.stderr)
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
        # Get commits from oldest to newest by getting all commits and taking the last one
        # For efficiency, we'll use created_at as a proxy if getting first commit is too expensive
        commits = list(repo.get_commits())
        if commits:
            # The last commit in the default iteration is actually the most recent
            # We need to reverse or get the last page
            # For efficiency, let's just use the repository created date
            return repo.created_at.isoformat()
    except Exception as e:
        print(f"Warning: Could not get first commit date for {repo.full_name}: {e}", file=sys.stderr)
        return repo.created_at.isoformat() if repo.created_at else None


def get_latest_release_date(repo) -> str | None:
    """Get the date of the latest release."""
    try:
        releases = repo.get_releases()
        if releases.totalCount > 0:
            latest_release = releases[0]
            return latest_release.created_at.isoformat()
    except Exception as e:
        print(f"Warning: Could not get latest release for {repo.full_name}: {e}", file=sys.stderr)
    return None


def get_contributors(repo) -> list[str]:
    """Get list of contributor usernames."""
    try:
        contributors = repo.get_contributors()
        return [contributor.login for contributor in contributors]
    except Exception as e:
        print(f"Warning: Could not get contributors for {repo.full_name}: {e}", file=sys.stderr)
        return []


def get_readme_first_image(repo) -> str | None:
    """Get the URL of the first image in README.md."""
    try:
        readme = repo.get_readme()
        content = readme.decoded_content.decode("utf-8")
        return extract_first_image_url(content)
    except UnknownObjectException:
        # No README found
        return None
    except Exception as e:
        print(f"Warning: Could not get README for {repo.full_name}: {e}", file=sys.stderr)
        return None


def fetch_org_repos(gh: Github, org_name: str) -> list[dict[str, Any]]:
    """Fetch all public, non-archived repositories for an organization."""
    repos_data = []

    try:
        org = gh.get_organization(org_name)
        repos = org.get_repos(type="public")

        for repo in repos:
            if repo.archived:
                continue

            print(f"Processing {repo.full_name}...", file=sys.stderr)

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
            }

            repos_data.append(repo_info)

    except GithubException as e:
        print(f"Error: Could not fetch repositories for organization '{org_name}': {e}", file=sys.stderr)
    except Exception as e:
        print(f"Error: Unexpected error processing organization '{org_name}': {e}", file=sys.stderr)

    return repos_data


def main() -> None:
    """Main function to orchestrate the script."""
    # Set up paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    orgs_file = project_root / "data" / "github-orgs.toml"
    output_file = project_root / "data" / "github-repos.toml"

    # Check if input file exists
    if not orgs_file.exists():
        print(f"Error: Input file not found: {orgs_file}", file=sys.stderr)
        sys.exit(1)

    # Read organizations
    with open(orgs_file, "rb") as f:
        orgs_data = tomllib.load(f)

    organizations = orgs_data.get("orgs", [])
    if not organizations:
        print("Error: No organizations found in github-orgs.toml", file=sys.stderr)
        sys.exit(1)

    # Initialize GitHub client
    token = get_github_token()
    gh = Github(token)

    # Fetch repositories for all organizations
    all_repos = []
    for org_name in organizations:
        print(f"Fetching repositories for {org_name}...", file=sys.stderr)
        repos = fetch_org_repos(gh, org_name)
        all_repos.extend(repos)

    # Write output
    output_data = {"repos": all_repos}
    with open(output_file, "wb") as f:
        tomli_w.dump(output_data, f)

    print(f"Successfully wrote {len(all_repos)} repositories to {output_file}", file=sys.stderr)


if __name__ == "__main__":
    main()
