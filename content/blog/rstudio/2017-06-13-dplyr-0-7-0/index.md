---
title: dplyr 0.7.0
people:
  - Hadley Wickham
date: '2017-06-13'
categories:
- Packages
- tidyverse
slug: dplyr-0-7-0
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
---


I'm pleased to announce that dplyr 0.7.0 is now on CRAN! (This was dplyr 0.6.0 previously; more on that below.) dplyr provides a "grammar" of data transformation, making it easy and elegant to solve the most common data manipulation challenges. dplyr supports multiple backends: as well as in-memory data frames, you can also use it with remote SQL databases. If you haven't heard of dplyr before, the best place to start is the [Data transformation](http://r4ds.had.co.nz/transform.html) chapter in [R for Data Science](http://r4ds.had.co.nz).

You can install the latest version of dplyr with:

```r
install.packages("dplyr")
```

## Features

dplyr 0.7.0 is a major release including over 100 improvements and bug fixes, as described in the [release notes](https://github.com/tidyverse/dplyr/releases/tag/v0.7.0). In this blog post, I want to discuss one big change and a handful of smaller updates. This version of dplyr also saw a major revamp of database connections. That's a big topic, so it'll get its own blog post next week.

### Tidy evaluation

The biggest change is a new system for programming with dplyr, called **tidy evaluation**, or tidy eval for short. Tidy eval is a system for capturing expressions and later evaluating them in the correct context. It is is important because it allows you to interpolate values in contexts where dplyr usually works with expressions:

```r
my_var <- quo(homeworld)

starwars %>%
  group_by(!!my_var) %>%
  summarise_at(vars(height:mass), mean, na.rm = TRUE)
#> # A tibble: 49 x 3
#>         homeworld   height  mass
#>
#>  1       Alderaan 176.3333  64.0
#>  2    Aleen Minor  79.0000  15.0
#>  3         Bespin 175.0000  79.0
#>  4     Bestine IV 180.0000 110.0
#>  5 Cato Neimoidia 191.0000  90.0
#>  6          Cerea 198.0000  82.0
#>  7       Champala 196.0000   NaN
#>  8      Chandrila 150.0000   NaN
#>  9   Concord Dawn 183.0000  79.0
#> 10       Corellia 175.0000  78.5
#> # ... with 39 more rows
```

This makes it possible to write your functions that work like dplyr functions, reducing the amount of copy-and-paste in your code:

```r
starwars_mean <- function(my_var) {
  my_var <- enquo(my_var)

  starwars %>%
    group_by(!!my_var) %>%
    summarise_at(vars(height:mass), mean, na.rm = TRUE)
}
starwars_mean(homeworld)
```

You can also use the new `.data` pronoun to refer to variables with strings:

```r
my_var <- "homeworld"

starwars %>%
  group_by(.data[[my_var]]) %>%
  summarise_at(vars(height:mass), mean, na.rm = TRUE)
```

This is useful when you're writing packages that use dplyr code because it avoids an annoying note from `R CMD check`.

To learn more about how tidy eval helps solve data analysis challenge, please read the new [programming with dplyr](http://dplyr.tidyverse.org/articles/programming.html) vignette. Tidy evaluation is implemented in the [rlang](http://rlang.tidyverse.org) package, which also provides a vignette on the [theoretical underpinnings](http://rlang.tidyverse.org/articles/tidy-evaluation.html). Tidy eval is a rich system and takes a while to get your head around it, but we are confident that learning tidy eval will pay off, especially as it roles out to other packages in the tidyverse (tidyr and ggplot2 are next on the todo list).

The introduction of tidy evaluation means that the standard evaluation (underscored) version of each main verb (`filter_()`, `select_()` etc) is no longer needed, and so these functions have been deprecated (but remain around for backward compatibility).

### Character encoding

We have done a lot of work to ensure that dplyr works with encodings other than Latin1 on Windows. This is most likely to affect you if you work with data that contains Chinese, Japanese, or Korean (CJK) characters. dplyr should now just work with such data. Please let us know if you have problems!

### New datasets

dplyr has some new datasets that will help write more interesting examples:

  * `starwars`, shown above, contains information about characters from the Star Wars movies, sourced from the [Star Wars API](https://swapi.co). It contains a number of list-columns.

```r
starwars
#> # A tibble: 87 x 13
#>                  name height  mass    hair_color  skin_color eye_color
#>
#>  1     Luke Skywalker    172    77         blond        fair      blue
#>  2              C-3PO    167    75                  gold    yellow
#>  3              R2-D2     96    32           white, blue       red
#>  4        Darth Vader    202   136          none       white    yellow
#>  5        Leia Organa    150    49         brown       light     brown
#>  6          Owen Lars    178   120   brown, grey       light      blue
#>  7 Beru Whitesun lars    165    75         brown       light      blue
#>  8              R5-D4     97    32            white, red       red
#>  9  Biggs Darklighter    183    84         black       light     brown
#> 10     Obi-Wan Kenobi    182    77 auburn, white        fair blue-gray
#> # ... with 77 more rows, and 7 more variables: birth_year ,
#> #   gender , homeworld , species , films ,
#> #   vehicles , starships
```

  * `storms` has the trajectories of ~200 tropical storms. It contains a strong grouping structure.

```r
storms
#> # A tibble: 10,010 x 13
#>     name  year month   day  hour   lat  long              status category
#>
#>  1   Amy  1975     6    27     0  27.5 -79.0 tropical depression       -1
#>  2   Amy  1975     6    27     6  28.5 -79.0 tropical depression       -1
#>  3   Amy  1975     6    27    12  29.5 -79.0 tropical depression       -1
#>  4   Amy  1975     6    27    18  30.5 -79.0 tropical depression       -1
#>  5   Amy  1975     6    28     0  31.5 -78.8 tropical depression       -1
#>  6   Amy  1975     6    28     6  32.4 -78.7 tropical depression       -1
#>  7   Amy  1975     6    28    12  33.3 -78.0 tropical depression       -1
#>  8   Amy  1975     6    28    18  34.0 -77.0 tropical depression       -1
#>  9   Amy  1975     6    29     0  34.4 -75.8      tropical storm        0
#> 10   Amy  1975     6    29     6  34.0 -74.8      tropical storm        0
#> # ... with 10,000 more rows, and 4 more variables: wind ,
#> #   pressure , ts_diameter , hu_diameter
```

  * `band_members`, `band_instruments` and `band_instruments2` has a tiny amount of data about bands. It's designed to be very simple so you can illustrate how joins work without getting distracted by the details of the data.

```r
band_members
#> # A tibble: 3 x 2
#>    name    band
#>
#> 1  Mick  Stones
#> 2  John Beatles
#> 3  Paul Beatles
band_instruments
#> # A tibble: 3 x 2
#>    name  plays
#>
#> 1  John guitar
#> 2  Paul   bass
#> 3 Keith guitar
```

### New and improved verbs

  * The `pull()` generic allows you to extract a single column either by name or position. It's similar to `select()` but returns a vector, rather than a smaller tibble.

```r
mtcars %>% pull(-1) %>% str()
#>  num [1:32] 4 4 1 1 2 1 4 2 2 4 ...
mtcars %>% pull(cyl) %>% str()
#>  num [1:32] 6 6 4 6 8 6 8 4 4 6 ...
```

Thanks to [Paul Poncet](https://github.com/paulponcet) for the idea!

  * `arrange()` for grouped data frames gains a `.by_group` argument so you can choose to sort by groups if you want to (defaults to `FALSE`).

  * All single table verbs now have scoped variants suffixed with `_if()`, `_at()` and `_all()`. Use these if you want to do something to every variable (`_all`), variables selected by their names (`_at`), or variables that satisfy some predicate (`_if`).

```r
iris %>% summarise_if(is.numeric, mean)
starwars %>% select_if(Negate(is.list))
storms %>% group_by_at(vars(month:hour))
```

### Other important changes

  * Local join functions can now control how missing values are matched. The default value is `na_matches = "na"`, which treats two missing values as equal. To prevent missing values from matching, use `na_matches = "never"`.

You can change the default behaviour by calling `pkgconfig::set_config("dplyr::na_matches", "never")`.

  * `bind_rows()` and `combine()` are more strict when coercing. Logical values are no longer coerced to integer and numeric. Date, POSIXct and other integer or double-based classes are no longer coerced to integer or double to avoid dropping important metadata. We plan to continue improving this interface in the future.

## Breaking changes

From time-to-time I discover that I made a mistake in an older version of dplyr and developed what is now a clearly suboptimal API. If the problem isn't too big, I try to just leave it - the cost of making small improvements is not worth it when compared to the cost of breaking existing code. However, there are bigger improvements where I believe the short-term pain of breaking code is worth the long-term payoff of a better API.

Regardless, it's still frustrating when an update to dplyr breaks your code. To minimise this pain, I plan to do two things going forward:

  * Adopt an odd-even release cycle so that API breaking changes only occur in odd numbered releases. Even numbered releases will only contain bug fixes and new features. This is why I've skipped dplyr 0.6.0 and gone directly to dplyr 0.7.0.

  * Invest time in developing better tools isolating packages across projects so that you can choose when to upgrade a package on a project-by-project basis, and if something goes wrong, easily roll back to a version that worked. Look for news about this later in the year.

## Contributors

dplyr is truly a community effort. Apart from the dplyr team (myself, [Kirill Müller](https://github.com/krlmlr), and [Lionel Henry](https://github.com/lionel-)), this release wouldn't have been possible without patches from [Christophe Dervieux](https://github.com/cderv), [Dean Attali](https://github.com/daattali), [Ian Cook](https://github.com/ianmcook), [Ian Lyttle](https://github.com/ijlyttle), [Jake Russ](https://github.com/JakeRuss), [Jay Hesselberth](https://github.com/jayhesselberth), [Jennifer (Jenny) Bryan](https://github.com/jennybc), [@lindbrook](https://github.com/lindbrook), [Mauro Lepore](https://github.com/maurolepore), [Nicolas Coutin](https://github.com/npjc), [Daniel](https://github.com/strengejacke), [Tony Fischetti](https://github.com/tonyfischetti), [Hiroaki Yutani](https://github.com/yutannihilation) and [Sergio Oller](https://github.com/zeehio). Thank you all for your contributions!

