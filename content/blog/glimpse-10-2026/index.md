---
title: "posit::glimpse() Newsletter – October 2026"
date: 2026-10-07
people:
  - Isabella Velásquez
description: >
  This edition of the posit::glimpse() newsletter features updates from posit::conf(2026).
image: "glimpse-conf.jpg"
image-alt: "Blue graphic with white text reading 'posit::glimpse() conf(2026) edition' over a faint pattern of data science and coding icons."
topics:
  - Community
software:
languages:
  - R
  - Python
hidesubscription: false
---

Hello, everyone! We’ve officially wrapped up posit::conf(2026), and to everyone who joined us in Houston or online, thank you for making incredible 💙🧡 Between the keynote reveals, lightning talks, and workshops, it was a lot to take in! In this edition, we’ve rounded up all the major news and announcements in one place.

Want to catch up on talks? While we prepare the videos for YouTube, all session recordings are available now on the event portal:

* Register / log in at [conf.posit.co](https://conf.posit.co)
* Go to "Schedule"
* Select any session and click "View recording"

{{< gallery >}}
- file: photos/photo1.jpeg
- file: photos/photo2.jpeg
- file: photos/photo3.jpeg
{{< /gallery >}}


## Announcing the winners of the Posit Impact Awards

We were thrilled to launch the inaugural Posit Impact Awards to celebrate stories of measurable, meaningful change across our community. At posit::conf(2026), we were honored to announce our eight winners, each receiving a conference pass to join us in Houston!

A huge congratulations to all our winners, and a heartfelt thank you for the incredible work you do (and for sharing it with us)!

* Explore their stories in the [2026 Posit Impact Awards](https://posit.co/blog/2026-posit-impact-awards) blog post and join us at the [Data Science Hangout](https://posit.co/data-science-hangout) to hear from other Impact Award winners and nominees featured in the next few weeks.

![Graphic presenting the 2026 Posit Impact Awards winners: Paulo Villarroel (Mission-Critical), Chendi Liao (Transformation), Claudio T. Rebelo (Scale & Reach), Skyler Elmstrom (Resilient Impact), Jon Harmon (Community Builder), Christian Martinez (Open Source), and Amanda Perez & Romina Mir (ROI & Efficiency).](images/impact-awards.jpeg)

## Open Source updates from posit::conf(2026)

### Introducing commons

[commons](https://posit-dev.github.io/commons/) 0.1.0 introduces a new framework for building trustworthy self-service data analysis agents in R and Python. The package implements a three-tier trust labeling system that transparently indicates whether agents invoke trusted code directly, write new code justified by vetted context, or provide untrusted answers. Built on Posit’s LLM stack ([ellmer](https://ellmer.tidyverse.org/), [chatlas](https://posit-dev.github.io/chatlas/), [shinychat](https://posit-dev.github.io/shinychat/)), commons enables teams to convert existing analytical code into AI agent capabilities while maintaining transparency about code sources.

* Learn more about [commons 0.1.0](https://opensource.posit.co/blog/2026-09-15_commons-0-1-0/).
* Join Sara & Simon's virtual webinar on October 28th to learn more about commons. [Register here](https://events.zoom.us/ev/Ajss5j9VeRMe0zw-AtFKf7AUAsthzYhaYjYPeEIu1uYAQe1K0ud1~Agb_hSt1UGxd9fUyIDC32e6jAdEtbl7G_AaLZUYhRvyZR5cGpY5Kp_A0-w?mkt_tok=NzA5LU5YTi03MDYAAAGhT3GTQTQ5s7LDxqZGUAE1zALOLmEDysbAsOyvVdJ9P72DB_IRwtWRTED6kyJA-j-YKF7WxCTY_ZlZ4rTkiyY).

### Quarto Hub

Quarto Hub is a new hosted platform from Posit. In Quarto Hub, you can create, edit, comment on, and publish your [Quarto projects](https://quarto.org/) (single documents, presentations, websites) collaboratively and in real time.

* Watch Carlos Scheidegger's talk, "Quarto Hub: Collaboratively edit, create, and share documents", on the event portal.

<script src="https://fast.wistia.com/player.js" async></script><script src="https://fast.wistia.com/embed/gd8zwcsex7.js" async type="module"></script><style>wistia-player[media-id='gd8zwcsex7']:not(:defined) { background: center / contain no-repeat url('https://fast.wistia.com/embed/medias/gd8zwcsex7/swatch'); display: block; filter: blur(5px); padding-top:56.25%; }</style> <wistia-player media-id="gd8zwcsex7" aspect="1.7777777777777777"></wistia-player>

### skiLift and skiPatrol

Posit has taken over maintenance over two R packages that provide comprehensive tools to work and collaborate within Snowflake’s data platform and ML ecosystem:

* [skiLift](https://github.com/posit-dev/skiLift/): a DBI-compliant Snowflake connector written in R, that authenticates and communicates via the Snowflake SQL API (REST).
* [skiPatrol](https://github.com/posit-dev/skiPatrol[/): an R interface to Snowflake's ML platform: model registry, feature store, experiments, model monitoring, and container services.

Learn more in the [R, meet Snowflake: Introducing Posit’s skiLift and skiPatrol Packages](https://posit.co/blog/r-meet-snowflake-introducing-posits-skilift-and-skipatrol-packages) blog post.

## Even more open source updates

Beyond all the exciting conf news, September was packed with major product updates and community highlights across the board!

### At the database layer

####  ggsql 0.5.0: Readers, Writers, and Beta status

[ggsql](https://ggsql.org/) is a tool that implements a grammar of graphics for SQL, enabling ggplot2-style data visualization directly from database queries. ggsql 0.5.0 reaches beta status with major improvements to database connectivity and rendering capabilities. The release introduces hybrid-reader mode for read-only connections with cache support, replaces the Vega-Lite renderer with a custom writer supporting PNG, JPEG, SVG, and PDF output, and adds rich text support through extended markdown. New features include caption support, minor breaks on scales, and true variable line aesthetics with gradients.

* Read more in the [ggsql 0.5.0: Readers, Writers, and Beta status](https://opensource.posit.co/blog/2026-09-24_ggsql_0_5_0/) blog post.

#### orbital 0.7.0

[orbital](https://orbital.tidymodels.org/) enables the running predictions of tidymodels workflows inside databases. orbital 0.7.0 and tidypredict 1.2.0 massively expand in-database prediction capabilities for tidymodels workflows. The release adds 27 new model/engine combinations including discriminant analysis, naive Bayes, neural networks, SVMs, partial least squares, and ensemble methods. tidypredict now functions as a developer toolkit with new generics for programmatic use, and improved error messaging guides users when probability predictions aren’t available.

* Read more in the [orbital 0.7.0](https://opensource.posit.co/blog/2026-09-09_orbital-0-7-0/) blog post.

### AI-powered R tools

#### ellmer 0.5.0

[ellmer](https://ellmer.tidyverse.org/) makes it easy to use large language models (LLM) from R. ellmer 0.5.0 brings major improvements for working with large language models in R. New file handling functions reduce token costs by efficiently managing documents. The release adds citation tracking from web search tools, token counting for cost prediction, and streaming structured output support. Developer features include `tool_context()` for accessing request metadata and new lifecycle hooks for building agents.

* Read more in the [ellmer 0.5.0](https://opensource.posit.co/blog/2026-09-14_ellmer-0-5-0/) blog post.

#### vitals 0.4.0

[vitals](https://vitals.tidyverse.org/) is a framework for large language model evaluation in R. vitals 0.4.0 brings significant performance improvements and new agent comparison capabilities for LLM evaluation in R. The release includes claude_code() and codex() helpers for benchmarking custom ellmer-built agents against leading coding agents, plus vitals_log_read() for loading log files back into resumable Chat objects. Log files are now ~4x smaller and the log viewer is substantially faster.

* Read more in the [vitals 0.4.0](https://opensource.posit.co/blog/2026-09-03_vitals-0-4-0/) blog post.

### Our stuff is so Shiny

Check out all the major work done by the Shiny team in September!

#### Introducing shinyreact: React UI backed by a Shiny server

[shinyreact](https://posit-dev.github.io/shinyreact/) enables developers to build Shiny applications with React-based UIs while keeping Shiny’s reactive computation on the server. The package provides two primary React hooks for client-server communication, gives access to the entire npm ecosystem of React components, and includes AI Agent Skills for building and converting apps.

* Read more in the [Introducing shinyreact: React UI backed by a Shiny server ](https://opensource.posit.co/blog/2026-09-30_introducing-shinyreact/) blog post.

#### Shiny for Python 1.8

[Shiny for Python](https://shiny.posit.co/py/) 1.8 introduces in-memory server testing without browsers, enabling developers to test reactive logic with pytest using a mock connection. The release adds `ui.page_html()` for using complete HTML documents from bundlers like Vite, and `session.allow_reconnect()` to maintain live sessions after dropped websocket connections. Additional improvements include deprecation of `ui.output_text_verbatim()` in favor of clearer naming, reactive value destruction fixes, and multiple bug fixes for downloads, navsets, and data frames.

* Read more in the [Shiny for Python 1.8](https://opensource.posit.co/blog/2026-09-22_shiny-python-1-8/) blog post.

#### Multiple tables, saved conversations, and take-home dashboards: querychat R 0.4.0 and Python 0.9.0

[querychat](https://posit-dev.github.io/querychat/) facilitates safe and reliable natural language exploration of tabular data, powered by SQL and large language models (LLMs). querychat R 0.4.0 and Python 0.9.0 introduce multiple table support with automatic joins, persistent conversation history across sessions, and the `/handoff` command for exporting chats as downloadable Quarto dashboards, Shiny apps, or marimo notebooks. The release builds on shinychat’s full-page layout with editable messages and file attachments, adds YAML-based data dictionaries for context, and integrates with pins boards for chatting with pinned data.

* Read more in the [Multiple tables, saved conversations, and take-home dashboards: querychat R 0.4.0 and Python 0.9.0](https://opensource.posit.co/blog/2026-09-29_querychat-tables-handoff/) blog post.

#### Complete chat applications in shinychat: R 0.5.0 and Python 0.7.1

[shinychat](https://posit-dev.github.io/shinychat/) provides a Shiny toolkit for building generative AI applications like chatbots and streaming content. shinychat R 0.5.0 and Python 0.7.1 deliver complete chat application capabilities with conversation history, message editing and branching, greetings, file attachments, and slash commands. The new `page_chat()` layout provides full-window interfaces with integrated navigation, tool displays, citations, and artifact previews. Features include persistent conversation storage, search and organization tools, streaming responses with thinking panels, and toolbars for contextual actions.

* Read more in the [Complete chat applications in shinychat: R 0.5.0 and Python 0.7.1](https://opensource.posit.co/blog/2026-09-15_shinychat-r-0.5.0-python-0.7.1/) blog post.

## posit::conf(2027) will be in Seattle, WA from Sept 13-15

Save the date: We're heading back to the Pacific Northwest for posit::conf(2027)! [Subscribe to "Events"](https://posit.co/about/subscription-management) to get notified when registration opens.

In the meantime, join us for our ongoing virtual events:

* [Data Science Hangout](https://pos.it/dsh) for casual conversations with leaders in the data space
* [Data Science Lab](https://pos.it/dslab) for live coding sessions with practitioners building cool things with code

Hope to see you there!
