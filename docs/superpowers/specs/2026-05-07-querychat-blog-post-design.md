# QueryChat Blog Post — Design Spec

## Overview

A blog post that serves as both the proper introduction to QueryChat and a showcase of its new ggsql-powered visualization capability (v0.6.0). The post targets a broad technical audience — data analysts, app developers, and data team leads — by layering accessible vision with technical depth.

## Format

- **File:** `content/blog/querychat/index.md` (plain Markdown, no executable code)
- **Visual assets:** Screenshots and/or GIFs showing QueryChat in action. These will need to be produced separately and added to the post directory.
- **Authors:** TBD (placeholder in frontmatter)
- **Date:** TBD (placeholder in frontmatter)
- **Topics:** TBD (must come from `data/topics.yaml`)
- **Software:** `querychat` (confirm folder exists in `content/software/`)
- **Languages:** R, Python

## Frontmatter

```yaml
title: "Introducing QueryChat: explore your data with natural language and ggsql"
date: YYYY-MM-DD
people:
  - TBD
description: >
  QueryChat lets you filter, query, and now visualize data using natural
  language — powered by SQL and ggsql. A proper introduction to the package
  and a showcase of its new visualization capability.
image: featured.png
image-alt: TBD
topics:
  - TBD
software:
  - querychat
languages:
  - R
  - Python
nohero: false
hidesubscription: false
```

## Structure and Content

### Section 1: Opening (announcement + visual hook)

**Purpose:** Hook the reader, announce what this is, set up the rest of the post.

**Content:**

A short declarative opening paragraph that announces QueryChat — a package for exploring data with natural language, powered by SQL — and immediately pivots to the new visualization capability as the headline. The key sentence: with the latest release, QueryChat can now visualize your data using ggsql, a grammar of graphics for SQL.

Immediately followed by a hero screenshot or GIF: a user asks a natural language question in the chat interface and gets an interactive ggsql-powered chart rendered inline. This is the "wow" moment before anything is explained.

A brief paragraph of context: QueryChat has been around for a while, powering natural language data exploration in Shiny, Streamlit, Gradio, and Dash apps. But it's never had a proper introduction — and with the new visualization capability, now is the perfect time.

**Visual assets needed:** 1 hero screenshot or GIF showing a compelling visualization produced from a natural language question.

**Approximate length:** 3-4 short paragraphs + hero image.

---

### Section 2: The problem / why this matters

**Purpose:** Frame the gap QueryChat fills. Make the reader nod before showing them the solution.

**Content (3-4 paragraphs):**

1. Data exploration today is fragmented. You write SQL to query, export to R/Python to visualize, or use a BI tool that's rigid and opaque. None of these let you fluidly move between filtering, querying, and visualizing in a single conversational interface.

2. LLMs have changed the game for natural language → structured query translation. They're genuinely good at SQL. But most "chat with your data" tools let the LLM run arbitrary code — which is a non-starter for production use. You need safety, auditability, and reproducibility.

3. QueryChat takes a different approach: constrain the LLM to SQL (and now ggsql), executed locally. Every action is a structured query you can inspect, reproduce, and audit. The LLM proposes; your system executes.

**Visual assets needed:** None.

**Approximate length:** 3-4 paragraphs.

---

### Section 3: What is QueryChat?

**Purpose:** The proper introduction. Give the reader a complete mental model.

**Content:**

**What it is:** A package (R and Python) that adds a natural language chat interface to your data app. Users type questions; QueryChat translates them to SQL via an LLM, executes the SQL locally, and returns results.

**Three capabilities, building on each other:**

1. **Filter** — "Show me only rows where region is West and revenue > 100k" → updates the dashboard's underlying data frame. QueryChat has proven useful as a tool for allowing users to filter the data behind a dashboard using natural language.

2. **Query** — "What's the average order size by quarter?" → runs an analytical SQL query, returns results inline in the chat for the LLM to interpret and summarize.

3. **Visualize** (new in v0.6.0) — "Show me a scatter plot of price vs. rating, colored by category" → generates a ggsql query that produces an interactive chart inline in the chat.

**How it works (brief architecture):** QueryChat uses LLM tool calling as its backbone. The LLM never executes anything itself — it proposes a SQL/ggsql statement via a tool call, and the local system executes it. Results flow back to the LLM for interpretation. This architecture is the foundation for safety and auditability (elaborated in Section 6).

**Ecosystem reach:**
- Works with Shiny, Streamlit, Gradio, and Dash — meets developers where they already are.
- Powered by any LLM via chatlas (Python) / ellmer (R) — Claude, GPT, Gemini, open-weight models, enterprise providers (Azure, Bedrock, Vertex). Easy to prototype with one model and deploy with another.
- Connects to real databases (PostgreSQL, BigQuery, SQLite, DuckDB, Snowflake) via SQLAlchemy and Ibis — not just local CSVs.

**Visual assets needed:** 1-2 screenshots showing the chat interface alongside a data table in a dashboard context (the "before visualization" experience — filtering and querying).

**Approximate length:** 5-7 paragraphs + screenshots.

---

### Section 4: Visualization with ggsql (the deep dive / centerpiece)

**Purpose:** The biggest section. Showcase the new visualization capability and make the reader want to try it.

**Content:**

**The unlock:** QueryChat has always been great at filtering and querying. But "show me" questions used to mean tables and numbers. Now, with ggsql, the LLM can express both the data transformation and the visual encoding in a single query. The result is an interactive chart, rendered inline in the chat.

**What is ggsql?** Brief recap for readers who missed the earlier blog post. ggsql is a grammar of graphics implemented in SQL syntax (link to the ggsql blog post for the full story). It extends SQL with `VISUALIZE`, `DRAW`, `SCALE`, `LABEL`, etc. The key insight for QueryChat: the LLM stays in the same language (SQL) it's already good at. It doesn't need to switch to a separate runtime to produce a chart.

**Why ggsql over other approaches?** This is the "grammar of graphics, anyone?" argument. Most BI chat tools produce rigid, canned chart types. ggsql gives the LLM the full expressive power of the grammar of graphics — faceting, layering, custom scales, annotations. It's the difference between a dropdown of chart types and a visualization language. And compared to approaches that have the LLM generate R or Python plotting code, ggsql is safer (no arbitrary code execution) and lighter (no R/Python runtime needed).

**Show it off (2-3 examples of increasing complexity):**

1. A simple ask → a clean chart (bar chart or scatter plot). Show the query that was generated.
2. A more nuanced ask → a richer visualization (faceted, layered, custom scales).
3. An iterative refinement — the user asks a follow-up ("make the dots bigger", "color by region", "add a trend line") and the chart updates. Demonstrates the conversational nature.

Each example shown as a screenshot/GIF with the ggsql query visible (QueryChat has a "Show Query" button on charts).

**LLMs are good at this:** From what we've seen, LLMs translate natural language to ggsql about as well as they do to SQL — which is to say, very well. The structured, declarative nature of both languages plays to LLM strengths. And recent advances in open-weight models are promising — they seem quite capable of exploring tidy data with SQL/ggsql.

**No runtime, no problem:** ggsql is a standalone executable — no R or Python runtime needed to render charts. Charts are Vega-Lite under the hood, so they're interactive (hover, zoom, etc.). The whole stack (DuckDB + ggsql) is remarkably lightweight.

**Visual assets needed:** 3-4 screenshots or GIFs showing the progression from simple to complex visualizations, with queries visible.

**Approximate length:** 8-12 paragraphs + screenshots. This is the longest section.

---

### Section 5: Understanding your data

**Purpose:** Address the accuracy concern — the LLM won't just write *any* SQL, it'll write the *right* SQL for your business.

**Content:**

**The problem:** One of the hardest challenges in "chat with your data" is ensuring the LLM knows how to correctly calculate domain-specific metrics. Column names and types aren't enough. The LLM needs to know that "churn rate" is calculated a specific way, that "active users" has a precise definition, that certain columns should always be filtered before aggregation.

**Three layers of data understanding, from automatic to rich:**

1. **Automatic schema inference** — QueryChat extracts column names, types, numerical ranges, and categorical values (for low-cardinality text columns) from any data source. This is what the LLM gets for free, and it's often enough for straightforward exploration.

2. **Data description** — A generic slot where you provide plain-text context about your data: a data dictionary, metric definitions, column semantics, units, caveats, or any domain knowledge the schema can't express. This works with any data source and is the primary mechanism for improving accuracy on domain-specific questions.

3. **Snowflake Semantic Models** (new in v0.6.0) — The richest version. If semantic metadata exists in your Snowflake dataset — business logic, metric definitions, relationships — QueryChat automatically discovers and incorporates it. No manual configuration needed. This is a game changer for correctness: instead of hoping the LLM infers the right calculation, you're giving it the authoritative definitions from your data team.

**Forward-looking:** This first release of semantic model support targets Snowflake users, but the principle generalizes. We anticipate adding support for more generic semantic layer solutions in the future.

**Visual assets needed:** None required, but a screenshot showing the data description configuration or a before/after comparison of query accuracy with semantic context could be effective.

**Approximate length:** 4-5 paragraphs.

---

### Section 6: Safety, auditability, and trust

**Purpose:** Make the production case. Address "can I actually use this?" head-on.

**Content:**

**SQL as a sandbox:** Every action the LLM takes is a SQL or ggsql query. QueryChat prohibits destructive keywords (INSERT, UPDATE, DELETE, DROP) at the tool level. With appropriate database permissions, destructive operations are impossible. The LLM literally cannot break your data.

**Full auditability:** Every query is visible to the user and logged. There's no black box. You can inspect, reproduce, and share any result. This is a fundamental difference from tools where the LLM runs arbitrary code behind the scenes. All actions are fully auditable and repeatable.

**OpenTelemetry support:** For production deployments, QueryChat benefits from Posit's new OpenTelemetry instrumentation across its stack — ellmer traces LLM calls and tool executions, Shiny traces session activity, DBI traces database queries. Link to the OpenTelemetry blog post. This gives you visibility into user activity, which is critical for building evals and understanding how people are using the tool.

**Open-weight models work:** Recent open-weight models are proving capable at SQL and ggsql generation. Combined with chatlas/ellmer's easy provider switching, you can prototype with a frontier model and deploy with something you host yourself. This matters for data-sensitive environments.

**Visual assets needed:** None required, but a screenshot of an OpenTelemetry trace showing QueryChat activity could be compelling.

**Approximate length:** 4-5 paragraphs.

---

### Section 7: Getting started

**Purpose:** Convert interest into action. Short and direct.

**Content:**

- Install commands for both R and Python
- The simplest possible example: point QueryChat at a data frame, get a chat interface with visualization enabled
- Links to the QueryChat documentation sites (R and Python)
- A forward-looking sentence or two: what's coming next, where the project is headed

**Visual assets needed:** None.

**Approximate length:** 2-3 short paragraphs + install code blocks.

---

## Cross-references to other blog posts

The post should link to:
- The ggsql blog post (`/blog/2026-04-20_ggsql_alpha_release/`) — when introducing ggsql in Section 4
- The OpenTelemetry blog post (`/blog/2026-05-07_opentelemetry/`) — when discussing observability in Section 6

Note: Permalink format is `/blog/YYYY-MM-DD_<folder-name>/`. Both paths verified against existing content.

## Tone and style

- Professional but conversational. Direct and practical — no fluffy intros.
- Lead with declarative statements, not questions or hedges.
- Let screenshots do the heavy lifting in Sections 1 and 4.
- Avoid tutorial-level detail — this is an overview and showcase, not a getting-started guide. Link to docs for that.
- The ggsql post uses an enthusiastic but technically grounded tone ("we are super excited to announce" paired with detailed syntax explanations). This post should have similar energy, especially around the visualization feature.

## Estimated total length

~1500-2000 words of prose (excluding frontmatter and code blocks), plus 5-8 screenshots/GIFs.

## Visual assets summary

| Section | Asset | Description |
|---------|-------|-------------|
| 1 | Hero screenshot/GIF | Compelling visualization from a natural language question |
| 3 | 1-2 screenshots | Chat interface with data table — filtering/querying experience |
| 4 | 3-4 screenshots/GIFs | Progression from simple to complex visualizations with queries visible |
| 5 | Optional screenshot | Data description config or before/after accuracy comparison |
| 6 | Optional screenshot | OpenTelemetry trace of QueryChat activity |

## Open questions

- Exact author list and publication date (to be provided later)
- Topics taxonomy values — available options are: Artificial Intelligence, Best Practices, Community, Data Wrangling, Interactive Apps, Machine Learning, MLOps and Admin, Publishing, Visualization. Likely candidates: "Artificial Intelligence", "Visualization", "Interactive Apps"
- Whether a `software` entry for `querychat` exists in `content/software/`
- Hero image for the post card/thumbnail
- Specific datasets to use in screenshots (should be relatable and visually interesting)
