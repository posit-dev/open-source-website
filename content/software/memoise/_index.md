---
description: Easy memoisation for R
github: r-lib/memoise
languages:
- R
latest_release: '2021-11-24T21:24:31+00:00'
people:
- Hadley Wickham
- Winston Chang
- Lionel Henry
title: memoise
website: https://memoise.r-lib.org

external:
  contributors:
  - jimhester
  - hadley
  - wch
  - krlmlr
  - sietse
  - egnha
  - MarkEdmondson1234
  - mgirlich
  - coolbutuseless
  - karldw
  - xhdong-umd
  - stelsemeyer
  - richardkunze
  - mpadge
  - ajdm
  - tracykteal
  - salim-b
  - richierocks
  - mdsumner
  - batpigandme
  - lionel-
  - jsta
  - dpprdan
  - dy-kim
  - csgillespie
  description: Easy memoisation for R
  first_commit: '2010-11-11T17:37:44+00:00'
  forks: 58
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.473703+00:00'
  latest_release: '2021-11-24T21:24:31+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Winston Chang
  - Lionel Henry
  repo: r-lib/memoise
  stars: 321
  title: memoise
  website: https://memoise.r-lib.org
---

Memoise is a performance optimization package that dramatically speeds up your R code by caching function results. When you memoise a function, it automatically stores the output of each computation and returns the cached result when the same inputs are encountered again, eliminating redundant calculations. This is particularly valuable for data scientists working with computationally expensive operations like complex statistical models, database queries, or API calls where the same parameters are frequently reused.

The package offers flexible caching strategies to suit different workflows. You can use in-memory caching for fast, session-specific performance, disk-based caching to persist results across R sessions, or even cloud storage backends for distributed computing environments. Memoise also provides intelligent cache management features, including automatic expiration policies, manual cache clearing, and the ability to share caches across multiple memoised functions without conflicts. With a simple function wrapper approach, memoise integrates seamlessly into existing code and can transform functions that take seconds or minutes to run into sub-millisecond operations on subsequent calls.
