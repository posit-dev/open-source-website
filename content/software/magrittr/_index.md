---
color: '#423928'
description: Improve the readability of R code with the pipe
github: tidyverse/magrittr
image: logo.png
languages:
- R
latest_release: '2025-09-11T16:42:35+00:00'
people:
- Lionel Henry
- Hadley Wickham
- Jeroen Janssens
- Gábor Csárdi
- Davis Vaughan
tags:
- tidyverse
title: magrittr
website: https://magrittr.tidyverse.org

external:  # updated automatically, do not edit
  description: Improve the readability of R code with the pipe
  first_commit: '2014-01-01T13:30:01+00:00'
  forks: 161
  languages:
  - R
  last_updated: '2026-03-05T16:20:23.549386+00:00'
  latest_release: '2025-09-11T16:42:35+00:00'
  license: NOASSERTION
  people:
  - Lionel Henry
  - Hadley Wickham
  - Jeroen Janssens
  - Gábor Csárdi
  - Davis Vaughan
  readme_image: man/figures/logo.png
  repo: tidyverse/magrittr
  stars: 967
  title: magrittr
  website: https://magrittr.tidyverse.org
---

The magrittr package provides pipe operators for R that allow you to chain function calls together in a left-to-right sequence, making code more readable by replacing nested function calls like `h(g(f(x)))` with `x %>% f %>% g %>% h`.

The package eliminates the need for temporary variables and nested parentheses when working with multiple sequential operations. It includes the main pipe operator `%>%`, a placeholder `.` for controlling where piped values are passed to functions, the ability to create reusable pipeline functions, and the `%$%` operator for exposing data frame variables to functions that don't have a data argument. These features make it straightforward to add, remove, or reorder steps in data processing workflows.
