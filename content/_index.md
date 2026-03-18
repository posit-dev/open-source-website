---
title: "Welcome to Posit Open Source"
---

We build open source software for data science, scientific research, and technical communication. Our tools are designed to help you do better work, whether you're analyzing data, building models, creating visualizations, or sharing insights.

{{< button url="about/posit/" text="Learn more about us" icon="boxicons--globe" >}}

## Core projects

We believe powerful data science tools should be open, accessible, and community-driven. That's why our core tools are free and open source, from RStudio IDE and the Tidyverse to Quarto and Positron. We're committed to supporting multiple languages and workflows, because your choice of tools should fit your work, not the other way around.

| Open-source software for R From the tidyverse to tidymodels, we maintain a robust, human-readable ecosystem of R packages and tools. [Learn about our R tools →](about/r) | Open-source software for Python We build native Python libraries that solve challenges in data presentation, interactivity, and more. [Learn about our Python tools →](about/python) |
| :---- | :---- |
| **Technical, scientific publishing** Quarto allows you to create reproducible documents, presentations, and websites with R, Python, Julia, and Observable. [Learn more about Quarto →](software/quarto) | **Web applications for data science** Shiny enables you to build and deploy performant, reactive web applications using R or Python, without requiring web development skills. [Learn more about Shiny for R →](software/shiny-r)  [Learn more about Shiny for Python →](software/shiny-python) |
| **IDEs for data science** RStudio and Positron provide purpose-built environments for code-first data science, analysis, and exploration. [Learn more about RStudio →](software/rstudio/)  [Learn more about Positron →](software/positron) | **AI tools for data science** Leverage AI tools in your data workflow while keeping your results accurate, transparent, and reproducible. [Learn about our AI tools →](about/ai) |

## Featured software

Explore some of our newest and most innovative packages. These tools represent our most significant open-source investments at the moment, and we encourage the community to explore them and help shape their direction!

{{< insert-items >}}
- software/mirai
- software/duckplyr
- software/orbital
{{< /insert-items>}}

{{< button url="/software/" text="Browse all software" icon="boxicons--hexagon-filled" >}}

## Latest from the blog

Recent releases, project deep dives, and updates from across our open-source ecosystem.

{{< query-items path="/blog/.*" sort-by="date" limit="3" cols="3" format="card" >}}

{{< button url="blog" text="Read all blog posts" icon="boxicons--message-filled" >}}

## Upcoming events

Join us at conferences, meetups, and workshops around the world where we share our latest work and connect with the community.

{{< query-items path="^/events/.*" filter=`{">": [{"var": "start_date"}, "$today"]}` sort-by="start_date" sort-direction="ascending" limit="3" cols="3" format="card" hide-badge=true >}}

{{< button url="/events/" text="See all events" icon="boxicons--calendar-event-filled" >}}

## About us

RStudio (now Posit, PBC) was founded in 2009 with the vision of creating high quality open-source software for data scientists. While our scope has expanded far beyond those early days, our core mission has never wavered.

Our open source work is supported by the mission of Posit: we are a PBC that both [sells](https://posit.co/products/enterprise/connect/) [software](https://posit.co/products/enterprise/workbench/) and supports the wider data science community with free software, open access books, and more.

{{< button url="about/posit/" text="Learn more about our mission" icon="boxicons--globe" >}}

The Open Source team is a global team of engineers, educators, and data scientists. We build better tools for data science and participate in the open source community that use them.

{{< button url="/people/" text="Meet the team" icon="boxicons--face-filled" >}}

## Get involved

This website is open source! We welcome contributions, bug reports, and feedback. Your input helps make this resource better for everyone.

{{< button url="https://github.com/posit-dev/open-source-website" text="Contribute on GitHub" icon="simple-icons--github" >}}
