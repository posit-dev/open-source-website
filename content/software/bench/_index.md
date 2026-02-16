---
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

external:
  contributors:
  - jimhester
  - DavisVaughan
  - lionel-
  - jdblischak
  - krlmlr
  - batpigandme
  - olivroy
  - MichaelChirico
  - oranwutang
  - tmstauss
  - romainfrancois
  - Robinlovelace
  - plietar
  - lorenzwalthert
  - jeroenjanssens
  - coatless
  - HughParsonage
  - espinielli
  - davidchall
  - hhau
  description: High Precision Timing of R Expressions
  first_commit: '2018-04-10T18:01:13+00:00'
  forks: 25
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.714252+00:00'
  latest_release: '2025-01-16T22:42:26+00:00'
  license: NOASSERTION
  people:
  - Davis Vaughan
  - Lionel Henry
  - Jeroen Janssens
  readme_image: man/figures/README-autoplot-1.png
  repo: r-lib/bench
  stars: 254
  title: bench
  website: http://bench.r-lib.org/
---

bench is a powerful benchmarking package for R that provides high-precision timing of code execution while tracking memory allocations and garbage collections. It helps data scientists and developers accurately measure and compare the performance of different approaches to solving the same problem, ensuring that optimizations actually improve performance rather than simply changing implementation details. The package uses the highest precision timing APIs available on each operating system and verifies that different expressions produce equivalent results, preventing common benchmarking mistakes.

Key features include adaptive stopping that runs expressions for a consistent amount of time rather than a fixed number of iterations, automatic filtering of iterations affected by garbage collection to isolate true performance characteristics, and human-readable output with custom formatting for times and memory usage. The package also provides bench::press() for easily benchmarking across grids of parameters, full integration with ggplot2 for visualization with custom scales and geoms, and system_time() as a more precise alternative to base R's system.time(). Together, these capabilities make bench an essential tool for performance optimization and comparing alternative implementations in R.