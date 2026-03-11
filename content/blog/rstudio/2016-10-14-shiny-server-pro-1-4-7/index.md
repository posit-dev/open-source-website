---
title: Shiny Server (Pro) 1.4.7
people:
  - Joe Cheng
date: '2016-10-14'
categories:
- Shiny
tags:
- Security
- Shiny
slug: shiny-server-pro-1-4-7
blogcategories:
- Products and Technology
events: blog
ported_from: rstudio
port_status: raw
---


[Shiny Server 1.4.7.815 and Shiny Server Pro 1.4.7.736 are now available!](https://www.rstudio.com/products/shiny/shiny-server/) This release includes new features to support Shiny 0.14. It also updates our Node.js to 0.10.47, which includes important security fixes for SSL/TLS.

### Connection robustness (a.k.a. grey-outs)

Shiny's architecture is built on top of websockets, which are long-lived network connections between the browser and an R session on the server. If this connection is broken for any reason, the browser is no longer able to communicate with its R session on the server. Shiny indicates this to the user by turning the page background grey and fading out the page contents.

In Shiny 0.14 and Shiny Server 1.4.7, we've done work at both the server and package levels to minimize the amount of greyouts users will see. Simply by upgrading Shiny Server, transient (<15sec) network interruptions should no longer disrupt Shiny apps. And for many Shiny apps, a secondary, opt-in reconnection mechanism should all but eliminate grey-outs. [This article on shiny.rstudio.com](https://shiny.rstudio.com/articles/reconnecting.html) has all the details.

### Bookmarkable state

Shiny 0.14 introduced a ["bookmarkable state" feature](https://shiny.rstudio.com/articles/bookmarking-state.html) that made it possible to snapshot the state of a running Shiny app, and send it to someone as a URL to try in their own browser. At the app author's option, the app state could either be fully encoded in the URL, or written to disk and referred to by a short ID. This latter approach requires support from the server, and that support is now officially provided by Shiny Server and Shiny Server 1.4.7. (This functionality is not yet available for ShinyApps.io, however.)

## Coming soon: Shiny Server 1.5.0

Just a heads up: Shiny Server (Pro) 1.5.0 is coming in a few weeks. Shiny Server was originally written using Node.js 0.10, which is nearing the end of its lifespan. This release will move to Node.js 6.x.

Due to the complexity of this upgrade, Shiny Server 1.5.0 will not add any new features, except for supporting [perfect forward secrecy](https://en.wikipedia.org/wiki/Transport_Layer_Security#Forward_secrecy) for SSL/TLS connections. The focus will be entirely on ensuring a smooth and stable release.

