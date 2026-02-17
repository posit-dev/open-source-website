---
description: Unicode symbols for CLI applications, with fallbacks
github: r-lib/clisymbols
languages:
- R
people:
- Gábor Csárdi
title: clisymbols
website: ''

external:
  description: Unicode symbols for CLI applications, with fallbacks
  first_commit: '2015-04-14T02:57:39+00:00'
  forks: 2
  languages:
  - R
  last_updated: '2026-02-17T11:32:44.924617+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  repo: r-lib/clisymbols
  stars: 83
  title: clisymbols
  website: ''
---

clisymbols provides a collection of Unicode symbols for R command-line interfaces with automatic ASCII fallbacks for terminals that don't support Unicode. It enables consistent visual feedback across different terminal environments.

The package includes symbols for common UI patterns like checkmarks, crosses, arrows, progress indicators, and status icons. It automatically detects terminal capabilities and substitutes ASCII equivalents when Unicode isn't supported, ensuring your CLI output works reliably across platforms. The symbols are accessed through a simple named list interface.
