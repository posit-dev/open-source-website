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
  contributors:
  - viking
  - spgarbet
  - hadley
  - yihui
  - dupontct
  - MichaelChirico
  - shikokuchuo
  - DavisVaughan
  - szabgab
  - gwarnes-mdsol
  - maelle
  - michaelquinn32
  - reikoch
  - aguynamedryan
  - salim-b
  - wibeasley
  - zkamvar
  - arnaudgallou
  description: R package for converting objects to and from YAML
  first_commit: '2008-04-28T21:52:03+00:00'
  forks: 41
  languages:
  - C
  last_updated: '2026-02-13T14:17:18.356636+00:00'
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

The yaml package provides R bindings to libyaml, a fast YAML parser and emitter that makes it easy to work with YAML data in your R workflows. YAML (YAML Ain't Markup Language) is a human-readable data serialization format widely used for configuration files, data exchange between languages, and storing structured data. Whether you're reading configuration files, exchanging data with other systems, or managing complex nested data structures, yaml seamlessly converts between YAML text and native R objects.

With simple functions like `yaml.load()` and `as.yaml()`, you can parse YAML strings into R lists and vectors, or convert R objects back into YAML format with just a single line of code. The package supports advanced features including custom handlers for special data types, flexible formatting options, and both string-based and file-based operations through convenient `read_yaml()` and `write_yaml()` functions. Built on the robust libyaml library, yaml delivers reliable performance for data scientists and developers who need to work with YAML in their R projects.
