---
description: Print Session Information
github: r-lib/sessioninfo
image: session-info2.svg
languages:
- R
latest_release: '2025-02-05T12:57:20+00:00'
people:
- Gábor Csárdi
- Jenny Bryan
- Garrick Aden-Buie
- Jeroen Janssens
- Max Kuhn
- Hadley Wickham
title: sessioninfo
website: https://sessioninfo.r-lib.org

external:  # updated automatically, do not edit
  description: Print Session Information
  first_commit: '2017-04-21T10:27:47+00:00'
  forks: 31
  languages:
  - R
  last_updated: '2026-02-24T09:26:35.174684+00:00'
  latest_release: '2025-02-05T12:57:20+00:00'
  license: GPL-2.0
  people:
  - Gábor Csárdi
  - Jenny Bryan
  - Garrick Aden-Buie
  - Jeroen Janssens
  - Max Kuhn
  - Hadley Wickham
  readme_image: https://raw.githubusercontent.com/r-lib/sessioninfo/main/man/figures/session-info2.svg
  repo: r-lib/sessioninfo
  stars: 80
  title: sessioninfo
  website: https://sessioninfo.r-lib.org
---

The sessioninfo package provides detailed information about your current R session, similar to `utils::sessionInfo()` but with enhanced output. It's designed for debugging, creating reproducible examples, and documenting your R environment when reporting issues or sharing code.

The package highlights potential installation problems like mismatched package versions or corrupted DLLs, shows package sources including GitHub commits, and displays information about external software dependencies. It can also report Python configuration when using reticulate, compare session info between environments with `session_diff()`, and selectively show loaded, attached, or installed packages with their recursive dependencies.
