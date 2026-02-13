#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "requests>=2.31.0",
# ]
# ///

"""
Download software images from GitHub README.

For each software directory without an image, downloads the readme_image
from GitHub and updates the frontmatter.
"""

import argparse
import sys
from pathlib import Path
from typing import Any

import requests
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


def write_frontmatter(file_path: Path, frontmatter: dict[str, Any], remaining_content: str) -> None:
    """Write updated frontmatter back to the markdown file."""
    yaml_content = yaml.dump(
        frontmatter,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        indent=2
    ).strip()

    new_content = f"---\n{yaml_content}\n---\n{remaining_content}"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)


def download_image(url: str, output_path: Path, try_master_fallback: bool = True) -> tuple[bool, str | None]:
    """
    Download image from URL to output path.

    Tries 'main' branch first, then 'master' if that fails with 404.

    Returns:
        tuple: (success: bool, final_url: str | None)
    """
    try:
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()

        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return True, url
    except requests.exceptions.HTTPError as e:
        # If 404 and we haven't tried master yet, try with master branch
        # Only do this for raw.githubusercontent.com URLs
        if (e.response.status_code == 404 and
            try_master_fallback and
            '/main/' in url and
            'raw.githubusercontent.com' in url):
            master_url = url.replace('/main/', '/master/')
            console.print(f"[dim]Trying master branch:[/] {master_url}")
            return download_image(master_url, output_path, try_master_fallback=False)
        else:
            console.print(f"[red]Error downloading:[/] {e}")
            return False, None
    except Exception as e:
        console.print(f"[red]Error downloading:[/] {e}")
        return False, None


def get_image_filename(url: str) -> str:
    """Extract filename from URL."""
    return Path(url).name


def process_software_directory(
    software_dir: Path,
    dry_run: bool
) -> tuple[int, int, int]:
    """
    Process all software directories to download missing images.

    Returns:
        tuple: (downloaded_count, skipped_count, error_count)
    """
    downloaded_count = 0
    skipped_count = 0
    error_count = 0

    # Find all software directories
    software_dirs = [d for d in software_dir.iterdir() if d.is_dir()]

    if not software_dirs:
        console.print("[yellow]Warning:[/] No software directories found")
        return 0, 0, 0

    console.print(f"\n[cyan]Found {len(software_dirs)} software directories[/]\n")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Processing...", total=len(software_dirs))

        for dir_path in software_dirs:
            software_name = dir_path.name
            progress.update(task, description=f"[cyan]{software_name}")

            index_file = dir_path / "_index.md"

            if not index_file.exists():
                console.print(f"  [dim]Skipped {software_name}: no _index.md[/]")
                skipped_count += 1
                progress.advance(task)
                continue

            try:
                # Read and parse frontmatter
                content = index_file.read_text(encoding='utf-8')
                frontmatter, yaml_section, remaining_content = parse_frontmatter(content)

                if not frontmatter:
                    console.print(f"  [yellow]Warning:[/] No frontmatter in {software_name}/_index.md")
                    skipped_count += 1
                    progress.advance(task)
                    continue

                # Check if image already exists
                if frontmatter.get('image'):
                    console.print(f"  [dim]Skipped {software_name}: image already exists[/]")
                    skipped_count += 1
                    progress.advance(task)
                    continue

                # Get GitHub repo and readme_image
                github_repo = frontmatter.get('github')
                external = frontmatter.get('external', {})
                readme_image = external.get('readme_image')

                if not github_repo or not readme_image:
                    console.print(f"  [dim]Skipped {software_name}: missing github or readme_image[/]")
                    skipped_count += 1
                    progress.advance(task)
                    continue

                # Construct image URL
                # If readme_image is already a full URL, use it directly
                if readme_image.startswith(('http://', 'https://')):
                    image_url = readme_image
                else:
                    # Otherwise construct raw GitHub URL
                    # Format: https://raw.githubusercontent.com/{owner}/{repo}/main/{path}
                    image_url = f"https://raw.githubusercontent.com/{github_repo}/main/{readme_image}"

                # Get filename
                image_filename = get_image_filename(readme_image)

                if dry_run:
                    branch_info = " (will try main/master)" if image_url.startswith("https://raw.githubusercontent.com/") else ""
                    console.print(f"  [green]✓[/] Would download {software_name}: {image_url} -> {image_filename}{branch_info}")
                    downloaded_count += 1
                    progress.advance(task)
                    continue

                # Download image
                output_path = dir_path / image_filename
                console.print(f"  [cyan]Downloading:[/] {image_url}")

                success, final_url = download_image(image_url, output_path)
                if success:
                    # Update frontmatter
                    frontmatter['image'] = image_filename
                    write_frontmatter(index_file, frontmatter, remaining_content)

                    # Show branch info only for GitHub URLs
                    if final_url and 'raw.githubusercontent.com' in final_url:
                        branch = "master" if "/master/" in final_url else "main"
                        console.print(f"  [green]✓[/] Downloaded {software_name}: {image_filename} (from {branch})")
                    else:
                        console.print(f"  [green]✓[/] Downloaded {software_name}: {image_filename}")
                    downloaded_count += 1
                else:
                    console.print(f"  [red]✗[/] Failed {software_name}")
                    error_count += 1

            except Exception as e:
                console.print(f"  [bold red]Error:[/] Failed to process {software_name}: {e}")
                error_count += 1

            progress.advance(task)

    return downloaded_count, skipped_count, error_count


def main() -> None:
    """Main function to orchestrate the script."""
    parser = argparse.ArgumentParser(
        description="Download software images from GitHub README."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be downloaded without actually downloading",
    )
    args = parser.parse_args()

    console.print("\n[bold blue]Software Image Downloader[/]\n")

    if args.dry_run:
        console.print("[yellow]DRY RUN MODE - No files will be downloaded[/]\n")

    # Set up paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    software_dir = project_root / "content" / "software"

    console.print(f"[dim]Software directory: {software_dir}[/]\n")

    # Check if software directory exists
    if not software_dir.exists():
        console.print(f"[bold red]Error:[/] Software directory not found: {software_dir}")
        sys.exit(1)

    # Process all software directories
    downloaded, skipped, errors = process_software_directory(software_dir, args.dry_run)

    # Summary
    console.print("\n[bold]Summary:[/]")
    console.print(f"  [green]✓[/] Downloaded: {downloaded}")
    console.print(f"  [dim]○[/] Skipped:    {skipped}")
    if errors > 0:
        console.print(f"  [red]✗[/] Errors:     {errors}")

    if args.dry_run:
        console.print("\n[yellow]DRY RUN - No changes were made[/]")

    console.print("\n[bold green]✓ Done![/]\n")

    if errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
