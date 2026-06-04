---
color: '#27341B'
description: A functional programming toolkit for R
github: tidyverse/purrr
image: logo.png
languages:
- R
latest_release: '2026-04-12T06:46:38+00:00'
people:
- Hadley Wickham
- Lionel Henry
- Charlie Gao
- Davis Vaughan
- Jenny Bryan
- Christophe Dervieux
- Gábor Csárdi
- Tomasz Kalinowski
- Neal Richardson
- Mine Çetinkaya-Rundel
tags:
- tidyverse
title: purrr
topics:
- Data Wrangling
website: https://purrr.tidyverse.org/

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: A functional programming toolkit for R
  first_commit: '2014-11-29T17:33:40+00:00'
  forks: 293
  languages:
  - R
  last_updated: '2026-05-20T08:05:44.093748+00:00'
  latest_release: '2026-04-12T06:46:38+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  - Charlie Gao
  - Davis Vaughan
  - Jenny Bryan
  - Christophe Dervieux
  - Gábor Csárdi
  - Tomasz Kalinowski
  - Neal Richardson
  - Mine Çetinkaya-Rundel
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidyverse/purrr
  stars: 1391
  title: purrr
  website: https://purrr.tidyverse.org/
---

purrr provides a complete and consistent toolkit for functional programming in R, focused primarily on the `map()` family of functions that allow you to apply operations across vectors and lists. It enables you to replace for loops with more concise and readable code.

The package offers several advantages over base R: it works naturally with the pipe operator, guarantees type-stable outputs (each function returns a predictable type or throws an error), and supports flexible function specifications using named functions, anonymous functions, lambda syntax, or shortcuts for extracting elements by name or position. It also includes built-in progress tracking for long-running operations and parallel computation support.

## Try it

{{< webr packages="purrr" >}}
library(purrr)

measurements <- list(a = c(3, 1, 4, 1, 5), b = c(2, 7, 1, 8), c = c(9, 2, 6))

map_dbl(measurements, mean)
{{< /webr >}}
