---
description: ''
github: tidymodels/shinymodels
languages:
- R
latest_release: '2024-01-31T15:11:11+00:00'
people:
- Max Kuhn
- Simon Couch
- Emil Hvitfeldt
- Julia Silge
- Carson Sievert
- Hannah Frick
title: shinymodels
website: https://shinymodels.tidymodels.org/

external:
  contributors:
  - adhikars11
  - topepo
  - simonpcouch
  - EmilHvitfeldt
  - juliasilge
  - cpsievert
  - hfrick
  - romainfrancois
  description: ''
  first_commit: '2021-06-03T04:19:47+00:00'
  forks: 6
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.703949+00:00'
  latest_release: '2024-01-31T15:11:11+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  - Simon Couch
  - Emil Hvitfeldt
  - Julia Silge
  - Carson Sievert
  - Hannah Frick
  repo: tidymodels/shinymodels
  stars: 49
  title: shinymodels
  website: https://shinymodels.tidymodels.org/
---

shinymodels creates interactive Shiny applications for exploring tidymodels tuning and resampling results. When working with complex model evaluation outputs, it can be challenging to interpret metrics and identify areas for improvement through code alone. shinymodels transforms these technical outputs into an intuitive visual interface, allowing you to interactively investigate model performance, examine observed versus predicted values, explore residual patterns, and identify outliers without writing additional analysis code.

The package works seamlessly with tidymodels functions like `fit_resamples()`, `last_fit()`, and various `tune_*()` functions, making it easy to launch an interactive exploration session directly from your modeling workflow. By revealing patterns such as nonlinear relationships in residuals or problematic observations, shinymodels helps you make faster, more informed decisions about model refinement and validation, bridging the gap between statistical model objects and actionable insights.