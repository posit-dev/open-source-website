---
title: "AI in Production"
event_type: conference
location: "Newcastle Upon Tyne, UK"
start_date: 2026-06-04
end_date: 2026-06-05
image: ai-in-production-2026.jpeg
website: https://ai-in-production.jumpingrivers.com/
description: "The first Jumping Rivers AI in Production will delve into the world of AI and Machine Learning."
languages:
- R
people:
- George Stagg
- Neal Richardson
---

The first Jumping Rivers AI in Production conference will delve into the world of AI and Machine Learning.

George Stagg will present on "Effective Agents: A Builder's Guide to Working with AI".

Description: The gap between a working demo and a reliable agent is where most of the interesting engineering happens. In this talk, we'll build up a practical mental model for working with AI. I'll start with some perhaps surprising fundamentals, and then share some of our hard-won lessons from shipping agents in production.

LLM APIs behave differently from other services you might have worked with before. They're stateless at the network level, context is everything, and a lot of surprising behaviour only becomes obvious when you look at the raw traffic. They'll also lie to you: confidently reporting that a capability is working when it isn't, or finding creative workarounds to limitations you didn't intend to be optional. So, I'll go over the anatomy of an AI network request and show why proxying your own traffic is one of the most useful tools you can develop in this space.

From there, we'll move into the practical realities of building and deploying agents: how to think about context management, why caching deserves more attention than it often gets, and when abstractions help versus when they obscure what's actually happening. I'll share what we learned from agentic tools like Claude Code, covering the best way for agents to interact with the world, why multi-agent systems with limited scope and focused toolsets outperform monolithic agents, and what increasing autonomy and abstraction means for how we build and debug. I'll end with what we'd do differently if we were starting over.
