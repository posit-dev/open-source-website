---
description: Large language model evaluation for R
github: tidyverse/vitals
image: logo.png
languages:
- JavaScript
latest_release: '2025-12-01T15:34:29+00:00'
people:
- Simon Couch
- Hadley Wickham
- Jeroen Janssens
- Mine Çetinkaya-Rundel
- Tomasz Kalinowski
title: vitals
website: https://vitals.tidyverse.org

external:
  contributors:
  - simonpcouch
  - howardbaik
  - mattwarkentin
  - SokolovAnatoliy
  - hadley
  - bjornkallerud
  - Copilot
  - jeroenjanssens
  - mine-cetinkaya-rundel
  - smach
  - t-kalinowski
  - github-actions[bot]
  description: Large language model evaluation for R
  first_commit: '2025-02-10T16:40:08+00:00'
  forks: 10
  languages:
  - JavaScript
  last_updated: '2026-02-13T14:17:09.054519+00:00'
  latest_release: '2025-12-01T15:34:29+00:00'
  license: NOASSERTION
  people:
  - Simon Couch
  - Hadley Wickham
  - Jeroen Janssens
  - Mine Çetinkaya-Rundel
  - Tomasz Kalinowski
  readme_image: man/figures/logo.png
  repo: tidyverse/vitals
  stars: 52
  title: vitals
  website: https://vitals.tidyverse.org
---

Building AI-powered applications with large language models requires more than just connecting to an API. Vitals is a framework for LLM evaluation in R that helps developers rigorously assess their AI systems before deployment. Whether you're testing different prompt strategies, comparing model performance, or validating that new features improve your application, vitals provides the tools to measure what matters: accuracy, cost, and reliability.

The framework centers on three core components that work together seamlessly. Datasets define your test inputs and expected outputs, solvers wrap your ellmer chats to generate responses, and scorers evaluate how well those responses match your targets. This structured approach makes it straightforward to identify problematic model behaviors, measure the impact of prompt modifications, and compare how different models affect performance metrics and response times. Built as an R-native alternative to Python's Inspect framework, vitals integrates naturally into R-based workflows while maintaining compatibility with Inspect's log viewer format.