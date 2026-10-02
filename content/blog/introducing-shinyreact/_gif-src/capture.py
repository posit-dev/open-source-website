"""Regenerate the post's inline media.

- hello-app.gif: the shinyreact `examples/01-hello` Old Faithful app
  (copied into ./hello-app), recorded frame-by-frame while the bin-count
  slider rests, then moves through a few values.
- plotomics-live.mp4: re-encoded from the screen recording used in the
  posit::conf(2026) talk (downloaded on demand, cached next to this file).

Usage (requires ffmpeg on PATH):

    uv run --with playwright --with shinyreact --with "shiny>=1.8" python capture.py

Outputs are written to the post directory (the parent of this folder).
"""

import pathlib
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
POST_DIR = HERE.parent
APP = HERE / "hello-app" / "app.py"

WIDTH, HEIGHT = 960, 540  # 16:9
FPS = 10
# (target bin count, seconds to slide there, seconds to rest afterwards)
MOVES = [(30, 0.0, 2.0), (8, 0.5, 1.5), (45, 0.7, 1.5), (20, 0.5, 1.5), (30, 0.4, 2.0)]

PLOTOMICS_MP4 = "https://schloerke.com/presentation-2026-09-15-posit-conf-shinyreact/images/plotomics-live.mp4"
PLOTOMICS_CACHE = HERE / "plotomics-live.mp4"

PALETTE = "split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer:bayer_scale=4"

# React only sees a range input change when the native value setter runs and
# an `input` event bubbles; `page.fill()` won't do it for type=range.
SET_BINS = """(v) => {
  const el = document.querySelector('#bins');
  Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set.call(el, String(v));
  el.dispatchEvent(new Event('input', { bubbles: true }));
}"""


def free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def wait_for(url: str) -> None:
    for _ in range(60):
        try:
            urllib.request.urlopen(url, timeout=1)
            return
        except OSError:
            time.sleep(0.5)
    raise SystemExit("app did not start")


def to_gif(frames_glob: str, out: pathlib.Path, extra: list[str] = ()) -> None:
    subprocess.run(
        ["ffmpeg", "-y", "-framerate", str(FPS), "-i", frames_glob, *extra,
         "-vf", PALETTE, "-loop", "0", str(out)],
        check=True,
        capture_output=True,
    )
    print(f"{out.name}: {out.stat().st_size / 1024:.0f} KB")


def record_hello() -> None:
    port = free_port()
    url = f"http://127.0.0.1:{port}/"
    app = subprocess.Popen(
        [sys.executable, "-m", "shiny", "run", "--port", str(port), str(APP)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        wait_for(url)
        with sync_playwright() as p, tempfile.TemporaryDirectory() as tmp:
            frames = pathlib.Path(tmp)
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": WIDTH, "height": HEIGHT})
            page.goto(url)
            page.wait_for_selector("svg rect")  # first histogram rendered
            page.wait_for_timeout(500)

            n = 0
            current = 30
            for target, slide_s, rest_s in MOVES:
                steps = int(slide_s * FPS)
                for i in range(1, steps + 1):
                    page.evaluate(SET_BINS, round(current + (target - current) * i / steps))
                    page.wait_for_timeout(1000 // FPS)
                    page.screenshot(path=str(frames / f"frame_{n:03d}.png"))
                    n += 1
                current = target
                for _ in range(int(rest_s * FPS)):
                    page.wait_for_timeout(1000 // FPS)
                    page.screenshot(path=str(frames / f"frame_{n:03d}.png"))
                    n += 1
                print(f"bins={target}: {n} frames so far", end="\r")
            browser.close()
            print()
            to_gif(str(frames / "frame_%03d.png"), POST_DIR / "hello-app.gif")
    finally:
        app.terminate()
        app.wait()


def convert_plotomics() -> None:
    # Stays an mp4: a million-point scatter defeats GIF palettes (16 MB at
    # 960px vs 2.7 MB h264), and the site already plays local mp4 in posts.
    if not PLOTOMICS_CACHE.exists():
        print("downloading plotomics-live.mp4...")
        urllib.request.urlretrieve(PLOTOMICS_MP4, PLOTOMICS_CACHE)
    out = POST_DIR / "plotomics-live.mp4"
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(PLOTOMICS_CACHE), "-an",
         "-vf", f"scale={WIDTH}:-2", "-c:v", "libx264", "-crf", "26",
         "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
         str(out)],
        check=True,
        capture_output=True,
    )
    print(f"{out.name}: {out.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    record_hello()
    convert_plotomics()
