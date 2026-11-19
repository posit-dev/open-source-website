---
title: SamplingStrata
image: page-1.png
resource_type: cheatsheet
by: community
date: '2020-01-01'
description: Optimize the stratification of a sampling frame to minimize sample size given precision constraints on target estimates.
download_url: SamplingStrata.pdf
people:
- Giulio Barcaroli
thumbnails:
- page-1.png
- page-2.png
languages:
- R
---

The SamplingStrata package determines optimal stratification for survey sampling using an evolutionary algorithm. It supports three methods depending on the stratification variable type: atomic (categorical), continuous (with k-means pre-clustering), and spatial (for geo-referenced frames with spatial correlation). The workflow covers precision constraint definition, optimization, evaluation, and sample selection.

## What's covered
- Optimal stratification – when to use atomic, continuous, or spatial methods
- Method "atomic" – `buildStrataDF()`, `optimStrata(method = "atomic")`, `evalSolution()`, `selectSample()`
- Method "continuous" – `KmeansSolution2()` for strata count suggestion, `prepareSuggestion()`, `optimStrata(method = "continuous")`
- Method "spatial" – variogram fitting, `buildFrameSpatial()`, `optimStrata(method = "spatial")`
- Precision constraints – `buildFrameDF()`, `cv` data frame with domain-level CV targets
- Evaluation – `evalSolution()` and coefficient of variation per domain
- Visualization – `plotStrata2d()` for strata by pairs of stratification variables
- Use of models – `computeGamma()` for linking target variables to covariates via linear or log-linear models
