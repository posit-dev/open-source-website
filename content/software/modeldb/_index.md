---
color: '#1E619C'
description: Run models inside a database using R
github: tidymodels/modeldb
image: logo.png
languages:
- R
latest_release: '2025-08-22T17:22:28+00:00'
people:
- Edgar Ruiz
- Max Kuhn
- Julia Silge
- Hannah Frick
- Emil Hvitfeldt
- Hadley Wickham
title: modeldb
website: https://modeldb.tidymodels.org

external:  # updated automatically, do not edit
  description: Run models inside a database using R
  first_commit: '2018-03-02T02:01:56+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-03-05T16:22:29.226922+00:00'
  latest_release: '2025-08-22T17:22:28+00:00'
  license: NOASSERTION
  people:
  - Edgar Ruiz
  - Max Kuhn
  - Julia Silge
  - Hannah Frick
  - Emil Hvitfeldt
  - Hadley Wickham
  readme_image: man/figures/logo.png
  repo: tidymodels/modeldb
  stars: 79
  title: modeldb
  website: https://modeldb.tidymodels.org
---

modeldb enables you to fit machine learning models directly inside databases without pulling data into R. It translates model algorithms into SQL queries using dplyr and dbplyr, working with most database backends.

The package solves memory and performance problems when working with large datasets that live in databases. It currently supports K-means clustering and linear regression, computing everything in the database and returning only the model coefficients or cluster assignments. The model outputs integrate with tidypredict for running predictions in the database as well.
