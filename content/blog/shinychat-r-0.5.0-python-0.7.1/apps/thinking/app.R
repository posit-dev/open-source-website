source("../_mock-client.R")

thinking_text <- paste0(
  "The user is asking about penguin body mass. I should compare the three ",
  "commonly studied species, note that Gentoos are the heaviest on average, ",
  "and mention that males outweigh females."
)

answer_text <- paste0(
  "Gentoo penguins are the heaviest of the three species commonly found on ",
  "the Antarctic Peninsula, averaging **5.5 kg**. Chinstrap penguins average ",
  "**4.6 kg**, and Adelie penguins average **4.3 kg**. Within each species, ",
  "males typically weigh 10--20% more than females."
)

ui <- page_chat(
  "Assistant",
  id = "chat",
  placeholder = "Ask a question...",
  enable_cancel = TRUE
)

thinking_stream <- coro::async_generator(function() {
  pieces <- strsplit(thinking_text, "(?<=\\s)", perl = TRUE)[[1]]
  n <- length(pieces)
  group <- ceiling(n / 20)
  for (i in seq(1, n, by = group)) {
    yield(structure(
      paste(pieces[i:min(i + group - 1, n)], collapse = ""),
      class = "shinychat_thinking"
    ))
    await(coro::async_sleep(0.25))
  }
  answer_pieces <- strsplit(answer_text, "(?<=\\s)", perl = TRUE)[[1]]
  for (piece in answer_pieces) {
    yield(piece)
    await(coro::async_sleep(0.05))
  }
})

server <- function(input, output, session) {
  chat_server("chat", mock_client(), history = FALSE)

  observeEvent(input$chat_user_input, {
    chat_append("chat", thinking_stream())
  })
}

shinyApp(ui, server)
