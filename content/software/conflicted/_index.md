---
image: logo.svg
color: "#72994E"
description: An alternative conflict resolution strategy for R
github: r-lib/conflicted
languages:
- R
latest_release: '2023-01-31T19:50:16+00:00'
people:
- Hadley Wickham
- Lionel Henry
title: conflicted
website: https://conflicted.r-lib.org/

external:  # updated automatically, do not edit
  description: An alternative conflict resolution strategy for R
  first_commit: '2018-05-20T23:37:42+00:00'
  forks: 14
  languages:
  - R
  last_updated: '2026-03-05T16:28:01.929940+00:00'
  latest_release: '2023-01-31T19:50:16+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  repo: r-lib/conflicted
  stars: 254
  title: conflicted
  website: https://conflicted.r-lib.org/
---

The conflicted package provides an alternative conflict resolution strategy for R. When multiple packages export functions with the same name, R's default behavior uses the most recently loaded package, which can hide conflicts. conflicted changes this by making every conflict an error, forcing you to explicitly choose which function to use.

This approach helps prevent bugs caused by accidentally using the wrong function, particularly when package updates introduce new conflicts. You can resolve conflicts either by using explicit namespacing (like `dplyr::filter()`) or by declaring session-wide preferences with `conflicts_prefer()`. The package also provides tools to identify all conflicts in your current session through `conflict_scout()`.
