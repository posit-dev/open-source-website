---
color: '#D44000'
description: Easy memoisation for R
github: r-lib/memoise
image: logo.svg
languages:
- R
latest_release: '2021-11-24T21:24:31+00:00'
people:
- Hadley Wickham
- Winston Chang
- Lionel Henry
title: memoise
website: https://memoise.r-lib.org

external:  # updated automatically, do not edit
  description: Easy memoisation for R
  first_commit: '2010-11-11T17:37:44+00:00'
  forks: 58
  languages:
  - R
  last_updated: '2026-03-20T10:27:51.488197+00:00'
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

The memoise package implements memoization for R functions, which caches function results so that repeated calls with the same inputs return previously computed outputs without re-executing the function. This speeds up expensive computations when functions are called multiple times with identical arguments.

The package uses the cachem library for caching, which provides automatic pruning to prevent caches from growing indefinitely. You can cache in memory or on disk, customize cache size and expiration times, and share caches between multiple functions. The cache key includes both function arguments and the function body itself, preventing collisions when different memoised functions are called with the same arguments.
