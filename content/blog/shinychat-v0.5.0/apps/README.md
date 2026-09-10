# Screenshot and video generation for the shinychat post

Every image and video in `../images/` is generated programmatically — no manual
screen recording. Each subdirectory here is one demo:

- `app.R` — a Shiny app using `bslib::page_chat()` + shinychat, backed by a
  mocked ellmer client (`_mock-client.R`: keyword-matched canned replies,
  streamed via a `coro::async_generator`). No network or LLM calls.
- `screenshot.R` — a chromote (Chrome DevTools Protocol) automation script that
  drives the app in headless Chrome and writes PNGs/MP4s into `../images/`.

Run one demo or everything:

```bash
Rscript apps/edit-branches/screenshot.R
Rscript apps/run-all.R
```

Requires R packages `chromote`, `callr`, `jsonlite`, `httpuv`, `shiny`,
`bslib`, `shinychat`, `ellmer`, `coro`, plus `ffmpeg` on PATH and a
launchable headless Chrome for chromote.

## `_common.R` harness

Shared helpers sourced by every `screenshot.R`:

- App lifecycle: `start_app()` (runs `shiny::runApp()` in a `callr` background
  process on a random free port, waits for readiness), `stop_app()`.
- Browser session: `connect()` (opens the app with a viewport and forces
  `prefers-color-scheme: light`), `set_viewport()`, `set_zoom()`.
  `set_zoom()` uses CSS zoom so the desktop layout survives at smaller
  viewport widths; because vh units scale with zoom, it also shrinks the
  `shiny-chat-page` root to keep the app exactly filling the window.
- Waiting: `wait_for()` / `wait_for_text()` / `wait_for_gone()` /
  `wait_for_app_ready()`.
- Interaction: `chat_type()` (CDP `Input$insertText` + optional Enter key),
  `click_selector()`, plus `js()` for arbitrary expressions.
- Stills: `viewport_png()`, `full_page_png()`, `element_png()`,
  `union_png()` (screenshot of the bounding box of several selectors, with
  padding — used for the tight cropped figures in the post).
- Movies: `movie_start(b, fps)` returns a recorder; `rec$snap()` captures a
  JPEG frame with a timestamp, `rec$loop(seconds)` snapshots at the target
  fps for that long. Actions performed between `loop()` calls are captured as
  single frames, so anything not wrapped in `loop()` appears instant.
  `movie_save(rec, path, fps = 15, width = NULL)` writes frames to a temp
  dir, builds an ffmpeg concat list with real inter-frame durations, and runs
  roughly `ffmpeg -f concat -i list.txt -vf "fps=15,scale=2400:-2,..."`.

## Notes for editing recordings

- Videos are embedded with `aspect-ratio="4x3"`, so the recorded viewport must
  be exactly 4:3 (e.g. 1200x900); see the comment in
  `edit-branches/screenshot.R`.
- `movie_save(width = 2400)` scales output to 2400px wide for retina
  sharpness; `-movflags +faststart` for web embedding.
- Timing tweaks (lead-in, how long a streaming response plays) are just
  `rec$loop()` durations around the actions.
- Frame captures run at ~12 fps while actions happen, so fast UI transitions
  may only get one frame; wrap anything that must look animated in `loop()`.
