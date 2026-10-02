---
title: 'Introducing debrief: profiling summaries for AI agents'
date: 2026-06-22T00:00:00.000Z
people:
  - Emil Hvitfeldt
description: >
  debrief turns profvis profiling output into text-based summaries: hotspots,
  call trees, source context, and memory allocations, readable in the terminal
  and consumable by AI agents.
image: featured.png
image-alt: >-
  Hexagon logo for the debrief package: two stylized figures, one whispering to
  the other, with the word DEBRIEF on a patchwork background.
software:
  - profvis
topics:
  - Best Practices
  - Artificial Intelligence
languages:
  - R
source: ai
hidesubscription: false
---


While AI agents are getting better at writing code,
they sometimes struggle with making the code faster.
We have a number of tools at our disposal to do this,
but some of them are not made with AI agents in mind.
The [profvis](https://profvis.r-lib.org/) package is one such example.
The interactive flame graph it produces is fantastic for human eyes,
it allows us to easily see the broad picture while also drilling down into the details.
This is what started the idea for this new package; debrief.
Allowing the AI agent to read the profvis results as text,
thus letting it make more informed decisions about how to optimize the code.

debrief is on CRAN:

``` r
install.packages("debrief")
# or the development version:
pak::pak("r-lib/debrief")
```

## From guessing to measuring

Prompt an AI agent to make your R code faster,
and it will either declare that a bottleneck exists without evidence,
or try to use `Rprof()` directly.
We find that `profvis()` is better and easier to use than `Rprof()` directly,
as it provides a more user-friendly interface and visualizations.
But that interface is designed for human eyes,
not for an LLM reading a transcript.

This is where debrief comes in.
It turns the output of `profvis()` into a text-based summary that can be easily read and understood by AI agents.
Every function is prefixed `pv_` (for profvis) and returns text designed to be read top to bottom:

``` r
library(debrief)

p <- profvis::profvis(slow_function(data))
pv_print_debrief(p)
#> ## PROFILING SUMMARY
#>
#>
#> Total time: 190 ms (19 samples @ 10 ms interval)
#> Source references: available
#>
#>
#> ### TOP FUNCTIONS BY SELF-TIME
#>    110 ms ( 57.9%)  paste
#>     20 ms ( 10.5%)  <GC>
#>     10 ms (  5.3%)  .bincode
#>     10 ms (  5.3%)  any
#>     10 ms (  5.3%)  anyDuplicated.default
#>     10 ms (  5.3%)  apply
#>     10 ms (  5.3%)  rnorm
#>     10 ms (  5.3%)  unlist
#>
#> ### TOP FUNCTIONS BY TOTAL TIME
#>    180 ms ( 94.7%)  FUN
#>    180 ms ( 94.7%)  lapply
#>    180 ms ( 94.7%)  process_data
#>    140 ms ( 73.7%)  summarize_data
#>    110 ms ( 57.9%)  paste
#>     30 ms ( 15.8%)  clean_data
#>     20 ms ( 10.5%)  <GC>
#>     20 ms ( 10.5%)  apply
#>     10 ms (  5.3%)  .bincode
#>     10 ms (  5.3%)  [.data.frame
#>
#> ### HOT LINES (by self-time)
#>    120 ms ( 63.2%)  analysis.R:22
#>                    list(
#>     10 ms (  5.3%)  analysis.R:9
#>                    x <- rnorm(n)
#>
#> ### HOT CALL PATHS
#>
#> 110 ms (57.9%) - 11 samples:
#>     lapply
#>   -> FUN
#>   -> process_data
#>   -> summarize_data (analysis.R:5)
#>   -> paste (analysis.R:22)
#>
#> 10 ms (5.3%) - 1 samples:
#>     base::tryCatch
#>   -> any
#>
#> 10 ms (5.3%) - 1 samples:
#>     lapply
#>   -> FUN
#>   -> process_data
#>   -> clean_data (analysis.R:4)
#>   -> [.data.frame (analysis.R:15)
#>   -> anyDuplicated.default
#>
#> 10 ms (5.3%) - 1 samples:
#>     lapply
#>   -> FUN
#>   -> process_data
#>   -> clean_data (analysis.R:4)
#>   -> cut.default
#>   -> .bincode
#>
#> 10 ms (5.3%) - 1 samples:
#>     lapply
#>   -> FUN
#>   -> process_data
#>   -> clean_data (analysis.R:4)
#>   -> scale.default
#>   -> apply
#>   -> FUN
#>   -> <GC>
#>
#> ### MEMORY ALLOCATION (by function)
#>    51.28 MB paste
#>    10.01 MB anyDuplicated.default
#>     2.90 MB any
#>     1.62 MB rnorm
#>
#> ### MEMORY ALLOCATION (by line)
#>    51.28 MB analysis.R:22
#>             list(
#>     1.62 MB analysis.R:9
#>             x <- rnorm(n)
#>
#> ### Next steps
#> pv_focus(p, "paste")
#> pv_source_context(p, "analysis.R")
#> pv_suggestions(p)
#> pv_help()
```

`pv_print_debrief()` is meant as the first entry point after profiling.
It gives a comprehensive overview of the profile with a number of sections.

- Top functions by self-time and total time
- Hot lines and hot call paths
- Memory allocation by function and by line
- Next steps

Both the hot lines and hot paths sections link back to source references when available,
Especially relevant if the bottleneck is happening in a common function name like `paste()` that is scattered across your package.
With this, we know exactly which `paste()` call is the culprit.

Each function in {debrief} also prints the name of the possible next functions to run,
so the assistant can drill down into the details.

debrief is a new package.
Its output almost certainly isn't part of any model's training data.
And output is also very unlikely to be added,
as profiling code is rarely committed.
This means that the package tries to be self-documenting by design,
With the hope that an AI agent doesn't need to read the documentation to understand how to use it.

## Getting an agent into the session

While you can use debrief with any AI agent,
it works better with agents that keep a persistent R session.
Otherwise, it will need to rerun the profile every time it wants to check the results of an edit.
You also won't be able to take full advantage of the "Next steps" hints,
which are designed to guide the agent through drilling down into the profile.

[Posit Assistant](https://posit.com/assistant) is the easiest way to do this.
It runs in the same session as you, so you can be a bigger part of the process.
The same assistant runs in Positron, RStudio, or the terminal,
so you can profile interactively or drive the whole loop headlessly from the `pa` CLI.

If you aren't using RStudio or Positron, or prefer an agent like Claude Code or Codex,
[mcp-repl](https://github.com/posit-dev/mcp-repl) gives you the same thing.
It's an MCP server that hands any MCP-capable agent a persistent R (or Python) session,
so you can load debrief and run the profiler once, then drill down as needed.

## Trying it out

The point of debrief is to put profiling results in a form an agent can easily interact with,
so it can measure instead of guess and iterate toward faster code.
We have already used it this way:
[tidymodels/textrecipes#309](https://github.com/tidymodels/textrecipes/pull/309)
is a profiling-driven optimization of `step_word_embeddings()`,
where each round of profile, read, change, and re-measure was guided by debrief's summaries.

Install debrief, point an agent at a slow function, and let it profile.
