---
description: Tree-sitter grammar for R
github: r-lib/tree-sitter-r
languages:
- R
latest_release: '2025-06-05T19:17:25+00:00'
people:
- Davis Vaughan
- Lionel Henry
- Jenny Bryan
title: tree-sitter-r
website: https://r-lib.github.io/tree-sitter-r/

external:  # updated automatically, do not edit
  description: Tree-sitter grammar for R
  first_commit: '2020-10-29T20:06:05+00:00'
  forks: 37
  languages:
  - R
  last_updated: '2026-02-24T09:26:36.498119+00:00'
  latest_release: '2025-06-05T19:17:25+00:00'
  license: MIT
  people:
  - Davis Vaughan
  - Lionel Henry
  - Jenny Bryan
  repo: r-lib/tree-sitter-r
  stars: 126
  title: tree-sitter-r
  website: https://r-lib.github.io/tree-sitter-r/
---

tree-sitter-r is a grammar for parsing R code using the tree-sitter parsing framework. It enables syntax analysis and code manipulation for R across multiple programming languages.

The grammar is available as bindings for R, Rust, and Node.js, making it accessible across different development environments. It closely follows the official R language specification but treats `]]` as a single literal token rather than two separate tokens, which simplifies working with subset operations and maintains consistency with how other bracket pairs are handled. This deviation from the official R grammar has minimal practical impact since splitting `]]` across lines is extremely rare in real-world R code.
