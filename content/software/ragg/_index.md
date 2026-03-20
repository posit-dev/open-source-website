---
color: '#DFB97E'
description: Graphic Devices Based on AGG
github: r-lib/ragg
image: logo.png
languages:
- C++
latest_release: '2025-09-02T06:41:38+00:00'
people:
- Thomas Lin Pedersen
- Jeroen Ooms
- Hadley Wickham
- Jeroen Janssens
tags:
- tidyverse
title: ragg
website: https://ragg.r-lib.org

external:  # updated automatically, do not edit
  description: Graphic Devices Based on AGG
  first_commit: '2019-03-15T10:11:11+00:00'
  forks: 30
  languages:
  - C++
  last_updated: '2026-03-20T10:27:55.326423+00:00'
  latest_release: '2025-09-02T06:41:38+00:00'
  license: NOASSERTION
  people:
  - Thomas Lin Pedersen
  - Jeroen Ooms
  - Hadley Wickham
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/ragg
  stars: 181
  title: ragg
  website: https://ragg.r-lib.org
---

ragg provides high-performance graphic devices for R based on the AGG library, offering drop-in replacements for the standard PNG, JPEG, and TIFF devices in grDevices. It renders plots and graphics with improved speed and quality compared to R's default raster devices.

The package delivers faster rendering (up to 40% faster than anti-aliased cairo), direct access to system fonts with advanced text features like right-to-left support and emoji rendering, high-quality anti-aliasing, and system-independent output that looks identical across Mac, Windows, and Linux. It also supports 16-bit output and includes a capture device for accessing rendered graphics directly as raster data in R. The package integrates with knitr and can be set as the default graphics backend in RStudio.
