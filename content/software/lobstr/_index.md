---
description: Understanding complex R objects with tools similar to str()
github: r-lib/lobstr
image: logo.png
color: "#52336A"
languages:
- C
latest_release: '2026-02-19T16:31:47+00:00'
people:
- Hadley Wickham
- Lionel Henry
- Nick Strayer
- Jeroen Janssens
title: lobstr
website: https://lobstr.r-lib.org/

external:  # updated automatically, do not edit
  description: Understanding complex R objects with tools similar to str()
  first_commit: '2015-03-20T20:57:44+00:00'
  forks: 30
  languages:
  - C
  last_updated: '2026-03-05T16:25:37.723767+00:00'
  latest_release: '2026-02-19T16:31:47+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  - Nick Strayer
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/lobstr
  stars: 312
  title: lobstr
  website: https://lobstr.r-lib.org/
---

lobstr provides tools for inspecting the internal structure of R objects, going beyond what `str()` offers. It helps developers understand how R represents and stores data at a low level.

The package includes three main capabilities: visualizing abstract syntax trees of R expressions with `ast()`, examining object references and memory sharing with `ref()` and `obj_size()`, and displaying call stack relationships with `cst()`. These tools are particularly useful for understanding R's memory management, debugging complex data structures, and learning how R evaluates code. The package reveals internal details that are typically hidden from users.
