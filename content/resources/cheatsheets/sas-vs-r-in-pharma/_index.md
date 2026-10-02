---
title: SAS vs. R in Pharma
image: page-1.png
resource_type: cheatsheet
by: community
date: '2022-11-01'
description: Compare SAS and R data manipulation techniques commonly used in the pharmaceutical industry.
download_url: SASvsRinPharma.pdf
people:
- Bharath Kumar
thumbnails:
- page-1.png
- page-2.png
languages:
- R
---

This cheat sheet shows side-by-side SAS and R code for pharmaceutical data workflows, using
clinical trial demo datasets (DM, VS, EX). It covers reading data, filtering, variable
creation, deduplication, transposing, appending, and merging datasets.

## What's covered
- Data inputs – creating datasets in SAS and data frames in R
- Variable sorting – `arrange` vs. `proc sort`
- Data filtering – `filter` vs. `if` statements
- Data operations – keep, drop, and rename variables
- Variable creation – `mutate` with derived variables and BMI calculation
- Remove duplicate records – `slice(1)` vs. `nodupkey`
- Data transformation: long to wide – `pivot_wider` vs. `proc transpose`
- Data transformation: wide to long – `pivot_longer` vs. `proc transpose`
- Data appending – `bind_rows` vs. `set`
- Data merging – inner join and full join via `proc sql` and `dplyr`
