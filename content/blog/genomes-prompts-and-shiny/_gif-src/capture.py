"""Regenerate the animated figures in this post.

Each figure is recorded from the deployed app with Playwright and turned into a
GIF with ffmpeg. Raw recordings go to a temporary folder and are deleted.

- tahoe-explorer.gif: a short tour of the Overview and Coverage tabs, then the
  assistant builds a breast cancer subset and the Subset builder tiles update.
- plotomics-live.gif: the Visium page fades its spots to show the tissue,
  recolours by gene expression and swaps in the ggplot2 image, then the
  protein structure page turns the TP53 model.

tahoe-explorer.gif uses an AI provider and needs GEMINI_API_KEY in the
environment. The key goes into the masked key field before the kept part of
the recording starts, so it never appears in the GIF, and the app is told to
forget it at the end.

Usage (requires ffmpeg on PATH):

    uv run --with playwright python capture.py                   # both
    uv run --with playwright python capture.py plotomics-live    # one of them

First run only:

    uv run --with playwright python -m playwright install chromium

Outputs are written to the post directory (the parent of this folder), or to
the folder given with --out.
"""

import argparse
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import time

from playwright.sync_api import sync_playwright

POST = pathlib.Path(__file__).resolve().parent.parent
TIMEOUT = 240_000  # ms; a Connect Cloud app can take minutes to wake up
VIEWPORT = {"width": 1600, "height": 900}


class Retake(Exception):
    """The take is not usable (for example the assistant changed nothing); record it again."""


class Clip:
    """A recording, the stretch of it to keep, and the parts to speed up or drop.

    Times are seconds since the recording started.
    """

    def __init__(self, page, started):
        self.page = page
        self.started = started
        self.start = None
        self.end = None
        self.changes = []  # (from, to, speed); speed None drops the stretch

    def now(self):
        return time.monotonic() - self.started

    def mark_start(self):
        self.start = self.now()

    def mark_end(self, at=None):
        self.end = self.now() if at is None else at

    def fast_forward(self, start, end, factor=4.0):
        if end - start > 0.5:
            self.changes.append((start, end, factor))

    def cut(self, start, end):
        self.changes.append((start, end, None))


def segments(clip):
    """Split the kept stretch into (from, to, speed) pieces, leaving out cuts."""
    start, end = max(0.0, clip.start - 0.3), clip.end
    pieces, t = [], start
    for a, b, speed in sorted(clip.changes):
        a, b = max(a, t), min(b, end)
        if b <= a:
            continue
        if a > t:
            pieces.append((t, a, 1.0))
        if speed:
            pieces.append((a, b, speed))
        t = b
    if end > t:
        pieces.append((t, end, 1.0))
    return pieces


def to_gif(webm, dest, clip, crop, width, fps):
    """Two ffmpeg passes: build a palette from the clip, then map frames to it."""
    pieces = segments(clip)
    graph = [
        f"[0:v]trim=start={a:.2f}:end={b:.2f},setpts=(PTS-STARTPTS)/{s}[p{i}]"
        for i, (a, b, s) in enumerate(pieces)
    ]
    graph.append(
        "".join(f"[p{i}]" for i in range(len(pieces)))
        + f"concat=n={len(pieces)}:v=1:a=0[cut]"
    )
    look = "[cut]" + (f"crop={crop[2]}:{crop[3]}:{crop[0]}:{crop[1]}," if crop else "")
    look += f"fps={fps},scale={width}:-1:flags=lanczos"
    palette = dest.with_suffix(".palette.png")
    try:
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-loglevel",
                "error",
                "-i",
                str(webm),
                "-filter_complex",
                ";".join([*graph, look + ",palettegen=stats_mode=diff"]),
                str(palette),
            ],
            check=True,
        )
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-loglevel",
                "error",
                "-i",
                str(webm),
                "-i",
                str(palette),
                "-filter_complex",
                ";".join(
                    [
                        *graph,
                        look + "[x]",
                        (
                            "[x][1:v]paletteuse=dither=bayer"
                            ":bayer_scale=5:diff_mode=rectangle"
                        ),
                    ]
                ),
                "-loop",
                "0",
                str(dest),
            ],
            check=True,
        )
    finally:
        palette.unlink(missing_ok=True)


def gif_length(clip):
    return sum((b - a) / s for a, b, s in segments(clip))


def record(pw, name, scene, out, viewport=VIEWPORT, crop=None, width=None, fps=12):
    """Run one scene in a fresh browser and write out/<name>.gif.

    `crop` is (x, y, width, height) in page pixels. The GIF is scaled down to
    `width`, at most 1200 px, and never scaled up.
    """
    raw = pathlib.Path(tempfile.mkdtemp(prefix=f"gif-{name}-"))
    width = width or min(1200, crop[2] if crop else viewport["width"])
    try:
        browser = pw.chromium.launch()
        context = browser.new_context(
            viewport=viewport, record_video_dir=str(raw), record_video_size=viewport
        )
        clip = Clip(context.new_page(), time.monotonic())
        try:
            scene(clip)
        finally:
            context.close()  # flushes the video
            browser.close()
        if clip.start is None or clip.end is None:
            raise RuntimeError(f"{name}: the scene never marked its start and end")
        dest = out / f"{name}.gif"
        to_gif(next(raw.glob("*.webm")), dest, clip, crop, width, fps)
        print(
            f"{dest.name}: {gif_length(clip):.1f}s, {dest.stat().st_size / 1e6:.1f} MB",
            flush=True,
        )
    finally:
        shutil.rmtree(raw, ignore_errors=True)


def gemini_key(name):
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise SystemExit(f"{name} needs GEMINI_API_KEY in the environment")
    return key


def masked(page, selector, name):
    """The key field, but only if it is a single masked input."""
    field = page.locator(f"input[type=password]{selector}")
    if field.count() != 1:
        raise SystemExit(f"{name}: no masked key field, refusing to enter the key")
    return field


def settle(page, timeout=120_000, quiet=4_000):
    """Wait until the page text has stopped changing for `quiet` ms.

    Returns the time.monotonic() of the last change, so a clip can end a fixed
    hold after it instead of after the whole quiet period.
    """
    last, since = page.locator("body").inner_text(), time.monotonic()
    deadline = time.monotonic() + timeout / 1000
    while time.monotonic() < deadline:
        page.wait_for_timeout(500)
        now = page.locator("body").inner_text()
        if now != last:
            last, since = now, time.monotonic()
        elif (time.monotonic() - since) * 1000 >= quiet:
            return since
    raise TimeoutError("the page kept changing")


def wait_for_reply(clip, chat, before, name, timeout=180):
    """Wait until the chat has grown by a sentence or so past `before` characters."""
    deadline = time.monotonic() + timeout
    while len(chat.inner_text()) < before + 40:
        if time.monotonic() > deadline:
            raise TimeoutError(f"{name}: the assistant never replied")
        clip.page.wait_for_timeout(250)


# shinychat marks a user's message with a custom element or, in newer versions, a class.
USER = "shiny-user-message, .shiny-chat-user-message"

QUESTION_JS = r"""(chat, user) => {
  // Scroll the chat so the last question sits at the top, with the reply below it.
  const asked = chat.querySelectorAll(user);
  const target = asked[asked.length - 1];
  if (!target) return false;
  target.scrollIntoView({block: "start", behavior: "smooth"});
  return true;
}"""


def back_to_question(clip, chat, quiet_since):
    """Drop the quiet wait after the reply, then scroll back up to the question."""
    clip.cut(quiet_since - clip.started + 0.6, clip.now())
    chat.evaluate(QUESTION_JS, USER)
    clip.page.wait_for_timeout(3_500)


def ease(page, steps, action, pause=40):
    """Run `action(t)` for t from 0 to 1 with an ease-in-out curve."""
    for i in range(steps + 1):
        x = i / steps
        action(x * x * (3 - 2 * x))
        page.wait_for_timeout(pause)


TILE_JS = r"""label => {
  // A tile is an element whose whole text is two lines: the label, then a value.
  // Only visible ones count: other tabs keep their own tiles in the page, hidden.
  for (const el of document.querySelectorAll("div, section, span")) {
    if (!el.checkVisibility()) continue;
    const lines = (el.innerText || "").split("\n").map(s => s.trim()).filter(Boolean);
    if (lines.length === 2 && lines[0] === label && /^[\d.,]+\s*[KMB]?$/.test(lines[1])) {
      return lines[1];
    }
  }
  return null;
}"""


def tile(page, label):
    """The value shown in one of the Tahoe summary tiles."""
    return page.evaluate(TILE_JS, label)


BAR_JS = r"""([id, category]) => {
  // Page position of a bar in a horizontal echarts bar chart, near its base.
  const el = document.getElementById(id);
  const chart = el && echarts.getInstanceByDom(el);
  if (!chart) return null;
  const y = chart.convertToPixel({yAxisIndex: 0}, category);
  const x = chart.convertToPixel({xAxisIndex: 0}, 0.6);
  const box = el.getBoundingClientRect();
  return {x: box.left + x, y: box.top + y};
}"""


# Gemini model for the Tahoe assistant. The app's default, gemini-2.5-flash, has
# its own daily quota, which ran out while these were recorded.
TAHOE_MODEL = "gemini-flash-latest"


def failed(chat):
    """True when the chat shows the app's error message in place of a reply."""
    return "An error occurred" in chat.inner_text()


def tahoe_explorer(clip):
    key = gemini_key("tahoe-explorer")
    page = clip.page
    page.goto(
        "https://posit-tahoe-explorer.share.connect.posit.cloud/",
        wait_until="domcontentloaded",
        timeout=TIMEOUT,
    )
    page.get_by_text("Subset builder", exact=False).first.wait_for(timeout=TIMEOUT)
    page.wait_for_timeout(2_500)

    # Render each tab once so the tour does not wait on first draws.
    for tab in ("Coverage", "Subset builder", "Overview"):
        page.get_by_role("tab", name=tab).click()
        page.wait_for_timeout(3_000)

    # Connect before the kept part starts, so the key is never on screen in the GIF.
    dock = page.locator("#toggle_assistant")
    dock.click()
    page.wait_for_timeout(1_500)
    page.get_by_text("Model & key", exact=False).first.click()
    field = masked(page, "#chat_dock-api_key", "tahoe-explorer")
    field.fill(key)
    page.wait_for_timeout(2_500)  # the model list loads from the key
    model = page.locator("#chat_dock-model-selectized")
    model.click()
    model.fill(TAHOE_MODEL)
    page.keyboard.press("Enter")
    page.wait_for_timeout(800)
    print(
        f"tahoe-explorer: model {page.locator('#chat_dock-model').input_value()}",
        flush=True,
    )
    page.get_by_role("button", name="Connect").first.click()
    page.get_by_text("Connected:", exact=False).first.wait_for(timeout=60_000)
    page.get_by_text("Model & key", exact=False).first.click()  # collapse the panel
    page.wait_for_timeout(1_000)
    dock.click()  # close the assistant for the tour
    page.wait_for_timeout(1_500)
    if field.is_visible():
        raise SystemExit("tahoe-explorer: key panel still open, refusing to record")

    try:
        clip.mark_start()
        page.wait_for_timeout(2_200)
        bar = page.evaluate(BAR_JS, ["overview-organ_plot", "Breast"])
        if bar is None:
            raise SystemExit("tahoe-explorer: cannot find the organ chart")
        page.mouse.click(bar["x"], bar["y"])  # filters the cell line table
        page.wait_for_timeout(2_600)
        page.get_by_role("tab", name="Coverage").click()
        page.wait_for_timeout(2_800)
        page.get_by_role("tab", name="Subset builder").click()
        page.wait_for_timeout(1_200)
        dock.click()
        page.wait_for_timeout(1_000)

        box = page.get_by_role("textbox", name="Chat message")
        box.click()
        box.type(
            "How can I make a subset for breast cancer, and can you build it "
            "for me in the subset builder?",
            delay=10,
        )
        before = tile(page, "Cell lines")
        if before is None:
            raise SystemExit("tahoe-explorer: cannot find the Cell lines tile")
        chat = page.locator("#chat_dock-chat")
        page.keyboard.press("Enter")
        sent = clip.now()

        # Keep a moment of the model thinking, then skip to its reply.
        page.get_by_text("build it for me", exact=False).first.wait_for(timeout=30_000)
        wait_for_reply(clip, chat, len(chat.inner_text()), "tahoe-explorer")
        replied = clip.now() + 1.5
        clip.cut(sent + 1.5, clip.now() - 0.3)

        # Done means the assistant changed the subset (the new counts can land a
        # few seconds after the reply) and then finished writing.
        settle(page)
        if failed(chat):
            raise SystemExit("tahoe-explorer: the assistant returned an error")
        deadline = time.monotonic() + 45
        while tile(page, "Cell lines") == before:
            if time.monotonic() > deadline:
                raise Retake("the assistant did not change the subset")
            page.wait_for_timeout(500)
        last_change = settle(page)
        clip.fast_forward(
            replied, last_change - clip.started, factor=3.5
        )  # the long recipe
        print(
            f"tahoe-explorer: Cell lines {before} -> {tile(page, 'Cell lines')}, "
            f"Cells {tile(page, 'Cells')}, Samples {tile(page, 'Samples')}",
            flush=True,
        )
        back_to_question(clip, chat, last_change)
        clip.mark_end()
    finally:
        # After the kept part: clear the key from the app session.
        if not page.get_by_text("Model & key", exact=False).first.is_visible():
            dock.click()
        page.get_by_text("Model & key", exact=False).first.click()
        page.get_by_role("button", name="Forget key").first.click()
        page.wait_for_timeout(1_000)


def plotomics_live(clip):
    page = clip.page
    url = "https://posit-plotomics-live.share.connect.posit.cloud/"

    def open_page(title):
        page.goto(url, wait_until="domcontentloaded", timeout=TIMEOUT)
        card = page.locator("a", has_text=title).first
        card.wait_for(timeout=TIMEOUT)
        page.wait_for_timeout(1_500)
        card.scroll_into_view_if_needed()
        card.click()
        page.locator("canvas").first.wait_for(timeout=TIMEOUT)
        page.wait_for_timeout(8_000)

    open_page("Visium spatial transcriptomics")
    slider = page.locator("input[type=range]").first
    colour = page.locator("select").first
    full, low = float(slider.input_value()), float(slider.get_attribute("min"))
    step = float(slider.get_attribute("step"))

    def opacity(value):
        # A range input takes only values on its step grid, written the way the
        # browser writes them back ("0.8", not "0.80").
        slider.fill(f"{round(round(value / step) * step, 4):g}")

    clip.mark_start()
    page.wait_for_timeout(1_500)
    ease(page, 18, lambda t: opacity(full - t * (full - low)))  # spots fade
    page.wait_for_timeout(1_400)
    ease(page, 12, lambda t: opacity(low + t * (full - low)))
    page.wait_for_timeout(600)
    colour.select_option(label="Gene expression")
    page.wait_for_timeout(2_200)
    page.get_by_role("button", name="ggplot2 (classic)").click()
    page.wait_for_timeout(2_400)

    # Drop the page change, then turn the protein.
    leave = clip.now()
    open_page("Protein structure")
    model = page.locator("canvas").first.bounding_box()
    cx, cy = model["x"] + model["width"] / 2, model["y"] + model["height"] / 2
    page.mouse.move(cx, cy)
    for _ in range(10):  # zoom out so most of the chain fits
        page.mouse.wheel(0, -150)
        page.wait_for_timeout(100)
    page.wait_for_timeout(1_500)
    page.mouse.move(cx - 260, cy)
    clip.cut(leave, clip.now() - 0.2)
    page.wait_for_timeout(600)
    page.mouse.down()
    ease(page, 60, lambda t: page.mouse.move(cx - 260 + 520 * t, cy + 40 * t), pause=25)
    page.mouse.up()
    page.wait_for_timeout(1_500)
    clip.mark_end()


# Viewports are tall enough that nothing the scene shows is cut off; crops drop
# empty margins.
SCENES = {
    "tahoe-explorer": {"scene": tahoe_explorer},
    "plotomics-live": {
        "scene": plotomics_live,
        "viewport": {"width": 1600, "height": 1100},
        "crop": (150, 40, 1300, 1040),
        "fps": 15,
    },
}


NEEDS_KEY = {"tahoe-explorer"}


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "names",
        nargs="*",
        metavar="name",
        help=f"any of {', '.join(SCENES)}; all of them when omitted",
    )
    parser.add_argument(
        "--out",
        type=pathlib.Path,
        default=POST,
        help="folder for the GIFs (default: the post folder)",
    )
    args = parser.parse_args()
    unknown = [n for n in args.names if n not in SCENES]
    if unknown:
        parser.error(f"unknown name(s): {', '.join(unknown)}")
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg is not on PATH")
    args.out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        for name in args.names or list(SCENES):
            if name in NEEDS_KEY and not os.environ.get("GEMINI_API_KEY"):
                print(f"skipping {name}: GEMINI_API_KEY is not set", flush=True)
                continue
            for take in range(1, 4):
                try:
                    record(pw, name, out=args.out, **SCENES[name])
                    break
                except Retake as why:
                    print(f"{name}: take {take} not used, {why}", flush=True)


if __name__ == "__main__":
    main()
