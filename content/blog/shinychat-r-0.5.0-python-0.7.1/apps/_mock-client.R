# Mock ellmer client and canned-response helpers shared by the demo apps.
# Modeled on the echo client bundled with shinychat's own examples: no
# network calls are ever made.

suppressPackageStartupMessages({
  library(shiny)
  library(bslib)
  library(shinychat)
  library(ellmer)
  library(coro)
})

mock_client <- function(model = "shinychat-mock", name = "Mock") {
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

mock_record <- function(client, user_text, assistant) {
  contents <- if (is.character(assistant)) {
    list(ellmer::ContentText(assistant))
  } else {
    lapply(assistant, function(piece) {
      if (is.character(piece)) ellmer::ContentText(piece) else piece
    })
  }
  client$set_turns(c(
    client$get_turns(),
    list(
      ellmer::UserTurn(contents = list(ellmer::ContentText(user_text))),
      ellmer::AssistantTurn(contents = contents)
    )
  ))
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

# Converts ellmer content objects (tool requests/results, thinking, ...)
# into the blocks shinychat renders. `contents_shinychat()` is internal
# but stable across the converters shinychat itself uses for streams.
contents_shinychat <- function(content) {
  getFromNamespace("contents_shinychat", "shinychat")(content)
}

mock_tool_def <- function(
  name,
  description,
  title,
  arguments = list(),
  icon = NULL,
  grouping = NULL
) {
  ellmer::ToolDef(
    function(...) NULL,
    name = name,
    description = description,
    arguments = do.call(ellmer::type_object, arguments),
    annotations = list(title = title, icon = icon, grouping = grouping)
  )
}

mock_tool_request <- function(id, name, arguments, tool = NULL) {
  ellmer::ContentToolRequest(
    id = id,
    name = name,
    arguments = arguments,
    tool = tool
  )
}

mock_tool_result <- function(request, value, display = NULL, error = NULL) {
  extra <- if (!is.null(display)) list(display = display) else list()
  ellmer::ContentToolResult(
    value = value,
    error = error,
    request = request,
    extra = extra
  )
}

# Build the content list for a rich assistant message: markdown strings,
# ellmer content objects, and htmltools tags can be mixed. Pass the result
# to chat_append_message(id, list(role = "assistant", content = msg)).
mock_message <- function(...) {
  lapply(list(...), function(item) {
    if (inherits(item, "ellmer::Content")) contents_shinychat(item) else item
  })
}

mock_append_message <- function(
  id,
  contents,
  session = shiny::getDefaultReactiveDomain()
) {
  shinychat::chat_append_message(
    id,
    list(role = "assistant", content = contents),
    chunk = FALSE,
    session = session
  )
}

# Stream a rich reply through chat_append(): tool requests appear as running
# activity rows before their results land, plain text streams word by word,
# and asides (inline HTML citations) are yielded whole. `on_done` runs
# server-side after the last chunk, e.g. to open the artifact drawer.
mock_stream_reply <- function(
  id,
  contents,
  block_delay = 1,
  word_delay = 0.035,
  on_done = NULL,
  session = shiny::getDefaultReactiveDomain()
) {
  shinychat::chat_append(
    id,
    coro::async_generator(function() {
      for (block in contents) {
        if (inherits(block, "ellmer::ContentToolResult")) {
          yield(block@request)
          coro::await(coro::async_sleep(block_delay / 2))
          yield(block)
          coro::await(coro::async_sleep(block_delay / 2))
        } else if (is.character(block) && !startsWith(block, "<shiny-aside")) {
          for (piece in strsplit(block, "(?<=\\s)", perl = TRUE)[[1]]) {
            yield(piece)
            coro::await(coro::async_sleep(word_delay))
          }
          coro::await(coro::async_sleep(block_delay / 2))
        } else {
          yield(block)
        }
      }
      if (!is.null(on_done)) on_done()
    })(),
    session = session
  )
}

# When history is enabled, chat_append() saves the conversation after each
# response. Rich messages are appended with chat_append_message() instead,
# so trigger the same save hook manually.
mock_save_history <- function(id, session = shiny::getDefaultReactiveDomain()) {
  on_response <- getFromNamespace("chat_history_on_response", "shinychat")
  on_response(id, promises::promise_resolve(TRUE), session = session)
  invisible(NULL)
}
