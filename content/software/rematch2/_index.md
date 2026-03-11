---
color: '#9A4665'
description: Tidy output from regular expression matches
github: r-lib/rematch2
image: logo.svg
languages:
- R
latest_release: '2020-04-30T10:30:07+00:00'
people:
- Gábor Csárdi
- Jenny Bryan
title: rematch2
website: ''

external:  # updated automatically, do not edit
  description: Tidy output from regular expression matches
  first_commit: '2017-06-20T15:18:28+00:00'
  forks: 6
  languages:
  - R
  last_updated: '2026-03-05T16:27:27.802068+00:00'
  latest_release: '2020-04-30T10:30:07+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jenny Bryan
  repo: r-lib/rematch2
  stars: 46
  title: rematch2
  website: ''
---

rematch2 is a wrapper around R's base regular expression functions (regexpr and gregexpr) that returns matching results as tidy data frames instead of the base functions' more complex output structures. It simplifies the process of extracting both complete matches and capture groups from pattern matching operations.

The package supports both named and unnamed capture groups, making it easy to extract structured data from text. It provides four main functions: re_match() and re_match_all() for extracting matches and capture groups, and re_exec() and re_exec_all() for cases where you also need the positions (start and end indices) of matches. All results are returned as tibbles, which integrate well with tidyverse workflows and are easier to work with than the nested lists returned by base R regex functions.
