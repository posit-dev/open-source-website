---
image: logo.svg
color: "#404041"
description: R implementation of Temporal Fusion Transformers
github: mlverse/tft
languages:
- R
people:
- Daniel Falbel
title: tft
website: https://mlverse.github.io/tft/

external:  # updated automatically, do not edit
  description: R implementation of Temporal Fusion Transformers
  first_commit: '2021-01-09T14:36:32+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-09-18T14:18:30.641901+00:00'
  license: NOASSERTION
  people:
  - Daniel Falbel
  repo: mlverse/tft
  stars: 33
  title: tft
  website: https://mlverse.github.io/tft/
---

`tft` is an R implementation of the Temporal Fusion Transformer, a neural network architecture for multi-horizon time series forecasting. It allows you to forecast multiple time series simultaneously within a single model.

The key advantage of TFT over conventional forecasting methods is how it handles different types of input data. The architecture encodes static covariates and time-varying inputs (both known and unknown) through separate pathways, rather than treating all features uniformly. It is built on torch for R and has shown strong benchmark results on standard forecasting tasks.
