---
title: h2o
image: page-1.png
resource_type: cheatsheet
by: community
date: '2018-06-01'
description: Work with H2O distributed in-memory data frames from R, covering data import, manipulation, math, and aggregation operations.
download_url: h2o.pdf
people:
- Juan Telleria Ruiz de Aguirre
thumbnails:
- page-1.png
- page-2.png
languages:
- R
source_files:
- file: h2o.pptx
  format: PowerPoint
---

The h2o R package provides an interface to the H2O distributed in-memory platform for scalable data processing and machine learning. This cheat sheet covers the full data workflow: importing and exporting files, converting between R and H2O objects, subscripting and subsetting H2O frames, performing vectorized math, and computing group-by and generic summaries.

## What's covered
- Data import/export – `h2o.uploadFile()`, `h2o.importFile()`, `h2o.exportFile()`
- Native R to H2O coercion – `as.h2o()`; H2O to R – `as.data.frame()`
- Data generation – `h2o.createFrame()`, `h2o.runif()`
- Data sampling/splitting
- Subscripting and subsetting – `x[i,j]`, `h2o.head()`, `h2o.tail()`
- Data attributes – `h2o.names()`, `h2o.dim()`, `h2o.nrow()`, `h2o.ncol()`
- Data type coercion – `h2o.asfactor()`, `h2o.asnumeric()`, `h2o.as_date()`
- Math operations – `h2o.abs()`, `h2o.sqrt()`, `h2o.log()`, cumulative functions
- Group by summaries – `nrow`, `max`, `min`, `sum`, `mean`, `sd`
- Generic summaries – `h2o.median()`, `h2o.cor()`, `h2o.quantile()`, `h2o.summary()`
- Aggregations – row/column aggregation with `apply`
