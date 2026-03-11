---
title: R Markdown v0.9.5
people:
  - RStudio Team
date: '2016-03-21'
categories:
- News
- Packages
- R Markdown
slug: rmarkdown-v0-9-5
blogcategories:
- Products and Technology
- Company News and Events
- Open Source
tags:
- Packages
- R Markdown
events: blog
ported_from: rstudio
port_status: raw
---


A new release of the [rmarkdown](https://rmarkdown.rstudio.com/) package is now available on CRAN. This release features some long-requested enhancements to the [HTML document](https://rmarkdown.rstudio.com/html_document_format.html) format, including:

  1. The ability to have a floating (i.e. always visible) table of contents.

  2. Folding and unfolding for R code (to easily show and hide code for either an entire document or for individual chunks).

  3. Support for presenting content within tabbed sections (e.g. several plots could each have their own tab).

  4. Five new themes including "lumen", "paper", "sandstone", "simplex", & "yeti".

There are also three new formats for creating [GitHub](https://rmarkdown.rstudio.com/github_document_format.html), [OpenDocument](https://rmarkdown.rstudio.com/odt_document_format.html), and [RTF](https://rmarkdown.rstudio.com/rtf_document_format.html) documents as well as a number of smaller enhancements and bug fixes (see the package [NEWS](https://cran.r-project.org/web/packages/rmarkdown/NEWS) for all of the details).

### Floating TOC

You can specify the `toc_float` option to float the table of contents to the left of the main document content. The floating table of contents will always be visible even when the document is scrolled. For example:

````
---
title: &quot;Habits&quot;
output:
  html_document:
    toc: true
    toc_float: true
---
````

Here's what the floating table of contents looks like on one of the R Markdown website's pages:

![FloatingTOC](https://rstudioblog.files.wordpress.com/2016/03/screen-shot-2016-03-21-at-7-19-59-am.png)

### Code Folding

When the knitr chunk option `echo = TRUE` is specified (the default behavior) the R source code within chunks is included within the rendered document. In some cases it may be appropriate to exclude code entirely (`echo = FALSE`) but in other cases you might want the code available but not visible by default.

The `code_folding: hide` option enables you to include R code but have it hidden by default. Users can then choose to show hidden R code chunks either indvidually or document wide. For example:

````
---
title: &quot;Habits&quot;
output:
  html_document:
    code_folding: hide
---
````

Here's the default HTML document template with code folding enabled. Note that each chunk has it's own toggle for showing or hiding code and there is also a global menu for operating on all chunks at once.

![Screen Shot 2016-03-21 at 7.27.40 AM](https://rstudioblog.files.wordpress.com/2016/03/screen-shot-2016-03-21-at-7-27-40-am.png)

Note that you can specify `code_folding: show` to still show all R code by default but then allow users to hide the code if they wish.

### Tabbed Sections

You can organize content using tabs by applying the `.tabset` class attribute to headers within a document. This will cause all sub-headers of the header with the `.tabset` attribute to appear within tabs rather than as standalone sections. For example:

````
## Sales Report {.tabset}

### By Product

(tab content)

### By Region

(tab content)
````

Here's what tabbed sections look like within a rendered document:

![Screen Shot 2016-03-21 at 7.43.38 AM](https://rstudioblog.files.wordpress.com/2016/03/screen-shot-2016-03-21-at-7-43-38-am.png)

### Authoring Enhancements

We also shouldn't fail to mention that the [most recent release](https://www.rstudio.com/products/rstudio/download/) of RStudio included several enhancements to R Markdown document editing. There's now an optional outline view that enables quick navigation across larger documents:

![Screen Shot 2015-12-22 at 9.27.34 AM](https://rstudioblog.files.wordpress.com/2015/12/screen-shot-2015-12-22-at-9-27-34-am.png&h=502)

We also also added inline UI to code chunks for running individual chunks, running all previous chunks, and specifying various commonly used knit options:

![Screen Shot 2015-12-22 at 9.30.11 AM](https://rstudioblog.files.wordpress.com/2015/12/screen-shot-2015-12-22-at-9-30-11-am.png&h=800)

### What's Next

We've got lots of additional work planned for R Markdown including new document formats, additional authoring enhancements in RStudio, and some new tools to make it easier to publish and manage documents created with R Markdown. More details to follow soon!

