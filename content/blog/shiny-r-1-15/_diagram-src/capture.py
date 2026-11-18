"""Regenerate close-vs-destroy.png from close-vs-destroy.html.

Writes the image to the post directory (the parent of this folder).

Usage:

    uv run --with playwright python capture.py
"""

import pathlib

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
POST_DIR = HERE.parent

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(
        viewport={"width": 1000, "height": 446}, device_scale_factor=2
    )
    page.goto((HERE / "close-vs-destroy.html").as_uri())
    # Fail loudly if the site fonts did not load; a system fallback looks wrong.
    page.evaluate("() => document.fonts.ready")
    for spec in ('600 16px "Open Sans"', '600 16px "Source Code Pro"'):
        if not page.evaluate(f"() => document.fonts.check('{spec}')"):
            raise SystemExit(f"font not loaded: {spec}")
    page.wait_for_timeout(300)
    page.screenshot(path=str(POST_DIR / "close-vs-destroy.png"))
    browser.close()

print("close-vs-destroy.png written")
