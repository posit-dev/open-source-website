"""Run each example app and save a screenshot of it next to the post.

- download-icon/app.py -> download-icon.png

sidebar-role/app.py has nothing to see (the role is in the markup only), so
it is not captured.

Also checks background-updates/app.py: its text input must change on its own,
with no user input, within a few seconds.

Usage (from this folder, with Shiny for Python >= 1.9):

    uv run --with "shiny>=1.9" --with pandas --with faicons --with playwright \
        python screenshot.py

Run `playwright install chromium` once first if Playwright has no browser.
"""

import pathlib
import socket
import subprocess
import sys
import time
import urllib.request

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
POST_DIR = HERE.parent


def free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def serve(app):
    port = free_port()
    proc = subprocess.Popen(
        [sys.executable, "-m", "shiny", "run", "--port", str(port), str(HERE / app)]
    )
    url = f"http://127.0.0.1:{port}"
    for _ in range(150):  # up to 30 seconds, for a cold start
        try:
            urllib.request.urlopen(url)
            return proc, url
        except OSError:
            time.sleep(0.2)
    proc.kill()
    raise SystemExit(f"{app} did not start")


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(
        viewport={"width": 640, "height": 300}, device_scale_factor=2
    )

    for app, png in [("download-icon/app.py", "download-icon.png")]:
        proc, url = serve(app)
        try:
            page.goto(url)
            page.wait_for_selector(".shiny-bound-output")
            page.wait_for_timeout(1000)
            page.screenshot(path=str(POST_DIR / png))
            print(f"{png} written")
        finally:
            proc.kill()

    proc, url = serve("background-updates/app.py")
    try:
        page.goto(url)
        status = page.locator("#status")
        first = status.input_value()
        page.wait_for_timeout(2500)
        assert status.input_value() != first, "background update was not sent"
        print("background-updates: input changed on its own")
    finally:
        proc.kill()

    browser.close()
