source("../_mock-client.R")

tool_defs <- list(
  run_sql = mock_tool_def(
    name = "run_sql",
    description = "Run a read-only SQL query against the sales warehouse",
    title = "Running SQL query",
    arguments = list(query = ellmer::type_string("The SQL query to run"))
  ),
  read_schema = mock_tool_def(
    name = "read_schema",
    description = "Read the schema of a table in the sales warehouse",
    title = "Reading table schema",
    arguments = list(table = ellmer::type_string("Table name"))
  )
)

reply <- mock_message(
  mock_tool_result(
    mock_tool_request(
      "call-sql-1",
      "run_sql",
      list(query = "SELECT region, SUM(amount) FROM sales_2026 GROUP BY region"),
      tool_defs$run_sql
    ),
    "region,total\nEast,412300\nWest,387150\nNorth,298400\nSouth,275900\nCentral,220050",
    display = shinychat::tool_result_display(
      title = "Run SQL query",
      label = "SELECT region, SUM(amount) FROM sales_2026...",
      value_preview = "5 rows"
    )
  ),
  mock_tool_result(
    mock_tool_request(
      "call-sql-2",
      "run_sql",
      list(query = "SELECT COUNT(*) FROM orders WHERE quarter = 'Q2'"),
      tool_defs$run_sql
    ),
    "1834",
    display = shinychat::tool_result_display(
      title = "Run SQL query",
      label = "SELECT COUNT(*) FROM orders WHERE...",
      value_preview = "1,834"
    )
  ),
  mock_tool_result(
    mock_tool_request(
      "call-schema-1",
      "read_schema",
      list(table = "sales_2026"),
      tool_defs$read_schema
    ),
    "order_id TEXT, region TEXT, amount NUMERIC, quarter TEXT, ...",
    display = shinychat::tool_result_display(
      title = "Read table schema",
      label = "sales_2026",
      value_preview = "8 columns"
    )
  ),
  paste0(
    "Here's the regional picture for 2026 so far:\n\n",
    "| Region | Sales |\n|---|---|\n| East | $412,300 |\n| West | $387,150 |\n",
    "| North | $298,400 |\n| South | $275,900 |\n| Central | $220,050 |\n\n",
    "The **East** region leads, and there are **1,834 orders** in Q2. ",
    "Want me to break any region down by product line?"
  )
)

ui <- page_chat(
  "Sales assistant",
  id = "chat",
  placeholder = "Ask about the sales warehouse..."
)

server <- function(input, output, session) {
  chat_server("chat", mock_client(), history = FALSE)

  observeEvent(input$chat_user_input, {
    text <- if (is.list(input$chat_user_input)) input$chat_user_input[[1]] else input$chat_user_input
    mock_append_message("chat", reply)
  })
}

shinyApp(ui, server)
