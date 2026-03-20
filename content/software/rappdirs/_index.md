---
color: '#447099'
description: Find OS-specific directories to store data, caches, and logs. A port
  of python's AppDirs
github: r-lib/rappdirs
image: logo.svg
languages:
- R
latest_release: '2026-01-16T22:03:17+00:00'
people:
- Hadley Wickham
- Gábor Csárdi
- Jeroen Janssens
title: rappdirs
website: https://rappdirs.r-lib.org

external:  # updated automatically, do not edit
  description: Find OS-specific directories to store data, caches, and logs. A port
    of python's AppDirs
  first_commit: '2012-08-10T14:06:28+00:00'
  forks: 15
  languages:
  - R
  last_updated: '2026-03-20T10:27:51.603433+00:00'
  latest_release: '2026-01-16T22:03:17+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Gábor Csárdi
  - Jeroen Janssens
  repo: r-lib/rappdirs
  stars: 91
  title: rappdirs
  website: https://rappdirs.r-lib.org
---

The rappdirs package helps R developers find the correct platform-specific directories for storing application data like caches, logs, and user files. It automatically returns the appropriate paths for Linux, macOS, and Windows following each operating system's conventions.

The package solves the problem of where to store persistent data across R sessions while complying with CRAN policies. It provides functions for user data directories, config directories, cache directories, site data directories, and log directories, ensuring your application uses the standard locations that users and operating systems expect. This is particularly valuable for package developers who need cross-platform file storage without hardcoding paths.
