---
description: Visual regression testing and graphical diffing with testthat
github: r-lib/vdiffr
languages:
- C++
latest_release: '2026-02-13T12:48:44+00:00'
people:
- Lionel Henry
- Thomas Lin Pedersen
- Carson Sievert
- Jeroen Ooms
- Christophe Dervieux
- Jeroen Janssens
title: vdiffr
website: https://vdiffr.r-lib.org

external:
  contributors:
  - lionel-
  - thomasp85
  - nathancday
  - cpsievert
  - batpigandme
  - dpseidel
  - yutannihilation
  - jeroen
  - KZARCA
  - mcol
  - maelle
  - cderv
  - paleolimbot
  - echasnovski
  - gshotwell
  - glin
  - gwarnes-mdsol
  - ilarischeinin
  - jeroenjanssens
  - karawoo
  - khusmann
  - MichaelChirico
  - maksymiuks
  description: Visual regression testing and graphical diffing with testthat
  first_commit: '2016-03-10T17:37:46+00:00'
  forks: 37
  languages:
  - C++
  last_updated: '2026-02-13T14:17:19.021185+00:00'
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

vdiffr is a testthat extension that brings visual regression testing to R package development. When you're building packages that generate plots and graphics, it can be challenging to detect subtle visual changes that might slip through traditional unit tests. vdiffr solves this by creating reproducible SVG snapshots of your plots and integrating them into testthat's snapshot testing framework, allowing you to systematically monitor and validate plot appearance across package versions. It works seamlessly with ggplot2 objects, base graphics, recorded plots, and any object with a print method.

What makes vdiffr particularly valuable for package maintainers is its practical approach to handling visual changes. Upstream changes to the R graphics engine or plotting libraries like ggplot2 can cause subtle differences in your plots that aren't actual failures. Rather than triggering automatic test failures on CRAN from these legitimate dependency updates, vdiffr uses snapshots to help you catch genuine regressions locally while avoiding false positives. The tool includes thoughtful conveniences like automatic title standardization, default minimalistic themes for consistency, and diagnostic tools including automatic SVG diff logging during R CMD check, making it an essential tool for any R package that produces visualizations.
