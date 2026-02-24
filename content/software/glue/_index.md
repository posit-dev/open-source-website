---
description: Glue strings to data in R. Small, fast, dependency free interpreted string
  literals.
github: tidyverse/glue
image: logo.png
languages:
- R
latest_release: '2024-09-27T15:59:19+00:00'
people:
- Jenny Bryan
- Hadley Wickham
- Gábor Csárdi
- Lionel Henry
- Davis Vaughan
- Mine Çetinkaya-Rundel
- Jeroen Janssens
title: glue
website: https://glue.tidyverse.org

external:  # updated automatically, do not edit
  description: Glue strings to data in R. Small, fast, dependency free interpreted
    string literals.
  first_commit: '2016-12-23T21:07:25+00:00'
  forks: 64
  languages:
  - R
  last_updated: '2026-02-24T09:26:23.581401+00:00'
  latest_release: '2024-09-27T15:59:19+00:00'
  license: NOASSERTION
  people:
  - Jenny Bryan
  - Hadley Wickham
  - Gábor Csárdi
  - Lionel Henry
  - Davis Vaughan
  - Mine Çetinkaya-Rundel
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidyverse/glue
  stars: 743
  title: glue
  website: https://glue.tidyverse.org
---

The glue package provides interpreted string literals for R by embedding R expressions inside curly braces, which are then evaluated and inserted into strings. It offers a small, fast, and dependency-free approach to string interpolation.

The package makes string formatting more readable and predictable compared to base R functions like paste() and sprintf(). It handles whitespace intelligently by automatically trimming common leading indentation, making code formatting align with output formatting. glue works with data from multiple sources including the local environment, named arguments, and data frames, and includes specialized variants like glue_sql() for database queries.
