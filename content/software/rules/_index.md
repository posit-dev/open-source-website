---
description: parsnip extension for rule-based models
github: tidymodels/rules
image: logo.png
languages:
- R
latest_release: '2023-03-08T23:13:46+00:00'
people:
- Max Kuhn
- Emil Hvitfeldt
- Simon Couch
- Julia Silge
- Hannah Frick
- Gábor Csárdi
- Jeroen Janssens
title: rules
website: https://rules.tidymodels.org

external:
  description: parsnip extension for rule-based models
  first_commit: '2019-10-27T20:58:03+00:00'
  forks: 7
  languages:
  - R
  last_updated: '2026-02-17T11:30:18.258364+00:00'
  latest_release: '2023-03-08T23:13:46+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  - Emil Hvitfeldt
  - Simon Couch
  - Julia Silge
  - Hannah Frick
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/rules
  stars: 42
  title: rules
  website: https://rules.tidymodels.org
---

The rules package is a parsnip extension that provides model definitions for rule-based machine learning models within the tidymodels framework. It enables fitting and prediction with three types of rule-based models: cubist models with linear rules and ensemble boosting, classification rules derived from decision trees, and rule-fit models that combine tree-extracted rules with regularized regression.

This package solves the problem of integrating rule-based models into tidymodels workflows using a consistent interface. It supports both classification and regression tasks across multiple engines (C5.0, Cubist, and xrf). Rule-based models offer interpretable predictions through human-readable if-then rules while maintaining competitive predictive performance compared to black-box models.
