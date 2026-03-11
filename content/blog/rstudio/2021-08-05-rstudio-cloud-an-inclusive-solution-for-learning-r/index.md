---
title: 'RStudio Cloud: An inclusive solution for learning R'
people:
  - Dr. Patricia Menéndez
date: '2021-08-05'
slug: rstudio-cloud-an-inclusive-solution-for-learning-r
categories:
  - Education
  - RStudio Cloud
tags:
  - Use Cases
description: Learn how Monash University uses RStudio Cloud in their Introduction to Data Analysis and Collaborative & Reproducible Practices units. From weekly tutorials and assignments during the semester to even a timed test with 300 students logging in simultaneously.
blogcategories:
- Training and Education
alttext: clouds
events: blog
ported_from: rstudio
port_status: raw
---
<sup>Patricia’s own cloud photo from Antarctica</sup>  

<div class="lt-gray-box">
*This is a guest post from Dr. Patricia Menéndez, Department of Econometrics and Business Statistics at Monash University, Melbourne, Australia*  
</div>

In 2019 I was assigned the task to teach two code-focused units at Monash University:  

* **Introduction to Data Analysis:** delivered to an audience of both undergraduate and graduate students, with a class size of approximately 300 students.  
* **Collaborative and Reproducible Practices:** offered to students enrolled in the Master of Business Analytics at Monash University with an average of 65 students. 

When I started to develop the materials for the two units, I realised the large number of students and different operating systems they use in class would be a challenge to manage. I was familiar with these challenges from my experience working outside of academia with people from various backgrounds and different proficiency levels in R. With that in mind, I decided to trial RStudio Cloud in my classrooms and have been using it ever since.

The two units began just before the COVID-19 pandemic hit Australia. After the first two weeks of the semester, we went into a hard lock-down. With the prospect of teaching on campus eliminated, I could not have been happier with my decision to use RStudio Cloud.

#### Getting Started with RStudio Cloud at Monash

RStudio Cloud is a platform that allows you to use R within RStudio by just logging in to the system using your preferred browser. This was a benefit for our team at Monash because students did not need to install any software in their own machines. Administrators can simply create a space for the classroom and invite participants to join. It could not be easier. 

RStudio Cloud Roles at Monash:  

* *Administrator:* In our case, the head teaching assistant and myself were nominated as administrators of the space.  
* *Moderator:* Other teaching assistants were delegated the role of Moderator so they could view and access any students’ projects.
* *Contributor:* Students and tutors were contributors in the space, which also ensured that they could not change the original exercise.
* *Viewer:* I have not explored this option but this could be useful if you want to ensure that some users can only see the materials.

As an administrator of the RStudio Cloud spaces for my units, I had the capacity to:

* Create new spaces for the classrooms where the weekly RStudio projects and corresponding solutions were made available to students
* Decide which version of R to use
* Determine the visibility of each project
* Customise the specific resources required for each project (RAM and CPU memory allocations)
* Manage users 

With RStudio Cloud, projects can be uploaded directly from GitHub or a zip file containing an R project. At the beginning of the semester, all the R projects for the 12-weeks were uploaded onto the classroom space and made available in the cloud. The corresponding projects were made visible to the students only at the beginning of each week, while the solutions were made available at the end of the week. 

With the centralised capacity, I could keep myself informed of how the students interacted with R and RStudio in the cloud. This allowed the lecture and tutorials to run smoothly through the semester without hiccups. 

In addition to creating an RStudio Cloud space for both of the units, I created another RStudio Cloud space for my teaching teams. The ability to make the projects visible to other members within the space proved to be extremely useful as it provided administrators the capacity to trial and test each project before making it visible to the users.

During the implementation process, we worked closely to easily troubleshoot any issues before students encountered them. In this test space, the unit materials were uploaded so my teaching assistants could try the code and go over the solutions. This has worked perfectly by affording them the opportunity to test all the projects before conducting the tutorials. To further facilitate the interactions among members of the teaching teams, we also set up a Slack channel through which we were able to communicate at any time. 

Administrators and teaching assistants could also log in to students’ projects so that we could promptly help students with any issues. To support any further technical issues, we set up a few Zoom meetings for students to join. Technical issues were resolved by us logging into their project as the administrator and rectifying the issues.

> The versatility of RStudio Cloud is simply amazing. I used RStudio Cloud for weekly tutorials and assignments during the semester and have even run a timed test with 300 students logging in simultaneously.

For the test, students were given access to an RStudio Cloud project which contained data and an RMarkdown file with questions for which they needed to create code to answer. The exercise was made visible to the students in the course space where they could be timed while working on it.  Students were required to download their RStudio Cloud project, which could be done easily in RStudio Cloud and upload it to the learning management systems as an assignment.

For the Introduction to Data Analysis, RStudio Cloud eliminated any potential challenges with software installation. Students with varying levels of coding knowledge can work under the same setup in the online environment, ensuring a smooth semester.

The Collaborative & Reproducible Practices unit focused primarily on reproducible reporting using RMarkdown, the use of Git via the command line terminal and GitHub as a remote repository. In this unit, we used RStudio Cloud for the first four weeks of the semester and then moved on to using R and RStudio local installations. RStudio Cloud allowed me to quickly give students instructions on installing in their local machines and was instrumental for getting students off the ground running with RMarkdown, git and GitHub.

<img style="float:left;margin:0 10px 10px 0;" src="patricia.jpg" alt = "Dr. Patricia Menéndez" width = 25%> The experience using RStudio Cloud in my units over the last two years has been truly wonderful. I would like to express appreciation to RStudio for their support and gratitude to my teaching team for enthusiastically jumping in the boat with me and providing input throughout the semesters. Last but not least, thank you to all the students whose feedback and input help make these units better each year! If you have any questions, feel free to reach out on Twitter! @PM_maths 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


> #### Helpful resources:  

>* <a href="https://www.rstudio.com/resources/webinars/teaching-r-online-with-rstudio-cloud/?_ga=2.169953248.1183963645.1628082102-748609636.1627930340" target = "_blank">Teaching R Online with RStudio Cloud Webinar</a>
>* <a href="https://rstudio.cloud/learn/guide" target="_blank">RStudio Cloud Guide - Getting Started</a>
>* Webinar for Instructors Getting Started with RStudio Cloud, <a href="https://www.youtube.com/channel/UC3xfbCMLCw1Hh4dWop3XtHg/videos" target="_blank">YouTube Premiere on August 18th at 1 pm ET</a>

