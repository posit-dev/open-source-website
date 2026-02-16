---
description: Simple Arrays
github: r-lib/rray
image: logo.png
languages:
- R
latest_release: '2019-07-24T13:42:10+00:00'
people:
- Davis Vaughan
title: rray
website: https://rray.r-lib.org

external:
  contributors:
  - DavisVaughan
  - dirkschumacher
  - batpigandme
  - RaymondBalise
  description: Simple Arrays
  first_commit: '2018-10-25T16:08:05+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.945745+00:00'
  latest_release: '2019-07-24T13:42:10+00:00'
  license: GPL-3.0
  people:
  - Davis Vaughan
  readme_image: man/figures/logo.png
  repo: r-lib/rray
  stars: 128
  title: rray
  website: https://rray.r-lib.org
---

rray is an array manipulation library designed to make working with multi-dimensional data in R more intuitive and consistent. While base R provides array functionality, it often exhibits unexpected behaviors like dimension dropping and lacks automatic broadcasting capabilities found in modern array libraries. rray addresses these limitations by introducing a stricter array class with consistent semantics and powerful dimension-aware operations, making complex array computations more straightforward and reliable.

What sets rray apart is its comprehensive approach to array handling, inspired by the tibble philosophy of stricter, more predictable behavior. The package enables automatic dimension alignment through broadcasting, allowing arrays of different shapes to work together seamlessly without manual preprocessing. Functions like `rray_bind()` can combine arrays with mismatched dimensions by automatically broadcasting them to compatible shapes, while operations consistently preserve dimensions instead of unexpectedly dropping them. Whether you're performing sophisticated numerical computations, working with tensor-like data structures, or need NumPy-style broadcasting in R, rray bridges the gap between R's native capabilities and modern array computing requirements.
