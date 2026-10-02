# The offcanvas trigger example from the post, used for offcanvas-trigger.png.
# (A docstring would render as page text in Express mode, so keep this a comment.)

from shiny.express import ui

ui.offcanvas(
    "Panel content goes here.",
    title="Settings",
    trigger=ui.input_action_button("open", "Open settings"),
)
