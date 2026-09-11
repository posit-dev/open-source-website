source("../_mock-client.R")

replies <- list(
  mountain_africa = paste0(
    "**Mount Kilimanjaro** is the tallest mountain in Africa, at 5,895 meters (19,341 ft) ",
    "above sea level. It's a free-standing volcanic massif in Tanzania."
  ),
  pivot_r = paste0(
    "To make data longer in R, use `tidyr::pivot_longer()`:\n\n",
    "``` r\n",
    "tidyr::pivot_longer(df, cols = -id, names_to = \"key\", values_to = \"value\")\n",
    "```\n\n",
    "Give it the columns to stack and names for the new key and value columns."
  ),
  recycling = paste0(
    "In R, **vector recycling** repeats a shorter vector when it's combined with a longer one. ",
    "If the lengths aren't multiples, R warns and still recycles. Prefer `vctrs::vec_recycle()` ",
    "when you need explicit control."
  ),
  fallback = "I'm a demo assistant running on canned responses."
)

reply_for <- function(text) {
  text <- tolower(text)
  if (grepl("mountain", text)) {
    replies$mountain_africa
  } else if (grepl("pivot|longer", text)) {
    replies$pivot_r
  } else if (grepl("recycl", text)) {
    replies$recycling
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
