---
description: Watch the File System for Changes
github: r-lib/watcher
languages:
- C++
latest_release: '2025-12-02T00:01:06+00:00'
people:
- Charlie Gao
- Jeroen Janssens
title: watcher
website: https://watcher.r-lib.org/

external:
  contributors:
  - shikokuchuo
  - jeroenjanssens
  description: Watch the File System for Changes
  first_commit: '2025-01-31T23:11:05+00:00'
  forks: 2
  languages:
  - C++
  last_updated: '2026-02-13T14:17:20.786362+00:00'
  latest_release: '2025-12-02T00:01:06+00:00'
  license: NOASSERTION
  people:
  - Charlie Gao
  - Jeroen Janssens
  repo: r-lib/watcher
  stars: 33
  title: watcher
  website: https://watcher.r-lib.org/
---

watcher provides efficient, cross-platform file system monitoring for R. Built on libfswatch, it automatically detects changes to files and directories using native operating system APIs like FSEvents on macOS, inotify on Linux, and ReadDirectoryChangesW on Windows. Whether you're developing data pipelines that need to trigger when new data arrives, building reactive applications, or automating workflows based on file changes, watcher provides a lightweight solution that runs asynchronously without blocking your R session.

The package makes it simple to watch files or entire directory trees recursively, and respond to changes either by logging events or executing custom R functions. With seamless integration into R's event loop through the later package, watcher is particularly well-suited for Shiny applications and interactive development workflows where you need to react to file system changes in real-time. The underlying event-driven architecture ensures optimal performance across all platforms, making it a reliable choice for production environments where monitoring file system activity is critical.
