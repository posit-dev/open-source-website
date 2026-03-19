---
title: R Markdown Custom Formats
people:
  - RStudio Team
date: '2016-03-21'
categories:
- Packages
- R Markdown
slug: r-markdown-custom-formats
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
- R Markdown
ported_from: rstudio
port_status: in-progress
software: ["rmarkdown"]
languages: ["R"]
---


The R Markdown package ships with a raft of output formats including HTML, PDF, MS Word, R package vignettes, as well as Beamer and HTML5 presentations. This isn't the entire universe of available formats though (far from it!). R Markdown formats are fully extensible and as a result there are several R packages that provide additional formats. In this post we wanted to highlight a few of these packages, including:

  * [tufte](http://rstudio.github.io/tufte/) — Documents in the style of Edward Tufte

  * [rticles](https://github.com/rstudio/rticles) — Formats for creating LaTeX based journal articles

  * [rmdformats](https://github.com/juba/rmdformats) — Formats for creating HTML documents

We'll also discuss how to create your own custom formats as well as re-usable document templates for existing formats.

### Using Custom Formats

Custom R Markdown formats are just R functions which return a definition of the format's behavior. For example, here's the metadata for a document that uses the `html_document` format:

````
---
title: "My Document"
output: html_document
---
````

When rendering, R Markdown calls the `rmarkdown::html_document` function to get the definition of the output format. A custom format works just the same way but is also qualified with the name of the package that contains it. For example, here's the metadata for a document that uses the `tufte_handout` format:

````
---
title: "My Document"
output: tufte::tufte_handout
---
````

Custom formats also typically register a template that helps you get started with using them. If you are using RStudio you can easily create a new document based on a custom format via the **New R Markdown** dialog:

![Screen Shot 2016-03-21 at 11.16.04 AM](https://rstudioblog.files.wordpress.com/2016/03/screen-shot-2016-03-21-at-11-16-04-am.png)

### Tufte Handouts

The [tufte](http://rstudio.github.io/tufte/) package includes custom formats for creating documents in the style that [Edward Tufte](http://www.edwardtufte.com/tufte/) uses in his books and handouts. Tufte's style is known for its extensive use of sidenotes, tight integration of graphics with text, and well-set typography. Formats for both LaTeX and HTML/CSS output are provided (these are in turn based on the work in [tufte-latex](https://github.com/tufte-latex/tufte-latex) and [tufte-css](https://github.com/edwardtufte/tufte-css)). Here's some example output from the LaTeX format:

![](https://rmarkdown.rstudio.com/images/tufte-handout.png)

If you want LaTeX/PDF output, you can use the `tufte_handout` format for handouts and `tufte_book` for books. For HTML output, you use the `tufte_html` format. For example:

````
---
title: "An Example Using the Tufte Style"
people:
output:
  tufte::tufte_handout: default
  tufte::tufte_html: default
---
````

You can install the tufte package from CRAN as follows:

````
install.packages("tufte")
````

See the [tufte package website](http://rstudio.github.io/tufte/) for additional documentation on using the Tufte custom formats.

### Journal Articles

The **rticles** package provides a suite of custom [R Markdown](https://rmarkdown.rstudio.com/) LaTeX formats and templates for various journal article formats, including:

  * [JSS](http://www.jstatsoft.org/) articles

  * [R Journal](http://journal.r-project.org/) articles

  * [CTeX](http://ctex.org/) documents

  * [ACM](http://www.acm.org/) articles

  * [ACS](http://pubs.acs.org/) articles

  * [Elsevier](https://www.elsevier.com/) journal submissions.

![Screen Shot 2016-03-21 at 11.48.40 AM](https://rstudioblog.files.wordpress.com/2016/03/screen-shot-2016-03-21-at-11-48-40-am.png)

You can install the [rticles](https://github.com/rstudio/rticles) package from CRAN as follows:

````
install.packages("rticles")
````

See the [rticles repository](https://github.com/rstudio/rticles) for more details on using the formats included with the package. The [source code](https://github.com/rstudio/rticles/tree/master/R) of the rticles package is an excellent resource for learning how to create LaTeX based custom formats.

### rmdformats Package

The [rmdformats](https://github.com/juba/rmdformats) package from Julien Barnier includes three HTML based document formats that provide nice alternatives to the default html_document format that is included in the rmarkdown package. The `readthedown` format is inspired by the [Read the docs](https://readthedocs.org/) Sphinx theme and is fully responsive, with collapsible navigation:

![readthedown](https://rstudioblog.files.wordpress.com/2016/03/readthedown.png)

The `html_docco` and `html_clean` formats both provide provide automatic thumbnails for figures with lightbox display, and html_clean provides an automatic and dynamic table of contents:

![html_docco](https://rstudioblog.files.wordpress.com/2016/03/html_docco.png) ![html_clean](https://rstudioblog.files.wordpress.com/2016/03/html_clean.png)

You can install the [rmdformats](https://github.com/juba/rmdformats) package from CRAN as follows:

````
install.packages("rmdformats")
````

See the [rmdformats repository](https://github.com/juba/rmdformats) for documentation on using the `readthedown`, `html_docco`, and `html_clean` formats.

### Creating New Formats

Hopefully checking out some of the custom formats described above has you inspired to create your very own new formats. The R Markdown website includes documentation on [how to create a custom format](https://rmarkdown.rstudio.com/developer_custom_formats.html). In addition, the source code of the [tufte](https://github.com/rstudio/tufte), [rticles](https://github.com/rstudio/rticles), and [rmdformats](https://github.com/juba/rmdformats) packages provide good examples to work from.

Short of creating a brand new format, it's also possible to create a re-usable document template that shows up within the RStudio **New R Markdown** dialog box. This would be appropriate if an existing template met your needs but you wanted to have an easy way to create documents with a pre-set list of options and skeletal content. See the article on [document templates](https://rmarkdown.rstudio.com/developer_document_templates.html) for additional details on how to do this.

