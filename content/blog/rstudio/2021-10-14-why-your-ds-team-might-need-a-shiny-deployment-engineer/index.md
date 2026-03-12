---
title: Why Your Data Science Team Might Need a Shiny Deployment Engineer
people:
  - Isabella Velásquez
date: '2021-10-14'
slug: why-your-ds-team-might-need-a-shiny-deployment-engineer
categories:
  - Data Science Leadership
tags:
  - shiny
  - code-first
description: We interviewed Vergil Weatherford from Guidehouse to learn why they are planning to hire a Senior Shiny Deployment Engineer. Weatherford believes data science teams can benefit from someone who can apply software development best practices to support the deployment of high-quality R and Python applications into production.
alttext: Purple flowers in the foreground with trees, shrubs, and a blue sky in the background 
events: blog
image: thumbnail.jpg
ported_from: rstudio
port_status: in-progress
---
<caption>
Photo by Vineesh Ramayyan at <a href="https://nilgiris.nic.in/tourist-place/rose-garden-ooty/" target = "_blank" rel = "noopener noreferrer">Ooty Rose Garden</a>
</caption>


What do data science teams need to ensure their Shiny apps work as intended once they hit “publish”? Software industry best practices — like continuous integration, deployment, and delivery (CI/CD) — can support the creation of production-ready data tools. Teams can test algorithms and models as part of the development cycle, and data scientists can deploy their apps at any moment with confidence.

This is why <a href="https://guidehouse.com/" target = "_blank" rel = "noopener noreferrer">Guidehouse</a>, a leading global provider of consulting services to the public sector and commercial markets, is currently looking for a <a href="https://careers.guidehouse.com/jobs/14420?lang=en-us" target = "_blank" rel = "noopener noreferrer">Senior Shiny Deployment Engineer</a>. Helping drive adoption of DevOps methodologies for R- and Python-based web applications, the Senior Shiny Deployment Engineer will bridge the worlds between data science and software development.

In this post, we interview <a href="https://guidehouse.com/professionals/w/weatherford-vergil" target = "_blank" rel = "noopener noreferrer">Vergil Weatherford</a>, Associate Director on the Advanced Solutions team at Guidehouse. A long-time proponent of open-source tools, Vergil oversees the architecture needed to streamline complex data collection and smooth development of data products.

We were excited to learn more about Vergil’s work planning and implementing data infrastructure, why he drives the adoption of open source at Guidehouse, and his vision for a Senior Shiny Deployment Engineer that will contribute to the data science team’s culture of quality.

### Welcome! Could you tell us a bit about yourself and your work?

I am an energy consultant-turned-data tooling enthusiast. Day in and day out, I help my team adopt modern data science tools to boost productivity and solve our clients’ most complex challenges. 

My first day on the job as a consultant was more than 12 years ago. I was given dozens of CSV files and asked to analyze the time-series residential air conditioner runtime data using Excel. I quickly found myself asking, "Is this really the best way to do this?" The answer led me on a long journey to where I am today, where I work on a specialized team dedicated to supporting code-first data science infrastructure at Guidehouse.

### What does a modern data science infrastructure allow your team to do?

I mainly build infrastructure for an analytics team working on our clients’ most complex business challenges related to the clean energy transition. This work requires us to use a myriad of  datasets. We work regularly with "smart meter" data, SCADA data, customer demographics, and building characteristics. We run surveys and deploy data acquisition devices to collect detailed energy usage data. We're given time series data from IoT devices like smart thermostats and data feeds from electric vehicle (EV) charging stations. We then look across the broad spectrum of data and technologies to assess and develop solutions.

This is one of the things that makes analytics in consulting unique: getting all of these varied datasets from external sources poses challenges not found when data comes from inside an organization. We need tools that help us create meaning and value from data instead of focusing on data wrangling or cleaning.

We also need approaches that let us standardize analysis methods and develop reusable interfaces regardless of what the data looks like.  The consulting industry is seeing big growth in systematizing solutions and building data products that can be quickly redeployed for different clients. “Modularity” has become the operative word. By having a strong infrastructure in place, we can use our previous work to put together solutions more quickly.
  
### How did you end up adopting open-source tools?

As a long-time Linux hobbyist, I am continually looking for ways to leverage open source to solve problems. So when the management team was looking for alternatives to a proprietary — and expensive!  — statistical analysis platform seven years ago, I suggested R mainly due to its strong following in academia and its open source nature.

Fast-forward to the present, and our tooling looks very different than it did when I joined. We're still using some proprietary tools where they are a good fit but our "daily driver" toolkit is mainly open source: R, Python, and Git, with Linux under the hood. Central to delivering that toolkit, we use the full suite of RStudio Team Enterprise tools to scale our data science work and share results with clients.

### What made you pick Shiny specifically?

Our data science team has a large and talented R user base. They have experience solving all kinds of unique and challenging problems, like detecting the effects of programs designed to incentivize energy savings, forecasting electric vehicle demand, or optimizing the pathway to achieve decarbonization goals. We have built up a lot of R code over the years as we have solved these problems.

Early on, we experimented with GUI-based dashboarding tools, but the jump from analysis in R to visualization in other business intelligence tools had too many gaps. With tools like Shiny, we can seamlessly apply the skills our data scientists have built up over time.

Shiny also allows data scientists to carry the solution development process much further along the deployment lifecycle. The team is able to turn custom analyses into web applications. Then, we can use software like RStudio Connect to rapidly deploy and tweak those web applications. We’re able to iterate and innovate as quickly and often as we would like.


### Why are you looking for a Senior Shiny Deployment Engineer?

We have a lot of depth and expertise in being able to solve our clients’ most complex problems with R and want to improve our client’s end-to-end experience with our data products. To enable this, we recognize the need for formalizing the Software Development Lifecycle (SDLC) early in the process by bringing software industry best practices to bear.

The Senior Shiny Deployment Engineer will help us do that. However, while our main front-end framework is Shiny, we want to make sure we do not miss out on potential candidates coming from a computer science or formal software development background. The skills required to deploy robust data applications require knowledge of good SDLC practices for testing, CI/CD, and DevOps principles. Those are the sorts of things that data scientists usually have to read up on but are standard skill sets for deployment engineers.

Writing a good Shiny app and deploying that Shiny app into production are two different things. The purpose of the role is to help push client-facing solutions over the finish line. We need to build applications thoughtfully from the early stages and have strategies in place for testing, quality assurance, versioning, updates, and ongoing maintenance. This is where the Senior Shiny Deployment Engineer can really make a difference.

### What else would you like to add about the role?

Team members with understanding of both dashboard development and deployment infrastructure are at a premium. When I shopped around the idea of this role with a few solution development leads, they were extremely enthusiastic and said they were very interested to learn from someone with this expertise.

We are really looking for someone who is ready to take their career to the next level: a teammate who can partner with different teams to help establish a culture of quality of the final deployed product starting in the Shiny app architecture and development phase. We look forward to the Senior Shiny Deployment Engineer working alongside other team members to embed software engineering best practices in a community of more research-focused individuals.

### Conclusion

Working alongside a Shiny Deployment Engineer, data science teams can apply deployment best practices to their development lifecycle. Data scientists are able to automate and innovate their frameworks, and clients reap the benefits from robust data science products. **Interested in applying your SDLC skills as a Senior Shiny Deployment Engineer? <a href="https://careers.guidehouse.com/jobs/14420?lang=en-us" target = "_blank" rel = "noopener noreferrer">Apply here!</a>**

Learn more about <a href="https://guidehouse.com/" target = "_blank" rel = "noopener noreferrer">Guidehouse</a>:

* 4 consecutive years as a Forbes top employer
* Rated Top 50 Companies for Diversity by DiversityInc
* Certified as a Great Place to Work
* Committed to science-based targets to reduce our GHG emissions
