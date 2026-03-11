---
color: '#F35C5D'
description: High Precision Timing of R Expressions
github: r-lib/bench
image: README-autoplot-1.png
languages:
- R
latest_release: '2025-01-16T22:42:26+00:00'
people:
- Davis Vaughan
- Lionel Henry
- Jeroen Janssens
title: bench
website: http://bench.r-lib.org/

external:  # updated automatically, do not edit
  description: High Precision Timing of R Expressions
  first_commit: '2018-04-10T18:01:13+00:00'
  forks: 25
  languages:
  - R
  last_updated: '2026-03-05T16:27:57.219795+00:00'
  latest_release: '2025-01-16T22:42:26+00:00'
  license: NOASSERTION
  people:
  - Davis Vaughan
  - Lionel Henry
  - Jeroen Janssens
  readme_image: man/figures/README-autoplot-1.png
  repo: r-lib/bench
  stars: 255
  title: bench
  website: http://bench.r-lib.org/
---

bench is a high-precision benchmarking package for R that measures code execution time, memory allocations, and garbage collection activity. It provides tools to compare the performance of different expressions and ensure they produce equivalent results.

The package uses the highest precision timing APIs available on each operating system and implements adaptive stopping to run expressions for a set duration rather than a fixed number of iterations. It filters out iterations affected by garbage collection to provide more accurate measurements, includes `bench::press()` for benchmarking across parameter grids, and returns results with human-readable units and built-in ggplot2 plotting support. The package verifies that compared expressions produce equal results by default, preventing accidental comparison of non-equivalent code.
