
# xopen

> Open System Files, URLs, Anything

<!-- badges: start -->
[![R-CMD-check](https://github.com/r-lib/xopen/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/r-lib/xopen/actions/workflows/R-CMD-check.yaml)
[![](https://www.r-pkg.org/badges/version/xopen)](https://www.r-pkg.org/pkg/xopen)
[![CRAN RStudio mirror downloads](https://cranlogs.r-pkg.org/badges/xopen)](https://www.r-pkg.org/pkg/xopen)
[![Codecov test coverage](https://codecov.io/gh/r-lib/xopen/graph/badge.svg)](https://app.codecov.io/gh/r-lib/xopen)
<!-- badges: end -->

Cross platform solution to open files, directories or URLs with their
associated programs. Inspired by `shell.exec()`,
https://github.com/pwnall/node-open and
https://github.com/sindresorhus/opn

## Installation

Stable version:

```r
install.packages("xopen")
```

Development version:

```r
pak::pak("r-lib/xopen")
```

## Usage

```r
library(xopen)
```

Open a file:

```r
xopen("test.R")
```

Open a URL:

```r
xopen("https://ps.r-lib.org")
```

URL with given app:

```r
chrome <- function() {
  switch(
    get_os(),
    win = "Chrome",
    macos = "google chrome",
    other = "google-chrome")
}
xopen("https://processx.r-lib.org", app = chrome())
```

Open a given app (or switch to it, if already open):

```r
xopen(app = chrome())
```

App and arguments. (You need to quit Chrome for this to work):
```r
xopen(app = c(chrome(), "--incognito", "https://github.com"))
```

## License

MIT © RStudio
