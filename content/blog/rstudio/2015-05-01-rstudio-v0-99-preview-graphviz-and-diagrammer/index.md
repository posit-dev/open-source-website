---
title: 'RStudio v0.99 Preview: Graphviz and DiagrammeR'
people:
  - RStudio Team
date: '2015-05-01'
categories:
- RStudio IDE
slug: rstudio-v0-99-preview-graphviz-and-diagrammer
blogcategories:
- Products and Technology
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: raw
---


Soon after the announcement of [htmlwidgets](http://www.htmlwidgets.org/), Rich Iannone released the [DiagrammeR](http://rich-iannone.github.io/DiagrammeR/) package, which makes it easy to generate graph and flowchart diagrams using text in a Markdown-like syntax. The package is very flexible and powerful, and includes:

  1. Rendering of [Graphviz](http://en.wikipedia.org/wiki/Graphviz) graph visualizations (via [viz.js](https://github.com/mdaines/viz.js/))

  2. Creating diagrams and flowcharts using [mermaid.js](http://knsv.github.io/mermaid/)

  3. Facilities for mapping R objects into graphs, diagrams, and flowcharts.

We're very excited about the prospect of creating sophisticated diagrams using an easy to author plain-text syntax, and built some special authoring support for DiagrammeR into RStudio v0.99 (which you can download a [preview release](https://www.rstudio.com/products/rstudio/download/preview/) of now).

### Graphviz Meets R

If you aren't familiar with Graphviz, it's a tool for rendering [DOT](http://en.wikipedia.org/wiki/DOT_(graph_description_language)) (a plain text graph description language). DOT draws directed graphs as hierarchies. Its features include well-tuned layout algorithms for placing nodes and edge splines, edge labels, "record" shapes with "ports" for drawing data structures, and cluster layouts (see <http://www.graphviz.org/pdf/dotguide.pdf> for an introductory guide).

DiagrammeR can render any DOT script. For example, with the following source file ("boxes.dot"):

![Screen Shot 2015-04-30 at 12.35.17 PM](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-30-at-12-35-17-pm.png)

You can render the diagram with:

```r
library(DiagrammeR)
grViz("boxes.dot")
```

![grviz-viewer](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-30-at-12-31-11-pm.png)

Since the diagram is an [htmlwidget](http://www.htmlwidgets.org) it can be used at the R console, within R Markdown documents, and within Shiny applications. Within RStudio you can preview a Graphviz or mermaid source file the same way you source an R script via the **Preview** button or the **Ctrl+Shift+Enter** keyboard shortcut.

This simple example only scratches the surface of what's possible, see the [DiagrammeR Graphviz documentation](http://rich-iannone.github.io/DiagrammeR/graphviz.html) for more details and examples.

### Diagrams with mermaid.js

Support for [mermaid.js](http://rich-iannone.github.io/DiagrammeR/mermaid.html) in DiagrammeR enables you to create several other diagram types not supported by Graphviz. For example, here's the code required to create a sequence diagram:

![sequence](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-30-at-1-31-11-pm.png)

You can render the diagram with:

```r
library(DiagrammeR)
mermaid("sequence.mmd")
```

![sequence-viewer](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-30-at-2-08-27-pm1.png)

See the [DigrammeR mermaid.js documentation](http://rich-iannone.github.io/DiagrammeR/mermaid.html) for additional details.

### Generating Diagrams from R Code

Both of the examples above illustrating creating diagrams by direct editing of DOT and mermaid scripts. The latest version of DiagrammeR (v0.6, just released to CRAN) also includes facilities for generating diagrams from R code. This can be done in a couple of ways:

  1. Using text substitution, whereby you create placeholders within the diagram script and substitute their values from R objects. See the documentation on [Graphviz Substitution](https://github.com/rich-iannone/DiagrammeR#graphviz-substitution) for more details.

  2. Using the [graphviz_graph](https://github.com/rich-iannone/DiagrammeR#using-data-frames-to-define-graphviz-graphs) function you can specify nodes and edges directly using a data frame.

Future versions of DiagrammeR are expected to include additional features to support direct generation of diagrams from R.

### Publishing with DiagrammeR

Diagrams created with DiagrammeR act a lot like R plots however there's an important difference: they are rendered as HTML content rather than using an R graphics device. This has the following implications for how they can be published and re-used:

  1. Within RStudio you can save diagrams as an image (PNG, BMP, etc.) or copy them to clipboard for re-use in other applications.

  2. For a more reproducible workflow, diagrams can be embedded within R Markdown documents just like plots (all of the required HTML and JS is automatically included). Note that because the diagrams depend on HTML and JavaScript for rendering they can only be used in HTML based output formats (they don't work in PDFs or MS Word documents).

  3. From within RStudio you can also publish diagrams to [RPubs](http://www.rpubs.com) or save them as standalone web pages.

![diagrammer-publish](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-30-at-2-18-12-pm.png)

See the [DiagrammeR documentation on I/O](http://rich-iannone.github.io/DiagrammeR/io.html) for additional details.

### Try it Out

To get started with DiagrammeR check out the excellent collection of demos and documentation on the [project website](http://rich-iannone.github.io/DiagrammeR/). To take advantage of the new RStudio features that support DiagrammeR you should download the latest [RStudio v0.99 Preview Release](https://www.rstudio.com/products/rstudio/download/preview/).

