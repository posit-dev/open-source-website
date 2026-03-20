---
color: '#E7B10A'
description: Bindings to libxml2
github: r-lib/xml2
image: logo.svg
languages:
- R
latest_release: '2025-03-13T19:24:32+00:00'
people:
- Hadley Wickham
- Jeroen Ooms
- Gábor Csárdi
- Jenny Bryan
- Jeroen Janssens
tags:
- tidyverse
title: xml2
website: https://xml2.r-lib.org/

external:  # updated automatically, do not edit
  description: Bindings to libxml2
  first_commit: '2015-02-12T19:43:52+00:00'
  forks: 83
  languages:
  - R
  last_updated: '2026-03-20T10:27:51.859239+00:00'
  latest_release: '2025-03-13T19:24:32+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Jeroen Ooms
  - Gábor Csárdi
  - Jenny Bryan
  - Jeroen Janssens
  repo: r-lib/xml2
  stars: 223
  title: xml2
  website: https://xml2.r-lib.org/
---

xml2 is an R package that provides bindings to the libxml2 library for working with HTML and XML documents. It offers a jQuery-inspired API for parsing, manipulating, and querying XML/HTML data structures in R.

The package handles memory management automatically, freeing XML documents when they're no longer referenced. It uses a simple class hierarchy with three main types (xml_node, xml_doc, xml_nodeset) and provides convenient namespace handling in XPath expressions. Operations on node sets are vectorized, applying functions across multiple nodes efficiently.
