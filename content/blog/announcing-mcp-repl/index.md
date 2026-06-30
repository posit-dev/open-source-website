---
title: Announcing mcp-repl
date: 2026-06-30
people:
  - Tomasz Kalinowski
description: >
  A sandboxed R and Python REPL for MCP-capable agents
image: mcp-repl-hex.png
image-alt: >
  Hex logo for mcp-repl showing a robot typing at a terminal inside a
  hexagon outline.
topics:
  - Artificial Intelligence
  - Best Practices
software:
  - mcp-repl
languages:
  - R
  - Python
source: ai
tags:
  - MCP
  - Agents
hidesubscription: false
---

Most AI agents can run code. That is not the same as having a useful R
or Python session.

R and Python work well because they are interactive. A session
accumulates objects, loaded packages, warnings, plots, documentation
lookups, debugging frames, and partial results. When an agent is doing
real data work, that continuity matters.

`mcp-repl` is a new open source MCP server from Posit that gives
MCP-capable agents a private, sandboxed, persistent R or Python REPL.

It is built for model-facing workflows rather than human-facing
consoles. The session keeps state across tool calls, returns plots
through MCP, renders help in-band, supports debugger modes and
stdin-driven nested REPLs, keeps large outputs bounded, and provides
explicit interrupt and reset controls.

The goal is narrow: give agents the interactive affordances that make R
and Python useful for real data work, without turning the runtime into
an unrestricted shell.

## Why agents need more than shell commands

Many agents interact with R and Python through batch commands:

```sh
Rscript -e '...'
python -c '...'
```

That is fine for isolated probes. It is a poor fit for exploratory
analysis, project debugging, and long-running work.

Each command starts over. The agent has to reload data, recreate
objects, re-import packages, re-open files, and reconstruct context
instead of continuing from the previous step.

A terminal session can preserve state, but it usually leaves the agent
with an unstructured stream of text. The agent may need to poll for
output, infer whether the interpreter is ready, guess how to handle
continuation prompts, and work around pagers, plots, help systems, and
debuggers.

`mcp-repl` provides a structured REPL interface for this kind of work.

It keeps the R or Python process alive across tool calls, captures the
parts of the session that matter to the model, and reports when the
interpreter is ready for the next input.

## A typical agent workflow

An agent using `mcp-repl` can move through an analysis in small steps
without restarting the runtime each time.

For example, you might ask an agent to analyze last week's sales data.
The agent can load the data once, inspect the shape and missingness,
compare it to recent history, generate plots, fit a quick model, read
documentation for an unfamiliar function, and refine its findings before
returning a concise report.

The important part is continuity. The agent is not rebuilding the
session at every step. It is working in a live runtime, using the same
objects, package state, plots, and debugging context as it narrows in on
the result.

That makes the interaction look less like repeated command execution and
more like a careful analyst working through a live R or Python session.

## A real REPL, not a prompt parser

`mcp-repl` runs R or Python as a long-lived worker behind an MCP
interface.

The agent sends code through a `repl` tool. The worker evaluates it,
captures useful output, and reports when the interpreter is ready for
the next step.

Because `mcp-repl` owns enough of the REPL loop, it does not need
prompt-string polling, fixed sleeps, or output-timing heuristics. The
server knows when the interpreter is idle and when a result has settled.

That matters for interactive features that batch code runners often
handle poorly:

- continuation prompts
- help pages
- pagers
- plots
- warnings and errors
- R `browser()` sessions
- Python `pdb` sessions
- nested interactive modes

These are normal parts of R and Python work. `mcp-repl` exposes them to
agents through a compact MCP interface instead of forcing the model to
reverse-engineer a terminal transcript.

## Designed for model-facing output

Human terminals and model contexts have different constraints.

A human can scroll through thousands of lines and visually skim. A model
usually needs compact, ordered, bounded output with a clear indication
of what happened and what is available next.

`mcp-repl` is designed around that constraint.

It uses smart echo behavior to avoid cluttering the transcript when the
input is already obvious. It captures plots and returns them through MCP
so vision-capable models can inspect them directly. For non-vision
models, plot files are still available by path.

Large outputs are handled deliberately. Instead of flooding the model
context, `mcp-repl` keeps the tool response short and writes the full
result to a structured bundle containing the transcript and any plot
files. The agent can inspect that bundle on demand.

This keeps ordinary interactions concise while still preserving access
to the full output when it matters.

## Sandboxed by default

Agents can run code quickly and repeatedly. That makes execution policy
part of the product, not an afterthought.

`mcp-repl` runs the backend in a sandbox by default. Network access is
disabled unless configured. Writes are constrained to the workspace and
session temporary paths. On supported platforms, the sandbox is enforced
with OS-level primitives at the process level rather than with prompt
instructions.

The default policy is intentionally useful for project work: the agent
can read and write within the working area, create session temporary
files, generate plots, and run analysis code, but it does not receive an
unrestricted shell by default.

For clients that can provide sandbox metadata, such as Codex, `mcp-repl`
can inherit the client's per-call sandbox policy. For other MCP clients,
it can be configured with an explicit policy such as workspace-write.

## A small MCP surface

The MCP surface is deliberately small.

The core tool is `repl`:

```json
{
  "input": "1 + 1\n",
  "timeout_ms": 10000
}
```

Interrupts and resets are explicit session controls. A Ctrl-C prefix
requests an interrupt and leaves the session running. A Ctrl-D prefix
requests a reset, shuts down the current worker through a bounded
shutdown path, and starts a fresh session.

Keeping the API small is intentional. Most of the complexity belongs
below the interface, where `mcp-repl` supervises worker lifecycle,
sandbox policy, output ordering, image capture, timeouts, interrupts,
resets, and oversized-output bundles.

The agent gets a simple tool. The runtime handles the messy parts.

## What the agent gets

`mcp-repl` exposes the parts of R and Python that matter during
interactive work:

- stateful execution across tool calls
- bounded, model-oriented output
- smart echo behavior for concise transcripts
- plot capture through MCP
- R help, vignettes, and manuals in-band
- Python help through `help()`, `dir()`, and `pydoc`
- support for R `browser()`, Python `pdb`, and nested REPLs like IPython
- structured bundles for oversized output
- explicit interrupt and reset controls
- sandboxed execution by default

These features are not a new programming model. They are the existing R
and Python workflow adapted to an agent interface.

## Where it fits

`mcp-repl` is useful when an MCP-capable agent needs to do R or Python
work with less supervision. It is especially useful for unattended or
lightly supervised workflows, where you launch an agent and come back
later.

Use `mcp-repl` when you want to:

- ask an agent to produce recurring reports, such as analyzing last
  week's sales data, finding what changed, and drafting a report that
  highlights fresh, surprising, or concerning trends
- give an evaluation harness a realistic R or Python runtime for
  measuring agent capability on data-analysis tasks, using tools such as
  [Inspect](https://inspect.aisi.org.uk)
- ask an agent to do initial reconnaissance, such as exploring a
  dataset, checking data quality, identifying strong signals, and
  suggesting the next analyses worth running
- ask an agent to debug an R or Python project, such as reproducing a
  failing package example, inspecting live objects, stepping through the
  debugger, and proposing a minimal fix
- ask an agent to prepare artifacts for review, such as privately
  iterating on analysis code, plots, and summary tables before returning
  final results with caveats

Because the runtime may be used unattended, the sandbox is part of the
core design rather than an optional wrapper around it.

`mcp-repl` is also useful in general-purpose agent harnesses.
MCP-capable tools such as Claude Code and Codex are not primarily built
around data analysis, but they are often used on R and Python projects.
Adding `mcp-repl` gives those agents a live, persistent runtime instead
of only isolated shell commands.

## How it relates to Posit Assistant

`mcp-repl` and Posit Assistant address different parts of AI-assisted
data work.

`mcp-repl` is a plug-in runtime for autonomous or lightly supervised
agents. It works through MCP and gives existing agents a private,
sandboxed R or Python REPL.

Posit Assistant is an integrated, human-in-the-loop product. It combines
a development environment with agent-facing execution support, so the
user and model can work with shared project context.

Both are about making R and Python better environments for AI-assisted
data work. `mcp-repl` focuses on autonomous work in a private runtime.
Posit Assistant focuses on close collaboration between a human and a
model.

## Getting started

Install from PyPI. The package is named `posit-mcp-repl` and exposes the
`mcp-repl` executable:

```sh
pipx install posit-mcp-repl
```

You can also install with `uv`:

```sh
uv tool install posit-mcp-repl
```

Or run it as a one-off command:

```sh
uvx posit-mcp-repl --help
```

You can also install from source with Cargo:

```sh
cargo install --git https://github.com/posit-dev/mcp-repl --locked
```

Prebuilt binaries are available for macOS, Linux, and Windows. On macOS
or Linux, you can install with:

```sh
curl -fsSL https://raw.githubusercontent.com/posit-dev/mcp-repl/main/scripts/install.sh | sh
```

On Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/posit-dev/mcp-repl/main/scripts/install.ps1 | iex
Install-McpRepl
```

The binaries do not bundle R or Python, so install those separately.

Then add `mcp-repl` to your MCP client configuration:

```sh
mcp-repl install
```

By default, this writes entries for both R and Python for supported
clients. You can also target a specific client or interpreter:

```sh
mcp-repl install --client codex
mcp-repl install --client claude
mcp-repl install --client codex --interpreter r
mcp-repl install --client claude --interpreter python
```

Once configured, the MCP client exposes the `repl` tool for running code
in the session. Interrupts and resets are handled through explicit
control prefixes.

## Open source

`mcp-repl` is open source under the Apache-2.0 license.

Project repository:

<https://github.com/posit-dev/mcp-repl>
