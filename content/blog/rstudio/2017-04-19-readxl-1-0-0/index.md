---
title: readxl 1.0.0
description: "readxl 1.0.0: target specific cells for reading Excel files plus new logical and list column types."
auto-description: true
people:
  - Jenny Bryan
date: '2017-04-19'
categories:
  - Data Wrangling
slug: readxl-1-0-0
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
  - RStudio
ported_from: rstudio
port_status: in-progress
software: ["tidyverse"]
languages: ["R"]
ported_categories:
  - Packages
  - tidyverse
---


I'm pleased to announce that [readxl](http://readxl.tidyverse.org) 1.0.0 is available on CRAN. [readxl](http://readxl.tidyverse.org) makes it easy to bring tabular data out of Excel and into R, for modern `.xlsx` files and the legacy `.xls` format. [readxl](http://readxl.tidyverse.org) does not have any tricky external dependencies, such as Java or Perl, and is easy to install and use on Mac, Windows, and Linux.

You can install it with:

```r
install.packages("readxl")
```

As well as fixing many bugs, this release:

  * Allows you to target specific cells for reading, in a variety of ways

  * Adds two new column types: `"logical"` and `"list"`, for data of disparate type

  * Is more resilient to the wondrous diversity in spreadsheets, e.g., those written by 3rd party tools

You can see a full list of changes in the [release notes](http://readxl.tidyverse.org/news/index.html). This is the first release maintained by Jenny Bryan.

## Specifying the data rectangle

In an ideal world, data would live in a neat rectangle in the upper left corner of a spreadsheet. But spreadsheets often serve multiple purposes for users with different priorities. It is common to encounter several rows of notes above or below the data, for example. The new `range` argument provides a flexible interface for describing the data rectangle, including Excel-style ranges and row- or column-only ranges.

```r
library(readxl)
read_excel(
  readxl_example("deaths.xlsx"),
  range = "arts!A5:F15"
)
#> # A tibble: 10 × 6
#>            Name Profession   Age `Has kids` `Date of birth`
#>
#> 1   David Bowie   musician    69       TRUE      1947-01-08
#> 2 Carrie Fisher      actor    60       TRUE      1956-10-21
#> 3   Chuck Berry   musician    90       TRUE      1926-10-18
#> 4   Bill Paxton      actor    61       TRUE      1955-05-17
#> # ... with 6 more rows, and 1 more variables: `Date of death`

read_excel(
  readxl_example("deaths.xlsx"),
  sheet = "other",
  range = cell_rows(5:15)
)
#> # A tibble: 10 × 6
#>           Name Profession   Age `Has kids` `Date of birth`
#>
#> 1   Vera Rubin  scientist    88       TRUE      1928-07-23
#> 2  Mohamed Ali    athlete    74       TRUE      1942-01-17
#> 3 Morley Safer journalist    84       TRUE      1931-11-08
#> 4 Fidel Castro politician    90       TRUE      1926-08-13
#> # ... with 6 more rows, and 1 more variables: `Date of death`
```

There is also a new argument `n_max` that limits the number of data rows read from the sheet. It is an example of [readxl](http://readxl.tidyverse.org)'s evolution towards a [readr](http://readr.tidyverse.org)-like interface. The [Sheet Geometry vignette](http://readxl.tidyverse.org/articles/sheet-geometry.html) goes over all the options.

## Column typing

The new ability to target cells for reading means that [readxl](http://readxl.tidyverse.org)'s automatic column typing will "just work" for most sheets, most of the time. Above, the `Has kids` column is automatically detected as `logical`, which is a new column type for [readxl](http://readxl.tidyverse.org).

You can still specify column type explicitly via `col_types`, which gets a couple new features. If you provide exactly one type, it is recycled to the necessary length. The new type `"guess"` can be mixed with explicit types to specify some types, while leaving others to be guessed.

```r
read_excel(
  readxl_example("deaths.xlsx"),
  range = "arts!A5:C15",
  col_types = c("guess", "skip", "numeric")
)
#> # A tibble: 10 × 2
#>            Name   Age
#>
#> 1   David Bowie    69
#> 2 Carrie Fisher    60
#> 3   Chuck Berry    90
#> 4   Bill Paxton    61
#> # ... with 6 more rows
```

The new argument `guess_max` limits the rows used for type guessing. Leading and trailing whitespace is trimmed when the new `trim_ws` argument is `TRUE`, which is the default. Finally, thanks to [Jonathan Marshall](https://github.com/jmarshallnz), multiple `na` values are accepted. The [Cell and Column Types vignette](http://readxl.tidyverse.org/articles/cell-and-column-types.html) has more detail.

### `"list"` columns

Thanks to [Greg Freedman Ellis](https://github.com/gergness) we now have a `"list"` column type. This is useful if you want to bring truly disparate data into R without the coercion required by atomic vector types.

```r
(df <- read_excel(
  readxl_example("clippy.xlsx"),
  col_types = c("text", "list")
))
#> # A tibble: 4 × 2
#>                   name      value
#>                  <chr>     <list>
#> 1                 Name  <chr [1]>
#> 2              Species  <chr [1]>
#> 3 Approx date of death <dttm [1]>
#> 4      Weight in grams  <dbl [1]>

tibble::deframe(df)
#> $Name
#> [1] "Clippy"
#>
#> $Species
#> [1] "paperclip"
#>
#> $`Approx date of death`
#> [1] "2007-01-01 UTC"
#>
#> $`Weight in grams`
#> [1] 0.9
```

## Everything else

To learn more, read the [vignettes and articles](http://readxl.tidyverse.org/articles/index.html) or [release notes](http://readxl.tidyverse.org/news/index.html). Highlights include:

  * General rationalization of sheet geometry, including detection and treatment of empty rows and columns.

  * Improved behavior and messaging around coercion and mismatched cell and column types.

  * Improved handling of datetimes with respect to 3rd party software, rounding, and the [Lotus 1-2-3 leap year bug](https://support.microsoft.com/en-us/help/214326/excel-incorrectly-assumes-that-the-year-1900-is-a-leap-year).

  * `read_xls()` and `read_xlsx()` are now exposed, so that files without an `.xls` or `.xlsx` extension can be read. Thanks [Jirka Lewandowski](https://github.com/jirkalewandowski)!

  * [readxl Workflows](http://readxl.tidyverse.org/articles/articles/readxl-workflows.html) showcases patterns that reduce tedium and increase reproducibility when raw data arrives in a spreadsheet.

