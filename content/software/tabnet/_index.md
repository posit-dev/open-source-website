---
color: '#E7B10A'
description: An R implementation of TabNet
github: mlverse/tabnet
image: logo.svg
languages:
- R
latest_release: '2026-07-22T06:45:27+00:00'
people:
- Daniel Falbel
title: tabnet
website: https://mlverse.github.io/tabnet/

external:  # updated automatically, do not edit
  description: An R implementation of TabNet
  first_commit: '2020-10-16T19:13:14+00:00'
  forks: 16
  languages:
  - R
  last_updated: '2026-09-18T14:18:28.941535+00:00'
  latest_release: '2026-07-22T06:45:27+00:00'
  license: NOASSERTION
  people:
  - Daniel Falbel
  readme_image: man/figures/README-model-fit-1.png
  repo: mlverse/tabnet
  stars: 119
  title: tabnet
  website: https://mlverse.github.io/tabnet/
---

tabnet is an R implementation of the TabNet deep learning architecture for tabular data, built on the torch package. It supports binary classification, multi-class classification, and regression tasks, with a tidymodels-compatible interface that accepts data frames, formulas, and recipes.

TabNet provides built-in interpretability through attention maps that show which features the model focuses on, viewable in aggregate or per network step. It handles missing predictor values natively through its masking mechanism, supports self-supervised pretraining for semi-labeled datasets, and includes an AUM loss function for imbalanced binary classification. It also supports hierarchical multi-label classification via coherent hierarchical networks, a capability not found in other TabNet implementations.
