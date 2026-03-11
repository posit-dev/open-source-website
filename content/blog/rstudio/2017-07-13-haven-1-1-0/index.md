---
title: haven 1.1.0
people:
  - Hadley Wickham
date: '2017-07-13'
slug: haven-1-1-0
categories:
- tidyverse
- Packages
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
- tidyverse
events: blog
ported_from: rstudio
port_status: raw
---


I'm pleased to announce the release of haven 1.1.0. Haven is designed to faciliate the transfer of data between R and SAS, SPSS, and Stata. It makes it easy to read SAS, SPSS, and Stata file formats in to R data frames, and makes it easy to save your R data frames in to SPSS and Stata if you need to collaborate with others using closed source statistical software. 

Install the latest version by running:

```R
install.packages("haven")
```

haven 1.1.0 is a small release that fixes a bunch of smaller issues. See the [release notes](http://haven.tidyverse.org/news/index.html#haven-1-1-0) for full details. The most important bug was ensuring that `read_sav()` once again correctly returns system defined missings as NA (rather than NaN). Other highlights include:

* Preliminary support for reading and writing SAS transport files with
  `read_xpt()` and `write_xpt()`.

* An experimental `cols_only` argument in `read_sas()` that allows you to 
  read only selected columns. 
  
* An update to the bundled ReadStat code, fixing many smaller reading and 
  writing bugs.
  
* Better checks in `write_sav()` and `write_dta()` making it more likely that
  you'll get a clear error in R instead of producing an invalid file.

A big thanks goes to community members [Evan Cortens](https://github.com/ecortens) and [Patrick Kennedy](https://github.com/pkq) who helped make this release possible with their code contributions.

