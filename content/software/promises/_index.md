---
description: A promise library for R
github: rstudio/promises
image: logo.svg
languages:
- R
latest_release: '2025-11-05T18:06:35+00:00'
people:
- Joe Cheng
- Barret Schloerke
- Winston Chang
- Charlie Gao
- Garrick Aden-Buie
- Carson Sievert
- Christophe Dervieux
title: promises
website: https://rstudio.github.io/promises/

external:
  description: A promise library for R
  first_commit: '2017-04-11T18:52:38+00:00'
  forks: 17
  languages:
  - R
  last_updated: '2026-02-17T11:19:13.600086+00:00'
  latest_release: '2025-11-05T18:06:35+00:00'
  license: NOASSERTION
  people:
  - Joe Cheng
  - Barret Schloerke
  - Winston Chang
  - Charlie Gao
  - Garrick Aden-Buie
  - Carson Sievert
  - Christophe Dervieux
  readme_image: man/figures/logo.svg
  repo: rstudio/promises
  stars: 210
  title: promises
  website: https://rstudio.github.io/promises/
---

The promises package brings asynchronous programming to R through a JavaScript-style promise API. It allows R code to execute non-blocking operations, which is particularly useful for long-running tasks in interactive applications like Shiny.

Promises solve the problem of keeping R applications responsive during time-consuming operations such as database queries, web API calls, or complex computations. Instead of blocking the entire R session while waiting for results, promises let you write code that executes asynchronously and handles results when they become available. This is especially valuable in Shiny applications where blocking operations would freeze the user interface for all users.
