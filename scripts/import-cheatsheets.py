#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "requests>=2.31.0",
#     "beautifulsoup4>=4.12.0",
#     "pyyaml>=6.0",
#     "lxml>=5.0.0",
# ]
# ///
"""
Import cheatsheets from rstudio.github.io/cheatsheets
Creates _index.md files with frontmatter for each cheatsheet.
Downloads PDFs and creates thumbnails.
"""

import re
import subprocess
import sys
from pathlib import Path
from datetime import date
from typing import Dict, List, Optional

import requests
from bs4 import BeautifulSoup
import yaml

BASE_URL = "https://rstudio.github.io/cheatsheets"
HTML_BASE_URL = f"{BASE_URL}/html"
CONTENT_DIR = Path("content/resources/cheatsheets")

CHEATSHEET_SLUGS = [
    "data-import",
    "data-transformation",
    "data-visualization",
    "factors",
    "great-tables",
    "gt",
    "keras",
    "lubridate",
    "nlp-with-llms",
    "package-development",
    "plotnine",
    "plumber",
    "posit-team",
    "positron",
    "purrr",
    "quarto",
    "reticulate",
    "rmarkdown",
    "rstudio-ide",
    "shiny",
    "shiny-python",
    "shinychat",
    "sparklyr",
    "strings",
    "tidyr",
]

SLUG_TO_SOFTWARE = {
    "data-import": ["readr", "readxl", "haven"],
    "data-transformation": ["dplyr"],
    "data-visualization": ["ggplot2"],
    "factors": ["forcats"],
    "great-tables": ["great-tables"],
    "gt": ["gt"],
    "keras": ["keras"],
    "lubridate": ["lubridate"],
    "nlp-with-llms": [],
    "package-development": ["devtools", "usethis"],
    "plotnine": ["plotnine"],
    "plumber": ["plumber"],
    "posit-team": [],
    "positron": ["positron"],
    "purrr": ["purrr"],
    "quarto": ["quarto"],
    "reticulate": ["reticulate"],
    "rmarkdown": ["rmarkdown"],
    "rstudio-ide": [],
    "shiny": ["shiny"],
    "shiny-python": ["shiny"],
    "shinychat": ["shinychat"],
    "sparklyr": ["sparklyr"],
    "strings": ["stringr"],
    "tidyr": ["tidyr"],
}

SLUG_TO_LANGUAGE = {
    "data-import": ["R"],
    "data-transformation": ["R"],
    "data-visualization": ["R"],
    "factors": ["R"],
    "great-tables": ["Python"],
    "gt": ["R"],
    "keras": ["R", "Python"],
    "lubridate": ["R"],
    "nlp-with-llms": ["Python"],
    "package-development": ["R"],
    "plotnine": ["Python"],
    "plumber": ["R"],
    "posit-team": [],
    "positron": [],
    "purrr": ["R"],
    "quarto": [],
    "reticulate": ["R", "Python"],
    "rmarkdown": ["R"],
    "rstudio-ide": ["R"],
    "shiny": ["R"],
    "shiny-python": ["Python"],
    "shinychat": ["Python"],
    "sparklyr": ["R"],
    "strings": ["R"],
    "tidyr": ["R"],
}


def fetch_cheatsheet_page(slug: str) -> Optional[BeautifulSoup]:
    """Fetch and parse a cheatsheet HTML page."""
    url = f"{HTML_BASE_URL}/{slug}.html"
    print(f"Fetching {url}...")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


def extract_title(soup: BeautifulSoup) -> str:
    """Extract the title from the page."""
    title_tag = soup.find("title")
    if title_tag:
        title = title_tag.text.strip()
        title = re.sub(r"\s*::\s*Cheat\s*Sheet\s*$", "", title, flags=re.IGNORECASE)
        return title

    h1_tag = soup.find("h1")
    if h1_tag:
        title = h1_tag.text.strip()
        title = re.sub(r"\s*::\s*Cheat\s*Sheet\s*$", "", title, flags=re.IGNORECASE)
        return title

    return "Untitled Cheatsheet"


def extract_description(soup: BeautifulSoup, slug: str) -> str:
    """Generate a description for the cheatsheet."""
    title = extract_title(soup)
    return f"Quick reference guide for {title.lower()}."


def extract_download_url(soup: BeautifulSoup, slug: str) -> str:
    """Extract the PDF download URL."""
    download_link = soup.find("a", href=re.compile(r"\.\.\/.*\.pdf"))
    if download_link:
        href = download_link.get("href")
        if href.startswith("../"):
            href = href[3:]
        return f"{BASE_URL}/{href}"

    return f"{BASE_URL}/{slug}.pdf"


def extract_translations(soup: BeautifulSoup) -> List[tuple[str, str]]:
    """Extract translation information as (language, url) tuples."""
    translations = []

    translation_sections = soup.find_all(
        string=re.compile(r"Translations\s*\(PDF\)", re.IGNORECASE)
    )

    for section in translation_sections:
        parent = section.find_parent()
        if parent:
            ul = parent.find_next("ul")
            if ul:
                for li in ul.find_all("li"):
                    link = li.find("a", href=re.compile(r"\.\.\/translations\/.*\.pdf"))
                    if link:
                        language = link.text.strip()
                        href = link.get("href")
                        if href.startswith("../"):
                            href = href[3:]
                        url = f"{BASE_URL}/{href}"
                        translations.append((language, url))

    return translations


def download_pdf(url: str, dest_path: Path) -> bool:
    """Download a PDF file to the specified destination."""
    print(f"    Downloading PDF: {url}")
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        with open(dest_path, "wb") as f:
            f.write(response.content)

        print(f"    ✓ Saved to: {dest_path}")
        return True
    except Exception as e:
        print(f"    ✗ Error downloading {url}: {e}")
        return False


def run_create_thumbnails(pdf_path: Path) -> None:
    """Run create-cheatsheet-thumbnails.py to generate thumbnails and update _index.md."""
    script = Path(__file__).parent / "create-cheatsheet-thumbnails.py"
    result = subprocess.run(
        [sys.executable, str(script), "--pdf", str(pdf_path)],
        capture_output=True,
        text=True,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="")
    if result.returncode != 0:
        print(f"    ✗ Thumbnail creation failed (exit code {result.returncode})")


def create_cheatsheet_frontmatter(
    slug: str,
    title: str,
    description: str,
    pdf_filename: str,
    translation_filenames: List[Dict[str, str]],
    software: List[str],
    languages: List[str],
) -> Dict:
    """Create the frontmatter dictionary for a cheatsheet."""
    frontmatter = {
        "title": title,
        "resource_type": "cheatsheet",
        "date": date.today().isoformat(),
        "description": description,
        "download_url": pdf_filename,
    }

    if software:
        frontmatter["software"] = software

    if languages:
        frontmatter["languages"] = languages

    if translation_filenames:
        frontmatter["translations"] = translation_filenames

    return frontmatter


def create_cheatsheet_file(slug: str, frontmatter: Dict, body: str = "") -> None:
    """Create the _index.md file for a cheatsheet."""
    cheatsheet_dir = CONTENT_DIR / slug
    cheatsheet_dir.mkdir(parents=True, exist_ok=True)

    index_file = cheatsheet_dir / "_index.md"

    if index_file.exists():
        print(f"  ⚠️  File already exists: {index_file}")
        response = input("  Overwrite? (y/n): ")
        if response.lower() != "y":
            print("  Skipped.")
            return

    with open(index_file, "w") as f:
        f.write("---\n")
        yaml.dump(
            frontmatter,
            f,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
        )
        f.write("---\n")
        if body:
            f.write("\n")
            f.write(body)

    print(f"  ✓ Created: {index_file}")


def process_cheatsheet(slug: str) -> None:
    """Process a single cheatsheet."""
    print(f"\nProcessing: {slug}")
    print("-" * 60)

    cheatsheet_dir = CONTENT_DIR / slug
    cheatsheet_dir.mkdir(parents=True, exist_ok=True)
    print(f"  Directory: {cheatsheet_dir}")

    soup = fetch_cheatsheet_page(slug)
    if not soup:
        print("  ✗ Failed to fetch page")
        return

    title = extract_title(soup)
    description = extract_description(soup, slug)
    download_url = extract_download_url(soup, slug)
    translations = extract_translations(soup)
    software = SLUG_TO_SOFTWARE.get(slug, [])
    languages = SLUG_TO_LANGUAGE.get(slug, [])

    print(f"  Title: {title}")
    print(f"  Description: {description}")
    print(f"  Download URL: {download_url}")
    print(f"  Translations: {len(translations)} found")
    print(f"  Software: {software}")
    print(f"  Languages: {languages}")

    pdf_filename = f"{slug}.pdf"
    pdf_path = cheatsheet_dir / pdf_filename
    if not download_pdf(download_url, pdf_path):
        print("  ✗ Failed to download main PDF, skipping...")
        return

    translation_filenames = []
    for language, trans_url in translations:
        trans_filename = Path(trans_url).name
        trans_path = cheatsheet_dir / trans_filename

        if download_pdf(trans_url, trans_path):
            translation_filenames.append({language: trans_filename})

    frontmatter = create_cheatsheet_frontmatter(
        slug,
        title,
        description,
        pdf_filename,
        translation_filenames,
        software,
        languages,
    )

    create_cheatsheet_file(slug, frontmatter)
    run_create_thumbnails(pdf_path)


def main():
    """Main function."""
    print("=" * 60)
    print("Importing Cheatsheets")
    print("=" * 60)

    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    for slug in CHEATSHEET_SLUGS:
        try:
            process_cheatsheet(slug)
        except Exception as e:
            print(f"  ✗ Error processing {slug}: {e}")

    print("\n" + "=" * 60)
    print("Import complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
