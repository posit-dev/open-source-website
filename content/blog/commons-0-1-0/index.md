---
title: Introducing commons
date: 2026-09-14T13:00:00.000Z
people:
  - Simon Couch
  - Sara Altman
description: >
  Introducing commons 0.1.0, a framework for building AI data analysis agents in
  R and Python.
image: 'commons.png'
image-alt: ''
topics:
  - Artificial Intelligence
languages:
  - R
  - Python
source: ai
hidesubscription: false
---


We're hootin' and hollerin' to share [commons](https://posit-dev.github.io/commons/), an R and Python package that helps data scientists build trustworthy data analysis agents. 

<video class="column-page" autoplay loop muted playsinline controls preload="metadata" aria-label="Screen recording of a commons agent answering 'How is traffic trending for our site?' by running a trusted calculation and displaying a chart showing daily site visits increased 22%.">
  <source src="commons-01-traffic-trend.mp4" type="video/mp4">
  Your browser does not support embedded videos.
</video>

The package is built on [ellmer](https://ellmer.tidyverse.org/), [chatlas](https://posit-dev.github.io/chatlas/), and [shinychat](https://github.com/posit-dev/shinychat/), Posit's open source LLM stack. You can use whatever model you want from any of the providers supported by those packages with it.

To install the R package, run:

``` r
install.packages("commons")
```

To install the Python package from PyPI, run:

``` py
pip install commons
```

Heads up that the Python package is a bit more bleeding-edge than the R release.

## Design philosophy

AI agents for data analysis can range from overly cautious and narrowly correct to wildly untrustworthy. commons increases the likelihood of correct answers by providing agents with access to existing **trusted code**, while still allowing them enough flexibility to answer novel, realistic questions.

If you are a data analyst, data scientist, statistical programmer, or other data practitioner, you likely have a collection of trusted code. This is code that you depend on for your analyses and use to create apps, reports, and packages. The core idea behind commons is that we can improve an agent's correctness by giving it the right access and documentation to run this code.

<style>
.commons-inline-icon {
  display: inline-block;
  height: 1.25em;
  margin: 0 0.08em;
  vertical-align: -0.25em;
  width: 1.25em;
}
</style>

When answering questions, commons agents first search through a pool of trusted code. If the agent finds an appropriate piece of trusted code, it can invoke it directly, and its response will be tagged with a green shield icon <img src="trusted-icon.svg" class="commons-inline-icon" alt="">. If it doesn't, it will search through relevant context before writing its own SQL, R, or Python. If the agent can find trusted context that justifies its approach, it can provide a citation <img src="citation-mark.svg" class="commons-inline-icon" alt=""> to it at the end of its answer, which will be deterministically checked by commons. Otherwise, the answer is marked with a small warning label <img src="warning-icon.svg" class="commons-inline-icon" alt="">.

<img src="trust-flow.svg" class="column-page" alt="Flow diagram. A commons agent searches trusted calculations. If it finds a relevant calculation, it runs the trusted calculation and returns a verified answer. Otherwise, it searches context, writes SQL or R, and returns either a cited or untrusted answer.">

Notably, the agent is not the one deciding which label gets placed on each response. commons determines the label deterministically based on the path the agent takes to get it to its answer.

## Get started

To get started with the R package, check out the [introductory vignette](https://posit-dev.github.io/commons/articles/commons.html). The package ships with an [agent skill](https://posit-dev.github.io/commons/articles/commons.html#working-with-the-agent-skill) that should help you hook your trusted code and context up to the agent.

The Python package is based on the same ideas, so the linked vignette from the R package will give you a sense of where the package is going. (The resulting apps will look _very_ similar regardless of whether you use R or Python—they literally share the same CSS!) Check out the [package README](https://github.com/posit-dev/commons/tree/main/pkg-py) to learn more.
