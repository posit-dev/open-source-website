# Screenshot and video generation for the shinychat post

Every image and video in `../images/` is generated programmatically — no manual
screen recording. Each subdirectory here is one demo:

- `app.R` — a Shiny app using `bslib::page_chat()` + shinychat, backed by a
  mocked ellmer client (`_mock-client.R`: keyword-matched canned replies,
  streamed via a `coro::async_generator`; `mock_stream_reply()` streams tool
  requests in as running activity rows before their results land and text
  word by word). No network or LLM calls.
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
  `press_enter()` (Enter key alone, e.g. after `type_natural()`),
  `click_selector()`, plus `js()` for arbitrary expressions.
- Stills: `viewport_png()`, `full_page_png()`, `element_png()`,
  `union_png()` (screenshot of the bounding box of several selectors, with
  padding — used for the tight cropped figures in the post).
- Movies: `movie_start(b, fps)` returns a recorder; `rec$snap()` captures a
  JPEG frame with a timestamp, `rec$loop(seconds)` snapshots at the target
  fps for that long, and `rec$loop_until(expr)` snapshots while polling for a
  JS condition (so streaming responses stay animated). Actions performed
  between `loop()` calls are captured as single frames, so anything not
  wrapped in `loop()` appears instant.
  `movie_save(rec, path, fps = 15, width = NULL)` writes frames to a temp
  dir, builds an ffmpeg concat list with real inter-frame durations, and runs
  roughly `ffmpeg -f concat -i list.txt -vf "fps=15,scale=2400:-2,..."`.
  Set `rec$clip <- movie_clip_fit(b, selectors)` to record only part of the
  app (e.g. just the conversation, no header or input); the clip is fit to
  exactly 4:3 so it fills the `aspect-ratio="4x3"` embed, and `movie_save()`
  should then be called with `width = rec$clip$width * 2` to keep the output
  at native retina resolution.
- Fake cursor: CDP clicks are invisible in captured frames, so
  `cursor_start(b)` injects a pointer element that `cursor_glideto()` /
  `cursor_glideto_el()` animate in step with the movie frames, dispatching
  real CDP mouse events along the way (these also trigger `:hover`, which is
  what reveals the message edit buttons). `rect_of_text()` finds the bounding
  box of the first element matching a selector *and* containing text, for
  gliding to a specific history entry. `cursor_click_here()` clicks with a
  brief press animation, `cursor_leave()` retreats off the right edge.
  Coordinates are client space; because root CSS zoom scales the rendered
  position of fixed elements, `cursor_place()` divides by the zoom factor.
- Natural input: `type_natural()` types one character at a time with
  human-ish delays, `select_edit_text()` selects an exact substring inside a
  contenteditable editor, and `press_backspace()` deletes the selection.

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
