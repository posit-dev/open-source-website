---
image: logo.svg
color: "#419599"
description: Pretty, human readable formatting of quantities
github: r-lib/prettyunits
languages:
- JavaScript
latest_release: '2023-09-24T10:52:33+00:00'
people:
- Gábor Csárdi
- Jeroen Janssens
title: prettyunits
website: http://r-lib.github.io/prettyunits/

external:  # updated automatically, do not edit
  description: Pretty, human readable formatting of quantities
  first_commit: '2014-10-03T19:59:19+00:00'
  forks: 16
  languages:
  - JavaScript
  last_updated: '2026-03-05T16:25:26.864915+00:00'
  latest_release: '2023-09-24T10:52:33+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Janssens
  repo: r-lib/prettyunits
  stars: 134
  title: prettyunits
  website: http://r-lib.github.io/prettyunits/
---

The prettyunits package converts numeric quantities into human-readable text formats. It handles time intervals, bytes, numbers, p-values, and colors, making raw numeric data easier to understand in R outputs.

The package solves the problem of displaying large or small numbers in a more intuitive way for users and reports. It supports multiple formatting options including compact and vague formats for time intervals, automatic unit scaling for bytes and quantities, and preservation of trailing zeros for rounding operations. Each formatter is designed for its specific use case, such as `pretty_bytes()` for file sizes, `pretty_ms()` for durations, and `time_ago()` for relative timestamps.
