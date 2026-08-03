"""Regenerate offcanvas-trigger.png from the real example app.

Runs the post's offcanvas trigger example (offcanvas-app/app.py) with
Shiny for Python, clicks the trigger button, screenshots the open panel,
and adds a 1px border so the mostly-white screenshot reads as one object
on the page background.

Usage (requires ffmpeg on PATH):

    uv run --with playwright --with "shiny>=1.7" python capture.py

The output is written to the post directory (the parent of this folder).
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
APP = HERE / "offcanvas-app" / "app.py"

with socket.socket() as s:
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]

app_proc = subprocess.Popen(
    [sys.executable, "-m", "shiny", "run", "--port", str(port), str(APP)],
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
        raise SystemExit("app did not start")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 880, "height": 400})
        page.goto(url)
        page.get_by_role("button", name="Open settings").click()
        # let the offcanvas slide-in animation finish
        page.wait_for_timeout(1000)
        page.screenshot(path=str(HERE / "raw.png"), scale="device")
        browser.close()
finally:
    app_proc.terminate()
    app_proc.wait()

subprocess.run(
    [
        "ffmpeg", "-y",
        "-i", str(HERE / "raw.png"),
        "-vf", "pad=iw+2:ih+2:1:1:color=#DEE2E6",
        str(POST_DIR / "offcanvas-trigger.png"),
    ],
    check=True,
    capture_output=True,
)
(HERE / "raw.png").unlink()
print(f"offcanvas-trigger.png written to {POST_DIR}")
