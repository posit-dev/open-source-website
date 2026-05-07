---
title: "AI Newsletter: A Data Cleaning Mode for Posit Assistant"
slug: ai-newsletter
date: 2026-05-08
people:
  - Sara Altman
  - Simon Couch
description: >
  The latest AI Newsletter, including a new data analysis feature for Posit Assistant and an open-source release supporting pre-trained models for tabular data.
image: "images/featured.png"
image-alt: "On the left-hand side, three robot icons representing Posit's AI assistants. On the right, hex sticker logos for Posit's AI-related open source packages including mall, mcptools, vitals, ragnar, ellmer, chatlas, shinychat, and gander."
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

## Posit news 

**The latest release of Posit Assistant includes a Data Cleaning Mode.** When Posit Assistant enters the mode, it spends time identifying and fixing data quality issues and preparing your data for analysis. When certain decisions (e.g., how to recode a variable) require user decisions, it surfaces those decisions in a specialized interface. When you and Posit Assistant are done making decisions about the cleaning process, all the cleaning code is written to a script.

![A screenshot of Posit Assistant in Data Cleaning Mode. The agent is asking the user a number of questions, presented as tabs, about data quality. The active question points out that the distribution of a variable in the data is very uneven and includes a table of row counts by the variable. The agent recommends keeping all rows, but runs this decision by the user first.](images/data-cleaning-mode.png)

Broadly, we've seen that many coding agents seem to have a superficial regard for data quality, focusing only on errors thrown by analysis code. This is one of several features we're iterating on to tailor the agent experience more closely to the real work of data science.

**The initial release of the tabpfn package [recently made it to CRAN](https://tidyverse.org/blog/2026/03/tabpfn-0-1-0/).** TabPFN is a pre-trained neural network for tabular data. In a typical predictive modeling workflow, you train a model on existing data (the training data), and then apply the resulting model to new, unseen data. TabPFN, in contrast, is a neural network pre-trained on a vast array of synthetic datasets. When using TabPFN, the model learns from the analyst's training data _in-context_, in a similar way that an LLM can 'learn' over the course of a conversation, allowing it to predict on new data without an explicit training step. The tabpfn package provides R tidymodels bindings to the pre-trained model.

## Terms

TabPFN and LLMs rely on **in-context learning** to provide more helpful responses.

Many recent model releases have announced increased **context windows** of 1 million tokens.^[A token is, roughly, a word.] The context window is the maximum length of the 'conversation history'. So, if you've had 10 messages back and forth with an LLM, and each message was composed of 100 tokens, the context length would be 1,000, well under the context window for most modern LLMs.

LLMs learn in a few different stages. The most recognizable stage is probably **pre-training,** in which the model gains general knowledge and capabilities by learning from massive collections of text. Another important stage of learning is **in-context learning,** which happens over the course of a conversation. For example, if you paste a document into an LLM chat and then start asking questions about it, the document has been learned in-context.

TabPFN follows this same learning setup as modern LLMs. The TabPFN team pre-trains the neural network and then allows users to download the resulting weights. Then, the model learns from the analysts' training data in-context.

## Learn more

* OpenAI released [GPT 5.5](https://openai.com/index/introducing-gpt-5-5/), an incremental improvement over GPT 5.4. Google Gemini released [Deep Research Max](https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/), an incremental improvement over its Deep Research tool.
* Yihui Xie [wrote up a thoughtful reflection on his experience with AI-assisted coding](https://yihui.org/en/2026/05/ai-reflections/).
* LLM use for open-source contributions can be controversial. [Zig](https://ziglang.org/) has instituted a [ban on LLM contributions](https://ziglang.org/code-of-conduct/). You can read their rationale [here](https://kristoff.it/blog/contributor-poker-and-ai/). 
