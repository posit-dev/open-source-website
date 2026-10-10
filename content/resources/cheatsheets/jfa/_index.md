---
title: Audit sampling with jfa
image: page-1.png
resource_type: cheatsheet
by: community
date: '2021-09-01'
description: Plan, select, and evaluate audit samples using classical or Bayesian statistics with a five-function workflow.
download_url: jfa.pdf
people:
- Koen Derks
thumbnails:
- page-1.png
languages:
- R
---

jfa implements the standard audit sampling workflow in R, supporting both classical and Bayesian inference. The package provides five main functions that map to the sequential steps of an audit: specifying a prior, calculating sample size, selecting items, evaluating misstatement, and generating a report.

## What's covered
- Basics – installation, workflow overview, and example dataset (`BuildIt`)
- Construct a prior distribution – `auditPrior()` with likelihood and method arguments
- Calculate the minimum sample size – `planning()` with materiality, expected errors, and likelihood
- Select items from the population – `selection()` with random, cell, or fixed-interval sampling
- Evaluate the misstatement – `evaluation()` with classical or Bayesian methods
- Create a report – `report()` generating an HTML summary of results
