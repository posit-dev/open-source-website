---
title: randomizr
image: page-1.png
resource_type: cheatsheet
by: community
date: '2018-06-01'
description: Conduct simple, complete, block, cluster, and block-and-cluster random assignment for experimental research designs.
download_url: randomizr.pdf
people:
- Alexander Coppock
thumbnails:
- page-1.png
languages:
- R
---

The randomizr package implements randomization procedures for experimental research, including simple, complete, block, cluster, and block-and-cluster random assignment. Each assignment function has a sampling analogue, and `declare_ra()` allows researchers to inspect and diagnose assignment procedures before conducting a study.

## What's covered
- Two-arm trials – `simple_ra()`, `complete_ra()`, `block_ra()`, `cluster_ra()`, `block_and_cluster_ra()`
- Multi-arm trials – `num_arms`, `conditions`, and `*_each` arguments for multi-arm designs
- Block designs – `block_m_each` and `block_prob_each` for block-varying probability designs
- Declaration – `declare_ra()`, `conduct_ra()`, `obtain_condition_probabilities()`
- Sampling – `simple_rs()`, `complete_rs()`, `strata_rs()`, `cluster_rs()`, `strata_and_cluster_rs()`
- Stata – equivalent Stata version of the package via `ssc install randomizr`
