---
color: '#404041'
description: A backend for functions taking tidyverse selections
github: r-lib/tidyselect
image: logo.svg
languages:
- R
latest_release: '2024-03-11T11:44:46+00:00'
people:
- Lionel Henry
- Hadley Wickham
- Davis Vaughan
- Jeroen Janssens
title: tidyselect
website: https://tidyselect.r-lib.org

external:  # updated automatically, do not edit
  description: A backend for functions taking tidyverse selections
  first_commit: '2017-05-23T18:19:37+00:00'
  forks: 40
  languages:
  - R
  last_updated: '2026-03-20T10:27:53.828855+00:00'
  latest_release: '2024-03-11T11:44:46+00:00'
  license: NOASSERTION
  people:
  - Lionel Henry
  - Hadley Wickham
  - Davis Vaughan
  - Jeroen Janssens
  repo: r-lib/tidyselect
  stars: 128
  title: tidyselect
  website: https://tidyselect.r-lib.org
---

tidyselect is a backend package that provides the column selection infrastructure used by dplyr, tidyr, and other tidyverse packages. It enables functions like `dplyr::select()` and `dplyr::pull()` to interpret flexible column selection expressions.

The package implements a consistent selection syntax across the tidyverse ecosystem, allowing users to select columns using bare names, ranges, helpers like `starts_with()`, and boolean operations. It's designed primarily for package developers who want to add tidyverse-style column selection to their own functions. The package handles the complex parsing and evaluation of selection expressions so that downstream packages don't need to implement this logic themselves.
