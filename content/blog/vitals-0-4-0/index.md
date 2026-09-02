---
title: "vitals 0.4.0"
date: 2026-09-03
people:
  - Simon Couch
description: >
  vitals 0.4.0, a package for LLM evaluation in R, is now on CRAN.
image: "featured.png"
image-alt: >
  The vitals hex sticker, a teddy bear in surgical scrubs holding a stethoscope,
  on a dark green gradient scattered with faint dots that drift upward to the
  right like a positively correlated scatterplot.
topics:
  - Artificial Intelligence
software:
  - vitals
languages:
  - R
source: tidyverse
---

I'm amped as Ella Langley's Gibson to share that [vitals](https://vitals.tidyverse.org/) 0.4.0 is now on CRAN! vitals implements a large language model evaluation toolkit for R, and this release contains several exciting features. 

To install the newest release, run the following in R:

```r
install.packages("vitals")
```

The package includes two new helpers, [`claude_code()`](https://vitals.tidyverse.org/reference/agent_solvers.html) and [`codex()`](https://vitals.tidyverse.org/reference/agent_solvers.html), which allow
you to compare your own ellmer-built agents with leading coding agents. This release also ships another new helper, [`vitals_log_read()`](https://vitals.tidyverse.org/reference/vitals_log_read.html), which supports reading log files back into tibbles, including columns of resumable ellmer Chats. Finally, the release includes several performance improvements; log files are much smaller, and the log viewer that reads them is now substantively faster.

To read the full list of changes, see the [changelog](https://vitals.tidyverse.org/news/index.html#vitals-040).

## Agent solvers

vitals is a port of [Inspect](https://inspect.aisi.org.uk/), a well-adopted Python framework for LLM eval from Posit's own JJ Allaire. One of the concepts that vitals borrows from Inspect is the concept of a "solver," or the LLM-powered system that sets out to solve some task. The simplest solver is just the LLM itself, with no system prompt or tools, like what you'd get from running `chat_anthropic()` from ellmer. Solvers can gain all sorts of prompts and tools, which allows vitals users to test the effect of a change in their prompt or the addition of a new tool.

In the last year or so, the dominant interface to solvers in Inspect has become "agent solvers:" interfaces to the popular coding agents Claude Code and Codex. You call the helper `claude_code()` or `codex()`, and Inspect will proxy traffic through the real coding agent harness.

vitals now has first-class support for these two helpers, allows users to compare their own agents built with ellmer to popular coding agents like Claude Code and Codex. You provide the set of tasks and grading guidance, and vitals will take care of the communication with Inspect.

## Read eval logs back into ellmer Chats

One of the big annoyances I've had in my own usage of vitals is log storage. So that users can use Inspect's log viewer directly, we write evaluation logs to a JSON format that Inspect can read.^[1] However, I often want to write R code against the original R objects—ellmer Chats especially—that the logs were generated from. Loading in the ellmer Chats would especially be helpful for inspecting (ha!) the conversation histories in the same interface that users of the ellmer application would see.

Because of this, I've often saved _both_ the JSON logs and `.rda` logs, the latter of which contain the ellmer Chats. These files are large on their own, and it feels even more silly passing around duplicates of them.

The new release of vitals introduces `vitals_log_read()`, which reads an eval log file back into a tibble of samples. (It's almost exactly what you'd get if you ran the `get_samples()` method on a vitals Task object.) That tibble includes reconstructed solver (and, for model-graded scorers, scorer) chats as ellmer Chat objects. For some providers, the chats will even be resumable; you can load in a solver from a JSON file into an R session and ask that solver a question yourself.

## Performance improvements

The long and the short of this section is just to say that:

1) Logs will take up less storage space than they did before. Roughly, logs written with the new vitals version will be 4x smaller than before, and the magnitude of savings increases with the complexity of the log.
2) We now display logs (with `vitals_view()`) _much_ more quickly. The log viewer should feel very snappy for almost all uses of the package.

I'm really excited to have this release on CRAN! Take it for a spin and let me know if you run into issues on the [package repository](https://github.com/tidyverse/vitals).

[^1]: More exactly, Inspect ships a little JS app that we vendor inside of the vitals package so that it's easier to install.
