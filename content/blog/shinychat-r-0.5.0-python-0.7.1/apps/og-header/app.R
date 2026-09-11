source("../_mock-client.R")

addResourcePath("assets", getwd())

greeting <- paste0(
  "<img src=\"assets/hex.svg\" width=\"104\" alt=\"shinychat hex sticker\">\n\n",
  "## Complete chat applications in shinychat\n\n",
  "Bringing history, greetings, suggestions, ",
  "citations, and tools together around the conversation.\n\n",
  "* <span class=\"suggestion\" title=\"shinychat for R\">New in v0.5.0</span>\n",
  "* <span class=\"suggestion\" title=\"shinychat for Python\">New in v0.7.1</span>\n"
)

greeting_css <- "
:root {
  --bs-body-bg: #E8EDF2;
  --bs-body-color: #294A62;
  --bs-secondary-color: #294a62c8;
}
.shiny-chat-greeting-content p {
  text-wrap: balance;
}
.shiny-chat-page-header { display: none; }
body,
shiny-chat-page,
.shiny-chat-page-body,
.shiny-chat-page-main,
.shiny-chat-page-panel {
  --shiny-chat-page-canvas-bg: #E8EDF2;
  --shiny-chat-page-surface-bg: #E8EDF2;
  background-color: #E8EDF2;
}
.shiny-chat-greeting { text-align: center; }
.shiny-chat-greeting-content img { margin: 0 auto 0.5rem; }
.shiny-chat-greeting-content .shiny-chat-suggestion-list { justify-content: center; }
.shiny-chat-greeting-content .shiny-chat-suggestion-list-item { text-align: left; }
shiny-chat-container .shiny-chat-suggestion-list .shiny-chat-suggestion-list-item {
  background-color: #f9fafb;
}
.form-control {
  background-color: #f9fafb;
}
"

ui <- page_chat(
  tags$style(HTML(greeting_css)),
  "shinychat",
  id = "chat",
  greeting = greeting,
  placeholder = "Ask about building chat apps with shinychat...",
  icon_assistant = FALSE
)

server <- function(input, output, session) {
  chat_server("chat", mock_client(), history = FALSE)

  observeEvent(input$chat_user_input, {
    text <- if (is.list(input$chat_user_input)) {
      input$chat_user_input[[1]]
    } else {
      input$chat_user_input
    }
    mock_respond(
      "chat",
      "This is a demo assistant running on canned responses. See the blog post for the real thing!"
    )
  })
}

shinyApp(ui, server)
