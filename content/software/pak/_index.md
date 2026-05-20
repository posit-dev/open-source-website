---
color: '#859900'
description: A fresh approach to package installation
github: r-lib/pak
image: cran.svg
languages:
- C
latest_release: '2026-04-27T08:54:27+00:00'
people:
- Gábor Csárdi
- Hadley Wickham
- Jenny Bryan
- Neal Richardson
- Mine Çetinkaya-Rundel
- Christophe Dervieux
title: pak
topics:
- Best Practices
- Visualization
website: https://pak.r-lib.org

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: A fresh approach to package installation
  first_commit: '2017-11-02T19:33:56+00:00'
  forks: 82
  languages:
  - C
  last_updated: '2026-05-20T08:05:56.081026+00:00'
  latest_release: '2026-04-27T08:54:27+00:00'
  people:
  - Gábor Csárdi
  - Hadley Wickham
  - Jenny Bryan
  - Neal Richardson
  - Mine Çetinkaya-Rundel
  - Jeroen Janssens
  - Christophe Dervieux
  readme_image: man/figures/cran.svg
  repo: r-lib/pak
  stars: 805
  title: pak
  website: https://pak.r-lib.org
---

pak is an R package installer that supports multiple sources including CRAN, Bioconductor, GitHub, git repositories, URLs, and local files. It serves as an alternative to `install.packages()` and `devtools::install_github()`.

pak offers three main advantages: speed through parallel downloads and caching, safety via dependency solving and system requirement management, and convenience by supporting packages from multiple sources in a single interface. It includes tools for visualizing dependency trees and explaining why specific dependencies are required, making it easier to understand and manage package installations.
