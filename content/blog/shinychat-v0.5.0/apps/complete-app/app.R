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

survey_reply <- list(
  contents = mock_message(
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
    paste0(
      "Across the season, Adelie pair counts at Cape Crozier **peaked in May at 118 active nests**",
      aside(
        "Survey observations",
        "https://data.example/penguins/cape-crozier",
        "peaked in May at 118 active nests",
        "Monthly survey counts, 2026 season. The May count reflects the height of incubation."
      ),
      ", before declining through June. Field notes attribute the June drop to two storm events ",
      "that flooded low-lying nests",
      aside(
        "Field notebook",
        "https://notes.example/may-survey",
        "flooded low-lying nests",
        "From `notes/may-survey.md`: *Calm seas. Counted 118 active nests at the north colony.*",
        "\n\nThe June entry records standing water across the terrace after the June 8 storm."
      ),
      "."
    )
  ),
  drawer_title = "Penguin counts"
)

fallback_reply <- list(
  contents = mock_message(
    paste0(
      "I'm the research assistant demo. Ask me about the penguin survey data ",
      "and I'll query the observation database and the field notebook for you."
    )
  )
)

# A small static plot for the artifact drawer
plot_file <- file.path(tempdir(), "penguin-counts.png")
grDevices::png(plot_file, width = 720, height = 480, res = 110)
par(mar = c(4.5, 4, 2, 1))
months <- c("Jan", "Feb", "Mar", "Apr", "May", "Jun")
counts <- c(38, 52, 71, 96, 118, 87)
barplot(
  counts,
  names.arg = months,
  col = "#447099",
  border = NA,
  ylim = c(0, 130),
  ylab = "Adelie pairs counted",
  main = "Adelie pairs by survey month, Cape Crozier"
)
grDevices::dev.off()
addResourcePath("assets", dirname(plot_file))

drawer_plot <- tags$div(
  tags$img(
    src = "assets/penguin-counts.png",
    style = "width: 100%; border-radius: 6px;"
  ),
  tags$p(
    "Count of Adelie breeding pairs recorded during monthly surveys.",
    style = "font-size: 0.85rem; color: var(--bs-secondary-color);"
  )
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
  sidebar = chat_sidebar(history = TRUE),
  drawer = chat_drawer(
    tags$p("Select a result to inspect it here."),
    title = "Latest result",
    open = FALSE
  ),
  greeting = paste0(
    "## Penguin research assistant\n\n",
    "I can query the survey observation database and read the field notebook.\n\n",
    "* <span class=\"suggestion submit\" title=\"Summarize the season\">What do the observations say about penguin counts?</span>\n",
    "* <span class=\"suggestion\" title=\"Compare colonies\">How do the colonies compare?</span>\n"
  ),
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

  observeEvent(input$chat_user_input, {
    text <- if (is.list(input$chat_user_input)) {
      input$chat_user_input[[1]]
    } else {
      input$chat_user_input
    }
    reply <- if (grepl("count|survey|observ|adelie", tolower(text))) {
      survey_reply
    } else {
      fallback_reply
    }
    mock_append_message("chat", reply$contents)
    mock_record(client, text, "See the response above.")
    mock_save_history("chat")
    chat_drawer_update(
      "chat",
      drawer_plot,
      title = reply$drawer_title %||% "Latest result"
    )
    chat_drawer_show("chat")
  })
}

shinyApp(ui, server)
