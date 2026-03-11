---
image: logo.svg
color: "#E7B10A"
description: R interface to TensorFlow Datasets API
github: rstudio/tfdatasets
languages:
- R
latest_release: '2025-08-20T14:50:10+00:00'
people:
- JJ Allaire
- Daniel Falbel
- Tomasz Kalinowski
title: tfdatasets
website: https://tensorflow.rstudio.com/tools/tfdatasets/

external:  # updated automatically, do not edit
  description: R interface to TensorFlow Datasets API
  first_commit: '2017-10-04T13:39:34+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-03-05T16:12:35.774040+00:00'
  latest_release: '2025-08-20T14:50:10+00:00'
  people:
  - JJ Allaire
  - Daniel Falbel
  - Tomasz Kalinowski
  repo: rstudio/tfdatasets
  stars: 34
  title: tfdatasets
  website: https://tensorflow.rstudio.com/tools/tfdatasets/
---

The tfdatasets package provides an R interface to TensorFlow's Dataset API for creating scalable input pipelines that feed data into TensorFlow and Keras models.

This package enables efficient data handling for machine learning workflows through streaming interfaces that can process arbitrarily large datasets without loading everything into memory. It supports multiple data formats including CSV and TFRecords, allows transformations like mapping, shuffling, and batching, and executes these operations as TensorFlow graph operations in C++ for parallel processing alongside model training. This makes it particularly valuable for building production-scale training pipelines where data preprocessing needs to be fast and memory-efficient.
