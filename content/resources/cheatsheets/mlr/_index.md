---
title: Machine Learning with mlr
image: page-1.png
resource_type: cheatsheet
by: community
date: '2018-02-01'
description: Build, tune, and evaluate machine learning models in R using the mlr framework's unified interface.
download_url: mlr.pdf
people:
- Aaron Cooley
thumbnails:
- page-1.png
- page-2.png
languages:
- R
---

The mlr package provides a unified interface for supervised and unsupervised machine learning in R, covering task creation, learner configuration, resampling, performance measurement, hyperparameter tuning, and visualization. It supports classification, regression, clustering, survival, and cost-sensitive tasks.

## What's covered
- Setup – `normalizeFeatures()`, `createDummyFeatures()`, `mergeSmallFactorLevels()`
- Task creation – `makeClassifTask()`, `makeRegrTask()`, `makeClusterTask()`, `makeSurvTask()`
- Training & testing – `makeLearner()`, `train()`, `predict()`, `performance()`, `listMeasures()`
- Resampling – `makeResampleDesc()` for CV, LOO, RepCV, bootstrap, and holdout; `resample()`
- Refining performance – `makeParamSet()`, `makeTuneControl*()`, `tuneParams()`
- Configuration – `configureMlr()` for error handling and output verbosity
- Feature extraction – `filterFeatures()` with importance-based selection methods
- Visualization – `plotThreshVsPerf()`, `plotROCCurves()`, `plotResiduals()`
- Wrappers – `makeDummyFeaturesWrapper()`, `makeImputeWrapper()`, `makePreprocWrapper()`
