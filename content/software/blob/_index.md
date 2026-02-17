---
description: A simple S3 class for representing BLOBs
github: tidyverse/blob
languages:
- R
latest_release: '2026-01-13T06:57:50+00:00'
people:
- Hadley Wickham
- Davis Vaughan
- Jeroen Janssens
title: blob
website: https://blob.tidyverse.org

external:
  description: A simple S3 class for representing BLOBs
  first_commit: '2016-10-27T13:11:54+00:00'
  forks: 14
  languages:
  - R
  last_updated: '2026-02-17T11:28:25.356767+00:00'
  latest_release: '2026-01-13T06:57:50+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Davis Vaughan
  - Jeroen Janssens
  repo: tidyverse/blob
  stars: 49
  title: blob
  website: https://blob.tidyverse.org
---

The blob package provides an S3 class for representing vectors of binary objects (BLOBs) in R. It wraps lists of raw vectors in a lightweight structure that can be included in data frames.

This package is primarily used transparently by other packages that need to handle binary data from databases or binary file formats. It provides a consistent interface for working with BLOB columns, eliminating the need for developers to handle raw binary vectors directly. Most users won't interact with blob explicitly, but it serves as essential infrastructure for database and file format packages in the R ecosystem.
