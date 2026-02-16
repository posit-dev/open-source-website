# urlchecker

<!-- badges: start -->
[![R-CMD-check](https://github.com/r-lib/urlchecker/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/r-lib/urlchecker/actions/workflows/R-CMD-check.yaml)
[![Codecov test coverage](https://codecov.io/gh/r-lib/urlchecker/graph/badge.svg)](https://app.codecov.io/gh/r-lib/urlchecker)
<!-- badges: end -->

The goal of urlchecker is to run the URL checks from R 4.1 in older versions of R and automatically update URLs as needed.

It also uses concurrent requests, so is generally much faster than the URL checks from the tools package.

## Installation

Install the released version from CRAN

```r
install.packages("urlchecker")
```

Or the development version from GitHub:

```r
# install.packages("pak")
pak::pak("r-lib/urlchecker")
```

## Usage

``` r
library(urlchecker)

# `url_check()` will check all URLs in a package, as is done by CRAN when
# submitting a package.
url_check("path/to/pkg")

# `url_update()` will check all URLs in a package, then update any 301
# redirects automatically to their new location.
url_update("path/to/pkg")
```

## Code of Conduct

Please note that the urlchecker project is released with a 
[Contributor Code of Conduct](https://r-lib.github.io/urlchecker/CODE_OF_CONDUCT.html).
By contributing to this project, you agree to abide by its terms.
