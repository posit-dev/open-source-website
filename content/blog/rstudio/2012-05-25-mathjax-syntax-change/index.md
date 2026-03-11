---
title: MathJax Syntax Change
people:
  - RStudio Team
date: '2012-05-25'
categories:
- News
slug: mathjax-syntax-change
blogcategories:
- Company News and Events
events: blog
ported_from: rstudio
port_status: raw
---


We've just a made a change to the syntax for embedding MathJax equations in R Markdown documents. The change was made to eliminate some parsing ambiguities and to support future extensibility to additional formats.

The revised syntax adds a "latex" qualifier to the `$` or `$$` equation begin delimiter. It looks like this:

![](https://rstudioblog.files.wordpress.com/2012/05/mathjax_latex_syntax.png)

This change was the result of a few considerations:

  1. Some users encountered situations where the `$equation$` syntax recognized standard text as an equation. There was an escape sequence (`\$`) to avoid this but for users not explicitly aware of MathJax semantics this was too hard to discover.

  2. The requirement to have no space between equation delimiters (`$`) and the equation body (intended to reduce parsing ambiguity) was also confusing for users.

  3. We want to eventually support [ASCIIMath](http://www1.chapman.edu/~jipsen/mathml/asciimath.html) and for this will require an additional qualifier to indicate the equation format.

RStudio v0.96.227 implements the new MathJax syntax and is [available for download](http://www.rstudio.org/download) now.

