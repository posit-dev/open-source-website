source("../_mock-client.R")

Sys.setenv(SHINYCHAT_ASIDE_FAVICON = "false")

`%||%` <- function(a, b) if (is.null(a)) b else a

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
  query_observations = mock_tool_def(
    name = "query_observations",
    description = "Query the survey observation database",
    title = "Querying survey observations",
    arguments = list(query = ellmer::type_string("The observation query")),
    grouping = "all"
  ),
  read_notebook = mock_tool_def(
    name = "read_notebook",
    description = "Read an entry from the field notebook",
    title = "Reading the field notebook",
    arguments = list(path = ellmer::type_string("Notebook path")),
    grouping = "all"
  )
)

counts_reply <- list(
  contents = list(
    mock_tool_result(
      mock_tool_request(
        "call-obs-1",
        "query_observations",
        list(query = "adelie pair counts by month"),
        tool_defs$query_observations
      ),
      "412 rows returned",
      display = shinychat::tool_result_display(
        title = "Queried survey observations",
        label = "adelie pair counts by month",
        value_preview = "412 rows"
      )
    ),
    mock_tool_result(
      mock_tool_request(
        "call-obs-2",
        "read_notebook",
        list(path = "notes/may-survey.md"),
        tool_defs$read_notebook
      ),
      "# May survey\n\nCalm seas. Counted 118 active nests at the north colony...",
      display = shinychat::tool_result_display(
        title = "Read field notebook",
        label = "notes/may-survey.md",
        value_preview = "18 entries"
      )
    ),
    "Across the season, Adelie pair counts at Cape Crozier **peaked in May at 118 active nests**",
    aside(
      "Survey observations",
      "https://data.example/penguins/cape-crozier",
      "peaked in May at 118 active nests",
      "Monthly survey counts, 2026 season. The May count reflects the height of incubation."
    ),
    ", before declining through June. Field notes attribute the June drop to two storm events that flooded low-lying nests",
    aside(
      "Field notebook",
      "https://notes.example/may-survey",
      "flooded low-lying nests",
      "From `notes/may-survey.md`: *Calm seas. Counted 118 active nests at the north colony.*",
      "\n\nThe June entry records standing water across the terrace after the June 8 storm."
    ),
    "."
  )
)

compare_reply <- list(
  contents = list(
    mock_tool_result(
      mock_tool_request(
        "call-obs-3",
        "query_observations",
        list(query = "pairs per colony, 2026 season"),
        tool_defs$query_observations
      ),
      "3 colonies, 223 pairs total",
      display = shinychat::tool_result_display(
        title = "Queried survey observations",
        label = "pairs per colony, 2026 season",
        value_preview = "3 colonies"
      )
    ),
    "The **north colony at Cape Crozier is the largest with 118 active pairs**",
    aside(
      "Survey observations",
      "https://data.example/penguins/colonies",
      "largest with 118 active pairs",
      "Colony totals for the 2026 season, all three occupied colonies."
    ),
    ", followed by **64 pairs at Cape Bird** and **41 at Cape Royds**.",
    "\n\nCape Royds has declined for three seasons in a row; the field notebook links the drop to storm flooding in consecutive Junes."
  ),
  drawer_title = "Colony comparison"
)

fallback_reply <- list(
  contents = list(
    paste0(
      "I'm the research assistant demo. Ask me about the penguin survey data ",
      "and I'll query the observation database and the field notebook for you."
    )
  )
)

reply_for <- function(text) {
  text <- tolower(text)
  if (grepl("count|survey|observ|season", text)) {
    counts_reply
  } else if (grepl("coloni|compare", text)) {
    compare_reply
  } else {
    fallback_reply
  }
}

# A small static plot for the artifact drawer
plot_file <- file.path(tempdir(), "colony-counts.png")
grDevices::png(plot_file, width = 720, height = 480, res = 110)
par(mar = c(4.5, 4, 2, 1))
colonies <- c("Cape Crozier", "Cape Bird", "Cape Royds")
pairs_counted <- c(118, 64, 41)
barplot(
  pairs_counted,
  names.arg = colonies,
  col = "#447099",
  border = NA,
  ylim = c(0, 130),
  ylab = "Adelie pairs counted",
  main = "Adelie pairs by colony, 2026 season"
)
grDevices::dev.off()
addResourcePath("assets", dirname(plot_file))

drawer_plot <- tags$div(
  tags$img(
    src = "assets/colony-counts.png",
    style = "width: 100%; border-radius: 6px;"
  ),
  tags$p(
    "Count of Adelie breeding pairs at each occupied colony this season.",
    style = "font-size: 0.85rem; color: var(--bs-secondary-color);"
  )
)

greeting_md <- paste0(
  "## Penguin research assistant\n\n",
  "I can query the survey observation database and read the field notebook.\n\n",
  "* <span class=\"suggestion submit\" title=\"Summarize the season\">What do the observations say about penguin counts?</span>\n",
  "* <span class=\"suggestion\" title=\"Compare colonies\">How do the colonies compare?</span>\n"
)

ui <- page_chat(
  "Research assistant",
  id = "chat",
  icon = tags$span("\U1F427"),
  toolbar = bslib::toolbar(
    bslib::toolbar_input_button(
      "new_survey",
      "New survey",
      icon = bsicons::bs_icon("plus-lg")
    )
  ),
  pages_navbar = list(
    chat_nav_panel(
      "Sources",
      tags$p("Sources selected during this session appear here.")
    )
  ),
  sidebar = chat_sidebar(history = TRUE, open = FALSE),
  drawer = chat_drawer(
    tags$p("Select a result to inspect it here."),
    title = "Latest result",
    open = FALSE
  ),
  greeting = greeting_md,
  placeholder = "Ask about the penguin survey...",
  icon_assistant = FALSE
)

server <- function(input, output, session) {
  client <- mock_client(model = "penguin-assistant", name = "Penguin assistant")
  chat_enable_history(
    "chat",
    client,
    options = history_options(
      store = "memory",
      title = function(recorded_turns) {
        first <- Filter(function(t) t$role == "user", recorded_turns)
        if (length(first)) {
          txt <- first[[1]]$content
          if (is.list(txt)) {
            txt <- txt[[1]]
          }
          if (nchar(txt) > 32) {
            txt <- paste0(substr(txt, 1, 32), "...")
          }
          txt
        } else {
          "New conversation"
        }
      }
    )
  )

  # New conversations clear the messages but leave a dismissed greeting in
  # place; clearing it re-arms greeting_requested so the greeting returns.
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
      block_delay = 1.6,
      word_delay = 0.05,
      on_done = function() {
        if (is.null(reply$drawer_title)) {
          return(invisible(NULL))
        }
        chat_drawer_update(
          "chat",
          drawer_plot,
          title = reply$drawer_title,
          session = session
        )
        chat_drawer_show("chat", session = session)
      }
    )
  })
}

shinyApp(ui, server)
