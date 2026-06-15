---
color: '#419599'
description: A modern YAML 1.2 parser and emitter for Python, written in Rust
github: posit-dev/py-yaml12
image: logo.svg
languages:
- Python
- Rust
people:
- Tomasz Kalinowski
- Rich Iannone
title: py-yaml12
website: https://posit-dev.github.io/py-yaml12/

include:
  languages:
  - Rust

external:  # updated automatically, do not edit
  description: A modern YAML 1.2 parser and emitter for Python, written in Rust
  first_commit: '2025-11-22T02:16:33+00:00'
  forks: 1
  languages:
  - Python
  last_updated: '2026-05-20T12:41:49.634245+00:00'
  license: MIT
  people:
  - Tomasz Kalinowski
  - Rich Iannone
  repo: posit-dev/py-yaml12
  stars: 14
  title: py-yaml12
  website: https://posit-dev.github.io/py-yaml12/
---

A YAML 1.2 parser/formatter for Python, implemented in Rust for speed
and correctness. Built on the excellent
[`saphyr`](https://github.com/saphyr-rs/saphyr) crate.

For almost every use case, `yaml12` lets you work with plain builtin
Python types end to end: `dict`, `list`, `int`, `float`, `str`, and
`None`. JSON is a subset of YAML 1.2, so all valid JSON is also valid
YAML and parses the same way.

- Parse YAML text or files with `parse_yaml()` and `read_yaml()`.
- Serialize Python values with `format_yaml()` or `write_yaml()`.
- 100% compliance with the [yaml-test-suite](https://github.com/yaml/yaml-test-suite).
- Advanced YAML features (document streams, tags, complex mapping keys) are supported and
  round-trip cleanly when needed. `Yaml` is the wrapper type for tagged nodes and unhashable
  mapping keys.

