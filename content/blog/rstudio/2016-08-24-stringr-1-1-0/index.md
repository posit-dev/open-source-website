---
title: stringr 1.1.0
people:
  - Hadley Wickham
date: '2016-08-24'
slug: stringr-1-1-0
blogcategories:
- Products and Technology
- Open Source
tags:
- tidyverse
ported_from: rstudio
port_status: in-progress
software: ["tidyverse"]
languages: ["R"]
categories:
  - Data Wrangling
ported_categories:
  - Packages
  - tidyverse
---


I'm pleased to announce version 1.1.0 of stringr. stringr makes string manipulation easier by using consistent function and argument names, and eliminating options that you don't need 95% of the time. To get started with stringr, check out the [strings chapter](http://r4ds.had.co.nz/strings.html) in [R for data science](http://r4ds.had.co.nz/). Install it with:

```r
install.packages("stringr")
```

This release is mostly bug fixes, but there are a couple of new features you might care out.

  * There are three new datasets, `fruit`, `words` and `sentences`, to help you practice your regular expression skills:

```r
str_subset(fruit, "(..)\\1")
#> [1] "banana"      "coconut"     "cucumber"    "jujube"      "papaya"
#> [6] "salal berry"
head(words)
#> [1] "a"        "able"     "about"    "absolute" "accept"   "account"
sentences[1]
#> [1] "The birch canoe slid on the smooth planks."
```

  * More functions work with `boundary()`: `str_detect()` and `str_subset()` can detect boundaries, and `str_extract()` and `str_extract_all()` pull out the components between boundaries. This is particularly useful if you want to extract logical constructs like words or sentences.

```r
x <- "This is harder than you might expect, e.g. punctuation!"
x %>% str_extract_all(boundary("word")) %>% .[[1]]
#> [1] "This"        "is"          "harder"      "than"        "you"
#> [6] "might"       "expect"      "e.g"         "punctuation"
x %>% str_extract(boundary("sentence"))
#> [1] "This is harder than you might expect, e.g. punctuation!"
```

  * `str_view()` and `str_view_all()` create HTML widgets that display regular expression matches. This is particularly useful for teaching.

For a complete list of changes, please see the [release notes](https://github.com/hadley/stringr/releases/tag/v1.1.0).

