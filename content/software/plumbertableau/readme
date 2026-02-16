
<!-- README.md is generated from README.Rmd. Please edit that file -->

# plumbertableau <a href='https://rstudio.github.io/plumbertableau/'><img src='man/figures/logo.svg' align="right" height="139" /></a>

<!-- badges: start -->

[![R-CMD-check](https://github.com/rstudio/plumbertableau/workflows/R-CMD-check/badge.svg)](https://github.com/rstudio/plumbertableau/actions)
[![Codecov test
coverage](https://codecov.io/gh/rstudio/plumbertableau/branch/main/graph/badge.svg)](https://app.codecov.io/gh/rstudio/plumbertableau?branch=main)
[![CRAN
status](https://www.r-pkg.org/badges/version/plumbertableau)](https://CRAN.R-project.org/package=plumbertableau)
<!-- badges: end -->

plumbertableau lets you call external R code in real time from Tableau
workbooks via [Tableau Analytics
Extensions](https://tableau.github.io/analytics-extensions-api/). You
achieve this by writing a plumbertableau extension, which is a
[Plumber](https://www.rplumber.io/) API with some extra annotations —
comments prefixed with `#*`.

``` r
library(plumber)
library(plumbertableau)

#* @apiTitle String utilities
#* @apiDescription Simple functions for mutating strings

#* Capitalize incoming text
#* @tableauArg str_value:[character] Strings to be capitalized
#* @tableauReturn [character] A capitalized string(s)
#* @post /capitalize
function(str_value) {
  toupper(str_value)
}

# The Plumber router modifier tableau_extension is required. This object is a
# function that acts as a plumber router modifier. For more details, see the
# Plumber documentation:
# https://www.rplumber.io/articles/annotations.html#plumber-router-modifier
#* @plumber
tableau_extension
```

plumbertableau extensions are used in Tableau’s *calculated fields*.
Let’s imagine we’ve published our extension to RStudio Connect and have
given it the custom URL `stringutils`. To use our `capitalize`
extension, we’d type the following into a Tableau calculated field, or
just copy and paste it from the automatically generated code samples.
(In real usage, you’ll probably replace `"Hello World"` with references
to Tableau data.)

    SCRIPT_STR("/stringutils/capitalize", "Hello World")

Before you use the extension in Tableau, Tableau needs to be able to
access it. plumbertableau integrates seamlessly with [RStudio
Connect](https://posit.co/products/enterprise/connect/), a commercial
publishing platform that enables R developers to easily publish a
variety of R content types. Connect lets you host multiple extensions by
ensuring that requests from Tableau are passed to the correct extension.
It’s also possible to host plumbertableau extensions on your own
servers.

## Installation

You can install plumbertableau from CRAN or install the latest
development version from GitHub.

``` r
# From CRAN
install.packages("plumbertableau")

# From GitHub
remotes::install_github("rstudio/plumbertableau")

library(plumbertableau)
```

## FAQ

#### I thought Tableau already supports R?

Tableau’s current support for R as an analytics extension is built on
[`Rserve`](https://rforge.net/Rserve/index.html). This approach requires
configuring Rserve in a separate environment and then passing R code as
plain text from Tableau calculated fields to be executed by Rserve.

#### Why would I use this instead of RServe?

The approach suggested here allows specific endpoints to be called,
rather than requiring the Tableau user to write and submit R code in a
plain text field from Tableau. This allows Tableau users to be seperate
from the extension developers. R developers can build extensions that
are then used by Tableau developers who may have no working knowledge of
R.

#### Is RStudio Connect required?

While this package has been designed specifically with RStudio Connect
in mind, it will work independent of RStudio Connect.

#### What are the advantages of RStudio Connect?

RStudio Connect offers a number of advantages as a deployment platform
for Tableau Analytics Extensions:

-   Tableau workbooks can only be configured to use a single extension
    endpoint, which typically limits a workbook to only using one type
    of extension. RStudio Connect can host both R and Python based
    extensions, which means that a single Tableau workbook can use both
    R and Python based extensions hosted on RStudio Connect.
-   R developers can develop extensions in their preferred development
    environment and then publish to RStudio Connect
-   Extensions published to RStudio Connect can be secured to only allow
    access from specific accounts
-   RStudio Connect natively handles
    [R](https://docs.posit.co/connect/admin/r/package-management/)
    and
    [Python](https://docs.posit.co/connect/admin/python/package-management/)
    packages, which allows extensions to seemlessly use different
    versions of underlying packages without creating conflicts.
-   RStudio Connect processes are
    [sandboxed](https://docs.posit.co/connect/admin/process-management/#sandboxing),
    which limits the scope of impact the extension can have on the
    underlying OS.

#### Why can’t I just write my own Plumber API to function as an analytics extension?

Tableau Analytics Extensions are configured to reach out to two specific
endpoints:

-   `/info`: Information about the extension
-   `/evaluate`: Execution endpoint for the extension

plumbertableau automatically generates the `/info` endpoint and reroutes
requests to `/evaluate` to the endpoint defined in the `script` value of
the request body. This allows multiple endpoints to function as
extensions, rather than relying on a single extension operating under
`/evaluate`. These features are intended to allow the R developer to
easily create Tableau Analytics Extensions as standard Plumber APIs
without needing to worry about the lower level implementation.

## Further Reading

You can read more about plumbertableau at
<https://rstudio.github.io/plumbertableau/>. There, you’ll find more
detail about writing plumbertableau extensions, publishing them to
RStudio Connect, configuring Tableau, and using your extensions in
Tableau.
