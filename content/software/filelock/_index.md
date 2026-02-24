---
description: Cross platform file locking in R
github: r-lib/filelock
languages:
- R
latest_release: '2023-12-11T01:11:32+00:00'
people:
- Gábor Csárdi
- Jeroen Janssens
title: filelock
website: https://r-lib.github.io/filelock/

external:  # updated automatically, do not edit
  description: Cross platform file locking in R
  first_commit: '2017-05-12T18:03:59+00:00'
  forks: 7
  languages:
  - R
  last_updated: '2026-02-24T09:26:35.235471+00:00'
  latest_release: '2023-12-11T01:11:32+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Janssens
  repo: r-lib/filelock
  stars: 44
  title: filelock
  website: https://r-lib.github.io/filelock/
---

The filelock package provides portable file locking for R across Windows and Unix-like systems, using platform-specific mechanisms (LockFile on Windows, fcntl on Unix). It enables processes to place exclusive or shared locks on files to coordinate access and prevent conflicts.

The package implements advisory locks (Unix) or mandatory locks (Windows) that are automatically released when a process terminates or when the lock object is garbage collected. It supports configurable timeout intervals for lock acquisition, including blocking indefinitely until a lock becomes available. The package is designed to work with dedicated lock files rather than locking actual data files directly, which avoids undefined behavior when reading or writing locked files.
