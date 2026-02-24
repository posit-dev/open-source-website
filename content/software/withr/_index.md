---
description: Methods For Temporarily Modifying Global State
github: r-lib/withr
image: logo.png
languages:
- R
latest_release: '2024-10-28T10:59:02+00:00'
people:
- Lionel Henry
- Hadley Wickham
- Jenny Bryan
- Gábor Csárdi
- Jeroen Janssens
- Davis Vaughan
title: withr
website: http://withr.r-lib.org

external:  # updated automatically, do not edit
  description: Methods For Temporarily Modifying Global State
  first_commit: '2015-04-21T19:18:28+00:00'
  forks: 44
  languages:
  - R
  last_updated: '2026-02-24T09:26:34.421695+00:00'
  latest_release: '2024-10-28T10:59:02+00:00'
  license: NOASSERTION
  people:
  - Lionel Henry
  - Hadley Wickham
  - Jenny Bryan
  - Gábor Csárdi
  - Jeroen Janssens
  - Davis Vaughan
  readme_image: man/figures/logo.png
  repo: r-lib/withr
  stars: 177
  title: withr
  website: http://withr.r-lib.org
---

The withr package provides functions to run R code with temporarily modified global state that automatically resets after execution. It helps you safely manage side effects like environment variables, working directories, options, graphics parameters, and file connections without leaving permanent changes.

withr offers two function patterns: `with_*()` functions that reset state immediately after code execution, and `local_*()` functions that reset when they go out of scope (typically at function end). This makes it safer to work with API keys, random seeds, locale settings, and other global state modifications, preventing errors caused by forgetting to manually restore original settings. The package originated from devtools and provides these utilities with minimal dependencies.
