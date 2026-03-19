---
title: readr 0.2.0
people:
  - Hadley Wickham
date: '2015-10-28'
categories:
  - Data Wrangling
slug: readr-0-2-0
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


readr 0.2.0 is now available on CRAN. readr makes it easy to read many types of tabular data, including csv, tsv and fixed width. Compared to base equivalents like `read.csv()`, readr is much faster and gives more convenient output: it never converts strings to factors, can parse date/times, and it doesn't munge the column names.

This is a big release, so below I describe the new features divided into four main categories:

  * Improved support for international data.

  * Column parsing improvements.

  * File parsing improvements, including support for comments.

  * Improved writers.

There were too many minor improvements and bug fixes to describe in detail here. See the [release notes](https://github.com/hadley/readr/releases/tag/v0.2.0) for a complete list.

## Internationalisation

readr now has a strategy for dealing with settings that vary across languages and localities: **locales**. A locale, created with `locale()`, includes:

  * The names of months and days, used when parsing dates.

  * The default time zone, used when parsing datetimes.

  * The character encoding, used when reading non-ASCII strings.

  * Default date format, used when guessing column types.

  * The decimal and grouping marks, used when reading numbers.

I'll cover the most important of these parameters below. For more details, see `vignette("locales")`.
To override the default US-centric locale, you pass a custom locale to `read_csv()`, `read_tsv()`, or `read_fwf()`. Rather than showing those funtions here, I'll use the `parse_*()` functions because they work with character vectors instead of a files, but are otherwise identical.

### Names of months and days

The first argument to `locale()` is `date_names` which controls what values are used for month and day names. The easiest way to specify them is with a ISO 639 language code:

```r
locale("ko") # Korean
#> <locale>
#> Numbers:  123,456.78
#> Formats:  %Y%.%m%.%d / %H:%M
#> Timezone: UTC
#> Encoding: UTF-8
#> <date_names>
#> Days:   일요일 (일), 월요일 (월), 화요일 (화), 수요일 (수), 목요일 (목),
#>         금요일 (금), 토요일 (토)
#> Months: 1월, 2월, 3월, 4월, 5월, 6월, 7월, 8월, 9월, 10월, 11월, 12월
#> AM/PM:  오전/오후
locale("fr") # French
#> <locale>
#> Numbers:  123,456.78
#> Formats:  %Y%.%m%.%d / %H:%M
#> Timezone: UTC
#> Encoding: UTF-8
#> <date_names>
#> Days:   dimanche (dim.), lundi (lun.), mardi (mar.), mercredi (mer.),
#>         jeudi (jeu.), vendredi (ven.), samedi (sam.)
#> Months: janvier (janv.), février (févr.), mars (mars), avril (avr.), mai
#>         (mai), juin (juin), juillet (juil.), août (août),
#>         septembre (sept.), octobre (oct.), novembre (nov.),
#>         décembre (déc.)
#> AM/PM:  AM/PM
```

This allows you to parse dates in other languages:

```r
parse_date("1 janvier 2015", "%d %B %Y", locale = locale("fr"))
#> [1] "2015-01-01"
parse_date("14 oct. 1979", "%d %b %Y", locale = locale("fr"))
#> [1] "1979-10-14"
```

### Timezones

readr assumes that times are in [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time), aka UTC. UTC is the best timezone for data because it doesn't have daylight savings. If your data isn't already in UTC, you'll need to supply a `tz` in the locale:

```r
parse_datetime("2001-10-10 20:10")
#> [1] "2001-10-10 20:10:00 UTC"
parse_datetime("2001-10-10 20:10",
  locale = locale(tz = "Pacific/Auckland"))
#> [1] "2001-10-10 20:10:00 NZDT"
parse_datetime("2001-10-10 20:10",
  locale = locale(tz = "Europe/Dublin"))
#> [1] "2001-10-10 20:10:00 IST"
```

List all available times zones with `OlsonNames()`. If you're American, note that "EST" is not Eastern Standard Time – it's a Canadian time zone that doesn't have DST! Instead of relying on ambiguous abbreivations, use:

  * PST/PDT = "US/Pacific"

  * CST/CDT = "US/Central"

  * MST/MDT = "US/Mountain"

  * EST/EDT = "US/Eastern"

### Default formats

Locales also provide default date and time formats. The time format isn't currently used for anything, but the date format is used when guessing column types. The default date format is `%Y-%m-%d` because that's unambiguous:

```r
str(parse_guess("2010-10-10"))
#>  Date[1:1], format: "2010-10-10"
```

If you're an American, you might want you use your illogical date sytem::

```r
str(parse_guess("01/02/2013"))
#>  chr "01/02/2013"
str(parse_guess("01/02/2013",
  locale = locale(date_format = "%d/%m/%Y")))
#>  Date[1:1], format: "2013-02-01"
```

### Character encoding

All readr functions yield strings encoded in UTF-8. This encoding is the most likely to give good results in the widest variety of settings. By default, readr assumes that your input is also in UTF-8, which is less likely to be the case, especially when you're working with older datasets. To parse a dataset that's not in UTF-8, you need to a supply an `encoding`.
The following code creates a string encoded with latin1 (aka ISO-8859-1), and shows how it's different from the string encoded as UTF-8, and how to parse it with readr:

```r
x <- "Émigré cause célèbre déjà vu.\n"
y <- stringi::stri_conv(x, "UTF-8", "Latin1")

# These strings look like they're identical:
x
#> [1] "Émigré cause célèbre déjà vu.\n"
y
#> [1] "Émigré cause célèbre déjà vu.\n"
identical(x, y)
#> [1] TRUE

# But they have different encodings:
Encoding(x)
#> [1] "UTF-8"
Encoding(y)
#> [1] "latin1"

# That means while they print the same, their raw (binary)
# representation is actually rather different:
charToRaw(x)
#>  [1] c3 89 6d 69 67 72 c3 a9 20 63 61 75 73 65 20 63 c3 a9 6c c3 a8 62 72
#> [24] 65 20 64 c3 a9 6a c3 a0 20 76 75 2e 0a
charToRaw(y)
#>  [1] c9 6d 69 67 72 e9 20 63 61 75 73 65 20 63 e9 6c e8 62 72 65 20 64 e9
#> [24] 6a e0 20 76 75 2e 0a

# readr expects strings to be encoded as UTF-8. If they're
# not, you'll get weird characters
parse_character(x)
#> [1] "Émigré cause célèbre déjà vu.\n"
parse_character(y)
#> [1] "\xc9migr\xe9 cause c\xe9l\xe8bre d\xe9j\xe0 vu.\n"

# If you know the encoding, supply it:
parse_character(y, locale = locale(encoding = "latin1"))
#> [1] "Émigré cause célèbre déjà vu.\n"
```

If you don't know what encoding the file uses, try `guess_encoding()`. It's not 100% perfect (as it's fundamentally a heuristic), but should at least get you pointed in the right direction:

```r
guess_encoding(y)
#>     encoding confidence
#> 1 ISO-8859-2        0.4
#> 2 ISO-8859-1        0.3

# Note that the first guess produces a valid string,
# but isn't correct:
parse_character(y, locale = locale(encoding = "ISO-8859-2"))
#> [1] "Émigré cause célčbre déjŕ vu.\n"
# But ISO-8859-1 is another name for latin1
parse_character(y, locale = locale(encoding = "ISO-8859-1"))
#> [1] "Émigré cause célèbre déjà vu.\n"
```

### Numbers

Some countries use the decimal point, while others use the decimal comma. The `decimal_mark` option controls which readr uses when parsing doubles:

```r
parse_double("1,23", locale = locale(decimal_mark = ","))
#> [1] 1.23
```

The `big_mark` option describes which character is used to space groups of digits. Do you write `1,000,000`, `1.000.000`, `1 000 000`, or `1'000'000`? Specifying the grouping mark allows `parse_number()` to parse large number as they're commonly written:

```r
parse_number("1,234.56")
#> [1] 1234.56

# dplyr is smart enough to guess that if you're using , for
# decimals then you're probably using . for grouping:
parse_number("1.234,56", locale = locale(decimal_mark = ","))
#> [1] 1234.56
```

## Column parsing improvements

One of the most useful parts of readr are the column parsers: the tools that turns character input into usefully typed data frame columns. This process is now described more fully in a new vignette: `vignette("column-types")`.
By default, column types are guessed by looking at the data. I've made a number of tweaks to make it more likely that your code will load correctly the first time:

  * readr now looks at the first 1000 rows (instead of just the first 100) when guessing column types: this only takes a fraction more time, but should hopefully yield better guesses for more inputs.

  * `col_date()` and `col_datetime()` no longer recognise partial dates like 19, 1900, 1900-01. These triggered many false positives and after re-reading the ISO8601 spec, I believe they actually refer to periods of time, so should not be parsed into a specific instant.

  * `col_integer()` no longer recognises values started with zeros (e.g. 0001) as these are often used as identifiers.

  * `col_number()` will automatically recognise numbers containing the grouping mark (see below for more details).

But you can override these defaults with the `col_types()` argument. In this version, `col_types` gains some much needed flexibility:

  * New `cols()` function takes of assembling the list of column types, and with its `.default` argument, allows you to control the default column type:

```r
read_csv("x,y\n1,2", col_types = cols(.default = "c"))
#> Source: local data frame [1 x 2]
#>
#>       x     y
#>   (chr) (chr)
#> 1     1     2
```

You can refer to parsers with their full name (e.g. `col_character()`) or their one letter abbreviation (e.g. `c`). The default value of `.default` is "?": guess the type of column from the data.

  * `cols_only()` allows you to load only the specified columns:

```r
read_csv("a,b,c\n1,2,3", col_types = cols_only("b" = "?"))
#> Source: local data frame [1 x 1]
#>
#>       b
#>   (int)
#> 1     2
```

Many of the individual parsers have also been improved:

  * `col_integer()` and `col_double()` no longer silently ignore trailing characters after the number.

  * New `col_number()`/`parse_number()` replace the old `col_numeric()`/ `parse_numeric()`. This parser is less flexible, so it's less likely to silently ignored bad input. It's designed specifically to read currencies and percentages. It only reads the first number from a string, ignoring the grouping mark defined by the locale:

```r
parse_number("1,234,566")
#> [1] 1234566
parse_number("$1,234")
#> [1] 1234
parse_number("27%")
#> [1] 27
```

  * New `parse_time()` and `col_time()` allow you to parse times. They have an optional `format` argument, that uses the same components as `parse_datetime()`. If `format` is omitted, they use a flexible parser that looks for hours, then an optional colon, then minutes, then an optional colon, then optional seconds, then optional am/pm.

```r
parse_time(c("1:45 PM", "1345", "13:45:00"))
#> [1] 13:45:00 13:45:00 13:45:00
```

`parse_time()` returns the number of seconds since midnight as an integer with class "time". readr includes a basic print method.

  * `parse_date()`/`col_date()` and `parse_datetime()`/`col_datetime()` gain two new format strings: "%+" skips one or more non-digits, and `%p` reads in AM/PM (and am/pm).

## File parsing improvements

`read_csv()`, `read_tsv()`, and `read_delim()` gain extra arguments that allow you to parse more files:

  * Multiple NA values can be specified by passing a character vector to `na`. The default has been changed to `na = c("", "NA")`.

```r
read_csv("a,b\n.,NA\n1,3", na = c(".", "NA"))
#> Source: local data frame [2 x 2]
#>
#>       a     b
#>   (int) (int)
#> 1    NA    NA
#> 2     1     3
```

  * New `comment` argument allows you to ignore all text after a string:

```r
read_csv(
"#This is a comment
#This is another comment
a,b
1,10
2,20", comment = "#")
#> Source: local data frame [2 x 2]
#>
#>       a     b
#>   (int) (int)
#> 1     1    10
#> 2     2    20
```

  * `trim_ws` argument controls whether leading and trailing whitespace is removed. It defaults to `TRUE`.

```r
read_csv("a,b\n     1,     2")
#> Source: local data frame [1 x 2]
#>
#>       a     b
#>   (int) (int)
#> 1     1     2
read_csv("a,b\n     1,     2", trim_ws = FALSE)
#> Source: local data frame [1 x 2]
#>
#>        a      b
#>    (chr)  (chr)
#> 1      1      2
```

Specifying the wrong number of column names, or having rows with an unexpected number of columns, now gives a warning, rather than an error:

```r
read_csv("a,b,c\n1,2\n1,2,3,4")
#> Warning: 2 parsing failures.
#> row col  expected    actual
#>   1  -- 3 columns 2 columns
#>   2  -- 3 columns 4 columns
#> Source: local data frame [2 x 3]
#>
#>       a     b     c
#>   (int) (int) (int)
#> 1     1     2    NA
#> 2     1     2     3
```

Note that the warning message now also shows you the first five problems. I hope this will often allow you to iterate immediately, rather than having to look at the full `problems()`.

## Writers

Despite the name, readr also provides some tools for writing data frames to disk. In this version there are three output functions:

  * `write_csv()` and `write_tsv()` write tab and comma delimted files, and `write_delim()` writes with user specified delimiter.

  * `write_rds()` and `read_rds()` wrap around `readRDS()` and `saveRDS()`, defaulting to no compression, because you're usually more interested in saving time (expensive) than disk space (cheap).

All these functions invisibly return their output so you can use them as part of a pipeline:

```r
my_df %>%
  some_manipulation() %>%
  write_csv("interim-a.csv") %>%
  some_more_manipulation() %>%
  write_csv("interim-b.csv") %>%
  even_more_manipulation() %>%
  write_csv("final.csv")
```

You can now control how missing values are written with the `na` argument, and the quoting algorithm has been further refined to only add quotes when needed: when the string contains a quote, the delimiter, a new line or the same text as missing value.
Output for doubles now uses the same precision as R, and POSIXt vectors are saved in a ISO8601 compatible format.
For testing, you can use `format_csv()`, `format_tsv()`, and `format_delim()` to write csv to a string:

```r
mtcars %>%
  head(4) %>%
  format_csv() %>%
  cat()
#> mpg,cyl,disp,hp,drat,wt,qsec,vs,am,gear,carb
#> 21,6,160,110,3.9,2.62,16.46,0,1,4,4
#> 21,6,160,110,3.9,2.875,17.02,0,1,4,4
#> 22.8,4,108,93,3.85,2.32,18.61,1,1,4,1
#> 21.4,6,258,110,3.08,3.215,19.44,1,0,3,1
```

This is particularly useful for generating [reprexes](https://github.com/jennybc/reprex).

