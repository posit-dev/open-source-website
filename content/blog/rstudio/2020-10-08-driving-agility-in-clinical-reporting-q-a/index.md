---
title: 'Using R to Drive Agility in Clinical Reporting: Questions and Answers'
people:
  - Andy Nicholls 
  - Michael Rimler
date: '2020-10-08'
slug: driving-agility-in-clinical-reporting-q-a
categories:
  - Data Science Leadership
tags:
  - shiny
  - Python
  - R
description: Andy Nicholls and Michael Rimler from healthcare firm GlaxoSmithKline plc (GSK) answer questions posed during their recent webinar, Using R to Drive Agility in Clinical Reporting.
resources:
- name: "hero"
  src: "hero.jpg"
  title: "Webinar title image"
blogcategories:
- Data Science Leadership
- Products and Technology
events: blog
ported_from: rstudio
port_status: raw
---


Following our recent RStudio webinar, <a href="https://rstudio.com/resources/webinars/using-r-to-drive-agility-in-clinical-reporting/" target="_blank" rel="noopener noreferrer">Using R to Drive Agility in Clinical Reporting</a>, we received an unprecedented number of questions from the audience. In this blog post, we attempt to answer as many of the 70+ questions that we received as possible. In some cases, we have grouped multiple questions into one to streamline the answers. The opinions are our own and do not necessarily reflect GlaxoSmithKline plc's (GSK) position or strategy.

### Can you speak to any specific advantages of R over SAS with respect to stakeholder engagement, efficiency, or development time?

The main selling point for R is that it provides additional capabilities through tools like Shiny, Rmarkdown and the `officer` package, which allow us to improve the way we communicate with other functions. We've never really tried to make any speed comparisons or claims when promoting the use of R. It can be faster to develop in R, especially when simulating data, but for a large part of what we do there's not much difference in speed of development, and the execution time differences are negligible. That said, the licensing model (R being free) allows us to scale more easily when we use parallelism, which does reduce execution times.

### Can you provide further details on your approaches to validation?

Although it wasn't the main focus of the talk, we received a lot of questions relating to validation. It's important to note that we're still in the midst of our journey and still have some open questions. At this moment in time, the Working Area for R Programming (WARP) environment is **qualified**. We are now developing a GxP batch execution model that we will validate. The R Validation Hub's <a href="https://www.pharmar.org/white-paper/" target="_blank" rel="noopener noreferrer">white paper</a> highlights some of the challenges in this space and describes a risk-based approach for validation of R packages which is quite similar to the approach we will be taking.

### Are you currently submitting results from your R environment to regulatory agencies?

We have not yet used the environment to produce study tables, listing and figures for production. However, our aim is to use R in production beginning in 2021.

### Can you speak more to the challenges faced with respect to the adoption of Shiny? Is it used for regulatory work?

Building enthusiasm for Shiny has not been difficult at all. The bigger challenge is training and supporting new Shiny users. Thus far, this has mostly been webinar-based. We are active in promoting good practice and the use of training modules and have begun to share template code via our GitHub Enterprise instance. Thankfully, we don't generally have to worry about deployment, as RStudio Connect takes care of that for us. But some additional support for our users has been required to ensure that they understand how the deployments work, particularly with respect to data. We haven't yet attempted to include a Shiny app in a submission, but this is a very interesting area that GSK and several other companies have been looking at.

GSK Biostatistics is currently building a Shiny-based application for clinical data analysis and reporting. Given that this is part of a GxP compliant workflow, it has raised many interesting questions around audit trails, quality control (QC), and so on. The longer term hope is that dynamic visualisation applications will replace many static outputs for reporting out clinical trial data and analyses.

### Why did GSK decide to first integrate R rather than other open source languages such as Python?

R offered a better starting point at GSK. Many of our Research Statisticians and Data Scientists were already using R. While we recognize the value of different programming languages for clinical reporting, we chose to begin our open source journey with R to leverage the synergies of the efforts coming from Statistical Data Sciences who already are driving broader R use within Biostatistics.

### What is your strategy for Python?

We have taken a strategic decision to treat R as a gateway to additional open source languages such as Python. The process for Python will likely be similar, but we will learn a lot from our journey with R. Given that our Python user base is much smaller, it is likely that we will initially explore the use of Python through R and RStudio (which is also a great IDE for Python), focusing on its strengths in the Machine Learning space.

### As GSK integrates into R, what is the migration strategy for SAS macro libraries into R?

We are not planning to migrate or translate our SAS reporting tools into R. There are a number of open source R packages that already provide fundamental capabilities required along the conventional clinical data pipeline from collection to clinical study report. Packages that were developed in-house for the R4QC project were primarily designed to reduce the volume of code used by streamlining common functionality with the reporting pipeline. In addition, there are a number of groups in the industry that are developing open source R packages that could collectively deliver the pipeline without the need for translating our SAS macro libraries.

### Will you be open sourcing your packages?

I am pleased to say that we have very recently agreed upon an approach that will enable us to open source several of the packages that we have developed. More news to follow later in the year.

### How do you address the underlying discrepancies between basic statistical calculation in SAS and R?

This is a great question. In R4QC, we noticed differences in both default rounding methodology and quantile calculations. In survival analyses, we also noticed a difference in the reported standard error. In all cases, results from both languages were consistent with their respective documentation.

<style type="text/css"> 
.quote-spacing { padding:0 80px; } 
.quote-size { font-size: 160%; line-height: 34px; } 
[@media] only screen and (max-width: 600px) {
.quote-spacing { padding:0; } 
.quote-size { font-size: 120%; line-height: 28px; }
}
</style>
<div style="background-color: #4476bb; color: #ffffff; padding:50px 30px 30px 30px; margin:50px 0;">
   <div class=".quote-spacing">
      <p class=".quote-size">
         <i>“Fundamentally, we believe that the challenge is not to ensure that the results from R and SAS match completely for a given analysis. Indeed, some analyses in one language may not even be possible to easily replicate in the other. Rather, the analysis should be based on sound statistical theory, taking into account such aspects as the underlying statistical hypothesis and distribution of the data.”
         </i>
      </p>
   </div>
</div>

### Why not combine all potential tools, including SAS, R and Python altogether to gain the best insights?

Our ultimate objective is exactly this - to expand the analyst's toolkit in order to facilitate more agility in our delivery of insights. In the GxP world where we must demonstrate reproducibility, traceability, and data integrity, it is not simply the flip of a switch. Along with other leaders in the industry, we are working toward a modern analytics environment where our capabilities are not constrained by the capabilities of a single piece of software.

### What is the percentage uptake of R among SAS programmers?

This is a great question, one that we are still learning through. Our operational uptake in the clinical reporting space has been slower that expected, but we believe it is primarily due to the timing study milestones and the availability of our training offerings.

When we green-lighted using R for Independent QC programming of non-statistical displays, many teams found themselves actively working on studies that were already in progress. SAS programs had already been developed for Independent QC, and the teams could not justify the time and effort required to reprogram using R without putting timelines at risk.

In addition, our initial training modules were designed as intensive, face-to-face sessions with hands-on programming opportunities. It may go without saying, but COVID-19 threw a wrench into the 2020 plans for making these trainings available to Biostatistics staff. The training team has worked hard to redesign the sessions to be delivered virtually and we have successfully restarted the training effort.

We expect to see a stronger rate of uptake in the near future.

### How will the move to R reflect in GSK's recruitment strategy?

The importance of R as a key skill will continue to grow. We are already actively seeking programmers with skills in R, for conventional reporting activities (datasets, tables, listings, figures), future activities (Shiny apps), and conventional Data Science roles. Further roles within our Statistical Data Sciences team will start to appear on our website soon.

### Conclusion

We're confident that the answers above address the overwhelming majority of questions that we received, but if we still haven't managed to respond to your questions then we can only apologize. Thank you for listening to the webinar and reading through this Q&A. We look forward to sharing more in the future!
