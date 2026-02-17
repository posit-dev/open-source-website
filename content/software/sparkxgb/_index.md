---
description: R interface for XGBoost on Spark
github: rstudio/sparkxgb
languages:
- R
latest_release: '2024-04-30T15:08:13+00:00'
people:
- Edgar Ruiz
title: sparkxgb
website: https://spark.posit.co/packages/sparkxgb/

external:
  description: R interface for XGBoost on Spark
  first_commit: '2018-11-21T08:31:04+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-02-17T11:21:21.876110+00:00'
  latest_release: '2024-04-30T15:08:13+00:00'
  license: NOASSERTION
  people:
  - Edgar Ruiz
  repo: rstudio/sparkxgb
  stars: 45
  title: sparkxgb
  website: https://spark.posit.co/packages/sparkxgb/
---

sparkxgb is a sparklyr extension that provides an interface to XGBoost on Spark, allowing you to run XGBoost models on distributed data. It supports both formula-based model specification and Spark ML Pipelines API for building machine learning workflows.

The package integrates XGBoost with Spark's distributed computing capabilities, enabling you to train gradient boosting models on large datasets that don't fit in memory. It provides both classifier and regressor implementations that work seamlessly with sparklyr's data manipulation functions and ML pipeline components. The package supports hyperparameter tuning through cross-validation and integrates with Spark's model evaluation framework.
