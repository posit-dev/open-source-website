---
title: Announcing RStudio v1.0!
people:
  - RStudio Team
date: '2016-11-01'
categories:
- News
- RStudio IDE
slug: announcing-rstudio-v1-0
blogcategories:
- Products and Technology
- Company News and Events
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: raw
---


Today we're very pleased to announce the availability of RStudio Version 1.0! Version 1.0 is our 10th major release since the initial launch in February 2011 (see the full release history below), and our biggest ever! Highlights include:

  * Authoring tools for [R Notebooks](https://rmarkdown.rstudio.com/r_notebooks.html).

  * Integrated support for the [sparklyr](http://spark.rstudio.com) package (R interface to Spark).

  * Performance profiling via integration with the [profvis](https://github.com/rstudio/profvis) package.

  * Enhanced data import tools based on the [readr](https://github.com/hadley/readr), [readxl](https://github.com/hadley/readxl) and [haven](https://github.com/hadley/haven) packages.

  * Authoring tools for R Markdown [websites](https://rmarkdown.rstudio.com/rmarkdown_websites.html) and the [bookdown](https://bookdown.org/) package.

  * Many other miscellaneous enhancements and bug fixes.

We hope you [download version 1.0](https://www.rstudio.com/products/rstudio/download/) now and as always [let us know](https://support.rstudio.com/hc/en-us) what you think.

## R Notebooks

[R Notebooks](https://rmarkdown.rstudio.com/r_notebooks.html) add a powerful notebook authoring engine to [R Markdown](https://rmarkdown.rstudio.com/). Notebook interfaces for data analysis have compelling advantages including the close association of code and output and the ability to intersperse narrative with computation. Notebooks are also an excellent tool for teaching and a convenient way to share analyses.

![](https://rmarkdown.rstudio.com/images/notebook-demo.png)

### Interactive R Markdown

As an authoring format, R Markdown bears many similarities to traditional notebooks like [Jupyter](https://jupyter.org/) and [Beaker](http://beakernotebook.com/). However, code in notebooks is typically executed interactively, one cell at a time, whereas code in R Markdown documents is typically executed in batch.

R Notebooks bring the interactive model of execution to your R Markdown documents, giving you the capability to work quickly and iteratively in a notebook interface without leaving behind the plain-text tools, compatibility with version control, and production-quality output you've come to rely on from R Markdown.

### Iterate Quickly

In a typical R Markdown document, you must re-knit the document to see your changes, which can take some time if it contains non-trivial computations. R Notebooks, however, let you run code and see the results in the document immediately. They can include just about any kind of content R produces, including console output, plots, data frames, and interactive [HTML widgets](http://www.htmlwidgets.org/).

![screen-shot-2016-09-20-at-4-16-47-pm](https://rstudioblog.files.wordpress.com/2016/09/screen-shot-2016-09-20-at-4-16-47-pm.png)

You can see the progress of the code as it runs:

![screen-shot-2016-09-21-at-10-52-02-am](https://rstudioblog.files.wordpress.com/2016/09/screen-shot-2016-09-21-at-10-52-02-am.png)

You can preview the results of individual inline expressions, too:

![notebook-inline-output](https://rstudioblog.files.wordpress.com/2016/09/notebook-inline-output.png)

Even your LaTeX equations render in real-time as you type:

![notebook-mathjax](https://rstudioblog.files.wordpress.com/2016/09/notebook-mathjax.png)

This focused mode of interaction doesn't require you to keep the console, viewer, or output panes open. Everything you need is at your fingertips in the editor, reducing distractions and helping you concentrate on your analysis. When you're done, you'll have a formatted, reproducible record of what you've accomplished, with plenty of context, perfect for your own records or sharing with others.

## Spark with sparklyr

The [sparklyr package](https://spark.rstudio.com/) is a new R interface for Apache Spark. RStudio now includes integrated support for Spark and the sparklyr package, including tools for:

  * Creating and managing Spark connections

  * Browsing the tables and columns of Spark DataFrames

  * Previewing the first 1,000 rows of Spark DataFrames

Once you've installed the sparklyr package, you should find a new **Spark** pane within the IDE. This pane includes a **New Connection** dialog which can be used to make connections to local or remote Spark instances:

![](https://spark.rstudio.com/images/spark-connect.png)

Once you've connected to Spark you'll be able to browse the tables contained within the Spark cluster:

![](https://spark.rstudio.com/images/spark-tab.png)

The Spark DataFrame preview uses the standard RStudio data viewer:

![](https://spark.rstudio.com/images/spark-dataview.png)

## Profiling with profvis

"How can I make my code faster?"

If you write R code, then you've probably asked yourself this question. A profiler is an important tool for doing this: it records how the computer spends its time, and once you know that, you can focus on the slow parts to make them faster.

RStudio now includes integrated support for profiling R code and for visualizing profiling data. R itself has long had a built-in profiler, and now it's easier than ever to use the profiler and interpret the results.

To profile code with RStudio, select it in the editor, and then click on **Profile -> Profile Selected Line(s)**. R will run that code with the profiler turned on, and then open up an interactive visualization.

[![](https://rstudioblog.files.wordpress.com/2016/05/profile1.gif&h=844)](https://rstudioblog.files.wordpress.com/2016/05/profile1.gif)

In the visualization, there are two main parts: on top, there is the code with information about the amount of time spent executing each line, and on the bottom there is a _flame graph_, which shows what R was doing over time. In the flame graph, the horizontal direction represents time, moving from left to right, and the vertical direction represents the _call stack_, which are the functions that are currently being called. (Each time a function calls another function, it goes on top of the stack, and when a function exits, it is removed from the stack.)

![profile.png](https://rstudioblog.files.wordpress.com/2016/05/profile.png&h=388)

The **Data** tab contains a call tree, showing which function calls are most expensive:

[![Profiling data pane](https://rstudioblog.files.wordpress.com/2016/05/data1.png&h=270)](https://rstudioblog.files.wordpress.com/2016/05/data1.png)

Armed with this information, you'll know what parts of your code to focus on to speed things up!

## Data Import

RStudio now integrates with the [readr](http://readr.tidyverse.org/), [readxl](https://cran.r-project.org/web/packages/readxl/index.html), and [haven](http://haven.tidyverse.org/) packages to provide comprehensive tools for importing data from many text file formats, Excel worksheets, as well as SAS, Stata, and SPSS data files. The tools are focused on interactively refining an import then providing the code required to reproduce the import on new datasets.

For example, here's the workflow we would use to import the Excel worksheet at <http://www.fns.usda.gov/sites/default/files/pd/slsummar.xls>.

First provide the dataset URL and review the import in preview mode (notice that this file contains two tables and as a result requires the first few rows to be removed):

![](https://support.rstudio.com/hc/en-us/article_attachments/206278038/Screen_Shot_2016-04-08_at_3.12.13_PM.png)

We can clean this up by skipping 6 rows from this file and unchecking the "First Row as Names" checkbox:

![](https://support.rstudio.com/hc/en-us/article_attachments/206278068/Screen_Shot_2016-04-08_at_3.12.21_PM.png)

The file is looking better but some columns are being displayed as strings when they are clearly numerical data. We can fix this by selecting "numeric" from the column drop-down:

![](https://support.rstudio.com/hc/en-us/article_attachments/206278098/Screen_Shot_2016-04-08_at_3.12.26_PM.png)

The final step is to click "Import" to run the code displayed under "Code Preview" and import the data into R. The code is executed within the console and imported dataset is displayed automatically:

![](https://support.rstudio.com/hc/en-us/article_attachments/206328087/Screen_Shot_2016-04-08_at_3.12.31_PM.png)

Note that rather than executing the import we could have just copied and pasted the import code and included it within any R script.

## RStudio Release History

We started working on RStudio in November of 2008 (8 years ago!) and had our first public release in February of 2011. Here are highlights of the various releases through the years:

| Version | Date | Highlights |
|:--|:--|:--|
| 0.92 | Feb 2011 | * Initial public release |
| 0.93 | Apr 2011 | * Interactive plotting with manipulate<br/> * Source editor themes<br/> * Configurable workspace layout |
| 0.94 | Jun 2011 | * Enhanced plot export<br/> * Enhanced package installation and management<br/> * Enhanced history management |
| 0.95 | Jan 2012 | * RStudio project system<br/> * Code navigation (typeahead search, go to definition)<br/> * Version control integration (Git and Subversion) |
| 0.96 | May 2012 | * Enhanced authoring for Sweave<br/> * Web publishing with R Markdown<br/> * Code folding and many other editing enhancements |
| 0.97 | Oct 2012 | * Package development tools<br/> * Vim editing mode<br/> * More intelligent R auto-indentation |
| 0.98 | Dec 2013 | * Interactive debugging tools<br/> * Enhanced environment pane<br/> * Viewer pane for web content / htmlwidgets |
| 0.98b | Jun 2014 | * R Markdown v2 (publish to PDF, Word, and more)<br/> * Integrated tools for Shiny application development<br/> * Editor support for XML, SQL, Python, and Bash |
| 0.99 | May 2015 | * Data viewer with support for large datasets, filtering, searching, and sorting<br/> * Major enhancements to R and C/C++ code completion and inline code diagnostics<br/> * Multiple cursors, tab re-ordering, enhanced Vim mode |
| 0.99b | Feb 2016 | * Emacs editing mode<br/> * Multi-window source editing<br/> * Customizable keyboard shortcuts<br/> * RStudio Addins |
| 1.0 | Nov 2016 | * Authoring tools for R Notebooks<br/> * Integrated support for sparklyr (R interface to Spark)<br/> * Enhanced data import tools<br/> * Performance profiling via integration with profvis |

The [RStudio Release History](https://support.rstudio.com/hc/en-us/articles/200716783-RStudio-Release-History) page on our support website provides a complete history of all major and minor point releases.

