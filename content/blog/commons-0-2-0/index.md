---
title: commons 0.2.0
date: 2026-11-19
people:
  - Simon Couch
  - Sara Altman
  - Josh Taillon
description: >
  commons 0.2.0 is now available, with one-click Share to Connect, Quarto artifacts, and improved interoperability.
image: kingfisher.jpg
image-alt: >-
  A common kingfisher with a turquoise back and orange breast perched on a
  thin branch against a blurred dark green background.
photo:
  url: https://unsplash.com/photos/selective-focus-photography-of-blue-kingfisher-vUNQaTtZeOo
  author: Vincent van Zalinge
topics:
  - Artificial Intelligence
software:
  - commons
languages:
  - R
  - Python
source: ai
hidesubscription: false
---

We're excited to announce the release of [commons](https://posit-dev.github.io/commons/) 0.2.0. commons is an R and Python package that helps data scientists build trustworthy data analysis agents. Among other things, this release makes commons interoperable with other coding agents and adds two new features to commons apps: Share (to Connect) and Quarto artifacts.

To install the R package from CRAN, run:

``` r
install.packages("commons")
```

It will be a few weeks before the 0.2.0 release of commons is out on PyPI. To install the current version of the Python package, run:

``` py
pip install commons
```

If you're new to commons, the [introductory post](/blog/2026-09-15_commons-0-1-0/) covers the package's design philosophy. This post highlights the biggest changes in 0.2.0; for a full list of changes, see the [NEWS](https://posit-dev.github.io/commons/r/news/index.html#commons-020).

## Interoperability

As we started working on the 0.2.0 release of commons, one of the biggest questions in our minds was how to help folks use commons with other coding agents, like Posit Assistant, Claude Code, or Codex. Relatedly, we wanted commons users to be able to use commons under the hood of other analyses, like Quarto reports and Shiny apps.

In service of this, the `commons()` function was split into two. Calls to `commons()` previously looked like this:

```r
commons <- commons(
  client, 
  data_sources, 
  semantic_layer, 
  context_layer
)
```

This interface coupled two operations that shouldn't have been coupled:

1) The data structure that holds the data sources, semantic layer, and context layer
2) The agent harness that makes that information available to an LLM

`commons()` is now the function used to create the former, while a new function `agent()` is used to create the latter:

```r
commons <- commons(
  data_sources, 
  semantic_layer, 
  context_layer
)
agent <- agent(client, commons = commons)
```

We call that first data structure "the commons." The commons can be used to invoke trusted code and search trusted context directly from R and is intended for use with other coding agents. For example, here's Posit Assistant using the commons underlying the [DevRel Agent](https://github.com/posit-dev/devrel-agent), an agent we use at Posit for answering questions about our open source projects.

<video class="column-page" autoplay loop muted playsinline controls preload="metadata" aria-label="Screen recording of Posit Assistant in Positron answering 'Plot opensource.posit.co traffic over time'. The assistant inspects a commons object, searches its governed metrics and context for web traffic, pulls daily pageviews and visitors, and plots them as a ggplot2 line chart from March through October 2026.">
  <source src="figures/posit-assistant-commons.mp4" type="video/mp4">
</video>

In the above, `devrel` is the commons. The agent runs "normal R code" to interface with it. For coding agents that don't already have a persistent R session, like Claude Code and Codex, we recommend [mcp-console](https://github.com/posit-dev/mcp-console). 

This split into two also means that commons users can use one commons across multiple projects. For example, a commons could be defined in an R package, and then used both in a Shiny app (by invoking the trusted code directly) and in an agent (by calling `agent()` on the commons).

This transition was implemented backward-compatibly; existing calls to `commons()` will raise a deprecation warning with migration instructions. See [`?commons()`](https://posit-dev.github.io/commons/r/reference/commons.html) and the new ["Sharing a commons across projects"](https://posit-dev.github.io/commons/r/articles/sharing.html) vignette to learn more.

## Sharing

On Posit Connect, users can now share conversations, documents, plots, or tables as static content they own. For example, we can click the "Share" button beside plots created with the deployed DevRel Agent and then share a link with collaborators:

<video class="column-page" autoplay loop muted playsinline controls preload="metadata" aria-label="Screen recording of sharing a plot from the DevRel Agent. The user clicks the share button on a bar chart of AI newsletter pageviews by release date, copies a link from the sharing dialog, and opens the shared page, which shows the chart, a collapsed code section, and a note linking back to the DevRel Agent.">
  <source src="figures/devrel-agent-share.mp4" type="video/mp4">
</video>

For plots and tables, the source code for the content is included in the deployed page as well as the date it was created and a link back to the agent where it can be reproduced.

(Since the public-facing deployment of DevRel Agent is publicly available on Posit Connect Cloud rather than internally deployed, that deployment of the agent will not have sharing enabled.)

Existing apps need no changes to enable this feature beyond a redeploy with the new commons version.

## Artifacts

commons agents can now also write self-contained, sharable reports as Quarto documents. 

<video class="column-page" autoplay loop muted playsinline controls preload="metadata" aria-label="Screen recording of the DevRel Agent responding to 'Put this in a sharable document' after producing a pageviews chart. The agent reads up on creating sharable documents, retrieves data, and streams a Quarto document titled 'AI newsletter pageviews by release date' into a drawer beside the chat. Once the document finishes running, a Share button appears.">
  <source src="figures/devrel-agent-artifact.mp4" type="video/mp4">
</video>

When users mention writing reports or creating something sharable, the agent can load an agent skill and then stream document code directly into a chat drawer. Documents get their data by calling `commons()` methods in their code, and they can be shared in the same way plots and tables can be.

## What's next

We're super grateful for all of the feedback since the initial release of commons, and we're excited to have this release out! Only the R side of commons 0.2.0 has been released; keep an eye out in the coming weeks for a release on the Python side with analogous features.

In the coming months, we'll be focused on another substantial commons release. For one, we want to continue making commons apps feel increasingly like modern, powerful chat apps; namely, commons agents should be able to author interactive applications as artifacts. We're also interested in "loops," where a user might be able to e.g. request that some report is recreated and sent to them weekly. If you have thoughts on where you'd like to see commons go, feel free to reach out on our [issue tracker](https://github.com/posit-dev/commons/issues).
