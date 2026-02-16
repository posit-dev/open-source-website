<!-- README.md is generated from README.Rmd. Please edit that file -->

# shinycoreci

<!-- badges: start -->

[![Lifecycle Experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental)
[![R CMD check](https://github.com/rstudio/shinycoreci/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/rstudio/shinycoreci/actions/workflows/R-CMD-check.yaml)
[![Test](https://github.com/rstudio/shinycoreci/actions/workflows/apps-test-matrix.yml/badge.svg)](https://github.com/rstudio/shinycoreci/actions/workflows/apps-test-matrix.yml)
[![Deploy](https://github.com/rstudio/shinycoreci/actions/workflows/apps-deploy.yml/badge.svg)](https://github.com/rstudio/shinycoreci/actions/workflows/apps-deploy.yml)
[![Docker](https://github.com/rstudio/shinycoreci/actions/workflows/apps-docker.yml/badge.svg)](https://github.com/rstudio/shinycoreci/actions/workflows/apps-docker.yml)
[![Dependencies](https://github.com/rstudio/shinycoreci/actions/workflows/apps-deps.yml/badge.svg)](https://github.com/rstudio/shinycoreci/actions/workflows/apps-deps.yml)
<!-- badges: end -->

<!-- This is an R package to install all dependencies to test the bleeding edge of all relevant packages to the Shiny team. -->
<!-- For more direct usage examples, see [`rstudio/shinycoreci-apps`](https://github.com/rstudio/shinycoreci-apps). -->

## Github Runner Images

shinycoreci [uses the following GitHub Runnner Images](https://github.com/rstudio/shinycoreci/blob/main/.github/workflows/apps-config.yml).

| Image               | Details                                                                                                 |                                                                                                            Status                                                                                                             |
|:--------------------|:--------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Ubuntu 20.04        | [ubuntu-20.04](https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2004-Readme.md)   |      [![status20](https://gh-runnerimagesdeploymentstatus.azurewebsites.net/api/status?imageName=ubuntu20&badge=1)](https://gh-runnerimagesdeploymentstatus.azurewebsites.net/api/status?imageName=ubuntu20&redirect=1)       |
| macOS 12            | [macos-12](https://github.com/actions/runner-images/blob/main/images/macos/macos-12-Readme.md)          |    [![statusumac12](https://gh-runnerimagesdeploymentstatus.azurewebsites.net/api/status?imageName=macos-12&badge=1)](https://gh-runnerimagesdeploymentstatus.azurewebsites.net/api/status?imageName=macos-12&redirect=1)     |
| Windows Server 2022 | [windows-2022](https://github.com/actions/runner-images/blob/main/images/windows/Windows2022-Readme.md) | [![statuswin22](https://gh-runnerimagesdeploymentstatus.azurewebsites.net/api/status?imageName=windows-2022&badge=1)](https://gh-runnerimagesdeploymentstatus.azurewebsites.net/api/status?imageName=windows-2022&redirect=1) |

## Installation

Install the development version from [GitHub](https://github.com/) with:

``` r
pak::pak("rstudio/shinycoreci")
```

These GitHub packages will be installed to make sure the latest package development is working as expected:

- [rstudio/bsicons](https://github.com/rstudio/bsicons)
- [rstudio/bslib](https://github.com/rstudio/bslib)
- [r-lib/cachem](https://github.com/r-lib/cachem)
- [rstudio/chromote](https://github.com/rstudio/chromote)
- [rstudio/crosstalk](https://github.com/rstudio/crosstalk)
- [rstudio/DT](https://github.com/rstudio/DT)
- [rstudio/dygraphs](https://github.com/rstudio/dygraphs)
- [r-lib/fastmap](https://github.com/r-lib/fastmap)
- [rstudio/flexdashboard](https://github.com/rstudio/flexdashboard)
- [rstudio/fontawesome](https://github.com/rstudio/fontawesome)
- [rstudio/gt](https://github.com/rstudio/gt)
- [rstudio/htmltools](https://github.com/rstudio/htmltools)
- [ramnathv/htmlwidgets](https://github.com/ramnathv/htmlwidgets)
- [rstudio/httpuv](https://github.com/rstudio/httpuv)
- [r-lib/later](https://github.com/r-lib/later)
- [rstudio/leaflet](https://github.com/rstudio/leaflet)
- [ropensci/plotly](https://github.com/ropensci/plotly)
- [rstudio/pool](https://github.com/rstudio/pool)
- [rstudio/promises](https://github.com/rstudio/promises)
- [rstudio/reactlog](https://github.com/rstudio/reactlog)
- [rstudio/sass](https://github.com/rstudio/sass)
- [rstudio/shiny](https://github.com/rstudio/shiny)
- [rstudio/shinycoreci](https://github.com/rstudio/shinycoreci)
- [schloerke/shinyjster](https://github.com/schloerke/shinyjster)
- [rstudio/shinymeta](https://github.com/rstudio/shinymeta)
- [rstudio/shinytest](https://github.com/rstudio/shinytest)
- [rstudio/shinytest2](https://github.com/rstudio/shinytest2)
- [rstudio/shinythemes](https://github.com/rstudio/shinythemes)
- [rstudio/shinyvalidate](https://github.com/rstudio/shinyvalidate)
- [rstudio/thematic](https://github.com/rstudio/thematic)
- [rstudio/webdriver](https://github.com/rstudio/webdriver)
- [rstudio/websocket](https://github.com/rstudio/websocket)

#### R-Universe

`{shinycoreci}` testing leverages rOpenSci [`r-universe`](https://r-universe.dev/search/), specifically the [`posit-dev-shinycoreci`](https://posit-dev-shinycoreci.r-universe.dev/builds) universe. This universe is used to install the latest development versions of the Shiny related packages (updated hourly) used in the testing apps without the need for a GitHub token. This last detail is important, as it allows GitHub Actions to install packages freely without the worry of being rate limited. This gives us the ability to attempt to install each app’s dependencies independently, leading to higher test coverage as a single dependencies does not block the entire test execution.

## Running manual tests

First, install the `{shinycoreci}` repo via {pak} (from instructions above). Before running any tests, you may need to add your `GITHUB_PAT` to your R Environ file (See `?usethis::edit_r_environ` and `?usethis::create_github_token`)

Commands used to test in different situations:

- [RStudio IDE](https://rstudio.com/products/rstudio/download/#download) - `shinycoreci::test_in_ide()`
- [RStudio Cloud](http://rstudio.cloud) - `shinycoreci::test_in_ide()`
- [RStudio Server Pro](https://colorado.rstudio.com) - `shinycoreci::test_in_ide()`
- R Terminal / R GUI - `shinycoreci::test_in_browser()`
- (Any) Web Browser - `shinycoreci::test_in_browser()`
- [shinyapps.io](http://shinyapps.io) - `shinycoreci::test_in_shinyappsio()`
- [Posit Connect](http://dogfood.team.pct.posit.it) - `shinycoreci::test_in_connect()`
- SSO - `shinycoreci::test_in_sso(release = "focal")`
  \> Requires `Docker` application to be running
- SSP - `shinycoreci::test_in_ssp(release = "centos7")`
  \> Requires `Docker` application to be running

All testing functions may be run from within the IDE (except for R Terminal / R GUI).

#### IDE Example

``` r
# install.packages("pak", repos = sprintf("https://r-lib.github.io/p/pak/stable/%s/%s/%s", .Platform$pkgType, R.Version()$os, R.Version()$arch))

# Install the latest from pak
pak::pkg_install("rstudio/shinycoreci")

# Install shinyverse
# Run all manual tests
shinycoreci::test_in_ide()
```

## View the latest test results

To view the latest test results, please visit <https://rstudio.github.io/shinycoreci/results/>. This link will update to the latest results when they are pushed.

If you see failures, this indicates that a test has failed. If it is related to a `{shinytest2}` snapshot failure, we can view and approve these failures with `shinycoreci::fix_snaps()`. Your working directory must be in a local checkout of the `rstudio/shinycoreci` repo. Once `shinycoreci::fix_snaps()` has finished running, use [GitHub Desktop](https://desktop.github.com/) to view the changes.

If you receive the error `No information found for sha: ABC1234 . Do you have a valid sha?`, you may have to provide the git sha value directly: `shinycoreci::fix_snaps(sha = "XYZ5678")`.

In the event that all testing failures can not be addressed by updating `{shinytest2}` baselines, have a look at the [GHA actions](https://github.com/rstudio/shinycoreci/actions) build log and keep the following troubleshooting tips in mind:

### Troubleshooting test failures

1.  Failures on old versions of R

If a testing app passes on recent version(s) of R, but fails in a suprising way on old R version(s), it may be due to an old R package version. In that case, modify the tests to run only if a sufficient version of the relevant package is available ([for example](https://github.com/rstudio/shinycoreci/blob/d8f627bea573cf7bb7a53788522f04d90aeb557f/inst/apps/145-dt-replacedata/tests/testthat/test-mytest.R)).

2.  Other failures that can’t replicated locally

Other surprising failures are often the result of timing issues (which can be difficult, if not impossible, to replicate locally). If your testing app uses dynamic UI and/or doesn’t have proper input/output bindings, **shinytest2** probably needs to know how long to wait for value(s) to update (in this case, use `app$wait_for_idle()`, [for example](https://github.com/rstudio/shinycoreci/blob/46cdf9df12ee665d5ac77f85eb22f511ce8a4fe6/inst/apps/135-bookmark-uioutput/tests/testthat/test-mytest.R#L6)). Somewhat similarly, when checking DOM values with **shinyjster**, you may need to wait for an update to DOM element(s) before checking value(s), in which case you can write a recursive function that keeps calling itself until the DOM is ready ([for example](https://github.com/rstudio/shinycoreci/blob/46cdf9df12ee665d5ac77f85eb22f511ce8a4fe6/inst/apps/187-navbar-collapse/app.R#L27-L36)).

3.  All of the windows shinytest plots have failed

When Windows virtual images update on GitHub Actions, the graphics device may behave exactly as the prior graphics device. Check to see if your windows `Image Version` has updated. (To view this, inspect the top lines in `./inst/apps/sys-info-win-XX.txt` for a change.) You should accept the updated shinytest output for the build with the higher `Image Version`.

## Contribute a testing app

When contributing a testing app, try to do the following:

- Capture all the functionality with automated tests.
  - Also, where possible, write “light-weight” tests (that is, try and avoid **shinytest2** `$expect_screenshot()` where possible since they are prone to false positive differences and thus have a maintenance cost).
  - If the app does need manual testing, flag the testing app for manual testing with `shinycoreci::use_manual_app()`.
- Add a description to the app’s UI that makes it clear what the app is testing for.

Note that **shinycoreci** only supports `{testthat}` testing framework. Call `shinytest2::use_shinytest2(APP_DIR)` to use `{shinytest2}` and `{testthat}`

1.  **shinytest2**: primarily useful for taking screenshots of shiny output binding(s) (before or after interacting with **shiny** input bindings). [See here](https://github.com/rstudio/shinycoreci/blob/d8f627bea573cf7bb7a53788522f04d90aeb557f/inst/apps/001-hello/tests/testthat/test-mytest.R) for an example (note that `shinytest2::record_test()` can be used to generate shinytest2 testing scripts).

2.  **shinyjster**: primarily useful for asserting certain expectations about the DOM (in JavaScript). [See here](https://github.com/rstudio/shinycoreci-apps/blob/5691d1f/apps/001-hello/app.R#L37-L61) for an example (note that `shinyjster::shinyjster_js()` needs to be placed in the UI and `shinyjster::shinyjster_server(input, output)` needs to be placed in the server).

3.  **testthat**: primarily useful in combination with `shiny::testServer()` to test server-side reactive logic of the application.

- [See here](https://github.com/rstudio/shinycoreci-apps/blob/5691d1f4/apps/001-hello/tests/testthat/tests.R#L4) for an example.

## Pruning old git branches

To help us store and manage the test results, git branches are automatically created for each test run. These branches are automatically removed on GitHub after 1 week of no activity, but you may want to periodically remove them on your local machine as well:

``` bash
git fetch --prune
```

## What workflows are available?

This repo contains several [GitHub Actions](https://github.com/features/actions) workflows:

- [**Test apps:**](https://github.com/rstudio/shinycoreci/actions/workflows/apps-test-matrix.yml) Run all automated tests (via `shiny::runTests()`). If on `main` branch, test results will be saved to `_test_results` branch.
- [**Docker:**](https://github.com/rstudio/shinycoreci/actions/workflows/apps-docker.yml) Create all SSO and SSP docker images. Docker images are hosted on [`rstudio/shinycoreci` via GitHub Packages](https://github.com/rstudio/shinycoreci/pkgs/container/shinycoreci).
- [**Deploy**](https://github.com/rstudio/shinycoreci/actions/workflows/apps-deploy.yml): Deploy all testing apps to [shinyapps.io](https://shinyapps.io) and [dogfood.team.pct.posit.it](https://dogfood.team.pct.posit.it)
- [**Build results website**](https://github.com/rstudio/shinycoreci/actions/workflows/build-results.yml): Builds results for **Test apps** workflow. This workflow is called from within **Test apps**. After all tests have completed, this workflow will process all results in `_test_results` branch into static files, storing the results in `gh-pages` branch. Final website location of results: <https://rstudio.github.io/shinycoreci/results/>
- [**Package checks**](https://github.com/rstudio/shinycoreci/actions/workflows/R-CMD-check.yaml): There are three main tasks that this workflow achieves:
  1.  Creates the `website` via `{pkgdown}`
  2.  Performs `routine` procedures like making sure all documentation and README.md is up to date
  3.  Performs `R CMD check` on `{shinycoreci}`, across macOS, Windows, and Ubuntu (multiple R versions).
- [**Update app deps**](https://github.com/rstudio/shinycoreci/actions/workflows/apps-deps.yml): Updates known dependencies of all Shiny applications in `./inst/apps`.
- [**Trim old branches**](https://github.com/rstudio/shinycoreci/actions/workflows/trim-old-branches.yml): The current data model of **Test apps** workflow is to create many `gha-**` branches containing the changes of each test run on `main`. `gha-**` branches that have been stale for more than a week are removed.

### Trigger

There are a handful of methods that can be called to trigger the GHA actions.

- `shinycoreci::trigger_tests()`: Trigger the **Test apps** workflow.
- `shinycoreci::trigger_docker()`: Trigger the **Docker** workflow.
- `shinycoreci::trigger_deploy()`: Trigger the **Deploy** workflow.
- `shinycoreci::trigger_results()`: Trigger the **Build results website** workflow.
- `shinycoreci::trigger(event_type=)`: Sends a custom event to the GHA workflow. For example, this can be used to trigger **Trim old branches** with `shinycoreci::trigger("trim")`.

A triggered workflow will run without having to push to the repo. Anyone with repo write access can call this command.

### Schedule

Most of the workflows are run on schedule.

Example schedule where the workflow is run at 2am UTC Monday through Friday:

``` yaml
  schedule:
    - cron:  '0 2 * * 1-5'
```

Schedule of `rstudio/shinycoreci` workflows:

- 12am UTC, S-S: **Trim old branches**; \< 1 min
- 12am UTC, M-F: **Update app deps**; \< 5 mins
- 2am UTC, M-F: **Deploy apps**; ~ 2 hrs
- 3am UTC, M-F: **Docker**; ~ 1 hr
- 5am UTC, M-F: **Test apps** (Internally calls **Build results website**); ~ 4 hrs

### `build-results.yml`

Breakdown of what happens in the **Build results website** workflow:

On completion of `apps-test-matrix.yml`…

- GHA will check out the latest `_test_results` branch into the local folder.
- GHA will check out the latest `gh-pages` branch into the `./_gh-pages` folder.
- GHA will install R and necessary package dependencies.
- Run `./build_site.R`
  - Read the *modify times* of each file in `_test_results` and processing files
  - Compare *modify times* to *modify times* of output files
  - If any input file is newer than the output file, reprocess the documen
  - If reprocessing, render `./render-results.Rmd` given proper subset of data
    - Save output to \`./\_gh-pages/results/YEAR/MONTH/DAY/index.html
  - Update `./_gh-pages/results/index.html` to redirect to the most recent results
- Within the `./_gh-pages` directory
  - Add any files that have been altered
  - Commit and push back any changes to the `gh-pages` website

Final results are available at: <https://rstudio.github.io/shinycoreci/results/>

# FAQ:

- If you run into an odd `{pak}` installation issue:
  - Run `pak::cache_clean()` to clear the cache and try your original command again
- Installing on fresh linux? Run these commands before testing:

``` r
pkgs <- c('base64enc', 'bslib', 'Cairo', 'clipr', 'curl', 'dbplyr', 'DiagrammeR',
  'dplyr', 'DT', 'evaluate', 'flexdashboard', 'future', 'ggplot2',
  'ggvis', 'hexbin', 'htmltools', 'htmlwidgets',
  'httpuv', 'jsonlite', 'knitr', 'later', 'leaflet', 'magrittr',
  'maps', 'markdown', 'memoise', 'networkD3', 'plotly', 'png',
  'progress', 'promises', 'pryr', 'radiant', 'ragg', 'RColorBrewer',
  'reactable', 'reactlog', 'reactR', 'rlang', 'rmarkdown', 'rprojroot',
  'rsconnect', 'RSQLite', 'rversions', 'scales', 'sf', 'shiny',
  'shinyAce', 'shinydashboard', 'shinyjs', 'shinymeta',
  'shinytest2', 'shinythemes', 'shinyvalidate', 'showtext', 'sysfonts',
  'systemfonts', 'testthat', 'thematic', 'tidyr', 'tm', 'websocket',
  'withr', 'wordcloud',
  'sessioninfo',
  'debugme', 'highcharter', 'parsedate', 'quantmod', 'rjson', 'rlist', 'showimage', 'TTR', 'XML', 'xts'
);
pak::pkg_system_requirements(pkgs, execute = TRUE);
install.packages(pkgs);
# Now you should be able to go about testing
```
