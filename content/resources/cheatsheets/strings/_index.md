---
title: String manipulation with stringr
image: page-1.png
resource_type: cheatsheet
by: posit
date: '2026-08-01'
description: Manipulate character strings in R with stringr to detect, subset, transform, join, split, and match patterns using regex.
download_url: strings.pdf
people:
- Garrett Grolemund
- Mine Çetinkaya-Rundel
- Averi Perny
- Andy Teucher
- Ryan Zomorrodi
- Curtis Kephart
- Elen Le Foll
- David Díaz Rodríguez
thumbnails:
- page-1.png
- page-2.png
software:
- stringr
languages:
- R
source_files:
- file: strings.key
  format: Keynote
- file: strings.pptx
  format: PowerPoint
translations:
- language: Portuguese (Brazil)
  lang: pt-BR
  file: strings_pt_br.pdf
  edition: stringr 1.4.0
  updated: 2021-08
  people:
  - Eric Scopinho
  source: strings_pt_br.pptx
- language: Spanish
  lang: es
  file: strings_es.pdf
  edition: stringr 1.5.1
  updated: 2024-05
  people:
  - L.P. Rojas Saunero
  - David Díaz Rodríguez
  source: strings_es.pptx
- language: Vietnamese
  lang: vi
  file: strings_vi.pdf
  edition: stringr 1.2.0
  updated: 2017-09
  people:
  - Anh Hoang Duc
---

<!-- Page 1 -->

The **stringr** package provides a set of internally consistent tools for working with character strings, i.e. sequences of characters surrounded by quotation marks.

```r
library(stringr)
```

## Detect Matches

-   `str_detect(string, pattern, negate = FALSE)`: Detect the presence of a pattern match in a string.
    Also `str_like()` for SQL `LIKE`-style wildcard matching (always case-sensitive) and `str_ilike()` for case-insensitive `ILIKE`-style matching.

    
    ```r
    str_detect(fruit, "a")
    str_ilike(fruit, "AP%")
    ```

-   `str_starts(string, pattern, negate = FALSE)`: Detect the presence of a pattern match at the beginning of a string.
    Also `str_ends()`.

    
    ```r
    str_starts(fruit, "a")
    ```

-   `str_which(string, pattern, negate = FALSE)`: Find the indexes of strings that contain a pattern match.

    
    ```r
    str_which(fruit, "a")
    ```

-   `str_locate(string, pattern)`: Locate the positions of pattern matches in a string.
    Also `str_locate_all()`.

    
    ```r
    str_locate(fruit, "a")
    ```

-   `str_count(string, pattern)`: Count the number of matches in a string.

    
    ```r
    str_count(fruit, "a")
    ```

## Mutate Strings

-   `str_sub() <- value`: Replace substrings by identifying the substrings with `str_sub()` and assigning into the results.

    
    ```r
    str_sub(fruit, 1, 3) <- "str"
    ```

-   `str_replace(string, pattern, replacement)`: Replace the first matched pattern in each string.
    Also `str_remove()`.

    
    ```r
    str_replace(fruit, "p", "-")
    ```

-   `str_replace_all(string, pattern, replacement)`: Replace all matched patterns in each string.
    Also `str_remove_all()`.

    
    ```r
    str_replace_all(fruit, "p", "-")
    ```

-   `str_to_lower(string, locale = "en")`^1^: Convert strings to lower case.

    
    ```r
    str_to_lower(sentences)
    ```

-   `str_to_upper(string, locale = "en")`^1^: Convert strings to upper case.

    
    ```r
    str_to_upper(sentences)
    ```

-   `str_to_title(string, locale = "en")`^1^: Convert strings to title case.
    Also `str_to_setence()`.

    
    ```r
    str_to_title(sentences)
    ```

-   `str_to_camel(string)`: onvert strings between programming case styles (`camelCase`, `snake_case`, `kebab-case`).
    Also `str_to_snake(string)` and `str_to_kebab(string)`.

    
    ```r
    str_to_camel("convert this string")
    ```

## Subset Strings

-   `str_sub(string, start = 1L, end = -1L)`: Extract substrings from a character vector.

    
    ```r
    str_sub(fruit, 1, 3)
    str_sub(fruit, -2)
    ```

-   `str_subset(string, pattern, negate = FALSE)`: Return only the strings that contain a pattern match.

    
    ```r
    str_subset(fruit, "p")
    ```

-   `str_extract(string, pattern)`: Return the first pattern match found in each string, as a vector.
    Also `str_extract_all()` to return every pattern match.

    
    ```r
    str_extract(fruit, "[aeiou]")
    ```

-   `str_match(string, pattern)`: Return the first pattern match found in each string, as a matrix with a column for each ( ) group in pattern.
    Also `str_match_all()`.

    
    ```r
    str_match(sentences, "(a|the) ([^ +])")
    ```

## Join and Split

-   `str_c(..., sep = "", collapse = NULL)`: Join multiple strings into a single string.

    
    ```r
    str_c(letters, LETTERS)
    ```

-   `str_flatten(string, collapse = "")`: Combines into a single string, separated by collapse.

    
    ```r
    str_flatten(fruit, ", ")
    ```

-   `str_dup(string, times, sep = "")`: Repeat strings times times, optionally separated by `sep`.
    Also `str_unique()` to remove duplicates.

    
    ```r
    str_dup(fruit, times = 2)
    ```

-   `str_split_fixed(string, pattern, n)`: Split a vector of strings into a matrix of substrings (splitting at occurrences of a pattern match).
    Also `str_split()` to return a list of substrings and `str_split_i()` to return the ith substring.

    
    ```r
    str_split_fixed(sentences, " ", n = 3)
    ```

-   `str_glue(..., .sep = "", .envir = parent.frame())`: Create a string from strings and {expressions} to evaluate.

    
    ```r
    str_glue("Pi is {pi}")
    ```

-   `str_glue_data(.x, ..., .sep = "", .envir = parent.frame(), .na = "NA")`: Use a data frame, list, or environment to create a string from strings and {expressions} to evaluate.

    
    ```r
    str_glue_data(mtcars, "{rownames(mtcars)} has {hp} hp")
    ```

## Manage Lengths

-   `str_length(string)`: The width of strings (i.e. number of code points, which generally equals the number of characters).

    
    ```r
    str_length(fruit)
    ```

-   `str_pad(string, width, side = c("left", "right", "both"), pad = " ")`: Pad strings to constant width.

    
    ```r
    str_pad(fruit, 17)
    ```

-   `str_trunc(string, width, side = c("left", "right", "both"), ellipsis = "...")`: Truncate the width of strings, replacing content with ellipsis.

    
    ```r
    str_trunc(sentences, 6)
    ```

-   `str_trim(string, side = c("left", "right", "both"))`: Trim whitespace from the start and/or end of a string.

    
    ```r
    str_trim(str_pad(fruit, 17))
    ```

-   `str_squish(string)`: Trim white space from each end and collapse multiple spaces into single spaces.

    
    ```r
    str_squish(str_pad(fruit, 17, "both"))
    ```

## Order Strings

-   `str_order(x, decreasing = FALSE, na_last = TRUE, locale = "en", numeric = FALSE, ...)^1^`: Return the vector of indexes that sorts a character vector.

    
    ```r
    fruit[str_order(fruit)]
    ```

-   `str_sort(x, decreasing = FALSE, na_last = TRUE, locale = "en", numeric = FALSE, ...)^1^`: Sort a character vector.

    
    ```r
    str_sort(fruit)
    ```

## Helpers

-   `str_conv(string, encoding)`: Override the encoding of a string.

    
    ```r
    str_conv(fruit, "ISO-8859-1")
    ```

-   `str_view(string, pattern, match = NA)`: View HTML rendering of all regex matches.
    Also `str_view()` to see only the first match.

    
    ```r
    str_view(sentences, "[aeiou]")
    ```

-   `str_equal(x, y, locale = "en", ignore_case = FALSE, ...)`^1^: Determine if two strings are equivalent.

    
    ```r
    str_equal(c("a", "b"), c("a", "c"))
    ```

-   `str_wrap(string, width = 80, indent = 0, exdent = 0)`: Wrap strings into nicely formatted paragraphs.

    
    ```r
    str_wrap(sentences, 20)
    ```

^1^ See <http://bit.ly/ISO639-1> for a complete list of locales.

<!-- Page 2 -->

## Regular Expressions

Regular expressions, or *regexps*, are a concise language for describing patterns in strings.

### Need to Know

Pattern arguments in stringr are interpreted as regular expressions *after any special characters have been parsed*.

In R, you write regular expressions as *strings*, sequences of characters surrounded by quotes(`""`) or single quotes (`''`).

Some characters cannot be directly represented in an R string.
These must be represented as **special characters**, sequences of characters that have a specific meaning, e.g. `\\` represents `\`, `\"` represents `"`, and `\n` represents a new line.
Run `?"'"` to see a complete list.

Because of this, whenever a `\` appears in a regular expression, you must write it as `\\` in the string that represents the regular expression.

Use `writeLines()` to see how R views your string after all special characters have been parsed.

For example, `writeLines("\\.")` will be parsed as `\.`

and `writeLines("\\ is a backslash")` will be parsed as `\ is a backslash`.

### Interpretation

Patterns in stringr are interpreted as regexs.
To change this default, wrap the pattern in one of:

-   `regex(pattern, ignore_case = FALSE, multiline = FALSE, comments = FALSE, dotall = FALSE, ...)`: Modifies a regex to ignore cases, match end of lines as well as end of strings, allow R comments within regexs, and/or to have `.` match everthing including `\n`.

    
    ```r
    str_detect("I", regex("i", TRUE))
    ```

-   `fixed()`: Matches raw bytes but will miss some characters that can be represented in multiple ways (fast).

    
    ```r
    str_detect("\u0130", fixed("i"))
    ```

-   `coll()`: Matches raw bytes and will use locale specific collation rules to recognize characters that can be represented in multiple ways (slow).

    
    ```r
    str_detect("\u0130", coll("i", TRUE, locale = "tr"))
    ```

-   `boundary()`: Matches boundaries between characters, line_breaks, sentences, or words.

    
    ```r
    str_split(sentences, boundary("word"))
    ```

### Match Characters

```r
see <- function(rx) str_view("abc ABC 123\t.!?\\(){}\n", rx)
```

<table>
<caption>1Many base R functions require classes to be wrapped in a second set of \[ \], e.g. **\[\[:digit:\]\]**</caption>
<tr>
<th>

string\
(type this)

</th>
<th>

regex\
(to mean this)

</th>
<th>

matches\
(which matches this)

</th>
<th>

example

</th>
<th>

example output (highlighted characters are in \<\>)

</th>
</tr>
<tr>
<td></td>
<td>

`a (etc.)`

</td>
<td>

`a (etc.)`

</td>
<td>

`see("a")`

</td>
<td>

```
<a>bc ABC 123\t.!?\(){}\n
```

</td>
</tr>
<tr>
<td>

`\\.`

</td>
<td>

`\.`

</td>
<td>

`.`

</td>
<td>

```see("\\.")`` ```

</td>
<td>

```
abc ABC 123\t<.>!?\(){}\n
```

</td>
</tr>
<tr>
<td>

`\\!`

</td>
<td>

`\!`

</td>
<td>

`!`

</td>
<td>

`see("\\!")`

</td>
<td>

```
abc ABC 123\t.<!>?\(){}\n
```

</td>
</tr>
<tr>
<td>

`\\?`

</td>
<td>

`\?`

</td>
<td>

`?`

</td>
<td>

`see("\\?")`

</td>
<td>

```
abc ABC 123\t.!<?>\(){}\n
```

</td>
</tr>
<tr>
<td>

`\\\\`

</td>
<td>

`\\`

</td>
<td>

`\`

</td>
<td>

`see("\\\\")`

</td>
<td>

```
abc ABC 123\t.!?<\>(){}\n
```

</td>
</tr>
<tr>
<td>

`\\(`

</td>
<td>

`\(`

</td>
<td>

`(`

</td>
<td>

`see("\\(")`

</td>
<td>

```
abc ABC 123\t.!?\<(>){}\n
```

</td>
</tr>
<tr>
<td>

`\\)`

</td>
<td>

`\)`

</td>
<td>

`)`

</td>
<td>

`see("\\)")`

</td>
<td>

```
abc ABC 123\t.!?\(<)>{}\n
```

</td>
</tr>
<tr>
<td>

`\\{`

</td>
<td>

`\{`

</td>
<td>

`{`

</td>
<td>

`see("\\{")`

</td>
<td>

```
abc ABC 123\t.!?\()<{>}\n
```

</td>
</tr>
<tr>
<td>

`\\}`

</td>
<td>

`\}`

</td>
<td>

`}`

</td>
<td>

`see("\\}")`

</td>
<td>

```
abc ABC 123\t.!?\(){<}>\n
```

</td>
</tr>
<tr>
<td>

`\\n`

</td>
<td>

`\n`

</td>
<td>

new line (return)

</td>
<td>

`see("\\n")`

</td>
<td>

```
abc ABC 123\t.!?\(){}<\n>
```

</td>
</tr>
<tr>
<td>

`\\t`

</td>
<td>

`\t`

</td>
<td>

tab

</td>
<td>

`see("\\t")`

</td>
<td>

```
abc ABC 123<\t>.!?\(){}\n
```

</td>
</tr>
<tr>
<td>

`\\s`

</td>
<td>

`\s`

</td>
<td>

any whitespace\
(`\S` for non-whitespaces)

</td>
<td>

`see("\\s")`

</td>
<td>

```
abc< >ABC< >123<\t>.!?\(){}<\n>
```

</td>
</tr>
<tr>
<td>

`\\d`

</td>
<td>

`\d`

</td>
<td>

any digit\
(`\D` for non-digits)

</td>
<td>

`see("\\d")`

</td>
<td>

```
abc ABC <1><2><3>\t.!?\(){}\n
```

</td>
</tr>
<tr>
<td>

`\\w`

</td>
<td>

`\w`

</td>
<td>

any word character\
(`\W` for non-word characters)

</td>
<td>

`see("\\w")`

</td>
<td>

```
<a><b><c> <A><B><C> <1><2><3>\t.!?\(){}\n
```

</td>
</tr>
<tr>
<td>

`\\b`

</td>
<td>

`\b`

</td>
<td>

word boundaries

</td>
<td>

`see("\\b")`

</td>
<td>

```
<>abc<> <>ABC<> <>123<>\t.!?\(){}\n
```

</td>
</tr>
<tr>
<td></td>
<td>

`[:digit:]`^1^

</td>
<td>

digits

</td>
<td>

`see("[:digit:]")`

</td>
<td>

```
abc ABC <1><2><3>\t.!?\(){}\n
```

</td>
</tr>
<tr>
<td></td>
<td>

`[:alpha:]`^1^

</td>
<td>

letters

</td>
<td>

`see("[:alpha:]")`

</td>
<td>

```
<a><b><c> <A><B><C> 123\t.!?\(){}\n
```

</td>
</tr>
<tr>
<td></td>
<td>

`[:lower:]`^1^

</td>
<td>

lowercase letters

</td>
<td>

`see("[:lower:]")`

</td>
<td>

```
<a><b><c> ABC 123\t.!?\(){}\n
```

</td>
</tr>
<tr>
<td></td>
<td>

`[:upper:]`^1^

</td>
<td>

uppercase letters

</td>
<td>

`see("[:upper:]")`

</td>
<td>

```
abc <A><B><C> 123\t.!?\(){}\n
```

</td>
</tr>
<tr>
<td></td>
<td>

`[:alnum:]`^1^

</td>
<td>

letters and numbers

</td>
<td>

`see("[:alnum:]")`

</td>
<td>

```
<a><b><c> <A><B><C> <1><2><3>\t.!?\(){}\n
```

</td>
</tr>
<tr>
<td></td>
<td>

`[:punct:]`^1^

</td>
<td>

punctuation

</td>
<td>

`see("[:punct:]")`

</td>
<td>

```
abc ABC 123\t<.><!><?><\><(><)><{><}>\n
```

</td>
</tr>
<tr>
<td></td>
<td>

`[:graph:]`^1^

</td>
<td>

letters, numbers, and punctuation

</td>
<td>

`see("[:graph:]")`

</td>
<td>

```
<a><b><c> <A><B><C> <1><2><3>\t<.><!><?><\><(><)><{><}>\n
```

</td>
</tr>
<tr>
<td></td>
<td>

`[:space:]`^1^

</td>
<td>

space characters (i.e. `\s`)

</td>
<td>

`see("[:space:]")`

</td>
<td>

```
abc< >ABC< >123<\t>.!?\(){}<\n>
```

</td>
</tr>
<tr>
<td></td>
<td>

`[:blank:]`^1^

</td>
<td>

space and tab (but not new line)

</td>
<td>

`see("[:blank:]")`

</td>
<td>

```
abc< >ABC< >123<\t>.!?\(){}\n
```

</td>
</tr>
<tr>
<td></td>
<td>

`.`

</td>
<td>

every character except a new line

</td>
<td>

`see(".")`

</td>
<td>

```
<a><b><c>< ><A><B><C>< ><1><2><3><\t><.><!><?><\><(><)><{><}><\n>
```

</td>
</tr>
</table>

#### Classes

-   The `[:space:]` class includes new line, and the `[:blank:]` class
    -   The `[:blank:]` class includes space and tab (`\t`)
-   The `[:graph:]` class contains all non-space characters, including `[:punct:]`, `[:symbol:]`, `[:alnum:]`, `[:digit:]`, `[:alpha:]`, `[:lower:]`, and `[:upper:]`
    -   `[:punct:]` contains punctuation: `. , : ; ? ! / * @ # - _ " [ ] { } ( )`

    -   `[:symbol:]` contains symbols: `` | ` = + ^ ~ < > $ ``

    -   `[:alnum:]` contains alphanumeric characters, including `[:digit:]`, `[:alpha:]`, `[:lower:]`, and `[:upper:]`

        -   `[:digit:]` contains the digits 0 through 9

        -   `[:alpha:]` contains letters, including `[:upper:]` and `[:lower:]`

            -   `[:upper:]` contains uppercase letters and `[:lower:]` contains lowercase letters
-   The regex `.` contains all characters in the above classes, except new line.

### Alternates

`alt <- function(rx) str_view("abcde", rx)`

<table>
<caption>Alternates</caption>
<tr>
<th>

regexp

</th>
<th>

matches

</th>
<th>

example

</th>
<th>

example output\
(highlighted characters are in \<\>)

</th>
</tr>
<tr>
<td>

`ab|d`

</td>
<td>

or

</td>
<td>

`alt("ab|d")`

</td>
<td>

```
<ab>c<d>e
```

</td>
</tr>
<tr>
<td>

`[abe]`

</td>
<td>

one of

</td>
<td>

`alt("[abe]"`

</td>
<td>

```
<a><b>cd<e>
```

</td>
</tr>
<tr>
<td>

`[^abe]`

</td>
<td>

anything but

</td>
<td>

`alt("[^abe]")`

</td>
<td>

```
ab<c><d>e
```

</td>
</tr>
<tr>
<td>

`[a-c]`

</td>
<td>

range

</td>
<td>

`alt("[a-c]")`

</td>
<td>

```
<a><b><c>de
```

</td>
</tr>
</table>

### Anchors

`anchor <- function(rx) str_view("aaa", rx)`

<table>
<caption>Anchors</caption>
<tr>
<th>

regexp

</th>
<th>

matches

</th>
<th>

example

</th>
<th>

example output
(highlighted characters are in \<\>)

</th>
</tr>
<tr>
<td>

`^a`

</td>
<td>

start of string

</td>
<td>

`anchor("^a")`

</td>
<td>

```
<a>aa
```

</td>
</tr>
<tr>
<td>

`a$`

</td>
<td>

end of string

</td>
<td>

`anchor("a$")`

</td>
<td>

```
aa<a>
```

</td>
</tr>
</table>

### Look Arounds

`look <- function(rx) str_view("bacad", rx)`

<table>
<caption>Look arounds</caption>
<tr>
<th>

regexp

</th>
<th>

matches

</th>
<th>

example

</th>
<th>

example output\
(highlighted characters are in \<\>)

</th>
</tr>
<tr>
<td>

`a(?=c)`

</td>
<td>

followed by

</td>
<td>

`look("a(?=c)")`

</td>
<td>

```
b<a>cad
```

</td>
</tr>
<tr>
<td>

`a(?!c)`

</td>
<td>

not followed by

</td>
<td>

`look("a(?!c)")`

</td>
<td>

```
bac<a>d
```

</td>
</tr>
<tr>
<td>

`(?<=b)a`

</td>
<td>

preceded by

</td>
<td>

`look("(?<=b)a")`

</td>
<td>

```
b<a>cad
```

</td>
</tr>
<tr>
<td>

`(?<!b)a`

</td>
<td>

not preceded by

</td>
<td>

`look("(?<!b)a")`

</td>
<td>

```
bac<a>d
```

</td>
</tr>
</table>

### Quantifiers

`quant <- function(rx) str_view(".a.aa.aaa", rx)`

<table>
<caption>Quantifiers</caption>
<tr>
<th>

regexp

</th>
<th>

matches

</th>
<th>

example

</th>
<th>

example output\
(highlighted characters are in \<\>)

</th>
</tr>
<tr>
<td>

`a?`

</td>
<td>

zero or one

</td>
<td>

`quant("a?")`

</td>
<td>

```
<>.<a><>.<a><a><>.<a><a><a><>
```

</td>
</tr>
<tr>
<td>

`a*`

</td>
<td>

zero or more

</td>
<td>

`quant("a*")`

</td>
<td>

```
<>.<a><>.<aa><>.<aaa><>
```

</td>
</tr>
<tr>
<td>

`a+`

</td>
<td>

one or more

</td>
<td>

`quant("a+")`

</td>
<td>

```
.<a>.<aa>.<aaa>
```

</td>
</tr>
<tr>
<td>

`a{n}`

</td>
<td>

exactly `n`

</td>
<td>

`quant("a{2}")`

</td>
<td>

```
.a.<aa>.<aa>a
```

</td>
</tr>
<tr>
<td>

`a{n, }`

</td>
<td>

`n` or more

</td>
<td>

`quant("a{2,}")`

</td>
<td>

```
.a.<aa>.<aaa>
```

</td>
</tr>
<tr>
<td>

`a{n, m}`

</td>
<td>

between `n` and `m`

</td>
<td>

`quant("a{2,4}")`

</td>
<td>

```
.a.<aa>.<aaa>
```

</td>
</tr>
</table>

### Groups

`ref <- function(rx) str_view("abbaab", rx)`

Use parentheses to set precedent (order of evaluation) and create groups

<table>
<caption>Groups</caption>
<tr>
<th>

regexp

</th>
<th>

matches

</th>
<th>

example

</th>
<th>

example output\
(highlighted characters are in \<\>)

</th>
</tr>
<tr>
<td>

`(ab|d)e`

</td>
<td>

sets precedence

</td>
<td>

`alt("(ab|d)e")`

</td>
<td>

```
abc<de>
```

</td>
</tr>
</table>

Use an escaped number to refer to and duplicate parentheses groups that occur earlier in a pattern.
Refer to each group by its order of appearance

<table>
<caption>More groups</caption>
<tr>
<th>

string\
(type this)

</th>
<th>

regexp\
(to mean this)

</th>
<th>

matches\
(which matches this)

</th>
<th>

example\
(the result is the same as `ref("abba")`)

</th>
<th>

example output\
(highlighted characters are in \<\>)

</th>
</tr>
<tr>
<td>

`\\1`

</td>
<td>

`\1` (etc.)

</td>
<td>

first () group, etc.

</td>
<td>

`ref("(a)(b)\\2\\1")`

</td>
<td>

```
<abba>ab
```

</td>
</tr>
</table>

------------------------------------------------------------------------

CC BY SA Posit Software, PBC • [info\@posit.co](mailto:info@posit.co) • [posit.co](https://posit.co)

Learn more at [stringr.tidyverse.org](https://stringr.tidyverse.org).

Updated: 2026-08.

::: {.cell}

```{.r .cell-code}
packageVersion("stringr")
```

```
[1] '1.6.0'
```

:::

------------------------------------------------------------------------
