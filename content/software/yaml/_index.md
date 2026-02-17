---
description: R package for converting objects to and from YAML
github: r-lib/yaml
languages:
- C
latest_release: '2024-07-22T15:23:35+00:00'
people:
- Hadley Wickham
- Charlie Gao
- Davis Vaughan
title: yaml
website: http://yaml.r-lib.org/

external:
  description: R package for converting objects to and from YAML
  first_commit: '2008-04-28T21:52:03+00:00'
  forks: 41
  languages:
  - C
  last_updated: '2026-02-17T11:31:36.419343+00:00'
  latest_release: '2024-07-22T15:23:35+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Charlie Gao
  - Davis Vaughan
  repo: r-lib/yaml
  stars: 169
  title: yaml
  website: http://yaml.r-lib.org/
---

The yaml package provides R bindings to libyaml, enabling fast parsing and emission of YAML format data in R. It allows you to convert between YAML text and R data structures like lists and vectors.

The package solves the common problem of reading configuration files and data serialization in YAML format, which is widely used across programming languages and DevOps tools. It offers both simple functions for quick conversions (`yaml.load()`, `as.yaml()`) and file-based operations (`read_yaml()`, `write_yaml()`). The underlying libyaml library provides performance advantages over pure R implementations.
