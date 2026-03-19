---
title: R Markdown v2
people:
  - Yihui Xie
date: '2014-06-18'
tags:
- dynamic documents
- interactive documents
- knitr
- Markdown
- Pandoc
- rmarkdown
slug: r-markdown-v2
blogcategories:
- Products and Technology
- Company News and Events
- Open Source
ported_from: rstudio
port_status: in-progress
software: ["markdown", "rmarkdown"]
languages: ["R"]
categories:
  - Publishing
ported_categories:
  - News
  - Packages
---
 

People rarely agree on a best authoring tool or language. Some people cannot live without `\LaTeX{}` because of the beauty and quality of its PDF output. Some \feel{} \uncomfortable{} \with{} \backslashes{}, and would rather live in another <del>World</del> Word. We have also witnessed the popularity of Markdown, an incredibly simple language (seriously? a LANGUAGE?) that has made reproducible research [much easier](http://rpubs.com).

Thinking of all these tools and languages, every developer will dream about "_One ring to rule them all_". `\section{}`, `<h1></h1>`, `===`, `#`, ... Why cannot we write the first-level section header in a single way? Yes, we are aware of [the danger](http://xkcd.com/927/) of "adding yet another so-called universal standard that covers all the previous standards". However, we believe [Pandoc](http://johnmacfarlane.net/pandoc/) has done a fairly good job in terms of "yet another Markdown standard". Standing on the shoulders of Pandoc, today we are excited to announce the second episode of our journey into the development of the tools for authoring dynamic documents:

_The Return of R Markdown_!

The R package [**markdown**](http://cran.rstudio.com/package=markdown) (plus [**knitr**](http://cran.rstudio.com/package=knitr)) was our first version of R Markdown. The primary output format was HTML, which certainly could not satisfy all users in the <del>World</del> Word. It did not have features like citations, footnotes, or metadata (title, author, and date, etc), either. When we were asked how one could convert Markdown to PDF/Word, we used to tell users to try Pandoc. The problem is that Pandoc's great power comes with a lot of command line options (more than 70), and **knitr** has the same problem of too many options. That is why we created the second generation of R Markdown, represented by the [**rmarkdown**](https://rmarkdown.rstudio.com/) package, to provide reasonably good defaults and an R-friendly interface to customize Pandoc options.

The [new version of RStudio](https://www.rstudio.com/products/rstudio/download/) (v0.98.932) includes everything you need to use R Markdown v2 (including pandoc and the **rmarkdown** package). If you are not using RStudio you can install rmarkdown and pandoc separately as described [here](https://github.com/rstudio/rmarkdown#installation). To get started with a "Hello Word" example, simply click the menu `File -> New File -> R Markdown` in RStudio IDE. You can choose the output format from the drop-down menu on the toolbar.

![R Markdown Formats](https://rstudioblog.files.wordpress.com/2014/06/r-markdown-formats.png)

The built-in output formats include HTML, LaTeX/PDF, Word, Beamer slides, HTML5 presentations, and so on. [Pandoc's Markdown](http://johnmacfarlane.net/pandoc/README.html#pandocs-markdown) allows us to write richer content such as tables, citations, and footnotes. For power users who understand LaTeX/HTML, you can even embed raw LaTeX/HTML code in Markdown, and Pandoc is smart enough to process these raw fragments. If you cannot remember the possible options for a certain output format in the YAML metadata (data between `---` and `---` in the beginning of a document), you can use the `Settings` button on the toolbar.

Extensive documentation for R Markdown v2 and all of it's supported output formats are available on the new R Markdown website at <http://rmarkdown.rstudio.com>.

We understand users will never be satisfied by our default templates, regardless of how hard we try to make them appealing. The **rmarkdown** package is fully customizable and extensible in the sense that you can define your custom templates and output formats. You want to contribute an article to The R Journal, or JSS (Journal of Statistical Software), but prefer writing in Markdown instead of LaTeX? [No problem!](https://rmarkdown.rstudio.com/developer_document_templates.html) Pandoc also supports many other output formats, and you want EPUB books, or a different type of HTML5 slides? [No problem!](https://rmarkdown.rstudio.com/developer_custom_formats.html) Not satisfied with one single static output document? You can embed interactive widgets into R Markdown documents as well! [Let there be Shiny!](https://rmarkdown.rstudio.com/authoring_shiny.html) The more you learn about **rmarkdown** and Pandoc, the more freedom you will get.

For a brief video introduction, you may [watch the talk](http://vimeo.com/94181521) below (jump to 18:30 if you only want to see the demos):

[vimeo 94181521 w=500 h=281]

The **rmarkdown** package is open-source (GPL-3) and is both included in the [RStudio IDE](https://www.rstudio.com/products/rstudio/) and [available on GitHub](https://github.com/rstudio/rmarkdown). The package is not on CRAN yet, but will be there as soon as we make all the improvements requested by early users.

To clarify the relationship between **rmarkdown** and RStudio IDE, our IDE is absolutely not the only way to compile R Markdown documents. You are free to call functions in **rmarkdown** in any environment. Please check out the R package documentation, in particular, the _render()_ function in **rmarkdown**.

Please let us know if you have any questions or comments, and your feedback is greatly appreciated. We hope you will enjoy R Markdown v2.

![Keep Calm and Markdown](https://rstudioblog.files.wordpress.com/2014/06/keep-calm-and-markdown.png)

