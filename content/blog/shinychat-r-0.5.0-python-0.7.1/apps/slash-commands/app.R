source("../_mock-client.R")

ui <- page_chat(
  "Assistant",
  id = "chat",
  placeholder = "Ask a question..."
)

server <- function(input, output, session) {
  client <- mock_client()
  chat <- chat_server("chat", client, history = FALSE)

  chat$slash_command("help", "Show what this assistant can do", function() {
    chat$append(
      paste0(
        "Here's what I can help with:\n\n",
        "- **/search topic** -- search the documentation and send a richer prompt\n",
        "- **/clear** -- clear the conversation without calling the model\n",
        "- **/help** -- show this guidance again"
      ),
      role = "assistant"
    )
  }, echo = FALSE)

  chat$slash_command("search", "Search the documentation", function(content) {
    chat$append(
      paste0(
        "Searching the documentation for **", content$user_text, "**...\n\n",
        "Found 3 relevant pages. I'll include summaries from each in my next response."
      ),
      role = "assistant"
    )
  }, echo = TRUE)

  chat$slash_command("clear", "Clear the conversation", function() {
    chat$clear()
  }, echo = FALSE)
}

shinyApp(ui, server)
