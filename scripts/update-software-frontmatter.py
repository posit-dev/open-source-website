#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
# ]
# ///

"""
Update software frontmatter from GitHub repositories.

Reads _index.md files from content/software directories, extracts the github
field from YAML frontmatter, looks up the corresponding repository in
data/github-repos.toml, and updates the frontmatter with an 'external' field containing
repository metadata. Also sets top-level frontmatter keys based on external,
include, exclude, and override fields.
"""

import sys
import tomllib
from pathlib import Path
from typing import Any

import yaml
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

console = Console(stderr=True)


def parse_frontmatter(content: str) -> tuple[dict[str, Any], str, str]:
    """
    Parse YAML frontmatter from markdown content.

    Returns:
        tuple: (frontmatter_dict, yaml_section, remaining_content)
    """
    lines = content.split('\n')

    if not lines or lines[0].strip() != '---':
        return {}, "", content

    # Find the closing ---
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_idx = i
            break

    if end_idx is None:
        return {}, "", content

    # Extract frontmatter YAML
    yaml_lines = lines[1:end_idx]
    yaml_section = '\n'.join(yaml_lines)

    try:
        frontmatter = yaml.safe_load(yaml_section) or {}
    except yaml.YAMLError as e:
        console.print(f"[yellow]Warning:[/] Failed to parse YAML: {e}")
        return {}, "", content

    # Remaining content
    remaining_content = '\n'.join(lines[end_idx + 1:])

    return frontmatter, yaml_section, remaining_content


class NoAliasYamlDumper(yaml.SafeDumper):
    """Custom YAML dumper that disables anchors and aliases."""
    def ignore_aliases(self, data):
        return True


def format_frontmatter(frontmatter: dict[str, Any]) -> str:
    """
    Format frontmatter dict back to YAML string.

    Uses block style for better readability and preserves structure.
    Disables YAML anchors/aliases (& and *).
    """
    yaml_str = yaml.dump(
        frontmatter,
        Dumper=NoAliasYamlDumper,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        indent=2
    )
    return yaml_str.strip()


def write_frontmatter(file_path: Path, frontmatter: dict[str, Any], remaining_content: str) -> None:
    """
    Write updated frontmatter back to the markdown file.
    """
    yaml_content = format_frontmatter(frontmatter)

    new_content = f"---\n{yaml_content}\n---\n{remaining_content}"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)


def load_repos_data(repos_file: Path) -> dict[str, dict[str, Any]]:
    """
    Load repository data from TOML file.

    Returns a dict mapping repo name (e.g., "posit-dev/positron") to repo metadata.
    """
    if not repos_file.exists():
        console.print(f"[bold red]Error:[/] Repos file not found: {repos_file}")
        sys.exit(1)

    try:
        with open(repos_file, 'rb') as f:
            data = tomllib.load(f)

        repos_list = data.get('repos', [])
        repos_dict = {repo['repo']: repo for repo in repos_list}

        console.print(f"[dim]Loaded {len(repos_dict)} repositories from {repos_file.name}[/]")
        return repos_dict

    except Exception as e:
        console.print(f"[bold red]Error:[/] Failed to load repos file: {e}")
        sys.exit(1)


def load_people_mapping(people_dir: Path) -> dict[str, str]:
    """
    Load people data and create a mapping of GitHub username to person name.

    Returns a dict mapping github username to person's title/name.
    """
    if not people_dir.exists():
        console.print(f"[yellow]Warning:[/] People directory not found: {people_dir}")
        return {}

    people_map = {}
    index_files = list(people_dir.glob("*/_index.md"))

    for index_file in index_files:
        try:
            content = index_file.read_text(encoding='utf-8')
            frontmatter, _, _ = parse_frontmatter(content)

            github_username = frontmatter.get('github', '').strip()
            person_name = frontmatter.get('title', '').strip()

            if github_username and person_name:
                people_map[github_username] = person_name

        except Exception as e:
            console.print(f"[yellow]Warning:[/] Failed to read {index_file}: {e}")
            continue

    console.print(f"[dim]Loaded {len(people_map)} people profiles[/]")
    return people_map


def extract_external_metadata(
    repo_data: dict[str, Any],
    people_map: dict[str, str]
) -> dict[str, Any]:
    """
    Extract relevant metadata fields for the 'external' section in frontmatter.

    Converts contributor GitHub usernames to person names where available.
    Uses 'title' instead of 'name' for the repository name.
    Converts primary 'language' to 'languages' list.
    """
    # Fields to include in the external section
    external_fields = [
        'repo',
        'description',
        'website',
        'stars',
        'forks',
        'latest_release',
        'first_commit',
        'license',
        'contributors',
        'readme_image',
        'last_updated'
    ]

    external = {}

    # Special handling: use 'name' from repo_data as 'title' in external
    if 'name' in repo_data and repo_data['name'] is not None:
        external['title'] = repo_data['name']

    for field in external_fields:
        if field in repo_data and repo_data[field] is not None:
            external[field] = repo_data[field]

    # Special handling: convert primary language to languages list
    if 'language' in repo_data and repo_data['language'] is not None:
        external['languages'] = [repo_data['language']]

    # Add people names based on contributors
    if 'contributors' in repo_data and repo_data['contributors']:
        people_names = []
        for contributor_username in repo_data['contributors']:
            if contributor_username in people_map:
                people_names.append(people_map[contributor_username])

        if people_names:
            external['people'] = people_names

    return external


def compute_top_level_keys(
    external: dict[str, Any],
    include: dict[str, Any],
    exclude: dict[str, Any],
    override: dict[str, Any]
) -> dict[str, Any]:
    """
    Compute top-level frontmatter keys based on external, include, exclude, and override.

    Logic:
    1. Start with values from external
    2. For list values: add items from include
    3. For list values: remove items from exclude
    4. Apply override (replaces any previous value)

    Keys computed: title, people, description, website, latest_release, languages
    """
    result = {}

    # Keys to process
    keys_to_process = ['title', 'people', 'description', 'website', 'latest_release', 'languages']

    for key in keys_to_process:
        # Start with external value
        value = external.get(key)

        # Handle list values with include/exclude
        if isinstance(value, list) and key in include:
            # Add items from include
            include_items = include.get(key, [])
            if isinstance(include_items, list):
                value = list(value)  # Make a copy
                value.extend(include_items)
                # Deduplicate while preserving order
                seen = set()
                value = [x for x in value if not (x in seen or seen.add(x))]

        if isinstance(value, list) and key in exclude:
            # Remove items from exclude
            exclude_items = exclude.get(key, [])
            if isinstance(exclude_items, list):
                value = [x for x in value if x not in exclude_items]

        # Apply override if present
        if key in override:
            value = override[key]

        # Only set if we have a value
        if value is not None:
            result[key] = value

    return result


def process_software_directory(
    software_dir: Path,
    repos_dict: dict[str, dict[str, Any]],
    people_map: dict[str, str]
) -> tuple[int, int, int]:
    """
    Process all _index.md files in software directories.

    Returns:
        tuple: (updated_count, skipped_count, error_count)
    """
    updated_count = 0
    skipped_count = 0
    error_count = 0

    # Find all _index.md files
    index_files = list(software_dir.glob("*/_index.md"))

    if not index_files:
        console.print("[yellow]Warning:[/] No _index.md files found in content/software")
        return 0, 0, 0

    console.print(f"\n[cyan]Found {len(index_files)} software directories[/]\n")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Processing...", total=len(index_files))

        for index_file in index_files:
            software_name = index_file.parent.name
            progress.update(task, description=f"[cyan]{software_name}")

            try:
                # Read the file
                content = index_file.read_text(encoding='utf-8')

                # Parse frontmatter
                frontmatter, yaml_section, remaining_content = parse_frontmatter(content)

                if not frontmatter:
                    console.print(f"  [yellow]Warning:[/] No frontmatter in {software_name}/_index.md")
                    skipped_count += 1
                    progress.advance(task)
                    continue

                # Check if github field exists
                github_repo = frontmatter.get('github')
                if not github_repo:
                    console.print(f"  [dim]Skipped {software_name}: no 'github' field[/]")
                    skipped_count += 1
                    progress.advance(task)
                    continue

                # Look up repo in github-repos.toml
                repo_data = repos_dict.get(github_repo)
                if not repo_data:
                    console.print(f"  [yellow]Warning:[/] Repository '{github_repo}' not found in github-repos.toml")
                    skipped_count += 1
                    progress.advance(task)
                    continue

                # Extract external metadata
                external = extract_external_metadata(repo_data, people_map)

                # Always update - never skip
                # Update external in frontmatter
                frontmatter['external'] = external

                # Get include, exclude, override from frontmatter (if they exist)
                include = frontmatter.get('include', {})
                exclude = frontmatter.get('exclude', {})
                override = frontmatter.get('override', {})

                # Compute top-level keys
                top_level = compute_top_level_keys(external, include, exclude, override)

                # Update top-level keys in frontmatter
                for key, value in top_level.items():
                    frontmatter[key] = value

                # Write back
                write_frontmatter(index_file, frontmatter, remaining_content)

                console.print(f"  [green]✓[/] Updated {software_name}")
                updated_count += 1

            except Exception as e:
                console.print(f"  [bold red]Error:[/] Failed to process {software_name}: {e}")
                error_count += 1

            progress.advance(task)

    return updated_count, skipped_count, error_count


def main() -> None:
    """Main function to orchestrate the script."""
    console.print("\n[bold blue]Software Frontmatter Updater[/]\n")

    # Set up paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    software_dir = project_root / "content" / "software"
    people_dir = project_root / "content" / "people"
    repos_file = project_root / "data" / "github-repos.toml"

    console.print(f"[dim]Software directory: {software_dir}[/]")
    console.print(f"[dim]People directory:   {people_dir}[/]")
    console.print(f"[dim]GitHub repos data:  {repos_file}[/]")

    # Check if directories exist
    if not software_dir.exists():
        console.print(f"[bold red]Error:[/] Software directory not found: {software_dir}")
        sys.exit(1)

    # Load repository data
    repos_dict = load_repos_data(repos_file)

    # Load people mapping
    people_map = load_people_mapping(people_dir)

    # Process all software directories
    updated, skipped, errors = process_software_directory(software_dir, repos_dict, people_map)

    # Summary
    console.print("\n[bold]Summary:[/]")
    console.print(f"  [green]✓[/] Updated:  {updated}")
    console.print(f"  [dim]○[/] Skipped:  {skipped}")
    if errors > 0:
        console.print(f"  [red]✗[/] Errors:   {errors}")

    if errors > 0:
        sys.exit(1)

    console.print("\n[bold green]✓ Done![/]\n")


if __name__ == "__main__":
    main()
