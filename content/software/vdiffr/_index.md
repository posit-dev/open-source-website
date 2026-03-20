---
color: '#404041'
description: Visual regression testing and graphical diffing with testthat
github: r-lib/vdiffr
image: logo.svg
languages:
- C++
latest_release: '2026-02-13T12:48:44+00:00'
people:
- Lionel Henry
- Thomas Lin Pedersen
- Carson Sievert
- Jeroen Ooms
- Christophe Dervieux
title: vdiffr
website: https://vdiffr.r-lib.org

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: Visual regression testing and graphical diffing with testthat
  first_commit: '2016-03-10T17:37:46+00:00'
  forks: 37
  languages:
  - C++
  last_updated: '2026-03-20T10:27:52.630640+00:00'
  latest_release: '2026-02-13T12:48:44+00:00'
  license: NOASSERTION
  people:
  - Lionel Henry
  - Thomas Lin Pedersen
  - Carson Sievert
  - Jeroen Ooms
  - Christophe Dervieux
  - Jeroen Janssens
  repo: r-lib/vdiffr
  stars: 195
  title: vdiffr
  website: https://vdiffr.r-lib.org
---

vdiffr is a testthat extension for R that monitors the visual appearance of plots by generating reproducible SVG files and tracking them as snapshots. It helps developers test that their plotting code produces consistent visual output across code changes and environments.

The package works by comparing current plot output against saved baseline snapshots, making it valuable for catching unintended visual regressions in plotting code. It handles both base R graphics and ggplot2 plots, and includes a review workflow for approving legitimate changes to plot appearance. The package is designed to avoid false failures on CRAN by only flagging visual differences in local development and CI environments where they can be properly reviewed.
