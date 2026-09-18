
<!-- README.md is generated from README.Rmd. Please edit that file -->

# pkgcache

> Cache CRAN-like metadata and package files

<!-- badges: start -->

[![lifecycle](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://lifecycle.r-lib.org/articles/stages.html)
[![CRAN
status](https://www.r-pkg.org/badges/version/pkgcache)](https://cran.r-project.org/package=pkgcache)
[![R-CMD-check](https://github.com/r-lib/pkgcache/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/r-lib/pkgcache/actions/workflows/R-CMD-check.yaml)
[![Codecov test
coverage](https://codecov.io/gh/r-lib/pkgcache/graph/badge.svg)](https://app.codecov.io/gh/r-lib/pkgcache)
<!-- badges: end -->

Metadata and package cache for CRAN-like repositories. This is a utility
package to be used by package management tools that want to take
advantage of caching.

## Installation

You can install the released version of pkgcache from
[CRAN](https://CRAN.R-project.org) with:

``` r
install.packages("pkgcache")
```

If you need the development version, you can install it from
[GitHub](https://github.com) with:

``` r
pak::pak("r-lib/pkgcache")
```

## Metadata cache

`meta_cache_list()` lists all packages in the metadata cache. It
includes Bioconductor package, and all versions (i.e. both binary and
source) of the packages for the current platform and R version.

(We load the pillar package, because it makes the pkgcache data frames
print nicer, similarly to tibbles.)

``` r
library(pkgcache)
library(pillar)
meta_cache_list()
#> # A data frame: 50,873 × 33
#>    package    version depends suggests license md5sum sha256sum needscompilation
#>    <chr>      <chr>   <chr>   <chr>    <chr>   <chr>  <chr>     <chr>           
#>  1 A3         1.0.0   R (>= … randomF… GPL (>… 71559… "\n     … no              
#>  2 AATtools   0.0.3   R (>= … <NA>     GPL-3   77b8a… "\n     … no              
#>  3 ABACUS     1.0.0   R (>= … rmarkdo… GPL-3   f6450… "\n     … no              
#>  4 ABC.RAP    0.9.0   R (>= … knitr, … GPL-3   0dd81… "\n     … no              
#>  5 ABCanalys… 1.2.1   R (>= … <NA>     GPL-3   fb77c… "\n     … no              
#>  6 ABCoptim   0.15.0  <NA>    testtha… MIT + … 0487b… "\n     … yes             
#>  7 ABCp2      1.2     MASS    <NA>     GPL-2   de0d8…  <NA>     no              
#>  8 ABHgenoty… 1.0.1   <NA>    knitr, … GPL-3   2b2aa… "\n     … no              
#>  9 ABM        0.4.3   <NA>    <NA>     GPL (>… 338a6… "\n     … yes             
#> 10 ABPS       0.3     <NA>    testthat GPL (>… 54a9e… "\n     … no              
#> # ℹ 50,863 more rows
#> # ℹ 25 more variables: imports <chr>, linkingto <chr>, archs <chr>,
#> #   enhances <chr>, priority <chr>, os_type <chr>, license_is_foss <chr>,
#> #   license_restricts_use <chr>, repodir <chr>, rversion <chr>, platform <chr>,
#> #   ref <chr>, type <chr>, direct <lgl>, status <chr>, target <chr>,
#> #   mirror <chr>, sources <list>, filesize <int>, sha256 <chr>, sysreqs <chr>,
#> #   built <chr>, published <chr>, deps <list>, path <chr>
```

`meta_cache_deps()` and `meta_cache_revdeps()` can be used to look up
dependencies and reverse dependencies.

The metadata is updated automatically if it is older than seven days,
and it can also be updated manually with `meta_cache_update()`.

See the `cranlike_metadata_cache` R6 class for a lower level API, and
more control.

## Package cache

Package management tools may use the `pkg_cache_*` functions and in
particular the `package_cache` class, to make use of local caching of
package files.

The `pkg_cache_*` API is high level, and uses a user level cache:

``` r
pkg_cache_summary()
#> $cachepath
#> [1] "/Users/gaborcsardi/Library/Caches/org.R-project.R/R/pkgcache/pkg"
#> 
#> $files
#> [1] 610
#> 
#> $size
#> [1] 640020676
```

``` r
pkg_cache_list()
#> # A data frame: 610 × 11
#>    fullpath    path  package url   etag  sha256 version platform built vignettes
#>    <chr>       <chr> <chr>   <chr> <chr> <chr>  <chr>   <chr>    <chr> <chr>    
#>  1 /Users/gab… bin/… vroom   http… "\"2… d3939… 1.6.5   aarch64… <NA>  <NA>     
#>  2 /Users/gab… bin/… fansi   http… "\"5… c4db0… 1.0.6   aarch64… <NA>  <NA>     
#>  3 /Users/gab… bin/… cli     http… "\"1… 52d9c… 3.6.4   aarch64… <NA>  <NA>     
#>  4 /Users/gab… bin/… bit     http… "\"1… b089c… 4.5.0.1 aarch64… <NA>  <NA>     
#>  5 /Users/gab… bin/… crayon  http… "\"2… 34c13… 1.5.3   aarch64… <NA>  <NA>     
#>  6 /Users/gab… bin/… glue    http… "\"2… 21363… 1.8.0   aarch64… <NA>  <NA>     
#>  7 /Users/gab… bin/… bit64   http… "\"8… 0a141… 4.6.0-1 aarch64… <NA>  <NA>     
#>  8 /Users/gab… bin/… tidyse… http… "\"3… 3d12b… 1.2.1   aarch64… <NA>  <NA>     
#>  9 /Users/gab… bin/… lifecy… http… "\"1… 2ef38… 1.0.4   aarch64… <NA>  <NA>     
#> 10 /Users/gab… bin/… pillar  http… "\"a… 2c06d… 1.10.1  aarch64… <NA>  <NA>     
#> # ℹ 600 more rows
#> # ℹ 1 more variable: rversion <chr>
```

``` r
pkg_cache_find(package = "dplyr")
#> # A data frame: 1 × 11
#>   fullpath     path  package url   etag  sha256 version platform built vignettes
#>   <chr>        <chr> <chr>   <chr> <chr> <chr>  <chr>   <chr>    <chr> <chr>    
#> 1 /Users/gabo… bin/… dplyr   http… "\"1… 0d399… 1.1.4   aarch64… <NA>  <NA>     
#> # ℹ 1 more variable: rversion <chr>
```

`pkg_cache_add_file()` can be used to add a file,
`pkg_cache_delete_files()` to remove files, `pkg_cache_get_files()` to
copy files out of the cache.

The `package_cache` class provides a finer API.

## Installed packages

pkgcache contains a very fast DCF parser to parse `PACKAGES*` files, or
the `DESCRIPTION` files in installed packages. `parse_packages()` parses
all fields from `PACKAGES`, `PACKAGES.gz` or `PACKAGES.rds` files.
`parse_installed()` reads *all* metadata from packages installed into a
library:

``` r
parse_installed()
#> # A data frame: 259 × 92
#>    Package     Title    Version `Authors@R` Description License URL   BugReports
#>    <chr>       <chr>    <chr>   <chr>       <chr>       <chr>   <chr> <chr>     
#>  1 pkgcache    Cache '… 2.2.3.… "c(\n    p… "Metadata … MIT + … "htt… https://g…
#>  2 abind       Combine… 1.4-8   "c(person(… "Combine m… MIT + …  <NA> <NA>      
#>  3 asciicast   Create … 2.3.1.… "c(\n    p… "Record 'a… MIT + … "htt… https://g…
#>  4 askpass     Passwor… 1.2.1   "person(\"… "Cross-pla… MIT + … "htt… https://g…
#>  5 backports   Reimple… 1.5.0   "c(\n    p… "\n    Fun… GPL-2 … "htt… https://g…
#>  6 base64enc   Tools f… 0.1-3    <NA>       "This pack… GPL-2 … "htt… <NA>      
#>  7 bench       High Pr… 1.1.4   "c(\n    p… "Tools to … MIT + … "htt… https://g…
#>  8 BiocManager Access … 1.30.25 "c(\n    p… "A conveni… Artist… "htt… https://g…
#>  9 bit         Classes… 4.6.0   "c(\n    p… "Provided … GPL-2 … "htt… <NA>      
#> 10 bit64       A S3 Cl… 4.6.0-1 "c(\n    p… "\n  Packa… GPL-2 … "htt… <NA>      
#> # ℹ 249 more rows
#> # ℹ 84 more variables: Depends <chr>, Imports <chr>, Suggests <chr>,
#> #   `Config/Needs/website` <chr>, `Config/testthat/edition` <chr>,
#> #   Encoding <chr>, Language <chr>, Roxygen <chr>, RoxygenNote <chr>,
#> #   `Config/usethis/last-upkeep` <chr>, Author <chr>, Maintainer <chr>,
#> #   Built <chr>, LibPath <chr>, Date <chr>, NeedsCompilation <chr>,
#> #   Packaged <chr>, Repository <chr>, `Date/Publication` <chr>, …
```

## Bioconductor support

Both the metadata cache and the package cache support Bioconductor by
default, automatically. See the `BioC_mirror` option and the
`R_BIOC_MIRROR` and `R_BIOC_VERSION` environment variables below to
configure Bioconductor support.

## Package Options

- The `BioC_mirror` option can be used to select a Bioconductor mirror.
  This takes priority over the `R_BIOC_MIRROR` environment variable.
- You can use the `pkg.current_platform` option to set the platform
  string for the current platform for the `current_r_platform()`
  function. This is useful if pkgcache didn’t detect the platform
  correctly. Alternatively, you can use the `PKG_CURRENT_PLATFORM`
  environment variable. The option takes priority.
- `pkgcache_timeout` is the HTTP timeout for all downloads. It is in
  seconds, and the limit for downloading the whole file. Defaults to
  3600, one hour. It corresponds to the [`TIMEOUT` libcurl
  option](https://curl.se/libcurl/c/CURLOPT_TIMEOUT.html).
- `pkgcache_connecttimeout` is the HTTP timeout for the connection
  phase. It is in seconds and defaults to 30 seconds. It corresponds to
  the [`CONNECTTIMEOUT` libcurl
  option](https://curl.se/libcurl/c/CURLOPT_CONNECTTIMEOUT.html).
- `pkgcache_low_speed_limit` and `pkgcache_low_speed_time` are used for
  a more sensible HTTP timeout. If the download speed is less than
  `pkgcache_low_speed_limit` bytes per second for at least
  `pkgcache_low_speed_time` seconds, the download errors. They
  correspond to the
  [`LOW_SPEED_LIMIT`](https://curl.se/libcurl/c/CURLOPT_LOW_SPEED_LIMIT.html)
  and
  [`LOW_SPEED_TIME`](https://curl.se/libcurl/c/CURLOPT_LOW_SPEED_TIME.html)
  curl options.
- `pkgcache_http_version` selects the HTTP version to use for HTTP requests.
  It corresponds to the [`HTTP_VERSION` libcurl
  option](https://curl.se/libcurl/c/CURLOPT_HTTP_VERSION.html), so e.g.
  `2` forces HTTP/1.1 and `0` lets libcurl choose. It defaults to HTTP/1.1,
  because HTTP/2 has caused transport-level failures with some client and
  server combinations.
- `pkgcache_retry` configures whether and how failed HTTP requests are
  retried. It is either a number, to set the maximum number of retries, or
  `TRUE` (the default) or `FALSE` to enable or disable retries. It can also
  be a named list for finer control over the retry policy.

## Package environment variables

- The `R_BIOC_VERSION` environment variable can be used to override the
  default Bioconductor version detection and force a given version. E.g.
  this can be used to force the development version of Bioconductor.
- The `R_BIOC_MIRROR` environment variable can be used to select a
  Bioconductor mirror. The `BioC_mirror` option takes priority over
  this, if set.
- You can use the `PKG_CURRENT_PLATFORM` environment variable to set the
  platform string for the current platform for the
  `current_r_platform()` function. This is useful if pkgcache didn’t
  detect the platform correctly. Alternatively, you can use the
  `pkg.current_platform` option, which takes priority over the
  environment variable.
- `PKGCACHE_PPM_REPO` is the name of the Posit Package Manager
  repository to use. Defaults to `"cran"`.
- `PKGCACHE_PPM_URL` is the base URL of the Posit Package Manager
  instance to use. It defaults to the URL of the Posit Public Package
  Manager instance at <https://packagemanager.posit.co/client/#/>.
- `PKGCACHE_TIMEOUT` is the HTTP timeout for all downloads. It is in
  seconds, and the limit for downloading the whole file. Defaults to
  3600, one hour. It corresponds to the [`TIMEOUT` libcurl
  option](https://curl.se/libcurl/c/CURLOPT_TIMEOUT.html). The
  `pkgcache_timeout` option has priority over this, if set.
- `PKGCACHE_CONNECTTIMEOUT` is the HTTP timeout for the connection
  phase. It is in seconds and defaults to 30 seconds. It corresponds to
  the [`CONNECTTIMEOUT` libcurl
  option](https://curl.se/libcurl/c/CURLOPT_CONNECTTIMEOUT.html). The
  `pkgcache_connecttimeout` option takes precedence over this, if set.
- `PKGCACHE_LOW_SPEED_LIMIT` and `PKGCACHE_LOW_SPEED_TIME` are used for
  a more sensible HTTP timeout. If the download speed is less than
  `PKGCACHE_LOW_SPEED_LIMIT` bytes per second for at least
  `PKGCACHE_LOW_SPEED_TIME` seconds, the download errors. They
  correspond to the
  [`LOW_SPEED_LIMIT`](https://curl.se/libcurl/c/CURLOPT_LOW_SPEED_LIMIT.html)
  and
  [`LOW_SPEED_TIME`](https://curl.se/libcurl/c/CURLOPT_LOW_SPEED_TIME.html)
  curl options. The `pkgcache_low_speed_time` and
  `pkgcache_low_speed_limit` options have priority over these
  environment variables, if they are set.
- `PKGCACHE_HTTP_VERSION` selects the HTTP version to use for HTTP requests.
  It corresponds to the [`HTTP_VERSION` libcurl
  option](https://curl.se/libcurl/c/CURLOPT_HTTP_VERSION.html), so e.g.
  `2` forces HTTP/1.1 and `0` lets libcurl choose. It defaults to HTTP/1.1,
  because HTTP/2 has caused transport-level failures with some client and
  server combinations. The `pkgcache_http_version` option has priority over
  this, if set.
- `PKGCACHE_RETRY` configures whether and how failed HTTP requests are
  retried. It is either a number, to set the maximum number of retries, or
  `TRUE` (the default) or `FALSE` to enable or disable retries. The
  `pkgcache_retry` option has priority over this, if set.
- `R_PKG_CACHE_DIR` is used for the cache directory, if set. (Otherwise
  `tools::R_user_dir("pkgcache", "cache")` is used, see also
  `meta_cache_summary()` and `pkg_cache_summary()`).

## Using pkgcache in CRAN packages

If you use pkgcache in your CRAN package, please make sure that

- you don’t use pkgcache in your examples, and
- you set the `R_USER_CACHE_DIR` environment variable to a temporary
  directory (e.g. via `tempfile()`) during test cases. See the
  `tests/testthat/setup.R` file in pkgcache for an example.

This is to make sure that pkgcache does not modify the user’s files
while running `R CMD check`.

## Code of Conduct

Please note that the pkgcache project is released with a [Contributor
Code of Conduct](https://r-lib.github.io/pkgcache/CODE_OF_CONDUCT.html).
By contributing to this project, you agree to abide by its terms.

## License

MIT (c) [Posit Software, PBC](https://posit.co)
