---
title: 'Strategic Analytics at Monash University: How RStudio Accelerated the Transformation'
people:
  - Behrooz Hassani-Mahmooei
date: '2021-06-24'
slug: strategic-analytics-at-monash-university-how-rstudio-accelerated-the-transformation
categories:
  - Data Science Leadership
tags:
  - Use Cases
description: Similar to any other large and complex organisation, Monash University employs a wide range of data to inform decision making and monitor different aspects of their operations.
blogcategories:
 - Data Science Leadership
events: blog
alttext: A colorful metal sculpture in fron of a modern building with 2 hexagonal floors
ported_from: rstudio
port_status: in-progress
---
<sup>Photo credit: <a href="https://www.monash.edu/" target="_blank">Monash University</a></sup>

<div class="lt-gray-box">
*This is a guest post from Dr. Behrooz Hassani-Mahmooei, Director of Strategic Intelligence and Insights Unit, and his team at <a href="https://www.monash.edu/" target="_blank">Monash University</a>, Australia*
</div>


Similar to any other large and complex organisation, at Monash University we employ a wide range of data to inform decision making and monitor different aspects of our operations; such as student outcomes, academic performance, research outputs, human resources and financial records.  

Following significant focus on people and system resources, as well as progress in data management and reporting, the university shifted its focus to build capacity to use these rich data sources to inform and support strategic decision making.   

Specifically, we aimed to integrate the collection, routine reporting and analysis of the existing large internal datasets to the development of data-driven insights which inform strategic thinking and decision making at the senior executive level.  

**Monash University's Approach:**  

* [**The Journey to Strategic Analytics**](#Journey)
    - [Linking internal and external data](#Link)
    - [Creating flexible analytics relevant to strategic decisions](#Flexible)
    - [Making the results accessible and understandable](#Accessible)
    - [Making our analysis findings relevant to the world around us](#Relevant)
* [**Three Key Workstreams**](#Workstreams)
    - [Establish a Platform for Data Linkage](#Establish)
    - [Deliver Analytics that are Flexible, Proactive and Integrated](#Deliver)
        - [Flexible data handling](#handling)
        - [Making analytics proactive, not reactive](#proactive)
        - [Fully integrated and collaborative analytic teams](#collaborative)
    - [Translate Analytic Research through Visualisations](#Translate)
* [**Integrating analytics into the broader strategic conversation**](#Strategic)

## <a name="Journey"></a>The Journey to Strategic Analytics

In 2017, Monash University established the Strategic Intelligence and Insights Unit (InSight), composed of members with multidisciplinary and diverse backgrounds and a broad set of research expertise, analytic skills and solid experience in higher education. 
InSight was tasked to employ advanced and multidisciplinary approaches to deliver innovative data solutions, intelligence, and insights to support the University’s strategy and help the University secure its positioning globally.  

We identified four main opportunities in our path to transition from day to day operational reporting toward strategic analytics:

* <a name="Link"></a>**Linking internal and external data:** We needed to bring together sources of internal data and establish reproducible processes to link internal and external data in a consistent, timely and reliable manner. We recognised early that there was no perfect single source of truth that combined all of the data sources across the university. Instead, we needed to create a flexible platform to run major data linkages with low cost and high accuracy.
* <a name="Flexible"></a>**Creating flexible analytics relevant to strategic decisions:** It was key to use advanced techniques and innovative solutions to establish the most relevant measures and indicators that could be linked to the high-level strategic questions and decisions across the institution. Ideally, this approach should minimise any manual interventions and instead deliver reproducible and reliable analyses.
* <a name="Accessible"></a>**Making the results accessible and understandable:** Another opportunity was presenting the data and insights in a concise, informative and accessible way that could be easily adopted and utilised to inform high-level strategic conversations. We needed to establish our role as analytics translators to link data to domain knowledge without delivering unnecessary business context or complicated analysis. 
* <a name="Relevant"></a>**Making our analysis findings relevant to the world around us:** Our internal data is limited to what we collect and the scope of our functions and services. To deliver outputs that can inform the senior management to make decisions, we need to reach beyond our own organisation and interrogate our local data within the broader evidence.  

## <a name="Workstreams"></a>Three Key Workstreams  

1. **Establish a Platform for Data Linkage**
2. **Deliver Analytics that are Flexible, Proactive and Integrated**
3. **Translate Analytic Research through Visualisations**

### <a name="Establish"></a>Establish a Platform for Data Linkage   
One of the key steps in delivering strategic analytics is harnessing the richness of multiple complementary datasets through data linkage and making it accessible across the university. We established two programs of work in this area.

Firstly, we designed and delivered a framework for linking our internal data scattered across different environments and organisational systems using the best practice methods using R. 

For example, in 2019, we linked a significant number of our internal data sources focused on student outcomes and experience. This involved linking separate datasets from the time a student commences at Monash University (admissions), all their activities during their studies (grades, extracurricular activities, student experience surveys, unit evaluations) through to life after graduation (graduate outcomes). 

This platform enabled us to run a wide range of analysis to understand how different programs and interventions impact the academic and non-academic outcomes of students as well as their career post-graduation. Secondly, it enabled us to link some of our internal data to available datasets outside our environment. 

For example, one of our projects involved cleaning, structuring and recalculating a large number of performance indicators (learning and teaching, research, finance, human resources) from the top 200 universities. We used this data to analyse the key drivers of research expenditure as well as emerging patterns in research outputs and partnerships across the world.

Different key features of R, such as rich capability in text analysis and reshaping data helped us link these sources of information, despite the lack of proper linkage keys and inconsistency across datasets.
 
 
### Deliver Analytics that are Flexible, Proactive and Integrated

One of the key challenges that many organisations face today is how to link the outcomes of their data science and analytics teams to decisions and interventions that lead to tangible results for their business. 

In the past few years, many Australian public and private organisations have established and then disbanded data science teams due to a range of barriers and failures such as lack of rich structured data to inform advanced analysis, unclear connection between the analysis and the business targets and outcomes, and lack of role clarity between business intelligence (BI), data analytics and data science teams. Another challenge that many public organisations such as universities face is the transition from data reporting frameworks that are mostly driven by compliance (such as reporting student numbers to the government) toward designing data-driven strategies.

Strategic analytics, in our experience, is driven by three key changes to how things are done traditionally:    
 
1. <a name="handling"></a>**Flexible data handling:** Administrative data frequently arrives in different formats and structures, disrupting the data preparation process. The traditional response requires manual interventions to address these issues.    
 
    Our approach is designed to deal with the uncertainty in the data automatically. If there are changes in the data format, the scripts can fix them with minimum input from the analysts, minimizing the time needed for manual preparation and analysis of the data.  
    
    For example, if we are analysing a time series dataset that has a structural break that can occur unexpectedly and needs to be identified and corrected for, we embed processes in the code that automatically identify where the break happens and correct for it. This means that in most cases we only need to deal with a data wrangling, transformation or quality issue once.
 
2. <a name="proactive"></a>**Making analytics proactive, not reactive:**  Historically, data analysis has been a responsive activity. For example, a strategic conversation at an executive meeting or a brainstorming session concludes with a data analysis request based on the direction of the meeting. The results from the analysis are then used to inform future conversations to validate or clarify an issue.

    However, using the platforms that we established, we successfully prepared the data to be part of that first conversation. This allowed the analysis to contribute to the direction of these conversations as early as possible rather than being done in response to them. Data analytics experts were made available, or even invited to participate, in the strategic discussions, highlighting the reliance on data-informed strategic thinking. The data could be interrogated throughout the strategic discussion to inform strategic thinking and progress the conversation beyond the initial context queries to explore the deeper underlying strategic issues. 
 
3. <a name="collaborative"></a>**Fully integrated and collaborative analytic teams:** Traditionally, different stages of analytics (for example descriptive, diagnostic, predictive and prescriptive) are done by different people using different tools and as separate steps. 

    We built capacity within the university by upskilling people across the organisation in using core methodologies and systems to consider analytics from an integrated perspective whereby each step informed the next. Critically, the prescriptive step which aims to inform an intervention was not conducted by a separate data science team in isolation, but instead by analysts with business knowledge who had conducted the descriptive, diagnostic and predictive phases. This added an important contextual element to the analysis which enhanced the strategic relevance of the analysis.

### <a name="Translate"></a>Translate Analytic Research through Visualisations    
Members of the InSight Unit have a strong background in research and about half of the team have completed a PhD in areas such as econometrics, applied economics, business information systems, and computational modelling. As a result of this expertise, the team was able to apply many core concepts of designing, planning, and undertaking a research project into the process of delivering analytics services. This helped the team deliver uniquely valuable insights and outputs.

This is most evident in the way that the team utilises data visualisation to communicate the findings of its analysis. Using the rich features of R and relying on the Connect Server, we were able to share a wide range of outputs from the team. These ranged from a simple descriptive statistic on student outcomes to the results of a complex regression analysis on co-authorship patterns. These results were visualised, communicated and translated so that they could be used by the senior management team to design intervention, policies and strategies across a wide range of areas.

As part of this communication, we considered using existing reporting tools. We found that BI tools are very useful when you want to start from data and generate information. However, when you have a specific decision that you are expected to inform on, especially a strategic decision, you need tools that enable you to start from that decision and reverse engineer back to the data. That is where R helped give us a competitive advantage, providing maximum flexibility and reproducibility as well as clarity for communication and translation.
 
## <a name="Strategic"></a>Integrating Analytics into the Broader Strategic Conversation

The InSight team set a goal to deliver informed recommendations of effective business models to improve the University’s overall positioning and competitiveness. To achieve this, the unit was equipped with strong capabilities in areas such as evidence reviews, environmental and horizon scanning, and state analysis. This helped to deliver outputs that extended beyond the scope of internal collected data to incorporate current best practice approaches and build upon the evidence from other institutions and sectors. In our experience, the addition of contextual intelligence informed and extended our analytics beyond the operational reporting, facilitated the delivery of actionable recommendations and supported rapid implementation and translation by the senior management.
Moreover, in our experience, the process of strategic analytics is not a linear process where a question is asked and an answer is provided. Rather, it starts from a high-level conversation between executives and data scientists about a strategy and a set of potential scenarios. 

The first step is primarily focused on analysing data through an iterative engagement process which allows the senior executive team to clarify their thinking and the strategic issue they are addressing, refine those scenarios and arrive at some early structured questions. 

Therefore, it is extremely important that the analytical techniques and team are agile, efficient and adaptable to the constantly evolving questions. A code-first approach delivered on RStudio’s professional products is a critical part of this sort of adaptable and agile approach. 

Strategic analytics teams need to be collaborative with decision-makers to arrive at an evidence-based strategic question that can be translated into a targeted in-depth data analysis project. Throughout this process, flexibility and reproducibility are critical components in the delivering of a methodologically robust, transparent and ultimately trusted strategic function. The technically advanced yet intuitive platform supported widespread uptake and adoption across the University was instrumental to achieving our transition from operational to strategic analytics.

--- 

## About Monash University
 
From a single campus at Clayton with fewer than 400 students, Monash has grown into a network of campuses, education centres and partnerships spanning the globe. With approximately 60,000 students (and 350,000 alumni) from over 170 countries, we are today Australia's largest university.
 
The University now offers a broad selection of courses within 10 faculties: Art, Design and Architecture; Arts; Business and Economic; Education; Engineering; Information Technology; Law; Medicine, Nursing and Health Sciences; Pharmacy and Pharmaceutical Sciences; and Science.
