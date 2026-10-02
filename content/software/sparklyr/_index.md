---
color: '#EE6331'
description: R interface for Apache Spark
github: sparklyr/sparklyr
image: sparklyr.png
languages:
- R
latest_release: '2026-06-19T17:19:07+00:00'
people:
- Edgar Ruiz
- Kevin Ushey
- JJ Allaire
- Neal Richardson
- Tomasz Kalinowski
- Jonathan McPherson
- Davis Vaughan
- Christophe Dervieux
- Gábor Csárdi
- Lionel Henry
title: sparklyr
website: https://spark.posit.co/

external:  # updated automatically, do not edit
  description: R interface for Apache Spark
  first_commit: '2016-05-20T15:28:53+00:00'
  forks: 310
  languages:
  - R
  last_updated: '2026-09-18T14:32:58.353261+00:00'
  latest_release: '2026-06-19T17:19:07+00:00'
  license: Apache-2.0
  people:
  - Edgar Ruiz
  - Kevin Ushey
  - JJ Allaire
  - Neal Richardson
  - Tomasz Kalinowski
  - Jonathan McPherson
  - Davis Vaughan
  - Christophe Dervieux
  - Gábor Csárdi
  - Lionel Henry
  readme_image: tools/readme/dplyr-ggplot2-1.png
  repo: sparklyr/sparklyr
  stars: 971
  title: sparklyr
  website: https://spark.posit.co/
---

sparklyr is an R interface for Apache Spark that lets you connect to local or remote Spark clusters and work with large-scale datasets using familiar R syntax. It supports connections via YARN, Mesos, Livy, Kubernetes, and Databricks Connect.

The package integrates directly with dplyr, so you can filter, aggregate, and transform Spark datasets using the same verbs you already know, then collect results into R for visualization. It provides access to Spark's machine learning library through high-level R functions that chain naturally into dplyr pipelines. sparklyr also supports distributed execution of arbitrary R code across cluster nodes via `spark_apply()`, direct SQL queries through a DBI interface, and reading and writing CSV, JSON, and Parquet formats.
