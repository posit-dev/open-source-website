---
title: "{{ replace .Name "-" " " | title }}"
date: {{ now.Format "2006-01-02" }}
people:
  - Your full name
description: >
  1-2 sentences shown in card listings and under the post hero. Also used for social previews.
image: "featured.png"
image-alt: ""
categories: # Delete what you don't need
  - Machine Learning
  - Artificial Intelligence
  - Visualization
  - Interactive Apps
  - Publishing
  - MLOps and Admin
  - Data Wrangling
  - Best Practices
  - Community
software: # Folder name from content/software/, e.g. ggplot2, quarto, great-tables
  -
languages: # Delete what you don't need
  - R
  - Python
tags: # Freeform; avoid duplicating software or categories values
  -
nohero: false
hidesubscription: false
# Uncomment to credit a stock photo:
# photo:
#   url: https://unsplash.com/photos/...
#   author: Photographer Name
---

<!--
TODO:
- [ ] Add image (1920×1080 PNG or JPG) and image-alt
- [ ] Trim categories, software, and languages to only what applies
- [ ] Open a PR against main for a Netlify preview
-->

Post content goes here.
