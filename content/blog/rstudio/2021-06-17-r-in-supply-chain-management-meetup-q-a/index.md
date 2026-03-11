---
title: 'R in Supply Chain Management: Meetup Q&A'
people:
  - Rachael Dempsey
date: '2021-06-17'
slug: r-in-supply-chain-management-meetup-q-a
categories:
  - Events
tags:
  - Shiny
  - Code-First
  - Use Cases
  - Data science
events: blog
description: Supply chain management presents a number of interesting and challenging problems to solve in topics such as demand and supply planning, inventory management, and forecasting. This post dives into questions from the R in Supply Chain Management meetup with Nicolas Nguyen. 
blogcategories: 
 - Company News and Events
ported_from: rstudio
port_status: raw
---

Supply chain management presents several unique challenges, with supply chain resilience particularly relevant due to disruptions from the pandemic. With thousands of SKUs and multi-tiered distribution networks, teams are using R and Python to improve forecasts, speed up operational planning, simulate variability, and design efficient supply chains. 

The RStudio Enterprise Community group recently hosted an R in Supply Chain Management <a href="https://community.rstudio.com/t/recording-of-r-in-supply-chain-management-rstudio-enterprise-virtual-meetup/104459" target="_blank">meetup</a> featuring Nicolas Nguyen, Digital Supply Chain and Global S&OP Leader at Carl Zeiss Meditec. Nicolas shared the work that he is doing with Shiny to balance demand and supply to support sales. Using Shiny, he has designed powerful, scalable, and reproducible applications for the business.

<a style="display: block; text-align:center;" href="https://www.youtube.com/watch?v=rzs6aSr4XoU" target="_blank"><img src="https://videoapi-muybridge.vimeocdn.com/animated-thumbnails/image/a3948c82-214b-4b6a-b348-fcdad00cf415.gif?ClientID=vimeo-core-prod&Date=1623431854&Signature=b83235c85c3666fcc6ff134adb0f8df8c6e9db2b" alt="R in Supply Chain Management with Nicolas Nguyen | Carl Zeiss Meditec" style=" max-height:100%; max-width:100%;"/></a>
<div align="right">Full meetup recording <a href="https://www.youtube.com/watch?v=rzs6aSr4XoU" target="_blank">here</a></div></font>

It was awesome to see the beautiful applications that Nicolas built, as well as the reactions and support among the supply chain community that came together for the event. His Shiny applications served as inspiration for many of us that attended.  

While we had time for a handful of questions during the session, I’ve included the full Q&A below, which also includes Nicolas’ response to any questions that went unanswered.

We have paraphrased and distilled portions of the responses for brevity and narrative quality.

## Meetup Q&A:

**How long did this take to create and what are the libraries used?**  

**Nicolas:** I created the R script to calculate the projected inventories and replenishment plan in 2017 over a few days (with trial & error). Since then, I have been reusing the same code with a bit of improvements. The libraries used are dplyr, DT, tidyverse, and lubridate.  

Depending on the complexity, the Shiny applications took anywhere from 4 hours to a couple of days.  

**Can you provide additional background about the algorithms for the prescriptive analytics, how you build supply chain scenarios, and how you find recommendations?**  

**Nicolas:** Yes, I will also create some examples of prescriptive analytics to share with the group within a few months. The idea is to create a “virtual supply planning assistant” that is going to analyze a situation (based on our code & parameters we defined) to propose potential solutions.  

A few examples of supply chain scenarios are:  

* If sales grow 20% above the current level in the next 6-12 months,   will we have enough production capacities to answer this demand?
* Should we anticipate production and build stock to be prepared?  
* Could we play on some safety stock levels in some markets, or shorter delivery lead time (shipping by air instead of sea), to reduce the production demand or accelerate our supplies?
* Could we play on the product mix and use the machines on a certain type of “similar” product to increase the overall output?
* In case of shortages, can we supply earlier to the market by doing a partial air shipment? Can we ship from another market?

**Do you have any suggestions to start developing similar tools? Any material or examples related to Supply & Demand?**  

**Nicolas:** Perhaps the easiest way to get started is to look at the existing tools (Excel, APS, SAP, etc.) used by the supply chain team in your company.  

Looking at the way they are used for data transformation, analysis, and charts - what are the problems faced (if any)? What is the degree of automation? Then, do the same thing using R & Shiny, and see if it answers some challenges.  

I will create a github in July/August to share a few examples:  

* Basic Projected Inventories & Coverages
* Single level DRP @ Monthly and Weekly Buckets
* Multi-Level DRP
* BOM (Bill Of Material) calculation
* Calculation of Dependent Demand (ex.: Kits / Promo Packs)
* Discontinuation of Products and NPL (New Product Launch) to replace them
* FeFo (First Expired First Out) calculation
* S&OP (Sales & Operations Planning) process app: illustrating Production Capacities

**Do you have an example of using R for the right inventory in distribution channels and warehouses across geography depending on demand sensing?**  

**Nicolas:** I currently do not have this, but this is to be created! :)

**For products that have 0 demand/supply for a time-point, would the forecasting algorithm impute or take actual 0?**  

**Nicolas:** The current algorithm works on projected coverages. If there is 0 demand next month but some demand the following months, it will maintain a coverage to be aligned with the demand of the following months. For any specific need, it’s always possible to modify the code to get the expected behaviour.

**What did you use for the plots, graphs, and tables you are showing?**  

**Nicolas:** The tables are <a href="https://rstudio.github.io/DT/" target="_blank">DT</a> and <a href="https://github.com/kcuilla/reactablefmtr" target="_blank">reactablefmtr</a>, and the plots are <a href="https://github.com/tidyverse/ggplot2" target="_blank">ggplot2</a> and <a href="https://jkunst.com/highcharter/">highcharter</a>. The Sankey diagrams are <a href="https://christophergandrud.github.io/networkD3/" target="_blank">networkD3</a>. I also used <a href="https://cran.r-project.org/web/packages/kableExtra/vignettes/awesome_table_in_html.html" target="_blank">kableExtra</a>, <a href="https://github.com/renkun-ken/formattable" target="_blank">formattable</a>, and <a href="http://shinyapps.dreamrs.fr/shinyWidgets/" target="_blank">shinywidgets</a>.


**Did you calculate the value you added to your company or the money you saved them? If so, how?**  

**Nicolas:** The easiest calculation was on the automation of the process. People could spend 2 or 3 months per year just on data processing. This multiplied by the number of planners, indicates the money saved only by automating the process. Considering that R & Shiny are free, this is a quick win!  

We also invested in RStudio Connect to be able to share those apps with different users (Supply Chain, Sales, Finance, Country Managers). The cost is really low compared to the savings done through automation and the time saved in sharing the analysis with different stakeholders.  

Then there were all the benefits around a proper calculation of demand & supply planning (reduction of shortages, management of allocations, etc.) that we did not quantify but mentioned.  

**Is there any interaction with a database with your applications?**  

**Nicolas:** Yes, for some apps using <a href="https://jrowen.github.io/rhandsontable/" target="_blank">rhandsontable</a> - (I also should try <a href="https://github.com/DillonHammill/DataEditR" target="_blank">DataEditR</a>). The user can input/change some data and launch a new calculation.  

**Where do you host your app? What about the security parameters and authorization matrix?**  

**Nicolas:** We are using RStudio Connect to host the various Shiny applications (and R Markdown files) behind the company firewall. Using RStudio Connect, we can decide which users can see which app and we then define a list of users per app.

**Did you build an API to communicate the data?**  

As per today, we haven’t built an API to communicate the data.


## Join the Supply Chain Community Conversation:  

Thank you to Nicolas for an awesome presentation on how he is using Shiny today. With all the interest from the community in this topic, we’d love to continue the discussion and connect us all through:  

* <a href="https://www.meetup.com/RStudio-Enterprise-Community-Meetup/" target="_blank">Future meetups</a> - Join us on July 26th for another R in Supply Chain Management event (details to be provided soon)
* <a href="https://r4ds.io/join" target="_blank">R for Data Science Online Learning Community</a> (Slack channel: #chat-supply_chain)
* RStudio Community

It would be great to hear from you on <a href="https://community.rstudio.com/t/recording-of-r-in-supply-chain-management-rstudio-enterprise-virtual-meetup/104459/2" target="_blank">RStudio Community</a> about your goals, challenges, and successes that you are having in this space.  

* How did code-based solutions help you pivot and respond to the pandemic?
* How are you using R to succeed in inventory management, inventory reduction and replenishment, delivery/shipments optimization, or demand forecasting?
* If you had a magic wand to deliver unlimited resources and budget, what projects would you be working on?

