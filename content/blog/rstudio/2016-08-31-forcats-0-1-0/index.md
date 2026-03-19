---
title: 'forcats 0.1.0 '
people:
  - Hadley Wickham
date: '2016-08-31'
categories:
- Packages
- tidyverse
slug: forcats-0-1-0
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
- tidyverse
ported_from: rstudio
port_status: in-progress
---


I'm excited to announce forcats, a new package for categorical variables, or factors. Factors have a bad rap in R because they often turn up when you don't want them. That's because historically, factors were more convenient than character vectors, as discussed in [_stringsAsFactors: An unauthorized biography_](http://simplystatistics.org/2015/07/24/stringsasfactors-an-unauthorized-biography/) by Roger Peng, and [_stringsAsFactors = <sigh>_](http://notstatschat.tumblr.com/post/124987394001/stringsasfactors-sigh) by Thomas Lumley.

If you use packages from the tidyverse (like [tibble](http://r4ds.had.co.nz/tibbles.html) and [readr](http://r4ds.had.co.nz/data-import.html)) you don't need to worry about getting factors when you don't want them. But factors are a useful data structure in their own right, particularly for modelling and visualisation, because they allow you to control the order of the levels. Working with factors in base R can be a little frustrating because of a handful of missing tools. The goal of forcats is to fill in those missing pieces so you can access the power of factors with a minimum of pain.

Install forcats with:

```r
install.packages("forcats")
```

forcats provides two main types of tools to change either the values or the order of the levels. I'll call out some of the most important functions below, using using the included `gss_cat` dataset which contains a selection of categorical variables from the [General Social Survey](http://gss.norc.org/).

```r
library(dplyr)
library(ggplot2)
library(forcats)

gss_cat
#> # A tibble: 21,483 × 9
#>    year       marital   age   race        rincome            partyid
#>   <int>        <fctr> <int> <fctr>         <fctr>             <fctr>
#> 1  2000 Never married    26  White  $8000 to 9999       Ind,near rep
#> 2  2000      Divorced    48  White  $8000 to 9999 Not str republican
#> 3  2000       Widowed    67  White Not applicable        Independent
#> 4  2000 Never married    39  White Not applicable       Ind,near rep
#> 5  2000      Divorced    25  White Not applicable   Not str democrat
#> 6  2000       Married    25  White $20000 - 24999    Strong democrat
#> # ... with 2.148e+04 more rows, and 3 more variables: relig <fctr>,
#> #   denom <fctr>, tvhours <int>
```

## Change level values

You can recode specified factor levels with [`fct_recode()`](https://hadley.github.io/forcats/fct_recode.html):

```r
gss_cat %>% count(partyid)
#> # A tibble: 10 × 2
#>              partyid     n
#>               <fctr> <int>
#> 1          No answer   154
#> 2         Don't know     1
#> 3        Other party   393
#> 4  Strong republican  2314
#> 5 Not str republican  3032
#> 6       Ind,near rep  1791
#> # ... with 4 more rows

gss_cat %>%
  mutate(partyid = fct_recode(partyid,
    "Republican, strong"    = "Strong republican",
    "Republican, weak"      = "Not str republican",
    "Independent, near rep" = "Ind,near rep",
    "Independent, near dem" = "Ind,near dem",
    "Democrat, weak"        = "Not str democrat",
    "Democrat, strong"      = "Strong democrat"
  )) %>%
  count(partyid)
#> # A tibble: 10 × 2
#>                 partyid     n
#>                  <fctr> <int>
#> 1             No answer   154
#> 2            Don't know     1
#> 3           Other party   393
#> 4    Republican, strong  2314
#> 5      Republican, weak  3032
#> 6 Independent, near rep  1791
#> # ... with 4 more rows
```

Note that unmentioned levels are left as is, and the order of the levels is preserved.

[`fct_lump()`](https://hadley.github.io/forcats/fct_relump.html) allows you to lump the rarest (or most common) levels in to a new "other" level. The default behaviour is to collapse the smallest levels in to other, ensuring that it's still the smallest level. For the religion variable that tells us that Protestants out number all other religions, which is interesting, but we probably want more level.

```r
gss_cat %>%
  mutate(relig = fct_lump(relig)) %>%
  count(relig)
#> # A tibble: 2 × 2
#>        relig     n
#>       <fctr> <int>
#> 1      Other 10637
#> 2 Protestant 10846
```

Alternatively you can supply a number of levels to keep, `n`, or minimum proportion for inclusion, `prop`. If you use negative values, `fct_lump()`will change direction, and combine the most common values while preserving the rarest.

```r
gss_cat %>%
  mutate(relig = fct_lump(relig, n = 5)) %>%
  count(relig)
#> # A tibble: 6 × 2
#>        relig     n
#>       <fctr> <int>
#> 1      Other   913
#> 2  Christian   689
#> 3       None  3523
#> 4     Jewish   388
#> 5   Catholic  5124
#> 6 Protestant 10846

gss_cat %>%
  mutate(relig = fct_lump(relig, prop = -0.10)) %>%
  count(relig)
#> # A tibble: 12 × 2
#>                     relig     n
#>                    <fctr> <int>
#> 1               No answer    93
#> 2              Don't know    15
#> 3 Inter-nondenominational   109
#> 4         Native american    23
#> 5               Christian   689
#> 6      Orthodox-christian    95
#> # ... with 6 more rows
```

## Change level order

There are four simple helpers for common operations:

  * [`fct_relevel()`](https://hadley.github.io/forcats/fct_relevel.html) is similar to `stats::relevel()` but allows you to move any number of levels to the front.

  * [`fct_inorder()`](https://hadley.github.io/forcats/fct_inorder.html) orders according to the first appearance of each level.

  * [`fct_infreq()`](https://hadley.github.io/forcats/fct_infreq.html) orders from most common to rarest.

  * [`fct_rev()`](https://hadley.github.io/forcats/fct_rev.html) reverses the order of levels.

[`fct_reorder()`](https://hadley.github.io/forcats/fct_reorder.html) and `fct_reorder2()` are useful for visualisations. `fct_reorder()` reorders the factor levels by another variable. This is useful when you map a categorical variable to position, as shown in the following example which shows the average number of hours spent watching television across religions.

```r
relig <- gss_cat %>%
  group_by(relig) %>%
  summarise(
    age = mean(age, na.rm = TRUE),
    tvhours = mean(tvhours, na.rm = TRUE),
    n = n()
  )

ggplot(relig, aes(tvhours, relig)) + geom_point()
```

![reorder-1](https://rstudioblog.files.wordpress.com/2016/08/reorder-1.png)

```r
ggplot(relig, aes(tvhours, fct_reorder(relig, tvhours))) +
  geom_point()
```

![reorder-2](https://rstudioblog.files.wordpress.com/2016/08/reorder-2.png)

`fct_reorder2()` extends the same idea to plots where a factor is mapped to another aesthetic, like colour. The defaults are designed to make legends easier to read for line plots, as shown in the following example looking at marital status by age.

```r
by_age <- gss_cat %>%
  filter(!is.na(age)) %>%
  group_by(age, marital) %>%
  count() %>%
  mutate(prop = n / sum(n))

ggplot(by_age, aes(age, prop)) +
  geom_line(aes(colour = marital))
```

![reorder2-1](https://rstudioblog.files.wordpress.com/2016/08/reorder2-1.png)

```r
ggplot(by_age, aes(age, prop)) +
  geom_line(aes(colour = fct_reorder2(marital, age, prop))) +
  labs(colour = "marital")
```

![reorder2-2](https://rstudioblog.files.wordpress.com/2016/08/reorder2-2.png)

## Learning more

You can learn more about forcats in [R for data science](http://r4ds.had.co.nz/factors.html), and on the [forcats website](https://hadley.github.io/forcats/).

Please [let me know](https://github.com/hadley/forcats/issues) if you have more factor problems that forcats doesn't help with!

