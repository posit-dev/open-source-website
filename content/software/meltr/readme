
<!-- README.md is generated from README.Rmd. Please edit that file -->

# meltr

<!-- badges: start -->

[![R-CMD-check](https://github.com/r-lib/meltr/workflows/R-CMD-check/badge.svg)](https://github.com/r-lib/meltr/actions)
[![Codecov test
coverage](https://codecov.io/gh/r-lib/meltr/branch/main/graph/badge.svg)](https://app.codecov.io/gh/r-lib/meltr?branch=main)
<!-- badges: end -->

<p align="center">
<img src="https://nacnudus.github.io/duncangarmonsway/posts/2018-12-29-meltcsv/im_melting_wicked_witch_of_the_west.jpg" alt="The wicked witch of the west saying 'I'm Melting, Melting!!!!!'">
</p>

The goal of ‘meltr’ is to provide a fast and friendly way to read
non-rectangular data (like ragged forms of ‘csv’, ‘tsv’, and ‘fwf’).

Standard tools like
[`readr::read_csv()`](https://readr.tidyverse.org/reference/read_delim.html)
can cope to some extent with unusual inputs, like files with empty rows
or newlines embedded in strings. But some files are so wacky that
standard tools don’t work at all, and instead you have to take the file
to pieces and reassemble to get structured data you can work with.

The meltr package provides tools to do this.

## Installation

You can install the released version of meltr from CRAN with:

``` r
install.packages("meltr")
```

Or you can install the development version with:

``` r
# install.packages("devtools")
devtools::install_github("r-lib/meltr")
```

## The problem with non-rectangular data

Here’s a contrived example that breaks two assumptions made by common
tools like `readr::read_csv()`.

1.  There are more cells in some rows than others.
2.  There are mixed data types within each column.

In contrast, the `melt_csv()` function reads the file one cell at a
time, importing each cell of the file into a whole row of the final data
frame.

``` r
writeLines("Help,,007,I'm
1960-09-30,FALSE,trapped in,7,1.21
non-rectangular,data,NA", "messy.csv")

library(meltr)

melt_csv("messy.csv")
#> # A tibble: 12 × 4
#>      row   col data_type value          
#>    <dbl> <dbl> <chr>     <chr>          
#>  1     1     1 character Help           
#>  2     1     2 missing   <NA>           
#>  3     1     3 character 007            
#>  4     1     4 character I'm            
#>  5     2     1 date      1960-09-30     
#>  6     2     2 logical   FALSE          
#>  7     2     3 character trapped in     
#>  8     2     4 integer   7              
#>  9     2     5 double    1.21           
#> 10     3     1 character non-rectangular
#> 11     3     2 character data           
#> 12     3     3 missing   <NA>
```

The output of `melt_csv()` gives us:

- A data frame of results – structured data about un-structured data!
- Rows of data corresponding to cells of the input data.
- Empty cells such as the cell on row 1, but not missing cells at the
  ends of rows 1 and 3.
- The raw, unconverted data, no data type conversion is attempted –
  every value is imported as a string, and the `data_type` column merely
  gives meltr’s best guess of what the data types ought to be.

What are some ways you can you use this? To begin with, you can do some
simple manipulations with ordinary functions.

For example you could extract the words.

``` r
library(dplyr)
#> 
#> Attaching package: 'dplyr'
#> The following objects are masked from 'package:stats':
#> 
#>     filter, lag
#> The following objects are masked from 'package:base':
#> 
#>     intersect, setdiff, setequal, union

data <- melt_csv("messy.csv")

data %>%
  filter(data_type == "character")
#> # A tibble: 6 × 4
#>     row   col data_type value          
#>   <dbl> <dbl> <chr>     <chr>          
#> 1     1     1 character Help           
#> 2     1     3 character 007            
#> 3     1     4 character I'm            
#> 4     2     3 character trapped in     
#> 5     3     1 character non-rectangular
#> 6     3     2 character data
```

Or find if there are missing entries.

``` r
data %>%
  filter(data_type == "missing")
#> # A tibble: 2 × 4
#>     row   col data_type value
#>   <dbl> <dbl> <chr>     <chr>
#> 1     1     2 missing   <NA> 
#> 2     3     3 missing   <NA>
```
