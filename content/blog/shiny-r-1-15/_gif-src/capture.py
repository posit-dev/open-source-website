"""Regenerate autoreload.gif: a real recording of Shiny's autoreload.

Runs a copy of autoreload-app/ with `options(shiny.autoreload = TRUE)`, shows
its source next to the live app (stage.html), then edits and saves the file
twice. Each save is a real write to disk, and the browser pane is the real app
reloading. Only the editor pane is drawn by the stage.

Usage (requires R with shiny, bslib and watcher):

    uv run --with playwright --with pillow python capture.py
"""

import io
import json
import pathlib
import shutil
import socket
import subprocess
import tempfile
import time
import urllib.request

from PIL import Image
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
POST_DIR = HERE.parent
SOURCE = (HERE / "autoreload-app" / "app.R").read_text()

# (text to find, replacement, text the reloaded app must show or None)
EDITS = [
    ('col = "steelblue"', 'col = "tomato"', None),
    ('h2("Old Faithful")', 'h2("Old Faithful: time between eruptions")', "time between eruptions"),
]

frames: list[tuple[Image.Image, int]] = []


def snap(page, ms: int) -> None:
    img = Image.open(io.BytesIO(page.screenshot())).convert("RGB")
    frames.append((img, ms))


def show(page, text: str, changed: list[int], state: str) -> None:
    page.evaluate(
        f"showCode({json.dumps(text)}, {json.dumps(changed)}, {json.dumps(state)})"
    )


def plot_src(app) -> str:
    app.locator("#plot img").wait_for()
    return app.locator("#plot img").get_attribute("src")


with socket.socket() as s:
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]

app_dir = pathlib.Path(tempfile.mkdtemp()) / "app"
shutil.copytree(HERE / "autoreload-app", app_dir)
proc = subprocess.Popen(
    [
        "Rscript",
        "-e",
        f"options(shiny.autoreload = TRUE); shiny::runApp('{app_dir}', port = {port})",
    ],
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
        page = browser.new_page(viewport={"width": 1100, "height": 480})
        page.goto((HERE / "stage.html").as_uri())
        page.evaluate("() => document.fonts.ready")
        page.evaluate(f"document.getElementById('app').src = {json.dumps(url)}")
        app = page.frame_locator("#app")
        text = SOURCE
        show(page, text, [], "saved")
        before = plot_src(app)
        page.wait_for_timeout(500)
        snap(page, 1800)

        for old, new, expect in EDITS:
            line = next(i for i, l in enumerate(text.split("\n")) if old in l)
            text = text.replace(old, new)
            show(page, text, [line], "unsaved")
            snap(page, 1200)

            (app_dir / "app.R").write_text(text)  # the real save
            show(page, text, [line], "saved")
            snap(page, 500)
            # Wait for the real reload: the page text or the plot image changes.
            deadline = time.time() + 20
            while time.time() < deadline:
                page.wait_for_timeout(150)
                try:
                    if expect:
                        done = app.get_by_text(expect).count() > 0
                    else:
                        done = plot_src(app) != before
                    if done:
                        break
                except Exception:
                    pass  # the iframe is mid-reload
            else:
                raise SystemExit(f"app did not reload after editing: {old}")
            before = plot_src(app)
            page.wait_for_timeout(600)
            snap(page, 2200)
        browser.close()
finally:
    proc.terminate()
    proc.wait()
    shutil.rmtree(app_dir.parent)

# One shared palette keeps the GIF small and stops colours shifting per frame.
both = Image.new("RGB", (frames[0][0].width, frames[0][0].height * 2))
both.paste(frames[0][0], (0, 0))
both.paste(frames[-1][0], (0, frames[0][0].height))
palette = both.quantize(colors=128, dither=Image.Dither.NONE)
images = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f, _ in frames]
images[0].save(
    POST_DIR / "autoreload.gif",
    save_all=True,
    append_images=images[1:],
    duration=[ms for _, ms in frames],
    loop=0,
    optimize=True,
)
print(f"autoreload.gif written ({len(frames)} frames)")
