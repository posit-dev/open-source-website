---
color: '#72994E'
description: R bindings to libarchive, supporting a large variety of archive formats
github: r-lib/archive
image: logo.svg
languages:
- C++
latest_release: '2026-04-11T20:54:37+00:00'
people:
- Gábor Csárdi
- Jeroen Ooms
title: archive
topics:
- Data Wrangling
website: https://archive.r-lib.org/

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: R bindings to libarchive, supporting a large variety of archive formats
  first_commit: '2017-03-07T18:59:55+00:00'
  forks: 18
  languages:
  - C++
  last_updated: '2026-05-20T08:05:55.765752+00:00'
  latest_release: '2026-04-11T20:54:37+00:00'
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
