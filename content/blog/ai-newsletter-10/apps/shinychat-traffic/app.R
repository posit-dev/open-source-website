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

tool_defs <- list(
  site_traffic_trend = mock_tool_def(
    name = "site_traffic_trend",
    description = "Run the reviewed site traffic trend calculation",
    title = "Calculating site traffic trend",
    arguments = list(period = ellmer::type_string("Reporting period"))
  ),
  search_context = mock_tool_def(
    name = "search_context",
    description = "Search internal analytics documentation",
    title = "Searching analytics documentation",
    arguments = list(query = ellmer::type_string("Search query")),
    grouping = "all"
  ),
  query_warehouse = mock_tool_def(
    name = "query_warehouse",
    description = "Query daily web analytics tables",
    title = "Querying the analytics warehouse",
    arguments = list(query = ellmer::type_string("Warehouse query")),
    grouping = "all"
  )
)

traffic_reply <- list(
  contents = list(
    mock_tool_result(
      mock_tool_request(
        "call-traffic-1",
        "site_traffic_trend",
        list(period = "latest 90 days"),
        tool_defs$site_traffic_trend
      ),
      "Average daily site visits increased 22%",
      display = shinychat::tool_result_display(
        title = "Calculated site traffic trend",
        label = "latest 90 days",
        value_preview = "Visits increased 22%"
      )
    ),
    paste0(
      "Daily site visits **increased 22%** over the latest 90 days, comparing ",
      "the average of the first and most recent 14-day periods."
    )
  )
)

source_reply <- list(
  contents = list(
    mock_tool_result(
      mock_tool_request(
        "call-context-1",
        "search_context",
        list(query = "canonical source for site traffic"),
        tool_defs$search_context
      ),
      paste(
        "sessions_daily is the canonical source for site traffic.",
        "It is the reviewed daily sessions metric used in reporting."
      ),
      display = shinychat::tool_result_display(
        title = "Searched analytics documentation",
        label = "canonical source for site traffic",
        value_preview = "1 relevant document"
      )
    ),
    mock_tool_result(
      mock_tool_request(
        "call-query-1",
        "query_warehouse",
        list(query = "preview sessions_daily"),
        tool_defs$query_warehouse
      ),
      "5 rows returned from sessions_daily",
      display = shinychat::tool_result_display(
        title = "Queried analytics warehouse",
        label = "preview sessions_daily",
        value_preview = "5 rows"
      )
    ),
    "Use **`sessions_daily` as the canonical source for site traffic**",
    aside(
      "Internal analytics guidance",
      "https://docs.example/site-traffic",
      "sessions_daily as the canonical source for site traffic",
      paste0(
        "`sessions_daily` is the canonical source for site traffic. It has one row ",
        "per day, and `visits` is the reviewed daily sessions metric used in reporting."
      )
    ),
    ". It has one row per day and provides the reviewed daily sessions metric used for reporting."
  )
)

busiest_reply <- list(
  contents = list(
    mock_tool_result(
      mock_tool_request(
        "call-busiest-1",
        "query_warehouse",
        list(query = "date with maximum visits"),
        tool_defs$query_warehouse
      ),
      "2026-08-29: 51,842 visits",
      display = shinychat::tool_result_display(
        title = "Queried analytics warehouse",
        label = "date with maximum visits",
        value_preview = "1 row"
      )
    ),
    "**August 29 had the most site visits, with 51,842 visits.**"
  )
)

fallback_reply <- list(
  contents = list(
    paste0(
      "I can answer questions about site visits, traffic data sources, and recent ",
      "traffic trends."
    )
  )
)

reply_for <- function(text) {
  text <- tolower(text)
  if (grepl("source|table|sessions", text)) {
    source_reply
  } else if (grepl("most|busiest|maximum", text)) {
    busiest_reply
  } else if (grepl("trend|traffic|visit", text)) {
    traffic_reply
  } else {
    fallback_reply
  }
}

greeting_md <- paste0(
  "## Site traffic assistant\n\n",
  "Ask a question about recent web analytics:\n\n",
  "* <span class=\"suggestion submit\">How is traffic trending for our site?</span>\n",
  "* <span class=\"suggestion\">Which table should I use for site traffic?</span>\n",
  "* <span class=\"suggestion\">Which day had the most site visits?</span>\n"
)

ui <- page_chat(
  "Site traffic assistant",
  id = "chat",
  icon = bsicons::bs_icon("graph-up-arrow"),
  sidebar = chat_sidebar(history = TRUE, open = FALSE),
  greeting = greeting_md,
  placeholder = "Ask about site traffic...",
  icon_assistant = FALSE
)

server <- function(input, output, session) {
  client <- mock_client(model = "traffic-assistant", name = "Traffic assistant")
  chat_enable_history(
    "chat",
    client,
    options = history_options(
      store = "memory",
      title = \(turns) turns[[1]]$content[[1]]
    )
  )

  observeEvent(input$chat_history_new, {
    chat_clear("chat", greeting = TRUE)
  })
  observeEvent(input$chat_greeting_requested, {
    chat_set_greeting("chat", greeting_md)
  })

  observeEvent(input$chat_user_input, {
    text <- if (is.list(input$chat_user_input)) {
      input$chat_user_input[[1]]
    } else {
      input$chat_user_input
    }
    reply <- reply_for(text)
    mock_record(client, text, reply$contents)
    mock_stream_reply(
      "chat",
      reply$contents,
      block_delay = 0,
      word_delay = 0
    )
  })
}

shinyApp(ui, server)
