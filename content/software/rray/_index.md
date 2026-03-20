---
color: '#B8150B'
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

external:  # updated automatically, do not edit
  description: Simple Arrays
  first_commit: '2018-10-25T16:08:05+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-03-20T10:27:54.960065+00:00'
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

rray is an array manipulation library for R that provides stricter, more consistent array operations and implements broadcasting throughout the package. Broadcasting allows arrays of different dimensions to be combined in operations without manual reshaping, similar to NumPy's behavior.

The package solves common array manipulation challenges by automatically handling dimension mismatches through broadcasting and consistently preserving dimensions where base R would drop them. It provides a unified toolkit that works with both its own rray class and base R matrices/arrays, offering more intuitive alternatives to functions like `sweep()`, `cbind()`, and `rbind()`. The implementation is built on the xtensor C++ library and uses vctrs for type stability.
