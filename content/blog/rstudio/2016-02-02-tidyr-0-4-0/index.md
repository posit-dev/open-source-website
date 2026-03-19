---
title: tidyr 0.4.0
people:
  - Hadley Wickham
date: '2016-02-02'
categories:
  - Data Wrangling
slug: tidyr-0-4-0
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


I'm pleased to announce tidyr 0.4.0. tidyr makes it easy to "tidy" your data, storing it in a consistent form so that it's easy to manipulate, visualise and model. Tidy data has a simple convention: put variables in the columns and observations in the rows. You can learn more about it in the [tidy data](http://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html) vignette. Install it with:

```r
install.packages("tidyr")
```

There are two big features in this release: support for nested data frames, and improved tools for turning implicit missing values into explicit missing values. These are described in detail below. As well as these big features, all tidyr verbs now handle `grouped_df` objects created by dplyr, `gather()` makes a character `key` column (instead of a factor), and there are lots of other minor fixes and improvements. Please see the [release notes](https://github.com/hadley/tidyr/releases/tag/v0.4.0) for a complete list of changes.

## Nested data frames

`nest()` and `unnest()` have been overhauled to support a new way of structuring your data: the **nested** data frame. In a grouped data frame, you have one row per observation, and additional metadata define the groups. In a nested data frame, you have one **row** per group, and the individual observations are stored in a column that is a list of data frames. This is a useful structure when you have lists of other objects (like models) with one element per group.

For example, take the [gapminder](https://github.com/jennybc/gapminder) dataset:

```r
library(gapminder)
library(dplyr)

gapminder
#> Source: local data frame [1,704 x 6]
#>
#>        country continent  year lifeExp      pop gdpPercap
#>         (fctr)    (fctr) (int)   (dbl)    (int)     (dbl)
#> 1  Afghanistan      Asia  1952    28.8  8425333       779
#> 2  Afghanistan      Asia  1957    30.3  9240934       821
#> 3  Afghanistan      Asia  1962    32.0 10267083       853
#> 4  Afghanistan      Asia  1967    34.0 11537966       836
#> 5  Afghanistan      Asia  1972    36.1 13079460       740
#> 6  Afghanistan      Asia  1977    38.4 14880372       786
#> 7  Afghanistan      Asia  1982    39.9 12881816       978
#> 8  Afghanistan      Asia  1987    40.8 13867957       852
#> ..         ...       ...   ...     ...      ...       ...
```

We can plot the trend in life expetancy for each country:

```r
library(ggplot2)

ggplot(gapminder, aes(year, lifeExp)) +
  geom_line(aes(group = country))
```

![unnamed-chunk-4-1](https://rstudioblog.files.wordpress.com/2016/02/unnamed-chunk-4-1.png)

But it's hard to see what's going on because of all the overplotting. One interesting solution is to summarise each country with a linear model. To do that most naturally, you want one data frame for each country. `nest()` creates this structure:

```r
by_country <- gapminder %>%
  group_by(continent, country) %>%
  nest()

by_country
#> Source: local data frame [142 x 3]
#>
#>    continent     country            data
#>       (fctr)      (fctr)          (list)
#> 1       Asia Afghanistan <tbl_df [12,4]>
#> 2     Europe     Albania <tbl_df [12,4]>
#> 3     Africa     Algeria <tbl_df [12,4]>
#> 4     Africa      Angola <tbl_df [12,4]>
#> 5   Americas   Argentina <tbl_df [12,4]>
#> 6    Oceania   Australia <tbl_df [12,4]>
#> 7     Europe     Austria <tbl_df [12,4]>
#> 8       Asia     Bahrain <tbl_df [12,4]>
#> ..       ...         ...             ...
```

The intriguing thing about this data frame is that it now contains one row per group, and to store the original data we have a new `data` column, a list of data frames. If we look at the first one, we can see that it contains the complete data for Afghanistan (sans grouping columns):

```r
by_country$data[[1]]
#> Source: local data frame [12 x 4]
#>
#>     year lifeExp      pop gdpPercap
#>    (int)   (dbl)    (int)     (dbl)
#> 1   1952    43.1  9279525      2449
#> 2   1957    45.7 10270856      3014
#> 3   1962    48.3 11000948      2551
#> 4   1967    51.4 12760499      3247
#> 5   1972    54.5 14760787      4183
#> 6   1977    58.0 17152804      4910
#> 7   1982    61.4 20033753      5745
#> 8   1987    65.8 23254956      5681
#> ..   ...     ...      ...       ...
```

This form is natural because there are other vectors where you'll have one value per country. For example, we could fit a linear model to each country with [purrr](http://r4ds.had.co.nz/lists.html):

```r
by_country <- by_country %>%
  mutate(model = purrr::map(data, ~ lm(lifeExp ~ year, data = .))
)
by_country
#> Source: local data frame [142 x 4]
#>
#>    continent     country            data   model
#>       (fctr)      (fctr)          (list)  (list)
#> 1       Asia Afghanistan <tbl_df [12,4]> <S3:lm>
#> 2     Europe     Albania <tbl_df [12,4]> <S3:lm>
#> 3     Africa     Algeria <tbl_df [12,4]> <S3:lm>
#> 4     Africa      Angola <tbl_df [12,4]> <S3:lm>
#> 5   Americas   Argentina <tbl_df [12,4]> <S3:lm>
#> 6    Oceania   Australia <tbl_df [12,4]> <S3:lm>
#> 7     Europe     Austria <tbl_df [12,4]> <S3:lm>
#> 8       Asia     Bahrain <tbl_df [12,4]> <S3:lm>
#> ..       ...         ...             ...     ...
```

Because we used `mutate()`, we get an extra column containing one linear model per country.

It might seem unnatural to store a list of linear models in a data frame. However, I think it is actually a really convenient and powerful strategy because it allows you to keep related vectors together. If you filter or arrange the vector of models, there's no way for the other components to get out of sync.

`nest()` got us into this form; `unnest()` gets us out. You give it the list-columns that you want to unnested, and tidyr will automatically repeat the grouping columns. Unnesting `data` gets us back to the original form:

```r
by_country %>% unnest(data)
#> Source: local data frame [1,704 x 6]
#>
#>    continent     country  year lifeExp      pop gdpPercap
#>       (fctr)      (fctr) (int)   (dbl)    (int)     (dbl)
#> 1       Asia Afghanistan  1952    43.1  9279525      2449
#> 2       Asia Afghanistan  1957    45.7 10270856      3014
#> 3       Asia Afghanistan  1962    48.3 11000948      2551
#> 4       Asia Afghanistan  1967    51.4 12760499      3247
#> 5       Asia Afghanistan  1972    54.5 14760787      4183
#> 6       Asia Afghanistan  1977    58.0 17152804      4910
#> 7       Asia Afghanistan  1982    61.4 20033753      5745
#> 8       Asia Afghanistan  1987    65.8 23254956      5681
#> ..       ...         ...   ...     ...      ...       ...
```

When working with models, unnesting is particularly useful when you combine it with [broom](https://github.com/dgrtwo/broom) to extract model summaries:

```r
# Extract model summaries:
by_country %>% unnest(model %>% purrr::map(broom::glance))
#> Source: local data frame [142 x 15]
#>
#>    continent     country            data   model r.squared
#>       (fctr)      (fctr)          (list)  (list)     (dbl)
#> 1       Asia Afghanistan <tbl_df [12,4]> <S3:lm>     0.985
#> 2     Europe     Albania <tbl_df [12,4]> <S3:lm>     0.888
#> 3     Africa     Algeria <tbl_df [12,4]> <S3:lm>     0.967
#> 4     Africa      Angola <tbl_df [12,4]> <S3:lm>     0.034
#> 5   Americas   Argentina <tbl_df [12,4]> <S3:lm>     0.919
#> 6    Oceania   Australia <tbl_df [12,4]> <S3:lm>     0.766
#> 7     Europe     Austria <tbl_df [12,4]> <S3:lm>     0.680
#> 8       Asia     Bahrain <tbl_df [12,4]> <S3:lm>     0.493
#> ..       ...         ...             ...     ...       ...
#> Variables not shown: adj.r.squared (dbl), sigma (dbl),
#>   statistic (dbl), p.value (dbl), df (int), logLik (dbl),
#>   AIC (dbl), BIC (dbl), deviance (dbl), df.residual (int).

# Extract coefficients:
by_country %>% unnest(model %>% purrr::map(broom::tidy))
#> Source: local data frame [284 x 7]
#>
#>    continent     country        term  estimate std.error
#>       (fctr)      (fctr)       (chr)     (dbl)     (dbl)
#> 1       Asia Afghanistan (Intercept) -1.07e+03   43.8022
#> 2       Asia Afghanistan        year  5.69e-01    0.0221
#> 3     Europe     Albania (Intercept) -3.77e+02   46.5834
#> 4     Europe     Albania        year  2.09e-01    0.0235
#> 5     Africa     Algeria (Intercept) -6.13e+02   38.8918
#> 6     Africa     Algeria        year  3.34e-01    0.0196
#> 7     Africa      Angola (Intercept) -6.55e+01  202.3625
#> 8     Africa      Angola        year  6.07e-02    0.1022
#> ..       ...         ...         ...       ...       ...
#> Variables not shown: statistic (dbl), p.value (dbl).

# Extract residuals etc:
by_country %>% unnest(model %>% purrr::map(broom::augment))
#> Source: local data frame [1,704 x 11]
#>
#>    continent     country lifeExp  year .fitted .se.fit
#>       (fctr)      (fctr)   (dbl) (int)   (dbl)   (dbl)
#> 1       Asia Afghanistan    43.1  1952    43.4   0.718
#> 2       Asia Afghanistan    45.7  1957    46.2   0.627
#> 3       Asia Afghanistan    48.3  1962    49.1   0.544
#> 4       Asia Afghanistan    51.4  1967    51.9   0.472
#> 5       Asia Afghanistan    54.5  1972    54.8   0.416
#> 6       Asia Afghanistan    58.0  1977    57.6   0.386
#> 7       Asia Afghanistan    61.4  1982    60.5   0.386
#> 8       Asia Afghanistan    65.8  1987    63.3   0.416
#> ..       ...         ...     ...   ...     ...     ...
#> Variables not shown: .resid (dbl), .hat (dbl), .sigma
#>   (dbl), .cooksd (dbl), .std.resid (dbl).
```

I think storing multiple models in a data frame is a powerful and convenient technique, and I plan to write more about it in the future.

## Expanding

The `complete()` function allows you to turn implicit missing values into explicit missing values. For example, imagine you've collected some data every year basis, but unfortunately some of your data has gone missing:

```r
resources <- frame_data(
  ~year, ~metric, ~value,
  1999, "coal", 100,
  2001, "coal", 50,
  2001, "steel", 200
)
resources
#> Source: local data frame [3 x 3]
#>
#>    year metric value
#>   (dbl)  (chr) (dbl)
#> 1  1999   coal   100
#> 2  2001   coal    50
#> 3  2001  steel   200
```

Here the value for steel in 1999 is implicitly missing: it's simply absent from the data frame. We can use `complete()` to make this missing row explicit, adding that combination of the variables and inserting a placeholder `NA`:

```r
resources %>% complete(year, metric)
#> Source: local data frame [4 x 3]
#>
#>    year metric value
#>   (dbl)  (chr) (dbl)
#> 1  1999   coal   100
#> 2  1999  steel    NA
#> 3  2001   coal    50
#> 4  2001  steel   200
```

With complete you're not limited to just combinations that exist in the data. For example, here we know that there should be data for every year, so we can use the `fullseq()` function to generate every year over the range of the data:

```r
resources %>% complete(year = full_seq(year, 1L), metric)
#> Source: local data frame [6 x 3]
#>
#>    year metric value
#>   (dbl)  (chr) (dbl)
#> 1  1999   coal   100
#> 2  1999  steel    NA
#> 3  2000   coal    NA
#> 4  2000  steel    NA
#> 5  2001   coal    50
#> 6  2001  steel   200
```

In other scenarios, you may not want to generate the full set of combinations. For example, imagine you have an experiment where each person is assigned one treatment. You don't want to expand the combinations of person and treatment, but you do want to make sure every person has all replicates. You can use `nesting()` to prevent the full Cartesian product from being generated:

```r
experiment <- data_frame(
  person = rep(c("Alex", "Robert", "Sam"), c(3, 2, 1)),
  trt  = rep(c("a", "b", "a"), c(3, 2, 1)),
  rep = c(1, 2, 3, 1, 2, 1),
  measurment_1 = runif(6),
  measurment_2 = runif(6)
)
experiment
#> Source: local data frame [6 x 5]
#>
#>   person   trt   rep measurment_1 measurment_2
#>    (chr) (chr) (dbl)        (dbl)        (dbl)
#> 1   Alex     a     1       0.7161        0.927
#> 2   Alex     a     2       0.3231        0.942
#> 3   Alex     a     3       0.4548        0.668
#> 4 Robert     b     1       0.0356        0.667
#> 5 Robert     b     2       0.5081        0.143
#> 6    Sam     a     1       0.6917        0.753

experiment %>% complete(nesting(person, trt), rep)
#> Source: local data frame [9 x 5]
#>
#>    person   trt   rep measurment_1 measurment_2
#>     (chr) (chr) (dbl)        (dbl)        (dbl)
#> 1    Alex     a     1       0.7161        0.927
#> 2    Alex     a     2       0.3231        0.942
#> 3    Alex     a     3       0.4548        0.668
#> 4  Robert     b     1       0.0356        0.667
#> 5  Robert     b     2       0.5081        0.143
#> 6  Robert     b     3           NA           NA
#> 7     Sam     a     1       0.6917        0.753
#> 8     Sam     a     2           NA           NA
#> ..    ...   ...   ...          ...          ...
```

