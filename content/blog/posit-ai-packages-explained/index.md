---
title: "Posit's AI Packages Explained: A Decision Map for R and Python Developers"
date: 2026-06-08
people:
  - Vedha Viyash
description: >
  Posit has released a wave of AI packages for R and Python. This guide maps
  the ecosystem—from the ellmer/chatlas foundation to higher-level tools—and
  helps you choose what to use based on what you are building.
image: "thumbnail.png"
image-alt: "Title card reading 'Posit's AI Packages Explained: A Decision Map for R and Python Developers' by Vedha Viyash."
topics:
  - Artificial Intelligence
software:
  - ellmer
  - chatlas
  - shinychat
  - querychat
  - ragnar
  - mcptools
  - vitals
  - btw
  - mall
languages:
  - R
  - Python
source: ai
---

Posit has released numerous AI packages recently, creating confusion among developers trying to understand their purpose and relationships. This guide maps out the ecosystem and helps developers choose which tools to use based on their specific needs.

## Foundation Layer: ellmer and chatlas

### ellmer (R)

ellmer provides R developers with a unified interface to multiple LLM providers. Key capabilities include:

- **Single constructor approach**: Use `chat_openai()`, `chat_anthropic()`, `chat_google_gemini()`, `chat_ollama()`, and others
- **Stateful conversations**: Maintains full chat history
- **Tool calling**: Register R functions for LLM invocation
- **Structured extraction**: Define schemas for clean, typed R objects
- **Additional features**: Streaming, async operations, multi-modal input, batch processing, and `live_console()`/`live_browser()` interactive chat

Documentation: [ellmer.tidyverse.org](https://ellmer.tidyverse.org)

### chatlas (Python)

The Python equivalent, designed to maintain feature parity with ellmer:

- Unified interface across providers
- Tool calling via Python function registration, with automatic schema generation from type hints
- Structured output using Pydantic models
- Full async support

Documentation: [posit-dev.github.io/chatlas](https://posit-dev.github.io/chatlas/)

### Choosing between them

Select ellmer for R projects and chatlas for Python. Both packages use consistent conceptual frameworks, making them ideal for projects spanning both languages.

## Higher-Level Tools

### shinychat – chat UI for Shiny

A ready-made chat UI component for Shiny applications (R and Python). Features include:

- Pre-built chat interface, eliminating manual construction
- Streaming response support
- Tool call displays
- Chat history bookmarking

It integrates directly with ellmer/chatlas chat objects.

Documentation: [posit-dev.github.io/shinychat](https://posit-dev.github.io/shinychat/)

### querychat – natural language to SQL

Converts natural language questions into SQL queries for tabular data exploration:

- The LLM generates SQL rather than accessing raw data directly
- Queries execute against local DuckDB instances
- Generated SQL remains visible for user verification
- Multi-framework support: works with Shiny, Streamlit, Gradio, and Dash
- Available for R and Python

Documentation: [posit-dev.github.io/querychat](https://posit-dev.github.io/querychat/)

### ragnar – RAG for R

Implements a Retrieval-Augmented Generation (RAG) pipeline:

- Document ingestion and chunking
- Embedding generation
- DuckDB storage
- Integration with ellmer for tool registration
- Allows LLMs to reference documents during conversations

Documentation: [ragnar.tidyverse.org](https://ragnar.tidyverse.org)

### mcptools – Model Context Protocol

Implements the Model Context Protocol (MCP) for R:

- **Server mode**: Enables MCP-compatible apps (Claude Desktop, VS Code Copilot) to run R code in active sessions
- **Client mode**: Registers third-party MCP servers with ellmer
- Pulls external context into Shiny or querychat applications

Documentation: [posit-dev.github.io/mcptools](https://posit-dev.github.io/mcptools/)

### vitals – LLM evaluation

An evaluation framework for ellmer-powered applications:

- Measure performance across labeled datasets
- Define datasets, solvers (ellmer chats), and scorers
- Track accuracy, cost, and latency
- Interactive result viewer for log exploration

Documentation: [vitals.tidyverse.org](https://vitals.tidyverse.org)

### btw – context toolkit

Connects R environments with LLMs:

- Gathers session context (data frames, package documentation, session info)
- Provides an in-IDE chat assistant
- Recommended MCP server for R via `btw_mcp_server()`

Documentation: [posit-dev.github.io/btw](https://posit-dev.github.io/btw/)

## Specialized and Emerging Tools

- **mall**: Batch NLP operations (sentiment analysis, classification, summarization) across data frame columns (R and Python)
- **Positron Assistant**: AI coding assistant integrated into the Positron IDE, with live session awareness
- **Databot**: Experimental EDA agent for Positron (research preview, not production-ready)
- **shinyrealtime**: Integrates OpenAI's Realtime API with Shiny for voice-enabled applications
- **ggbot2**: Voice assistant for ggplot2 visualization creation (requires an OpenAI API key)
- **chores**: Connects ellmer to editors for automated code transformations
- **gander**: Inline AI code assistance with R environment awareness

## Getting Started: Three Decision Paths

![Layered architecture diagram titled "Building with LLMs in R," grouping the packages by layer: ellmer at the foundation; btw, chores, gander, and chattr as developer tools; shinychat and querychat in the application layer; ragnar and mcptools for knowledge and context; mall and lang for data operations; and vitals for evaluation. Each package shows its version and CRAN status.](decision-map.png "The R + LLM package ecosystem, organized by layer.")

### Path 1: AI inside Shiny dashboards

1. Start with ellmer (R) or chatlas (Python)
2. Add shinychat for the chat interface
3. Optional: add querychat for natural language data queries

### Path 2: chat-with-data (verifiable)

1. Start with querychat standalone
2. It doesn't require ellmer or shinychat initially
3. Scale into Shiny components as needed
4. Also compatible with Streamlit, Gradio, and Dash

### Path 3: context-aware answers from internal documents

1. Use ragnar for building knowledge stores
2. Use ellmer with registered retrieval tools
3. Optional: add mcptools for integrating external services

## Pharma Applications: AI in Clinical Dashboards

Clinical dashboard development benefits significantly from this stack:

- **Data queries**: Clinicians ask questions like "show adverse event rates for the treatment arm in patients over 65" without writing code; querychat translates to SQL and returns verifiable results
- **Document grounding**: ragnar + ellmer combinations retrieve relevant sections from Statistical Analysis Plans, protocol amendments, and SOPs
- **Integrated reporting**: Clinical data, company documents, and validated analytical code work through a unified interface

## Frequently Asked Questions

**Do I need R knowledge to use these packages?**

Most packages are R-first, with some Python availability. Basic familiarity with either language is helpful but not essential for getting started.

**Provider flexibility?**

No vendor lock-in. Both ellmer and chatlas support OpenAI, Anthropic, Google Gemini, Azure OpenAI, AWS Bedrock, Databricks, and Ollama. Switching typically requires a one-line change.

**Production readiness?**

Core packages (ellmer, chatlas, shinychat, querychat, ragnar, vitals) are available on CRAN and actively maintained. mcptools remains experimental, with possible interface changes. Databot is research-preview only.

**Is clinical data safe in regulated environments?**

querychat never sends raw data to LLMs—only schema metadata. The model generates SQL that runs locally. ragnar passes only retrieved text chunks, not full document stores. Organizational data governance policies should guide final decisions.
