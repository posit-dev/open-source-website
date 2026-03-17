---
color: '#523C2E'
description: '🐈🐈🐈🐈: tools for working with categorical variables (factors)'
github: tidyverse/forcats
image: logo.png
languages:
- R
latest_release: '2025-09-24T17:08:08+00:00'
people:
- Hadley Wickham
- Jenny Bryan
- Lionel Henry
- Mine Çetinkaya-Rundel
- Jeroen Janssens
tags:
- tidyverse
title: forcats
website: https://forcats.tidyverse.org/

external:  # updated automatically, do not edit
  description: '🐈🐈🐈🐈: tools for working with categorical variables (factors)'
  first_commit: '2016-08-08T18:07:47+00:00'
  forks: 135
  languages:
  - R
  last_updated: '2026-03-05T16:21:01.433333+00:00'
  latest_release: '2025-09-24T17:08:08+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Jenny Bryan
  - Lionel Henry
  - Mine Çetinkaya-Rundel
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidyverse/forcats
  stars: 555
  title: forcats
  website: https://forcats.tidyverse.org/
---

forcats is an R package designed to simplify working with factors, which are R's way of handling categorical variables with fixed sets of possible values. It provides tools for common factor manipulation tasks like reordering levels, changing values, and collapsing infrequent categories.

The package addresses the pain points of factor manipulation in R through functions that reorder factors by frequency (`fct_infreq()`), by another variable (`fct_reorder()`), manually (`fct_relevel()`), or collapse rare levels into an "other" category (`fct_lump()`). These tools are particularly useful for improving data visualization and analysis workflows. forcats is part of the tidyverse collection of packages and integrates seamlessly with other tidyverse tools.
