---
title: R Notebooks
people:
  - Jonathan McPherson
date: '2016-10-05'
categories:
- R Markdown
- RStudio IDE
slug: r-notebooks
blogcategories:
- Products and Technology
- Open Source
tags:
- R Markdown
- RStudio IDE
events: blog
ported_from: rstudio
port_status: raw
---


Today we're excited to announce [R Notebooks](https://rmarkdown.rstudio.com/r_notebooks.html), which add a powerful notebook authoring engine to [R Markdown](https://rmarkdown.rstudio.com/). Notebook interfaces for data analysis have compelling advantages including the close association of code and output and the ability to intersperse narrative with computation. Notebooks are also an excellent tool for teaching and a convenient way to share analyses.

![screen-shot-2016-09-21-at-3-42-44-pm](https://rstudioblog.files.wordpress.com/2016/09/screen-shot-2016-09-21-at-3-42-44-pm.png)

You can try out R Notebooks today in the [RStudio Preview Release](https://www.rstudio.com/products/rstudio/download/preview/).

## Interactive R Markdown

As an authoring format, R Markdown bears many similarities to traditional notebooks like [Jupyter](https://jupyter.org/) and [Beaker](http://beakernotebook.com/). However, code in notebooks is typically executed interactively, one cell at a time, whereas code in R Markdown documents is typically executed in batch.

R Notebooks bring the interactive model of execution to your R Markdown documents, giving you the capability to work quickly and iteratively in a notebook interface without leaving behind the plain-text tools and production-quality output you've come to rely on from R Markdown.

<table style="color:#808080;border:1px solid #d0d0d0;padding:2px;margin-top:15px;margin-bottom:15px;" >
<tbody >
<tr >

R Markdown Notebooks
Traditional Notebooks
</tr>
<tr >

<td style="text-align:left;" >Plain text representation
</td>

<td style="color:#000000;text-align:center;" >✓
</td>

<td >
</td>
</tr>
<tr >

<td style="text-align:left;" >Same editor/tools used for R scripts
</td>

<td style="color:#000000;text-align:center;" >✓
</td>

<td >
</td>
</tr>
<tr >

<td style="text-align:left;" >Works well with version control
</td>

<td style="color:#000000;text-align:center;" >✓
</td>

<td >
</td>
</tr>
<tr >

<td style="text-align:left;" >Focus on production output
</td>

<td style="color:#000000;text-align:center;" >✓
</td>

<td >
</td>
</tr>
<tr >

<td style="text-align:left;" >Output inline with code
</td>

<td style="color:#000000;text-align:center;" >✓
</td>

<td style="color:#000000;text-align:center;" >✓
</td>
</tr>
<tr >

<td style="text-align:left;" >Output cached across sessions
</td>

<td style="color:#000000;text-align:center;" >✓
</td>

<td style="color:#000000;text-align:center;" >✓
</td>
</tr>
<tr >

<td style="text-align:left;" >Share code and output in a single file
</td>

<td style="color:#000000;text-align:center;" >✓
</td>

<td style="color:#000000;text-align:center;" >✓
</td>
</tr>
<tr >

<td style="text-align:left;" >Emphasized execution model
</td>

<td style="color:#000000;text-align:center;" >Interactive & Batch
</td>

<td style="color:#000000;text-align:center;" >Interactive
</td>
</tr>
</tbody>
</table>

This video provides a bit more background and a demonstration of notebooks in action:

[youtube https://www.youtube.com/watch?v=zNzZ1PfUDNk&w=560&h=315]

## Iterate Quickly

In a typical R Markdown document, you must re-knit the document to see your changes, which can take some time if it contains non-trivial computations. R Notebooks, however, let you run code and see the results in the document immediately. They can include just about any kind of content R produces, including console output, plots, data frames, and interactive [HTML widgets](http://www.htmlwidgets.org/).

![screen-shot-2016-09-20-at-4-16-47-pm](https://rstudioblog.files.wordpress.com/2016/09/screen-shot-2016-09-20-at-4-16-47-pm.png)

You can see the progress of the code as it runs:

![screen-shot-2016-09-21-at-10-52-02-am](https://rstudioblog.files.wordpress.com/2016/09/screen-shot-2016-09-21-at-10-52-02-am.png)

You can preview the results of individual inline expressions, too:

![notebook-inline-output](https://rstudioblog.files.wordpress.com/2016/09/notebook-inline-output.png)

Even your LaTeX equations render in real-time as you type:

![notebook-mathjax](https://rstudioblog.files.wordpress.com/2016/09/notebook-mathjax.png)

This focused mode of interaction doesn't require you to keep the console, viewer, or output panes open. Everything you need is at your fingertips in the editor, reducing distractions and helping you concentrate on your analysis. When you're done, you'll have a formatted, reproducible record of what you've accomplished, with plenty of context, perfect for your own records or sharing with others.

## Batteries Included

R Notebooks can run more than just R code. You can run chunks [written in other languages](https://rmarkdown.rstudio.com/authoring_knitr_engines.html), like Python, Bash, or C++ (Rcpp).

![screen-shot-2016-09-20-at-4-25-48-pm](https://rstudioblog.files.wordpress.com/2016/09/screen-shot-2016-09-20-at-4-25-48-pm.png)

It's even possible to run SQL directly:

![notebook-sql](https://rstudioblog.files.wordpress.com/2016/09/notebook-sql.png)

This makes an R Notebook an excellent tool for orchestrating a reproducible, end-to-end data analysis workflow; you can easily ingest data using your tool of choice, and share data among languages by using packages like [feather](https://cran.r-project.org/web/packages/feather/index.html), or ordinary CSV files.

## Reproducible Notebooks

While you can run chunks (and even individual lines of R code!) in any order you like, a fully reproducible document must be able to be re-executed start-to-finish in a clean environment. There's a built-in command to do this, too, so it's easy to test your notebooks for reproducibility.

![screen-shot-2016-09-21-at-3-52-34-pm](https://rstudioblog.files.wordpress.com/2016/09/screen-shot-2016-09-21-at-3-52-34-pm.png)

## Rich Output Formats

Since they're built on R Markdown, R Notebooks work seamlessly with other R Markdown output types. You can use any existing R Markdown document as a notebook, or render (knit) a notebook to any R Markdown output type.

![notebook-yaml](https://rstudioblog.files.wordpress.com/2016/09/notebook-yaml.png)

The same document can be used as a notebook when you're quickly iterating on ideas and later rendered to a wholly different format for publication – no duplication of code, data, or output required.

## Share and Publish

R Notebooks are easy to share with collaborators. Because they're plain-text files, they work well with version control systems like Git. Your collaborators don't even need RStudio to edit them, since notebooks can be [rendered in the R console](https://rmarkdown.rstudio.com/r_notebook_format.html) using the open source [rmarkdown](https://cran.r-project.org/web/packages/rmarkdown/index.html) package.

Rendered notebooks can be previewed right inside RStudio:

![notebook-preview](https://rstudioblog.files.wordpress.com/2016/09/notebook-preview.png)

While the notebook preview looks similar to a rendered R Markdown document, the notebook preview does not execute any of your R code chunks; it simply shows you a rendered copy of the markdown in your document along with the most recent chunk output. Because it's very fast to generate this preview (again, no R code is executed), it's generated every time you save the R Markdown document.

The generated HTML file has the special extension _.nb.html_. It is self-contained, free of dependencies, and can be viewed locally or published to any static web hosting service.

![screen-shot-2016-09-14-at-12-12-35-pm](https://rstudioblog.files.wordpress.com/2016/09/screen-shot-2016-09-14-at-12-12-35-pm.png)

It also includes a bundled copy of the R Markdown source file, so it can be seamlessly opened in RStudio to resume work on the notebook with all output intact.

## Try It Out

To try out R Notebooks, you'll need to download the latest [RStudio Preview Release](https://www.rstudio.com/products/rstudio/download/preview/).

You can find documentation on notebook features on the [R Notebooks](https://rmarkdown.rstudio.com/r_notebooks.html) page on the R Markdown website, and we've also published a video tutorial in our [R Notebooks Webinar](https://www.rstudio.com/resources/webinars/introducing-notebooks-with-r-markdown/).

We believe the R Notebook will become a powerful new addition to your toolkit. Give it a spin and let us know what you think!

