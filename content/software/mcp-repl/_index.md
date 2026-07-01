---
color: '#4B5563'
description: Persistent R and Python REPL sessions for coding agents
github: posit-dev/mcp-repl
image: logo.png
languages:
- Rust
- R
- Python
latest_release: '2026-05-18T23:09:38+00:00'
people:
- Tomasz Kalinowski
title: mcp-repl
topics:
- Artificial Intelligence
- Best Practices
website: https://github.com/posit-dev/mcp-repl

include:
  languages:
  - R
  - Python

override:
  description: Persistent R and Python REPL sessions for coding agents
  website: https://github.com/posit-dev/mcp-repl

external:  # updated automatically, do not edit
  description: ''
  first_commit: '2026-02-12T15:26:11+00:00'
  forks: 4
  languages:
  - Rust
  last_updated: '2026-05-20T08:05:17.523929+00:00'
  latest_release: '2026-05-18T23:09:38+00:00'
  license: Apache-2.0
  people:
  - Tomasz Kalinowski
  repo: posit-dev/mcp-repl
  stars: 32
  title: mcp-repl
  website: ''
---

mcp-repl is an MCP server that gives coding agents persistent R and Python sessions across tool calls. It lets an agent load data once, inspect objects, read help, make plots, and keep iterating in a live REPL instead of rebuilding state for every command.

The server is designed for agent workflows that need interactive language features: persistent variables, in-band help, plot capture, interrupts, resets, curated large-output handling, and sandboxed execution.
