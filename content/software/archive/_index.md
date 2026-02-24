---
description: R bindings to libarchive, supporting a large variety of archive formats
github: r-lib/archive
languages:
- C++
latest_release: '2025-03-24T12:32:21+00:00'
people:
- Gábor Csárdi
- Jeroen Ooms
- Jeroen Janssens
title: archive
website: https://archive.r-lib.org/

external:  # updated automatically, do not edit
  description: R bindings to libarchive, supporting a large variety of archive formats
  first_commit: '2017-03-07T18:59:55+00:00'
  forks: 18
  languages:
  - C++
  last_updated: '2026-02-24T09:26:35.092904+00:00'
  latest_release: '2025-03-24T12:32:21+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Ooms
  - Jeroen Janssens
  repo: r-lib/archive
  stars: 147
  title: archive
  website: https://archive.r-lib.org/
---

The archive package provides R bindings to libarchive for working with compressed archives and files. It supports reading and writing many archive formats including tar, ZIP, 7-zip, RAR, and CAB, as well as various compression filters like gzip, bzip2, lzma, and xz.

The package offers connection-based interfaces that integrate seamlessly with base R and tidyverse functions like readr. It handles both single-file and multi-file archives, and can automatically detect compression formats when reading files. The package also supports layered compression and filtering, allowing you to combine multiple compression methods on a single file.
