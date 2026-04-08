---
title: dplyr 0.1.2
description: "dplyr 0.1.2 improves select() with starts_with(), ends_with(), contains(), and named arguments for renaming."
auto-description: true
people:
  - Hadley Wickham
date: '2014-02-25'
categories:
  - Data Wrangling
slug: dplyr-0-1-2
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
  - RStudio
ported_from: rstudio
port_status: in-progress
software: ["dplyr"]
languages: ["R"]
ported_categories:
  - Packages
---


We're pleased to announce a new minor version of dplyr. This fixes a number of bugs that crashed R, and considerably improves the functionality of `select()`. You can now use named arguments to rename existing variables, and use new functions `starts_with()`, `ends_with()`, `contains()`,  `matches()` and `num_range()` to select variables based on their names. Finally, `select()` now makes a shallow copy, substantially reducing its memory impact. I've also added the `summarize()` alias for people from countries who don't spell correctly ;)

For a complete list of changes, please see the [github release](https://github.com/hadley/dplyr/releases/tag/v0.1.2), and as always, you can install the latest version with `install.packages("dplyr").`

