---
title: xml2 1.0.0
people:
  - Hadley Wickham
date: '2016-07-05'
categories:
  - Data Wrangling
slug: xml2-1-0-0
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
  - tidyverse
ported_from: rstudio
port_status: in-progress
software: ["tidyverse"]
languages: ["R"]
ported_categories:
  - Packages
  - tidyverse
---


We are pleased to announced that xml2 1.0.0 is now available on CRAN. Xml2 is a wrapper around the comprehensive [libxml2](http://xmlsoft.org) C library, and makes it easy to work with XML and HTML files in R. Install the latest version with:

```r
install.packages("xml2")
```

There are three major improvements in 1.0.0:

  1. You can now modify and create XML documents.

  2. `xml_find_first()` replaces `xml_find_one()`, and provides better semantics for missing nodes.

  3. Improved namespace handling when working with XPath.

There are many other small improvements and bug fixes: please see the [release notes](https://github.com/hadley/xml2/releases/tag/v1.0.0) for a complete list.

## Modification and creation

xml2 now supports modification and creation of XML nodes. This includes new functions `xml_new_document()`, `xml_new_child()`, `xml_new_sibling()`, `xml_set_namespace()`, `xml_remove()`, `xml_replace()`, `xml_root()`, and replacement methods for `xml_name()`, `xml_attr()`, `xml_attrs()` and `xml_text()`.

The basic process of creating an XML document by hand looks something like this:

```r
root <- xml_new_document() %>% xml_add_child("root")

root %>%
  xml_add_child("a1", x = "1", y = "2") %>%
  xml_add_child("b") %>%
  xml_add_child("c") %>%
  invisible()

root %>%
  xml_add_child("a2") %>%
  xml_add_sibling("a3") %>%
  invisible()

cat(as.character(root))
#> <?xml version="1.0"?>
#> <root><a1 x="1" y="2"><b><c/></b></a1><a2/><a3/></root>
```

For a complete description of creation and mutation, please see [`vignette("modification", package = "xml2")`](https://cran.r-project.org/web/packages/xml2).

## `xml_find_first()`

`xml_find_one()` has been deprecated in favor of `xml_find_first()`. `xml_find_first()` now always returns a single node: if there are multiple matches, it returns the first (without a warning), and if there are no matches, it returns a new `xml_missing` object.

This makes it much easier to work with ragged/inconsistent hierarchies:

```r
x1 <- read_xml("<a>
  <b></b>
  <b><c>See</c></b>
  <b><c>Sea</c><c /></b>
</a>")

c <- x1 %>%
  xml_find_all(".//b") %>%
  xml_find_first(".//c")
c
#> {xml_nodeset (3)}
#> [1] <NA>
#> [2] <c>See</c>
#> [3] <c>Sea</c>
```

Missing nodes are replaced by missing values in functions that return vectors:

```r
xml_name(c)
#> [1] NA  "c" "c"
xml_text(c)
#> [1] NA    "See" "Sea"
```

## XPath and namespaces

XPath is challenging to use if your document contains any namespaces:

```r
x <- read_xml('
 <root>
   <doc1 xmlns = "http://foo.com"><baz /></doc1>
   <doc2 xmlns = "http://bar.com"><baz /></doc2>
 </root>
')
x %>% xml_find_all(".//baz")
#> {xml_nodeset (0)}
```

To make life slightly easier, the default `xml_ns()` object is automatically passed to `xml_find_*()`:

```r
x %>% xml_ns()
#> d1 <-> http://foo.com
#> d2 <-> http://bar.com
x %>% xml_find_all(".//d1:baz")
#> {xml_nodeset (1)}
#> [1] <baz/>
```

If you just want to avoid the hassle of namespaces altogether, we have a new nuclear option: `xml_ns_strip()`:

```r
xml_ns_strip(x)
x %>% xml_find_all(".//baz")
#> {xml_nodeset (2)}
#> [1] <baz/>
#> [2] <baz/>
```

