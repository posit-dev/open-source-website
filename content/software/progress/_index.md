---
description: Progress bar in your R terminal
github: r-lib/progress
image: logo.png
languages:
- R
latest_release: '2023-12-05T09:32:50+00:00'
people:
- Gábor Csárdi
title: progress
website: http://r-lib.github.io/progress/

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: Progress bar in your R terminal
  first_commit: '2014-10-03T20:14:56+00:00'
  forks: 40
  languages:
  - R
  last_updated: '2026-03-20T10:27:51.813764+00:00'
  latest_release: '2023-12-05T09:32:50+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/progress
  stars: 474
  title: progress
  website: http://r-lib.github.io/progress/
---

The progress package provides ASCII progress bars for R terminal sessions. It uses an R6 class interface to create and update progress bars during long-running computations or downloads.

The package offers customizable display formats including elapsed time, estimated time to completion, download rates, and custom tokens. It works with both traditional for loops and functional programming approaches using purrr. The package includes a C++ API for use in compiled code and provides plyr integration for progress tracking in data manipulation pipelines.
