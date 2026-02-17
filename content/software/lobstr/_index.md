---
description: Understanding complex R objects with tools similar to str()
github: r-lib/lobstr
image: logo.png
languages:
- C
latest_release: '2025-11-14T13:22:25+00:00'
people:
- Hadley Wickham
- Nick Strayer
- Lionel Henry
- Jeroen Janssens
title: lobstr
website: https://lobstr.r-lib.org/

external:
  description: Understanding complex R objects with tools similar to str()
  first_commit: '2015-03-20T20:57:44+00:00'
  forks: 30
  languages:
  - C
  last_updated: '2026-02-17T11:32:43.344574+00:00'
  latest_release: '2025-11-14T13:22:25+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Nick Strayer
  - Lionel Henry
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/lobstr
  stars: 312
  title: lobstr
  website: https://lobstr.r-lib.org/
---

lobstr provides tools for inspecting the internal structure of R objects, going beyond what `str()` offers. It helps developers understand how R represents and stores data at a low level.

The package includes three main capabilities: visualizing abstract syntax trees of R expressions with `ast()`, examining object references and memory sharing with `ref()` and `obj_size()`, and displaying call stack relationships with `cst()`. These tools are particularly useful for understanding R's memory management, debugging complex data structures, and learning how R evaluates code. The package reveals internal details that are typically hidden from users.
