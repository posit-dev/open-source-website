#!/usr/bin/env python3
"""
Download content from production site for local development.

This script downloads:
- Cheatsheet thumbnail images
- Video transcription files
- Video thumbnail images

Usage:
    python scripts/download-production-content.py --cheatsheets
    python scripts/download-production-content.py --videos
    python scripts/download-production-content.py --all
"""

import argparse
import requests
from pathlib import Path
import sys

PROD_URL = "https://posit-open-source.netlify.app"
CONTENT_DIR = Path(__file__).parent.parent / "content"

def download_file(url, local_path):
    """Download a file from URL to local path."""
    local_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            local_path.write_bytes(response.content)
            print(f"✓ Downloaded: {local_path.relative_to(CONTENT_DIR)}")
            return True
        elif response.status_code == 404:
            print(f"✗ Not found: {url}")
            return False
        else:
            print(f"✗ Error {response.status_code}: {url}")
            return False
    except Exception as e:
        print(f"✗ Failed: {url} - {e}")
        return False

def download_cheatsheets():
    """Download cheatsheet thumbnail images."""
    print("\n📄 Downloading cheatsheet thumbnails...")

    cheatsheets_dir = CONTENT_DIR / "resources" / "cheatsheets"
    if not cheatsheets_dir.exists():
        print(f"✗ Directory not found: {cheatsheets_dir}")
        return

    downloaded = 0
    for cheatsheet_dir in cheatsheets_dir.iterdir():
        if not cheatsheet_dir.is_dir() or cheatsheet_dir.name.startswith('.'):
            continue

        index_file = cheatsheet_dir / "_index.md"
        if not index_file.exists():
            continue

        # Read frontmatter to find thumbnail files
        content = index_file.read_text()
        if "thumbnails:" not in content:
            continue

        # Parse thumbnails from frontmatter
        in_thumbnails = False
        for line in content.split('\n'):
            if line.strip() == "thumbnails:":
                in_thumbnails = True
                continue
            elif in_thumbnails:
                if line.startswith('- '):
                    thumb_file = line.replace('- ', '').strip()
                    local_path = cheatsheet_dir / thumb_file

                    if local_path.exists():
                        print(f"⊙ Already exists: {local_path.relative_to(CONTENT_DIR)}")
                        continue

                    url = f"{PROD_URL}/resources/cheatsheets/{cheatsheet_dir.name}/{thumb_file}"
                    if download_file(url, local_path):
                        downloaded += 1
                elif line and not line.startswith(' ') and not line.startswith('-'):
                    break

    print(f"\n✓ Downloaded {downloaded} cheatsheet images")

def download_videos():
    """Download video transcripts and thumbnails."""
    print("\n🎥 Downloading video content...")

    videos_dir = CONTENT_DIR / "resources" / "videos"
    if not videos_dir.exists():
        print(f"✗ Directory not found: {videos_dir}")
        return

    downloaded = 0
    for video_dir in videos_dir.iterdir():
        if not video_dir.is_dir() or video_dir.name.startswith('.'):
            continue

        index_file = video_dir / "_index.md"
        if not index_file.exists():
            continue

        # Download transcription.txt
        transcript_local = video_dir / "transcription.txt"
        if not transcript_local.exists():
            transcript_url = f"{PROD_URL}/resources/videos/{video_dir.name}/transcription.txt"
            if download_file(transcript_url, transcript_local):
                downloaded += 1
        else:
            print(f"⊙ Already exists: {transcript_local.relative_to(CONTENT_DIR)}")

        # Download thumbnail.jpg
        thumbnail_local = video_dir / "thumbnail.jpg"
        if not thumbnail_local.exists():
            thumbnail_url = f"{PROD_URL}/resources/videos/{video_dir.name}/thumbnail.jpg"
            if download_file(thumbnail_url, thumbnail_local):
                downloaded += 1
        else:
            print(f"⊙ Already exists: {thumbnail_local.relative_to(CONTENT_DIR)}")

    print(f"\n✓ Downloaded {downloaded} video files")

def main():
    parser = argparse.ArgumentParser(description="Download production content for local development")
    parser.add_argument("--cheatsheets", action="store_true", help="Download cheatsheet thumbnails")
    parser.add_argument("--videos", action="store_true", help="Download video transcripts and thumbnails")
    parser.add_argument("--all", action="store_true", help="Download all content")

    args = parser.parse_args()

    if not any([args.cheatsheets, args.videos, args.all]):
        parser.print_help()
        sys.exit(1)

    print(f"🌐 Downloading content from: {PROD_URL}")
    print(f"📁 Saving to: {CONTENT_DIR}")

    if args.all or args.cheatsheets:
        download_cheatsheets()

    if args.all or args.videos:
        download_videos()

    print("\n✅ Done!")

if __name__ == "__main__":
    main()
