---
color: '#D44000'
description: R Package Dependency Resolution
github: r-lib/pkgdepends
image: logo.svg
languages:
- C
latest_release: '2026-04-08T20:57:57+00:00'
people:
- Gábor Csárdi
- Hadley Wickham
- Lionel Henry
- Jenny Bryan
- Christophe Dervieux
title: pkgdepends
topics:
- MLOps and Admin
website: https://r-lib.github.io/pkgdepends/

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: R Package Dependency Resolution
  first_commit: '2017-09-09T09:17:38+00:00'
  forks: 43
  languages:
  - C
  last_updated: '2026-05-19T11:56:53.147286+00:00'
  latest_release: '2026-04-08T20:57:57+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Hadley Wickham
  - Lionel Henry
  - Jeroen Janssens
  - Jenny Bryan
  - Christophe Dervieux
  readme_image: /Users/gaborcsardi/works/pkgdepends/man/figures/README/deps.svg
  repo: r-lib/pkgdepends
  stars: 132
  title: pkgdepends
  website: https://r-lib.github.io/pkgdepends/
---

pkgdepends is a toolkit for resolving R package dependencies, downloading packages, and installing them. It's designed to be used as a building block within other R packages rather than as a standalone package manager.

The package includes a dependency solver that finds consistent package versions across your dependency tree. It supports multiple package sources including CRAN, Bioconductor, GitHub, GitLab, git repositories, and local files. All downloads and HTTP queries run concurrently, and package builds and installations happen in parallel for better performance.
