---
description: Additional functions for model tuning
github: tidymodels/finetune
image: logo.png
color: "#361535"
languages:
- R
latest_release: '2025-05-20T21:08:32+00:00'
people:
- Max Kuhn
- Simon Couch
- Hannah Frick
- Emil Hvitfeldt
- Julia Silge
- Gábor Csárdi
- Jeroen Janssens
title: finetune
website: https://finetune.tidymodels.org/

external:  # updated automatically, do not edit
  description: Additional functions for model tuning
  first_commit: '2020-07-04T20:12:07+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-03-05T16:23:30.548730+00:00'
  latest_release: '2025-05-20T21:08:32+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  - Simon Couch
  - Hannah Frick
  - Emil Hvitfeldt
  - Julia Silge
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/finetune
  stars: 63
  title: finetune
  website: https://finetune.tidymodels.org/
---

The finetune package extends the tidymodels tune package with additional hyperparameter optimization methods for machine learning models. It provides two main approaches: simulated annealing for iterative search and racing methods for efficient grid search.

Simulated annealing explores the parameter space iteratively to find optimal values, accepting both better and occasionally worse configurations to escape local optima. Racing methods start by evaluating all parameter combinations on a small number of resamples, then use statistical testing (ANOVA-based or win/loss tournament-style) to eliminate poor performers early and focus computational resources on promising candidates. This makes hyperparameter tuning faster by avoiding full evaluation of parameter combinations that are unlikely to perform well.
