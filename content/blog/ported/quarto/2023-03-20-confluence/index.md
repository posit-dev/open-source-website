---
title: Confluence Publishing
subtitle: Publish from Quarto to Confluence
description: >
  Quarto 1.3 adds support for publishing individual documents, and projects
  containing many documents to Atlassian Confluence.
topics:
  - Publishing
people:
  - Charlotte Wickham
date: '2023-03-20'
image: confluence-logo-gradient-blue-attribution_rgb@2x.png
image-alt: Atlassian Confluence Logo
ported_from: quarto
source: quarto
port_status: review
software:
  - quarto
languages:
  - R
  - Python
  - Julia
ported_categories:
  - Features
  - Authoring
  - Quarto 1.3
tags:
  - Quarto
  - Features
  - Authoring
  - Quarto 1.3
slug: confluence
---


<div class="callout callout-note" role="note" aria-label="Note">
<div class="callout-header">
<span class="callout-title">Quarto 1.3 Feature</span>
</div>
<div class="callout-body">

This post is part of a series highlighting new features in the 1.3 release of Quarto. Get the latest release the [download page](https://quarto.org/docs/download/)

</div>
</div>

[Atlassian Confluence](https://www.atlassian.com/software/confluence) is a publishing platform for supporting team collaboration. Confluence has a variety of hosting options which include both free and paid subscription plans.

Quarto 1.3 adds support for publishing individual documents, as well as projects composed of multiple documents into [Confluence Spaces](https://support.atlassian.com/confluence-cloud/docs/use-spaces-to-organize-your-work/).

<div class="grid gap-12 items-start md:grid-cols-2">
<div class="prose max-w-none">

<figure>
<img src="images/confluence-qmd.png" data-fig-alt="A screenshot of a Quarto document with the title Using R - Doc in the RStudio Editor." alt="A Quarto Document" />
<figcaption aria-hidden="true">A Quarto Document</figcaption>
</figure>

</div>
<div class="prose max-w-none">

<figure>
<img src="images/confluence-page.png" data-fig-alt="A screenshot of a document with the title Using R - Doc in a Confluence Space." alt="Published to Confluence" />
<figcaption aria-hidden="true">Published to Confluence</figcaption>
</figure>

</div>
</div>
<div class="grid gap-12 items-start md:grid-cols-[800fr_969fr]">
<div class="prose max-w-none">

<figure>
<img src="images/confluence-project.png" data-fig-alt="A screenshot of a Quarto project in VS Code. On the left in the Explorer, the project folder is called &#39;Guide-site&#39;, and contains folders &#39;authoring&#39;, and &#39;computation&#39;, along with some other files. A document from the folder &#39;python&#39; inside the folder &#39;computations&#39; with the title &#39;Using Python - site&#39; is open in the Source Pane. " alt="A Quarto Project" />
<figcaption aria-hidden="true">A Quarto Project</figcaption>
</figure>

</div>
<div class="prose max-w-none">

<figure>
<img src="images/confluence-site.png" data-fig-alt="A screenshot of Space in Confluence. On the left in the Sdiebar under Pages is a page called &#39;Guide-site&#39;. Nested under this page are pages called &#39;authoring&#39;, and &#39;computation&#39;, along with some other pages. The &#39;computation&#39; page item is expanded and shows a page called &#39;Using Python - site&#39;, nested under a page called &#39;python&#39;. A page is displayed on the right with the title &#39;Using Python - site&#39;" alt="Published to Confluence" />
<figcaption aria-hidden="true">Published to Confluence</figcaption>
</figure>

</div>
</div>

Managing Confluence content with Quarto allows you to author content in Markdown, manage that content with your usual version control tools like Git and GitHub, and leverage Quarto's tools for including computational output.

<!-- Quick overview of key features: new format and project type, local preview, `quarto publish confluence`. -->

If you're curious about using Confluence Publishing for your own project, head to the [Confluence Publishing page](https://quarto.org/docs/publishing/confluence.html) of the pre-release highlights to learn more.
