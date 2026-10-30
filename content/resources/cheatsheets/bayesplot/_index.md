---
title: bayesplot
image: page-1.png
resource_type: cheatsheet
by: community
date: '2020-06-01'
description: Visualize posterior distributions, MCMC diagnostics, and posterior predictive checks for Bayesian models.
download_url: bayesplot.pdf
people:
- Edward A. Roualdes
thumbnails:
- page-1.png
languages:
- R
---

bayesplot provides ggplot2-based plotting functions for assessing Bayesian models fit with Stan or other samplers. It is designed to work directly with posterior draw arrays and integrates with rstanarm and other Stan-based packages.

## What's covered
- Model parameters – `mcmc_areas()` for posterior distribution plots with credible intervals
- MCMC traceplots – `mcmc_trace()` for convergence diagnosis
- Pairs plots – `mcmc_pairs()` for detecting correlated parameters
- Posterior predictive checks – `ppc_intervals()`, `ppc_stat_grouped()` using `posterior_predict()`
- NUTS diagnostics – `mcmc_nuts_energy()` for energy diagnostic plots
