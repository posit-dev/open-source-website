# Mock ellmer client and canned-response helpers for the og-header demo.
# Modeled on the shinychat post's apps/_mock-client.R: no network calls are
# ever made.

suppressPackageStartupMessages({
  library(shiny)
  library(bslib)
  library(shinychat)
  library(ellmer)
  library(coro)
})

mock_client <- function(model = "querychat-mock", name = "Mock") {
  stored_turns <- list()
  client <- list(
    get_turns = function() stored_turns,
    set_turns = function(value) {
      stored_turns <<- value
      invisible(client)
    },
    get_system_prompt = function() NULL,
    get_tools = function() list(),
    get_provider = function() {
      ellmer::Provider(
        name = name,
        base_url = "http://127.0.0.1:1",
        model = model
      )
    },
    get_model = function() model,
    clone = function() mock_client(model = model, name = name)
  )
  class(client) <- c("Chat", "R6")
  client
}

mock_stream <- coro::async_generator(function(text, delay = 0.04) {
  pieces <- strsplit(text, "(?<=\\s)", perl = TRUE)[[1]]
  for (piece in pieces) {
    coro::yield(piece)
    if (delay > 0) coro::await(coro::async_sleep(delay))
  }
})

# A streaming reply that never touches a model
mock_respond <- function(
  id,
  text,
  delay = 0.04,
  session = shiny::getDefaultReactiveDomain()
) {
  shinychat::chat_append(
    id,
    mock_stream(text, delay = delay),
    session = session
  )
}
