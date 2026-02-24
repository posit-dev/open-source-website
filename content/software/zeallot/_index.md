---
description: Variable assignment with zeal! (or multiple, unpacking, and destructuring
  assignment in R)
github: r-lib/zeallot
languages:
- R
latest_release: '2025-06-03T01:23:45+00:00'
title: zeallot
website: ''

external:  # updated automatically, do not edit
  description: Variable assignment with zeal! (or multiple, unpacking, and destructuring
    assignment in R)
  first_commit: '2017-01-03T22:33:47+00:00'
  forks: 13
  languages:
  - R
  last_updated: '2026-02-24T09:26:34.990035+00:00'
  latest_release: '2025-06-03T01:23:45+00:00'
  license: NOASSERTION
  repo: r-lib/zeallot
  stars: 272
  title: zeallot
  website: ''
---

zeallot provides destructuring assignment in R through the `%<-%` operator, allowing you to unpack lists, vectors, and other objects into multiple named variables in a single operation. This eliminates the need to manually extract values from list elements or function return values that contain multiple components.

The package is particularly useful when working with functions that return lists of multiple values, such as `purrr::safely()`, where you can immediately assign the result and error components to separate variables rather than dealing with nested list indexing. It supports nested unpacking for complex data structures, partial unpacking with collector syntax (`..rest`), and direct column extraction from data frames. The syntax makes code more concise and self-documenting by giving explicit names to each component at the point of assignment.
