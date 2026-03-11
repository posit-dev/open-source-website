---
title: Data management with ShinyApps.io
people:
  - Garrett Grolemund
date: '2014-09-29'
categories:
- Shiny
- shinyapps.io
tags:
- Article
- shiny
- Shiny
- shinyapps.io
slug: data-management-with-shinyapps-io
blogcategories:
- Products and Technology
events: blog
ported_from: rstudio
port_status: raw
---


![ShinyApps.io dashboard](https://www.shinyapps.io/assets/images/dashboard-screen.png)

Some of the most innovative Shiny apps share data across user sessions. Some apps share the results of one session to use in future sessions, others track user characteristics over time and make them available as part of the app.

This level of sophistication creates tricky design choices when you host your app on a server. A nimble server will open new instances of your app to speed up performance, or relaunch your app on a bigger server when it becomes popular. How should you ensure that your app can find and use its data trail along the way?

Shiny Server developer Jeff Allen explains the best ways to share data between sessions in [Share data across sessions with ShinyApps.io](https://shiny.rstudio.com/articles/share-data.html), a new article at the Shiny Dev Center.

