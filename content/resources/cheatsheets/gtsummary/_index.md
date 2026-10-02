---
title: gtsummary
image: page-1.png
resource_type: cheatsheet
by: community
date: '2022-04-01'
description: Produce descriptive, regression, and survival summary tables from R data frames and model objects.
download_url: gtsummary.pdf
people:
- Esther Drill
thumbnails:
- page-1.png
- page-2.png
languages:
- R
source_files:
- file: gtsummary.pptx
  format: PowerPoint
translations:
- language: Vietnamese
  lang: vi
  file: gtsummary_vi.pdf
  updated: 2022-04
  people:
  - Le-Huynh Truc-Ly
  source: gtsummary_vi.pptx
---

gtsummary turns R data frames and model objects into formatted, customizable tables suitable for publication. A consistent set of add-on functions applies across all table types for adding p-values, overall columns, and formatting.

## What's covered
- `tbl_summary()` – descriptive statistics for continuous, categorical, and dichotomous variables
- `tbl_svysummary()` – survey-weighted descriptive tables
- Customization arguments – `by`, `label`, `statistic`, `digits`, `type`, `value`, `missing`
- `add_p()` – p-value column with configurable statistical tests
- `add_n()`, `add_overall()`, `add_q()` – additional columns
- `bold_p()`, `bold_labels()` – formatting helpers
- `tbl_regression()` – formatted regression model output with exponentiation option
- `tbl_survfit()` – time-to-event estimates from survfit objects
