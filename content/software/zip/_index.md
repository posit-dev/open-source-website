---
color: '#D44000'
description: Platform independent zip compression via miniz
github: r-lib/zip
image: logo.svg
languages:
- C
latest_release: '2025-05-13T13:31:24+00:00'
people:
- Gábor Csárdi
- Jeroen Ooms
title: zip
topics:
- MLOps and Admin
website: https://r-lib.github.io/zip/

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: Platform independent zip compression via miniz
  first_commit: '2017-04-09T01:06:13+00:00'
  forks: 24
  languages:
  - C
  last_updated: '2026-05-20T08:05:55.828593+00:00'
  latest_release: '2025-05-13T13:31:24+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Janssens
  - Jeroen Ooms
  repo: r-lib/zip
  stars: 95
  title: zip
  website: https://r-lib.github.io/zip/
---

The zip package provides cross-platform tools for creating, reading, and extracting ZIP archives in R. It offers a simple interface for common compression tasks without requiring external system dependencies.

This package solves the problem of ZIP file handling across different operating systems by using a pure R implementation with C code. It supports background processing for compression and decompression operations, allowing non-blocking archive operations. The package can append files to existing archives, list archive contents with metadata like permissions and timestamps, and recursively add directories.
