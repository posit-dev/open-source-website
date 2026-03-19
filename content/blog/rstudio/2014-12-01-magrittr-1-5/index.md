---
title: magrittr 1.5
people:
  - Hadley Wickham
date: '2014-12-01'
categories:
  - Data Wrangling
slug: magrittr-1-5
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
  - RStudio
ported_from: rstudio
port_status: in-progress
software: ["magrittr"]
languages: ["R"]
ported_categories:
  - Packages
---


(Posted on behalf of Stefan Milton Bache)

Sometimes it's the small things that make a big difference. For me, the introduction of our awkward looking friend, `%>%`, was one such little thing. I'd never suspected that it would have such an impact on the way quite a few people think and write `R` (including my own), or that pies would be baked ([see here](https://twitter.com/zevross/status/534703645703405570)) and t-shirts printed ([e.g. here](https://twitter.com/yokkuns/status/505679441381433344)) in honor of the successful three-char-long and slightly overweight operator. Of course a big part of the success is the very fruitful relationship with dplyr and its powerful verbs.

Quite some time went by without any changes to the CRAN version of magrittr. But many ideas have been evaluated and tested, and now we are happy to finally bring an update which brings both some optimization and a few nifty features — we hope that we have managed to strike a balance between simplicity and usefulness and that you will benefit from this update. You can install it now with:

```r
install.packages("magrittr")
```

The underlying evaluation model is more coherent in this release; this makes the new features more natural extensions and improves performance somewhat. Below I'll recap some of the important new features, which include functional sequences, a few specialized supplementary operators and better lambda syntax.

## Functional sequences

The basic (pseudo) usage of the pipe operator goes something like this:

```r
awesome_data <-
  raw_interesting_data %>%
  transform(somehow) %>%
  filter(the_good_parts) %>%
  finalize
```

This statement has three parts: an input, an output, and a sequence transformations. That's suprisingly close to the definition of a function, so in magrittr is really just a convenient way of of defining and applying a function.
A new really useful feature of magrittr 1.5 makes that explicit: you can use `%>%` to not only produce _values_ but also to produce _functions_ (or _functional sequences_)! It's really all the same, except sometimes the function is applied instantly and produces a result, and sometimes it is not, in which case the function itself is returned. In this case, there is no initial value, so we replace that with the dot placeholder. Here is how:

```r
mae <- . %>% abs %>% mean(na.rm = TRUE)
mae(rnorm(10))
#> [1] 0.5605
```

That's equivalent to:

```r
mae <- function(x) {
  mean(abs(x), na.rm = TRUE)
}
```

Even for a short function, this is more compact, and is easier to read as it is defined linearly from left to right.
There are some really cool use cases for this: [functionals](http://adv-r.had.co.nz/Functionals.html)! Consider how clean it is to pass a function to `lapply` or `aggregate`!

```r
info <-
  files %>%
  lapply(. %>% read_file %>% extract(the_goodies))
```

Functions made this way can be indexed with `[` to get a new function containing only a subset of the steps.

## Lambda expressions

The new version makes it clearer that each step is really just a single-statement body of a unary function. What if we need a little more than one command to make a satisfactory "step" in a chain? Before, one might either define a function outside the chain, or even anonymously inside the chain, enclosing the entire definition in parentheses. Now extending that one command is like extending a standard one-command function: enclose whatever you'd like in braces, and that's it:

```r
value %>%
  foo %>% {
    x <- bar(.)
    y <- baz(.)
    x * y
  } %>%
  and_whatever
```

As usual, the name of the argument to that unary function is `.`.

## Nested function calls

In this release the dot (`.`) will work also in nested function calls on the right-hand side, e.g.:

```r
1:5 %>%
  paste(letters[.])
#> [1] "1 a" "2 b" "3 c" "4 d" "5 e"
```

When you use `.` inside a function call, it's used in addition to, not instead of, `.` at the top-level. For example, the previous command is equivalent to:

```r
1:5 %>%
  paste(., letters[.])
#> [1] "1 a" "2 b" "3 c" "4 d" "5 e"
```

If you don't want this behaviour, wrap the function call in `{`:

```r
1:5 %>% {
  paste(letters[.])
}
#> [1] "a" "b" "c" "d" "e"
```

## A few of `%>%`'s friends

We also introduce a few operators. These are supplementary operators that just make some situations more comfortable.
The **tee** operator, `%T>%`, enables temporary branching in a pipeline to apply a few side-effect commands to the current value, like plotting or logging, and is inspired by the Unix tee command. The only difference to `%>%` is that `%T>%` returns the left-hand side rather than the result of applying the right-hand side:

```r
value %>%
  transform %T>%
  plot %>%
  transform(even_more)
```

This is a shortcut for:

```r
value %>%
  transform %>%
  { plot(.); . } %>%
  transform(even_more)
```

because `plot()` doesn't normally return anything that can be piped along!
The **exposition** operator, `%$%`, is a wrapper around `with()`,
which makes it easy to refer to the variables inside a data frame:

```r
mtcars %$%
  plot(mpg, wt)
```

Finally, we also have `%<>%`, the **compound assignment** pipe operator. This must be the first operator in the chain, and it will assign the result of the pipeline to the left-hand side name or expression. It's purpose is to shorten expressions like this:

```r
data$some_variable <-
  data$some_variable %>%
  transform
```

and turn them into something like this:

```r
data$some_variable %<>%
  transform
```

Even a small example like `x %<>% sort` has its appeal!
In summary there is a few new things to get to know; but magrittr is like it always was. Just a little coolr!

