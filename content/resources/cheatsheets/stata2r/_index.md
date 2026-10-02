---
title: Stata to R
image: page-1.png
resource_type: cheatsheet
by: community
date: '2019-10-01'
description: Translate common Stata econometrics commands to their base R equivalents.
download_url: stata2r.pdf
people:
- Anthony Nguyen
thumbnails:
- page-1.png
- page-2.png
languages:
- R
source_files:
- file: stata2r.pptx
  format: PowerPoint
---

Stata to R maps Stata commands for econometric workflows to R equivalents, using datasets from
Wooldridge's Introductory Econometrics. It covers data exploration, variable manipulation,
model estimation, and postestimation, with notes on key differences between the two environments.

## What's covered
- Setup – installing the `wooldridge` package and loading datasets
- Basic plots – histogram, scatter plot, fitted line, and boxplot
- Summarize data – `browse`, `describe`, `summarize`, `tabulate` equivalents
- Create and edit variables – generating, dropping, keeping, recoding, and creating dummies
- Estimate models: OLS – `lm`, robust and clustered standard errors via `estimatr`
- Estimate models: MLE – logit, probit, and tobit regression
- Estimate models: panel/longitudinal – fixed effects with `plm`
- Estimate models: instrumental variables (2SLS) – `ivreg` from the AER package
- Postestimation – `predict`, residuals, and diagnostic tests
