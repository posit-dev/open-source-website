---
description: Turn SciKitLearn pipelines into SQL
github: posit-dev/orbital
languages:
- Python
latest_release: '2026-02-09T13:14:04+00:00'
title: orbital
website: https://posit-dev.github.io/orbital/

external:
  contributors:
  - amol-
  - gregorywaynepower
  description: Turn SciKitLearn pipelines into SQL
  first_commit: '2025-02-25T10:47:37+00:00'
  forks: 2
  languages:
  - Python
  last_updated: '2026-02-13T14:16:46.419072+00:00'
  latest_release: '2026-02-09T13:14:04+00:00'
  license: MIT
  repo: posit-dev/orbital
  stars: 110
  title: orbital
  website: https://posit-dev.github.io/orbital/
---

Orbital transforms Scikit-Learn machine learning pipelines into SQL queries that can execute directly in your database, eliminating the need for Python runtime environments during inference. This powerful tool enables you to deploy models in SQL-first environments where Python isn't available or practical, allowing predictions to run at database query time with reduced latency and operational complexity. Whether you're migrating ML workflows to a database-centric architecture or looking to simplify your model serving infrastructure, Orbital bridges the gap between Python-trained models and production SQL systems.

Supporting a wide range of Scikit-Learn models including linear and logistic regression, tree-based methods like decision trees and random forests, gradient boosting, and regularized regression (Lasso, Elastic Net), Orbital handles both model conversion and common data preprocessing transformations such as standardization through ColumnTransformer components. The tool currently supports DuckDB with plans to expand to additional database dialects, making it easier for data scientists and developers to leverage their existing machine learning pipelines in high-performance database environments without rewriting their models from scratch.
