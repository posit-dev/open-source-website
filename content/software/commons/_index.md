---
color: '#2A5C61'
description: AI Agents for Data Analysis
github: posit-dev/commons
image: commons.png
languages:
- R
- Python
latest_release: '2026-09-11T15:27:22+00:00'
people:
- Simon Couch
- Josh Taillon
- Sara Altman
- Carson Sievert
- Garrick Aden-Buie
tags:
- AI
title: commons
topics:
- Artificial Intelligence
website: https://posit-dev.github.io/commons/

include:
  languages:
  - Python

external:  # updated automatically, do not edit
  description: AI Agents for Data Analysis
  first_commit: '2026-06-22T12:44:07+00:00'
  forks: 1
  languages:
  - R
  last_updated: '2026-09-12T21:07:16.598002+00:00'
  latest_release: '2026-09-11T15:27:22+00:00'
  license: NOASSERTION
  people:
  - Simon Couch
  - Josh Taillon
  - Sara Altman
  - Carson Sievert
  - Garrick Aden-Buie
  readme_image: pkg-r/man/figures/logo.png
  repo: posit-dev/commons
  stars: 24
  title: commons
  website: https://posit-dev.github.io/commons/
---

Data teams typically have trusted code that they use to analyze their data and build reports and apps. commons leverages their expertise, situating that trusted code in a series of prompts and tools designed to create an accurate, fast, and cost-effective agent. Trusted calculations can come from R and Python code, data dictionary definitions, Snowflake semantic views, or Databricks metric views.

When answering questions, commons agents first search through a pool of trusted code. If the agent finds an appropriate piece of trusted code, it invokes that code directly. If it does not find relevant trusted code, it searches through additional context before writing custom SQL, R, or Python code. Answers display provenance markers deterministically assigned based on the analysis path.

## Installation

To install the R package:

```r
install.packages("commons")
```

To install the Python package:

```sh
pip install commons
```
