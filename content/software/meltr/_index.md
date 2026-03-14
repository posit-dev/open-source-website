---
color: '#E7B10A'
description: Read Non-Rectangular Text Data
github: r-lib/meltr
image: logo.svg
languages:
- C++
latest_release: '2022-09-10T19:37:00+00:00'
people:
- Jenny Bryan
title: meltr
website: https://r-lib.github.io/meltr/

external:  # updated automatically, do not edit
  description: Read Non-Rectangular Text Data
  first_commit: '2021-07-07T21:18:25+00:00'
  forks: 2
  languages:
  - C++
  last_updated: '2026-03-05T16:29:57.985629+00:00'
  latest_release: '2022-09-10T19:37:00+00:00'
  license: NOASSERTION
  people:
  - Jenny Bryan
  readme_image: https://nacnudus.github.io/duncangarmonsway/posts/2018-12-29-meltcsv/im_melting_wicked_witch_of_the_west.jpg
  repo: r-lib/meltr
  stars: 32
  title: meltr
  website: https://r-lib.github.io/meltr/
---

The meltr package reads non-rectangular CSV, TSV, and fixed-width files by treating each cell as a separate row in the output. It handles data that breaks assumptions made by standard tools like readr, such as rows with different numbers of columns or mixed data types within columns.

This package solves problems where files are too irregular for standard parsers. It preserves all cells including empty ones, provides row and column coordinates for each cell, and returns all data as strings with type guesses rather than performing automatic conversion. The output is structured data about unstructured input, which you can then filter and manipulate with standard tools like dplyr to extract specific types or patterns from messy files.
