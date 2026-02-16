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

external:
  contributors:
  - DavisVaughan
  - jimhester
  - kevinushey
  - aspeddro
  - lionel-
  - nokome
  - echasnovski
  - amaanq
  - jennybc
  - rien
  - clason
  - ezradyck
  - hendrikvanantwerpen
  - Beebeeoii
  - mjambon
  - MichaelChirico
  description: Tree-sitter grammar for R
  first_commit: '2020-10-29T20:06:05+00:00'
  forks: 38
  languages:
  - R
  last_updated: '2026-02-13T14:17:20.488123+00:00'
  latest_release: '2025-06-05T19:17:25+00:00'
  license: MIT
  people:
  - Davis Vaughan
  - Lionel Henry
  - Jenny Bryan
  repo: r-lib/tree-sitter-r
  stars: 123
  title: tree-sitter-r
  website: https://r-lib.github.io/tree-sitter-r/
---

tree-sitter-r provides a robust grammar for parsing R code using the Tree-sitter framework, enabling developers to build powerful tools for code analysis, syntax highlighting, and automated refactoring. Whether you're developing editor extensions, building code quality tools, or creating automated documentation systems, this grammar gives you accurate, efficient parsing capabilities that handle R's unique syntax with precision. The parser is designed with cross-platform compatibility in mind, offering native bindings for R, Rust, and Node.js ecosystems.

One of the key advantages of tree-sitter-r is its thoughtful design for working with R's various bracket operators. By treating parentheses, square brackets, and double brackets as consistent literal tokens, the grammar allows developers to handle function calls, subsetting, and other operations uniformly in their syntax trees. This consistency makes it significantly easier to build maintainable code analysis tools without writing special cases for each operator type, streamlining the development of everything from IDE integrations to automated code formatters.
