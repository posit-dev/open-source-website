---
description: Sparklyr Extensions API
github: rstudio/sparkapi
languages:
- R
people:
- JJ Allaire
title: sparkapi
website: http://spark.rstudio.com/extensions.html

external:
  contributors:
  - jjallaire
  - javierluraschi
  - dselivanov
  - lepennec
  description: Sparklyr Extensions API
  first_commit: '2016-06-20T20:23:25+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-02-13T14:17:02.388612+00:00'
  license: Apache-2.0
  people:
  - JJ Allaire
  repo: rstudio/sparkapi
  stars: 32
  title: sparkapi
  website: http://spark.rstudio.com/extensions.html
---

The sparkapi package provides a powerful extensions API that enables developers to build custom R interfaces to Apache Spark. It exposes the same internal facilities that sparklyr uses for its dplyr and machine learning interfaces, allowing you to create specialized extensions for custom ML pipelines, third-party Spark packages, and domain-specific distributed computing workflows. With core functions like `invoke()`, `invoke_new()`, and `invoke_static()`, developers can seamlessly call Spark methods from R, bridging the gap between R's expressive syntax and Spark's distributed computing capabilities.

The API is built around three fundamental classes that manage the R-to-Java bridge: `spark_connection` for managing communication with the Spark shell, `spark_jobj` for representing remote Spark objects, and `spark_dataframe` for referencing remote DataFrames. This extensible architecture has enabled a thriving ecosystem of extension packages, from H2O integration and geospatial analysis to BigQuery connectivity and XGBoost support. Whether you're wrapping existing Spark functionality or integrating custom Java/Scala libraries, sparkapi provides the dependency management tools and wrapper patterns you need to create R packages that feel native while leveraging Spark's distributed processing power.
