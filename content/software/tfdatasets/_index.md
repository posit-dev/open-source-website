---
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

external:
  contributors:
  - jjallaire
  - dfalbel
  - t-kalinowski
  - javierluraschi
  - terrytangyuan
  - ericricky
  description: R interface to TensorFlow Datasets API
  first_commit: '2017-10-04T13:39:34+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-02-13T14:17:03.098106+00:00'
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

tfdatasets brings the power of TensorFlow's Dataset API to R, providing a robust framework for building efficient data pipelines for machine learning workflows. It enables you to work with arbitrarily large datasets through a streaming interface, reading and transforming data without loading everything into memory. The package supports multiple data formats including CSV and TFRecords, and offers essential operations like shuffling, batching, repeating datasets across epochs, and applying custom transformations through mapping functions.

What makes tfdatasets particularly powerful is that all data reading and transformation operations run as TensorFlow graph operations, executed in C++ and in parallel with model training for maximum performance. This seamless integration with TensorFlow's underlying infrastructure means your data pipelines can scale efficiently alongside your models. With high-level convenience functions for Keras integration, tfdatasets streamlines the entire process from raw data to trained models, making it an essential tool for R users building production-ready machine learning systems.
