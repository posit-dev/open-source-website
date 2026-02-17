---
description: 🖍️ R package for colored terminal output — now superseded by cli
github: r-lib/crayon
image: 102484487-41cd2900-405e-11eb-87d4-65793ad9db6a.png
languages:
- R
latest_release: '2024-06-20T11:48:46+00:00'
people:
- Gábor Csárdi
- Jeroen Janssens
- Davis Vaughan
title: crayon
website: http://r-lib.github.io/crayon/

external:
  description: 🖍️ R package for colored terminal output — now superseded by cli
  first_commit: '2014-09-22T20:07:22+00:00'
  forks: 38
  languages:
  - R
  last_updated: '2026-02-17T11:32:24.738559+00:00'
  latest_release: '2024-06-20T11:48:46+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Janssens
  - Davis Vaughan
  readme_image: https://user-images.githubusercontent.com/660288/102484487-41cd2900-405e-11eb-87d4-65793ad9db6a.png
  repo: r-lib/crayon
  stars: 323
  title: crayon
  website: http://r-lib.github.io/crayon/
---

Crayon is an R package for adding color and text styling to terminal output. It provides functions to apply ANSI formatting like colors, bold, underline, and background colors to console text.

The package automatically detects ANSI color support and makes it easy to combine multiple styles using operators like `$` and `%+%`. It supports standard ANSI colors plus 256-color palettes on modern terminals, with automatic fallback for simpler terminals. Note that crayon is now superseded by the cli package, though it continues to receive bug fixes.
