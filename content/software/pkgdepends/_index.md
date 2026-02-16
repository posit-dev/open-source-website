---
description: R Package Dependency Resolution
github: r-lib/pkgdepends
languages:
- C
latest_release: '2025-05-27T06:57:46+00:00'
people:
- Gábor Csárdi
- Hadley Wickham
- Lionel Henry
- Jeroen Janssens
- Jenny Bryan
- Christophe Dervieux
title: pkgdepends
website: https://r-lib.github.io/pkgdepends/

external:
  contributors:
  - gaborcsardi
  - jimhester
  - pat-s
  - hadley
  - krlmlr
  - dgkf
  - jameslairdsmith
  - paleolimbot
  - olivroy
  - salim-b
  - pawelru
  - Luke-Symes-Tsy
  - lionel-
  - joachim-gassen
  - jeroenjanssens
  - jennybc
  - Fan-iX
  - cderv
  - katrinabrock
  - billdenney
  description: R Package Dependency Resolution
  first_commit: '2017-09-09T09:17:38+00:00'
  forks: 39
  languages:
  - C
  last_updated: '2026-02-13T14:17:19.570600+00:00'
  latest_release: '2025-05-27T06:57:46+00:00'
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
  stars: 129
  title: pkgdepends
  website: https://r-lib.github.io/pkgdepends/
---

pkgdepends is a comprehensive toolkit for handling R package dependencies, downloads, and installations. It provides the core infrastructure for resolving complex dependency trees, supporting diverse package sources including CRAN, Bioconductor, GitHub, GitLab, git repositories, and local files. With built-in caching, concurrent downloads, and a sophisticated dependency solver, pkgdepends ensures that all package requirements are satisfied efficiently and reliably.

Designed as a developer toolkit rather than a standalone tool, pkgdepends is ideal for building R packages and applications that require sophisticated dependency management capabilities. Its parallel processing features and integration with pkgcache make it particularly valuable for creating tools that need to handle package installations at scale. Whether you're developing package management utilities, continuous integration pipelines, or automated R environments, pkgdepends provides the robust foundation needed to manage dependencies programmatically with confidence.
