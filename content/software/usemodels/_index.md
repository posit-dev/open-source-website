---
description: Boilerplate Code for tidymodels
github: tidymodels/usemodels
languages:
- R
latest_release: '2022-02-18T22:08:12+00:00'
people:
- Max Kuhn
- Emil Hvitfeldt
- Julia Silge
- Hannah Frick
- Gábor Csárdi
- Jeroen Janssens
title: usemodels
website: https://usemodels.tidymodels.org

external:
  contributors:
  - topepo
  - EmilHvitfeldt
  - juliasilge
  - hfrick
  - qiushiyan
  - bryceroney
  - gaborcsardi
  - jeroenjanssens
  - vinchinzu
  description: Boilerplate Code for tidymodels
  first_commit: '2020-06-06T00:02:59+00:00'
  forks: 7
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.563376+00:00'
  latest_release: '2022-02-18T22:08:12+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  - Emil Hvitfeldt
  - Julia Silge
  - Hannah Frick
  - Gábor Csárdi
  - Jeroen Janssens
  repo: tidymodels/usemodels
  stars: 86
  title: usemodels
  website: https://usemodels.tidymodels.org
---

usemodels is a productivity-boosting R package that eliminates the repetitive task of writing boilerplate code for tidymodels workflows. Instead of manually setting up recipes, model specifications, workflows, and tuning grids from scratch every time you start a new modeling project, usemodels generates tailored code snippets for you based on your data and chosen model. Simply provide a formula and dataset to one of the `use_*` functions, and it instantly creates appropriate preprocessing steps, model configurations, and tuning parameters that match your data types and modeling approach.

The package intelligently adapts to your specific context, automatically including necessary recipe steps based on your data characteristics and model requirements. For example, when using glmnet with categorical predictors, it knows to add dummy variable encoding and normalization steps. With support for 16+ popular modeling engines including xgboost, ranger, glmnet, and keras, usemodels accelerates your workflow while teaching best practices through example code. Whether you're prototyping quickly or learning the tidymodels framework, usemodels helps you focus on the modeling decisions that matter rather than remembering syntax and preprocessing requirements.
