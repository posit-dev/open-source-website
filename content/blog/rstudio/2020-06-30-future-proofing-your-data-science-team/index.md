---
title: Future-Proofing Your Data Science Team
people:
  - Dean Wood 
date: '2020-06-30'
slug: future-proofing-your-data-science-team
categories:
- Data Science Leadership
tags:
- data science
description: Data science today requires allowing employees to work from home. Mango
  Solutions believes that a centralized cloud-based platform and collaborative communication
  are key to making data science teams productive.
blogcategories:
- Data Science Leadership
events: blog
image: thumbnail.jpg
ported_from: rstudio
port_status: raw
---


<sup>Photo by <a style="color: #000000;" href="https://unsplash.com/@sushioutlaw?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Brian McGowan</a> on <a style="color: #000000;" href="/s/photos/brian-mcgowan-tomorrowland?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></sup>

*This is a guest post from RStudio's partner, Mango Solutions*

As RStudio’s Carl Howe recently discussed in his blog post on <a href="https://blog.rstudio.com/2020/05/12/equipping-wfh-data-science-teams/" target="_blank" rel="noopener noreferrer">equipping remote data science teams</a>, with the rapidly evolving COVID-19 crisis, companies have been increasingly forced to adopt working from home policies. Our technology and digital infrastructure has never been more important. Newly formed remote data science teams need to maintain productivity and continue to drive effective stakeholder communication and business value, and the only way to achieve this is through appropriate infrastructure and well-defined ways of working. 

Whether your workforce works remotely or otherwise, centralizing platforms and enabling a cloud based infrastructure for data science will lead to more opportunities for collaboration. It may even reduce IT spend in terms of equipment and maintenance overhead, thus future-proofing your data science infrastructure for the long run. 

So when it comes to implementing long-lived platform, here are some things to keep in mind:

## Collaboration Through a Centralized Data and Analytics Platform

A centralized platform, such as RStudio Server Pro, means all your data scientists will have access to an appropriate platform and be working within the same environment. Working in this way means that a package written by one developer can work with a minimum of effort in all your developers’ environments allowing simpler collaboration. There are other ways of achieving this with technologies such as _virtualenv_ for Python, but this requires that each project set up its own environment, thereby increasing overhead. Centralizing this effort ensures that  there is a well-understood way of creating projects, and each developer is working in the same way. 

When using a centralized platform, some significant best practices are:

- **Version control**. If you are writing code of any kind, even just scripts, it should be versioned religiously and have clear commit messages. This ensures that users can see each change made in scripts if anything breaks and can reproduce your results on their own. 
- **Packages**. Whether you are working in Python or R, code should be packaged and treated like the valuable commodity it is. At Mango Solutions, a frequent challenge we address with our clients is to debug legacy code where a single ‘expert’ in a particular technology has written some piece of process which has become mission critical and then left the business. There is then no way to support, develop, or otherwise change this process without the whole business grinding to a halt. Packaging code and workflows helps to document and enforce dependencies, which can make legacy code easier to manage. These packages can then be maintained by RStudio Package Manager or Artifactory. 
- **Reusability.** By putting your code in packages and managing your environments with _renv_, you’re able to make your data science reusable. Creating this institutional knowledge means that you can avoid a Data Scientist becoming a single point of failure, and, when a data scientist does leave, you won’t be left with a model that nobody understands or can’t run. As Lou Bajuk explained in his blog post, <a href="https://blog.rstudio.com/2020/06/24/delivering-durable-value/" target="_blank" rel="noopener noreferrer">Does your Data Science Team Deliver Durable Value?</a>, durable code is a significant criteria for future-proofing your data science organization.

## Enabling a Cloud-based Environment

In addition to this institutional knowledge benefit, running this data science  platform on a cloud instance allows us to scale up the platform easily. With the ability to deploy to Kubernetes, scaling your deployment as your data science team grows is a huge benefit while only requiring you to pay for what you need to, when you need it.

This move to cloud comes with some tangential benefits which are often overlooked. Providing  your data science team with a cloud-based environment has a number of benefits:

1. The cost of hardware for your data science staff can be reduced to low cost laptops rather than costly high end on-premise hardware.
2. By providing a centralized development platform, you allow remote and mobile work which is a key discriminator for hiring the best talent.
3. By enhancing flexibility, you are better positioned to remain productive in unforeseen circumstances.

This last point cannot be overstated. At the beginning of the Covid-19 lockdown, a nationwide company whose data team was tied to desktops found themselves struggling to provide  enough equipment to continue working through the lockdown. As a result, their data science team could not function and were unable to provide insights that would have been  invaluable through these changing times. By contrast, here at Mango, our data science platform strategy allowed us to switch seamlessly to remote working, add value to our partners, and deliver insights when they were needed most. 

Building agility into your basic ways of working means that you are well placed to adapt to unexpected events and adopt new platforms which are easier to update as technology moves on.

Once you have a centralized analytics platform and cloud-based infrastructure in place, how are you going to convince the business to use it? This is where the worlds of Business Intelligence and software dev-ops come to the rescue. 

Analytics-backed dashboards using technologies like Shiny or Dash for Python with RStudio Connect means you can quickly and easily create front ends for business users to access results from your models. You can also easily expose APIs that allow  your websites to be backed by scalable models, potentially creating new ways for customers to engage with your business. 

A word of caution here: Doing this without considering how you are going to maintain and update what have now become software products can be dangerous. Models may go out of date, functionality can become  irrelevant,  and the business can become disillusioned. Fortunately, these are solved problems in the web world, and solutions such as containers and Kubernetes alongside CI/CD tools make this a simpler challenge. As a consultancy we have a tried and tested solutions that expose APIs from R or Python that back high-throughput websites from across a number of sectors for our customers. 

## Collaborative Forms of Communications

The last piece of the puzzle for your data science team to be productive has nothing to do with data science but is instead about communication. Your data science team may create insights from your data, but they are like a rudderless ship without input from the business. Understanding business problems and what has value to the wider enterprise requires good communication. This means that  your data scientists have to partner with people who understand the sales and marketing strategy. And if you are to embrace the ethos of flexibility as protection against the future, then good video-conferencing and other technological communications are essential. 

<hr style="width:100%;border:1px solid rgba(0,0,0,.1);margin:50px 0">

### About Dean Wood and Mango Solutions

Dean Wood is a Data Science Leader at <a href="https://www.mango-solutions.com"  target="_blank" rel="noopener noreferrer">Mango Solutions</a>. Mango Solutions provides complex analysis solutions, consulting, training, and application development for some of the largest companies in the world. Founded and based in the UK in 2002, the company offers a number of bespoke services for data analysis including validation of open-source software for regulated industries.


