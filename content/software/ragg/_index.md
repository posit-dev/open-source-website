---
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
title: ragg
website: https://ragg.r-lib.org

external:
  contributors:
  - thomasp85
  - jeroen
  - espinielli
  - yutannihilation
  - klausbrunner
  - alexreg
  - arni-magnusson
  - edavidaja
  - QuLogic
  - hadley
  - jimhester
  - kevinushey
  - pmur002
  - trevorld
  - yixuan
  - olivroy
  description: Graphic Devices Based on AGG
  first_commit: '2019-03-15T10:11:11+00:00'
  forks: 30
  languages:
  - C++
  last_updated: '2026-02-13T14:17:20.061720+00:00'
  latest_release: '2025-09-02T06:41:38+00:00'
  license: NOASSERTION
  people:
  - Thomas Lin Pedersen
  - Jeroen Ooms
  - Hadley Wickham
  readme_image: man/figures/logo.png
  repo: r-lib/ragg
  stars: 181
  title: ragg
  website: https://ragg.r-lib.org
---

ragg provides modern, high-performance graphics devices for R based on the AGG (Anti-Grain Geometry) library. As a drop-in replacement for R's standard raster devices, ragg delivers up to 40% faster rendering while producing higher quality output with enhanced anti-aliasing. The package ensures consistent, pixel-perfect graphics across macOS, Windows, and Linux, eliminating the platform-specific inconsistencies that often plague data visualization workflows.

Whether you're generating publication-ready plots or interactive graphics for reports, ragg offers advanced features that elevate your visual output. It provides sophisticated text rendering with support for right-to-left text, emoji integration, and automatic font fallback, allowing you to use system fonts directly without conversion. The package integrates seamlessly with knitr and RStudio, making it easy to adopt as your default graphics backend. With support for 16-bit color depth, high-quality rotated text, and functions like `agg_png()`, `agg_jpeg()`, and `agg_tiff()`, ragg empowers data scientists and developers to create stunning, reproducible visualizations with minimal effort.