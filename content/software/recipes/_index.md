---
color: '#70bdd0'
description: Pipeable steps for feature engineering and data preprocessing to prepare
  for modeling
github: tidymodels/recipes
image: logo.png
languages:
- R
latest_release: '2026-05-30T21:02:36+00:00'
people:
- Emil Hvitfeldt
- Max Kuhn
- Julia Silge
- Davis Vaughan
- Hannah Frick
- Simon Couch
- Daniel Falbel
- Lionel Henry
- Garrick Aden-Buie
- Gábor Csárdi
- Jeroen Janssens
title: recipes
topics:
- Data Wrangling
- Machine Learning
website: https://recipes.tidymodels.org

external:  # updated automatically, do not edit
  description: Pipeable steps for feature engineering and data preprocessing to prepare
    for modeling
  first_commit: '2016-12-16T02:40:24+00:00'
  forks: 128
  languages:
  - R
  last_updated: '2026-07-21T09:44:10.613822+00:00'
  latest_release: '2026-05-30T21:02:36+00:00'
  license: NOASSERTION
  people:
  - Emil Hvitfeldt
  - Max Kuhn
  - Julia Silge
  - Davis Vaughan
  - Hannah Frick
  - Simon Couch
  - Daniel Falbel
  - Lionel Henry
  - Garrick Aden-Buie
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/recipes
  stars: 618
  title: recipes
  website: https://recipes.tidymodels.org
---

The recipes package provides a dplyr-like interface for building feature engineering pipelines to prepare data for modeling. It allows you to define a sequence of preprocessing steps that can be applied consistently across training and test datasets.

Recipes offers an alternative to R's traditional formula and model.matrix approach, addressing their limitations when handling complex preprocessing workflows. The package excels at tasks like normalizing predictors, handling categorical variables, and creating derived features through a composable, step-by-step framework. It integrates seamlessly with the tidymodels ecosystem for end-to-end modeling workflows.
