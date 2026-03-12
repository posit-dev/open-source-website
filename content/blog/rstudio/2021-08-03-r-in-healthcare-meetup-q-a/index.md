---
title: R in Healthcare Meetup Q&A
people:
  - Chris Bumgardner
date: '2021-08-03'
slug: r-in-healthcare-meetup-q-a
events: blog
categories:
  - Data Science Leadership
  - Events
tags:
  - Use Cases
description: The team at Children’s Wisconsin is using R and RStudio’s suite of tools to enable forecasting, modeling, and data mining among other data science activities. During the meetup, Chris Bumgardner shared a few examples of the applications that have been created to support their vision that the kids of Wisconsin will be the healthiest in the nation.
blogcategories:
 - Industry
alttext: Cultivating an R-Based Analytic Practice title slide
image: thumbnail.jpg
ported_from: rstudio
port_status: in-progress
---
<div class="lt-gray-box">
<i>This is a guest post from Chris Bumgardner, Data Science Program Manager at Children’s Wisconsin. The RStudio Enterprise Community group recently hosted an <a href="https://www.youtube.com/watch?v=pHZ8dsc0PhY" target="_blank">R in Healthcare meetup</a> highlighting the powerful work that Chris and his team are doing to help ensure Wisconsin’s kids are healthy, happy, and safe.</i>
</div>

An active academic healthcare organization requires tools and practices that enhance the application of statistical and algorithmic approaches. 

To positively impact care, system operations, or even well-being at the community-level, these tools need to support solutions which can be rapidly deployed and communicated as well as reproduced when studying longitudinal trends.

At Children’s Wisconsin, we are using R and RStudio’s suite of tools to enable forecasting, modeling, and data mining among other data science activities. We communicate the results of our efforts using interactive applications built with Shiny as well as reports and push analytics created using RMarkdown. 

During the <a href="https://www.youtube.com/watch?v=pHZ8dsc0PhY" target="_blank">R in Healthcare meetup</a> on June 30th, I shared how we have developed this capability and provided a few examples of the applications that have been created to support our vision that the kids of Wisconsin will be the healthiest in the nation.

I’ve included the full Q&A below, which also includes the response to any questions that went unanswered.

## Meetup Q&A:
**How is data collected, cleaned, stored, retrieved that fuels this great work?**  

The data science team is a small team and we sit within the analytics group. We have data engineers in the larger analytics team that are shared. The data engineers help bring in a lot of this data and we store it in our data warehouse. For this application, we pull the processed data into an R data file for Shiny to use. This results in much better performance for our users. The data engineers perform a lot of the data cleaning and scrubbing, but we collaborate with them. The data scientists will usually take the first pass with a rough cut of the data, think about what we need, look for quality issues as well as other statistical concerns, and then the data engineers will automate our process to productionalize that.

**What are you using to link igraph to the selected youth info panel? Is it crosstalk or something else?**  

To update the child details table when clicking on a node in the network it is using the **selected** event firing from the outputed visNetwork object.

More details can be found in the <a href = "https://cran.r-project.org/web/packages/visNetwork/vignettes/Introduction-to-visNetwork.html" target = "_blank">Introduction to visNetwork</a> vignette in the **Use with Shiny** section.

In the example code below, I watch for the selection to occur (the output is named “full_network”, so visNetwork creates an input with the suffix of “_selected” when used in a Shiny application), filter to the correct child, and then pass the information to a helper function to create the actual informational panel.

    #Update the node_info table with child details on the full network
    
    output$node_info <- renderTable({
      
    req(input$full_network_selected)
    
    dat <- placement_df %>%
      filter(ChildID == input$full_network_selected) 
    
    return(createChildInformation(dat))
  
  
**What is the organizational structure of your data science program within the organization and how have you gotten buy-in to build R into the analytics infrastructure?**  

<script src="https://fast.wistia.com/embed/medias/w03jvpjn3n.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_w03jvpjn3n videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/w03jvpjn3n/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

<font size="2" skip=0pt><div align="right">Full meetup recording <a href="https://youtu.be/pHZ8dsc0PhY" target="_blank">here</a></div></font>

Back in 2012-2013, we brought the majority of the analysts together into an enterprise analytics group. Instead of having them dispersed among the departments within Children’s Wisconsin, we brought them together to try and build a shared understanding of our data, tools, and common data definitions and rules. At the same time we were rolling out a new electronic health record (EHR). It was a perfect time to bring everyone together and level-set on data and data sources. Then at some point, we would possibly spin individual analysts back out into the business. 

For analysts not officially included on the common team we created an Analytics Center of Excellence to reach out to power users to help disperse this information, but the majority of the analysts still sit within the enterprise team and that’s the team that data science is a part of. We have plenty of analysts and 2-3 data scientists who work on the more strategic, longer-term projects.

To get buy-in, I think it’s those small wins where you can actually get in, deep-dive, learn all you can and produce an insight that will “wow” the team. I know it’s hard to predict when that’s possible, but I think we’ve been lucky in that we’ve had very curious counterparts on the business side and at the hospital that work with us to help achieve that initial success. Once we garner the first win, they will want to share it and so we initially used the open-source Shiny Server. Once we got to a point where we needed to have our solutions tied into Active Directory and share outputs securely, that’s where we really started to gain the necessary toehold to integrate R more fully.

**How open is data access for your data science team within your organization?**  

Our data science team and analysts have access to just about everything we need. In our data warehouse we have the ability to apply user-level security to the included data sets and if we require additional access for a certain project we can usually get the permissions necessary. Overall, it hasn’t been an issue within our organization.

**How long does it take to go from concept to production for a project like this? Does the engineering work occur before or alongside your build?** 

I would say it’s very iterative. With the COVID app, we brought it up in a week or two because it could build on the other dashboards we have created. Once we have something scripted, we then have these template or skeletal apps where we can pull something together quickly. We are definitely leveraging our great analysts and data engineers to pull a lot of the data together for us before we even have to work on a problem. The Inpatient Modeling app I shared started for me at the end of April, so that app, including the simulations and scenarios came together in two months. I think it can be very rapid and that’s really the power of R. We can be so iterative and responsive in a short amount of time - once you’re fluent in it of course.

**In your organization, how do you determine whether ethics approval is required for exploratory data analysis or modeling?**  

While we do not have a dedicated ethics review panel, we do have an Institutional Review Board (IRB) for research requests involving human subjects. With approved requests there are well-defined pathways for what is to be included and how to handle modifications to the request.

For operational or performance improvement requests we have a multi-disciplinary team that triages data-related project requests and considers ethical factors in addition to time and resources when deciding when and if a project will be initiated.

Most importantly, as an organization we understand the importance of fairness and limiting bias in our models. This awareness has led us to not use outputs from models lacking in transparency or that give us hesitation when considering equitable care. We still have much to do in this area!

**In your application, are “confirmed” children those have been trafficked, or are participating as actors in the trafficking of others?**

Those children could be either a victim or a participant. The state of Wisconsin has an indicator guide for child trafficking and we follow those definitions. There are three tiers included in the state’s guide that we also use in the application. 

It is important to note that the factors associated with each tier are used to guide the classification, and the tier status is not a quantitative score that is simply totalled to arrive at a category. Human intervention is still required before any of the tier levels are assigned.

**‘Anon’ v 0.7.0 - is that package available externally?**  

This package is something that I created for use within our Shiny applications. It’s something that we could definitely consider making publicly available on GitHub. It’s enabled via the switch on the introductory page of the Shiny app that then runs the code to anonymize all the names shown in the application. We use baby names from the Social Security Administration and surnames from the U.S. Census Bureau to create reasonable names that are similar by year of birth and sex.


**How do you decide when to use Shiny vs. flexdashboard? What about R vs. BI tools?**  

I have considered this question myself when I thought about how much we want to take on as a data science team whenI think about the analytics program as  a whole. The larger team has BI developers who currently specialize in QlikView. I think the choice usually comes down to what our analysis will be used for, how long the organization will need those results, and how they will be shared. At first, we will do mostly ad-hoc analysis with static outputs and when we start to see that there is a longer term need to have some interactivity, we’ll bring in Shiny. Usually it starts with R Markdown or a flexdashboard that is a little lighter weight. If the request is something that’s truly servicing our service line needs, such as counts, volumes, or something we have an existing QlikView app for, we’ll push it to the appropriate resources within the analytics team. The data scientists are a scarce resource and we want to ensure they are having the most impact they can within the list of prioritized work.


**Does your team validate R Packages or is it a requirement at all?**  

Yes, we do make efforts to validate the R packages we use regularly and maintain a standard list of “trusted” packages that we recommend to other R users in the organization. While we do not technically limit what packages can be used, we encourage best practices via lunch and learn sessions, code reviews, and an internal Slack channel. We are also piloting the use of the RStudio Package Manager, which we are using to help make package management easier and more consistent across the organization and within the Data Science environment.

**What type and/or amount of clinician involvement do you have on your team?**  

We are definitely partnering every step of the way. We have a CMIO (Chief Medical Information Officer) who works very closely with us to understand and support our analytic efforts. Our Enterprise Analytics team is not within what would be considered the traditional IS (Information Systems) organizational structure. Instead, we’re located within our Health Management group which is similar to a population health team. We actually have nurses/RNs on that team as well which enables us to be more engaged with the various entities across the health system. For any kind of request that comes in, we’re always working with providers side by side which is very enjoyable. This collaboration is a great thing about Children’s. We get a lot of involvement, which helps make us successful. This is something that we look for as we take on new projects too - how invested is the business side before we go too far with it.


## Keeping the conversation going:

If you have follow-up questions, are interested in speaking at a future meetup, and/or would like to be a part of this R in Healthcare Community, join the <a href="https://join.slack.com/t/rinhealthcare/shared_invite/zt-sc7lc4k6-K9zb~kX826dOXMcaj~Wt~w" target="_blank">Slack group here</a>.
