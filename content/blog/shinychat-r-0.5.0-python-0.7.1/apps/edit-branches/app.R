source("../_mock-client.R")

replies <- list(
  africa = paste0(
    "**Mount Kilimanjaro** is the tallest mountain in Africa, at 5,895 meters (19,341 ft) ",
    "above sea level. It's a free-standing volcanic massif in Tanzania."
  ),
  south_america = paste0(
    "**Aconcagua** is the tallest mountain in South America, at 6,961 meters (22,838 ft) ",
    "above sea level. It's the highest peak anywhere outside Asia."
  ),
  asia = paste0(
    "**Mount Everest** is the tallest mountain in Asia -- and the world -- at 8,849 meters ",
    "(29,032 ft) above sea level, on the border between Nepal and China."
  ),
  fallback = "I'm a demo assistant running on canned responses."
)

reply_for <- function(text) {
  text <- tolower(text)
  if (grepl("africa", text)) {
    replies$africa
  } else if (grepl("asia", text)) {
    replies$asia
  } else if (grepl("south america", text)) {
    replies$south_america
  } else {
    replies$fallback
  }
}

ui <- page_chat(
  "Assistant",
  id = "chat",
  placeholder = "Ask a question..."
)

server <- function(input, output, session) {
  client <- mock_client()
  chat_enable_history(
    "chat",
    client,
    options = history_options(
      store = "memory",
      title = function(recorded_turns) {
        first <- Filter(function(t) t$role == "user", recorded_turns)
        if (!length(first)) return("New conversation")
        txt <- first[[1]]$content
        if (is.list(txt)) txt <- txt[[1]]
        if (nchar(txt) > 30) txt <- paste0(substr(txt, 1, 30), "...")
        txt
      }
    )
  )

  observeEvent(input$chat_user_input, {
    text <- if (is.list(input$chat_user_input)) input$chat_user_input[[1]] else input$chat_user_input
    mock_respond("chat", reply_for(text))
    mock_record(client, text, reply_for(text))
    mock_save_history("chat")
  })
}

shinyApp(ui, server)
