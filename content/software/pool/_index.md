---
color: '#9A4665'
description: Object Pooling in R
github: rstudio/pool
image: logo.svg
languages:
- R
latest_release: '2024-10-07T14:57:52+00:00'
people:
- Hadley Wickham
- Joe Cheng
- Winston Chang
- Barret Schloerke
title: pool
website: http://rstudio.github.io/pool/

external:  # updated automatically, do not edit
  description: Object Pooling in R
  first_commit: '2016-05-18T17:33:18+00:00'
  forks: 32
  languages:
  - R
  last_updated: '2026-03-05T16:10:51.093225+00:00'
  latest_release: '2024-10-07T14:57:52+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Joe Cheng
  - Winston Chang
  - Barret Schloerke
  repo: rstudio/pool
  stars: 255
  title: pool
  website: http://rstudio.github.io/pool/
---

The pool package manages database connections automatically, eliminating the need to manually create and close connections in R applications. This is particularly useful in interactive contexts like Shiny apps where connection management can be complex.

Pool creates a reusable pool of database connections that automatically grows, shrinks, or maintains itself based on demand. It integrates seamlessly with DBI and dplyr, requiring minimal code changes—typically just replacing `DBI::dbConnect()` with `dbPool()` and adding `poolClose()` at the end. This solves the problem of connection lifecycle management in multi-user or long-running applications where creating new connections for each query would be inefficient or error-prone.
