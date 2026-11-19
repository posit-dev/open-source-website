---
title: estimatr
image: page-1.png
resource_type: cheatsheet
by: community
date: '2018-11-01'
description: Fit OLS, 2SLS, and two-group estimators with design-appropriate robust and clustered standard errors.
download_url: estimatr.pdf
people:
- Graeme Blair
- Jasper Cooper
- Alexander Coppock
- Macartan Humphreys
- Luke Sonnet
thumbnails:
- page-1.png
languages:
- R
---

estimatr is part of the DeclareDesign suite and provides fast linear and instrumental variables estimators with robust standard errors designed for experimental and observational research. It covers OLS with `lm_robust()`, two-stage least squares with `iv_robust()`, fixed-effects regression, and two-group estimators, with ggplot2 and texreg integrations.

## What's covered
- OLS with `lm_robust()` – HC2 default, SE type options
- Clustered standard errors – CR2 default
- Fixed effects – dummies approach and `fixed_effects` absorbing approach
- 2SLS with `iv_robust()` – clustered IV regression
- Two-group estimators – `difference_in_means()`, `horvitz_thompson()`
- Post-estimation commands – `tidy()`, `vcov()`, `confint()`, `predict()`
- ggplot2 integration – `stat_smooth(method = "lm_robust")`
- Multiple models – same outcome different subsets, different outcomes same subset
- Extras – Lin covariate adjustment (`lm_lin()`), texreg tables
- estimatr-to-Stata dictionary
