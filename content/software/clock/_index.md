---
color: '#046D0C'
description: A Date-Time Library for R
github: r-lib/clock
image: logo.png
languages:
- R
latest_release: '2026-01-13T16:12:36+00:00'
people:
- Davis Vaughan
- Jenny Bryan
- Jeroen Janssens
- Lionel Henry
title: clock
website: https://clock.r-lib.org

external:  # updated automatically, do not edit
  description: A Date-Time Library for R
  first_commit: '2020-10-26T19:27:27+00:00'
  forks: 7
  languages:
  - R
  last_updated: '2026-03-05T16:29:44.168508+00:00'
  latest_release: '2026-01-13T16:12:36+00:00'
  license: NOASSERTION
  people:
  - Davis Vaughan
  - Jenny Bryan
  - Jeroen Janssens
  - Lionel Henry
  readme_image: man/figures/logo.png
  repo: r-lib/clock
  stars: 110
  title: clock
  website: https://clock.r-lib.org
---

clock is an R package for working with date-times, providing tools for parsing, formatting, arithmetic, rounding, and extracting or updating components. It offers both a high-level API for R's native Date and POSIXct types and a low-level API with new date-time classes designed to minimize time zone complications.

The package introduces four core date-time types (durations, time points, zoned-times, and calendars) that partition responsibilities for different operations. It requires explicit handling of invalid dates and ambiguous times caused by daylight saving time, preventing silent errors. Built on the high-performance C++ date library, clock efficiently handles irregular periods like months and quarters while providing correct time zone conversions.
