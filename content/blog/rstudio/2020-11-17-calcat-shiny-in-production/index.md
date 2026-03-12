---
title: How California Uses Shiny in Production to Fight COVID-19
people:
  - Daniel Petzold
date: '2020-11-19'
slug: using-shiny-in-production-to-monitor-covid-19
categories:
  - Data Science Leadership
  - Shiny
  - RStudio Connect
  - Workbench
  - RStudio Package Manager
tags:
  - shiny
description: RStudio analyzes how the California Department of Public Health built a COVID-19 dashboard in R and Shiny that now serves millions of California citizens.
resources:
- name:  "hero"
  src:   "hero.jpg"
  title: "Hero image"
- name:  "opioid"
  src:   "opioid-dashboard.png"
  title: "Opiod dashboard"
- name:  "covid"
  src:   "covid-dashboard.jpg"
  title: "Covid dashboard"
blogcategories:
- Data Science Leadership
- Products and Technology
events: blog
image: thumbnail.jpg
ported_from: rstudio
port_status: in-progress
---

<figure>
<img align="center" src="hero.jpg">
  <figcaption><i>Short term forecast from the <a href="https://calcat.covid19.ca.gov/cacovidmodels/" target="_blank" rel="noopener noreferrer">California COVID Assessment Tool (CalCAT)</a></i></figcaption>
</figure>

> "Things move along so rapidly nowadays that people saying: "It can't be done," are always being interrupted by somebody doing it." *-- Puck magazine, 1903.*

As we at RStudio have talked about the topic of <a href="https://blog.rstudio.com/2020/05/19/driving-real-lasting-value-with-serious-data-science/" target="_blank" rel="noopener noreferrer">serious data science</a>, we often field questions about the suitability of R for use in large-scale, production environments. Those questions typically coalesce around:

1.  **Speed:** Is R fast enough to run production workloads?
2.  **Scalability:** Can R be used for large scale production?
3.  **Infrastructure:** What kind of R infrastructure do administrators need to run production applications?

Instead of debating these question in theory in this post, we'll instead turn to an organization that is not just talking about deploying Shiny dashboards in large-scale production, but is actually "doing it".

Many definitions exist for what constitutes an application being in large-scale production. For the purposes of this article, we'll define large-scale production as:

<div style="padding:0px 30px 0px 30px; margin:20px 0;">
   <div class=".quote-spacing">
      <div class=".quote-size">
         <i>Applications serving thousands of users on a daily basis.</i>
      </div>
   </div>
</div>

One application that fits this definition nicely is the California COVID Assessment Tool (CalCAT) which serves 32 million Californian citizens. CalCAT is a Shiny dashboard written in R by a group of data scientists within the California Department of Public Health (CDPH) and is hosted on an array of commercial <a href="https://rstudio.com/products/team/" target="_blank" rel="noopener noreferrer">RStudio Team</a> servers.

RStudio recently talked with members of the team who deployed this dashboard to understand how this public, large-scale Shiny app came to be. The following sections present some of our takeaways from those discussions.

<style type="text/css"> 
.quote-spacing    { padding:0 80px; } 
.quote-size       { font-size: 160%; line-height: 34px; } 
.speaker-quote    { padding-left: 50px; text-indent: -50px; }
.no-speaker-quote { padding-left: 50px; }

[@media] only screen and (max-width: 600px) {
   .quote-spacing { padding-top:0; } 
   .quote-size    { font-size: 120%; line-height: 28px; }
}
</style>

## CDPH's First Shiny Dashboard Tracked Opiod Use

<figure>
  <div style="padding: 35px 0 0 0;">
    <a href="https://skylab.cdph.ca.gov/ODdash/" target="_blank" rel="noopener noreferrer">
      <img align="center" src="opioid-dashboard.png">
    </a>
  </div>
  <figcaption><i>CDPH's <a href="https://skylab.cdph.ca.gov/ODdash/" target="_blank" rel="noopener noreferrer">Opioid Overdose Surveillance application</a></i></figcaption>
</figure>

The CalCAT dashboard project was born out of CDPH's experience fielding a prior public-facing Shiny dashboard in 2016, namely the  <a href="https://skylab.cdph.ca.gov/ODdash/" target="_blank" rel="noopener noreferrer">CDPH Opioid Overdose Surveillance application</a>. That application evolved largely from:

- **A need to get data out quickly.** CDPH didn't really have an enterprise-level dashboarding solution secured in 2016. When the opioid crisis arrived, the department realized it needed to get data out quickly and update it as needed as the epidemic gripped the state.
- **The ability to deploy a dashboard using free software and cloud resources.** When looking for a dashboarding solution, one of the developers evaluated Shiny, realized it was free and open source, and that RStudio offered shinyapps.io for a very low cost way for CDPH to deploy it. Without the need for a capital investment to get started, they created some basic visualizations, shopped them to leadership including the director of the department, and got the full go-ahead to develop and deploy shortly thereafter. This allowed them to get their opioid dashboard out in 3 or 4 months, which was unheard of at the time.
- **A positive reception by users.** California was one of the first states in the country that had a public opioid overdose dashboard. This positive experience with Shiny and shinyapps.io generated interest in R and encouraged the building of more internal infrastructure for hosting and deploying these apps.

## COVID-19's Arrival Made Sharing Data Mission Critical

When COVID-19 arrived in the United States in early 2020, many organizations, both inside and outside of the California Department of Public Health, suddenly found themselves wanting data to respond to the pandemic. That demand led to:

- **The formation of the CalCAT development team.** CalCAT evolved out of some early work with Johns Hopkins University regarding scenario-based models. Initially, CalCAT just wanted to develop a quick lightweight app to explore the simulations that Johns Hopkins was providing and to share it using an RStudio Connect server with other CDPH staff.
- **Creation of a extranet-hosted Shiny dashboard for COVID-19.** Based on their experience with the Opioid Dashboard, the team developed an internal Shiny app to provide visualizations of what was going on throughout the state. As the dashboard evolved, CDPH moved it to the state government extranet for others to access.
- **Expanding the dashboard to serve other departments with data.** While the app began as an effort to share data with county health officers and local epidemiologists, people from other departments started asking, "How did you get this number? We can't replicate it." That led the team to expand the app to allow users to download the code and data behind the visualizations and do their own analyses.

Once other departments gained access to the data, the app quickly became a vital source of COVID information throughout the state because it:

- **Allowed authenticated access to internal confidential data.** Because the COVID dashboard authenticated county health officers to gain access to the Shiny app, it could include aggregated confidential data beyond what would normally be available to the general public.
- **Supported county-based dashboards.** County health jurisdictions found that they could download their county's data and republish it on their own dashboards, thereby giving their users visibility into their local situation.
- **Drove county-level pandemic actions.** California established <a href="https://covid19.ca.gov/safer-economy/" target="_blank" rel="noopener noreferrer">hard metrics such as case and infection rates</a> to guide which businesses were allowed to open. The data published by this extranet dashboard ensured everyone was working from a consistent set of measurements and actions that were authorized by the state.

## Responding to the Emergency: Creating A Public Dashboard for California Citizens

<figure>
  <div style="padding: 35px 0 0 0;">
    <a href="https://calcat.covid19.ca.gov/cacovidmodels/" target="_blank" rel="noopener noreferrer">
      <img align="center" src="covid-dashboard.jpg">
    </a>
  </div>
  <figcaption><a href="https://calcat.covid19.ca.gov/cacovidmodels/" target="_blank" rel="noopener noreferrer"><i>The CalCAT public dashboard</i></a></figcaption>
</figure>

The extranet site helped CDPH and the county health officers understand both the depth and breadth of pandemic infections within California. However, on March 4, 2020, the following announcement spurred the department to build a public site. 

> "As part of the state's response to address the global COVID-19 outbreak, Governor Gavin Newsom today declared a State of Emergency to make additional resources available, formalize emergency actions already underway across multiple state agencies and departments, and help the state prepare for broader spread of COVID-19. The proclamation comes as the number of positive California cases rises and following one official COVID-19 death." <i>-- Gavin Newsom, Governor of California, March 4, 2020</i>

In response to the Governor's mandate, the team:

- **Deployed the public COVID dashboard app you see today.** Based on their work with their internal county-based dashboard and with advice from DJ Patil, the Chief Data Scientist of the United States in the Obama administration, the team modified and upgraded the internal county-based app into what you currently see today. This dashboard allows people to explore both the California models and an ensemble of estimates from other organizations to provide a single picture for the state and its counties. The team used R to do some statistical work in the background while also creating interactive visualizations to share those results.
- **Made their code open source.** The CalCAT team made <a href="https://github.com/StateOfCalifornia/CalCAT" target="_blank" rel="noopener noreferrer">the source code for the site public on Github</a> so anybody in the world could access and improve on it. In addition to the website, they also created an open data portal for the state that includes additional aggregated data.

## CDPD's R Infrastructure Evolved to Support the Pandemic Efforts

As CalCAT gained popularity and the team gained experience, the infrastructure supporting the team evolved to meet the new demands by adding:

- **Multiple hosting environments.** The CalCAT environment now features both a public-facing environment and an extranet environment that requires authentication with partners and staff. CDPH now also has internal testing platforms on which they run apps before they go out to the public-facing and extranet servers.
- **Professional products**. While the project started off with open source Shiny Servers and shinyapps.io for the Opioid Dashboard, the team later moved to RStudio Server Pro for development and then added RStudio Connect and RStudio Package Manager for publishing. They now run multiple instances of those products to spread the workload out and accommodate the millions of users who access the public site.
- **Collaborative workflows**. Once the team grew beyond just one or two developers, it created <a href="https://github.com/StateOfCalifornia/CalCAT" target="_blank" rel="noopener noreferrer">a Github repository</a> where it could collaboratively work on code, push changes, and adopt changes from others. While this workflow required scientists within the department to learn basic devops software development techniques, the team decided the benefits from collaboration were worth climbing that learning curve.

### CalCAT's Success Has Encouraged R Use Within CDPH

The project team noted how much the Opiod dashboard changed CDPH's thinking about how R could be used to deliver data to the public by:

- **Providing examples of what was possible.** The Opioid dashboard expanded the scope of what could be done with CDPH data. The CalCAT dashboard proved that, with the help of their infrastructure and IT team, such applications could be scaled up to provide service to the public. Collaborating with IT also introduced the CalCAT scientists to software tools they wouldn't have discovered themselves.
- **Rapidly deploying new apps.** After the COVID dashboard was up, other groups started asking for new apps that could tackle other aspects of the crisis. One such application was a very simple program to create unique IDs for COVID tests, which was mandated and published within a week. The ability to respond quickly to department needs burnished R's reputation within CDPH.
- **Creating an internal R community.** The team is already seeing real expansion in personnel with R skills, especially in hiring. Their job descriptions now ask for R skills, and people are being recruited from other disciplines. Increasingly, the personnel within the department are coming in with R experience.
- **Embracing a code-based approach.** One developer noted that writing code to do data science instead of using a point-and-click tool was analogous to a team doing rock climbing. Working code creates a path and anchors for others to use, and new developers then can use those anchors to follow in their footsteps.

## Takeaways

The CalCAT experience shows that, despite claims to the contrary, R can be used for large-scale production applications. When we re-examine the three categories of concern about R with which we started the piece, we discover that:

-   **Speed of development was the key to success.** This was an application that had to be deployed quickly in response to a national emergency. Using R and Shiny allowed the team to deploy an interactive app that provided access to COVID data in weeks, not months.
-   **Scaling up production use was an evolutionary process.** The team took advantage of its prior experience with the Opioid Dashboard to deploy both the extranet and public versions of the COVID-19 application. The team had already deployed public apps on shinyapps.io and had deployed server infrastructure in house as part of their extranet application. When the time came to go public with the public CalCAT dashboard, scaling up became mostly a matter of replicating servers they already had experience with.
-   **Infrastructure to support this application was available off the shelf.** Instead of having to roll their own deployment process, the group was able to use RStudio's server product suite to do the app development as well as the large-scale deployment on an array of RStudio Connect servers.

By using a code-based approach, the California Department of Public Health has built a repository of human and intellectual capital around building public health dashboards. This small team's work and open source code can now be passed on to others both within and outside of California government. Their efforts will likely spawn new projects that will better inform citizens and continue to help them stay safe throughout this unprecedented pandemic.

## To Learn More

You can learn about each of RStudio's commercial products by following the links below.
<ul>
  <li>
    <a href="https://rstudio.com/products/rstudio-server-pro/" target="_blank" rel="noopener noreferrer">RStudio Server Pro</a> delivers fully integrated development environments for R and Python accessible via a browser.
  </li>
  <li>
    <a href="https://rstudio.com/products/connect/" target="_blank" rel="noopener noreferrer">RStudio Connect</a> connects data scientists with decision makers with a one-button publishing solution from the RStudio IDE.
  </li>
  <li>
    <a href="https://rstudio.com/products/package-manager/" target="_blank" rel="noopener noreferrer">RStudio Package Manager</a> controls package distribution for reproducible data science.
  </li>
  <li><a href="https://rstudio.com/products/team/" target="_blank" rel="noopener noreferrer">RStudio Team</a> bundles RStudio Server Pro, RStudio Connect, and RStudio Package Manager products to ease purchasing and administration.
  </li>
</ul>
