---
description: A simple class for storing time-of-day values
github: tidyverse/hms
image: logo.png
languages:
- R
latest_release: '2025-10-16T19:10:13+00:00'
people:
- Hadley Wickham
- Lionel Henry
- Jeroen Ooms
title: hms
website: https://hms.tidyverse.org/

external:
  description: A simple class for storing time-of-day values
  first_commit: '2016-03-31T09:05:58+00:00'
  forks: 29
  languages:
  - R
  last_updated: '2026-02-17T11:28:14.051473+00:00'
  latest_release: '2025-10-16T19:10:13+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  - Jeroen Ooms
  readme_image: man/figures/logo.png
  repo: tidyverse/hms
  stars: 142
  title: hms
  website: https://hms.tidyverse.org/
---

The hms package provides a simple class for storing and displaying time-of-day values or durations in the hh:mm:ss format. It's designed to simplify data exchange with databases, spreadsheets, and other data sources that use time values.

The package stores times internally as seconds since midnight and supports construction from explicit hour, minute, or second values. It handles edge cases like times exceeding 24 hours or negative durations, and displays fractional seconds up to microseconds by default. The class is built on R's difftime class and works seamlessly as a data frame column, with easy coercion to and from other time formats like POSIXt.
