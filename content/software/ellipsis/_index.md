---
description: Tools for Working with ...
github: r-lib/ellipsis
languages:
- R
latest_release: '2021-04-29T12:05:34+00:00'
people:
- Hadley Wickham
- Lionel Henry
title: ellipsis
website: https://ellipsis.r-lib.org

external:
  contributors:
  - hadley
  - lionel-
  - yutannihilation
  - batpigandme
  - noamross
  - jimhester
  - krlmlr
  - dkahle
  - jyuu
  description: Tools for Working with ...
  first_commit: '2018-07-06T20:49:16+00:00'
  forks: 14
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.813509+00:00'
  latest_release: '2021-04-29T12:05:34+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  repo: r-lib/ellipsis
  stars: 140
  title: ellipsis
  website: https://ellipsis.r-lib.org
---

ellipsis is an essential R package that makes functions using the `...` parameter safer and more reliable. The `...` construct in R is powerful for passing arguments through to other functions, but it comes with a critical drawback: misspelled or extraneous arguments are silently ignored, leading to subtle bugs that are hard to detect. For example, calling `mean(1, 2, 3, 4)` returns 1 instead of the expected result because the extra arguments disappear without warning. ellipsis solves this problem by providing validation functions that transform these silent failures into explicit errors, helping developers catch mistakes early.

The package offers three key validation functions tailored to different use cases. `check_dots_used()` ensures all arguments passed through `...` are actually evaluated, preventing arguments from being accidentally swallowed. `check_dots_unnamed()` enforces that components are unnamed, making it easier to catch misspelled named arguments. `check_dots_empty()` takes the strictest approach by erroring if `...` is used at all, forcing users to specify full argument names explicitly. Whether you're building R packages or writing robust data analysis functions, ellipsis helps you create more predictable code and deliver better user experiences by catching common mistakes before they become production issues.
