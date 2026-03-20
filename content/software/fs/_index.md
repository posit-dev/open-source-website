---
color: '#53366B'
description: Provide cross platform file operations based on libuv.
github: r-lib/fs
image: logo.png
languages:
- R
latest_release: '2025-04-12T09:38:14+00:00'
people:
- Gábor Csárdi
- Hadley Wickham
- Jenny Bryan
- Jeroen Ooms
- Winston Chang
- Christophe Dervieux
- Garrick Aden-Buie
title: fs
website: https://fs.r-lib.org/

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: Provide cross platform file operations based on libuv.
  first_commit: '2017-12-13T21:01:16+00:00'
  forks: 82
  languages:
  - R
  last_updated: '2026-03-20T10:27:54.174790+00:00'
  latest_release: '2025-04-12T09:38:14+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Hadley Wickham
  - Jenny Bryan
  - Jeroen Ooms
  - Winston Chang
  - Christophe Dervieux
  - Garrick Aden-Buie
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/fs
  stars: 382
  title: fs
  website: https://fs.r-lib.org/
---

The fs package provides a cross-platform, uniform interface to file system operations in R, built on the libuv C library that powers Node.js. It offers a consistent API for working with paths, files, directories, and links across different operating systems.

The package addresses key inconsistencies in base R's file handling functions through full vectorization of all operations, predictable return values that always convey paths, explicit error handling instead of warnings with system-dependent codes, and UTF-8 encoding for all paths across platforms. It uses a consistent naming convention and returns "tidy" paths that always use forward slashes as delimiters, making file system operations more reliable and easier to debug. The package integrates well with tidyverse tools for tasks like filtering files by attributes, tabulating folder sizes, and reading multiple files into data frames.
