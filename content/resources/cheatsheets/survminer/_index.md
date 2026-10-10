---
title: survminer
image: page-1.png
resource_type: cheatsheet
by: community
date: '2017-03-01'
description: Create survival analysis plots using ggplot2 with survminer.
download_url: survminer.pdf
people:
- Przemysław Biecek
thumbnails:
- page-1.png
languages:
- R
translations:
- language: Spanish
  lang: es
  file: survminer_es.pdf
  added: 2021-08
  people:
  - Maria Dermit
---

The survminer package provides functions for visualizing survival analysis results, producing
ggplot2 graphics from survfit and coxph objects. It covers Kaplan-Meier
curves, Cox model diagnostics, forest plots, and adjusted survival curves.

## What's covered
- Creating survival plots – `ggsurvplot` for survival probability, cumulative event, and cumulative hazard
- Survival curves – customizing strata, risk tables, and number at risk
- Diagnostics of Cox model – `ggcoxzph` for testing the proportional hazards assumption
- Summary of Cox model – `ggforest` for hazard ratio forest plots
- Adjusted survival curves – `ggadjustedcurves` for Cox model-based group comparisons
