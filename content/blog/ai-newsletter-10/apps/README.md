# Screenshot and video generation for AI Newsletter 10

This directory contains deterministic Shiny apps and Chromote automation scripts
for generating the newsletter's shinychat visuals. The harness and demos were
adapted from the programmatic media workflow committed with the shinychat R 0.5.0
/ Python 0.7.1 release post.

No live LLM calls or API credentials are required. The demos use the mock ellmer
client in `_mock-client.R`.

## Structure

- `_common.R` starts apps, drives headless Chrome with Chromote, captures PNGs,
  records timed frames, and assembles MP4 videos with ffmpeg.
- `_mock-client.R` provides deterministic streamed responses, tool calls,
  citations, and conversation history for the Shinychat demo.
- `shinychat-traffic/` generates the newsletter's three site-traffic assistant
  screenshots.
- `run-all.R` runs every demo in a separate R process.

Generated files are written to the post's sibling `images/` directory.

## Requirements

The R packages are chromote, callr, jsonlite, httpuv, shiny, bslib, shinychat,
ellmer, coro, promises, and bsicons. Chrome or Chromium must be launchable by
Chromote. ffmpeg must be on `PATH` to generate MP4 files; it is not required for
PNG-only demos.

## Generate media

From the post directory, run all demos with:

```bash
Rscript apps/run-all.R
```

To run one demo, make its directory the working directory first:

```bash
cd apps/shinychat-traffic
Rscript screenshot.R
```

The scripts overwrite media files with the same output names. After changing a
demo, regenerate its media and inspect the result before committing it.

## Newsletter media plan

The intended shortlist is:

- `shinychat-page-chat.png` for the complete `page_chat()` layout.
- `shinychat-history.png` for conversation history.
- `shinychat-tools-citations.png` for grouped tool calls and citations.

Prefer MP4 over GIF for newly recorded browser interactions: MP4 is smaller and
sharper, and the site's video shortcode supports looping local videos.
