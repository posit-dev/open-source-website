---
title: The RStudio CRAN mirror
people:
  - Hadley Wickham
date: '2013-06-10'
categories:
  - Community
slug: rstudio-cran-mirror
blogcategories:
  - Company News and Events
ported_from: rstudio
port_status: in-progress
languages: ["R"]
ported_categories:
  - News
tags:
  - RStudio
  - News
---


RStudio maintains its own CRAN mirror, <http://cran.rstudio.com>. The server itself is a virtual machine run by Amazon's EC2 service, and it syncs with the main CRAN mirror in Austria once per day. When you contact <http://cran.rstudio.com>, however, you're probably not talking to our CRAN mirror directly. That's because we use [Amazon CloudFront](http://aws.amazon.com/cloudfront/), a [content delivery network](http://en.wikipedia.org/wiki/Content_delivery_network), which automatically distributes the content to locations [all over the world](http://aws.amazon.com/cloudfront/#details). When you try to download a package from the Rstudio cloud mirror, it'll be retrieved from a local CloudFront cache instead of the CRAN mirror itself. That means that, no matter where you are in the world, the data doesn't need to travel very far, and so is fast to download.

To back this up with some data, we asked some friends to time downloads from all the CRAN mirrors. The RStudio mirror was not always the fastest (especially if you have a mirror nearby), but it was consistently fast around the world. (If you think you could improve on our testing methodology, the scripts and raw data are available at <https://gist.github.com/hadley/5420147> - let us know what you come up with!)

You can use our mirror, even if you don't use RStudio. (If you haven't deliberately chosen a CRAN mirror in RStudio, we'll use ours by default). It's the first one in the list of mirrors ("0-Cloud"), or if you don't want to select it every time you install a package, you can it as the default in your .Rprofile:

```r
options(repos = c(CRAN = "http://cran.rstudio.com"))
```

Of course, speed isn't the only factor you want to consider when choosing a mirror. Another important factor is reliability: is the mirror always available, and how often is it updated? CRAN provides the useful [mirror monitoring report](http://cran.r-project.org/mirmon_report.html).  Running a mirror is easy (it's just a simple script run every few hours), so it's a warning flag if a mirror has any non-green squares. We care about the availability of our mirror, and if it ever does go down, we'll endeavour to fix it as quickly as possible.

Finally, because every download from a CRAN mirror is logged, CRAN mirrors provide a rich source of data about R and package usage. To date, it's been hard to get access to this data. We wanted to change that, so you can now download our anonymised log data from [cran-logs.rstudio.com](http://cran-logs.rstudio.com). We've tried to strike a balance between utility and privacy. We've parsed the raw log data into fields that mean something to R users (like r version, architecture and os). The IP address is potentially revealing, so we've replaced it with a combination of country and a unique id within each day. This should make it possible to explore download patterns without undermining the privacy of the mirror users.

            date     time    size r_version r_arch        r_os           date     time    size r_version r_arch        r_os
    1 2013-01-01 00:18:22  551371    2.15.2 x86_64 darwin9.8.0
    2 2013-01-01 00:43:47  220277    2.15.2 x86_64     mingw32
    3 2013-01-01 00:43:51 3505851    2.15.2 x86_64     mingw32
    4 2013-01-01 00:43:53  761107    2.15.2 x86_64     mingw32
    5 2013-01-01 00:31:15  187381    2.15.2   i686   linux-gnu
    6 2013-01-01 00:59:46 2388932    2.15.2 x86_64     mingw32
        package version country ip_id
    1     knitr     0.9      RU     1
    2 R.devices   2.1.3      US     2
    3     PSCBS  0.30.0      US     2
    4      R.oo  1.11.4      US     2
    5     akima   0.5-8      US     3
    6 spacetime   1.0-3      VN     4

Altogether, there's currently around 150 megs of gzipped log files, representing over 7,000,000 package downloads. We're looking forward to seeing what the R community does with this data, and we'll highlight particularly interesting analyses in a future blog post. If you have any problems using the data, or you'd like to highlight a particularly interesting result, please feel free to [email me](mailto:hadley@rstudio.com).

