---
title: imputeTS
image: page-1.png
resource_type: cheatsheet
by: community
date: '2020-08-01'
description: Impute missing values in univariate numeric time series using interpolation, Kalman smoothing, moving averages, and seasonal methods.
download_url: imputeTS.pdf
thumbnails:
- page-1.png
languages:
- R
source_files:
- file: imputeTS.pptx
  format: PowerPoint
---

imputeTS specializes in missing value imputation for univariate, equally-spaced numeric time series, with a focus on sensor and IoT data. It offers multiple imputation algorithms, ggplot2-based diagnostic plots for understanding and evaluating missing data patterns, and works naturally in tidy pipe workflows.

## What's covered
- Mission, features, and scope – univariate numeric equally-spaced time series
- Imputation algorithms – `na_interpolation()`, `na_kalman()`, `na_locf()`, `na_ma()`, `na_mean()`, `na_random()`, `na_seadec()`, `na_seasplit()`, `na_replace()`, `na_remove()`
- Missing data overview plots – `ggplot_na_distribution()`, `ggplot_na_intervals()`, `ggplot_na_gapsize()`
- Imputation analysis plots – `ggplot_na_imputations()` for evaluating imputation quality
- Workflows – pipe-based usage with forecast packages
- Datasets – `tsAirgap`, `tsNH4`, `tsHeating`
