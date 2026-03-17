#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pillow>=10.0.0",
#     "rich>=13.0.0",
# ]
# ///
"""
Resize oversized images in the content directory to reduce Hugo memory usage.

Scans for images wider than a configurable threshold (default 2400px) and
resizes them proportionally. Original files are backed up with a .original
suffix. Use --undo to restore originals or --clean to remove backups.
"""

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageOps
from rich.console import Console

script_dir = Path(__file__).parent
project_root = script_dir.parent

console = Console(stderr=True)

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif"}


def is_animated_gif(path: Path) -> bool:
    """Check if a GIF file has multiple frames (is animated)."""
    try:
        with Image.open(path) as img:
            try:
                img.seek(1)
                return True
            except EOFError:
                return False
    except Exception:
        return False


def resize_images(
    content_dir: Path,
    max_width: int,
    quality: int,
    dry_run: bool,
    verbose: bool,
) -> None:
    """Find and resize images wider than max_width."""
    console.print(f"\n[bold blue]Resizing images wider than {max_width}px[/]")
    console.print(f"  Directory: {content_dir}")
    if dry_run:
        console.print("  [yellow]Dry run — no files will be changed[/]")
    console.print()

    scanned = 0
    resized = 0
    skipped_backup = 0
    skipped_animated = 0
    skipped_small = 0
    skipped_error = 0
    bytes_before = 0
    bytes_after = 0

    for path in sorted(content_dir.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        if path.name.endswith(".original"):
            continue

        scanned += 1
        backup_path = path.parent / f"{path.name}.original"

        if path.suffix.lower() == ".gif" and is_animated_gif(path):
            skipped_animated += 1
            if verbose:
                console.print(f"  [dim]skip (animated)[/] {path.relative_to(project_root)}")
            continue

        try:
            with Image.open(path) as img:
                width = img.width
        except Exception as e:
            skipped_error += 1
            if verbose:
                console.print(
                    f"  [red]skip (error)[/] {path.relative_to(project_root)}: {e}"
                )
            continue

        if width <= max_width:
            skipped_small += 1
            continue

        if backup_path.exists():
            skipped_backup += 1
            if verbose:
                console.print(
                    f"  [yellow]skip (backup exists)[/] {path.relative_to(project_root)}"
                )
            continue

        size_before = path.stat().st_size
        bytes_before += size_before

        if dry_run:
            console.print(
                f"  [cyan]would resize[/] {path.relative_to(project_root)} "
                f"({width}px -> {max_width}px)"
            )
            resized += 1
            continue

        try:
            with Image.open(path) as img:
                img = ImageOps.exif_transpose(img)
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                resized_img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

                # Back up original
                path.rename(backup_path)

                # Save resized image in original format
                fmt = img.format or path.suffix.lstrip(".").upper()
                save_kwargs = {}
                if fmt in ("JPEG", "JPG"):
                    fmt = "JPEG"
                    save_kwargs["quality"] = quality
                elif fmt == "PNG":
                    save_kwargs["optimize"] = True
                elif fmt == "WEBP":
                    save_kwargs["quality"] = quality

                resized_img.save(path, format=fmt, **save_kwargs)

            size_after = path.stat().st_size
            bytes_after += size_after
            resized += 1

            if verbose:
                saved_pct = (1 - size_after / size_before) * 100 if size_before else 0
                console.print(
                    f"  [green]resized[/] {path.relative_to(project_root)} "
                    f"({width}px -> {max_width}px, {saved_pct:.0f}% smaller)"
                )
        except Exception as e:
            skipped_error += 1
            # Restore backup if we moved it but failed to save
            if backup_path.exists() and not path.exists():
                backup_path.rename(path)
            console.print(
                f"  [red]error[/] {path.relative_to(project_root)}: {e}"
            )

    # Summary
    console.print()
    console.print("[bold]Summary:[/]")
    console.print(f"  Scanned:         {scanned}")
    console.print(f"  Resized:         {resized}")
    console.print(f"  Skipped (small): {skipped_small}")
    if skipped_backup:
        console.print(f"  Skipped (backup exists): {skipped_backup}")
    if skipped_animated:
        console.print(f"  Skipped (animated GIF):  {skipped_animated}")
    if skipped_error:
        console.print(f"  Skipped (error):         {skipped_error}")
    if bytes_before and not dry_run:
        saved = bytes_before - bytes_after
        console.print(
            f"  Size saved:      {saved / 1024 / 1024:.1f} MB "
            f"({bytes_before / 1024 / 1024:.1f} MB -> {bytes_after / 1024 / 1024:.1f} MB)"
        )
    console.print()


def undo(content_dir: Path, verbose: bool) -> None:
    """Restore .original backup files."""
    console.print("\n[bold blue]Restoring original images[/]")
    console.print(f"  Directory: {content_dir}\n")

    restored = 0
    for backup_path in sorted(content_dir.rglob("*.original")):
        if not backup_path.is_file():
            continue
        original_path = backup_path.parent / backup_path.name.removesuffix(".original")
        backup_path.rename(original_path)
        restored += 1
        if verbose:
            console.print(f"  [green]restored[/] {original_path.relative_to(project_root)}")

    console.print(f"\n[bold]Restored {restored} files[/]\n")


def clean(content_dir: Path, verbose: bool) -> None:
    """Remove .original backup files."""
    console.print("\n[bold blue]Removing backup files[/]")
    console.print(f"  Directory: {content_dir}\n")

    removed = 0
    bytes_freed = 0
    for backup_path in sorted(content_dir.rglob("*.original")):
        if not backup_path.is_file():
            continue
        size = backup_path.stat().st_size
        bytes_freed += size
        backup_path.unlink()
        removed += 1
        if verbose:
            console.print(f"  [red]removed[/] {backup_path.relative_to(project_root)}")

    console.print(f"\n[bold]Removed {removed} backups ({bytes_freed / 1024 / 1024:.1f} MB freed)[/]\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Resize oversized images in content/ to reduce Hugo memory usage."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--undo",
        action="store_true",
        help="Restore original images from .original backups",
    )
    group.add_argument(
        "--clean",
        action="store_true",
        help="Remove .original backup files",
    )
    parser.add_argument(
        "--max-width",
        type=int,
        default=2400,
        help="Resize images wider than this (default: 2400)",
    )
    parser.add_argument(
        "--quality",
        type=int,
        default=85,
        help="JPEG/WebP quality for resized images (default: 85)",
    )
    parser.add_argument(
        "--content-dir",
        type=Path,
        default=project_root / "content",
        help="Directory to scan (default: content/)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would be done without changing files",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show per-file actions",
    )
    args = parser.parse_args()

    if not args.content_dir.is_dir():
        console.print(f"[bold red]Error:[/] {args.content_dir} is not a directory")
        sys.exit(1)

    if args.undo:
        undo(args.content_dir, args.verbose)
    elif args.clean:
        clean(args.content_dir, args.verbose)
    else:
        resize_images(
            args.content_dir,
            args.max_width,
            args.quality,
            args.dry_run,
            args.verbose,
        )


if __name__ == "__main__":
    main()
