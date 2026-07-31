---
color: '#9A4665'
description: Simulate installing and loading a package
github: r-lib/pkgload
image: logo.svg
languages:
- R
latest_release: '2026-06-15T13:07:26+00:00'
people:
- Hadley Wickham
- Lionel Henry
- Winston Chang
- Gábor Csárdi
- Jenny Bryan
- Kevin Ushey
- JJ Allaire
- Daniel Falbel
- Tomasz Kalinowski
- Charlie Gao
title: pkgload
topics:
- Best Practices
website: http://pkgload.r-lib.org

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: Simulate installing and loading a package
  first_commit: '2016-11-07T21:45:48+00:00'
  forks: 52
  languages:
  - R
  last_updated: '2026-07-21T09:49:49.294354+00:00'
  latest_release: '2026-06-15T13:07:26+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  - Winston Chang
  - Gábor Csárdi
  - Jenny Bryan
  - Kevin Ushey
  - JJ Allaire
  - Daniel Falbel
  - Tomasz Kalinowski
  - Charlie Gao
  - Jeroen Janssens
  repo: r-lib/pkgload
  stars: 61
  title: pkgload
  website: http://pkgload.r-lib.org
---

pkgload simulates installing and loading an R package without performing the full installation process, enabling much faster iteration during package development. It's typically accessed through `devtools::load_all()` rather than used directly.

The package accelerates the development workflow by eliminating the time-consuming full installation step each time you modify your package code. It was originally part of devtools but was separated into its own package as part of the devtools restructuring. This makes it faster to test changes during active development compared to repeatedly installing the package.
