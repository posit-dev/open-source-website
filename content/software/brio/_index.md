---
color: '#E7B10A'
description: Basic R Input Output
github: r-lib/brio
image: logo.svg
languages:
- R
latest_release: '2024-04-24T18:51:12+00:00'
people:
- Gábor Csárdi
- George Stagg
- Jeroen Janssens
title: brio
website: https://brio.r-lib.org/

external:  # updated automatically, do not edit
  description: Basic R Input Output
  first_commit: '2020-03-20T19:53:01+00:00'
  forks: 8
  languages:
  - R
  last_updated: '2026-03-05T16:29:08.359839+00:00'
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

brio is an R package that provides basic file input/output functions with guaranteed UTF-8 encoding and explicit control over line endings. It offers simple, reliable functions for reading and writing text files.

The package solves encoding inconsistencies by always using UTF-8, unlike base R functions which depend on system locale. It provides faster file reading than base R (roughly 4x faster) through larger block sizes and fewer memory copies. brio includes drop-in replacements for `base::readLines()` and `base::writeLines()` that allow straightforward package migration.
