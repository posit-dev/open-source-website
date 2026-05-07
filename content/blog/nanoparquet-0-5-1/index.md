---
title: nanoparquet 0.5.1
date: 2026-04-30T00:00:00.000Z
people:
  - Gábor Csárdi
description: >
  nanoparquet 0.5.1 brings lots of bug fixes and a few new features: list
  columns, `bit64::integer64` and `blob::blob` support, writing Parquet to the
  standard output.
image: featured.jpg
image-alt: >
  A close-up of an assorted chocolate box divided into six compartments, each
  holding multiple different types of chocolates: truffles, chocolate-dipped
  sticks, caramel clusters, and layered bars.
topics:
  - Data Wrangling
software:
  - nanoparquet
languages:
  - R
tags:
  - packages
  - parquet
  - rlib
  - tidyverse
photo:
  url: https://pixabay.com/photos/chocolate-box-square-brown-white-7892542
  author: ykaiavu
source: tidyverse
nohero: false
hidesubscription: false
---


<!--
TODO:
- [x] Add image (1920×1080 PNG or JPG) and image-alt
- [x] Trim topics, software, and languages to only what applies
- [ ] Open a PR against main for a Netlify preview
-->

We're very chuffed to announce the release of
[nanoparquet](https://nanoparquet.r-lib.org/) 0.5.1 (and 0.5.0).
nanoparquet is a small, self-sufficient R package for reading and
writing Parquet files.

You can install it from CRAN with:

``` r
install.packages("nanoparquet")
```

This blog post will go over some of the improvements in nanoparquet 0.5.0
and 0.5.1.

You can see a full list of changes in the release notes
[here](https://github.com/r-lib/nanoparquet/releases/tag/v0.5.0) and
[here](https://github.com/r-lib/nanoparquet/releases/tag/v0.5.1).

``` r
library(nanoparquet)
```

## List columns

Parquet has a `LIST` type for columns whose values are variable-length
sequences of scalars. nanoparquet 0.5.0 adds support for reading and
writing such columns.

> **Note:** for now nanoparquet supports one level of nesting: each
> element of a list column must be an atomic vector of a single type,
> not a list of lists. All elements in a column must have the same scalar
> type.

To write a list column, put a regular R list into your data frame.
Each element must be an atomic vector (integer, double, or character),
`NULL` for a missing list, or an empty vector for an empty list.
`NA` values inside an element vector encode missing elements.

``` r
df <- data.frame(id = 1:4)
df$scores <- list(c(80L, 95L, 70L), c(100L), NULL, integer(0))
write_parquet(df, tmp <- tempfile(fileext = ".parquet"))
```

``` r
read_parquet_schema(tmp)
```

    # A data frame: 5 × 14
      file_name  r_col name  r_type type  type_length repetition_type converted_type
      <chr>      <int> <chr> <chr>  <chr>       <int> <chr>           <chr>         
    1 /var/fold…    NA sche… <NA>   <NA>           NA <NA>            <NA>          
    2 /var/fold…     1 id    integ… INT32          NA REQUIRED        INT_32        
    3 /var/fold…     2 scor… list(… <NA>           NA OPTIONAL        LIST          
    4 /var/fold…     2 list  <NA>   <NA>           NA REPEATED        <NA>          
    5 /var/fold…     2 elem… <NA>   INT32          NA OPTIONAL        INT_32        
    # ℹ 6 more variables: logical_type <I<list>>, num_children <int>, scale <int>,
    #   precision <int>, field_id <int>, children <list>

`read_parquet()` reads `LIST` columns back as R list columns:

``` r
as.data.frame(read_parquet(tmp))
```

      id     scores
    1  1 80, 95, 70
    2  2        100
    3  3       NULL
    4  4           

`infer_parquet_schema()` shows how nanoparquet maps each column to a Parquet
type. For list columns, the `r_type` shows e.g. `list(integer)`:

``` r
infer_parquet_schema(df)[2:7]
```

    # A data frame: 4 × 6
      r_col name    r_type        type  type_length repetition_type
      <int> <chr>   <chr>         <chr>       <int> <chr>          
    1     1 id      integer       INT32          NA REQUIRED       
    2     2 scores  list(integer) <NA>           NA OPTIONAL       
    3     2 list    <NA>          <NA>           NA REPEATED       
    4     2 element <NA>          INT32          NA OPTIONAL       

A `LIST` column occupies three rows in the schema: the outer list node,
a repeated group node, and the leaf element node.

When you need to specify the element type explicitly, you can use
`parquet_schema()`:

``` r
schema <- parquet_schema(
  id     = "INT32",
  scores = list("LIST", element = "INT32")
)
write_parquet(df, tmp2 <- tempfile(fileext = ".parquet"), schema = schema)
```

``` r
read_parquet_schema(tmp2)
```

    # A data frame: 5 × 14
      file_name  r_col name  r_type type  type_length repetition_type converted_type
      <chr>      <int> <chr> <chr>  <chr>       <int> <chr>           <chr>         
    1 /var/fold…    NA sche… <NA>   <NA>           NA <NA>            <NA>          
    2 /var/fold…     1 id    integ… INT32          NA REQUIRED        <NA>          
    3 /var/fold…     2 scor… list(… <NA>           NA OPTIONAL        LIST          
    4 /var/fold…     2 list  <NA>   <NA>           NA REPEATED        <NA>          
    5 /var/fold…     2 elem… <NA>   INT32          NA OPTIONAL        INT_32        
    # ℹ 6 more variables: logical_type <I<list>>, num_children <int>, scale <int>,
    #   precision <int>, field_id <int>, children <list>

## New types

### `bit64::integer64`

Parquet's `INT64` type holds 64-bit integers. R's native `integer` is
only 32 bits, so nanoparquet has mapped `INT64` to `double` by default.
nanoparquet 0.5.1 adds support for `bit64::integer64`, which gives you true
64-bit integer arithmetic in R.

`write_parquet()` now writes `bit64::integer64` columns as `INT64`:

``` r
library(bit64)
df2 <- data.frame(id = as.integer64(c(1e18, 2e18, 3e18)))
write_parquet(df2, tmp3 <- tempfile(fileext = ".parquet"))
read_parquet_schema(tmp3)
```

    # A data frame: 2 × 14
      file_name  r_col name  r_type type  type_length repetition_type converted_type
      <chr>      <int> <chr> <chr>  <chr>       <int> <chr>           <chr>         
    1 /var/fold…    NA sche… <NA>   <NA>           NA <NA>            <NA>          
    2 /var/fold…     1 id    double INT64          NA REQUIRED        INT_64        
    # ℹ 6 more variables: logical_type <I<list>>, num_children <int>, scale <int>,
    #   precision <int>, field_id <int>, children <list>

To read `INT64` columns back as `bit64::integer64` instead of the default
`double`, use the `read_int64_type` option. The bit64 package must be
installed; if it isn't, nanoparquet throws a clear error.

``` r
read_parquet(tmp3, options = parquet_options(read_int64_type = "integer64"))
```

    # A data frame: 3 × 1
           id
      <int64>
    1    0e18
    2    2e18
    3    3e18

### `blob::blob`

`read_parquet()` previously returned raw `BYTE_ARRAY` and
`FIXED_LEN_BYTE_ARRAY` columns (i.e. those without a string, UUID, or
decimal annotation) as plain lists of raw vectors. They are now returned as
`blob::blob` objects, which print more neatly and come with the full set of
blob helpers. `write_parquet()` now also accepts `blob::blob` columns, so
round-tripping binary data is straightforward:

``` r
library(blob)
df3 <- data.frame(id = 1:3)
df3$payload <- blob::blob(
  charToRaw("hello"),
  charToRaw("world"),
  charToRaw("!")
)
write_parquet(df3, tmp4 <- tempfile(fileext = ".parquet"))
as.data.frame(read_parquet(tmp4))
```

      id   payload
    1  1 blob[5 B]
    2  2 blob[5 B]
    3  3 blob[1 B]

## nanoparquet as a filter

In Unix, a *filter* is a program that reads from standard input and writes
to standard output, making it a composable building block in shell pipelines.
`write_parquet()` now supports writing to standard output via
`file = ":stdout:"`:

``` r
write_parquet(mtcars, ":stdout:")
```

The most common use case is from the command line:

``` sh
Rscript --quiet -e 'nanoparquet::write_parquet(mtcars, ":stdout:")' > mtcars.parquet
```

You can build this into a data pipeline. For example, to convert a CSV
to Parquet, and then process Parquet with another tool in one shot,
without an intermediate `.parquet` file on the disk, you can do:

``` sh
cat data.csv |
  Rscript --quiet -e '
    df <- read.csv(file("stdin"))
    nanoparquet::write_parquet(df, ":stdout:")
  ' | another-parquet-tool
```

Since nanoparquet 0.4.0, `read_parquet()` can also read from an R
connection, so you can pipe Parquet data *in* as well:

``` r
url <- "https://raw.githubusercontent.com/r-lib/nanoparquet/main/inst/extdata/userdata1.parquet"
con <- pipe(paste("curl --silent", url))
df <- read_parquet(con)
```

## Acknowledgements

We thank all contributors to nanoparquet so far, for opening issues,
submitting pull requests, and providing feedback:
[@Aariq](https://github.com/Aariq),
[@alvarocombo](https://github.com/alvarocombo),
[@apalacio9502](https://github.com/apalacio9502),
[@atsyplenkov](https://github.com/atsyplenkov),
[@cboettig](https://github.com/cboettig),
[@ChandlerLutz](https://github.com/ChandlerLutz),
[@cmrnp](https://github.com/cmrnp),
[@D3SL](https://github.com/D3SL),
[@damonbayer](https://github.com/damonbayer),
[@DavideMessinaARS](https://github.com/DavideMessinaARS),
[@eitsupi](https://github.com/eitsupi),
[@gksmyth](https://github.com/gksmyth),
[@hadley](https://github.com/hadley),
[@jack-davison](https://github.com/jack-davison),
[@jeroenjanssens](https://github.com/jeroenjanssens),
[@lbm364dl](https://github.com/lbm364dl),
[@lschneiderbauer](https://github.com/lschneiderbauer),
[@mrcaseb](https://github.com/mrcaseb),
[@pmarks](https://github.com/pmarks),
[@PMassicotte](https://github.com/PMassicotte),
[@r2evans](https://github.com/r2evans),
[@RealTYPICAL](https://github.com/RealTYPICAL),
[@tanho63](https://github.com/tanho63),
[@thisisnic](https://github.com/thisisnic),
[@torfason](https://github.com/torfason),
[@TurnaevEvgeny](https://github.com/TurnaevEvgeny),
[@Upipa](https://github.com/Upipa),
[@vankesteren](https://github.com/vankesteren),
[@vincentarelbundock](https://github.com/vincentarelbundock),
[@wlandau](https://github.com/wlandau),
[@YipengUva](https://github.com/YipengUva), and
[@yutannihilation](https://github.com/yutannihilation).
