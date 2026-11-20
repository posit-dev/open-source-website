"""Regenerate skill-before.png and skill-after.png from the two example apps.

Runs before-app/ and after-app/ with Shiny for R, screenshots each one, and
writes the images to the post directory (the parent of this folder).

Each image gets a 1px border so the mostly-white screenshot reads as one
object on the page background.

Usage (requires R with shiny, bslib and ggplot2):

    uv run --with playwright --with pillow python capture.py
"""

import pathlib
import socket
import subprocess
import time
import urllib.request

from PIL import Image, ImageOps
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
POST_DIR = HERE.parent


def free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def shoot(page, app: str, out: str) -> None:
    port = free_port()
    proc = subprocess.Popen(
        ["Rscript", "-e", f"shiny::runApp('{HERE / app}', port = {port})"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        url = f"http://127.0.0.1:{port}/"
        for _ in range(60):
            try:
                urllib.request.urlopen(url, timeout=1)
                break
            except OSError:
                time.sleep(0.5)
        else:
            raise SystemExit(f"{app} did not start")
        page.goto(url)
        page.wait_for_selector("#plot img")
        page.wait_for_timeout(1000)
        page.screenshot(path=str(POST_DIR / out))
        img = Image.open(POST_DIR / out).convert("RGB")
        ImageOps.expand(img, border=2, fill="#DEE2E6").save(POST_DIR / out)
    finally:
        proc.terminate()
        proc.wait()


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(
        viewport={"width": 1000, "height": 680}, device_scale_factor=2
    )
    shoot(page, "before-app", "skill-before.png")
    shoot(page, "after-app", "skill-after.png")
    browser.close()

print(f"skill-before.png and skill-after.png written to {POST_DIR}")
