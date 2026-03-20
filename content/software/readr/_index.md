---
color: '#144279'
description: Read flat files (csv, tsv, fwf) into R
github: tidyverse/readr
image: logo.png
languages:
- R
latest_release: '2026-02-19T07:06:02+00:00'
people:
- Hadley Wickham
- Jenny Bryan
- Christophe Dervieux
- Lionel Henry
- Jeroen Ooms
- Mine Çetinkaya-Rundel
- Davis Vaughan
- Emil Hvitfeldt
tags:
- tidyverse
title: readr
website: https://readr.tidyverse.org

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: Read flat files (csv, tsv, fwf) into R
  first_commit: '2013-07-25T15:28:22+00:00'
  forks: 292
  languages:
  - R
  last_updated: '2026-03-20T10:27:40.619483+00:00'
  latest_release: '2026-02-19T07:06:02+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Jenny Bryan
  - Christophe Dervieux
  - Lionel Henry
  - Jeroen Ooms
  - Mine Çetinkaya-Rundel
  - Davis Vaughan
  - Jeroen Janssens
  - Emil Hvitfeldt
  readme_image: man/figures/logo.png
  repo: tidyverse/readr
  stars: 1027
  title: readr
  website: https://readr.tidyverse.org
---

readr is an R package that provides fast, user-friendly functions for reading rectangular data from delimited files like CSV and TSV. It's designed to parse diverse real-world data formats while providing clear diagnostic messages when parsing encounters unexpected results.

The package automatically guesses column types during exploratory work but encourages explicit type specifications for production code. It's significantly faster than base R (up to 10-100x), handles strings and dates more sensibly by default, and follows tidyverse conventions for consistency across workflows. Since version 2.0.0, it uses the vroom parsing engine for improved performance.
