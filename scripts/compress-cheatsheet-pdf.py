#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pikepdf>=9.0",
#     "pillow>=10.0.0",
#     "rich>=13.0.0",
# ]
# ///
"""
Compress cheat sheet PDFs without losing accessibility tags.

Ghostscript produces smaller files but drops the structure tree (tags) that
screen readers rely on. This script instead:

1. downsamples raster images whose effective resolution exceeds --max-ppi
   (soft masks are downsampled along with their image; ICC color spaces and
   JPEG encoding are kept),
2. re-packs the file losslessly (object streams, recompressed Flate streams),
3. verifies the result (same page count, same extracted word count, same
   tagged status, rendered pages visually unchanged) and keeps it only if it
   is smaller. Otherwise the original is left untouched.

Requires poppler (`pdfimages`, `pdftotext`, `pdftoppm`, `pdfinfo`).

Usage:
    scripts/compress-cheatsheet-pdf.py content/resources/cheatsheets/tidyr/*.pdf
    scripts/compress-cheatsheet-pdf.py input.pdf -o output.pdf
"""

import argparse
import io
import math
import shutil
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path

import pikepdf
from pikepdf import Name, PdfImage
from PIL import Image, ImageChops, ImageStat
from rich.console import Console

console = Console(stderr=True, width=200)

JPEG_QUALITY = 85
MAX_RMSE = 0.02  # normalized RMSE between renders of the original and result
MIN_SAVING = 0.02  # keep the result only if it is at least 2% smaller


def image_ppi(pdf_path: Path) -> dict[int, float]:
    """Map image object number to its lowest effective ppi on any page."""
    out = subprocess.run(
        ["pdfimages", "-list", str(pdf_path)], capture_output=True, text=True
    ).stdout
    ppi: dict[int, float] = {}
    for line in out.splitlines()[2:]:
        cols = line.split()
        if len(cols) < 14 or cols[2] != "image":
            continue
        try:
            obj, x_ppi, y_ppi = int(cols[10]), float(cols[12]), float(cols[13])
        except ValueError:
            continue
        effective = max(x_ppi, y_ppi)
        ppi[obj] = min(ppi.get(obj, math.inf), effective)
    return ppi


def encode(stream: pikepdf.Stream, image: Image.Image, as_jpeg: bool) -> None:
    """Write a PIL image into a PDF image stream."""
    if as_jpeg:
        buf = io.BytesIO()
        image.save(buf, "JPEG", quality=JPEG_QUALITY, optimize=True)
        stream.write(buf.getvalue(), filter=Name.DCTDecode)
    else:
        stream.write(zlib.compress(image.tobytes(), 9), filter=Name.FlateDecode)
    stream.Width, stream.Height = image.width, image.height
    stream.BitsPerComponent = 8
    for key in ("/DecodeParms", "/Decode"):
        if key in stream:
            del stream[key]


def downsample_images(pdf: pikepdf.Pdf, ppi: dict[int, float], max_ppi: float) -> int:
    """Downsample images above max_ppi in place. Returns the number changed."""
    changed = 0
    for obj in pdf.objects:
        if not isinstance(obj, pikepdf.Stream) or obj.get("/Subtype") != Name.Image:
            continue
        if obj.get("/ImageMask", False):
            continue
        effective = ppi.get(obj.objgen[0])
        if not effective or effective == math.inf or effective <= max_ppi * 1.1:
            continue
        try:
            image = PdfImage(obj).as_pil_image()
        except Exception:
            continue

        alpha = None
        if image.mode in ("RGBA", "LA"):
            alpha = image.getchannel("A")
            image = image.convert("RGB" if image.mode == "RGBA" else "L")
        elif image.mode == "P":
            image = image.convert("RGB")
        if image.mode not in ("L", "RGB"):
            continue  # e.g. CMYK, 1-bit: leave as is

        scale = max_ppi / effective
        size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
        image = image.resize(size, Image.Resampling.LANCZOS)

        color_space = obj.get("/ColorSpace")
        keep_icc = (
            isinstance(color_space, pikepdf.Array)
            and color_space[0] == Name.ICCBased
            and int(color_space[1].get("/N", 0)) == len(image.getbands())
        )
        was_jpeg = obj.get("/Filter") in (Name.DCTDecode, pikepdf.Array([Name.DCTDecode]))
        encode(obj, image, as_jpeg=was_jpeg)
        if not keep_icc:
            obj.ColorSpace = Name.DeviceGray if image.mode == "L" else Name.DeviceRGB

        if alpha is not None and "/SMask" in obj:
            smask = obj.SMask
            encode(smask, alpha.resize(size, Image.Resampling.LANCZOS), as_jpeg=False)
            smask.ColorSpace = Name.DeviceGray
        changed += 1
    return changed


def page_count(path: Path) -> int:
    with pikepdf.open(path) as pdf:
        return len(pdf.pages)


def word_count(path: Path) -> int:
    text = subprocess.run(
        ["pdftotext", "-q", str(path), "-"], capture_output=True, text=True
    ).stdout
    return len(text.split())


def is_tagged(path: Path) -> bool:
    info = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True).stdout
    return any(l.startswith("Tagged:") and l.split()[-1] == "yes" for l in info.splitlines())


def render(path: Path, out_dir: Path, prefix: str) -> list[Path]:
    subprocess.run(
        ["pdftoppm", "-r", "60", "-png", str(path), str(out_dir / prefix)],
        capture_output=True,
    )
    return sorted(out_dir.glob(f"{prefix}*.png"))


def max_rmse(original: Path, result: Path) -> float:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        a_pages, b_pages = render(original, tmp_dir, "a"), render(result, tmp_dir, "b")
        if len(a_pages) != len(b_pages):
            return 1.0
        worst = 0.0
        for a_path, b_path in zip(a_pages, b_pages):
            a, b = Image.open(a_path).convert("RGB"), Image.open(b_path).convert("RGB")
            if a.size != b.size:
                return 1.0
            diff = ImageStat.Stat(ImageChops.difference(a, b))
            rmse = math.sqrt(sum(v for v in diff.sum2) / (3 * a.width * a.height)) / 255
            worst = max(worst, rmse)
        return worst


def compress(src: Path, dst: Path, max_ppi: float) -> tuple[bool, str]:
    """Compress src into dst. Returns (kept_result, message)."""
    ppi = image_ppi(src)
    with tempfile.TemporaryDirectory() as tmp:
        candidate = Path(tmp) / "out.pdf"
        with pikepdf.open(src) as pdf:
            changed = downsample_images(pdf, ppi, max_ppi)
            pdf.save(
                candidate,
                compress_streams=True,
                recompress_flate=True,
                object_stream_mode=pikepdf.ObjectStreamMode.generate,
            )

        before, after = src.stat().st_size, candidate.stat().st_size
        if after > before * (1 - MIN_SAVING):
            if dst != src:
                shutil.copyfile(src, dst)
            return False, f"kept original ({before / 1e6:.2f} MB; no gain)"

        checks = []
        if page_count(src) != page_count(candidate):
            checks.append("page count")
        if word_count(src) != word_count(candidate):
            checks.append("word count")
        if is_tagged(src) != is_tagged(candidate):
            checks.append("tagged status")
        rmse = max_rmse(src, candidate)
        if rmse > MAX_RMSE:
            checks.append(f"render RMSE {rmse:.3f}")
        if checks:
            if dst != src:
                shutil.copyfile(src, dst)
            return False, f"kept original (failed check: {', '.join(checks)})"

        shutil.copyfile(candidate, dst)
        return True, (
            f"{before / 1e6:.2f} MB → {after / 1e6:.2f} MB "
            f"({changed} images downsampled, RMSE {rmse:.3f})"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("pdfs", nargs="+", type=Path, help="PDF files (compressed in place)")
    parser.add_argument("-o", "--output", type=Path, help="Output path (single input only)")
    parser.add_argument("--max-ppi", type=float, default=300, help="Image resolution cap (default: 300)")
    args = parser.parse_args()

    if args.output and len(args.pdfs) != 1:
        parser.error("--output requires exactly one input PDF")

    for src in args.pdfs:
        dst = args.output or src
        try:
            kept, message = compress(src, dst, args.max_ppi)
        except Exception as e:  # keep going for batch runs
            console.print(f"[red]✗[/] {src}: {e}")
            continue
        mark = "[green]✓[/]" if kept else "[yellow]–[/]"
        console.print(f"{mark} {src}: {message}")


if __name__ == "__main__":
    sys.exit(main())
