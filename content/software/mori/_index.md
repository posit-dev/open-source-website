---
color: '#d2604a'
description: Shared Memory for R Objects
github: r-lib/mori
image: logo.svg
languages:
- C
latest_release: '2026-07-21T10:06:26+00:00'
people:
- Charlie Gao
title: mori
topics:
- Best Practices
website: https://mori.r-lib.org/

external:  # updated automatically, do not edit
  description: Shared Memory for R Objects
  first_commit: '2026-04-16T11:27:41+00:00'
  forks: 4
  languages:
  - C
  last_updated: '2026-09-18T14:31:52.576012+00:00'
  latest_release: '2026-07-21T10:06:26+00:00'
  license: NOASSERTION
  people:
  - Charlie Gao
  readme_image: man/figures/logo.svg
  repo: r-lib/mori
  stars: 144
  title: mori
  website: https://mori.r-lib.org/
---

mori shares R objects across processes on the same machine via a single copy in OS-level shared memory — POSIX shared memory on Linux and macOS, Win32 file mapping on Windows. Every process reads from the same physical pages through the R ALTREP framework, giving lazy, zero-copy access.

`share()` writes an R object into shared memory and returns an ALTREP wrapper that behaves like a regular R vector. Shared objects serialize compactly as their shared-memory name rather than their full contents, so sending a shared data frame to a mirai daemon transmits ~300 bytes instead of the underlying 200 MB. Shared memory is managed by R's garbage collector and freed automatically when the last reference is dropped, and consumer processes see the data as read-only so copy-on-write keeps mutations local.
