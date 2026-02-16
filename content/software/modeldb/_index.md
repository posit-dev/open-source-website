---
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

external:
  contributors:
  - edgararuiz
  - topepo
  - edgararuiz-zz
  - juliasilge
  - hfrick
  - EmilHvitfeldt
  - GarrettMooney
  - hadley
  - karldw
  description: Run models inside a database using R
  first_commit: '2018-03-02T02:01:56+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.166603+00:00'
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

modeldb is an innovative R package that enables you to run machine learning algorithms directly inside your database. By leveraging dplyr and dbplyr for SQL translation, modeldb keeps computations where your data resides, eliminating the need to transfer large datasets into R's memory. This approach is particularly valuable when working with massive datasets that would be impractical to load locally, allowing you to harness your existing database infrastructure for analytical workloads while maintaining the familiar tidyverse workflow.

The package currently supports linear regression and k-means clustering, with results that integrate seamlessly with other tidymodels packages like tidypredict for in-database predictions. What makes modeldb especially powerful for data scientists and developers is its transparency: it generates explicit SQL queries that you can inspect, modify, and audit, providing full visibility into how your models execute at the database level. Whether you're building reproducible analysis pipelines or need to keep sensitive data within your organization's database systems, modeldb delivers a streamlined workflow that combines the flexibility of R with the scalability of database computing.
