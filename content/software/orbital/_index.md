---
color: '#72994E'
description: Turn SciKitLearn pipelines into SQL
github: posit-dev/orbital
image: logo.svg
languages:
- Python
latest_release: '2026-03-02T18:19:46+00:00'
title: orbital
topics:
- Data Wrangling
- MLOps and Admin
- Machine Learning
website: https://posit-dev.github.io/orbital/

external:  # updated automatically, do not edit
  description: Turn SciKitLearn pipelines into SQL
  first_commit: '2025-02-25T10:47:37+00:00'
  forks: 3
  languages:
  - Python
  last_updated: '2026-05-20T08:05:16.170678+00:00'
  latest_release: '2026-03-02T18:19:46+00:00'
  license: MIT
  repo: posit-dev/orbital
  stars: 117
  title: orbital
  website: https://posit-dev.github.io/orbital/
---

Orbital converts trained scikit-learn pipelines into SQL queries that can execute directly in a database without requiring Python. This enables deploying machine learning models where only database access is available.

The package automatically translates both preprocessing steps (like StandardScaler) and model predictions (including linear models, decision trees, random forests, and gradient boosting) into equivalent SQL. This solves the deployment problem of running scikit-learn models in environments where Python isn't available or when you need to score data at scale directly in the database. The generated SQL produces identical predictions to the original scikit-learn pipeline.
