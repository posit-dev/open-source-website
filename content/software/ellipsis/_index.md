---
color: '#EE6331'
description: Tools for Working with ...
github: r-lib/ellipsis
image: logo.svg
languages:
- R
latest_release: '2021-04-29T12:05:34+00:00'
people:
- Hadley Wickham
- Lionel Henry
title: ellipsis
website: https://ellipsis.r-lib.org

external:  # updated automatically, do not edit
  description: Tools for Working with ...
  first_commit: '2018-07-06T20:49:16+00:00'
  forks: 14
  languages:
  - R
  last_updated: '2026-03-05T16:28:10.451041+00:00'
  latest_release: '2021-04-29T12:05:34+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  repo: r-lib/ellipsis
  stars: 140
  title: ellipsis
  website: https://ellipsis.r-lib.org
---

The ellipsis package provides tools to make R's `...` (dot-dot-dot) argument safer by catching common errors like misspelled or unused arguments. Without these checks, functions that accept `...` silently ignore incorrect arguments, which can lead to bugs that are hard to detect.

The package offers three main checking functions: `check_dots_used()` ensures all arguments passed to `...` are actually evaluated by the function, `check_dots_unnamed()` validates that no named arguments appear where only unnamed ones are expected, and `check_dots_empty()` enforces that no extra arguments are provided at all. These checks help catch typos and misused arguments that would otherwise be silently ignored, making function interfaces more robust and user errors more visible.
