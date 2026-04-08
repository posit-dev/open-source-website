---
title: 'Announcing blogdown: Create Websites with R Markdown'
description: "Announcing blogdown: create static websites with R Markdown and Hugo."
auto-description: true
people:
  - Yihui Xie
date: '2017-09-11'
slug: announcing-blogdown
categories:
  - Publishing
tags:
  - Markdown
  - R Markdown
  - Hugo
  - Website
  - Jekyll
  - Hexo
  - Wordpress
  - Packages
  - RStudio
blogcategories:
  - Products and Technology
  - Open Source
ported_from: rstudio
port_status: in-progress
software: ["blogdown"]
languages: ["R"]
ported_categories:
  - Packages
  - R Markdown
---


Today I'm excited to announce a new R package, **blogdown**, to help you create general-purpose (static) websites with R Markdown. The first version of **blogdown** is available on CRAN now, and you can install it with:

```r
install.packages("blogdown")
```

The source package is hosted on Github in the repository [rstudio/blogdown](https://github.com/rstudio/blogdown). Since **blogdown** is a new package, you may install and test the development version using `devtools::install_github("rstudio/blogdown")` if you run into problems with the CRAN version.

## Introduction

In a nutshell, **blogdown** is an effort to integrate R Markdown with static website generators, so that you can generate web pages dynamically. For example, you can use R code chunks (or [other languages](https://rmarkdown.rstudio.com/authoring_knitr_engines.html) that **knitr** supports) to generate tables and graphics automatically on any web page. Before **blogdown**, you can easily do this using:

- the **rmarkdown** package to create single output files from R Markdown documents;
- and the [**bookdown**](https://github.com/rstudio/bookdown) package to compile multiple R Markdown documents to a book;

But the structure of a website can be far more complicated than a collection of independent HTML pages or a book. With **blogdown**, the directory structure of your R Markdown files can be arbitrary. You can easily create a project website, or a blog. Each page can have its own metadata (such as categories and tags), and you can generate pages of lists of content (such as a list of blog posts or examples).

Besides the advantage in website structures, another highlight of **blogdown** is that it inherited **bookdown**'s Markdown extensions (based on Pandoc's Markdown), which means you can easily write technical content on your website, including everything that Pandoc supports (e.g., headings, lists, footnotes, tables, figures, citations, LaTeX math, and quotes, etc) and **bookdown**'s extensions (e.g., figure and table captions, cross-references, theorems, proofs, numbered equations, and HTML widgets, etc).

There are several popular static site generators, and the main one we support in **blogdown** is [Hugo](https://gohugo.io). Hugo is easy to install (no dependencies), lightning fast (one millisecond per page), and very flexible. We have also provided (limited) support for [Jekyll](https://jekyllrb.com) and [Hexo](https://hexo.io) (see documentation). The Markdown support in these generators is often poor in terms of functionalities (you cannot easily beat Pandoc's Markdown), and sometimes it is painful that they use different flavors of Markdown. With **blogdown**, you can use richer Markdown syntax if you want.

## Get Started

It is extremely easy to get started with a new website. After you have installed the **blogdown** package, it only takes one step to create a new website---just call the function `new_site()` under an empty directory (or an empty RStudio project):

```r
blogdown::new_site()
```

It will download and install Hugo if it has not been installed, download a default Hugo theme, add some sample posts, build the site, and launch it in your web browser (or RStudio Viewer) so that you can immediately preview the website. Note you only need to use this function once for every new site. For an existing website, you may call `blogdown::serve_site()` or the RStudio addin "Serve Site" to preview the site; it will watch changes in your source files continuously and rebuild your site automatically.

To write new posts, you may use the RStudio addin "New Post":

![New Post](https://bookdown.org/yihui/blogdown/images/new-post.png)

If you are not satisfied with the default theme, you can try to create another new site with [a different theme](https://bookdown.org/yihui/blogdown/other-themes.html) till you find a theme that you like.

## Documentation

The comprehensive documentation of this package is a book written in **bookdown**, which is freely available at https://bookdown.org/yihui/blogdown/ and to be published by Chapman & Hall later this year. The book may seem to be short (about 150 pages), but it contains many external resources, such as examples that we have spent a lot of time on creating. It may take you quite a while to fully digest this book, but perhaps it is not necessary. For example, you do not have to read Chapter 2 to understand how Hugo works if you can find a theme that you like and don't want to customize too much (hint: this is unlikely---you will surely be bored by the appearance of your website someday). Anyway, you are expected to read at least Chapter 1 of this book.

## Migration

If you don't have a website right now, consider yourself to be lucky. It is much easier to start a new website than converting an existing website. The latter is not impossible, and we have shown in [Chapter 4](https://bookdown.org/yihui/blogdown/migration.html) how to convert WordPress and Jekyll websites to Hugo. To give you an idea about how long it takes to convert a website: 

- I spent a whole week on converting [my personal website](https://yihui.name) from Jekyll to Hugo. The complication was that I had a Chinese blog, an English blog, two project websites ([**knitr**](https://yihui.name/knitr/) and [**animation**](https://yihui.name/animation/)), and several single-page project websites (such as [**formatR**](https://yihui.name/formatR/)). Finally I managed to put all of them in [one repository](https://github.com/rbind/yihui).

- [Rob Hyndman](https://robjhyndman.com) spent several days on converting his WordPress website to **blogdown** ([read more here](https://support.rbind.io/2017/05/15/converting-robjhyndman-to-blogdown/)), when the **blogdown** documentation was far from being complete (Chapter 4 did not exist).

- It took me four hours to convert [Simply Statistics blog](https://simplystatistics.org/) from Jekyll to **blogdown**. It had about 1000 posts at that time.

- I have converted three WordPress sites by myself: [the RViews blog](https://rviews.rstudio.com/) took me a few days, [the RStudio blog](https://blog.rstudio.com/) took me one day, and [Karl Broman](http://kbroman.org/)'s blog took me one hour.

I have provided the scripts that I used in Chapter 4, and hopefully you can reuse them to convert your own websites to save you some time.

## Conclusion

I believe **blogdown** can introduce a highly streamlined experience to create and maintain a website. At least I feel addicted to blogging again after three years. I have been a firm believer in writing, but I hated the fact that I had to log in an online system to write something (e.g., WordPress), or manually type out all the YAML metadata in a new post (which is why I created the RStudio addin "New Post"). Now I just need to open my RStudio project, use the "Serve Site" addin, then create a new post using the addin "New Post" or revise existing posts, and I can live preview the site immediately in RStudio Viewer when I save the post. Deployment of the website is as simple as pushing to Github, and [Netlify](https://www.netlify.com) will do the rest of work for me.

![cats flow](https://slides.yihui.name/gif/cat-flow.gif)

There are many advantages of static websites as mentioned in [Chapter 2](https://bookdown.org/yihui/blogdown/static-sites.html) of the book. You whole website is just contained in a folder that you can preview locally (even offline!) or publish to any web server. Your posts are plain-text files that you can create or edit at any time, which means finally you have got something more meaningful to do [on your next flight](https://twitter.com/imtaras/status/906392194012999680) than having to stare at Sudoku puzzles to kill time (you may teach your neighbors R Markdown and **blogdown** if they feel jealousy looking at your screen).

## Acknowledgements

Although **blogdown** is still relatively new, I have received a lot of useful feedback during the development of the package and the book. There have been about 200 [Github issues](https://github.com/rstudio/blogdown/issues) (including [pull requests](https://github.com/rstudio/blogdown/pulls)) and a few dozen questions on [StackOverflow](http://stackoverflow.com/questions/tagged/blogdown). Some Github issues were really inspiring (e.g., [#40](https://github.com/rstudio/blogdown/issues/40) and [#97](https://github.com/rstudio/blogdown/issues/97)), and I was very glad that they filed the feature requests. I also want to thank [those who](https://github.com/rstudio/blogdown/graphs/contributors) submitted Github pull requests to improve the book. To be honest, this book was quite painful to write, because there are too many technologies potentially related to a website (e.g., JavaScript, domain names, DNS, and continuous deployment). However, I have gained a lot of motivation and inspiration from several early brave users who created their websites and wrote their own **blogdown** tutorials (even before the official documentation existed). That is also [how I found](https://bookdown.org/yihui/blogdown/author.html) the co-authors of this book, [Amber](https://twitter.com/ProQuesAsker) and [Alison](https://apreshill.rbind.io).

I'm particularly grateful to the feedback from beginners (so please don't be shy to ask "dumb" questions). It is very helpful to see what can be confusing to beginners, so that we can try better explanations or implementations, which can usually benefit users of all levels.

If you are looking for inspirations from other people's **blogdown**-based websites, you may thumb through the Github organization https://github.com/rbind. You are also welcome to move your website over there to share with or inspire more people.

As usual, please feel free to ask questions on [StackOverflow](https://stackoverflow.com/questions/tagged/blogdown) (with at least tags `r` and `blogdown`), and file bug reports and feature requests [on Github](https://github.com/rstudio/blogdown). I recommend you to spend some time on reading the **blogdown** book, but I understand it may not be easy to digest, so it is fine to ask questions before you finish reading the book. I'll be happy to point you to the relevant sections if your questions have been answered in the book. I hope you can enjoy this package, and have fun with your website!

