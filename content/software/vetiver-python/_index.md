---
description: Version, share, deploy, and monitor models.
github: rstudio/vetiver-python
image: logo.png
languages:
- Python
latest_release: '2024-12-17T02:43:43+00:00'
people:
- Isabel Zimmerman
- Hassan Kibirige
- Julia Silge
- Michael Chow
title: vetiver-python
website: https://rstudio.github.io/vetiver-python/stable/

external:
  description: Version, share, deploy, and monitor models.
  first_commit: '2021-12-09T02:14:08+00:00'
  forks: 18
  languages:
  - Python
  last_updated: '2026-02-17T11:24:57.075133+00:00'
  latest_release: '2024-12-17T02:43:43+00:00'
  license: MIT
  people:
  - Isabel Zimmerman
  - Hassan Kibirige
  - Julia Silge
  - Michael Chow
  readme_image: docs/figures/logo.png
  repo: rstudio/vetiver-python
  stars: 70
  title: vetiver-python
  website: https://rstudio.github.io/vetiver-python/stable/
---

Vetiver is a Python package for versioning, deploying, and monitoring trained machine learning models. It provides tools to record model metadata, manage input data prototypes, and serve predictions via API endpoints.

The package works with popular frameworks like scikit-learn, PyTorch, statsmodels, XGBoost, and spaCy, with support for custom model handlers. It integrates with the pins package for model storage across multiple backends (local folders, Posit Connect, S3) and uses FastAPI to deploy models as REST APIs. Vetiver handles both the MLOps lifecycle and model governance by tracking versions and validating input data against the model's expected prototype.
