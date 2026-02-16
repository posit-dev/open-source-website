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

external:
  contributors:
  - gaborcsardi
  - krlmlr
  - jeroenjanssens
  - jonthegeek
  - kforner
  - MHenderson
  description: Easy and efficient debugging for R packages
  first_commit: '2016-09-25T14:36:52+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.137974+00:00'
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

debugme is a lightweight debugging solution for R packages that makes troubleshooting your code effortless. Instead of cluttering your package with conditional print statements or complex logging frameworks, debugme lets you embed debug messages as special string constants that can be turned on or off through environment variables. This means you can ship debugging capabilities with your package and activate them only when needed, without modifying a single line of code.

The package shines with its elegant simplicity and zero performance overhead. Debug messages are written as string literals prefixed with `!DEBUG`, and you can even include R code within backticks to inspect variables at runtime. When debugging is disabled, these strings have practically no performance impact on your code. Whether you're developing a data analysis pipeline, building an R package, or troubleshooting production issues, debugme gives you powerful debugging capabilities without the usual complexity or performance trade-offs.
