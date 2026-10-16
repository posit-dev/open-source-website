---
title: BCEA
image: page-1.png
resource_type: cheatsheet
by: community
date: '2021-02-01'
description: Perform Bayesian cost-effectiveness analysis on posterior samples of costs and clinical benefits for multiple interventions.
download_url: bcea.pdf
people:
- Gianluca Baio
thumbnails:
- page-1.png
languages:
- R
---

BCEA (Bayesian Cost-Effectiveness Analysis) takes simulated posterior samples of costs and effectiveness for two or more interventions and computes the standard suite of health economic statistics. Analysis parameters can be set at construction, via setter functions, or at plot time, providing flexible control over reference and comparison groups.

## What's covered
- Introduction – `bcea()` constructor and constituent functions
- Value assignment – three equivalent ways to set reference and comparison
- Selecting analysis interventions – default, set reference, set comparisons
- Expected incremental benefit – `eib.plot()`
- Cost-effectiveness acceptability curve – `ceac_plot()`
- Cost-effectiveness plane – `ceplane_plot()`
- Cost-effectiveness planes with contours – `contour[2]()`
- Expected value of information – `evi.plot()`
- Expected value of perfect partial information – `plot.evppi()`
- Grid of CE plane, EIB, EVI, and CEAC – `plot.bcea()`
- Summarise data – `summary.bcea()`, `sim.table()`, `make.report()`
