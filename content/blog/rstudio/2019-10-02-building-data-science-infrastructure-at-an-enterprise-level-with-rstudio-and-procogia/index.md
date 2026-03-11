---
title: Building Data Science Infrastructure at an Enterprise Level with RStudio and
  ProCogia
people:
  - Samantha Toet
date: '2019-10-02'
slug: building-data-science-infrastructure-at-an-enterprise-level-with-rstudio-and-procogia
categories:
- Events
blogcategories:
- Company News and Events
events: blog
image: thumbnail.png
ported_from: rstudio
port_status: raw
---

<sup> Photo by <a href="https://unsplash.com/@phoebezzf?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Zhifei Zhou</a> on <a href="https://unsplash.com/s/photos/seattle?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></sup>
  

We’re hosting a free, half-day event with one of our [Full Service Certified Partners](https://rstudio.com/certified-partners/), ProCogia, in Seattle on Wednesday October 9th. This event is for data science and IT teams that want to learn more about:

* helpful new RStudio R packages like `pins`
* what RStudio professional products can do for your data science team if you have both Jupyter and RStudio users
* using Kubernetes or Slurm to scale your work

**If you’re interested in learning more, be sure to register on the ProCogia event page:
[RStudio & ProCogia Roadshow: R in Enterprise](https://www.eventbrite.com/e/rstudio-and-procogia-roadshow-tickets-72099330037).**

For a taste of what to expect, here’s a discussion on using enterprise RStudio and python products to build a containerized data science development environment, written by Gagandeep Singh, data scientist and certified RStudio administrator, at ProCogia.

“Modern organizations are spending a considerable amount of resources on data science research and development. Companies are recognizing that the need to have a dedicated data science department in-house has increased exponentially. Companies are looking at external partners with dedicated competence and experience in this field to assist in building a comprehensive solution. As specialty data science consultants, we have established partnerships with popular data science platform providers such as RStudio and are involved in the JupyterHub project. For example, we were brought in by a multinational leading biotechnology company to design, develop and deploy an integrated data science development platform for their team of over 100 international data scientists. The ask was to build a comprehensive solution where users can use either R and/or Python, develop models, and share results through a common platform. 

The biggest concern for us was to provide a solution that could handle a multitude of user sessions, but also provide high-performance computing and resources at the same time. The safe option was to build a high-availability, load-balanced environment, although it might create troubles in the future as the number of users kept increasing and resources needed to be optimized.  

We instead decided to take a two-pronged approach, in which a Kubernetes-backed, containerized solution would be the primary interface, and a load-balanced product would be backing up any additional load. Users launch their own containers for each processing session and Kubernetes takes care of the backend resource allocations. They can run both Jupyter notebooks and R scripts in the container, and perform multiple assignments concurrently. The publishing platform, RStudio Connect, provides a cohesive product to share results through shiny applications, HTML reports, and even Jupyter Notebooks with Python code. RStudio Server Pro 1.2 now supports running sessions and jobs on Kubernetes.

Connect has both Python and R enabled. It has also been configured to schedule reports to be sent as emails. We also configured the RStudio Server Pro IDE in a load-balanced, high-availability environment. In this situation, the RStudio IDE’s internal load balancer works with AWS’s load balancer to accommodate backup and smooth operations in case any of the servers go down. The publishing platform is also configured with high availability, which means multiple servers are simultaneously serving the users’ publishing needs using a common database. We integrated a high-availability RStudio Package Manager into the mix, which enabled the administrator to establish control over both package access and downloads. Users could utilize RStudio Package Manager to access different versions of R packages. Our instance of Package Manager was also capable of serving internally developed packages by connecting to the original git source, which eliminated the need for additional administration. 

A customized solution that took into account security protocols, data sharing and management, and the needs of individual data scientists and administrators is what was needed. There cannot be a one-size-fits-all solution when it comes to the architecture of data science environments for organizations across various industries. The environment must be tailored to business goals, administrator concerns, and user productivity. A solution that works with regards to security protocols may not be a solution that works for users of the environment. The factors are all considered when creating a data science environment for organizations based on their specific goals at the time and in the future.” 

Space is limited, so reserve your seat now! 

Agenda:

* 8:30 am Registration & Breakfast
* 9:00 am Welcome & Introduction
* 9:15 am Open Source in Enterprise: a Virtuous Cycle - Lou Bajuk (RStudio)
* 9:45 am Automating RStudio Products in the Cloud - ProCogia
* 10:30 am Coffee Break
* 10:45 am The R Community in Transitioning to Pro from Open Source - Daniella Mark (ProCogia)
* 11:00 am Looking Ahead: R in Enterprise - Kevin Bolger (ProCogia)
* 11:30 am New Data Workflows in RStudio Connect Using the `pins` Package - Javier Luraschi (RStudio)
* 12:00 pm Closing Remarks & Lunch 





