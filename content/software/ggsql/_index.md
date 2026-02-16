---
description: A experimental SQL extension for declarative data visualisation based
  on the Grammar of Graphics.
github: posit-dev/ggsql
languages:
- Rust
people:
- George Stagg
- Thomas Lin Pedersen
- Teun Van den Brand
- Carson Sievert
title: ggsql
website: http://ggsql.org/

external:
  contributors:
  - georgestagg
  - thomasp85
  - teunbrand
  - cpsievert
  description: A experimental SQL extension for declarative data visualisation based
    on the Grammar of Graphics.
  first_commit: '2025-12-04T13:26:11+00:00'
  forks: 4
  languages:
  - Rust
  last_updated: '2026-02-13T14:16:47.163146+00:00'
  license: MIT
  people:
  - George Stagg
  - Thomas Lin Pedersen
  - Teun Van den Brand
  - Carson Sievert
  repo: posit-dev/ggsql
  stars: 34
  title: ggsql
  website: http://ggsql.org/
---

ggsql is an experimental SQL extension that brings declarative data visualization directly into your SQL queries using the Grammar of Graphics framework. By extending SQL syntax with visualization commands, ggsql lets you write integrated queries that combine data retrieval and visual specifications in one composable expression. The system splits queries at the VISUALISE boundary, routing SQL operations to pluggable data readers like DuckDB or PostgreSQL, while rendering visualizations through multiple output formats including Vega-Lite and ggplot2.

The project provides a complete development ecosystem including a CLI tool, REST API server, Jupyter kernel with inline rendering, VS Code extension with syntax highlighting, and Python bindings. Whether you're exploring data in Jupyter notebooks, generating server-side visualizations via APIs, or creating charts programmatically, ggsql offers a unified syntax with core grammar components like DRAW for geometric layers, SCALE for data transformations, FACET for small multiples, and flexible coordinate systems and theming options.
