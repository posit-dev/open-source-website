---
title: "AI Newsletter: EDA log in Posit Assistant"
slug: ai-newsletter
date: 2026-07-31
people:
  - Sara Altman
  - Simon Couch
description: >
  A new EDA log feature for Posit Assistant. 
image: "images/hero-4.png"
image-alt: "Screenshot of Positron. On the left, the Posit Assistant panel shows R ggplot2 code, a bar chart titled 'Top 20 states by number of Spanish speakers' led by California, Texas, and Florida, a written summary of the findings, and suggested follow-up questions. On the right, the EDA Log opens in an editor tab titled 'ACS language speakers': a table with Area, Status, and Notes columns lists four areas—'Dataset structure & quality', 'Top languages nationwide', and 'Spanish speakers by state' marked Explored, and 'Language coverage across states' marked Partial—each with bullet-point findings, followed by a 'Next steps' section of suggested directions."
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

<div class="callout callout-note" role="note" aria-label="Note">
<div class="callout-body">

**Subscribe to the AI Newsletter!** 

The AI newsletter is now published as an RSS feed. Follow it in your favorite reader: 

<a href="/tags/ai-newsletter/index.xml" target="_blank" rel="noopener noreferrer" class="btn-shortcode inline-flex mb-5 mr-5 items-center px-4 py-3 text-sm leading-5 gap-2 rounded-lg bg-blue-400 text-white font-semibold align-middle hover:bg-blue-500 transition no-underline">Subscribe via RSS</a>

**Want the newsletter as an email?** Paste the feed URL — <https://opensource.posit.co/tags/ai-newsletter/index.xml> — into a free RSS-to-email service such as [Blogtrottr](https://blogtrottr.com/), [Feedrabbit](https://feedrabbit.com/), or [Follow.it](https://follow.it/), and each new issue will arrive in your inbox.

</div>
</div>

## EDA log for Posit Assistant 

The latest version of [Posit Assistant](https://assistant.posit.co/) in Positron includes an EDA log feature to help you keep track of exploratory analysis done with the agent.

![Screenshot of Positron. On the left, Posit Assistant has analyzed a dataset of U.S. language speakers, showing a bar chart and written findings. On the right, the EDA Log opens in an editor tab titled "ACS language speakers": a table with Area, Status, and Notes columns lists three areas—"Dataset structure & quality" and "Top languages nationwide" marked Explored, and "Language coverage across states" marked Partial—each with bullet-point findings and an arrow that links back to the conversation, followed by a "Next steps" section of suggested directions.](images/eda-log-zoom.png)

The log summarizes findings for different areas of exploration and keeps track of next steps. To use the log, run the `/eda-log` slash command after you've started the EDA process. 

### Why we made this

Exploratory data analysis, the open-ended orientation to your data that often comes before anything else, can be a branching, nonlinear process. There are many questions you can ask of your data, and new areas of inquiry can open with each question you ask. Because of this, it is often hard to keep track of what you've looked into, where that code lives, and what you want to explore next. 

Historically, the EDA process was limited by how quickly you could write code and interpret the output. Coding agents like Posit Assistant lift the first of those constraints. They can carry out EDA far faster than you can on your own, which can exacerbate the issue of keeping track of what you've explored. 

This speed also introduces a new problem: the point of EDA is typically for you, the human, to understand your data, but coding agents can produce output faster than you can absorb it. If the agent completes an analysis but you haven't understood the insights in the data, the exploration process hasn't really happened. 

Posit Assistant already has various features that tackle this problem, including an exploratory mode of interaction where it runs shorter turns and stops more frequently to involve the user. 

The EDA log is another lightweight tool for the same goal. It keeps a running summary of what you and Posit Assistant have explored, helping your understanding keep pace with the agent's and giving you a clearer picture of what's already been done.

### Details

<script src="https://fast.wistia.com/player.js" async></script>
<script src="https://fast.wistia.com/embed/bu9ch5gqvx.js" async type="module"></script>
<style>wistia-player[media-id='bu9ch5gqvx']:not(:defined) { background: center / contain no-repeat url('https://fast.wistia.com/embed/medias/bu9ch5gqvx/swatch'); display: block; filter: blur(5px); padding-top:60.42%; }</style>

<wistia-player media-id="bu9ch5gqvx" aspect="1.6551724137931034"></wistia-player>

* When you run `/eda-log`, Posit Assistant will create a log for the exploration done in the conversation so far. The log then opens in the editor area in Positron. 
* The underlying logs are stored as YAML files in `.posit/assistant/eda-logs/`, next to where plans are stored.
* Posit Assistant is instructed to loosely keep the log up to date as the conversation progresses, but you can also manually trigger an update at any time with the "Refresh" button. 
* Clicking the arrow next to an area scrolls you back to the spot in the conversation where that insight originated, so you can revisit the code and context that produced it.
* Suggested next steps appear as clickable text. Clicking one sends it to Posit Assistant as your next message.
* The creation of an EDA log is always user-triggered. Posit Assistant will never create one on its own.
* The feature is currently only in Positron, but will come to RStudio soon. 

## Recent past newsletters

* [Which models are best at spotting data quality problems?](/blog/2026-07-17_ai-newsletter/)
* [How to choose between AGENTS.md, skills, and MCP servers](/blog/2026-07-03_ai-newsletter/)

<br>
<br>

<a href="/tags/ai-newsletter/index.xml" target="_blank" rel="noopener noreferrer" class="btn-shortcode inline-flex mb-5 mr-5 items-center px-4 py-3 text-sm leading-5 gap-2 rounded-lg bg-blue-400 text-white font-semibold align-middle hover:bg-blue-500 transition no-underline">Subscribe via RSS</a>


