---
title: AI chatbots with shinychat
image: page-1.png
resource_type: cheatsheet
by: posit
date: '2026-08-01'
description: Build LLM-powered chatbot apps in R and Python Shiny using shinychat with ellmer providers, streaming output, tool displays, and slash commands.
download_url: shinychat.pdf
people:
- Mine Çetinkaya-Rundel
- Sara Altman
- Carson Sievert
thumbnails:
- page-1.png
- page-2.png
software:
- shinychat
languages:
- Python
source_files:
- file: shinychat.key
  format: Keynote
---

shinychat adds AI chatbot interfaces to Shiny apps in both R and Python. It integrates with ellmer for LLM provider connections and handles streaming, rich markdown rendering, and built-in conversation history automatically.

## What's covered
- Connect to LLM – `chat_anthropic()`, `chat_openai()`, `chat_google()`, and other ellmer providers
- Create a basic chatbot – `chat_ui()`, `chat_server()`, and `shinyApp()` wiring
- Quickly iterate – `live_browser()` for one-line chat app launch
- First impression – custom greetings and suggestion markup via `chat_ui(greeting=)`
- Layouts – screen-filling (`page_fillable()`), sidebar (`page_sidebar()`), and card layouts
- Built-in chat features – conversation history, attachments, cancel/edit, thinking display, rich streaming output
- Opt-in features – greetings, suggestions, slash commands
- Tool displays – automatic and customizable display of tool calls for transparency
- Slash commands – `chat$slash_command()` for shortcuts like clearing history
