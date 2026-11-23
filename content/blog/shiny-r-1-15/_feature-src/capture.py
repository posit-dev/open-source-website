"""Regenerate the post's feature image from feature.html.

Writes feature.png (1920x1080) to the post directory (the parent of this
folder).

Usage:

    uv run --with playwright python capture.py
"""

import pathlib

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
POST_DIR = HERE.parent
SRC = (HERE / "feature.html").as_uri()

WIDTH, HEIGHT = 1200, 675  # 16:9; 1.6x device scale gives 1920x1080

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(
        viewport={"width": WIDTH, "height": HEIGHT},
        device_scale_factor=1.6,
    )
    page.goto(SRC)
    # Fail loudly if the site fonts did not load; a system fallback looks wrong.
    page.evaluate("() => document.fonts.ready")
    for spec in ('600 16px "Open Sans"', '500 16px "Source Code Pro"'):
        if not page.evaluate(f"() => document.fonts.check('{spec}')"):
            raise SystemExit(f"font not loaded: {spec}")
    page.wait_for_timeout(300)
    page.screenshot(path=str(POST_DIR / "feature.png"))
    browser.close()

print("feature.png written (1920x1080)")
