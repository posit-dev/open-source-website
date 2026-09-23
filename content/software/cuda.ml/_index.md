---
color: '#B0BAFB'
description: R interface for cuML
github: mlverse/cuda.ml
image: logo.png
languages:
- R
latest_release: '2026-08-20T14:20:08+00:00'
people:
- Tomasz Kalinowski
- Daniel Falbel
title: cuda.ml
website: https://mlverse.github.io/cuda.ml/

external:  # updated automatically, do not edit
  description: R interface for cuML
  first_commit: '2021-06-23T20:44:53+00:00'
  forks: 6
  languages:
  - R
  last_updated: '2026-09-18T14:18:46.196574+00:00'
  latest_release: '2026-08-20T14:20:08+00:00'
  license: NOASSERTION
  people:
  - Tomasz Kalinowski
  - Daniel Falbel
  readme_image: https://cranlogs.r-pkg.org/badges/cuda.ml?color=brightgreen
  repo: mlverse/cuda.ml
  stars: 50
  title: cuda.ml
  website: https://mlverse.github.io/cuda.ml/
---

cuda.ml is an R interface to NVIDIA's RAPIDS cuML library, enabling GPU-accelerated machine learning directly from R. It supports supervised and unsupervised algorithms including linear models, random forests, SVMs, k-nearest neighbors, k-means, DBSCAN, PCA, UMAP, and t-SNE, all running on CUDA-capable GPUs.

The package integrates with the tidymodels ecosystem, providing parsnip engine bindings so existing modeling workflows can switch to GPU acceleration with minimal code changes. It also offers nvForest inference for XGBoost, LightGBM, and Treelite models, with an optional CPU-only backend for deployment without a GPU. The native backend runs on Linux x86_64 (including WSL2 on Windows) and requires an NVIDIA driver 580+ for GPU operations.
