---
title: "Introducing pkgsite: Quarto-native reference pages for R packages"
date: 2026-05-22
people:
  - Edgar Ruiz
description: >
  pkgsite converts your R package's Rd files into Quarto files, making it easy
  to build a package website that uses Quarto freeze, custom layouts, and
  combined R and Python reference pages.
image: "logo.png"
image-alt: "A flow diagram showing an Rd icon on the left, an arrow pointing to a cardboard box labeled pkgsite with a globe on its face and a cat peeking out, then another arrow pointing to the Quarto logo on the right."
topics:
  - Publishing
languages:
  - R
---

We are happy to introduce `pkgsite`. It reads the compiled `.Rd` files in your
R package and converts them into `.qmd` reference pages, plus an index that
lists all your exported functions. You arrange and extend those files as needed,
then let Quarto render the HTML. It is now available on CRAN, to install use:

```r
install.packages("pkgsite")
```

## Why `pkgsite`?

[`pkgdown`](https://pkgdown.r-lib.org/) goes all the way to a finished,
publication-ready HTML website in one step, and for most packages that is
exactly what you want: it is mature, has a large ecosystem of themes and
extensions, and just works. `pkgsite`, on the other hand, only creates `.qmd`
files with the help content. You decide how to structure the site around them,
and Quarto handles the final HTML output. Two scenarios where that distinction
matters stand out.

### Examples that require local resources

Some packages depend on things that are not available in CI: databases, large
language models, or Spark clusters. Running their examples on GitHub Actions
is not feasible, yet you still want working, rendered documentation.

Quarto's [freeze](https://quarto.org/docs/projects/code-execution.html#freeze)
solves this cleanly. You render the site once locally where those resources are
available, commit the `_freeze/` folder alongside your source, and GitHub
rebuilds the site on every push without re-executing a single line of code.

The [`mall`](https://mlverse.github.io/mall/) package is a concrete example.
Its function examples call an LLM, so they cannot run in CI. With `pkgsite` and
freeze, rendering happens on a developer machine where the model is accessible,
and the frozen output travels with the repository.

### Unified R and Python sites

If your project ships both an R package and a Python package, you can combine
`pkgsite`'s output with
[`Quartodoc`](https://machow.github.io/quartodoc/get-started/overview.html)'s
output into a single Quarto website. Both tools write `.qmd` reference pages
that Quarto assembles together, giving R and Python users a consistent
experience on one site. The `mall` package's
[reference section](https://mlverse.github.io/mall/reference/) is a live
example: R and Python pages side by side, built from two different tools,
served as one site.

## A portable example

`pkgsite` ships with a small built-in example package so you can try it
without touching your own project:

``` r
library(pkgsite)

example_pkg <- system.file("example", package = "pkgsite")
write_reference(project = example_pkg, folder = tempdir())
```

```
── pkgsite ──────────────────────────────────────────────────────────────────────
Creating index file:
  `/tmp/Rtmp123456/index.qmd`

Converting .Rd to .qmd:
  `path/to/example/man/index_to_qmd.Rd` → `/tmp/Rtmp123456/index_to_qmd.qmd`

  `path/to/example/man/rd_to_list.Rd` → `/tmp/Rtmp123456/rd_to_list.qmd`

  `path/to/example/man/rd_to_qmd.Rd` → `/tmp/Rtmp123456/rd_to_qmd.qmd`
```

`write_reference()` does two things: it creates a `reference/index.qmd` that
links to all your exported functions, and it converts each `.Rd` file in
`man/` to its own `.qmd` reference page.

When used in your own package directory, calling it without arguments reads
any configuration from `_quarto.yml` and defaults to writing files into a
`reference/` folder. You only need to re-run it when you add, rename, or
remove exported functions.

### What a generated page looks like

`rd_to_qmd()` converts a single `.Rd` file and returns the Quarto content
as a character vector, useful for inspecting the output without writing
any files:

``` r
output <- rd_to_qmd("rd_to_qmd.Rd", project = example_pkg)
cat(output, sep = "\n")
```

Here is what `pkgsite` generates for the `rd_to_qmd()` function:

````markdown
---
title: "Converts 'Rd' to Quarto files"
execute:
  eval: true
  freeze: true
---

## rd_to_qmd

## Description

Converts 'Rd' to Quarto files

## Usage

```r
rd_to_qmd(rd_file, project = ".", pkg = NULL, examples = TRUE,
  not_run_examples = FALSE, template = NULL)
```

## Arguments

| Arguments | Description |
|---|---|
| rd_file | The name of the source Rd file |
| project | The path to the root folder of the project. |
| pkg | The path inside the project folder. Use only if the R package itself is in a sub-folder within the project. |
| examples | Flag that sets the examples code chunk to be evaluated when the Quarto document is rendered |
| not_run_examples | Flag that sets the `\dontrun{}` examples code chunk to be evaluated when the Quarto document is rendered |
| template | Path to a custom template file. If `NULL`, `pkgsite` uses its own default. |

## Value

A character vector with the resulting contents of converting the
Rd file format into a Quarto file format.

## See Also

Other Conversion functions: `index_to_qmd()`, `rd_to_list()`

## Examples

```r
library(pkgsite)
rd_to_qmd("rd_to_qmd.Rd", project = ".")
```
````

The result is a plain Quarto document. Because it is plain Quarto, you can
open any generated file and add prose, insert runnable code chunks, or adjust
frontmatter options without any special tooling.

## Configuring via `_quarto.yml`

Following the same convention as `Quartodoc`, `pkgsite` reads from a `pkgsite:`
section at the top level of `_quarto.yml`. Here is the full set of available
options:

```yaml
pkgsite:
  dir: "."                    # path to the package root
  reference:
    dir: reference            # where to write the .qmd files
    not_run_examples: false   # whether to execute \dontrun{} examples
    template: inst/templates/_reference.qmd   # custom page template
    index:
      file: index.qmd         # name of the index file
      template: inst/templates/_index.qmd     # custom index template
      contents:               # optional: custom function grouping
        - section: "Write files"
          contents:
            - write_reference.qmd
            - write_reference_index.qmd
            - write_reference_pages.qmd
        - section: "Conversion"
          contents:
            - rd_to_qmd.qmd
            - rd_to_list.qmd
            - index_to_qmd.qmd
```

Calling `write_reference()` with no arguments picks up this configuration
automatically. You only pass arguments when you need to override a value
for a one-off run.

The optional `contents` key also controls how functions are grouped and ordered
in the index. If you omit it, `pkgsite` falls back to grouping by `roxygen2`
`@family` tags, then alphabetical order.

## Customizing the page layout

The layout of every reference page and the index is driven by a Quarto template
file that uses `{{{{section.name}}}}` placeholders. The defaults work well for
most packages, but if you want to re-order sections, add a logo, link to source
code, or adjust per-page frontmatter, you can supply your own template. The
[Customize the pages](https://edgararuiz.github.io/pkgsite/articles/customize.html)
article covers the full template reference.

## Building and publishing a complete site

`pkgsite` is primarily designed to generate reference pages. To build a complete
package website around them (with a homepage, a changelog, long-form articles,
and a navbar), see the
[Building a full package website with Quarto](https://edgararuiz.github.io/pkgsite/articles/quarto-website.html)
article walks through how the pieces fit together.

For publishing to GitHub Pages, the
[GitHub Pages](https://edgararuiz.github.io/pkgsite/articles/github-actions.html)
article covers a complete GitHub Actions workflow. It also shows how to set up
[`downlit`](https://downlit.r-lib.org/) so that function names in your rendered
pages automatically link to their reference documentation.

## Get started

```r
install.packages("pkgsite")
```

The full documentation lives at
[edgararuiz.github.io/pkgsite](https://edgararuiz.github.io/pkgsite/), and the
source is on [GitHub](https://github.com/edgararuiz/pkgsite). Issues and
feature requests go to the
[issue tracker](https://github.com/edgararuiz/pkgsite/issues).
