---
description: Find tools needed to build R packages
github: r-lib/pkgbuild
languages:
- R
latest_release: '2025-05-26T10:36:19+00:00'
people:
- Gábor Csárdi
- Hadley Wickham
- Jeroen Ooms
- Lionel Henry
- Jeroen Janssens
- Christophe Dervieux
title: pkgbuild
website: https://pkgbuild.r-lib.org

external:
  description: Find tools needed to build R packages
  first_commit: '2016-11-10T14:16:37+00:00'
  forks: 38
  languages:
  - R
  last_updated: '2026-02-17T11:33:46.264737+00:00'
  latest_release: '2025-05-26T10:36:19+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Hadley Wickham
  - Jeroen Ooms
  - Lionel Henry
  - Jeroen Janssens
  - Christophe Dervieux
  repo: r-lib/pkgbuild
  stars: 77
  title: pkgbuild
  website: https://pkgbuild.r-lib.org
---

pkgbuild makes it easy to build R packages that contain compiled code. It provides tools to configure your R session, verify that build tools are installed correctly, and trigger automatic installation of build tools when using RStudio.

The package helps developers avoid common build problems by checking that compilation tools are properly configured before attempting to build. It can run code in an environment guaranteed to have build tools available, and it offers configuration options to optimize the build process for packages with large directories or special compilation requirements. The package also provides helpers to determine when package DLLs need recompilation based on source file changes.
