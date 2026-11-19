---
title: nimble
image: page-1.png
resource_type: cheatsheet
by: community
date: '2020-05-01'
description: Write, compile, and run Bayesian hierarchical models and customizable MCMC algorithms using NIMBLE in R.
download_url: nimble.pdf
thumbnails:
- page-1.png
- page-2.png
languages:
- R
---

NIMBLE provides a system for writing hierarchical Bayesian models in BUGS-like syntax (`nimbleCode()`), compiling them to C++ for fast execution, and running customizable MCMC samplers with `buildMCMC()` and `runMCMC()`. Models are treated as objects that expose nodes, variables, and dependency graphs for inspection and debugging.

## What's covered
- NIMBLE workflow – `nimbleCode()`, `nimbleModel()`, `configureMCMC()`, `buildMCMC()`, `compileNimble()`, `runMCMC()`
- Writing model code – stochastic (`~`), deterministic (`<-`), truncated, and constraint declarations; link functions; vectorized nodes
- Using models – `model$calculate()`, `model$simulate()`, `model$getLogProb()`, variable access
- Models are graphs – `getNodeNames()`, `getVarNames()`, `getDependencies()`, `expandNodeNames()`
- Debugging models – `myModel$check()`, `initializeInfo()`, `checkBasics()`, `newModel()`
- Distributions – univariate continuous distributions with canonical and alternative parameterizations (beta, chi-square, log-normal, logistic, inverse-gamma, and more)
