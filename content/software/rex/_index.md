---
color: '#9A4665'
description: Friendly regular expressions for R.
github: r-lib/rex
image: logo.svg
languages:
- R
latest_release: '2021-11-24T20:50:29+00:00'
people:
- Hadley Wickham
title: rex
website: https://rex.r-lib.org

external:  # updated automatically, do not edit
  description: Friendly regular expressions for R.
  first_commit: '2014-09-23T01:13:17+00:00'
  forks: 28
  languages:
  - R
  last_updated: '2026-03-05T16:25:20.591985+00:00'
  latest_release: '2021-11-24T20:50:29+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  repo: r-lib/rex
  stars: 335
  title: rex
  website: https://rex.r-lib.org
---

Rex is an R package that provides a human-readable syntax for building regular expressions. It transforms complex regex patterns into composable, self-documenting code using plain English function names.

The package makes regular expressions easier to write, read, and maintain by replacing cryptic symbols with functions like `maybe()`, `capture()`, and `one_or_more()`. It uses PCRE (Perl Compatible Regular Expressions) as its underlying engine while providing a friendlier interface. Rex is particularly useful for complex patterns like URL parsing or log file analysis where traditional regex syntax becomes difficult to understand and debug.
