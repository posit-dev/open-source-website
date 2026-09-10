source("../_mock-client.R")

# The greeting the "model" writes: a variation of the penguin assistant
# greeting from greeting-suggestions. Text blocks stream word by word; the
# suggestion list items are yielded whole so the cards pop in as cards rather
# than as half-written HTML.
greeting_blocks <- c(
  "## Welcome to the penguins assistant!\n\n",
  paste0(
    "Hi! I'm ready to help you explore the penguins dataset. ",
    "What would you like to do?\n\n"
  ),
  "* <span class=\"suggestion submit\" title=\"Summarize my data\">Summarize the penguins dataset</span>\n",
  "* <span class=\"suggestion\" title=\"Create a plot\">Plot bill length by species</span>\n"
)

greeting_stream <- coro::async_generator(
  function(start_delay = 2, word_delay = 0.09, card_delay = 0.35) {
    coro::await(coro::async_sleep(start_delay))
    for (block in greeting_blocks) {
      if (grepl("<span", block, fixed = TRUE)) {
        coro::yield(block)
        coro::await(coro::async_sleep(card_delay))
      } else {
        pieces <- strsplit(block, "(?<=\\s)", perl = TRUE)[[1]]
        for (piece in pieces) {
          coro::yield(piece)
          coro::await(coro::async_sleep(word_delay))
        }
      }
    }
  }
)

ui <- page_chat(
  "Assistant",
  id = "chat",
  placeholder = "Ask about the penguins dataset..."
)

server <- function(input, output, session) {
  client <- mock_client(model = "penguin-assistant", name = "Penguin assistant")

  generate_greeting <- function(client) {
    chat_greeting(greeting_stream())
  }

  chat_server("chat", client, greeting = generate_greeting, history = FALSE)
}

shinyApp(ui, server)
