---
title: dplyr 0.1.1
people:
  - Hadley Wickham
date: '2014-01-30'
categories:
- Packages
slug: dplyr-0-1-1
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
ported_from: rstudio
port_status: in-progress
software: ["dplyr"]
languages: ["R"]
---


We're pleased to announce a new minor version of dplyr. This fixes a few bugs that crashed R, adds a few minor new features (like a `sort` argument to `tally()`), and uses shallow copying in a few more places. There is one backward incompatible change: `explain_tbl()` has been renamed to `explain`. For a complete list of changes, please see the [github release](https://github.com/hadley/dplyr/releases/tag/v0.1.1) notice.

As always, you can install the latest version with `install.packages("dplyr").`

