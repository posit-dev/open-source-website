---
title: 'Announcing RPubs: A New Web Publishing Service for R'
people:
  - RStudio Team
date: '2012-06-04'
categories:
  - Publishing
slug: announcing-rpubs
blogcategories:
  - Company News and Events
ported_from: rstudio
port_status: in-progress
languages: ["R"]
ported_categories:
  - News
tags:
  - RStudio
  - News
---


Today we're very excited to announce [RPubs](http://www.rpubs.com/), a free service that makes it easy to publish documents to the web from R. RPubs is a quick and easy way to disseminate data analysis and R code and do ad-hoc collaboration with peers.

[![](https://rstudioblog.files.wordpress.com/2012/06/rpubs_document.png)](http://rpubs.com/jjallaire/friday-demo)

RPubs documents are based on [R Markdown](http://rstudio.org/docs/authoring/using_markdown), a new feature of knitr 0.5 and RStudio 0.96. To publish to RPubs within RStudio, you simply create an R Markdown document then click the **Publish** button within the HTML Preview window:

![](https://rstudioblog.files.wordpress.com/2012/06/publish_to_rpubs.png)

RPubs documents include a moderated comment stream for feedback and dialog with readers, and can be updated with changes by publishing again from within RStudio.

Note that you'll only see the Publish button if you update to the latest version of RStudio (v0.96.230, [available for download](http://www.rstudio.org/download) today).

## The markdown package

RStudio has integrated support for working with R Markdown and publishing to RPubs, but we also want to make sure that no matter what tools you use it's still possible to get the same results. To that end we've also been working on a new version of the [markdown](http://cran.r-project.org/web/packages/markdown/index.html) package (v0.5, available now on CRAN).

The markdown package provides a standalone implementation of R Markdown rendering that can be integrated with other editors and IDEs. The package includes a function to upload to RPubs, but is also flexible enough to support lots of other web publishing scenarios. We've been working with Jeff Horner on this and he has a more detailed write-up on the [capabilities of the markdown package](http://jeffreyhorner.tumblr.com/post/24404112057/announcing-the-r-markdown-package) on his blog.

## Gallery of examples

We've also published a [gallery of example documents](http://www.rpubs.com/gallery) on RPubs—the gallery illustrates some of the most useful techniques for getting the most out of R Markdown, and includes the following articles:

  * [MathJax and Writing Equations](http://rpubs.com/gallery/equations)

  * [Dynamic Graphics with the googleVis Package](http://rpubs.com/gallery/googleVis)

  * [Customizing Chunk Options](http://rpubs.com/gallery/options)

  * [Caching Code Chunks](http://rpubs.com/gallery/cache)

Let us know what additional examples you'd like to see—we'll be adding more in the weeks ahead.

##

