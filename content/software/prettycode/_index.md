---
color: '#D44000'
description: Syntax highlight R code in the terminal
github: r-lib/prettycode
image: logo.svg
languages:
- R
latest_release: '2019-12-16T13:00:40+00:00'
people:
- Gábor Csárdi
- Jeroen Janssens
title: prettycode
website: https://r-lib.github.io/prettycode/

external:  # updated automatically, do not edit
  description: Syntax highlight R code in the terminal
  first_commit: '2016-11-15T13:30:58+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-03-05T16:26:47.185828+00:00'
  latest_release: '2019-12-16T13:00:40+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Janssens
  repo: r-lib/prettycode
  stars: 107
  title: prettycode
  website: https://r-lib.github.io/prettycode/
---

The prettycode package adds syntax highlighting to R functions when they are printed in the terminal. It replaces R's standard print method with one that uses ANSI colors to make code more readable.

The package automatically handles long functions by paging them, and it only applies colors when the terminal supports them. It provides a simple way to make R code output more visually clear without requiring manual formatting. The main benefit is improved readability when inspecting function definitions interactively.
