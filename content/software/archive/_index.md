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

external:
  contributors:
  - jimhester
  - gaborcsardi
  - cielavenir
  - jeroen
  - coolbutuseless
  - allenluce
  - ajdamico
  - arisp99
  - jeroenjanssens
  - salim-b
  - barracuda156
  - kalibera
  description: R bindings to libarchive, supporting a large variety of archive formats
  first_commit: '2017-03-07T18:59:55+00:00'
  forks: 18
  languages:
  - C++
  last_updated: '2026-02-13T14:17:19.354315+00:00'
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

The archive package provides comprehensive R bindings to libarchive, enabling seamless reading and writing of compressed files and multi-file archives. Whether you're working with tar, ZIP, 7-zip, RAR, or other archive formats, archive offers a unified interface that integrates naturally with base R and popular packages like readr. Its automatic compression detection and connection-based API make it effortless to read compressed data directly into your analysis workflows without manual extraction steps.

Built for efficiency and flexibility, archive supports a wide range of compression methods including gzip, bzip2, lzma, and xz, allowing you to handle compressed data archives without loading entire files into memory. The package excels at extracting specific files from multi-file archives by name or number, combining archiving and compression in single operations, and providing disk-efficient methods for processing large datasets. For data scientists and developers who regularly work with archived data sources or need to distribute compressed outputs, archive simplifies the entire workflow with powerful, well-integrated tools.
