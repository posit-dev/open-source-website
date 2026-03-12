---
title: Equipping Your Data Science Team to Work from Home
people:
  - Carl Howe
date: '2020-05-12'
slug: equipping-wfh-data-science-teams
categories:
- Data Science Leadership
tags:
- Connect
- Workbench
- Shiny Server Pro
- RStudio Package Manager
resources:
- name: work-from-home-desk
  src: work-from-home-desk.jpg
  title: Photo of a work-from-home desk
blogcategories:
- Data Science Leadership
events: blog
ported_from: rstudio
port_status: in-progress
---

<sup>Photo by Djurdjica Boskovic on Unsplash</sup>

If your data science team experienced an abrupt transition to working at home, it may be a good time to rethink their development tools. In this post, I'll talk about why laptop-centric data science gets in the way of strong data science teams and why you should consider deploying development and publishing servers.

## Working from Home Has Affected Both People and Data

Like tigers and koalas, we data scientists are fairly solitary creatures. We typically eschew meetings, embrace focus time, and block out distractions to focus on our work. And on those rare times when we need help, our typical reaction is to walk over to a colleague's desk and brainstorm an answer.

Enter COVID-19 and the new work-from-home environment. At first glance, it would appear nothing really has to change for the typical data science workflow; team members armed with laptops appear well-equipped to continue their data science work. However, many data science teams are now struggling with:

- **Collaborative deprivation.** While we all feel some sense of isolation during this lockdown, working from home deprives data scientists of their most effective collaboration techniques. Without the ability to pop over to someone's desk to ask a question or get help debugging a piece of code, many data scientists find themselves not making the progress they are used to.
- **Locked-in development licenses**. Many teams have been rather chagrined to find that their commercial data analysis software licenses are only valid in their enterprise environment, forcing them into a painful dance with VPN software when working from home.
- **Firewalled data**. Many organizations prohibit access to sensitive corporate data from outside the firewall to limit security risks and preserve user privacy. That's no big deal when the data science team is working from an office, but it becomes a serious issue when working from home.
- **Inconsistent laptop environments**. Data scientists often download their own versions of libraries and development tools. However, that means that code developed on one data scientist's laptop won't necessarily work for another data scientist who has different versions of packages loaded. Working from home without regular contact with other team members allows these inconsistencies to fester and grow, raising roadblocks to reproducible results. Worse, data scientists risk losing code and data living in those unique laptop environments should their hard drive fail or their laptop fall victim to a household accident.

## Serious Data Science Requires Collaborative Tools

To be able to do their work collaboratively and repeatably, data science teams need infrastructure that encourages it and is supported by the organization and IT. That typically means shared servers for:

- **Code Development**. Having a shared development server allows everyone to share a consistent programming environment. Servers can also be configured to provide more computational and memory resources for the team to share, including back end CPU and GPU clusters. For teams working on machine learning models, for example, training a new model on a laptop might take days, while training that same model using a Kubernetes cluster might only take hours or minutes. And since the development server is typically hosted within the organization firewall, it can be configured to have full access to datasets that would not be allowed externally.
- **Application publishing**. Data scientists who used to share their insights using a conference room and a projector now need ways to publish results that don't require real-time attendance. While most companies have some types of internal web servers, those rarely support R and Python run-time environments. Data science teams need a publishing platform that is easy to use, letting them share work without opening an IT ticket for every change.
- **Package control**. Solitary data scientists tend to do their own package management, frequently installing the latest and greatest packages that they find. However, using the latest and greatest software can often backfire when other team members try to reproduce or build onto their work. Storing approved packages on a centralized server and defining that as the standard data science environment makes your data science work more reproducible and long-lasting.

## Which Servers Should You Choose?

Which server-based tools you choose obviously depend on factors such as team size, workload, and company software policies. RStudio offers both open source and commercial alternatives, allowing organizations to choose whichever satisfies their needs best. Table 1 summarizes both approaches.

In addition to providing enhanced security, auditing, and usage monitoring, Pro solutions add other benefits that are less quantifiable. Specifically:

- **RStudio Server Pro adds back end computational muscle.** As we noted above, many data science workloads benefit significantly from being run on server platforms with beefy processors and capacious memory. RStudio Server Pro offers a feature called <a href="https://solutions.rstudio.com/documents/Scaling-RStudio-Server-Pro-with-Kubernetes.pdf" target="_blank" rel="noopener noreferrer">Launcher that can offload R and Python job execution onto a back end Kubernetes or SLURM cluster</a>. For groups doing serious machine learning, this one feature can speed up the team's productivity significantly.
- **RStudio Connect creates a production environment that your team controls**. Shiny apps, Jupyter Notebooks, and R Markdown documents are great tools for communicating with people outside your data science team, but they need a place to live. RStudio Connect provides that place to live and gives your team a secure, centralized portal for data products, automated emails, and Plumber and Dash APIs that let non-data scientists make use of their insights.
- **RStudio Package Manager ensures your team's work is repeatable**. With 15,000 R packages on CRAN constantly being updated, an R application that runs with today's versions of those packages won't necessarily work with tomorrow's. Package Manager makes it easier to have stable access to packages, so your whole team can be using the same playbook. It can also restrict packages versions to only those that have been certified by a central authority, thereby ensuring approved results. 

<table>
  <tr>
    <th> Open Source Solution</th>
    <th> Value </th>
    <th> Pro Solution </th>
    <th> Added Value in Pro </th>
  </tr>
  <tr>
    <td><a href="https://rstudio.com/products/rstudio/#rstudio-server">RStudio Server</a></td>
    <td>
      <ul>
        <li>Broadens access to development tools</li>
        <li>Boosts compute and memory resources available</li>
        <li>Ensures common development environment</li>
      </ul>
    </td>
    <td><a href="https://rstudio.com/products/rstudio/#rstudio-server">RStudio Server Pro*</a></td>
    <td>
      <ul>
        <li>Adds collaborative editing and projects</li>
        <li>Supports multiple R versions and sessions</li>
        <li>Provides Launcher support for back end execution clusters</li>
        <li>Supports bilingual data science teams with Jupyter</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><a href="https://rstudio.com/products/shiny/shiny-server/">Shiny Server</a>,<br />Homegrown Web Servers</td>
    <td>
      <ul>
        <li>Eases publishing of Shiny applications</li>
        <li>Allows broad access to data science results</li>
      </ul>
    </td>
    <td><a href="https://rstudio.com/products/connect/">RStudio Connect</a></td>
    <td>
      <ul>
        <li>Consolidates many types of content on one server</li>
        <li>Allows scheduled production and emails</li>
        <li>Hosts R- and Python-based APIs</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><a href="https://cran.r-project.org/web/packages/miniCRAN/index.html">miniCRAN Mirror</a></td>
    <td>
      <ul>
        <li>Maintains a local copy of packages from approved sources</li>
      </ul>
    </td>
    <td><a href="https://rstudio.com/products/package-manager/">RStudio Package Manager</a></td>
    <td>
      <ul>
        <li>Speeds installs using binaries</li>
        <li>Allows use of multiple package versions and checkpoints for roll back</li>
        <li>Provides package use insights for IT</li>
      </ul>
    </td>
  </tr>
</table>

#### Table 1: Open Source and Professional Server Options To Support Data Scientists.

*RStudio Server Pro, RStudio Connect, and RStudio Package Manager are also available bundled as RStudio Team.</caption>

## Don't Be Afraid To Mix and Match Servers As Your Needs Dictate

The collaboration processes data science teams have used for years have already been disrupted by COVID-19 and work from home mandates. The question for data science leaders is what they can do to provide new ways of working that are as good or better than what went before. Centralizing your data science development and production processes is a way to do that.

Emily Riederer, an Analytics Manager at Capital One, <a href="https://vimeo.com/theranchstudios/review/398622411/383d5791b1?sort=lastUserActionEventDate&direction=desc" target="_blank" rel="noopener noreferrer">summarized some of the benefits she’s seen from this centralized approach</a> at RStudio::conf 2020.

<div style="padding: 35px 0 35px 0;">
<script src="https://fast.wistia.com/embed/medias/cac6g1r9gr.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_cac6g1r9gr videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/cac6g1r9gr/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>
</div>

With that said, using servers to make your work-from-home data science team more productive doesn't have to be a Manhattan Project all-or-nothing proposition. If your data scientists are comfortable developing code on their laptops, you may want to begin by installing a publishing platform like RStudio Connect, and put off development and package management servers for another day. Similarly, some teams start by installing RStudio Server for centralized development and defer publishing and package management. But for teams doing serious data science, they have to start somewhere.

We’ll be posting additional commentary and case studies on equipping data science teams to work from home in the coming weeks. In the meantime, we recommend <a href="https://appsilon.com/rstudio-connect-as-a-solution-for-remote-data-science-teams/" target="_blank" rel="noopener noreferrer">a recent post about how Appsilon has used Connect</a> to create a remote work-friendly culture. 

## For More Information

If you’d like to learn more about how to better equip your data science team to work from home, we recommend:

- **<a href="https://rstudio.com/resources/rstudioconf-2019/rstudio-job-launcher-changing-where-we-run-r-stuff/" target="_blank" rel="noopener noreferrer">Changing Where We Run Stuff</a>**. This 18-minute video of an RStudio::conf 2019 talk by Darby Hadley describes how Launcher improves workload scaling and isolation. 
- **<a href="https://solutions.rstudio.com/launcher/kubernetes/#want-to-learn-more-about-rstudio-server-pro-and-kubernetes" target="_blank" rel="noopener noreferrer">RStudio Server Pro with Kubernetes Overview</a>**. This document provides architectural block diagrams and links to frequently asked questions about RStudio Pro and Launcher.
- **<a href="https://rstudio.com/products/connect/" target="_blank" rel="noopener noreferrer">The RStudio Connect Product Page</a>**. This overview of RStudio Connect provides links to several videos going into details of how it can help your data science team communicate better throughout the organization.
- **<a href="https://rstudio.com/resources/rstudioconf-2020/building-a-new-data-science-pipeline-for-the-ft-with-rstudio-connect/" target="_blank" rel="noopener noreferrer">Building a new data science pipeline for the FT with RStudio Connect</a>.** George Kastrinakis from the Financial Times presented this 16-minute talk at RStudio::conf 2020 about how RStudio Connect significantly sped up its data science work and made it more agile.
- **<a href="https://rstudio.com/resources/webinars/reproducibility-in-production/" target="_blank" rel="noopener noreferrer">Reproducibility in Production</a>.** This webinar by Garrett Grolemund describes how computational documents (such as RMarkdown and Jupyter Notebooks) help deliver reproducible results for your business stakeholders. 
- **<a href="https://rstudio.com/resources/webinars/introduction-to-the-rstudio-package-manager/" target="_blank" rel="noopener noreferrer">Introduction to RStudio Package Manager</a>.** This recorded webinar provides a detailed description of what RStudio Package Manager is and how it aids reproducibility in R applications.

