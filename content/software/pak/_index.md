---
description: A fresh approach to package installation
github: r-lib/pak
image: cran.svg
color: "#859900"
languages:
- C
latest_release: '2025-12-21T19:30:49+00:00'
people:
- Gábor Csárdi
- Hadley Wickham
- Jeroen Janssens
- Mine Çetinkaya-Rundel
- Neal Richardson
- Jenny Bryan
- Christophe Dervieux
title: pak
website: https://pak.r-lib.org

external:  # updated automatically, do not edit
  description: A fresh approach to package installation
  first_commit: '2017-11-02T19:33:56+00:00'
  forks: 78
  languages:
  - C
  last_updated: '2026-03-05T16:27:38.946207+00:00'
  latest_release: '2025-12-21T19:30:49+00:00'
  people:
  - Gábor Csárdi
  - Hadley Wickham
  - Jeroen Janssens
  - Mine Çetinkaya-Rundel
  - Neal Richardson
  - Jenny Bryan
  - Christophe Dervieux
  readme_image: man/figures/cran.svg
  repo: r-lib/pak
  stars: 787
  title: pak
  website: https://pak.r-lib.org
---

pak is an R package installer that supports multiple sources including CRAN, Bioconductor, GitHub, git repositories, URLs, and local files. It serves as an alternative to `install.packages()` and `devtools::install_github()`.

pak offers three main advantages: speed through parallel downloads and caching, safety via dependency solving and system requirement management, and convenience by supporting packages from multiple sources in a single interface. It includes tools for visualizing dependency trees and explaining why specific dependencies are required, making it easier to understand and manage package installations.
