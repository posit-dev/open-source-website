---
description: Sliding Window Functions
github: r-lib/slider
languages:
- R
latest_release: '2025-11-14T20:31:30+00:00'
people:
- Davis Vaughan
- Gábor Csárdi
- Jeroen Janssens
title: slider
website: https://slider.r-lib.org

external:
  contributors:
  - DavisVaughan
  - gaborcsardi
  - dpprdan
  - Edgar-Zamora
  - jeroenjanssens
  description: Sliding Window Functions
  first_commit: '2019-07-01T03:02:14+00:00'
  forks: 13
  languages:
  - R
  last_updated: '2026-02-13T14:17:20.143341+00:00'
  latest_release: '2025-11-14T20:31:30+00:00'
  license: NOASSERTION
  people:
  - Davis Vaughan
  - Gábor Csárdi
  - Jeroen Janssens
  repo: r-lib/slider
  stars: 310
  title: slider
  website: https://slider.r-lib.org
---

slider is an R package that provides powerful sliding window functions for computing rolling calculations across your data. Whether you need to calculate moving averages, cumulative statistics, or rolling regressions, slider offers an intuitive and performant API with three core functions: slide() for standard sliding windows, slide_index() for calculations relative to irregular time periods, and slide_period() for time-based grouping. Built with C-level optimization for speed, the package includes specialized high-performance variants like slide_sum() and slide_mean() for common operations, while maintaining type stability and flexible control through .before and .after parameters.

What makes slider particularly valuable for data scientists is its row-wise iteration over data frames, aligned with R's vctrs framework, which makes complex operations like rolling regressions remarkably straightforward. Unlike earlier solutions, slider provides a more intuitive interface while supporting any object type, not just numeric data. Whether you're analyzing time series data, building financial models, or performing statistical analysis with moving windows, slider delivers the performance and flexibility you need with an API that mirrors the familiar purrr package structure, making it easy to integrate into your existing workflows.
