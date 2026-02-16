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
  contributors:
  - isabelizimm
  - has2k1
  - ganesh-k13
  - juliasilge
  - machow
  - gsingh91
  - sagerb
  - mikemahoney218
  - randyzwitch
  - SamEdwardes
  - M4thM4gician
  - tom-ruhland-cla
  - xuf12
  description: Version, share, deploy, and monitor models.
  first_commit: '2021-12-09T02:14:08+00:00'
  forks: 18
  languages:
  - Python
  last_updated: '2026-02-13T14:17:05.357961+00:00'
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

Vetiver provides a unified toolkit for managing machine learning models throughout their entire lifecycle, from training to production deployment. The package addresses a critical challenge in ML workflows: bridging the gap between model development and real-world deployment. Rather than creating ad-hoc solutions for each project, vetiver offers standardized, reproducible processes for versioning, sharing, deploying, and monitoring trained models with fluent tooling designed for practical workflows.

With support for popular frameworks including scikit-learn, PyTorch, statsmodels, XGBoost, and spaCy, vetiver captures essential model metadata and input data prototypes, stores them using flexible backends like local folders, S3, or Posit Connect, and converts models into production-ready REST APIs built on FastAPI. The package includes intelligent data validation to prevent prediction errors and extensible handlers for custom model types, making it an essential tool for data scientists and ML engineers seeking to maintain model reproducibility, collaborate effectively, and deploy scalable web services with confidence.