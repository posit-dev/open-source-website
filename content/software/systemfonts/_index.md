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
- Jeroen Janssens
- Mine Çetinkaya-Rundel
title: systemfonts
website: https://systemfonts.r-lib.org

external:  # updated automatically, do not edit
  description: System Native Font Handling in R
  first_commit: '2019-06-04T08:45:46+00:00'
  forks: 18
  languages:
  - C++
  last_updated: '2026-03-05T16:28:55.490559+00:00'
  latest_release: '2025-10-01T11:54:44+00:00'
  license: NOASSERTION
  people:
  - Thomas Lin Pedersen
  - Jeroen Ooms
  - George Stagg
  - Hadley Wickham
  - Jeroen Janssens
  - Mine Çetinkaya-Rundel
  readme_image: man/figures/logo.png
  repo: r-lib/systemfonts
  stars: 96
  title: systemfonts
  website: https://systemfonts.r-lib.org
---

systemfonts is an R package that locates installed fonts on your system and returns the file paths needed to use them. It provides cross-platform font discovery using native libraries (CoreText on Mac, FontConfig on Linux, and Freetype on Windows).

The package solves the problem of finding and accessing fonts programmatically across different operating systems, which is particularly useful for graphics devices and plotting systems. It can query font metadata, search through all available system fonts, and manage custom fonts that aren't installed system-wide by loading them from local directories or downloading them from online repositories like Google Fonts. It also provides a C API for use in compiled code, making it valuable for package developers building graphics capabilities.
