---
color: '#657B83'
description: Call R from R
github: r-lib/callr
image: simple.svg
languages:
- R
latest_release: '2024-03-25T12:09:25+00:00'
people:
- Gábor Csárdi
- Daniel Falbel
- Jenny Bryan
- Lionel Henry
- Hadley Wickham
- Winston Chang
- Jeroen Ooms
- Jeroen Janssens
title: callr
website: https://callr.r-lib.org/

external:  # updated automatically, do not edit
  description: Call R from R
  first_commit: '2016-05-13T10:26:09+00:00'
  forks: 40
  languages:
  - R
  last_updated: '2026-03-05T16:26:16.454033+00:00'
  latest_release: '2024-03-25T12:09:25+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Daniel Falbel
  - Jenny Bryan
  - Lionel Henry
  - Hadley Wickham
  - Winston Chang
  - Jeroen Ooms
  - Jeroen Janssens
  readme_image: man/figures/simple.svg
  repo: r-lib/callr
  stars: 303
  title: callr
  website: https://callr.r-lib.org/
---

callr is an R package that executes R functions in separate R processes, isolating computations from the current R session. It enables both synchronous and asynchronous process execution without affecting the parent process.

The package handles argument passing and return value copying between processes seamlessly, including error objects with full stack traces. It supports one-off function calls, persistent R sessions for repeated computations, and background processes that can be managed concurrently using polling. callr also provides interfaces for running R CMD commands and R scripts, with options to capture or redirect standard output and error streams.
