---
title: RStudio Adds New R Features in Qubole's Open Data Lake
people:
  - Samantha Toet
date: '2020-08-03'
slug: rstudio-adds-new-r-features-in-qubole-s-open-data-lake
tags:
- Workbench
description: Data science teams using Qubole now have the ability to use RStudio Server
  Pro seamlessly within the Qubole platform to access and analyze large datasets.
resources:
- name: qubole-launch
  src: qubole-launch.png
  title: Qubole Launch
events: blog
ported_from: rstudio
port_status: in-progress
---


<sup>
<p class="text-right">Launch RStudio Server Pro from inside the Qubole platform</p>
</sup>

We are excited to team up with Qubole to offer data science teams the ability to <a href="https://spark.rstudio.com/examples/qubole-cluster/" target="_blank" rel="noopener noreferrer">use RStudio Server Pro from directly within the Qubole Open Data Lake Platform</a>. Qubole is an open, simple, and secure data lake platform for machine learning, streaming and ad-hoc analytics. RStudio and Qubole customers now have access to RStudio’s out-of-the-box features and Qubole’s unique managed services that supercharge data science and data exploration workflows for R users, while optimizing costs for R-based projects. Within the Qubole platform, data scientists are able to easily access and analyze large datasets using the RStudio IDE, securely within their enterprise running in their public cloud environment of choice (AWS, Azure, or Google).

With massive amounts of data becoming more accessible, data scientists increasingly need more computational power. Cluster frameworks such as Apache Spark, and their integration with R using the SparkR and SparklyR libraries, help these users quickly make sense of their big data and derive actionable insights for their businesses. However, high CPU costs, long setup times, and complex management processes often prevent data scientists from taking advantage of these powerful frameworks.

Now that Qubole has added RStudio Server Pro into its offering, it now offers its users:

* **Single click access to Spark clusters**. With Qubole’s authentication mechanisms, no additional sign-in is required. 
* **Automatic persistence** of users’ files and data sets when clusters are restarted. 
* **Pre-installed packages** such as Sparklyr, tidyverse, and other popular R packages.
* **Cluster Package Manager** allows users to define cluster-wide R & Python dependencies for Spark applications
* **Performance optimizations** such as Qubole’s optimized spark distribution allows the cluster to automatically scale up when the sparklyr application needs more resources and downscales as cluster resources are not in use.
* **Spark UI, Logs, and Resource Manager links** available in the RStudio Connections pane for seamlessly managing applications. 

<div style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/vfmdaIwxbMw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Enterprise users benefit from this new integration because this new upgraded platform:
 
* **Limits CPU expenses to what users need.** The Qubole cluster automatically scales up when the sparklyr application needs more resources, and downscales when cluster resources are not un use. 
* **Allows on-demand cluster use.** With single-click integration, users can seamlessly access large datasets that can persist automatically. 
* **Simplifies cluster management.** Qubole’s Cluster Package Manager, with pre-installed R packages, lets users define R and Python dependencies across their clusters. 

### How do I enable this integration? 

If you already are a Qubole customer, and would like to enable RStudio Server Pro in your environment, please <a href="https://www.qubole.com/company/contact-us/" target="_blank" rel="noopener noreferrer">contact</a> your Qubole support team. 
 
### Want to learn more about RStudio Server Pro?

<a href="https://rstudio.com/products/rstudio-server-pro/" target="_blank" rel="noopener noreferrer">RStudio Server Pro</a> is the preferred data analysis and integrated development experience for professional R users and data science teams who use R and Python. RStudio Server Pro enables the collaboration, centralized management, metrics, security, and commercial support that professional data science teams need to operate at scale.
 
**<a href="https://rstudio.com/products/rstudio-server-pro/evaluation/" target="_blank" rel="noopener noreferrer">Try a Free 45 Day Evaluation</a>** or **<a href="https://rstudio.chilipiper.com/book/rsp-demo" target="_blank" rel="noopener noreferrer">See in in Action</a>**

