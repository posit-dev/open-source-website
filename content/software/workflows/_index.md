---
description: Modeling Workflows
github: tidymodels/workflows
image: logo.png
languages:
- R
latest_release: '2025-08-27T09:07:53+00:00'
people:
- Davis Vaughan
- Hannah Frick
- Simon Couch
- Emil Hvitfeldt
- Max Kuhn
- Julia Silge
- Gábor Csárdi
- Jeroen Janssens
title: workflows
website: https://workflows.tidymodels.org/

external:
  contributors:
  - DavisVaughan
  - hfrick
  - simonpcouch
  - EmilHvitfeldt
  - topepo
  - juliasilge
  - brshallo
  - collinberke
  - gaborcsardi
  - jeroenjanssens
  description: Modeling Workflows
  first_commit: '2019-09-25T15:45:32+00:00'
  forks: 25
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.374433+00:00'
  latest_release: '2025-08-27T09:07:53+00:00'
  license: NOASSERTION
  people:
  - Davis Vaughan
  - Hannah Frick
  - Simon Couch
  - Emil Hvitfeldt
  - Max Kuhn
  - Julia Silge
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/workflows
  stars: 210
  title: workflows
  website: https://workflows.tidymodels.org/
---

Building machine learning pipelines often means juggling multiple objects: data preprocessing recipes, model specifications, and fitted results scattered across your workspace. The workflows package simplifies this complexity by bundling preprocessing, modeling, and post-processing steps into a single, cohesive workflow object. With workflows, you can fit an entire pipeline with one call to `fit()`, eliminating the error-prone process of manually managing recipe preparation, model training, and ensuring consistency between training and prediction phases.

Workflows integrates seamlessly with the tidymodels ecosystem, combining recipes for feature engineering with parsnip models for statistical and machine learning approaches. The package provides intuitive functions to update, remove, or modify pipeline components, making it easy to experiment with different preprocessing strategies or model types without rewriting your entire analysis. Whether you're comparing multiple models or building complex preprocessing pipelines, workflows ensures reproducibility by capturing all necessary components in a portable object that can be saved, shared, and deployed with confidence.