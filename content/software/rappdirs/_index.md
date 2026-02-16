---
description: Find OS-specific directories to store data, caches, and logs. A port
  of python's AppDirs
github: r-lib/rappdirs
languages:
- R
latest_release: '2026-01-16T22:03:17+00:00'
people:
- Hadley Wickham
- Gábor Csárdi
- Jeroen Janssens
title: rappdirs
website: https://rappdirs.r-lib.org

external:
  contributors:
  - hadley
  - gaborcsardi
  - trevorld
  - jefferis
  - fmichonneau
  - jeroenjanssens
  description: Find OS-specific directories to store data, caches, and logs. A port
    of python's AppDirs
  first_commit: '2012-08-10T14:06:28+00:00'
  forks: 15
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.556903+00:00'
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

Every application needs to store data somewhere, but where should that data live? The answer varies dramatically between macOS, Windows, and Linux, each with their own conventions and best practices. rappdirs solves this cross-platform puzzle by providing a simple, reliable way to find the right directories for your application's data, caches, configuration files, and logs. A port of Python's popular AppDirs library, rappdirs ensures your R packages follow operating system conventions while staying compliant with CRAN policies.

Whether you're building a package that needs to cache downloaded files, store user preferences, or maintain logs, rappdirs handles the platform-specific details for you. With five core functions—`user_data_dir()`, `user_config_dir()`, `user_cache_dir()`, `site_data_dir()`, and `user_log_dir()`—the package automatically adapts to the appropriate locations on each operating system, from `~/Library/Application Support/` on macOS to XDG Base Directory paths on Linux. This means you can write portable code that works seamlessly across all major platforms without worrying about the underlying file system conventions.
