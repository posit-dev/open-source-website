---
color: '#447099'
description: Sliding Window Functions
github: r-lib/slider
image: logo.svg
languages:
- R
latest_release: '2025-11-14T20:31:30+00:00'
people:
- Davis Vaughan
- Gábor Csárdi
- Jeroen Janssens
title: slider
website: https://slider.r-lib.org

external:  # updated automatically, do not edit
  description: Sliding Window Functions
  first_commit: '2019-07-01T03:02:14+00:00'
  forks: 13
  languages:
  - R
  last_updated: '2026-03-05T16:28:57.882469+00:00'
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

slider provides a family of general-purpose sliding window functions for R with an API similar to purrr. It computes rolling calculations like moving averages, cumulative sums, or rolling regressions by iterating over data with a sliding window that always returns output the same size as the input.

The package offers three core approaches: `slide()` for standard fixed-width windows, `slide_index()` for index-aware calculations relative to irregular time series (like computing 3-month rolling averages where months have different lengths), and `slide_period()` for sliding over time blocks. It includes optimized C implementations for common operations like `slide_mean()` and `slide_sum()` that are significantly faster than general-purpose equivalents. The package handles data frames in a row-wise fashion, making operations like rolling regressions straightforward.
