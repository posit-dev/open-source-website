# The same app as ../after-app, written with the habits the shiny-for-r skill
# steers agents away from: nested fluidRow()/column() grids, and tabs faked
# with buttons and conditionalPanel().
library(shiny)

ui <- fluidPage(
  titlePanel("Fuel economy"),
  fluidRow(
    column(
      3,
      wellPanel(
        checkboxGroupInput("cyl", "Cylinders", c(4, 6, 8), selected = c(4, 6, 8)),
        sliderInput("hp", "Horsepower", 50, 340, c(50, 340))
      )
    ),
    column(
      9,
      fluidRow(
        column(4, h4("Cars"), textOutput("n")),
        column(4, h4("Average mpg"), textOutput("mpg")),
        column(4, h4("Average weight"), textOutput("wt"))
      ),
      fluidRow(
        column(
          12,
          actionButton("show_plot", "Plot"),
          actionButton("show_data", "Data")
        )
      ),
      fluidRow(
        column(
          12,
          conditionalPanel("output.view == 'plot'", plotOutput("plot")),
          conditionalPanel("output.view == 'data'", tableOutput("data"))
        )
      )
    )
  )
)

server <- function(input, output, session) {
  view <- reactiveVal("plot")
  observeEvent(input$show_plot, view("plot"))
  observeEvent(input$show_data, view("data"))
  output$view <- renderText(view())
  outputOptions(output, "view", suspendWhenHidden = FALSE)

  cars <- reactive({
    mtcars[mtcars$cyl %in% input$cyl & mtcars$hp >= input$hp[1] & mtcars$hp <= input$hp[2], ]
  })
  output$n <- renderText(nrow(cars()))
  output$mpg <- renderText(round(mean(cars()$mpg), 1))
  output$wt <- renderText(paste(round(mean(cars()$wt) * 1000), "lb"))
  output$plot <- renderPlot(plot(cars()$wt, cars()$mpg, xlab = "wt", ylab = "mpg"))
  output$data <- renderTable(cars(), rownames = TRUE)
}

shinyApp(ui, server)
