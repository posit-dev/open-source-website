---
color: '#419599'
description: R interface to Google Cloud Machine Learning Engine
github: rstudio/cloudml
image: logo.svg
languages:
- R
latest_release: '2025-08-18T22:42:41+00:00'
people:
- JJ Allaire
- Daniel Falbel
- Tomasz Kalinowski
title: cloudml
website: https://tensorflow.rstudio.com/tools/cloudml/

external:  # updated automatically, do not edit
  description: R interface to Google Cloud Machine Learning Engine
  first_commit: '2017-02-17T19:29:06+00:00'
  forks: 23
  languages:
  - R
  last_updated: '2026-03-05T16:11:44.234035+00:00'
  latest_release: '2025-08-18T22:42:41+00:00'
  people:
  - JJ Allaire
  - Daniel Falbel
  - Tomasz Kalinowski
  repo: rstudio/cloudml
  stars: 65
  title: cloudml
  website: https://tensorflow.rstudio.com/tools/cloudml/
---

The cloudml package provides an R interface to Google Cloud Machine Learning Engine, enabling scalable training and deployment of machine learning models built with keras, tfestimators, and tensorflow packages on Google's managed infrastructure.

The package solves the problem of limited local computational resources by providing on-demand access to powerful hardware including GPUs and Tesla P100 accelerators. It includes built-in hyperparameter tuning capabilities to optimize model architectures and supports deploying trained models to Google's global prediction platform that can handle thousands of concurrent users and terabytes of data. You only pay for the hardware resources you actually use during training and prediction.
