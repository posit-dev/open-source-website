---
title: caret
image: page-1.png
resource_type: cheatsheet
by: community
date: '2017-09-01'
description: Train and tune machine learning models in R with caret's unified interface, covering preprocessing, resampling, performance metrics, and parallel processing.
download_url: caret.pdf
people:
- Max Kuhn
thumbnails:
- page-1.png
languages:
- R
translations:
- language: French
  lang: fr
  file: caret_fr.pdf
  updated: 2017-09
  people:
  - Ahmadou Dicko
- language: Korean
  lang: ko
  file: caret_ko.pdf
  added: 2017-09
  people:
  - Kwangchun Lee
- language: Portuguese
  lang: pt
  file: caret_pt.pdf
  updated: 2017-09
  people:
  - Karen da Silva Lopes
- language: Spanish
  lang: es
  file: caret_es.pdf
  updated: 2017-09
- language: Turkish
  lang: tr
  file: caret_tr.pdf
  updated: 2017-09
  people:
  - İlkim Ecem Emre
---

The caret (Classification And REgression Training) package provides a consistent interface to over 200 predictive modeling algorithms in R. It wraps the training, tuning, and evaluation steps into a single workflow centered on the `train()` function.

## What's covered
- Specifying the Model – formula, `x`/`y`, and recipe interfaces to `train()`
- Preprocessing – `preProc` options for centering, scaling, imputation, and filtering
- Adding Options – `trainControl()` for resampling and other settings
- Resampling Options – k-fold CV, repeated CV, bootstrap, LGOCV, LOO, time-slice
- Performance Metrics – `summaryFunction` with `defaultSummary`, `twoClassSummary`, `prSummary`
- Grid Search – `tuneGrid` with `expand.grid()` for explicit tuning parameter values
- Random Search – `tuneLength` with `search = "random"` in `trainControl()`
- Subsampling – `sampling` option for class imbalance (down, up, SMOTE, ROSE)
- Parallel Processing – `doMC` (macOS/Linux) and `doParallel` (Windows) via foreach
