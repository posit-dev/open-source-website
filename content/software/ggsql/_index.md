---
color: '#EE6331'
description: A experimental SQL extension for declarative data visualisation based
  on the Grammar of Graphics.
github: posit-dev/ggsql
image: logo.svg
languages:
- SQL
people:
- George Stagg
- Thomas Lin Pedersen
- Teun Van den Brand
- Carson Sievert
title: ggsql
website: http://ggsql.org/

override:
  languages:
  - SQL

external:  # updated automatically, do not edit
  description: A experimental SQL extension for declarative data visualisation based
    on the Grammar of Graphics.
  first_commit: '2025-12-04T13:26:11+00:00'
  forks: 4
  languages:
  - Rust
  last_updated: '2026-03-05T16:06:48.129668+00:00'
  license: MIT
  people:
  - George Stagg
  - Thomas Lin Pedersen
  - Teun Van den Brand
  - Carson Sievert
  repo: posit-dev/ggsql
  stars: 36
  title: ggsql
  website: http://ggsql.org/
---

ggsql is a SQL extension that embeds data visualization directly in SQL queries using Grammar of Graphics syntax. It splits queries at the VISUALISE boundary, passing the SQL portion to a data source (like DuckDB) and compiling the visualization portion into specs that can be rendered through various backends (Vega-Lite, ggplot2, etc.).

The package provides a complete ecosystem for declarative visualization including a tree-sitter grammar with full AST validation, multiple interfaces (CLI tool, REST API, Jupyter kernel, VS Code extension with Positron integration), and Python bindings that output Altair charts. Its pluggable architecture supports different data readers (DuckDB, PostgreSQL, CSV) and visualization writers, allowing single queries to combine data transformation with visualization specifications for multiple geometric layers, scales, facets, and coordinate systems.
