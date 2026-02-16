---
description: An interface to Google's BigQuery from R.
github: r-dbi/bigrquery
languages:
- R
latest_release: '2025-09-10T12:43:44+00:00'
people:
- Hadley Wickham
- Jenny Bryan
- Joe Cheng
- Jeroen Janssens
- Edgar Ruiz
- Davis Vaughan
title: bigrquery
website: https://bigrquery.r-dbi.org

external:
  contributors:
  - hadley
  - jennybc
  - craigcitro
  - byapparov
  - BrianWeinstein
  - apalacio9502
  - jarodmeng
  - realAkhmed
  - batpigandme
  - mgirlich
  - krlmlr
  - MichaelChirico
  - cassws
  - totogo
  - davidadamsphd
  - meztez
  - jimmyg3g
  - jcheng5
  - Ka2wei
  - mpancia
  - maelle
  - mfansler
  - mcanouil
  - deflaux
  - rasmusab
  - drewlanenga
  - r2evans
  - ras44
  - jeroenjanssens
  - j450h1
  - edgararuiz
  - paleolimbot
  - DavisVaughan
  - paulsendavidjay
  - husseyd
  - backlin
  - clente
  - bbrewington
  - ahmohamed
  - AdeelK93
  description: An interface to Google's BigQuery from R.
  first_commit: '2013-05-22T14:04:16+00:00'
  forks: 190
  languages:
  - R
  last_updated: '2026-02-13T14:17:21.864429+00:00'
  latest_release: '2025-09-10T12:43:44+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Jenny Bryan
  - Joe Cheng
  - Jeroen Janssens
  - Edgar Ruiz
  - Davis Vaughan
  repo: r-dbi/bigrquery
  stars: 525
  title: bigrquery
  website: https://bigrquery.r-dbi.org
---

bigrquery is an R package that provides a seamless interface to Google BigQuery, making it easy to work with massive datasets in the cloud directly from your R environment. Whether you're querying petabyte-scale data, managing datasets and tables, or integrating BigQuery into your data analysis pipelines, bigrquery streamlines the entire workflow by wrapping BigQuery's REST API with intuitive R functions. The package works with Google's free sandbox environment and public datasets, giving data scientists immediate access to powerful cloud computing without requiring infrastructure setup.

The package offers three levels of abstraction to match your expertise and workflow preferences: a low-level API for granular control, a DBI interface for standard database operations, and a dplyr interface that lets you write familiar R code while automatically generating optimized SQL queries. This flexibility means you can execute complex queries, upload datasets, retrieve metadata, and manage BigQuery resources using whichever approach best fits your needs. With built-in authentication handling and security-conscious defaults, bigrquery makes enterprise-grade cloud analytics accessible to R users at any skill level.
