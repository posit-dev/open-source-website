---
color: '#E20000'
description: Data validation toolkit for assessing and monitoring data quality.
github: posit-dev/pointblank
image: pointblank_logo.svg
languages:
- Python
latest_release: '2026-02-26T14:30:49+00:00'
people:
- Rich Iannone
- Michael Chow
title: pointblank
website: https://posit-dev.github.io/pointblank/

external:  # updated automatically, do not edit
  description: Data validation toolkit for assessing and monitoring data quality.
  first_commit: '2024-10-23T23:55:57+00:00'
  forks: 24
  languages:
  - Python
  last_updated: '2026-03-05T16:04:50.559722+00:00'
  latest_release: '2026-02-26T14:30:49+00:00'
  license: MIT
  people:
  - Rich Iannone
  - Michael Chow
  readme_image: https://posit-dev.github.io/pointblank/assets/pointblank_logo.svg
  repo: posit-dev/pointblank
  stars: 376
  title: pointblank
  website: https://posit-dev.github.io/pointblank/
---

Pointblank is a Python data validation toolkit that assesses and monitors data quality across multiple backends including Polars, Pandas, DuckDB, PostgreSQL, MySQL, SQLite, Parquet, PySpark, and Snowflake. It provides a chainable API for building validation pipelines that check data against business rules and generate interactive reports showing validation results.

The package emphasizes clear communication of data quality issues through customizable reports that make validation results immediately understandable to both technical and non-technical stakeholders. It includes AI-powered validation drafting that automatically suggests intelligent validation rules based on your data, threshold-based alerts with custom actions, YAML configuration support for version-controlled workflows, a CLI for running validations in CI/CD pipelines, and synthetic data generation for testing. Unlike validation libraries that only catch errors, Pointblank focuses on both finding issues and effectively sharing insights across teams.
