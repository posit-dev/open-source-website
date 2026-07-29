---
title: "AI Newsletter: EDA log in Posit Assistant"
slug: ai-newsletter
date: 2026-07-28
people:
  - Sara Altman
  - Simon Couch
description: >
  TODO: 1–2 sentence description.
image: "images/hero.png"
image-alt: "TODO: describe the hero image."
topics:
  - Artificial Intelligence
software: []
languages: []
tags:
  - ai-newsletter
source: []
nohero: false
hidesubscription: false
---

## EDA log for Posit Assistant 

The latest version of Posit Assistant in Positron includes an EDA log feature to help you keep track of exploratory analysis done with the agent.

![TODO: alt text describing the EDA log](images/eda-log.png)

The log summarizes findings for different areas of exploration and keeps track of next steps. To use the log, run the `/eda-log` slash command after you've started the EDA process. 

<script src="https://fast.wistia.com/player.js" async></script>
<script src="https://fast.wistia.com/embed/bu9ch5gqvx.js" async type="module"></script>
<style>wistia-player[media-id='bu9ch5gqvx']:not(:defined) { background: center / contain no-repeat url('https://fast.wistia.com/embed/medias/bu9ch5gqvx/swatch'); display: block; filter: blur(5px); padding-top:60.42%; }</style>

<wistia-player media-id="bu9ch5gqvx" aspect="1.6551724137931034"></wistia-player>

### Why we made this

Exploratory data analysis, the open-ended orientation to your data that often comes before anything else, can be a branching, nonlinear process. There are many questions you can ask your data, and, until coding agents, you were limited to how fast you could write code and understand that output when asking questions of your data. Because of this, it is often hard to keep track of what you've looked into, where that code is, and what you want to capture next. 

Data analysis agents like Posit Assistant can carry out EDA with lightning speed, which enables them to push the exploratory process deeper and more quickly than humans can alone. This is great in terms of terrain covered, but can make it difficult for users to follow and keep track of what has been done. This introduces a new problem: the purpose of EDA is typically for you, the human, to learn about your data. But coding agents can quickly outpace humans, producing so much analysis that it is difficult for the human to catch up. 

Posit Assistant already has various features that tackle this problem, including an exploratory mode of interaction where it runs shorter turns and stops more frequently to involve the user.  

The log is a lightweight tool to help users interact with data analysis agents better and improve the process and your own understanding of the data and the exploratory process. 

### Details

* When you run `/eda-log`, Posit Assistant will create a log for the exploration done in the conversation so far. The log then opens in the editor area in Positron. 
* The underlying logs are stored as YAML files in `.posit/assistant/eda-logs/`, next to where plans are stored.
* Posit Assistant is instructed to loosely keep the log up to date as the conversation progresses, but you can also manually trigger an update at any time with the "Refresh" button. 
* Clicking the arrow next to a topic will scroll you back to the spot in the conversation that the insight originated in, so you can look at the source code. 
* Suggestions from the conversation render as clickable next steps in the log. 
* The creation of an EDA log is always user-triggered. Posit Assistant will never create one on its own.

## External news


