---
title: admiral
image: page-1.png
resource_type: cheatsheet
by: community
date: '2024-07-01'
description: Build CDISC ADaM datasets in R using modular, composable derivation functions from the pharmaverse.
download_url: admiral.pdf
people:
- Stefan Bundfuss
thumbnails:
- page-1.png
- page-2.png
languages:
- R
---

admiral is an open-source, modularized R toolbox for developing CDISC ADaM analysis datasets. It is built around interchangeable function blocks—individual `derive_*` calls—that are chained together to sequentially add variables and parameters to a dataset. It is part of the pharmaverse ecosystem of clinical reporting packages.

## What's covered
- What you need to know – introduction to the ADaM workflow
- Generic variable-adding functions – `derive_vars_merged()`, `derive_vars_joined()`, and related
- Generic parameter-adding functions – `derive_param_computed()`, `derive_extreme_records()`
- Functions treating days/dates/datetimes – `derive_vars_dt()`, `derive_vars_dy()`, `derive_vars_duration()`
- Special variable-adding functions – age, period, toxicity grade, baseline/change
- Special parameter-adding functions
- Higher order functions – `call_derivation()`, `restrict_derivation()`
- Computation functions for vectors – `compute_age_years()`, `compute_duration()`
- Templates – `list_all_templates()`, `use_ad_template()`
- Utilities – `convert_blanks_to_na()`, `filter_exist()`
