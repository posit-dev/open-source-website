source("../_mock-client.R")

Sys.setenv(SHINYCHAT_ASIDE_FAVICON = "false")

aside <- function(label, url, span, ...) {
  sprintf(
    '<shiny-aside label="%s" url="%s" grounded-span="%s">%s</shiny-aside>',
    label,
    url,
    span,
    paste0(...)
  )
}

reply <- mock_message(
  paste0(
    "The training report recommends **a smaller batch size** for the next run ",
    aside(
      "Internal report",
      "https://intranet.example/reports/training",
      "a smaller batch size",
      "The report recommends reducing the batch size from 256 to 64 after observing ",
      "unstable gradients late in training."
    ),
    ", and suggests **freezing the embedding layer** for the first two epochs ",
    aside(
      "Experiment log",
      "https://wiki.example/experiments/run-42",
      "freezing the embedding layer",
      "Run 42 froze the embedding layer for two epochs, which reduced warm-up loss ",
      "by 12% compared to the baseline."
    ),
    "."
  )
)

ui <- page_chat(
  "Assistant",
  id = "chat",
  placeholder = "Ask about the training report..."
)

server <- function(input, output, session) {
  chat_server("chat", mock_client(), history = FALSE)

  observeEvent(input$chat_user_input, {
    text <- if (is.list(input$chat_user_input)) input$chat_user_input[[1]] else input$chat_user_input
    mock_append_message("chat", reply)
  })
}

shinyApp(ui, server)
