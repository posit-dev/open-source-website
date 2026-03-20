---
color: '#EE6331'
description: Finding files in project subdirectories
github: r-lib/rprojroot
image: logo.svg
languages:
- R
latest_release: '2025-08-26T15:22:36+00:00'
people:
- Jenny Bryan
- Garrick Aden-Buie
title: rprojroot
website: https://rprojroot.r-lib.org/

external:  # updated automatically, do not edit
  description: Finding files in project subdirectories
  first_commit: '2015-05-19T02:10:40+00:00'
  forks: 23
  languages:
  - R
  last_updated: '2026-03-20T10:27:51.969604+00:00'
  latest_release: '2025-08-26T15:22:36+00:00'
  license: NOASSERTION
  people:
  - Jenny Bryan
  - Garrick Aden-Buie
  repo: r-lib/rprojroot
  stars: 149
  title: rprojroot
  website: https://rprojroot.r-lib.org/
---

The rprojroot package helps R developers access files relative to a project root directory, eliminating dependency on the current working directory. It identifies project roots using strict criteria (like detecting a DESCRIPTION file for R packages) and provides functions to construct file paths from that root.

The package solves the problem of fragile code that breaks when run from different directories within a project. It works by searching up the directory tree from your current location to find the project root based on customizable criteria, then constructs paths relative to that root. This makes file paths consistent regardless of where your script is executed from, and it serves as the foundation for the higher-level `here` package.
