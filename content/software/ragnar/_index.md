---
color: '#0D1234'
description: RAG in R
github: tidyverse/ragnar
image: logo.png
tags:
- AI
languages:
- R
latest_release: '2026-01-23T17:26:32+00:00'
people:
- Tomasz Kalinowski
- Daniel Falbel
- Charlie Gao
- Garrick Aden-Buie
- Jeroen Janssens
- Max Kuhn
title: ragnar
website: http://ragnar.tidyverse.org

external:  # updated automatically, do not edit
  description: RAG in R
  first_commit: '2025-01-20T19:30:06+00:00'
  forks: 22
  languages:
  - R
  last_updated: '2026-03-05T16:21:51.365574+00:00'
  latest_release: '2026-01-23T17:26:32+00:00'
  license: NOASSERTION
  people:
  - Tomasz Kalinowski
  - Daniel Falbel
  - Charlie Gao
  - Garrick Aden-Buie
  - Jeroen Janssens
  - Max Kuhn
  readme_image: man/figures/logo.png
  repo: tidyverse/ragnar
  stars: 167
  title: ragnar
  website: http://ragnar.tidyverse.org
---

ragnar is an R package for building Retrieval-Augmented Generation (RAG) workflows that provide LLMs with relevant context from document collections. It handles the complete pipeline: converting documents to markdown, chunking text while preserving semantic structure, generating embeddings, storing data in DuckDB, and retrieving relevant chunks based on similarity search or keyword matching.

The package emphasizes transparency and control at each step rather than black-box automation. It supports multiple document formats through MarkItDown, offers configurable chunking strategies that preserve document structure like headings, integrates with popular embedding providers (OpenAI, Ollama, Bedrock, Databricks, Google Vertex), and uses DuckDB's vector similarity search and full-text search for efficient retrieval. ragnar can also equip ellmer Chat objects with retrieval tools, letting LLMs automatically pull relevant information from knowledge stores during conversations.
