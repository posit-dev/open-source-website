---
color: '#72994E'
description: Watch the File System for Changes
github: r-lib/watcher
image: logo.svg
languages:
- C++
latest_release: '2025-12-02T00:01:06+00:00'
people:
- Charlie Gao
title: watcher
website: https://watcher.r-lib.org/

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: Watch the File System for Changes
  first_commit: '2025-01-31T23:11:05+00:00'
  forks: 2
  languages:
  - C++
  last_updated: '2026-03-20T10:27:57.267329+00:00'
  latest_release: '2025-12-02T00:01:06+00:00'
  license: NOASSERTION
  people:
  - Charlie Gao
  - Jeroen Janssens
  repo: r-lib/watcher
  stars: 35
  title: watcher
  website: https://watcher.r-lib.org/
---

watcher provides R bindings to libfswatch for monitoring file system changes. It watches files or directories recursively and executes callbacks when changes are detected, using asynchronous background monitoring that doesn't block the R session.

The package uses platform-specific, event-driven APIs (FSEvents on macOS, inotify on Linux, ReadDirectoryChangesW on Windows, etc.) for optimal performance on each operating system. It integrates with the later package to execute callbacks when R is idle, making it compatible with interactive sessions and Shiny applications. You can configure it to log changes or run custom R functions in response to file system events.
