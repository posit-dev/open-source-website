---
title: "posit::glimpse() Newsletter – September 2026"
date: 2026-09-02
people:
  - Isabella Velásquez
description: >
  Monthly roundup of open source updates from Posit, featuring package releases, new resources, and highlights from upcoming conf talks.
image: "thumbnail.jpg"
image-alt: "A blue background with a repeating pattern of white line drawings of various data-related icons, such as graphs, code symbols, and animals. Centered on the image is the white text 'posit::glimpse()'."
topics:
  - Community
software: []
languages:
  - R
  - Python
hidesubscription: false
---

> Welcome to our newsletter, posit::glimpse()!
>
> If you're currently reading this on our blog, consider subscribing to Product Updates - Open Source on our <a href="https://posit.co/about/subscription-management" target="_blank" rel="noopener">subscription page</a> to receive this newsletter directly in your inbox.

Welcome to this month's roundup of the latest open-source developments from Posit\! Our update list is slightly shorter this time around, because our team is hard at work putting the final touches on [**posit::conf**](https://posit.co/conference/)\!

In this special feature, we are spotlighting a few presentations that will be broadcast live throughout the conference. Be sure to [**register today**](https://conf.posit.co/2026/registration/) if you'd like to tune in live. And, if you enjoy being chronically online like me, I'll be hanging out in the Discord community server throughout the event, alongside your 1000+ closest data pals 👾

## Key product updates and new releases

### Positron August Release Highlights

The [Positron](https://positron.posit.co/) 2026.08 Release blog post highlights several key updates and improvements to Posit’s next-generation data science IDE, including expanded Data Connections (preview), more polished Quarto inline output, centralized AI provider configuration, and performance and reliability upgrades.

* Read more in the [Positron August Release Highlights](/blog/2026-08-13_positron-2026-08-release/) blog post.

### Kimi K3 and GLM 5.2 are now in Posit AI

Posit has added two new open-weights models, Kimi K3 and GLM 5.2, to the [Posit AI](https://posit.ai) platform. Both models stream tokens nearly twice as fast as Anthropic’s models in internal testing and offer lower cost-per-token rates (partly due to more efficient tokenizers and no extra charge for cache writes).

* Read more in the [Kimi K3 and GLM 5.2 are now in Posit AI](/blog/2026-08-10_kimi-k3-glm-5-2-posit-ai/) blog post.
* Learn how to pick your models in the [AI Newsletter: How to choose a model](/blog/2026-08-14_ai-newsletter/) blog post.

### cuda.ml 0.4.0

[cuda.ml](https://mlverse.github.io/cuda.ml/) is an R package that brings [NVIDIA GPU-accelerated machine learning](https://docs.nvidia.com/cuml/) directly to R workflows. This release introduces streamlined setup and developer experience and expanded tree-ensemble inference.

* Read more in the [cuda.ml 0.4.0: GPU-accelerated machine learning from R](/blog/2026-08-21_cuda-ml-0-4-0/) blog post.

### Orbital 0.6.0

[Orbital](https://posit-dev.github.io/orbital/) converts Scikit-learn pipelines into SQL queries so that they can run in your database. Orbital 0.6.0 adds PyTorch neural network support, enabling trained torch.nn.Sequential models to compile directly to SQL for database-native inference without requiring a Python runtime, ONNX Runtime, or separate model server.

* Read more in the [Neural networks in Orbital for Python 0.6.0: PyTorch straight to your database](/blog/2026-08-17_pyorbital-0-6-0/) blog post.

### recipes 1.4.0

[recipes](https://recipes.tidymodels.org/) lets you create a pipeable sequence of feature engineering steps. Recipes 1.4.0 introduces a new way to look inside a recipe partway through, a substantial speedup for steps that are applied to many columns, and multi-column support in `step_regex()` and `step_count()`.

* Read more in the [recipes 1.4.0](/blog/2026-08-26_recipes-1-4-0/) blog post.

### themis 1.1.0

[themis](https://themis.tidymodels.org/) contains extra steps for the recipes package for dealing with unbalanced data. Version 1.1.0 adds eleven new sampling steps for handling unbalanced data. It also adds setting sampling targets per class and more distance metrics.

* Read more in the [themis 1.1.0](/blog/2026-08-13_themis-1-1-0/) blog post.

## New cheatsheets

We’ve refreshed our cheatsheets page, which now features three brand-new additions\!

* **Python Polars:** Developed in partnership with Polars, Inc., this cheatsheet introduces Polars core concepts and key expressions.
* **tidymodels:** Updated cheatsheets detailing practical workflows across the entire tidymodels ecosystem.
* **yardstick:** Guidance on using yardstick within tidymodels to evaluate model predictive performance.

Check them below:

{{< insert-items format="card" hide-badge=true >}}
- resources/cheatsheets/polars/
- resources/cheatsheets/ml-tidymodels/
- resources/cheatsheets/ml-measure-performance/
{{< /insert-items>}}

## posit::conf(2026) talk sneak peeks

With over 100 talks, it’s impossible to feature all of them in this newsletter (but you can explore the complete lineup on the [event schedule](https://conf.posit.co/2026/sessions/)\!). I wanted to give a quick preview of topics you can look forward to (whether you tune in live during the conference or catch up on demand).

1. ### Positron in prime time

It’s been about two years since the public release of Positron, and 🎵this IDE is on fire 🎵

The lineup of conf talks proves it. From Quarto notebooks in Positron (did you know [inline output is available](https://positron.posit.co/quarto-inline-output.html)?!), to using Positron in education, to how it treats SQL as a first-class language, to delightful workflows in Python and R, come see what people are cooking up with Positron.

2. ### What can’t you do with Quarto?

The best way of discovering what Quarto can do is seeing how others are using it\!

We’re starting off strong, with the first session of Virtual Day (September 14th) being “Quarto, R \+ Python”, where Björn Fisseler will discuss creating accessible reports and Wasim Lorgat sharing the history of notebooks. The Quarto theme continues on the 15th and 16th with talks on designing influential and scalable reports, creating learning ecosystems, teaching bilingual data science, developing wiki chatbots, and developing unreasonably effective dashboards and slides — all in Quarto.

3. ### I’ll definitely be joining…

   * **Positron and the Three Bears: Teaching Python with Positron** (presented by Marc Dotson) \- Practical lessons from an educator navigating Python instruction and finding the sweet spot with Positron
   * **First Impressions Matter: Styling Data Products That People Actually Want to Use** (presented by Shelby Level) \- Shelby creates visually striking data products, and I can’t wait to pick up some design inspiration and techniques from her session
   * **A Grammar of Graphics for SQL** (presented by Thomas Lin Pedersen) \- We’ll hear the developer of ggsql share the story of bringing ggplot2-style visualization concepts to SQL
   * **Outgrowing Spreadsheets: Rebuilding Research Data Collection with Shiny and Posit Connect** (presented by Kelsey Chalmers) \- Kelsey shares the before-and-after architecture and how their research team transformed a fragile, spreadsheet-based data collection process into a sustainable system using Shiny and Posit Connect

Of course, this is just the tip of the conf iceberg. One of my favorite things about conf is the diversity of talks, from real-world data science implementation, to insights from the field, to creative and whimsical experiments. I hope to [see you there](https://conf.posit.co/2026/registration/)\!

If you can’t wait til conf (or if you’re reading after conf is over\!), there are other events that you can join us at:

* [Data Science Lab](https://pos.it/dslab), every Tuesday at 12pm ET
* [Data Science Hangout](https://pos.it/dsh), every Thursday at 12pm ET
* [Building Repeatable AI Workflows with Custom MCP Servers](https://events.zoom.us/ev/Ajss5j9VeRMe0zw-AtFKf7AUAsthzYhaYjYPeEIu1uYAQe1K0ud1~Agb_hSt1UGxd9fUyIDC32e6jAdEtbl7G_AaLZUYhRvyZR5cGpY5Kp_A0-w?mkt_tok=NzA5LU5YTi03MDYAAAGhT3GTQTQ5s7LDxqZGUAE1zALOLmEDysbAsOyvVdJ9P72DB_IRwtWRTED6kyJA-j-YKF7WxCTY_ZlZ4rTkiyY), September 30
* [Our next conference appearance](https://opensource.posit.co/events/)

Have a lovely September, and reach out anytime\! isabella \[dot\] velasquez \[at\] posit \[dot\] co
