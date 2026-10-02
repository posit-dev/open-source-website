---
title: SAS <-> R
image: page-1.png
resource_type: cheatsheet
by: community
date: '2022-10-01'
description: Map common SAS data manipulation and plotting procedures to their tidyverse equivalents in R.
download_url: sas-r.pdf
people:
- Brendan O'Dowd
thumbnails:
- page-1.png
- page-2.png
software:
- tidyverse
languages:
- R
---

The SAS <-> R cheat sheet shows side-by-side equivalents for common SAS data steps and procedures
and their R counterparts using the tidyverse. It covers the full data manipulation workflow from
importing and subsetting data to summarising, joining, pivoting, and plotting.

## What's covered
- Introduction and setup – installing and loading tidyverse
- Datasets; drop, keep, and rename variables
- Conditional filtering
- Sorting and row-wise operations
- New variables and conditional editing – `mutate`, `if_else`, `case_when`
- Counting and summarising – `count`, `group_by`, `summarise`
- Combining datasets – `bind_rows`, `left_join`, and related joins
- String manipulation – `str_detect`, `str_sub`, `str_replace_all`, `str_extract`
- Transpose/pivot – `pivot_wider`, `pivot_longer`
- Plotting in R – ggplot2 line, point, bar, and column charts
