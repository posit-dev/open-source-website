---
title: 'Complete chat applications in shinychat: R 0.5.0 and Python 0.7.1'
date: 2026-09-15T00:00:00.000Z
people:
  - Garrick Aden-Buie
  - Carson Sievert
description: >
  shinychat v0.5.0 for R and v0.7.1 for Python make it easier to build complete,
  conversation-centered Shiny chat applications with history, editing,
  branching, greetings, suggestions, citations, tool displays, and more.
image: images/og-header.png
image-alt: >
  A shinychat chat application greeting: the shinychat hex sticker above a
  heading reading "Complete chat applications in shinychat", a short
  introduction, and two suggestion cards — one for shinychat v0.5.0 for R and
  one for shinychat v0.7.1 for Python.
topics:
  - Artificial Intelligence
  - Interactive Apps
software:
  - shinychat
languages:
  - R
  - Python
source: shiny
hidesubscription: false
---


We're excited to announce [shinychat v0.5.0 for R](https://posit-dev.github.io/shinychat/r/) and [shinychat v0.7.1 for Python](https://posit-dev.github.io/shinychat/py/).
This release brings the pieces of a complete chat application together around the conversation itself.

shinychat is a toolkit for building complete, conversation-centered chat applications with Shiny.
The R package pairs with [ellmer](https://ellmer.tidyverse.org/), and the Python package pairs with [chatlas](https://posit-dev.github.io/chatlas/).
Install the latest releases from CRAN or PyPI:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-1" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-1-1">R</a></li>
<li><a href="#tabset-1-2">Python</a></li>
</ul>
<div id="tabset-1-1">

``` r
install.packages("shinychat")
```

</div>
<div id="tabset-1-2">

``` bash
pip install -U shinychat
```

</div>
</div>

We cover a lot in this post, and there's even more in the releases.
See the [R release notes](https://github.com/posit-dev/shinychat/blob/main/pkg-r/NEWS.md) and the [Python changelog](https://github.com/posit-dev/shinychat/blob/main/pkg-py/CHANGELOG.md) for the complete list of changes.

If you are upgrading an existing shinychat app, two changes matter.
In R, `chat_mod_ui()` and `chat_mod_server()` are soft-deprecated.
In both languages, startup messages no longer seed a conversation when history is enabled.
We cover both in [a few changes for existing apps](#a-few-changes-for-existing-apps) at the end of this post.

## Build a complete chat application around the conversation

{{< video src="images/complete-app.mp4" aspect-ratio="4x3" title="A complete chat application: the history sidebar lists saved conversations, the assistant answers with a tool activity row and citations, and the artifact drawer opens beside the chat with a plot" >}}

A useful chat application needs more than a text box and a streaming response.
Your users need a way to return to an earlier conversation, start a new one, correct a question, compare answers, inspect sources, and see what the model is doing when it calls a tool.
They may also need to upload a file, open a preview, or move between the chat and the rest of the application.

shinychat gives you sensible starting points for building that experience.
Pair it with [ellmer](https://ellmer.tidyverse.org/) in R or [chatlas](https://posit-dev.github.io/chatlas/) in Python, and you can get a working chat app running with little setup.
The chat application model has three layers:

1.  `page_chat()` gives you a full-window chat app with space for navigation, history, tools, and supporting content.
2.  `chat_ui()` lets you place chat wherever it fits best in your application.
3.  `chat_server()` for R or `Chat(client=...)` for Python connects your app to an `ellmer` or `chatlas` client and enables the integrated chat features.

When you want a fully custom experience or need a model client other than ellmer or chatlas, the lower-level pieces are still available for you to assemble yourself.

## Start with a complete chat application

When chat is the center of your application, use `page_chat()`.
It gives your users a full-window experience with a chat home, navigation pages, sidebars, toolbars, history, and an artifact drawer.
Users can move to a settings or sources page while their conversation keeps working and streaming.
The [Get started](https://posit-dev.github.io/shinychat/r/articles/get-started.html) guide for R and the [Page chat](https://posit-dev.github.io/shinychat/py/page-chat.html) guide for Python walk through the full layout.

`page_chat()` also brings together recent work on [toolbars](../../blog/2026-05-26_introducing-toolbars/) and [offcanvas panels](../../blog/2026-08-04_shiny-r-1-14-python-1-7/).
Toolbars give you clear places for controls that belong to a page, a sidebar, or the conversation, and offcanvas panels keep secondary content available without taking over the screen.
Both come up again when we [build the rest of the application around the chat](#build-the-rest-of-the-application-around-the-chat).

### Get a working chat app running

Here is the same starting point in both languages:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-2" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-2-1">R</a></li>
<li><a href="#tabset-2-2">Python</a></li>
</ul>
<div id="tabset-2-1">

``` r
library(shiny)
library(shinychat)

ui <- page_chat(title = "Assistant", id = "chat")

server <- function(input, output, session) {
  client <- ellmer::chat_openai(
    system_prompt = "You are a helpful assistant."
  )

  chat_server("chat", client)
}

shinyApp(ui, server)
```

</div>
<div id="tabset-2-2">

``` python
from chatlas import ChatAnthropic
from shinychat.express import Chat, page_chat

client = ChatAnthropic(system_prompt="You are a helpful assistant.")
chat = Chat(id="chat", client=client)

page_chat(title="Assistant", id="chat")
```

</div>
</div>

These small examples give you a working chat app backed by a real model.
In R, `chat_server()` connects the app to an `ellmer::Chat` object.
In Python, `Chat(client=...)` connects it to a `chatlas` client.
If you're new to LLM apps with Shiny, [Build Your First LLM App with Shiny](../../blog/2025-09-15_shiny-side-of-llms-part-3/) walks through the process from the beginning.

The same setup works for multi-user applications.
For local development in R, pass a client to `chat_app()` and get a personal chat UI in one call.
In Python, `Chat(client=client).app()` does the same.

### Welcome users and give them a place to start

<img src="images/greeting-suggestions-greeting.png" data-fig-alt="A new chat with a short welcome message and a grid of three suggestion cards beneath it." />

A blank chat can be intimidating, especially when users are not sure what the application can do.
Add a greeting to explain the application, set expectations, and give users a useful first step before they write their first message.
By default, greetings disappear when the user starts chatting.
Wrap the greeting in `chat_greeting(persistent = TRUE)` to keep it visible at the top of the conversation history.

Suggestions make the greeting actionable.
Users can click a suggestion to fill the input, ready to edit before sending.

<img src="images/greeting-suggestions-fill-input.png" data-fig-alt="Clicking a suggestion card fills the chat input with the suggested prompt, ready to edit before sending." />

When the suggestion should send without further editing, add the `submit` class and the click sends the prompt right away.

When you present suggestions as a list, shinychat turns them into a grid of cards with optional headings and descriptions.
The cards support keyboard navigation, so users can choose a suggested action without reaching for the mouse.

Here is the Markdown for a greeting with suggestion cards:

``` markdown
## Welcome!

What would you like to do?

* <span class="suggestion submit">Summarize my data</span>
* <span class="suggestion">Create a plot</span>
* <span class="suggestion">Explain this code</span>
```

The `suggestion` class makes the text clickable.
Add a `title` attribute to give a suggestion card a heading.

Suggestions can also appear later in a conversation, so the model can offer useful next steps instead of leaving users to guess what to ask next.
For model-generated suggestions, add instructions like these to your system prompt:

``` text
When you suggest next steps, format each suggestion as a Markdown list item.
Wrap the suggested text in <span class="suggestion">...</span>.
Add the submit class when the suggestion should be sent immediately.
```

You can also generate the greeting when the chat becomes visible, which is useful when the welcome message should reflect the user's context or come from the model.
A generated greeting is a natural place to introduce an application built around a particular dataset, workflow, or set of supported tasks.
The chat calls your `greeting` function when it needs its first message and passes it a fresh client based on the main client:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-3" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-3-1">R</a></li>
<li><a href="#tabset-3-2">Python</a></li>
</ul>
<div id="tabset-3-1">

``` r
ui <- page_chat("Assistant", id = "chat")

server <- function(input, output, session) {
  client <- ellmer::chat_openai(
    system_prompt = "You are a helpful assistant."
  )

  generate_greeting <- function(client) {
    stream <- client$stream_async(
      "Write a short, friendly welcome message."
    )
    chat_greeting(stream)
  }

  chat_server("chat", client, greeting = generate_greeting)
}
```

</div>
<div id="tabset-3-2">

``` python
from chatlas import ChatAnthropic
from shinychat import chat_greeting
from shinychat.express import Chat, page_chat

client = ChatAnthropic(
    system_prompt="You are a helpful assistant."
)


def generate_greeting(client):
    return chat_greeting(
        client.stream_async(
            "Write a short, friendly welcome message."
        )
    )


chat = Chat(id="chat", client=client, greeting=generate_greeting)

page_chat("Assistant", id="chat")
```

</div>
</div>
{{< video src="images/greeting-stream.mp4" aspect-ratio="4x3" title="A generated greeting streams into the empty chat: the welcome message arrives word by word, then two suggestion cards appear" >}}

Creating the client in `server()` gives each user session its own conversation.
The greeting prompt and its response aren't persisted in the main chat history, so the model starts fresh with the user's first message.

## Make the conversation the application state

<img src="images/history-list.png" data-fig-alt="The conversation history drawer open beside the chat, listing several named conversations under Today with a search field and a New conversation button." />

The biggest change in this release is the conversation history system.
When you use `chat_server()` in R or `Chat(client=...)` in Python, your app can give users several saved conversations instead of one growing transcript.

### Save and restore conversations

The history drawer lets users:

- Start a new conversation.
- Switch between saved conversations.
- Search conversations.
- Rename a conversation.
- Delete a conversation.
- Return to the conversation that was active when they last opened the app.

shinychat generates a short title once the conversation has enough content.
Users can replace that title, and title generation never overwrites a manual rename.

<div class="panel-tabset">
<ul id="tabset-4" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-4-1">Rename</a></li>
<li><a href="#tabset-4-2">Search</a></li>
</ul>
<div id="tabset-4-1">

<img src="images/history-actions-menu.png" data-fig-alt="The menu on a saved conversation with options to rename and delete it." />

</div>
<div id="tabset-4-2">

<img src="images/history-search.png" data-fig-alt="Typing in the history drawer search field narrows the conversation list to matching titles." />

</div>
</div>

You can keep conversations in memory during development or store them on disk in a deployed app.
Configure storage, user scope, title generation, and restore behavior with `history_options()` in R or `HistoryOptions` in Python.

For example, this configuration stores conversations on disk, keeps them separate by user, and puts the active conversation ID in the URL:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-5" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-5-1">R</a></li>
<li><a href="#tabset-5-2">Python</a></li>
</ul>
<div id="tabset-5-1">

``` r
history <- history_options(
  store = "file",
  scope = function(session) paste0("team-", session$user),
  restore_mode = "url"
)

chat_server("chat", client, history = history)
```

</div>
<div id="tabset-5-2">

``` python
from shinychat import Chat
from shinychat.types import HistoryOptions

history = HistoryOptions(
    store="file",
    scope=lambda session: f"team-{session.user}",
    restore_mode="url",
)

chat = Chat("chat", client=client, history=history)
```

</div>
</div>

Use `store = "memory"` in R or `store="memory"` in Python when conversations need to last only for the current process, such as during local development or tests.
On Posit Connect, conversation history is included with the platform and is enabled automatically when you provide a model client.
The default configuration uses Connect's [persistent storage](https://docs.posit.co/connect/user/structuring-content/#persistent-storage-on-posit-connect) and scopes conversations to the authenticated user.
That gives every user a private conversation history without an additional history service or per-user setup.

Users can return to a conversation after a reload, through a URL, or through Shiny bookmarking ([R](https://shiny.posit.co/r/articles/share/bookmarking-state/), [Python](https://shiny.posit.co/py/docs/bookmarking.html)).
The app keeps the transcript in its configured store instead of putting the full conversation in the URL.

### Edit a message without losing the original answer

{{< video src="images/edit-branches-edit.mp4" aspect-ratio="4x3" title="Editing an earlier message and resending it starts a new branch, and the sibling navigation control appears on the response" >}}

Editing a message now creates a new conversation **branch**.
When a user edits and resends an earlier message, shinychat forks the conversation at that point.
The original question and the rest of the conversation that follows stay on their branch.
The edited question starts a new branch, and users move between the two answers with the branch controls in the message.

<div class="panel-tabset">
<ul id="tabset-6" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-6-1">Branch 1</a></li>
<li><a href="#tabset-6-2">Branch 2</a></li>
</ul>
<div id="tabset-6-1">

<img src="images/edit-branches-original.png" data-fig-alt="The original conversation with an assistant response showing a 1 / 2 sibling navigation control." />

</div>
<div id="tabset-6-2">

<img src="images/edit-branches-new.png" data-fig-alt="The same conversation after editing a message, with the new branch&#39;s response selected and the sibling navigation control showing 2 / 2." />

</div>
</div>

Branches help when a prompt is almost right or when a model takes an unhelpful direction, and they make comparing answers easy without starting over.
And they are part of the saved conversation, so users return to their place in the conversation after a reload.

## Build the rest of the application around the chat

When chat is part of a larger application, your users still need access to filters, settings, sources, and results.
`page_chat()` gives you a place to put those alongside the conversation: a drawer for results, toolbars for controls, and offcanvas panels for settings you would rather keep off screen.

### Drawer: Show results and content next to the chat

The artifact drawer gives your users a second region next to the conversation.
Use it for a source preview, a rendered report, a table, a plot, or another piece of Shiny UI.
Your app can update the drawer as the conversation changes, so users can inspect a result without leaving the chat.

That separation fits applications where the conversation asks for something and the drawer shows the result.
A user can keep the conversation visible while inspecting a generated chart or document.

<img src="images/complete-app-nav-drawer.png" data-fig-alt="The research assistant app with the Research assistant and Sources navigation pages in the header, the conversation in the main region, and the artifact drawer open beside the chat showing a bar chart of penguin counts." />

Declare the drawer with the `drawer` argument of `page_chat()`:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-7" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-7-1">R</a></li>
<li><a href="#tabset-7-2">Python</a></li>
</ul>
<div id="tabset-7-1">

``` r
ui <- page_chat(
  "Research assistant",
  id = "chat",
  drawer = chat_drawer(
    tags$p("Select a result to inspect it here."),
    title = "Latest result",
    open = FALSE
  )
)
```

</div>
<div id="tabset-7-2">

``` python
from shiny import ui
from shinychat import chat_drawer
from shinychat.express import page_chat

page_chat(
    "Research assistant",
    id="chat",
    drawer=chat_drawer(
        ui.p("Select a result to inspect it here."),
        title="Latest result",
        open=False,
    ),
)
```

</div>
</div>

Inside `chat_drawer()`, the first argument is the content users see until your application fills the drawer with a result.
`title` names the region, and `open = FALSE` starts the drawer closed.

From the server, `chat_drawer_update()` fills the drawer with new content and `chat_drawer_show()` opens it, so a response with a result worth inspecting can bring the drawer up beside the conversation.
`chat_drawer_hide()` and `chat_drawer_toggle()` round out the controls, and the drawer content can be any Shiny UI, including live outputs:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-8" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-8-1">R</a></li>
<li><a href="#tabset-8-2">Python</a></li>
</ul>
<div id="tabset-8-1">

``` r
server <- function(input, output, session) {
  chat_server("chat", client)

  observeEvent(input$chat_user_input, {
    chat_drawer_update(
      "chat",
      drawer_plot,
      title = "Penguin counts"
    )
    chat_drawer_show("chat")
  })
}
```

</div>
<div id="tabset-8-2">

``` python
from shiny import reactive
from shinychat import Chat

chat = Chat("chat")


@reactive.effect
async def _show_result():
    await chat.drawer.update(drawer_plot, title="Penguin counts")
    await chat.drawer.show()
```

</div>
</div>

The video earlier in this post shows the pair in action: the research assistant's second response updates the drawer and opens it beside the conversation.

The toolbars and navigation pages in the screenshot come later in this section.
We assemble the complete application in code at the end.

### Toolbars: Put controls in the header or beside the chat input

<img src="images/toolbars-home.png" data-fig-alt="The research assistant home page with an active conversation. The page-scoped toolbar with a Clear conversation button and the global Help and Answer settings buttons sit in the header next to the navigation, and a toolbar with a response style selector sits below the chat input." />

Controls in a chat application have different scopes.
A button that clears the conversation belongs on the chat page.
A help button belongs on every page.
`page_chat()` gives each scope its own toolbar argument, built on the [toolbars](../../blog/2026-05-26_introducing-toolbars/) that bslib and Shiny shipped earlier this year.

`toolbar` holds controls scoped to the home page, where the conversation lives.
They appear with the navigation controls in the header.
`toolbar_global` holds controls that stay on every page, after the page-scoped toolbar.
By default, it contains the dark-mode toggle.
Pass `NULL` in R or `None` in Python to remove the global toolbar, including the dark-mode toggle.

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-9" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-9-1">R</a></li>
<li><a href="#tabset-9-2">Python</a></li>
</ul>
<div id="tabset-9-1">

``` r
ui <- page_chat(
  "Research assistant",
  id = "chat",
  toolbar = bslib::toolbar(
    bslib::toolbar_input_button(
      "clear_chat",
      "Clear conversation",
      icon = bsicons::bs_icon("arrow-counterclockwise")
    )
  ),
  toolbar_global = bslib::toolbar(
    bslib::toolbar_input_button(
      "help",
      "Help",
      icon = bsicons::bs_icon("question-circle")
    )
  )
)
```

</div>
<div id="tabset-9-2">

``` python
page_chat(
    "Research assistant",
    id="chat",
    toolbar=ui.toolbar(
        ui.toolbar_input_button(
            id="clear_chat",
            label="Clear conversation",
            icon=icon_svg("arrow-counterclockwise"),
        )
    ),
    toolbar_global=ui.toolbar(
        ui.toolbar_input_button(
            id="help",
            label="Help",
            icon=icon_svg("question-circle"),
        )
    ),
)
```

</div>
</div>

The buttons in these toolbars use `toolbar_input_button()`, a compact button designed for small spaces like headers, card headers, and footers.
When you give it an icon, it shows the icon alone and uses the label as its tooltip.

Users see the **Clear conversation** button while they chat and the **Help** button on every page, next to the dark-mode toggle.

The page-scoped toolbar follows the active page.
When you add a secondary page, its `chat_nav_panel()` supplies a `toolbar` that replaces the page-scoped toolbar while the user is on that page.
The global toolbar stays where it is.

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-10" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-10-1">R</a></li>
<li><a href="#tabset-10-2">Python</a></li>
</ul>
<div id="tabset-10-1">

``` r
chat_nav_panel(
  "Sources",
  tags$p("Sources selected during this session appear here."),
  toolbar = bslib::toolbar(
    bslib::toolbar_input_button(
      "refresh_sources",
      "Refresh",
      icon = bsicons::bs_icon("arrow-repeat")
    )
  )
)
```

</div>
<div id="tabset-10-2">

``` python
chat_nav_panel(
    "Sources",
    ui.p("Sources selected during this session appear here."),
    toolbar=ui.toolbar(
        ui.toolbar_input_button(
            id="refresh_sources",
            label="Refresh",
            icon=icon_svg("arrow-repeat"),
        )
    ),
)
```

</div>
</div>

On the Sources page, the page-scoped toolbar shows the **Refresh** button instead, while **Help** and the dark-mode toggle remain.

Controls that act on the message itself get a third spot.
`toolbar_input` places a toolbar directly below the chat input, independent of the navigation toolbars.
Explore it in the [shinychat for R](https://posit-dev.github.io/shinychat/r/) or [shinychat for Python](https://posit-dev.github.io/shinychat/py/) documentation.

### Offcanvas: Open a panel over the app from any page

A toolbar button is also a natural trigger for an [offcanvas panel](../../blog/2026-08-04_shiny-r-1-14-python-1-7/).
Here, a button in the global toolbar opens an **Answer settings** panel from any page, without leaving the conversation:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-11" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-11-1">R</a></li>
<li><a href="#tabset-11-2">Python</a></li>
</ul>
<div id="tabset-11-1">

``` r
ui <- page_chat(
  "Research assistant",
  id = "chat",
  toolbar_global = bslib::toolbar(
    bslib::toolbar_input_button(
      "show_settings",
      "Answer settings",
      icon = bsicons::bs_icon("gear")
    )
  )
)

server <- function(input, output, session) {
  observeEvent(input$show_settings, {
    bslib::show_offcanvas(
      bslib::offcanvas(
        title = "Answer settings",
        id = "answer_settings",
        placement = "right",
        sliderInput("length", "Target length", 100, 1000, 400),
        checkboxInput("citations", "Request citations", TRUE)
      ),
      session = session
    )
  })
}
```

</div>
<div id="tabset-11-2">

``` python
from faicons import icon_svg
from shiny import reactive, ui
from shinychat.express import page_chat

page_chat(
    "Research assistant",
    id="chat",
    toolbar_global=ui.toolbar(
        ui.toolbar_input_button(
            id="show_settings",
            label="Answer settings",
            icon=icon_svg("gear"),
        )
    ),
)


@reactive.effect
@reactive.event(input.show_settings)
def open_answer_settings():
    ui.show_offcanvas(
        ui.offcanvas(
            title="Answer settings",
            id="answer_settings",
            placement="right",
            ui.input_slider("length", "Target length", 100, 1000, 400),
            ui.input_checkbox("citations", "Request citations", True),
        )
    )
```

</div>
</div>

<img src="images/toolbars-offcanvas.png" data-fig-alt="The research assistant app with the Answer settings offcanvas open along the right edge, showing a target length slider and a citations checkbox beside the conversation." />

### Putting it all together

Add navigation pages with `chat_nav_panel()` or the corresponding Shiny navigation helpers.
Add a sidebar for filters or other controls.
On a narrow screen, users can find the same controls in the application menu.

You can compose these regions directly in `page_chat()`.
This is the same research assistant from the screenshots throughout this section, with the toolbars, the navigation pages, and the drawer all in one call:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-12" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-12-1">R</a></li>
<li><a href="#tabset-12-2">Python</a></li>
</ul>
<div id="tabset-12-1">

``` r
ui <- page_chat(
  "Research assistant",
  id = "chat",
  toolbar = bslib::toolbar(
    bslib::toolbar_input_button(
      "clear_chat",
      "Clear conversation",
      icon = bsicons::bs_icon("arrow-counterclockwise")
    )
  ),
  toolbar_global = bslib::toolbar(
    bslib::toolbar_input_button(
      "help",
      "Help",
      icon = bsicons::bs_icon("question-circle")
    )
  ),
  pages_navbar = list(
    chat_nav_panel(
      "Sources",
      tags$p("Sources selected during this session appear here."),
      toolbar = bslib::toolbar(
        bslib::toolbar_input_button(
          "refresh_sources",
          "Refresh",
          icon = bsicons::bs_icon("arrow-repeat")
        )
      )
    )
  ),
  drawer = chat_drawer(
    tags$p("Select a result to inspect it here."),
    title = "Latest result",
    open = FALSE
  )
)
```

</div>
<div id="tabset-12-2">

``` python
from shiny import ui
from shinychat import chat_drawer, chat_nav_panel
from shinychat.express import page_chat

page_chat(
    "Research assistant",
    id="chat",
    toolbar=ui.toolbar(
        ui.toolbar_input_button(
            id="clear_chat",
            label="Clear conversation",
            icon=icon_svg("arrow-counterclockwise"),
        )
    ),
    toolbar_global=ui.toolbar(
        ui.toolbar_input_button(
            id="help",
            label="Help",
            icon=icon_svg("question-circle"),
        )
    ),
    pages_navbar=[
        chat_nav_panel(
            "Sources",
            ui.p("Sources selected during this session appear here."),
            toolbar=ui.toolbar(
                ui.toolbar_input_button(
                    id="refresh_sources",
                    label="Refresh",
                    icon=icon_svg("arrow-repeat"),
                )
            ),
        )
    ],
    drawer=chat_drawer(
        ui.p("Select a result to inspect it here."),
        title="Latest result",
        open=False,
    ),
)
```

</div>
</div>

Users see the **Clear conversation** button while they chat, the **Help** button on every page, a **Sources** page with its own **Refresh** toolbar, and a **Latest result** drawer beside the conversation.

## Help users follow the model's work

Your users can now follow more than the final answer.
A response can include ordinary text, thinking content, web activity, citations, tool calls, tool results, and custom UI.
shinychat presents each part in a way that helps users understand the answer and what produced it.

### Tool calls stay visible and readable

<img src="images/tool-calls-collapsed.png" data-fig-alt="A sales assistant conversation where two SQL queries and a schema read appear as compact activity rows above the answer." />

Tool calls now appear as compact activity rows instead of taking over the conversation, a refinement of the [tool-call cards shinychat introduced last year](../../blog/2025-11-20_shinychat-tool-ui/).
shinychat groups related calls into a single row.
Users can expand a group, open an individual call, and inspect the request and result when they need more detail.

Each call can show a short title, a label such as a file name or query, and a value preview such as a row count.
Users can see the activity while the tool runs and inspect the result after it finishes.

<img src="images/tool-calls-expanded.png" data-fig-alt="The grouped tool-call row expanded to show the two SQL queries with row count and result previews." />

Opening an individual call shows the request and the result in a card:

<img src="images/tool-calls-result.png" data-fig-alt="The SQL query expanded to a card showing the full tool call arguments and the query result as a small table." />

Configure grouping with `tool_grouping` when your application needs a different amount of detail.

For example, use `"all"` to show one activity row for a complete tool-calling loop, or use `"none"` to show every call separately:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-13" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-13-1">R</a></li>
<li><a href="#tabset-13-2">Python</a></li>
</ul>
<div id="tabset-13-1">

``` r
ui <- page_chat(
  "Assistant",
  id = "chat",
  tool_grouping = "all"
)
```

</div>
<div id="tabset-13-2">

``` python
page_chat(
    "Assistant",
    id="chat",
    tool_grouping="all",
)
```

</div>
</div>

Grouping keeps the answer readable, and the request and result stay one click away.
To learn how to register tools and customize their display, see [Tool UI in shinychat for R](https://posit-dev.github.io/shinychat/r/articles/tool-ui.html), [Tools in Shiny for Python](https://shiny.posit.co/py/docs/genai-tools.html), [tool/function calling in ellmer](https://ellmer.tidyverse.org/articles/tool-calling.html), or [tool calling in chatlas](https://posit-dev.github.io/chatlas/get-started/tools.html).

### Citations stay connected to the claims they support

When your model provider supports citations, shinychat shows them directly.
Providers with built-in web search or web fetch tools return citations with the response, and users can open each citation beside the claim it supports or browse the message-wide Sources summary.
When the provider supplies grounded spans, each citation stays connected to the exact text it supports.

Custom retrieval applications, like the RAG systems you can build with [raghilda](../../blog/2026-04-14_rag-with-raghilda/), can produce the same display.
Write a `<shiny-aside>` tag into an assistant response, or prompt the model to write one, with the source URL and the exact text the source supports:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-14" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-14-1">R</a></li>
<li><a href="#tabset-14-2">Python</a></li>
</ul>
<div id="tabset-14-1">

``` r
chat_append(
  "chat",
  paste0(
    "The report recommends a smaller batch size ",
    '<shiny-aside label="Internal report" ',
    'url="https://example.com/report" ',
    'grounded-span="The report recommends a smaller batch size">',
    "See the methods section for the supporting analysis.",
    "</shiny-aside>."
  )
)
```

</div>
<div id="tabset-14-2">

``` python
await chat.append_message(
    "The report recommends a smaller batch size "
    '<shiny-aside label="Internal report" '
    'url="https://example.com/report" '
    'grounded-span="The report recommends a smaller batch size">'
    "See the methods section for the supporting analysis."
    "</shiny-aside>."
)
```

</div>
</div>

When the message renders, users see a citation beside the claim.
The `label` names the source, the `url` links to it, and `grounded-span` marks the answer text the source supports.

<img src="images/citations-popover.png" data-fig-alt="An assistant response where each cited claim is underlined and a pill reading Internal report +1 marks the message&#39;s sources, with the citation popover open just below the pill showing the source name, a link, the supporting passage, and controls to move between the message&#39;s two citations." />

### Thinking and streaming remain part of the conversation

Responses still stream into the chat as the model produces them.
When a model provides thinking content, shinychat shows it in a collapsible panel above the response and collapses the panel when the answer begins.

<img src="images/thinking-collapsed.png" data-fig-alt="An assistant response with a collapsed panel reading Thought for 4s between the user&#39;s question and the answer." />

If a response is taking too long, your users can stop it with the cancel button or the Escape key.
The partial response remains in the conversation instead of disappearing.

<img src="images/streaming-stop.png" data-fig-alt="While a response streams in, the send button at the right of the chat input becomes a red stop button." />

## Let users add context and shortcuts

### Attach images, PDFs, and text files

Your users can send images, PDFs, and text files through a file picker, drag and drop, or paste.
With the integrated `ellmer` or `chatlas` setup, those files reach the model alongside the user's message.

<img src="images/attachments-plot.png" data-fig-alt="A plot attached to the chat input as a thumbnail chip above the prompt Explain this plot, with the attach button at the left of the input." />

In R, set `allow_attachments = TRUE` on `chat_ui()` or `page_chat()` when you want to offer attachments.
In Python, `Chat(client=...)` enables attachments automatically.
Both packages accept a list of MIME types when your application needs to restrict the files users can send.
The default limit is about 30 MB across the files in one message.
You can change it with the `SHINYCHAT_MAX_ATTACHMENT_SIZE` environment variable.

To accept only images and PDFs, pass the MIME types to the chat UI:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-15" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-15-1">R</a></li>
<li><a href="#tabset-15-2">Python</a></li>
</ul>
<div id="tabset-15-1">

``` r
ui <- page_chat(
  "Assistant",
  id = "chat",
  allow_attachments = c("image/*", "application/pdf")
)
```

</div>
<div id="tabset-15-2">

``` python
page_chat(
    "Assistant",
    id="chat",
    allow_attachments=["image/*", "application/pdf"],
)
```

</div>
</div>

With this configuration, the file picker accepts only images and PDFs.

### Add slash commands

<img src="images/slash-commands-palette.png" data-fig-alt="The slash command palette open above the chat input, listing /help, /search, and /clear with short descriptions." />

Your users can type `/` to open a command palette.
A command can expand the user's text into a richer prompt, perform an action without calling the model, or run entirely in the browser.

For example, `/search shiny modules` can retrieve documentation and send a larger prompt to the model.
A `/clear` command can clear the active conversation without involving the model.
A client-side command can open a modal, clear the input, or trigger another browser action without a server round-trip.

Register commands on the object returned by `chat_server()` in R or on the `Chat` object in Python.
When users return to a saved conversation, they still see the command they entered.

For example, add a `/help` command that displays guidance without sending anything to the model:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-16" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-16-1">R</a></li>
<li><a href="#tabset-16-2">Python</a></li>
</ul>
<div id="tabset-16-1">

``` r
chat <- chat_server("chat", client)

chat$slash_command("help", "Show help", function() {
  showModal(
    modalDialog(
      "Try `/search topic` to search the documentation.",
      title = "Help",
      easyClose = TRUE
    )
  )
}, echo = FALSE)
```

</div>
<div id="tabset-16-2">

``` python
chat = Chat("chat", client=client)

@chat.slash_command("help", "Show help", echo=False)
def _():
    m = ui.modal(
      "Try `/search topic` to search the documentation.",
      title="Help"
    )
    ui.modal_show(m)
```

</div>
</div>

When a user chooses `/help`, the command opens a modal with the guidance and sends nothing to the model.

## The same chat experience in either language

Whichever language you use, you can give users the same conversation-centered experience:

| Application need             | R                   | Python                  |
|------------------------|------------------------|------------------------|
| Full-window chat application | `page_chat()`       | `page_chat()`           |
| Embedded chat                | `chat_ui()`         | `chat_ui()`             |
| Connect a model client       | `chat_server()`     | `Chat(client=...)`      |
| Model client                 | `ellmer::Chat`      | `chatlas` client        |
| Conversation settings        | `history_options()` | `HistoryOptions`        |
| Standalone helper            | `chat_app()`        | `shinychat.page_chat()` |

You can focus on the application you want to build while `ellmer` or `chatlas` handles model requests and tools.
shinychat gives that model a conversation interface with history, rich responses, and the controls your users need.
And for a ready-made chat-with-your-data application, take a look at [querychat](../../blog/2026-06-17_querychat-ggsql/).

## A few changes for existing apps

Existing `chat_ui()` applications remain supported.
Use `chat_ui()` when you want chat to share a page with other top-level content.
Use `page_chat()` when you want the conversation to fill the application.
Use `page_chat()` as the outermost page container. Nesting it inside another page layout breaks the full-window layout and history experience.

In R, `chat_mod_ui()` and `chat_mod_server()` are soft-deprecated in favor of pairing `chat_ui()` and `chat_server()` by ID.
In both languages, startup messages are no longer the right way to seed a conversation when history is enabled.
Use a greeting or append messages through the chat object instead.

The release also protects users from unsafe model-authored Markdown, shows an error when a response fails before streaming starts, and preserves tool results, citations, attachments, and other rich content when users return to a conversation.

With `page_chat()`, `chat_server()` or `Chat(client=...)`, and the history options, you can now give your users a complete chat application: saved conversations they can return to, messages they can edit into new branches, greetings and suggestions to start from, and responses with visible tool calls, citations, and thinking.

Read the [shinychat for R documentation](https://posit-dev.github.io/shinychat/r/) or the [shinychat for Python documentation](https://posit-dev.github.io/shinychat/py/) to explore the examples.
For the complete list of changes, see the [R release notes](https://github.com/posit-dev/shinychat/blob/main/pkg-r/NEWS.md) and the [Python changelog](https://github.com/posit-dev/shinychat/blob/main/pkg-py/CHANGELOG.md).

## Acknowledgements

We thank everyone who contributed to these releases, for opening issues,
submitting pull requests, and providing feedback:
[@bastianolea](https://github.com/bastianolea),
[@bianchenhao](https://github.com/bianchenhao),
[@christophsax](https://github.com/christophsax),
[@cpsievert](https://github.com/cpsievert),
[@crissthiandi](https://github.com/crissthiandi),
[@elnelson575](https://github.com/elnelson575),
[@gadenbuie](https://github.com/gadenbuie),
[@Harshit28j](https://github.com/Harshit28j),
[@JamesHWade](https://github.com/JamesHWade),
[@jcheng5](https://github.com/jcheng5),
[@jlxAtNovozymes](https://github.com/jlxAtNovozymes),
[@jnhyeon](https://github.com/jnhyeon),
[@jose-c-milliman](https://github.com/jose-c-milliman),
[@kaipingyang](https://github.com/kaipingyang),
[@lucasrod16](https://github.com/lucasrod16),
[@markmcd](https://github.com/markmcd),
[@nbenn](https://github.com/nbenn),
[@parmsam](https://github.com/parmsam),
[@schloerke](https://github.com/schloerke),
[@shea-parkes](https://github.com/shea-parkes),
[@simonpcouch](https://github.com/simonpcouch),
[@slupczynskim](https://github.com/slupczynskim),
[@thisisnic](https://github.com/thisisnic),
[@wlandau](https://github.com/wlandau), and
[@xx02al](https://github.com/xx02al).
