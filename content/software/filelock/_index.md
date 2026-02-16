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

external:
  contributors:
  - gaborcsardi
  - jeroenjanssens
  - orichters
  description: Cross platform file locking in R
  first_commit: '2017-05-12T18:03:59+00:00'
  forks: 7
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.470487+00:00'
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

filelock is a lightweight R package that provides cross-platform file locking capabilities for managing concurrent access to shared resources. When multiple R processes need to access the same files or data simultaneously, filelock prevents race conditions and ensures data integrity by establishing exclusive or shared locks. It handles the complexity of platform-specific locking mechanisms, using LockFile on Windows and fcntl locks on Unix-like systems, so you can write portable code without worrying about OS-level implementation details.

The package offers flexible lock acquisition with configurable timeouts, allowing processes to fail immediately, wait for a specified duration, or wait indefinitely until a lock becomes available. Locks are automatically released when a process terminates, crashes, or when the lock object is garbage collected, ensuring that resources don't remain locked indefinitely. Whether you're running parallel data processing pipelines, coordinating multiple analysis scripts, or building applications that need safe file access, filelock provides a simple and reliable solution for synchronizing operations across R processes.
