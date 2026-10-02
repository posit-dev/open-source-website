
# gitcreds

> Query git credentials from R

<!-- badges: start -->

[![R build
status](https://github.com/r-lib/gitcreds/workflows/R-CMD-check/badge.svg)](https://github.com/r-lib/gitcreds/actions)
[![R-CMD-check](https://github.com/r-lib/gitcreds/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/r-lib/gitcreds/actions/workflows/R-CMD-check.yaml)
[![Codecov test
coverage](https://codecov.io/gh/r-lib/gitcreds/graph/badge.svg)](https://app.codecov.io/gh/r-lib/gitcreds)
<!-- badges: end -->

## Features

- (Re)use the same credentials in command line git, R and the RStudio
  IDE., etc. Users can set their GitHub token once and use it
  everywhere.

- Typically more secure than storing passwords and tokens in `.Renviron`
  files.

- gitcreds has a cache that makes credential lookup very fast.

- gitcreds supports multiple users and multiple hosts, including
  Enterprise GitHub installations.

- If git or git credential helpers are not available, e.g. typically on
  a Linux server, or a CI, then gitcreds can fall back to use
  environment variables, and it still supports multiple users and hosts.

## Installation

Install the package from CRAN:

``` r
install.packages("gitcreds")
```

Install the development version from GitHub:

``` r
pak::pak("r-lib/gitcreds")
```

## Usage

gitcreds is typically used upstream, in R packages that need to
authenticate to git or GitHub. End users of these packages might still
find it useful to call gitcreds directly, to set up their credentials,
or check that they have been set up correctly.

You can also use gitcreds in an R script. In this case you are both the
end user and the upstream developer.

### Usage as an end user

``` r
library(gitcreds)
```

Use `gitcreds_get()` to check your GitHub or other git credentials. It
returns a named list, with a `password` entry. The password is not
printed by default:

``` r
gitcreds_get()
```

``` r
#> <gitcreds>
#>   protocol: https
#>   host    : github.com
#>   username: gaborcsardi
#>   password: <-- hidden -->
```

Use `gitcreds_set()` to add new credentials, or replace existing ones.
It always asks you before replacing existing credentials:

``` r
gitcreds_set()
```

``` r
#> -> Your current credentials for 'https://github.com':
#> 
#>   protocol: https
#>   host    : github.com
#>   username: gaborcsardi
#>   password: <-- hidden -->
#> 
#> -> What would you like to do?
#> 
#> 1: Keep these credentials
#> 2: Replace these credentials
#> 3: See the password / token
#> 
#> Selection: 2
#> 
#> ? Enter new password or token: secret
#> -> Removing current credentials...
#> -> Adding new credentials...
#> -> Removing credentials from cache...
#> -> Done.
```

Use `gitcreds_delete()` to delete credentials. It always asks you before
actually deleting any credentials:

``` r
gitcreds_delete()
```

``` r
#> -> Your current credentials for 'https://github.com':
#> 
#>   protocol: https
#>   host    : github.com
#>   username: token
#>   password: <-- hidden -->
#> 
#> -> What would you like to do?
#> 
#> 1: Keep these credentials
#> 2: Delete these credentials
#> 3: See the password / token
#> 
#> Selection: 2
#> -> Removing current credentials...
#> -> Removing credentials from cache...
#> -> Done.
```

### Usage as a package author

If you want to use git’s credentials in your package, call
`gitcreds_get()`. You probably want to handle the various errors it can
return. Here is an example for a function that optionally neeeds a
GitHub token. It searches the code of a GitHub repository:

``` r
github_search <- function(query, repo = "wch/r-source") {
  token <- tryCatch(
    gitcreds::gitcreds_get(),
    error = function(e) NULL
  )

  url <- "https://api.github.com/search/code"
  q <- list(q = paste0(query, "+repo:", repo))
  token <- paste0("token ", token$password)

  httr::GET(url, query = q, httr::add_headers(Authorization = token))
}
```

The next example always needs a GitHub token, so it fails without one.
It lists the public repositories of the current user:

``` r
msg <- function(wh) {
  msgs <- c(
    no_git = paste0(
      "No git installation found. You need to install git and set up ",
      "your GitHub Personal Access token using `gitcreds::gitcreds_set()`."),
    no_creds = paste0(
      "No git credentials found. Please set up your GitHub Personal Access ",
      "token using `gitcreds::gitcreds_set()`.")
    )
  msgs[wh]
}

my_private_repos <- function() {
  token <- tryCatch(
    gitcreds::gitcreds_get(),
    gitcreds_nogit_error = function(e) stop(msg("no_git")),
    gitcreds_no_credentials = function(e) stop(msg("no_creds"))    
  )

  url <- "https://api.github.com/user/repos"
  q <- list(visibility = "public")
  token <- paste0("token ", token$password)

  httr::GET(url, query = q, httr::add_headers(Authorization = token))
}
```

Point your users to `gitcreds_set()` for adding/updating their
credentials, or write your own wrapper for this.

If you want more control or a different UI, take a look at the lower
level `gitcreds_fill()`, `gitcreds_approve()` and `gitcreds_reject()`
functions.

See also [gitcreds for package
authors](https://gitcreds.r-lib.org/articles/package.html).

## Code of Conduct

Please note that the gitcreds project is released with a [Contributor
Code of
Conduct](https://contributor-covenant.org/version/2/1/CODE_OF_CONDUCT.html).
By contributing to this project, you agree to abide by its terms.

## License

MIT © [RStudio](https://github.com/rstudio)
