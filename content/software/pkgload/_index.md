---
description: Simulate installing and loading a package
github: r-lib/pkgload
languages:
- R
latest_release: '2025-09-23T10:17:36+00:00'
people:
- Hadley Wickham
- Winston Chang
- Lionel Henry
- Gábor Csárdi
- Jenny Bryan
- JJ Allaire
- Daniel Falbel
- Tomasz Kalinowski
- Charlie Gao
- Jeroen Janssens
title: pkgload
website: http://pkgload.r-lib.org

external:
  description: Simulate installing and loading a package
  first_commit: '2016-11-07T21:45:48+00:00'
  forks: 53
  languages:
  - R
  last_updated: '2026-02-17T11:33:44.145633+00:00'
  latest_release: '2025-09-23T10:17:36+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Winston Chang
  - Lionel Henry
  - Gábor Csárdi
  - Jenny Bryan
  - JJ Allaire
  - Daniel Falbel
  - Tomasz Kalinowski
  - Charlie Gao
  - Jeroen Janssens
  repo: r-lib/pkgload
  stars: 59
  title: pkgload
  website: http://pkgload.r-lib.org
---

pkgload simulates installing and loading an R package without performing the full installation process, enabling much faster iteration during package development. It's typically accessed through `devtools::load_all()` rather than used directly.

The package accelerates the development workflow by eliminating the time-consuming full installation step each time you modify your package code. It was originally part of devtools but was separated into its own package as part of the devtools restructuring. This makes it faster to test changes during active development compared to repeatedly installing the package.
