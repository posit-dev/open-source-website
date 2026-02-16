---
description: RAG in R
github: tidyverse/ragnar
image: logo.png
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

external:
  contributors:
  - t-kalinowski
  - dfalbel
  - atheriel
  - shikokuchuo
  - Christophe-Regouby
  - gadenbuie
  - howardbaik
  - jeroenjanssens
  - luisDVA
  - mattwarkentin
  - topepo
  - smach
  - Rednose22
  - bowerth
  description: RAG in R
  first_commit: '2025-01-20T19:30:06+00:00'
  forks: 21
  languages:
  - R
  last_updated: '2026-02-13T14:17:09.038949+00:00'
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
  stars: 163
  title: ragnar
  website: http://ragnar.tidyverse.org
---

Ragnar brings Retrieval-Augmented Generation (RAG) workflows to R with a transparent, inspectable approach. Rather than treating RAG as a black box, ragnar provides a complete seven-step pipeline with sensible defaults while giving experienced users precise control over each stage. The package seamlessly converts documents to markdown, chunks text while preserving semantic structure, generates embeddings through major LLM providers (OpenAI, Ollama, Bedrock, Google Vertex, Databricks), and stores everything in DuckDB for optimized retrieval. Whether you're building searchable knowledge bases from documentation or creating AI assistants grounded in domain-specific data, ragnar combines vector similarity search with full-text BM25 search to deliver contextual, cited information.

For data scientists and developers working with large language models, ragnar solves the challenge of augmenting LLM responses with custom data sources. The package integrates directly with ellmer for chat-based retrieval, allowing LLMs to fetch relevant context on-demand during conversations. Every step of the pipeline can be inspected and refined, making it easy to diagnose issues, optimize performance, and ensure your RAG system produces accurate, verifiable results. Whether you're enhancing model responses with internal documentation, research papers, or proprietary datasets, ragnar provides the transparency and flexibility needed for production-ready RAG implementations.
