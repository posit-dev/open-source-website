---
title: "Data transformation with dplyr"
resource_type: cheatsheet
date: 2024-06-15
description: "Quick reference guide for data manipulation with dplyr. Covers select, filter, mutate, summarize, and more."
download_url: "https://rstudio.github.io/cheatsheets/data-transformation.pdf"
software:
  - dplyr
languages:
  - R
people:
  - Hadley Wickham
---

Master data transformation with this comprehensive cheatsheet covering all essential dplyr functions. Learn how to efficiently filter rows, select columns, create new variables, and summarize data using the grammar of data manipulation.

dplyr functions work with pipes and expect tidy data. In tidy data:

- Each variable is in its own column
- Each observation, or case, is in its own row

**Pipes:** `x |> f(y)` becomes `f(x, y)`

```r
library(dplyr)
```

## Summarize cases

Create summary statistics tables:

- `summarize()` - Compute table of summaries
- `count()` - Count rows in each group
- `tally()`, `add_count()`, `add_tally()` - Additional counting helpers

## Group cases

- `group_by()` - Create grouped copies for separate manipulation
- `.by` argument - Alternative syntax within functions
- `rowwise()` - Group data into individual rows
- `ungroup()` - Return ungrouped copy

## Manipulate cases

### Extract cases

- `filter()` - Extract rows meeting logical criteria
- `distinct()` - Remove duplicate rows
- `slice()` - Select rows by position
- `slice_sample()` - Randomly select rows
- `slice_min()` / `slice_max()` - Select lowest/highest values
- `slice_head()` / `slice_tail()` - Select first/last rows

### Arrange cases

- `arrange()` - Order rows; use `desc()` for reverse order

### Add cases

- `add_row()` - Add one or more rows

## Manipulate variables

### Extract variables

- `pull()` - Extract column as vector
- `select()` - Extract columns as table
- `relocate()` - Move columns to new positions

### Select helpers

Use with `select()`: `contains()`, `ends_with()`, `starts_with()`, `matches()`, `everything()`, `num_range()`, `:` range notation, `all_of()`, `any_of()`, negation with `!`

### Multiple variables

- `across()` - Summarize/mutate multiple columns similarly
- `c_across()` - Compute across columns in row-wise data

### Make new variables

- `mutate()` - Compute new columns
- `rename()` - Rename columns
- `rename_with()` - Rename using a function

## Vectorized functions

For use with `mutate()`:

**Offset:** `lag()`, `lead()`

**Cumulative aggregate:** `cumall()`, `cumany()`, `cummax()`, `cummean()`, `cummin()`, `cumprod()`, `cumsum()`

**Ranking:** `cume_dist()`, `dense_rank()`, `min_rank()`, `ntile()`, `percent_rank()`, `row_number()`

**Math:** Arithmetic operators, logarithm functions, comparison operators, `between()`, `near()`

**Miscellaneous:** `case_when()`, `coalesce()`, `if_else()`, `na_if()`, `pmax()`, `pmin()`

## Summary functions

For use with `summarize()`:

**Count:** `n()`, `n_distinct()`, `sum(!is.na())`

**Position:** `mean()`, `median()`

**Logical:** `mean()` for proportions of TRUE, `sum()` for counts of TRUE

**Order:** `first()`, `last()`, `nth()`

**Rank:** `quantile()`, `min()`, `max()`

**Spread:** `IQR()`, `mad()`, `sd()`, `var()`

## Combine tables

### Combine variables

- `bind_cols()` - Place tables side by side

### Combine cases

- `bind_rows()` - Stack tables vertically

### Mutating joins

- `left_join()` - Include all rows from left table
- `right_join()` - Include all rows from right table
- `inner_join()` - Include only matching rows
- `full_join()` - Include all rows from both tables

### Filtering joins

- `semi_join()` - Rows of x with matches in y
- `anti_join()` - Rows of x without matches in y

### Nest join

- `nest_join()` - Inner join with nested results

Use `by = join_by()` for specifying column matches.

### Set operations

`intersect()`, `setdiff()`, `union()`, `union_all()`, `setequal()`
