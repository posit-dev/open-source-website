
<!-- README.md is generated from README.Rmd. Please edit that file -->

# yaml

<!-- badges: start -->

[![R-CMD-check](https://github.com/r-lib/yaml/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/r-lib/yaml/actions/workflows/R-CMD-check.yaml)
[![Codecov test
coverage](https://codecov.io/gh/r-lib/yaml/graph/badge.svg)](https://app.codecov.io/gh/r-lib/yaml)
<!-- badges: end -->

yaml provides R bindings to [libyaml](https://pyyaml.org/wiki/LibYAML),
a fast [YAML](https://yaml.org/) parser and emitter.

## Installation

Install from CRAN:

``` r
install.packages("yaml")
```

Or install the development version from GitHub:

``` r
# install.packages("pak")
pak::pak("r-lib/r-yaml")
```

## Usage

``` r
library(yaml)
```

Parse YAML with `yaml.load()` or `read_yaml()`:

``` r
yaml.load(
  "
- 1
- 2
- 3
"
)
#> [1] 1 2 3

yaml.load(
  "
a: 1
b: 2
"
)
#> $a
#> [1] 1
#> 
#> $b
#> [1] 2
```

Convert R objects to YAML with `as.yaml()` or `write_yaml()`:

``` r
cat(as.yaml(list(a = 1:3, b = 4:6)))
#> a:
#> - 1
#> - 2
#> - 3
#> b:
#> - 4
#> - 5
#> - 6
```

See `vignette("yaml")` for more details on handlers, formatting options,
and advanced usage.
