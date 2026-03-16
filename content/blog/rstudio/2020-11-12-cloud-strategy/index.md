---
title: Where Does RStudio Fit into Your Cloud Strategy?
people:
  - Lou Bajuk
date: '2020-11-12'
slug: cloud-strategy
categories:
  - Data Science Leadership
tags:
  - RStudio Cloud
description: "Over the last few years, more companies have begun migrating their data science work to the cloud. As they do, they naturally want to bring along their favorite data science tools, including RStudio, R, and Python. In this blog post, we discuss the various ways RStudio products can be a part of that journey."
blogcategories:
- Data Science Leadership
events: blog
ported_from: rstudio
port_status: in-progress
---

<sup>Photo by <a href="https://unsplash.com/@mantashesthaven?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="blank" rel="noopener noreferrer"> Mantas Hesthaven</a> on <a href="https://unsplash.com/s/photos/journey?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="blank" rel="noopener noreferrer">Unsplash</a></sup>

Over the last few years, more companies have begun migrating their data science work to the cloud. As they do, they naturally want to bring along their favorite data science tools, including RStudio, R, and Python. In this blog post, we discuss the various ways RStudio products can help you along that journey.

## Why Do Organizations Want to Move to the Cloud?

There are many reasons why organizations are looking to use cloud services more widely for data science. They include:

-   **Long delays and high startup costs for new data science teams:** When you bring a new team of data scientists onboard, it can be costly and time consuming to spin up the necessary hardware for the team. New hardware might be needed for developing data science analyses or for sharing interactive Shiny applications for stakeholders. These burdens tend to fall either on the individual data scientists or on DevOps and IT administrators who are responsible for configuring servers.
-   **Obstacles to collaboration between organizations or groups:** If a team is restricted to operating within their organization's firewall, it can be very difficult to support collaboration or instruction between groups that don't normally interact with each other. For example, running a data science workshop or statistics class can be unwieldy if everyone is working within their own separate environments.
-   **High costs of computing infrastructure:** Another key challenge is the potentially high costs of setting up and maintaining an organization's computing infrastructure, including both hardware and software. These costs include the initial investments, maintenance and upgrade fees, and the related manpower costs.
-   **Difficulty scaling to meet variable demand:** Scaling server resources to satisfy highly variable data science demands can be very difficult because organizations rarely maintain excess capacity. For example, an organization may want to publish a news article or a COVID dashboard for which they expect high demand, only to discover that it needs the IT organization to spin up a back-end Kubernetes cluster to handle the load.
-   **Excessive time and costs moving the data to the analysis:** If an organization's data is already stored on one of the major cloud providers or in a remote data center, moving that data to your laptop for analysis can be slow and expensive. Ideally, you should perform the data access, transformation and analysis as close to where the data lives as possible. Not doing so could subject you to excessive data transfer charges to move the data.

## Let Your Data Science Goals Drive Your Cloud Strategy

Depending on the circumstances of your organization and what specific challenges you are trying to address, you should consider four possible options for your data science cloud strategy:

-   **Hosted and Software as a Service (SaaS) offerings:** A fully hosted service can minimize the cost and time required to start up a new project. However, functionality may be limited compared to on premise offerings and integration with your internal data and infrastructure can be challenging.
-   **Deployment to a Virtual Private Cloud (VPC) provider:** Deploying software on a major cloud platform such as Amazon Web Services (AWS) or Azure can provide the full flexibility and customization of on premise software. However, setting up a virtual private cloud application often requires more management overhead to integrate with your internal systems as well as careful administration of usage to avoid unexpected usage charges.
-   **Cloud marketplace Offerings:** Pre-built applications offered on services such as the AWS and Azure Marketplaces make it easy to get started at a pay-as-you-go hourly cost, but require careful management to ensure the software is available and running only when needed.
-   **Data science in your data lake:** By embedding your data science tools into your existing data platform, your computations can be run close to the data, minimize overhead, and easily tie into your data pipeline. However, this adds additional complexity and potential limitations.

We're provided the table below to help you assess the various RStudio cloud offerings. It matches up problems and potential solutions with specific RStudio options and resources to consider. The options are arranged in order of increasing complexity of configuration and administration.

<div class="text-center mt-5">
<strong>Table 1: Summary of Cloud Options for RStudio Software</strong>
</div>
<table>
  <thead>
  <tr>
    <th class="problem"> Problem </th>
    <th class="solution"> Potential Solution </th>
    <th class="proscons"> Pros and Cons </th>
    <th class="options"> Options to consider </th>
  </tr>
  </thead>
  <tr><td>Simplify and reduce startup costs </td>
    <td> SaaS/Hosted offering </td>
    <td><div class="procon">Pros:</div>
    <ul><li>Simplest and lowest cost to deploy</li>
	      <li>Hardware and software managed by the provider</li>
	      <li>Costs may be fixed, variable or a mix of the two</li>
    </ul>
    <div class="procon">Cons:</div> <ul><li>Limited integration with your organization’s internal data and security protocols. </li>
	<li>May not be cost efficient for large groups</li>
	<li>May have limited options for custom configuration</li>
    </ul></td>
    <td><div class="action">Create data science analyses with <a href="https://rstudio.cloud/" target="blank" rel="noopener noreferrer">RStudio Cloud</a></div>
      <div class="action">Share Shiny applications with <a href="https://www.shinyapps.io/" target="blank" rel="noopener noreferrer">shinyapps.io</a></div>
      <div class="action">Manage packages with <a href="https://packagemanager.rstudio.com/client/#/" target="blank" rel="noopener noreferrer">RStudio Public Package Manager</a>, a free service to provide easy installation of package binaries, and access to previous package versions</div>
    </td>
  </tr>
  <tr>
    <td> Promote collaboration or instruction between organizations or groups </td>
    <td> SaaS/Hosted offering </td>
    <td> <div class="procon">Pros:</div>
      <ul>
	<li>Same pros as above, plus the ability to easily share projects</li>
      </ul>
      <div class="procon">Cons:</div>
      <ul>
	<li>Same cons as above</li>
      </ul>
    </td>
    <td> Share projects or teach classes/workshops with <a href="https://rstudio.cloud/" target="blank" rel="noopener noreferrer">RStudio Cloud</a> </td>
  </tr>
  <tr>
    <td rowspan="2"> Mitigate high costs of computing infrastructure </td>
    <td> Marketplace Offerings </td>
    <td> <div class="procon">Pros:</div>
      <ul>
	<li>Easy to get started at minimal, pay-as-you-go (hourly) cost.</li>
	<li>Access to specialized hardware (e.g GPUs)</li>
      </ul>
      <div class="procon">Cons:</div>
      <ul><li>To manage hourly costs, careful management is required to ensure software is running only when needed </li>
      </ul>
    </td>
    <td>
      RStudio products on <a href="https://aws.amazon.com/marketplace/seller-profile?id=6185573f-e9d3-4df1-a8da-2cd4996a3561" target="blank" rel="noopener noreferrer">AWS Marketplace</a>, <a href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=rstudio" target="blank" rel="noopener noreferrer">Azure Marketplace</a>, and <a href="https://console.cloud.google.com/marketplace/partners/rstudio-launcher-public" target="blank" rel="noopener noreferrer">Google Cloud Platform</a>.
    </td>
  </tr>
  <tr>
    <td> Deployment to a VPC on a major cloud provider </td>
    <td> <div class="procon">Pros:</div>
      <ul>
	<li>Outsources hardware costs</li>
	<li>Integrates with existing analytic assets on cloud platforms</li>
	<li>Allows easy customization and configuration</li>
	<li>Provides access to specialized hardware (e.g GPUs)</li>
	<li>Ensures data sovereignty by running your processes in a local cloud region</li>
      </ul>
      <div class="procon">Cons:</div>
      <ul>
	<li>Complexity of managing software configuration and integration with your organization’s on-premise data and security protocols. </li>
	<li>Costs may be highly variable, based on usage</li>
      </ul>
    </td>
    <td> <div class="action">Deploy RStudio products in a VPC, using cloud formation templates for AWS and Azure ARM template (See <a href="https://github.com/rstudio/rstudio-cloud-tools" target="blank" rel="noopener noreferrer">RStudio Cloud Tools</a>)</div>
      <div class="action">Deploy RStudio products via Docker e.g. use EKS (Elastic Kubernetes Service) on AWS. (See <a href="http://github.com/rstudio/rstudio-docker-products" target="blank" rel="noopener noreferrer">Docker images for RStudio Professional Products</a>)</div>
      <div class="action"><a href="https://docs.rstudio.com/pro-drivers/" target="blank" rel="noopener noreferrer">Connect to cloud based data storage</a>, such as Redshift or S3.</div>
    </td>
  </tr>
  <tr>
    <td> Scale to meet variable demand </td>
    <td> Clustering approaches, including Kubernetes </td>
    <td> <div class="procon">Pros:</div>
      <ul>
	<li>Cloud-deployed applications can be easily scaled to meet demand, since cloud providers provide container resources on demand.</li>
      </ul>
      <div class="procon">Cons:</div>
      <ul>
	<li>Careful management required to avoid unnecessary compute costs, while still matching job requirements to computational needs.</li>
      </ul>
    </td>
    <td>
      <div class="action">In addition to the points above, <a href="https://solutions.rstudio.com/launcher/kubernetes/" target="blank" rel="noopener noreferrer">RStudio Server Pro's Launcher</a> integrates with Kubernetes, an industry-standard clustering solution that allows efficient scaling.</div>
      <div class="action">RStudio Connect provides <a href="https://support.rstudio.com/hc/en-us/articles/231874748-Scaling-and-Performance-Tuning-in-RStudio-Connect" target="blank" rel="noopener noreferrer">many options to scale and tune performance</a>, including being part of an autoscaling group. These options allow Connect to deliver dashboards, Shiny applications, and other types of content to large numbers of users.</div> 
    </td>
  </tr>
  <tr>
    <td> Minimize data movement </td>
    <td> Data lakes </td>
    <td> <div class="procon">Pros:</div>
      <ul>
	<li>Run your computations close to the data, minimizing overhead</li>
	<li>Tie your data science directly into your data pipeline</li>
      </ul>
      <div class="procon">Cons:</div>
      <ul>
	<li>Adds additional complexity and potential limitations</li>
      </ul>
    </td>
    <td>
      <div class="action"><a href="https://www.qubole.com/qubole-supercharges-capabilities-for-data-science-and-exploration-via-rstudio-integration/" target="blank" rel="noopener noreferrer">RStudio Server Pro in Qubole Data Platform</a>, for Azure, AWS and  GCP</div>
      <div class="action"><a href="https://spark.rstudio.com/examples/databricks-cluster/" target="blank" rel="noopener noreferrer">Use sparklyr with DataBricks</a></div>
      <div class="action"><a href="https://docs.rstudio.com/pro-drivers/" target="blank" rel="noopener noreferrer">Connect to cloud based data storage</a>, such as Redshift or S3.</div>
      <div class="action">Managed RStudio Server Pro on Spark and Hadoop on Azure and AWS (<a href="https://cazena.com/data-lake-solutions/rstudio" target="blank" rel="noopener noreferrer">Cazena</a>) </div>
    </td>
  </tr>
</table>

## Ready to Take RStudio to the Cloud?

If you'd like to take RStudio along on your journey to the cloud, you can start by exploring the resources linked in the table above. We also invite you to join us on December 2 for a webinar, "<a href="https://rstudio.com/registration/why-data-science-in-the-cloud/" target="blank" rel="noopener noreferrer">What does it mean to do data science in the cloud?</a>", conducted with our partner <a href="https://www.procogia.com/" target="blank" rel="noopener noreferrer">ProCogia</a>. You can <a href="https://rstudio.com/registration/why-data-science-in-the-cloud/" target="blank" rel="noopener noreferrer">register for the webinar here</a>.

Our product team is also happy to provide advice and guidance along this journey. If you'd like to set up a time to talk with us, you can <a href="https://rstudio.chilipiper.com/book/schedule-time-with-rstudio" target="blank" rel="noopener noreferrer">book a time here</a>. We look forward to being your guide.


<style>

table thead th {
  border-bottom: 1px solid #ddd;
}
th {
  font-size: 90%;
  background-color: #4D8DC9;
  color: #fff;
  vertical-align: center 
}
td {
  font-size: 80%;
  background-color: #F6F6FF;
  vertical-align: top;
  line-height: 16px;
}
caption {
  padding: 0 0 16px 0;
}
table {
  width: 100%;
}
th.problem {
  width: 15%;
}
th.solution {
  width: 15%;
}
th.proscons {
  width: 35%;
}
th.options {
  width: 35%;
}
div.action {
  padding: 0 0 16px 0;
}
div.procon {
  padding: 0 0 0 0;
}
td.ul {
  padding: 0 0 0 0;
  margin-block-start: 0em;
}
table {
  border-top-style: hidden;
  border-bottom-style: hidden;
  border-collapse: separate;
  text-indent: initial;
  border-spacing: 2px;
}
table>thead>tr>th, .table>thead>tr>th {
  font-size: 0.7em !important;
}
table>tbody>tr>td {
  line-height: inherit;
  vertical-align: baseline;
}
table tbody td {
  font-size: 14px;
}
</style>
