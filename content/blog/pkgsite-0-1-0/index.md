---
title: "pkgsite 0.1.0: Convert your `.Rd` files to Quarto"
date: 2026-05-22
people:
  - Edgar Ruiz
description: >
  Convert your R package documentation into Quarto files and use them to build
  your site.
image: "logo.png"
image-alt: "A flow diagram showing an Rd icon on the left, an arrow pointing to a cardboard box labeled pkgsite with a globe on its face and a cat peeking out, then another arrow pointing to the Quarto logo on the right."
topics:
  - Publishing
languages:
  - R
---

We are happy to introduce `pkgsite`. It reads the compiled `.Rd` files in your
R package and converts them into `.qmd` files. It can also automatically create
a reference index page that lists all your exported functions. You can customize
the format of both using templates, then let Quarto render the HTML. `pkgsite`
is now available on CRAN, to install use:

```r
install.packages("pkgsite")
```

`pkgsite` is inspired by Python's [`Quartodoc`](https://machow.github.io/quartodoc/get-started/overview.html),
which does the same for Python packages.

## Why `pkgsite`?

The main website builder for R packages is [`pkgdown`](https://pkgdown.r-lib.org/).
It goes all the way to a finished, publication-ready HTML website in one step,
and for most packages that is exactly what you want. It is mature, has a large
ecosystem of themes and extensions, and just works.

`pkgsite`, on the other hand, only creates `.qmd` files with the help content.
You decide how to structure the site around them, and Quarto handles the final
HTML output. Two cases where we have seen it make a difference are:

- Examples that require local resources
- Unified R and Python Quarto sites

### Examples that require local resources

Some packages depend on things that are not available on automated build and
publishing platforms such as GitHub Actions or Netlify: databases, large
language models, or Spark clusters. Running their examples there is not
feasible, yet you still want working, rendered documentation.

Quarto's [freeze](https://quarto.org/docs/projects/code-execution.html#freeze)
solves this cleanly. You render the site once locally where those resources are
available, commit the `_freeze/` folder alongside your source, and GitHub
rebuilds the site on every push without re-executing a single line of code.

The [`mall`](https://mlverse.github.io/mall/) and
[`lang`](https://mlverse.github.io/lang/) packages are concrete examples.
Their function examples call an LLM, so they cannot run on those platforms.
With `pkgsite` and freeze, rendering happens on a developer machine where the
model is accessible, and the frozen output travels with the repository.

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

## Getting started

From within your package directory, one call does the work:

```r
library(pkgsite)
write_reference()
```

`write_reference()` creates a `reference/index.qmd` that links to all your
exported functions, and converts each `.Rd` file in `man/` into its own `.qmd`
reference page.

You can customize its behavior through arguments. For example, if you want to
skip running the examples when Quarto renders the reference pages:

```r
write_reference(examples = FALSE, not_run_examples = FALSE)
```

Calling it without arguments reads any configuration from a `pkgsite:` section
at the top level of `_quarto.yml`. Following the same convention as `Quartodoc`,
this is where you set the package root, the output folder, templates, and
optionally how functions are grouped and ordered in the index:

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

If you omit `contents`, `pkgsite` falls back to grouping by `roxygen2`
`@family` tags, then alphabetical order. You only need to re-run
`write_reference()` when you add, rename, or remove exported functions.

### What a generated page looks like

`rd_to_qmd()` converts a single `.Rd` file and returns the Quarto content
as a character vector, useful for inspecting the output without writing
any files:

```r
rd_to_qmd("write_reference.Rd")
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


## Customizing the page layout

The layout of every reference page and the index is driven by a Quarto template
file that uses `{{{{section.name}}}}` placeholders. The defaults work well for
most packages, but if you want to re-order sections, add a logo, link to source
code, or adjust per-page frontmatter, you can supply your own template. The
[Customize the pages](https://edgararuiz.github.io/pkgsite/articles/customize.html)
article covers the full template reference.

## Publishing to GitHub Pages

To publish your site automatically on every push to `main`, you will need a
GitHub Actions workflow. It is also worth knowing that your rendered function
names can automatically become links that point to their own reference pages,
making the site much easier to navigate. We have an article that covers how to
set up the GitHub Actions job and includes an example. You can find it on the
`pkgsite` website here:
[GitHub Pages](https://edgararuiz.github.io/pkgsite/articles/github-actions.html).

## Get started

The full documentation lives at
[edgararuiz.github.io/pkgsite](https://edgararuiz.github.io/pkgsite/), and the
source is on [GitHub](https://github.com/edgararuiz/pkgsite). Issues and
feature requests go to the
[issue tracker](https://github.com/edgararuiz/pkgsite/issues).
