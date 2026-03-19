---
title: Where in the world is R and RStudio
people:
  - Hadley Wickham
date: '2012-10-01'
categories:
- News
slug: where-in-the-world
blogcategories:
- Company News and Events
ported_from: rstudio
port_status: in-progress
---


Using the web logs collected when users download RStudio, we've prepared the following two maps showing where RStudio is being used, over the whole globe and just within the continental USA. Obviously this data is somewhat biased, as it reflects the number of downloads of RStudio, rather than the number of users of R (which we'd really love to know!). However, based on a month's worth of data, we think the broad patterns are pretty interesting.

![](https://rstudioblog.files.wordpress.com/2012/10/us.png)
![](https://rstudioblog.files.wordpress.com/2012/10/world.png)

We made the maps by translating IP addresses to latitude and longitude with the free [GeoIP](http://www.maxmind.com/app/geolite) databases provided by [MaxMind](http://www.maxmind.com/). To make it easier to see the main patterns for each map, we used k-means clustering to group the original locations into 300 clusters for the world and 100 clusters for the US,  then used ggplot2 to display the number of users in each cluster with the area of each bubble.

