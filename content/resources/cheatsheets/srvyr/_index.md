---
title: survey data analysis with srvyr
image: page-1.png
resource_type: cheatsheet
by: community
date: '2025-01-01'
description: Analyze complex survey data with dplyr-style syntax using srvyr.
download_url: srvyr.pdf
people:
- Greg Freedman Ellis
- Ben Schneider
thumbnails:
- page-1.png
- page-2.png
languages:
- R
---

srvyr wraps the survey package to bring dplyr-compatible syntax to weighted survey analysis.
It handles stratified, clustered, and multistage sample designs and returns weighted estimates
along with standard errors and confidence intervals.

## What's covered
- Describing the survey design – `as_survey_design` with ids, strata, fpc, and weights arguments
- Replicate weights – `as_survey_rep`, replication types, and scale factors
- Dealing with lonely PSUs – `survey.lonely.psu` option settings
- Database-backed surveys – using `tbl()` with `as_survey_design`
- Manipulating data – `filter` and `mutate` on design objects
- Summarizing functions – `summarize`, `survey_count`, `group_by`
- Statistical summary functions – `survey_total`, `survey_mean`, `survey_prop`
- Standard errors and confidence intervals – `vartype` argument (se, ci, var, cv)
- Proportions and percentages
