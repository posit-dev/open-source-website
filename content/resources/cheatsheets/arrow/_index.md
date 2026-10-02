---
title: Arrow for R
image: page-1.png
resource_type: cheatsheet
by: community
date: '2022-02-01'
description: Read, write, and manipulate larger-than-memory datasets using the Apache Arrow C++ library from R.
download_url: arrow.pdf
people:
- Mauricio Vargas
thumbnails:
- page-1.png
- page-2.png
software:
- dplyr
languages:
- R
---

arrow gives R users access to the Apache Arrow C++ library, a language-independent columnar memory format designed for efficient analytics. It provides dplyr-compatible operations on datasets too large to fit in memory, and enables zero-copy data sharing between R and Python.

## What's covered
- Arrow data structures – Table and Dataset objects
- Read individual files – `read_parquet()`, `read_feather()`, `read_csv_arrow()`
- Read multi-file datasets – `open_dataset()` with format and partitioning options
- Write individual files – `write_parquet()`, `write_feather()`, compression options
- Write multi-file datasets – `write_dataset()` with partitioning
- Manipulate larger-than-memory datasets – dplyr verbs with `collect()`
- Zero-copy R and Python data sharing – reticulate and pyarrow integration
- Cloud storage support (S3) – reading and writing from S3 URIs
