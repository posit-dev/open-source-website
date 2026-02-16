---
description: Basic R Input Output
github: r-lib/brio
languages:
- R
latest_release: '2024-04-24T18:51:12+00:00'
people:
- Gábor Csárdi
- George Stagg
- Jeroen Janssens
title: brio
website: https://brio.r-lib.org/

external:
  contributors:
  - jimhester
  - gaborcsardi
  - georgestagg
  - QuLogic
  - jeroenjanssens
  - batpigandme
  - ms609
  - salim-b
  - pbarber
  description: Basic R Input Output
  first_commit: '2020-03-20T19:53:01+00:00'
  forks: 8
  languages:
  - R
  last_updated: '2026-02-13T14:17:20.209224+00:00'
  latest_release: '2024-04-24T18:51:12+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - George Stagg
  - Jeroen Janssens
  repo: r-lib/brio
  stars: 59
  title: brio
  website: https://brio.r-lib.org/
---

Brio is a lightweight R package that simplifies file input/output operations with consistent UTF-8 handling and explicit control over line endings across different operating systems. Designed as a drop-in replacement for base R's `readLines()` and `writeLines()` functions, brio provides faster and more memory-efficient file operations while ensuring your code behaves consistently across Windows, macOS, and Linux environments. The package eliminates common encoding headaches by always reading and writing UTF-8 files, and gives you fine-grained control over line endings with functions like `read_lines()`, `write_lines()`, and `file_line_endings()`.

For R developers and data scientists working with text files, brio delivers measurable performance improvements—benchmarks show roughly 4x faster reading speeds compared to base R when processing typical text files. Beyond raw speed, brio's optimized block handling reduces memory allocations during write operations, making it particularly valuable for packages that perform frequent file I/O. Whether you're building data pipelines, maintaining cross-platform R packages, or simply want more reliable file handling without manual encoding specification, brio provides a cleaner, faster alternative to base R's file operations.
