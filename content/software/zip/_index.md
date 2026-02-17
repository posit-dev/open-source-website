---
description: Platform independent zip compression via miniz
github: r-lib/zip
languages:
- C
latest_release: '2025-05-13T13:31:24+00:00'
people:
- Gábor Csárdi
- Jeroen Janssens
- Jeroen Ooms
title: zip
website: https://r-lib.github.io/zip/

external:
  description: Platform independent zip compression via miniz
  first_commit: '2017-04-09T01:06:13+00:00'
  forks: 23
  languages:
  - C
  last_updated: '2026-02-17T11:34:11.157116+00:00'
  latest_release: '2025-05-13T13:31:24+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Janssens
  - Jeroen Ooms
  repo: r-lib/zip
  stars: 93
  title: zip
  website: https://r-lib.github.io/zip/
---

The zip package provides cross-platform tools for creating, reading, and extracting ZIP archives in R. It offers a simple interface for common compression tasks without requiring external system dependencies.

This package solves the problem of ZIP file handling across different operating systems by using a pure R implementation with C code. It supports background processing for compression and decompression operations, allowing non-blocking archive operations. The package can append files to existing archives, list archive contents with metadata like permissions and timestamps, and recursively add directories.
