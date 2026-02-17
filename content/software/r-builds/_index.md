---
description: an opinionated environment for compiling R
github: rstudio/r-builds
languages:
- Shell
people:
- Gábor Csárdi
title: r-builds
website: ''

external:
  description: an opinionated environment for compiling R
  first_commit: '2019-03-25T16:56:28+00:00'
  forks: 19
  languages:
  - Shell
  last_updated: '2026-02-17T11:22:08.458697+00:00'
  license: GPL-3.0
  people:
  - Gábor Csárdi
  repo: rstudio/r-builds
  stars: 116
  title: r-builds
  website: ''
---

r-builds provides precompiled R binaries for multiple Linux distributions that can be installed side-by-side without conflicts. These binaries are built with minimal dependencies and installed to `/opt/R/${R_VERSION}`, allowing developers to run multiple R versions simultaneously on systems like Posit Workbench.

The binaries work consistently across different Linux distributions and support both x86_64 and arm64 architectures. They use OpenBLAS for performance and include patches for known security vulnerabilities in older R versions. The package includes automated builds for new R releases, quick installation scripts, and extensive testing on platforms used in production by Posit Cloud and shinyapps.io.
