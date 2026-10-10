---
title: Create, query and manipulate distributions with distr6
image: page-1.png
resource_type: cheatsheet
by: community
date: '2019-08-01'
description: Work with probability distributions as R6 objects, with flexible parameterizations, properties, decorators, and composite wrappers.
download_url: distr6.pdf
people:
- Raphael Sonabend
thumbnails:
- page-1.png
- page-2.png
languages:
- R
---

distr6 provides a unified object-oriented interface for probability distributions using R6 classes. It implements a wide range of distributions and kernels, supports multiple parameterizations for each, and allows distributions to be extended via decorators for numerical imputation or combined into composites via wrappers. Every R6 method also has an S3 dispatch available.

## What's covered
- Introduction and R6 class hierarchy – Distribution, SDistribution, Kernel, Decorator, Wrapper, ParameterSet
- R6 basics – dollar-sign method notation
- Construct a distribution – default and alternative parameterizations
- Get and set parameters – `$parameters()`, `$getParameterValue()`, `$setParameterValue()`
- Properties and traits – `$support()`, `$symmetry()`, `$kurtosis()`, `$skewness()`
- S3 and piping – S3 equivalents and magrittr `%>%` method chaining
- Multivariate distributions – `MultivariateNormal` and other multivariate classes
