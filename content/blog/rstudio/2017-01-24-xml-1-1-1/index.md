---
title: xml2 1.1.1
people:
  - Jim Hester
date: '2017-01-24'
categories:
  - Data Wrangling
slug: xml-1-1-1
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
ported_from: rstudio
port_status: in-progress
software: ["xml2"]
languages: ["R"]
ported_categories:
  - Packages
---


Today we are pleased to release version 1.1.1 of xml2. xml2 makes it easy to read, create, and modify XML with R. You can install it with:

```r
install.packages("xml2")
```

As well as fixing many bugs, this release:

  * Makes it easier to create an modify XML

  * Improves roundtrip support between XML and lists

  * Adds support for XML validation and XSLT transformations.

You can see a full list of changes in the [release notes](https://github.com/hadley/xml2/releases/tag/v1.1.1). This is the first release maintained by [Jim Hester](https://github.com/jimhester).

## Creating and modifying XML

xml2 has been overhauled with a set of methods to make generating and modfying XML easier:

  * `xml_new_root()` can be used to create a new document and root node simultaneously.

```r
xml_new_root("x") %>%
  xml_add_child("y") %>%
  xml_root()
#> {xml_document}
#> <x>
#> [1] <y/>
```

  * New `xml_set_text()`, `xml_set_name()`, `xml_set_attr()`, and `xml_set_attrs()` make it easy to modify nodes within a pipeline.

```r
x <- read_xml("<a>
    <b />
    <c><b/></c>
  </a>")
x
#> {xml_document}
#> <a>
#> [1] <b/>
#> [2] <c>\n  <b/>\n</c>

x %>%
  xml_find_all(".//b") %>%
  xml_set_name("banana") %>%
  xml_set_attr("oldname", "b")
x
#> {xml_document}
#> <a>
#> [1] <banana oldname="b"/>
#> [2] <c>\n  <banana oldname="b"/>\n</c>
```

  * New `xml_add_parent()` makes it easy to insert a node as the parent of an existing node.

  * You can create more esoteric node types with `xml_comment()` (comments), `xml_cdata()` (CDATA nodes), and `xml_dtd()` (DTDs).

## Coercion to and from R Lists

xml2 1.1.1 improves support for converting to and from R lists, thanks in part to work by [Peter Foley](https://github.com/peterfoley) and [Jenny Bryan](https://github.com/jennybc). In particular xml2 now supports preserving the root node name as well as saving all xml2 attributes as R attributes. These changes allows you to convert most XML documents to and from R lists with `as_list()` and `as_xml_document()` without loss of data.

```r
x <- read_xml("<fruits><apple color = 'red' /></fruits>")
x
#> {xml_document}
#> <fruits>
#> [1] <apple color="red"/>
as_list(x)
#> $apple
#> list()
#> attr(,"color")
#> [1] "red"
as_xml_document(as_list(x))
#> {xml_document}
#> <apple color="red">
```

## XML validation and xslt

xml2 1.1.1 also adds support for XML validation, thanks to [Jeroen Ooms](https://github.com/jeroenooms). Simply read the document and schema files and call `xml_validate()`.

```r
doc <- read_xml(system.file("extdata/order-doc.xml", package = "xml2"))
schema <- read_xml(system.file("extdata/order-schema.xml", package = "xml2"))
xml_validate(doc, schema)
#> [1] TRUE
#> attr(,"errors")
#> character(0)
```

Jeroen also released the first xml2 extension package in conjunction with xml2 1.1.1, [xslt](https://cran.r-project.org/package=xslt). xslt allows one to apply [XSLT (Extensible Stylesheet Language Transformations)](https://en.wikipedia.org/wiki/XSLT) to XML documents, which are great for transforming XML data into other formats such as HTML.

