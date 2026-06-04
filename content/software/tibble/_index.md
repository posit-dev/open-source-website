---
color: '#21202F'
description: A modern re-imagining of the data frame
github: tidyverse/tibble
image: logo.png
languages:
- R
latest_release: '2026-01-10T18:28:34+00:00'
people:
- Hadley Wickham
- Jenny Bryan
- Lionel Henry
- Davis Vaughan
- Tomasz Kalinowski
- Max Kuhn
- Christophe Dervieux
tags:
- tidyverse
title: tibble
topics:
- Data Wrangling
website: https://tibble.tidyverse.org/

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: A modern re-imagining of the data frame
  first_commit: '2015-10-28T23:57:00+00:00'
  forks: 134
  languages:
  - R
  last_updated: '2026-05-20T08:05:44.177922+00:00'
  latest_release: '2026-01-10T18:28:34+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Jenny Bryan
  - Lionel Henry
  - Davis Vaughan
  - Tomasz Kalinowski
  - Max Kuhn
  - Jeroen Janssens
  - Christophe Dervieux
  readme_image: man/figures/logo.png
  repo: tidyverse/tibble
  stars: 744
  title: tibble
  website: https://tibble.tidyverse.org/
---

The tibble package provides a modern replacement for R's data.frame that follows stricter, more predictable behavior. Tibbles are designed to be "lazy and surly" - they don't automatically change variable names or types, don't do partial matching, and warn you more explicitly about problems.

This stricter behavior helps catch errors earlier in your data analysis workflow. Tibbles also include an enhanced print method that handles large datasets and complex objects better than standard data frames, making it easier to inspect your data in the console. The package offers functions for creating tibbles from existing data structures (`as_tibble()`), from column vectors (`tibble()`), and row-by-row (`tribble()`).

## Try it

{{< webr packages="tibble" >}}
library(tibble)

# Create a tibble with tibble()
t <- tibble(
  name  = c("Alice", "Bob", "Carol"),
  score = c(91.5, 87.0, 95.2),
  grade = c("A", "B", "A")
)
t

# Row-by-row construction with tribble()
tribble(
  ~city,       ~pop_m,
  "New York",  8.3,
  "London",    9.0,
  "Tokyo",    13.9
)
{{< /webr >}}
