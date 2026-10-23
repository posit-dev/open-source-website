---
title: Scaling Up with R and Apache Arrow
subtitle: Bigger Data, Easier Workflows
date: '2025-05-31'
description: Learn how to analyze data that doesn't fit in memory from R with the arrow package and familiar dplyr code, including Parquet files, multi-file datasets, cloud storage, and DuckDB.
image: cover.jpg
color: '#8A923E'
resource_type: book
edition: 1
publisher: CRC Press
isbn: '9781032660288'
pages: 160
people:
- Nic Crane
- Jonathan Keane
- Neal Richardson
website: https://arrowrbook.com/
read_url: https://arrowrbook.com/
buy_url: https://www.routledge.com/Scaling-Up-with-R-and-Apache-Arrow-Bigger-Data-Easier-Workflows/Crane-Keane-Richardson/p/book/9781032660288
github: arrowrbook/book
software:
- dplyr
languages:
- R
topics:
- Data Wrangling
---

R works best when data fits in memory, but as datasets grow, analyses can slow down or stop working entirely.
Written by developers of the `arrow` R package, this book shows how to analyze larger-than-memory data directly from R, on your own laptop or workstation, without setting up a database or cluster.

Because `arrow` implements the `dplyr` interface, you can query directories of CSV or Parquet files with code you already know, and the package processes the data in chunks rather than loading it all at once.
The book also explains the origins and goals of the Apache Arrow project and why it helps connect data science tools with the wider big data ecosystem.
It is aimed at R users who want to scale up their data processing without learning a whole new framework.

Topics covered include:

- The Apache Arrow project and how the `arrow` R package fits into it
- Manipulating data with familiar `dplyr` syntax
- Choosing and working with file formats such as CSV and Parquet
- Working with multi-file datasets that are larger than memory
- Querying data stored in cloud services such as Amazon S3 and Google Cloud Storage
- Extending `arrow` with user-defined functions and Acero, Arrow's query engine
- Integrating with DuckDB and other tools, and working with geospatial data
- Sharing data across languages and systems

The full text is available online at the book's companion website.
