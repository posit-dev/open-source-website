---
description: Variable assignment with zeal! (or multiple, unpacking, and destructuring
  assignment in R)
github: r-lib/zeallot
languages:
- R
latest_release: '2025-06-03T01:23:45+00:00'
title: zeallot
website: ''

external:
  contributors:
  - nteetor
  - pteetor
  description: Variable assignment with zeal! (or multiple, unpacking, and destructuring
    assignment in R)
  first_commit: '2017-01-03T22:33:47+00:00'
  forks: 13
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.270889+00:00'
  latest_release: '2025-06-03T01:23:45+00:00'
  license: NOASSERTION
  repo: r-lib/zeallot
  stars: 272
  title: zeallot
  website: ''
---

Working with functions that return multiple values in R often means dealing with unwieldy lists and extracting elements one at a time. zeallot brings the power of multiple assignment to R through its `%<-%` operator, allowing you to unpack lists, destructure data frames, and assign multiple values in a single, elegant expression. Whether you're working with functions that return complex nested structures or simply want to write more concise and readable code, zeallot lets you assign multiple values to explicit variable names in one go.

The package shines when working with modern R patterns like purrr's safe functions, where you can unpack both the result and error in one line (`c(res, err) %<-% safe_log(10)`), or when you need to extract specific columns from a data frame (`c(cyl=, wt=) %<-% mtcars`). zeallot also supports nested unpacking for complex list structures and collector variables for capturing remaining elements, making it a versatile tool for data scientists who want to write self-documenting code without sacrificing clarity or brevity.
