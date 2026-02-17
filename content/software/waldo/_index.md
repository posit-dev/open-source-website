---
description: Find differences between R objects
github: r-lib/waldo
image: unnamed-chunk-2.svg
languages:
- R
latest_release: '2025-07-11T13:26:57+00:00'
people:
- Hadley Wickham
- Davis Vaughan
- Tomasz Kalinowski
title: waldo
website: http://waldo.r-lib.org/

external:
  description: Find differences between R objects
  first_commit: '2020-03-29T16:00:40+00:00'
  forks: 21
  languages:
  - R
  last_updated: '2026-02-17T11:36:01.280846+00:00'
  latest_release: '2025-07-11T13:26:57+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Davis Vaughan
  - Tomasz Kalinowski
  readme_image: man/figures/README/unnamed-chunk-2.svg
  repo: r-lib/waldo
  stars: 300
  title: waldo
  website: http://waldo.r-lib.org/
---

waldo finds and describes differences between pairs of R objects, primarily designed to help debug failing unit tests. The `compare()` function works like `all.equal()` but provides more actionable output for troubleshooting.

The package prioritizes differences from most to least important, displays only the values that actually differ in atomic vectors, and uses color to highlight changes. It shows differences using executable R code paths rather than text descriptions, compares named elements by name instead of position, and includes context around changes in long vectors. The output adapts to console width with three display modes for optimal readability.
