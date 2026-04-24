---
title: "tidymodels Cheatsheets"
date: 2026-04-24
people:
  - Edgar Ruiz
description: >
  Two new cheatsheets for tidymodels are now available: one for creating models
  with parsnip, and one for preprocessing data with recipes.
image: "tidymodels-cheatsheets.png"
image-alt: ""
topics:
  - Machine Learning
software:
  - tidymodels
languages:
  - R
resources:
  - cheatsheets
tags:
  -
source: tidyverse
nohero: false
hidesubscription: false
---

<!--
TODO:
- [ ] Add image (1920×1080 PNG or JPG) and image-alt
- [ ] Review/expand highlights below
- [ ] Open a PR against main for a Netlify preview
-->

We are excited to share two new cheatsheets for [tidymodels](https://www.tidymodels.org/) — a collection of R packages for modeling and machine learning that shares the design principles of the tidyverse.

{{< button url="/resources/cheatsheets/ml-create-models/" text="Create Models cheatsheet" >}}
{{< button url="/resources/cheatsheets/ml-preprocessing-data/" text="Preprocessing Data cheatsheet" >}}

## Create Models with tidymodels

The **Create Models** cheatsheet is your quick reference for building models with [parsnip](https://parsnip.tidymodels.org/). Key highlights:

- **Unified model interface** — specify models independently of the underlying engine using `set_engine()` and `set_mode()`
- **Wide model support** — covers linear regression, logistic regression, random forests, boosted trees, neural networks, and more
- **Consistent workflow** — `fit()` and `predict()` work the same regardless of which engine is powering your model

## Preprocessing Data with tidymodels

The **Preprocessing Data** cheatsheet covers the [recipes](https://recipes.tidymodels.org/) package. Key highlights:

- **Step-by-step preprocessing** — chain `step_*()` functions to build reproducible preprocessing pipelines
- **Role assignment** — use `update_role()` to distinguish predictors, outcomes, and ID columns
- **Common transformations** — normalization (`step_normalize()`), imputation (`step_impute_*()`), dummy encoding (`step_dummy()`), and more
