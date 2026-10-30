---
title: Prediction Performance with metrica
image: page-1.png
resource_type: cheatsheet
by: community
date: '2023-01-01'
description: Evaluate prediction accuracy of regression and classification models using more than 80 performance metrics.
download_url: metrica.pdf
people:
- Carlos Hernandez
- Adrian A. Correndo
thumbnails:
- page-1.png
languages:
- R
translations:
- language: Portuguese (Brazil)
  lang: pt-BR
  file: metrica_pt_br.pdf
  updated: 2023-01
- language: Russian
  lang: ru
  file: metrica_ru.pdf
  updated: 2023-01
  people:
  - Denis Gazetdinov
- language: Spanish
  lang: es
  file: metrica_es.pdf
  updated: 2023-01
---

The metrica package compiles over 80 functions for quantifying and visualizing prediction performance of point-forecast models for both continuous (regression) and categorical (classification) targets. Individual metrics such as `R2()`, `RMSE()`, and `accuracy()` share a common `obs`/`pred` interface, and `metrics_summary()` computes a selected list at once.

## What's covered
- Basics – `obs` and `pred` arguments, `data` and `tidy` options shared by all functions
- Installation – CRAN and GitHub development versions
- Native datasets – built-in regression (wheat, barley, sorghum, chickpea) and classification (land_cover, maize_phenology) examples
- Regression metrics – `R2()`, `RMSE()`, `KGE()`, and `metrics_summary()` for regression
- Classification metrics – `accuracy()`, `precision()`, `recall()`, `fscore()`, and `metrics_summary()` for classification
- Plots – `scatter_plot()` and `bland_altman_plot()`
- Confusion matrix – `confusion_matrix()` for binary and multinomial cases
