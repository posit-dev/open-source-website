---
title: purrr 0.2.0
people:
  - Hadley Wickham
date: '2016-01-06'
categories:
  - Data Wrangling
slug: purrr-0-2-0
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


I'm pleased to announce purrr 0.2.0. Purrr fills in the missing pieces in R's functional programming tools, and is designed to make your pure (and now) type-stable functions purrr.

I'm still working out exactly what purrr should do, and how it compares to existing functions in base R, dplyr, and tidyr. One main insight that has affected much of the current version is that functions designed for programming should be type-stable. Type-stability is an idea brought to my attention by Julia. Even though functions in R and Julia can return different types of output, by and large, you should strive to make functions that always return the same type of data structure. This makes functions more robust to varying input, and makes them easier to reason about (and in Julia, to optimise). (But not every function can be type-stable - how could `$` work?)

Purrr 0.2.0 adds type-stable alternatives for maps, flattens, and `try()`, as described below. There were a lot of other minor improvements, bug fixes, and a number of deprecations. Please see the [release notes](https://github.com/hadley/purrr/releases/tag/v0.2.0) for a complete list of changes.

## Type stable maps

A **map** is a function that calls an another function on each element of a vector. Map functions in base R are the "applys": `lapply()`, `sapply()`, `vapply()`, etc. `lapply()` is type-stable: no matter what the inputs are, the output is already a list. `sapply()` is not type-stable: it can return different types of output depending on the input. The following code shows a simple (if somewhat contrived) example of `sapply()` returning either a vector, a matrix, or a list, depending on its inputs:

```r
df <- data.frame(
  a = 1L,
  b = 1.5,
  y = Sys.time(),
  z = ordered(1)
)

df[1:4] %>% sapply(class) %>% str()
#> List of 4
#>  $ a: chr "integer"
#>  $ b: chr "numeric"
#>  $ y: chr [1:2] "POSIXct" "POSIXt"
#>  $ z: chr [1:2] "ordered" "factor"
df[1:2] %>% sapply(class) %>% str()
#>  Named chr [1:2] "integer" "numeric"
#>  - attr(*, "names")= chr [1:2] "a" "b"
df[3:4] %>% sapply(class) %>% str()
#>  chr [1:2, 1:2] "POSIXct" "POSIXt" "ordered" "factor"
#>  - attr(*, "dimnames")=List of 2
#>   ..$ : NULL
#>   ..$ : chr [1:2] "y" "z"
```

This behaviour makes `sapply()` appropriate for interactive use, since it usually guesses correctly and gives a useful data structure. It's not appropriate for use in package or production code because if the input isn't what you expect, it won't fail, and will instead return an unexpected data structure. This typically causes an error further along the process, so you get a confusing error message and it's difficult to isolate the root cause.

Base R has a type-stable version of `sapply()` called `vapply()`. It takes an additional argument that determines what the output will be. purrr takes a different approach. Instead of one function that does it all, purrr has multiple functions, one for each common type of output: `map_lgl()`, `map_int()`, `map_dbl()`, `map_chr()`, and `map_df()`. These either produce the specified type of output or throw an error. This forces you to deal with the problem right away:

```r
df[1:4] %>% map_chr(class)
#> Error: Result 3 is not a length 1 atomic vector
df[1:4] %>% map_chr(~ paste(class(.), collapse = "/"))
#>                a                b                y                z
#>        "integer"        "numeric" "POSIXct/POSIXt" "ordered/factor"
```

Other variants of `map()` have similar suffixes. For example, `map2()` allows you to iterate over two vectors in parallel:

```r
x <- list(1, 3, 5)
y <- list(2, 4, 6)
map2(x, y, c)
#> [[1]]
#> [1] 1 2
#>
#> [[2]]
#> [1] 3 4
#>
#> [[3]]
#> [1] 5 6
```

`map2()` always returns a list. If you want to add together the corresponding values and store the result as a double vector, you can use `map2_dbl()`:

```r
map2_dbl(x, y, `+`)
#> [1]  3  7 11
```

Another map variant is `invoke_map()`, which takes a list of functions and list of arguments. It also has type-stable suffixes:

```r
spread <- list(sd = sd, iqr = IQR, mad = mad)
x <- rnorm(100)

invoke_map_dbl(spread, x = x)
#>        sd       iqr       mad
#> 0.9121309 1.2515807 0.9774154
```

## Type-stable flatten

Another situation when type-stability is important is flattening a nested list into a simpler data structure. Base R has `unlist()`, but it's dangerous because it always succeeds. As an alternative, purrr provides `flatten_lgl()`, `flatten_int()`, `flatten_dbl()`, and `flatten_chr()`:

```r
x <- list(1L, 2:3, 4L)
x %>% str()
#> List of 3
#>  $ : int 1
#>  $ : int [1:2] 2 3
#>  $ : int 4
x %>% flatten() %>% str()
#> List of 4
#>  $ : int 1
#>  $ : int 2
#>  $ : int 3
#>  $ : int 4
x %>% flatten_int() %>% str()
#>  int [1:4] 1 2 3 4
```

## Type-stable `try()`

Another function in base R that is not type-stable is `try()`. `try()` ensures that an expression always succeeds, either returning the original value or the error message:

```r
str(try(log(10)))
#>  num 2.3
str(try(log("a"), silent = TRUE))
#> Class 'try-error'  atomic [1:1] Error in log("a") : non-numeric argument to mathematical function
#>
#>   ..- attr(*, "condition")=List of 2
#>   .. ..$ message: chr "non-numeric argument to mathematical function"
#>   .. ..$ call   : language log("a")
#>   .. ..- attr(*, "class")= chr [1:3] "simpleError" "error" "condition"
```

`safely()` is a type-stable version of try. It always returns a list of two elements, the result and the error, and one will always be `NULL`.

```r
safely(log)(10)
#> $result
#> [1] 2.302585
#>
#> $error
#> NULL
safely(log)("a")
#> $result
#> NULL
#>
#> $error
#> <simpleError in .f(...): non-numeric argument to mathematical function>
```

Notice that `safely()` takes a function as input and returns a "safe" function, a function that never throws an error. A powerful technique is to use `safely()` and `map()` together to attempt an operation on each element of a list:

```r
safe_log <- safely(log)
x <- list(10, "a", 5)
log_x <- x %>% map(safe_log)

str(log_x)
#> List of 3
#>  $ :List of 2
#>   ..$ result: num 2.3
#>   ..$ error : NULL
#>  $ :List of 2
#>   ..$ result: NULL
#>   ..$ error :List of 2
#>   .. ..$ message: chr "non-numeric argument to mathematical function"
#>   .. ..$ call   : language .f(...)
#>   .. ..- attr(*, "class")= chr [1:3] "simpleError" "error" "condition"
#>  $ :List of 2
#>   ..$ result: num 1.61
#>   ..$ error : NULL
```

This is output is slightly inconvenient because you'd rather have a list of three results, and another list of three errors. You can use the new `transpose()` function to switch the order of the first and second levels in the hierarchy:

```r
log_x %>% transpose() %>% str()
#> List of 2
#>  $ result:List of 3
#>   ..$ : num 2.3
#>   ..$ : NULL
#>   ..$ : num 1.61
#>  $ error :List of 3
#>   ..$ : NULL
#>   ..$ :List of 2
#>   .. ..$ message: chr "non-numeric argument to mathematical function"
#>   .. ..$ call   : language .f(...)
#>   .. ..- attr(*, "class")= chr [1:3] "simpleError" "error" "condition"
#>   ..$ : NULL
```

This makes it easy to extract the inputs where the original functions failed, or just keep the good successful result:

```r
results <- x %>% map(safe_log) %>% transpose()

(ok <- results$error %>% map_lgl(is_null))
#> [1]  TRUE FALSE  TRUE
(bad_inputs <- x %>% discard(ok))
#> [[1]]
#> [1] "a"
(successes <- results$result %>% keep(ok) %>% flatten_dbl())
#> [1] 2.302585 1.609438
```

