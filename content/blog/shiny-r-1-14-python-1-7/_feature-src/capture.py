"""Regenerate the post's feature images from the HTML sources in this folder.

- feature.png (static fallback / social preview): screenshot of feature.html,
  captured at 1.6x device scale so the output is exactly 1920x1080 (16:9)
- feature.gif (animated, used as the post's `image`): frame-by-frame capture
  of feature-anim.html, which exposes a deterministic `seek(t)` function

Usage (requires ffmpeg on PATH):

    uv run --with playwright python capture.py

Outputs are written to the post directory (the parent of this folder).
"""

import pathlib
import subprocess
import tempfile

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
POST_DIR = HERE.parent

WIDTH, HEIGHT = 1200, 675  # 16:9
LOOP_MS = 4600
FPS = 10
N_FRAMES = LOOP_MS * FPS // 1000

def await_fonts(page):
    """Block until the self-hosted site fonts are loaded, and fail loudly if
    they didn't load -- a silent fallback to a system sans would look wrong."""
    page.evaluate("() => document.fonts.ready")
    for spec in ('600 16px "Open Sans"', '500 16px "Source Code Pro"'):
        if not page.evaluate(f"() => document.fonts.check('{spec}')"):
            raise SystemExit(f"font not loaded: {spec}")


with sync_playwright() as p:
    browser = p.chromium.launch()

    # Static card -> feature.png at 1920x1080
    page = browser.new_page(
        viewport={"width": WIDTH, "height": HEIGHT},
        device_scale_factor=1.6,
    )
    page.goto((HERE / "feature.html").as_uri())
    await_fonts(page)
    page.wait_for_timeout(300)
    page.screenshot(path=str(POST_DIR / "feature.png"))
    page.close()
    print("feature.png written (1920x1080)")

    # Animated card -> feature.gif at 1200x675
    page = browser.new_page(viewport={"width": WIDTH, "height": HEIGHT})
    page.goto((HERE / "feature-anim.html").as_uri())
    await_fonts(page)
    page.wait_for_timeout(300)

    with tempfile.TemporaryDirectory() as tmp:
        frames = pathlib.Path(tmp)
        for i in range(N_FRAMES):
            page.evaluate(f"seek({i * 1000 / FPS})")
            page.screenshot(path=str(frames / f"frame_{i:03d}.png"))
            print(f"frame {i + 1}/{N_FRAMES}", end="\r")
        browser.close()

        print("\nassembling gif...")
        subprocess.run(
            [
                "ffmpeg", "-y",
                "-framerate", str(FPS),
                "-i", str(frames / "frame_%03d.png"),
                "-vf", "split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer:bayer_scale=4",
                "-loop", "0",
                str(POST_DIR / "feature.gif"),
            ],
            check=True,
            capture_output=True,
        )

size = (POST_DIR / "feature.gif").stat().st_size
print(f"feature.gif: {size / 1024:.0f} KB")
