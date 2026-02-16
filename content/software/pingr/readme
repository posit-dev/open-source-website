
<!-- badges: start -->

[![R-CMD-check](https://github.com/r-lib/pingr/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/r-lib/pingr/actions/workflows/R-CMD-check.yaml)
[![CRAN RStudio mirror
downloads](http://cranlogs.r-pkg.org/badges/pingr)](https://r-pkg.org/pkg/pingr)
[![Codecov test
coverage](https://codecov.io/gh/r-lib/pingr/graph/badge.svg)](https://app.codecov.io/gh/r-lib/pingr)
<!-- badges: end -->

# pingr: check if a server is alive

The pingr package has tools to check if a remote computer or web server
is up and some other related tools.

## Installation

Install the package from CRAN:

``` r
install.packages("pingr")
```

If you need the development version, install it from GitHub:

``` r
pak::pak("r-lib/pingr")
```

## ICMP ping

The `ping()` function does ICMP ping, via the system’s `ping` utility:

``` r
library(pingr)
```

    #> 
    #> Attaching package: 'pingr'

    #> The following object is masked from 'package:utils':
    #> 
    #>     nsl

``` r
ping("127.0.0.1")
```

    #> [1] 0.084 0.097 0.068

By default it sends three packets and measures the time it receives and
answer. It waits between sending out the packets, so if you want a
really quick check, you can just send a single packet:

``` r
ping("127.0.0.1", count = 1)
```

    #> [1] 0.069

If a machine is down (or it does not exist), then `NA` is returned
instead of the roundtrip time:

``` r
ping("192.0.2.1", count = 1)
```

    #> [1] NA

## TCP ping

With TCP ping we can check if a machine is listeing on a TCP port,
e.g. if google’s search web server is up and running:

``` r
ping_port("www.google.com", port = 80, count = 1)
```

    #> [1] 17.737

## Query the public IP address of the computer

`my_ip()` queries the public IP of the computer, either via DNS or
HTTPS:

``` r
my_ip()
```

    #> [1] "83.50.74.244"

## Check if the computer is online

`is_online()` checks if the computer is online. It makes three tries:

- Queries myip.opendns.com on OpenDNS, see `my_ip()`.
- Retrieves icanhazip.com via HTTPS, see `my_ip()`.
- Retrieve Apple’s Captive Portal test page, see `apple_captive_test()`.

If any of these are successful, it returns `TRUE`.

``` r
is_online()
```

    #> [1] TRUE

## DNS queries

The package also contains a function to perform DNS queries. This is a
more portable and more functional version of the `utils::nsl()`
function:

``` r
nsl("www.r-project.org", type = 1L)
```

    #> $answer
    #>                 name class type  ttl               data
    #> 1  www.r-project.org     1    5 7054 cran.wu-wien.ac.at
    #> 2 cran.wu-wien.ac.at     1    1  231      137.208.57.37
    #> 
    #> $flags
    #>    aa    tc    rd    ra    ad    cd 
    #> FALSE FALSE  TRUE  TRUE FALSE FALSE

``` r
nsl("google.com", type = 28L)
```

    #> $answer
    #>         name class type ttl                     data
    #> 1 google.com     1   28 236 2a00:1450:4003:80d::200e
    #> 
    #> $flags
    #>    aa    tc    rd    ra    ad    cd 
    #> FALSE FALSE  TRUE  TRUE FALSE FALSE

## License

MIT © RStudio
