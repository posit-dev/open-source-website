---
description: Read Non-Rectangular Text Data
github: r-lib/meltr
languages:
- C++
latest_release: '2022-09-10T19:37:00+00:00'
people:
- Jenny Bryan
title: meltr
website: https://r-lib.github.io/meltr/

external:
  contributors:
  - nacnudus
  - jimhester
  - jennybc
  - IndrajeetPatil
  description: Read Non-Rectangular Text Data
  first_commit: '2021-07-07T21:18:25+00:00'
  forks: 2
  languages:
  - C++
  last_updated: '2026-02-13T14:17:20.569746+00:00'
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

Real-world data is messy, and not every file fits neatly into a rectangular table. meltr is an R package designed for reading unstructured or "non-rectangular" data files that violate the assumptions of standard CSV readers. Instead of forcing irregular data into columns with consistent types, meltr reads files cell-by-cell and returns structured metadata about each cell's position, data type, and raw value. This approach is particularly valuable when working with files that have varying column counts per row, mixed data types, embedded newlines, or formatting so irregular that conventional tools simply fail.

By preserving the original data as strings while annotating each cell with its inferred type and location, meltr gives you the flexibility to extract, filter, and transform messy data using familiar tools like dplyr. Whether you're identifying missing values scattered throughout a file, extracting specific data types from chaotic spreadsheets, or preparing irregular data for manual review, meltr provides a solid foundation for tackling data challenges that would otherwise require extensive manual preprocessing.