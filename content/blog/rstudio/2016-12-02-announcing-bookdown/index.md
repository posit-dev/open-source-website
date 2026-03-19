---
title: 'Announcing bookdown: Authoring Books and Technical Documents with R Markdown'
people:
  - Yihui Xie
date: '2016-12-02'
categories:
- Packages
- R Markdown
slug: announcing-bookdown
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
- R Markdown
ported_from: rstudio
port_status: in-progress
---


We have released the R package **bookdown** (v0.3) to [CRAN](https://cran.rstudio.com/package=bookdown). It may be old news to some users, but we are happy to make an official announcement today. To install the package from CRAN, you can

```r
install.packages("bookdown")
```

The **bookdown** package provides an easier way to write books and technical publications than traditional tools such as LaTeX and Word. It inherits the simplicity of syntax and flexibility for data analysis from R Markdown, and extends R Markdown for technical writing, so that you can make better use of document elements such as figures, tables, equations, theorems, citations, and references, etc. Similar to LaTeX, you can number and cross-reference these elements with **bookdown**. <!-- more -->Below are some screenshots to show what **bookdown** can produce:

![An example of figure numbers and captions](https://rstudioblog.files.wordpress.com/2016/12/screen-shot-2016-12-01-at-2-39-28-pm.png)


![Examples of table numbers and captions](https://rstudioblog.files.wordpress.com/2016/12/screen-shot-2016-12-01-at-2-40-20-pm.png)


![Math equations](https://rstudioblog.files.wordpress.com/2016/12/screen-shot-2016-12-01-at-2-41-18-pm.png)


Your document can even include live examples (e.g. [HTML widgets](http://htmlwidgets.org) and [Shiny apps](https://shiny.rstudio.com)) so readers can interact with them while reading the book. The book can be rendered to multiple output formats, including LaTeX/PDF, HTML, EPUB, and Word, thus making it easy to put your documents online. The style and theme of these output formats can be customized. Most features apply to all output formats, e.g., you can also number equations and theorems in HTML output.

[![The bookdown book](https://bookdown.org/yihui/bookdown/images/cover.jpg)](https://bookdown.org/yihui/bookdown)

You can find the full documentation at <https://bookdown.org/yihui/bookdown>. As a matter of fact, the documentation was written using **bookdown** (of course!), and its source is fully available [on GitHub](https://github.com/rstudio/bookdown/tree/master/inst/examples). The book is to be published by [Chapman & Hall](http://crcpress.com/product/isbn/9781138700109) by the end of this month (pre-order also available on [Amazon](http://a.co/0uHNbno)). We used books and R primarily for examples in this book, but **bookdown** is not only for books or R. Most features introduced in this book also apply to other types of publications: journal papers, reports, [dissertations](https://github.com/cpsievert/phd-thesis), [course handouts](https://geanders.github.io/RProgrammingForResearch/), study notes, and even novels. You do not have to use R, either. Other choices of computing languages include Python, C, C++, SQL, Bash, Stan, JavaScript, and so on, although R is best supported. You can also leave out computing, for example, to write a novel.

There have been a large number of books published on <https://bookdown.org>, and we hope you can find some inspiration there to start your own book.

![mimic.gif](https://rstudioblog.files.wordpress.com/2016/12/mimic.gif)

To be clear, the goal of **bookdown** is definitely not to replace sophisticated typesetting tools like LaTeX, but help authors focus on content (instead of appearance), and present common components of a technical document more easily using the Markdown syntax (such sections, quotes, figures, tables, and so on). To some degree, **bookdown** reinvented a small part of LaTeX in other formats (HTML, EPUB, Word). There are surely features of other typesetting tools that are unavailable in **bookdown**, in which case we encourage you to either submit a feature request with justifications, or take a deep breath and [say **no** to new features](https://twitter.com/kwbroman/status/798938827876421633) to keep things simple (for your reference, the **bookdown** package and book didn't exist about [a year ago](https://github.com/rstudio/bookdown/graphs/contributors)).

Writing books can be highly addictive: it helps you organize your (random) thoughts and content into chapters and sections, and it is very rewarding to see the number of pages grow each day like a little baby. You can do things that you normally cannot/won't do in journal papers. For example, you can thank your kids in the preface (without whom you should have finished the book two years earlier). Choose a fresh and crispy font, and you simply cannot stop writing! With one click of a button, you can go directly from R Markdown documents to [a PDF](https://bookdown.org/yihui/bookdown/bookdown.pdf) that is ready to be printed by your publisher.

We hope you will enjoy **bookdown**. Please feel free to [let us know](https://github.com/rstudio/bookdown/issues) if you have any feedback, or ask technical questions on [StackOverflow](http://stackoverflow.com/questions/tagged/bookdown).

