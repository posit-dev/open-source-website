---
title: DeclareDesign
image: page-1.png
resource_type: cheatsheet
by: community
date: '2019-04-01'
description: Declare research designs using the MIDA framework and diagnose their properties via Monte Carlo simulation.
download_url: declaredesign.pdf
people:
- Graeme Blair
- Jasper Cooper
- Alexander Coppock
- Macartan Humphreys
- Neal Fultz
thumbnails:
- page-1.png
languages:
- R
---

DeclareDesign is an R implementation of the MIDA framework, in which a research design has a Model of the world, an Inquiry, a Data strategy, and an Answer strategy. Each component is declared as a composable R function; designs are combined with `+` and diagnosed using Monte Carlo simulation to estimate properties such as power and bias.

## What's covered
- Model – `declare_population()` for simple and hierarchical datasets, `declare_potential_outcomes()`
- Inquiry – `declare_estimand()` for causal, descriptive, and conditional estimands
- Data strategy – `declare_sampling()` and `declare_assignment()` with stratification and clustering
- Answer strategy – `declare_estimator()` for OLS, 2SLS, and difference-in-means
- Design declaration – combining components with `+`
- Design diagnosis – `diagnose_design()`, `summary()`, custom diagnosands
