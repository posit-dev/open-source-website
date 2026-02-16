---
description: Print Session Information
github: r-lib/sessioninfo
image: session-info2.svg
languages:
- R
latest_release: '2025-02-05T12:57:20+00:00'
people:
- Gábor Csárdi
- Jenny Bryan
- Garrick Aden-Buie
- Jeroen Janssens
- Max Kuhn
- Hadley Wickham
title: sessioninfo
website: https://sessioninfo.r-lib.org

external:
  contributors:
  - gaborcsardi
  - jennybc
  - ateucher
  - muschellij2
  - jthomasmock
  - IndrajeetPatil
  - llrs
  - gadenbuie
  - patperry
  - BrianDiggs
  - QuLogic
  - HenrikBengtsson
  - jeroenjanssens
  - jimhester
  - kevinushey
  - topepo
  - m-muecke
  - MichaelChirico
  - certara-jcraig
  - hadley
  - nash-delcamp-slp
  description: Print Session Information
  first_commit: '2017-04-21T10:27:47+00:00'
  forks: 31
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.420822+00:00'
  latest_release: '2025-02-05T12:57:20+00:00'
  license: GPL-2.0
  people:
  - Gábor Csárdi
  - Jenny Bryan
  - Garrick Aden-Buie
  - Jeroen Janssens
  - Max Kuhn
  - Hadley Wickham
  readme_image: https://raw.githubusercontent.com/r-lib/sessioninfo/main/man/figures/session-info2.svg
  repo: r-lib/sessioninfo
  stars: 79
  title: sessioninfo
  website: https://sessioninfo.r-lib.org
---

When debugging R issues or reporting bugs, understanding your computational environment is essential. sessioninfo provides a modern, enhanced alternative to R's built-in `utils::sessionInfo()`, delivering comprehensive details about your R session, packages, and system configuration. It goes beyond basic version information by revealing package sources (including GitHub repositories and commit hashes), highlighting potential installation problems like mismatched loaded and on-disk versions, and providing insights into external software dependencies, Python configurations via reticulate, and library paths.

The package shines in collaborative troubleshooting scenarios with features designed for real-world workflows. You can compare two session info outputs side-by-side using `session_diff()` to quickly identify environmental differences between systems, easily copy session details to the clipboard for sharing in bug reports, and query information about external libraries, Python environments, or specific package dependencies. Whether you're diagnosing why code works on one machine but not another, documenting reproducible analysis environments, or contributing to open-source projects that require detailed system information, sessioninfo makes capturing and sharing this critical context straightforward and actionable.