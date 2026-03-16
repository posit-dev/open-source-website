---
title: New Version of RStudio (v0.96)
people:
  - RStudio Team
date: '2012-05-14'
categories:
- RStudio IDE
slug: rstudio-v096
blogcategories:
- Products and Technology
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: in-progress
---


Today a new version of RStudio (v0.96) is [available for download](http://www.rstudio.org/download/) from our website. The main focus of this release is improved tools for authoring, reproducible research, and web publishing. This means lots of new [Sweave](http://www.statistik.lmu.de/~leisch/Sweave/) features as well as tight integration with the [knitr](http://yihui.name/knitr/) package (including support for creating dynamic web reports with the new R Markdown and R HTML formats).

We've also added some other frequently requested editing features including code folding. Here's a short video demo of the new authoring and web publishing features:

http://vimeo.com/79723940

We're particularly excited about the new possibilities opened up by R Markdown, which make it easier than ever to create web content with R. On June 5th in New York we'll talking about the latest releases of knitr and RStudio with Yihui Xie (knitr) and Jeff Horner (R/Apache and Rook):

<http://www.meetup.com/nyhackr/events/64279002/>

We'll also be announcing some more new stuff at the meetup—hope to see you there!

You can [download RStudio 0.96](http://www.rstudio.org/download/) from our website now. Here's a list of all the new features:

**Sweave / knitr**

  * Spell checking for Sweave and TeX documents.

  * Integrated PDF previewer that supports two-way synchronization ([SyncTeX](http://mactex-wiki.tug.org/wiki/index.php/SyncTeX)) between the editor and PDF view.

  * Support for weaving Rnw files using the [knitr](http://yihui.name/knitr/) package (requires knitr version 0.5 or higher).

  * Parsing of TeX error logs to extract errors, warnings, and bad boxes and present them in a navigable list.

  * Chunk option auto-complete, chunk folding, jump to chunk, and iterative execution of chunks.

  * Compilation based on multiple input files (support for specifying a root TeX document) .

  * TeX formatting commands, block comment/uncomment, and various new compilation options.

**Web Publishing**

  * Editing and previewing R Markdown and R HTML files (like Sweave except for web pages).

  * Creation of easy to distribute standalone HTML files (with embedded images).

  * Support for including LaTeX, ASCIIMath, and MathML equations in web pages using [MathJax](http://www.mathjax.org/).

**Source Editing**

  * Find in files with regular expressions.

  * Code folding (expanding and collapsing regions of code).

  * Automatic comment reflowing (Cmd+Shift+/).

  * Smart editing of Roxygen comments.

  * Syntax highlighting for Markdown, HTML, Javascript, and CSS files.

  * New font customization options.

**Miscellaneous**

  * Fixed incompatibility with Winbind for PAM authentication.

  * Fixed editor cursor off by one line problem that occurred after rapid scrolling.

