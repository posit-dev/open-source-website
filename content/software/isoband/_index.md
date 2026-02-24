---
description: 'isoband: An R package to generate contour lines and polygons.'
github: r-lib/isoband
image: logo.png
languages:
- C++
latest_release: '2025-12-05T12:51:46+00:00'
people:
- Thomas Lin Pedersen
- Hadley Wickham
- Jeroen Janssens
title: isoband
website: http://isoband.r-lib.org/

external:  # updated automatically, do not edit
  description: 'isoband: An R package to generate contour lines and polygons.'
  first_commit: '2018-12-29T06:05:34+00:00'
  forks: 16
  languages:
  - C++
  last_updated: '2026-02-24T09:26:35.924342+00:00'
  latest_release: '2025-12-05T12:51:46+00:00'
  license: NOASSERTION
  people:
  - Thomas Lin Pedersen
  - Hadley Wickham
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/isoband
  stars: 132
  title: isoband
  website: http://isoband.r-lib.org/
---

The isoband package generates contour lines (isolines) and contour polygons (isobands) from regularly spaced elevation grids. It provides two main functions, `isolines()` and `isobands()`, that take grid coordinates and elevation data as input and return lists of contour features at specified levels.

The package outputs coordinate vectors with ID information that can be rendered directly with base R grid graphics or converted to spatial features for use with ggplot2 and sf. It handles large datasets efficiently, as demonstrated with the volcano elevation dataset, and provides a simple API for creating publication-quality contour visualizations. The coordinate format makes it straightforward to integrate contour output into existing spatial data workflows.
