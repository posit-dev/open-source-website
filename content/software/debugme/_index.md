---
description: Easy and efficient debugging for R packages
github: r-lib/debugme
languages:
- R
latest_release: '2024-04-25T07:24:47+00:00'
people:
- Gábor Csárdi
- Jeroen Janssens
title: debugme
website: https://r-lib.github.io/debugme/

external:  # updated automatically, do not edit
  description: Easy and efficient debugging for R packages
  first_commit: '2016-09-25T14:36:52+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-02-24T09:26:34.827793+00:00'
  latest_release: '2024-04-25T07:24:47+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Janssens
  repo: r-lib/debugme
  stars: 153
  title: debugme
  website: https://r-lib.github.io/debugme/
---

debugme is a lightweight debugging tool for R packages that uses special string literals to add debug messages without function call overhead. You mark debug statements with "!DEBUG" prefixes in your code, then control which packages show debug output by setting the DEBUGME environment variable.

The package has essentially zero performance impact when debugging is disabled because debug strings are just ignored string literals. It supports multiple packages simultaneously with color-coded output for each package, allows embedded R code evaluation within debug messages using backticks, and requires minimal setup - just one .onLoad function in your package. This makes it practical to leave debug statements in production code without worrying about performance penalties.
