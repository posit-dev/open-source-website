---
title: "AI Agent-Driven Executive Reports with Quarto: A Mobile Analytics Case Study"
date: 2026-06-03
people:
  - Adrien Sales
description: >
  How I used the HERMES agent (Qwen 3.7 Max via OpenRouter) to drive Quarto and generate
  multi-stakeholder executive reports from DuckDB mobile consumption data — including
  role-playing simulation to tailor the report by persona (CEO, CIO, sysadmin, programmer).
image: "images/featured.png"
image-alt: >-
  A Quarto-generated PDF executive report showing API availability KPIs, a sparkline chart,
  and annotated latency charts for OPT-NC mobile data — produced by the HERMES AI agent.
topics:
  - Artificial Intelligence
  - Publishing
software:
  - quarto
languages: []
source: quarto
tags:
  - ai-agents
  - duckdb
  - executive-report
  - hermes
  - openrouter
---

What if an AI agent could not only answer questions about your data — but also decide *how*
to present those findings to a CEO, a CIO, and a sysadmin, and style the report accordingly?
That's exactly what happened when I entered the [HERMES Dev Challenge](https://dev.to/adriens/i-reverse-engineered-my-mobile-operators-apk-then-hermes-agent-wrote-the-executive-report-2j3o)
with my [Helia Monitor](https://github.com/adriens/helia) project.

## The data setup

[OPT-NC](https://www.opt.nc) is the telecom and postal operator of New Caledonia.
Their mobile offer, Helia, ships an Android app — but it only shows current consumption,
no history. I reverse-engineered the APK to extract the private HTTP calls, then built
a Go CLI that snapshots voice/data/SMS into a local **DuckDB** database every five minutes.

The result: a personal data lakehouse on my laptop, with months of mobile consumption
history, API availability timings, and latency metrics — data the official app never
surfaces.

## Entering the HERMES Dev Challenge

[HERMES](https://github.com/nixiesearch/hermes) is an open-source AI agent framework.
The Dev.to challenge invited participants to push HERMES to its limits.
My angle: skip the usual chatbot demo and go straight to *executive reporting* — have the
agent analyze my Helia data and produce a publication-quality PDF, multi-stakeholder,
with styled charts.

For the model, I chose **Qwen 3.7 Max via [OpenRouter](https://openrouter.ai/)** — a
frontier open model I had never used before. Everything in the video is genuine first-time
discovery: no rehearsal, no cherry-picked prompts.

## From AsciiDoc to Quarto

The first agent-generated report came out as AsciiDoc. Functional, but not what I wanted.
I then switched the challenge target: could HERMES drive **Quarto** to produce something
print-ready?

The answer was yes — and faster than expected.

HERMES autonomously:

1. Discovered my pre-built DuckDB views (`voice_trend`, `api_availability_kpi`, etc.)
2. Wrote the Quarto source, wiring each section to a DuckDB SQL query
3. Rendered the PDF and iterated on styling and theming
4. Annotated the charts — including a bimodal distribution of API response times it
   flagged without being asked

```
{{< video src="https://www.youtube.com/watch?v=Zw-lfNFA0fQ" width="600" >}}
```

## Role-playing simulation to tailor the report

The most unexpected part of the session: role-playing.

I asked HERMES to re-read the report *as* a CEO, then as a CIO, then as a sysadmin,
then as a programmer — and to suggest improvements from each perspective. Each pass
surfaced a genuinely different set of issues:

- **CEO**: "Too many raw numbers. Give me a traffic-light summary."
- **CIO**: "Where is the SLA breach risk? Which service degraded first?"
- **Sysadmin**: "Show me the timeout distribution by hour-of-day, not by day."
- **Programmer**: "The sparkline query doesn't handle NULL gaps correctly."

The agent self-improved across four passes, and the final PDF was structurally different
from the first draft — without me writing a single line of Quarto myself.

## What I discovered in the data

Two findings emerged that I hadn't pre-wired into any view:

1. **Bimodal distribution of API response times** — HERMES spotted a clear two-peak
   distribution in the latency histogram and labeled it in the chart automatically.
2. **Hour-of-day timeout pattern** — a heatmap (GitHub contribution-style) of timeout
   counts by day × hour revealed a recurring early-morning degradation window.

Both appeared because the agent was free to query DuckDB directly, not just read
pre-computed summaries.

## Why Quarto was the right output format

I could have asked for a plain Markdown report or a CSV summary. I chose Quarto because:

- **PDF rendering** is first-class: `quarto render` produces a print-ready document
  with no extra tooling.
- **Parameterization** is natural: each stakeholder section became a Quarto callout or
  tabset, separating audiences within one source file.
- **Theming** is straightforward: HERMES applied a custom SCSS theme and adjusted the
  logo placement in one pass.
- **Portability**: the `.qmd` source + DuckDB file is the complete reproducible artifact.
  Anyone with Quarto and the database can re-render the full report.

The agent never needed to know *how* Quarto works internally — just that
`quarto render index.qmd` produces a PDF. The declarative nature of Quarto's
frontmatter and chunk syntax is exactly what makes it agentic-friendly.

## Results and cost

- **17-page executive PDF**, three stakeholder sections (CEO / CIO / Network Admin)
- **326 LLM requests**, 61.4M tokens
- **$19.57 total cost** on Qwen 3.7 Max via OpenRouter
- Development time: one session, roughly 85 minutes end-to-end (watch the full video above)

For comparison: a consulting firm would charge at minimum a week of work for a comparable
deliverable. The agent produced a first draft in under 20 minutes.

## Try it yourself

- Full article and context: [Dev.to post](https://dev.to/adriens/i-reverse-engineered-my-mobile-operators-apk-then-hermes-agent-wrote-the-executive-report-2j3o)
- Source repo: [github.com/adriens/helia](https://github.com/adriens/helia)
- Live demo (85 min): [YouTube](https://youtu.be/Zw-lfNFA0fQ)

The complete stack — Go CLI + DuckDB + HERMES + Quarto — is open source.
If you have a data source with an API (or a reverse-engineered one), the same pipeline
should work for any periodic consumption or availability dataset.
