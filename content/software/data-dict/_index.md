---
image: logo.svg
color: "#404041"
description: ''
github: tidyverse/data-dict
languages:
- Rust
latest_release: '2026-08-21T20:27:42+00:00'
people:
- Hadley Wickham
- Gábor Csárdi
- Carlos Scheidegger
title: data-dict
website: http://data-dict.tidyverse.org/

external:  # updated automatically, do not edit
  description: ''
  first_commit: '2026-03-17T17:59:53+00:00'
  forks: 8
  languages:
  - Rust
  last_updated: '2026-09-18T14:21:56.570461+00:00'
  latest_release: '2026-08-21T20:27:42+00:00'
  people:
  - Hadley Wickham
  - Gábor Csárdi
  - Carlos Scheidegger
  repo: tidyverse/data-dict
  stars: 102
  title: data-dict
  website: http://data-dict.tidyverse.org/
---

`data-dict.yaml` is a YAML specification for defining data dictionaries — describing tables, columns, types, constraints, and relationships — along with a Rust CLI that validates data against those definitions and renders them as self-contained HTML documentation. It is designed for polyglot teams working across R, Python, and SQL.

The package turns human-readable YAML into an enforceable data contract by validating at three levels: spec conformance, metadata consistency, and actual data values. It can also draft dictionaries from Parquet files, translate assertions into R, Python, or SQL code, and export resolved JSON for programmatic use. The CLI includes a language server for editor support and a live-reloading development mode for customizing the rendered output.
