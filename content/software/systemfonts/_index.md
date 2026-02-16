---
description: System Native Font Handling in R
github: r-lib/systemfonts
image: logo.png
languages:
- C++
latest_release: '2025-10-01T11:54:44+00:00'
people:
- Thomas Lin Pedersen
- Jeroen Ooms
- George Stagg
- Hadley Wickham
- Mine Çetinkaya-Rundel
title: systemfonts
website: https://systemfonts.r-lib.org

external:
  contributors:
  - thomasp85
  - jeroen
  - jimhester
  - einsibjarni
  - georgestagg
  - hadley
  - yutannihilation
  - jan-glx
  - kevinushey
  - batpigandme
  - MichaelChirico
  - mine-cetinkaya-rundel
  - musvaage
  - pekkarr
  description: System Native Font Handling in R
  first_commit: '2019-06-04T08:45:46+00:00'
  forks: 17
  languages:
  - C++
  last_updated: '2026-02-13T14:17:20.126425+00:00'
  latest_release: '2025-10-01T11:54:44+00:00'
  license: NOASSERTION
  people:
  - Thomas Lin Pedersen
  - Jeroen Ooms
  - George Stagg
  - Hadley Wickham
  - Mine Çetinkaya-Rundel
  readme_image: man/figures/logo.png
  repo: r-lib/systemfonts
  stars: 95
  title: systemfonts
  website: https://systemfonts.r-lib.org
---

Creating high-quality data visualizations and documents in R often requires precise control over typography, but managing fonts across different operating systems can be surprisingly complex. systemfonts solves this challenge by providing a unified interface to locate and work with fonts installed on your system, leveraging native libraries like CoreText on macOS, FontConfig on Linux, and the Windows font registry.

Whether you're building graphics with ggplot2, creating reports with R Markdown, or developing packages that need reliable font access, systemfonts makes it easy to discover available fonts, match them by family and style, and retrieve detailed font metadata. The package goes beyond system fonts by allowing you to register custom fonts from local files or even fetch fonts on-demand from online repositories like Google Fonts. With special cross-platform aliases for common font categories (sans, serif, mono, emoji) and a C/C++ API for package developers, systemfonts provides the foundation for consistent, professional typography in R graphics and documents across any platform.
