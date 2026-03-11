---
title: R & RStudio - The Interoperability Environment for Data Analytics
people:
  - Curtis Kephart
date: '2020-08-17'
slug: r-and-rstudio-the-interoperability-environment-for-data-analytics
categories:
- Data Science Leadership
tags:
- data science
resources:
- name: hex
  src: large_image.jpg
  title: Laptop with hexes
description: From design philosophies to current development priorities, R with RStudio
  is a wonderful environment for anyone who seeks understanding through the analysis
  of data. Here's why.
blogcategories:
- Data Science Leadership
events: blog
image: thumbnail.jpg
ported_from: rstudio
port_status: raw
---


On the RStudio Developer Blog we’ve recently written a series on <a href="https://blog.rstudio.com/2020/07/07/interoperability-july/" target="_blank">interoperability and R</a>, including why <a href="https://blog.rstudio.com/2020/07/15/interoperability-maximize-analytic-investments/" target="_blank">enterprises should embrace workflows that are open to diverse toolsets</a>.

The designers of R, from its very beginnings, have dealt directly with how best to tap into other tools.
Statisticians, analysts, and data scientists have long been challenged to bring together all the statistical methods and technologies required to perform the analysis the situation calls for—and this challenge has grown as more tools, libraries, and frameworks become available.

John Chambers writing on the design philosophy behind the S programming language, the predecessor to R, 

<blockquote>
“[W]e wanted to be able to begin in an interactive environment, where they did not consciously think of themselves as programming. Then as their needs become clearer and their sophistication increased, they should be able to slide gradually into programming, when the language and system aspects would become more important.” 
</blockquote>

Part of this design philosophy is to minimize the amount of effort and overhead required to get your analytics work done. It is not fair to assume that every data scientist is programming all day, or coming from a computer science background, but they still need to implement some of the most sophisticated tools programmers use. 

The ecosystem around R has striven to strike the right balance between a domain specific environment optimized for data science workflows and output, and a general programming environment. For example CRAN, Bioconductor, rOpenSci, and GitHub provide collections of packages written with data science in mind, which extend core R’s functionality, letting you tap into (and share) statistical methods and field-specific tools — when and only when you need them. 

Many of the most popular packages offer interfaces to tools in other languages. For example, most tidyverse packages include compiled (C/C++) code. Interestingly, core R itself connects you to tooling mostly written in other programming languages. As of R 4.0.2 over 75% of the lines in core R’s codebase are written C or Fortran (C 43%, Fortran 33%, & R 23.9%). 

## RStudio - design philosophy and development priorities

Our <a href="https://rstudio.com/about/" target="_blank">mission</a> at RStudio is to create free and open source software for data science, scientific research, and technical communication. R is a wonderful environment for data analysis, and we’ve focused on making it easier to use. We do this through our IDE and <a href="https://rstudio.com/about/pbc-report/" target="_blank">open sources packages</a>, such as the tidyverse. We also do this by making data science easier to learn through <a href="https://rstudio.com/products/cloud/" target="_blank">RStudio Cloud</a> and our support for <a href="https://education.rstudio.com/" target="_blank">data science education</a>. And we help make R easier to manage and scale out across an organization through our <a href="https://rstudio.com/products/team/" target="_blank">our professional products</a>, supporting best practices for data science in the enterprise through our <a href="https://solutions.rstudio.com/" target="_blank">solutions team</a>. 

As part of this effort, we have focused heavily on enabling and supporting interoperability between R and other tools.
We recently outlined in a <a href="https://blog.rstudio.com/2020/07/07/interoperability-july/" target="_blank">recent blog post</a> how the RStudio IDE allows you to embed many different languages in RMarkdown documents, including:

- **Using R & Python together** through the `reticulate` package
- **SQL code** for accessing databases,
- **BASH code** for shell scripts,
- **C and C++ code** using the `Rcpp` package,
- **STAN code** with `rstan` for Bayesian modeling,
- **Javascript** for doing web programming,
- **and many more languages**. You can find a complete list of the many platforms supported in the language engines chapter of the book, <a href="https://bookdown.org/yihui/rmarkdown/language-engines.html" target="_blank">R Markdown: The Definitive Guide</a>.

And we work with the community to support: 

- Bilingual data science teams, by providing a single platform for data scientists to develop in R or Python (<a href="https://rstudio.com/products/rstudio-server-pro/" target="_blank">RStudio Server Pro</a>), and to deploy applications built with either (through <a href="https://rstudio.com/products/connect/" target="_blank">RStudio Connect</a>)
- Making it easy to create web applications with shiny or put models into production via plumber APIs
- Supporting easy access to data sources, such `odbc`, `DBI`, and `dbplyr` for <a href="https://db.rstudio.com/" target="_blank">database access and wrangling</a>. 
- Incubating <a href="https://ursalabs.org/" target="_blank">Ursa Labs</a>, which is focused on building the next generation of cross language tools, leveraging the Apache Arrow project. 
- Integration from R with other modeling frameworks, including <a href="https://tensorflow.rstudio.com/" target="_blank">TensorFlow</a> and <a href="https://spark.rstudio.com/mlib/" target="_blank">SparkMLlib</a>
- Using <a href="https://spark.rstudio.com/" target="_blank">Sparklyr</a> and  <a href="https://docs.rstudio.com/rsp/integration/launcher-kubernetes/" target="_blank">Launcher with kubernetes</a> to distribute your calculations or modeling operations over many machines, *which we will be discussing in more depth in an upcoming blog post*.  

This list goes on and on and grows by the week. 

R with RStudio is a wonderful environment for anyone who seeks understanding through the analysis of data. It does this by finding a balance between a domain specific environment and a general programming language that doesn't prioritize data scientists. That is, it strives to be an environment optimized for analytics workflows and output. At the fulcrum of this balance is extensive interoperability, the ability to pull in interfaces into other technologies as they are needed, and a vibrant community sustaining these. This has been the goal for R since initial design principles, through the extensive work shared by the R community, and significant continued investment by RStudio. 

