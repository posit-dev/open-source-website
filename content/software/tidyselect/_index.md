---
description: A backend for functions taking tidyverse selections
github: r-lib/tidyselect
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

external:
  contributors:
  - lionel-
  - hadley
  - krlmlr
  - romainfrancois
  - DavisVaughan
  - batpigandme
  - olivroy
  - atusy
  - zkamvar
  - yutannihilation
  - musvaage
  - leondutoit
  - laplasi
  - kevinushey
  - gergness
  - eutwt
  - bvuk
  - terrytangyuan
  - statnmap
  - samuelfielding
  - MichaelChirico
  - matthewjnield
  - karawoo
  - jeroenjanssens
  - hsbadr
  - fmichonneau
  - ddsjoberg
  - dpprdan
  description: A backend for functions taking tidyverse selections
  first_commit: '2017-05-23T18:19:37+00:00'
  forks: 40
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.503987+00:00'
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

tidyselect is the engine that powers column selection in popular tidyverse packages like dplyr and tidyr. It provides a consistent, intuitive syntax for selecting variables from data frames, enabling you to work with columns using flexible patterns like ranges, helper functions, and set operations. Whether you're using `select()` to choose specific columns, `pull()` to extract a single variable, or any of the tidyr verbs that operate on column subsets, tidyselect is working behind the scenes to interpret your selections.

For package developers, tidyselect offers a robust framework for implementing your own selecting functions that feel native to the tidyverse ecosystem. It handles the complexity of parsing selection expressions, resolving column names, and managing edge cases, so you can focus on your package's core functionality. With tidyselect, you can create data manipulation functions that accept the same intuitive selection syntax your users already know and love, ensuring a seamless experience across the R data science ecosystem.
