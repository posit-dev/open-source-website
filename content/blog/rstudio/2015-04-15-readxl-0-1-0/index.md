---
title: Get data out of excel and into R with readxl
people:
  - Hadley Wickham
date: '2015-04-15'
categories:
  - Data Wrangling
slug: readxl-0-1-0
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
ported_from: rstudio
port_status: in-progress
software: ["readxl"]
languages: ["R"]
ported_categories:
  - Packages
---


I'm pleased to announced that the first version of readxl is now available on CRAN. Readxl makes it easy to get tabular data out of excel. It:

  * Supports both the legacy `.xls` format and the modern xml-based `.xlsx` format. `.xls` support is made possible the with [libxls](http://sourceforge.net/projects/libxls/) C library, which abstracts away many of the complexities of the underlying binary format. To parse `.xlsx`, we use the insanely fast [RapidXML](http://rapidxml.sourceforge.net) C++ library.

  * Has no external dependencies so it's easy to use on all platforms.

  * Re-encodes non-ASCII characters to UTF-8.

  * Loads datetimes into POSIXct columns. Both Windows (1900) and Mac (1904) date specifications are processed correctly.

  * Blank columns are automatically dropped.

  * Returns output with class `c("tbl_df", "tbl", "data.frame")` so if you also use [dplyr](https://blog.rstudio.com/2015/01/09/dplyr-0-4-0/) you'll get an enhanced print method (i.e. you'll see just the first ten rows, not the first 10,000!).

You can install it by running:

```r
install.packages("readxl")
```

There's not really much to say about how to use it:

```r
library(readxl)
# Use a excel file included in the package
sample <- system.file("extdata", "datasets.xlsx", package = "readxl")

# Read by position
head(read_excel(sample, 2))
#>    mpg cyl disp  hp drat    wt  qsec vs am gear carb
#> 1 21.0   6  160 110 3.90 2.620 16.46  0  1    4    4
#> 2 21.0   6  160 110 3.90 2.875 17.02  0  1    4    4
#> 3 22.8   4  108  93 3.85 2.320 18.61  1  1    4    1
#> 4 21.4   6  258 110 3.08 3.215 19.44  1  0    3    1
#> 5 18.7   8  360 175 3.15 3.440 17.02  0  0    3    2
#> 6 18.1   6  225 105 2.76 3.460 20.22  1  0    3    1

# Or by name:
excel_sheets(sample)
#> [1] "iris"     "mtcars"   "chickwts" "quakes"
head(read_excel(sample, "mtcars"))
#>    mpg cyl disp  hp drat    wt  qsec vs am gear carb
#> 1 21.0   6  160 110 3.90 2.620 16.46  0  1    4    4
#> 2 21.0   6  160 110 3.90 2.875 17.02  0  1    4    4
#> 3 22.8   4  108  93 3.85 2.320 18.61  1  1    4    1
#> 4 21.4   6  258 110 3.08 3.215 19.44  1  0    3    1
#> 5 18.7   8  360 175 3.15 3.440 17.02  0  0    3    2
#> 6 18.1   6  225 105 2.76 3.460 20.22  1  0    3    1
```

You can see the documentation for more info on the `col_names`, `col_types` and `na` arguments.

Readxl is still under active development. If you have problems loading a dataset, please try the [development version](https://github.com/hadley/readxl), and if that doesn't work, [file an issue](https://github.com/hadley/readxl/issues).

