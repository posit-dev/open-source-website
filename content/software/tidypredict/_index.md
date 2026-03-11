---
description: Run predictions inside the database
github: tidymodels/tidypredict
image: logo.png
color: "#FF00D2"
languages:
- R
latest_release: '2026-02-26T22:11:23+00:00'
people:
- Edgar Ruiz
- Emil Hvitfeldt
- Max Kuhn
- Simon Couch
- Julia Silge
- Hannah Frick
- Davis Vaughan
- Jeroen Janssens
title: tidypredict
website: https://tidypredict.tidymodels.org

external:  # updated automatically, do not edit
  description: Run predictions inside the database
  first_commit: '2017-12-18T00:26:43+00:00'
  forks: 33
  languages:
  - R
  last_updated: '2026-03-05T16:22:26.923325+00:00'
  latest_release: '2026-02-26T22:11:23+00:00'
  license: NOASSERTION
  people:
  - Edgar Ruiz
  - Emil Hvitfeldt
  - Max Kuhn
  - Simon Couch
  - Julia Silge
  - Hannah Frick
  - Davis Vaughan
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/tidypredict
  stars: 263
  title: tidypredict
  website: https://tidypredict.tidymodels.org
---

The tidypredict package converts R model objects into formulas that can be executed inside databases via SQL. It parses fitted models (like lm, glm, randomForest, xgboost, and others) and extracts the coefficients and structure needed to generate predictions without requiring the original model object or R environment.

This package solves the problem of scoring models at scale by pushing predictions into the database layer rather than pulling data into R. It works through dplyr's database interface to support multiple SQL backends, eliminating the need to save model objects as .rds files or use PMML for deployment. The package also provides a parsed model specification format that can be stored as a simple data structure and works with parsnip-fitted models from the tidymodels ecosystem.
