source("../_mock-client.R")

greeting <- paste0(
  "## Welcome to the penguins assistant!\n\n",
  "What would you like to do?\n\n",
  "* <span class=\"suggestion submit\" title=\"Summarize my data\">Get a quick summary of the penguins dataset</span>\n",
  "* <span class=\"suggestion\" title=\"Create a plot\">Plot bill length by species</span>\n",
  "* <span class=\"suggestion\" title=\"Explain this code\">Explain what my R script does</span>\n"
)

replies <- list(
  summarize = paste0(
    "Here's a quick summary of the **palmerpenguins** dataset:\n\n",
    "| Species | N | Mean bill length (mm) |\n",
    "|---|---|---|\n",
    "| Adelie | 152 | 38.8 |\n",
    "| Chinstrap | 68 | 48.8 |\n",
    "| Gentoo | 124 | 47.6 |\n\n",
    "Ask me to summarize a subset, or say \"Create a plot\" to see the distribution."
  ),
  plot = paste0(
    "Here's what I can tell you about **bill length by species**:\n\n",
    "- *Gentoo* penguins have the longest bills on average (47.6 mm).\n",
    "- *Adelie* penguins have the shortest (38.8 mm).\n\n",
    "Say **Create a plot** again and I'll draw a box plot of the distribution."
  ),
  explain = paste0(
    "Paste your script in a message (or attach it with the paperclip) and I'll ",
    "walk through it block by block."
  ),
  fallback = "I'm a demo assistant running on canned responses -- try one of the suggestions!"
)

reply_for <- function(text) {
  text <- tolower(text)
  if (grepl("summar", text)) {
    replies$summarize
  } else if (grepl("plot|bill", text)) {
    replies$plot
  } else if (grepl("explain", text)) {
    replies$explain
  } else {
    replies$fallback
  }
}

ui <- page_chat(
  "Assistant",
  id = "chat",
  greeting = greeting,
  placeholder = "Ask about the penguins dataset...",
  allow_attachments = TRUE
)

server <- function(input, output, session) {
  chat_server("chat", mock_client(), history = FALSE)

  observeEvent(input$chat_user_input, {
    text <- if (is.list(input$chat_user_input)) {
      input$chat_user_input[[1]]
    } else {
      input$chat_user_input
    }
    mock_respond("chat", reply_for(text))
  })
}

shinyApp(ui, server)
