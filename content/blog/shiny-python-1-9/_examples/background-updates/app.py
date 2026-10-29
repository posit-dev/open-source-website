import asyncio
from datetime import datetime

from shiny import App, ui

app_ui = ui.page_fixed(
    ui.input_text("status", "Last heartbeat"),
)


def server(input, output, session):
    async def heartbeat():
        while True:
            await asyncio.sleep(1)
            ui.update_text("status", value=datetime.now().strftime("%H:%M:%S"))

    task = asyncio.create_task(heartbeat())
    session.on_ended(task.cancel)


app = App(app_ui, server)
