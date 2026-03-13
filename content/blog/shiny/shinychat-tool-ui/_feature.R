library(shinychat)
library(shiny)
library(bslib)

ui <-
  page_fillable(
    style = css(
      justify_content = "center",
      # https://www.css-gradient.com/?c1=004a75&c2=0088da&gt=l&gd=dbb
      background = "#004A75",
      background = "linear-gradient(0deg, #004A75, #0088DA 120%)"
    ),
    gap = 0,
    tags$style(
      "
    :root { font-size: 24px }
    .bi::after {
      mask-repeat: no-repeat;
    }
    "
    ),
    shinychat:::new_tool_card(
      "request",
      "test123",
      "shinychat_tool_ui",
      tool_title = "Add Tool Calling UI",
      intent = "shinychat for Python v0.2.0",
      arguments = "Tool calling UI was added to `shinychat` for Python in **v0.2.0**!"
    ),
    shinychat:::new_tool_card(
      "result",
      "test1234",
      "shinychat_tool_ui",
      icon = shiny::icon("check", class = "text-success"),
      tool_title = "Added Tool Calling UI",
      intent = "shinychat for R v0.3.0",
      show_request = FALSE,
      value = "Tool calling UI was added to <code>shinychat</code> for R in <strong>v0.3.0!</strong>",
      value_type = "html"
    )
  )

post_dir <- here::here("blog/posts/shinychat-tool-ui")

feature_dir <- fs::dir_create(fs::path(post_dir, "feature"))
feature_page <- fs::path(post_dir, "feature", "index.html")
htmltools::save_html(ui, feature_page)

webshot2::appshot(
  shinyApp(ui, server = function(input, output, session) {}),
  vwidth = 1200 / 1.5,
  vheight = 630 / 1.5,
  zoom = 4,
  file = here::here("blog/posts/shinychat-tool-ui/feature.png")
)
