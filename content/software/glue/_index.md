---
color: '#EB4C0B'
description: Glue strings to data in R. Small, fast, dependency free interpreted string
  literals.
github: tidyverse/glue
image: logo.png
languages:
- R
latest_release: '2026-04-16T22:52:32+00:00'
people:
- Jenny Bryan
- Hadley Wickham
- Gábor Csárdi
- Lionel Henry
- Davis Vaughan
- Mine Çetinkaya-Rundel
title: glue
topics:
- Best Practices
- Data Wrangling
website: https://glue.tidyverse.org

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: Glue strings to data in R. Small, fast, dependency free interpreted
    string literals.
  first_commit: '2016-12-23T21:07:25+00:00'
  forks: 63
  languages:
  - R
  last_updated: '2026-05-20T08:05:44.366172+00:00'
  latest_release: '2026-04-16T22:52:32+00:00'
  license: NOASSERTION
  people:
  - Jenny Bryan
  - Hadley Wickham
  - Gábor Csárdi
  - Lionel Henry
  - Davis Vaughan
  - Jeroen Janssens
  - Mine Çetinkaya-Rundel
  readme_image: man/figures/logo.png
  repo: tidyverse/glue
  stars: 747
  title: glue
  website: https://glue.tidyverse.org
---

The glue package provides interpreted string literals for R by embedding R expressions inside curly braces, which are then evaluated and inserted into strings. It offers a small, fast, and dependency-free approach to string interpolation.

The package makes string formatting more readable and predictable compared to base R functions like paste() and sprintf(). It handles whitespace intelligently by automatically trimming common leading indentation, making code formatting align with output formatting. glue works with data from multiple sources including the local environment, named arguments, and data frames, and includes specialized variants like glue_sql() for database queries.
