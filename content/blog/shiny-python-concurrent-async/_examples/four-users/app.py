"""
One app, four users: a demo of how Shiny for Python 1.9 runs async code.

The page at "/" shows four people using the app, each in an iframe, so each one
is a separate session in the same Python process. Alice, Bob and Carol run a
report with two outputs, "sales" and "forecast". Each output awaits
`asyncio.sleep(DELAY)`, in place of a slow database query. Dan only watches a
live chart that the server updates every 0.2s.

Before Shiny 1.9, a flush runs one output at a time, behind the process-wide
`reactive.lock()`. When the three reports start together, they finish after 4s,
8s and 12s, and Dan's chart stops until all of them finish. In Shiny 1.9 and
later, every report finishes after 2s and Dan's chart keeps moving.

"/?user=<name>" is one person's view. Its "Run report" button has the id "run".
The browser splits the wait after a click into "Waited", "Computed" and
"Blocked", and stores the time from the click to the last result in the
"data-seconds" attribute of "#elapsed".
"""

import asyncio
import json
import random
import time
from collections import deque
from urllib.parse import parse_qs

import otel_trace
import shiny
from shiny import App, reactive, render, req, ui
from shiny.session import Session

DELAY = 2
USERS = [("Alice", True), ("Bob", True), ("Carol", True), ("Dan", False)]
OUTPUTS = {"sales": "Sales", "forecast": "Forecast"}
FEED_POINTS = 60

OTEL = otel_trace.install()
CONCURRENT = hasattr(Session, "run_once_when_idle")
MODE = "sessions run at the same time" if CONCURRENT else "sessions share a global lock"
VERSION_LABEL = "Shiny v1.9+" if CONCURRENT else "Shiny pre-v1.9"

# Shinylive gives each app iframe a socket by sending "openChannel" to the parent
# window. The user views are iframes inside this page, so pass their messages on.
RELAY_JS = """
window.addEventListener("message", (event) => {
  if (event.data?.type === "openChannel" && window.parent !== window) {
    window.parent.postMessage(event.data, "*", event.ports);
  }
});
"""

CLICK_ALL_JS = """
$(document).on("click", "#everyone", () => {
  window.traceAnchor?.();
  document.querySelectorAll("iframe[data-runs]").forEach((frame) => {
    frame.contentDocument.getElementById("run").click();
  });
});
"""

STOPWATCH_JS = """
// Splits a person's wait into three parts that add up to the wall time, one per
// line:
// - Waited: from the click until their first output starts.
// - Computed: the time that at least one of their outputs is running.
// - Blocked: from the end of their outputs until their session sends its next
//   update (the live chart moves again).
// Each line counts up in tenths of a second while it runs, and settles on whole
// seconds. A view without a "Run report" button counts any pause in its live
// chart as blocked.
//
// Each output has a status icon that follows Shiny's own messages: a hand from
// the click until the server starts the output, a spinner from its
// "recalculating" message, and a check from its "recalculated" message.
const outputs = __OUTPUTS__;
const DELAY = __DELAY__;
const FEED_GAP = 0.5;  // seconds without a chart update that count as blocked
const now = () => Date.now() / 1000;  // the server reports times on this clock
const live = (seconds) => `${seconds.toFixed(1)}s`;
const whole = (seconds) => `${Math.round(seconds)}s`;
const ICONS = {
  queued: '<span title="Queued">&#x270B;</span>',
  running: '<span class="spinner-border text-primary" title="Running"></span>',
  done: '<svg viewBox="0 0 16 16" width="18" height="18" aria-label="Done">' +
    '<circle cx="8" cy="8" r="8" fill="#008300"/>' +
    '<path d="M4.5 8.2l2.3 2.3 4.7-4.9" fill="none" stroke="#fff" ' +
    'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
};
let clickedAt = null;    // set while a run is in progress
let startedAt = null;    // when the browser heard that the first output started
let pending = new Set();
let intervals = [];
let lastFeed = now();
let blockedFrom = null;

function show(selector, text, cls) {
  $(selector).text(text).attr("class", cls ?? "");
}

function setStatus(id, state) {
  $(`#${id}-status`).html(ICONS[state]);
}

function finishBlocked(t) {
  const blocked = t - blockedFrom;
  blockedFrom = null;
  show("#blocked", `Blocked for ${whole(blocked)}`, blocked > FEED_GAP ? "bad" : "quiet");
}

$(document).on("click", "#run", () => {
  if (window.parent !== window) window.parent.traceAnchor?.();
  clickedAt = now();
  startedAt = null;
  pending = new Set(outputs);
  intervals = [];
  blockedFrom = null;
  show("#elapsed", "");
  show("#blocked", "");
  $("#elapsed").removeAttr("data-seconds");
  outputs.forEach((id) => setStatus(id, "queued"));
});

$(document).on("shiny:message", (event) => {
  const msg = event.message?.recalculating;
  if (clickedAt === null || !msg || !outputs.includes(msg.name)) return;
  if (msg.status === "recalculating") {
    if (startedAt === null) startedAt = now();
    setStatus(msg.name, "running");
  } else if (msg.status === "recalculated") {
    setStatus(msg.name, "done");
  }
});

$(document).on("shiny:value", (event) => {
  const t = now();
  if (event.name === "feed") {
    if (blockedFrom !== null) finishBlocked(t);
    lastFeed = t;
    return;
  }
  if (clickedAt === null || !pending.delete(event.name)) return;
  // Each output reports when its work started and ended.
  const html = event.value?.html ?? "";
  const start = /data-start="([0-9.]+)"/.exec(html);
  const end = /data-end="([0-9.]+)"/.exec(html);
  if (start && end) intervals.push([Number(start[1]), Number(end[1])]);
  if (pending.size > 0) return;

  intervals.sort((a, b) => a[0] - b[0]);
  let computed = 0, until = -Infinity;
  for (const [a, b] of intervals) {
    if (b > until) { computed += b - Math.max(a, until); until = b; }
  }
  const waited = Math.max(0, intervals[0][0] - clickedAt);
  show("#waited", `Waited for ${whole(waited)}`, waited > FEED_GAP ? "bad" : "quiet");
  show("#elapsed", `Computed in ${whole(computed)}`, computed > DELAY + FEED_GAP ? "done" : "fast");
  $("#elapsed").attr("data-seconds", t - clickedAt);
  outputs.forEach((id) => setStatus(id, "done"));
  clickedAt = null;
  // The session is blocked until its next update.
  blockedFrom = until;
});

setInterval(() => {
  const t = now();
  if (clickedAt !== null) {
    if (startedAt === null) {
      show("#waited", `Waiting ${live(t - clickedAt)}`, "waiting");
    } else {
      show("#waited", `Waited for ${live(startedAt - clickedAt)}`, "waiting");
      show("#elapsed", `Computing ${live(t - startedAt)}`, "waiting");
    }
    return;
  }
  const watchOnly = $("#run").length === 0;
  if (blockedFrom === null && watchOnly && t - lastFeed > FEED_GAP) blockedFrom = lastFeed;
  if (blockedFrom !== null && t - blockedFrom > FEED_GAP) {
    show("#blocked", `Blocked for ${live(t - blockedFrom)}`, "bad");
  }
}, 50);
"""
STOPWATCH_JS = STOPWATCH_JS.replace("__OUTPUTS__", json.dumps(list(OUTPUTS)))
STOPWATCH_JS = STOPWATCH_JS.replace("__DELAY__", str(DELAY))

STYLE = """
html, body { height: 100%; }
body { padding: 0.5rem 0.75rem; }
body > .container { height: 100%; display: flex; flex-direction: column; padding: 0; }
#waited, #elapsed, #blocked {
  font-size: 1.15rem; font-weight: 600; font-variant-numeric: tabular-nums;
  min-height: 1.7rem; line-height: 1.7rem; white-space: nowrap;
}
.waiting { color: #52514e; }
.quiet { color: #52514e; }
.fast { color: #008300; }
.done { color: #0b0b0b; }
.bad { color: #c62828; }
/* The outputs' status sits just above the chart, at the bottom of the card. */
.outputs { margin-top: auto; }
.outputs + .feed { margin-top: 0; }
.output-row { display: flex; align-items: center; gap: 0.4rem; height: 1.6rem; }
.status {
  display: inline-flex; align-items: center; justify-content: center;
  width: 1.3rem; height: 1.3rem; font-size: 1rem;
}
.status .spinner-border { width: 1rem; height: 1rem; border-width: 0.16em; }
/* The outputs only report timings, but must stay visible so that Shiny runs them. */
.probe { display: inline-block; width: 1px; height: 1em; overflow: hidden; }
.feed { margin-top: auto; padding-top: 0.25rem; }
.feed svg { width: 100%; height: 56px; background: #f4f4f2; border-radius: 4px; }
iframe { width: 100%; height: 100%; border: 0; overflow: hidden; }
.half { flex: 1 1 0 !important; min-height: 0; }
"""


def user_ui(name: str, runs_report: bool):
    if runs_report:
        role = f"Two outputs, {DELAY}s each"
        body = [
            ui.input_action_button("run", "Run report", class_="btn-primary w-100 mb-1"),
            ui.div(id="waited"),
            ui.div(id="elapsed"),
            ui.div(id="blocked"),
            ui.div(
                *[
                    ui.div(
                        ui.span(id=f"{id}-status", class_="status"),
                        label,
                        ui.output_ui(id, inline=True, class_="probe"),
                        class_="output-row",
                    )
                    for id, label in OUTPUTS.items()
                ],
                class_="outputs",
            ),
        ]
    else:
        role = "Only watches the live chart"
        body = [ui.div(id="blocked")]
    return ui.page_fixed(
        ui.tags.style(STYLE),
        ui.tags.script(STOPWATCH_JS),
        ui.h5(name, class_="mb-0"),
        ui.p(role, class_="small text-body-secondary mb-2"),
        *body,
        ui.div(ui.output_ui("feed"), class_="feed"),
    )


def explanation():
    this_server = " **(this server)**"
    return ui.markdown(f"""
##### What you see

Four people use one Shiny app at the same time. Each panel is an `<iframe>`
that loads the app's page for one person (for example `?user=Alice`). So each
panel is a separate Shiny session in the same Python process, the same as four
people who open the app in their own browsers.

##### The report

“Run report” starts two async outputs, “Sales” and “Forecast”. Each one runs
`await asyncio.sleep({DELAY})`, which stands in for slow I/O, such as a database
query or a call to an API.

Each output has a status icon, which follows the messages Shiny sends to the
browser: a hand while the output waits for the server to start it, a spinner
once the server starts it, and a check when it has finished.

The stopwatch runs in the browser. It measures from the click, and splits the
time into three parts that add up to the wall time. “Waited” lasts until the
person's first output starts. “Computed” is the time that at least one of their
outputs was running. “Blocked” lasts from the end of their outputs until their
session updates again (their live chart moves). Dan does not click, so his
panel counts any pause in his chart as blocked.

##### The live chart

The server draws each chart again every 0.2 seconds with
`reactive.invalidate_later()`. The data is random. When a chart stops moving,
that session is not getting updates from the server. The time under the chart
shows the last update.

##### The span timeline

Shiny emits OpenTelemetry spans for its work. Each user has one row. The blue
and orange bars are the `output sales` and `output forecast` spans, from when
each output starts to when it ends. A green tick is an `output feed` span, one
redraw of the live chart. A lighter bar is a span that is still running. The
page reads the spans over a separate HTTP route that does not wait for the
reactive lock, so the timeline keeps moving even when every session waits.

##### What to expect

**Before Shiny 1.9**{"" if CONCURRENT else this_server}: every session's reactive
updates run behind one `reactive.lock()` for the whole process, one output at
a time. Each report takes 4 seconds, because its two outputs run one after
the other. The three reports finish after 4, 8 and 12 seconds, and all charts,
Dan's too, stop while the reports run. In the timeline, the output spans form
a staircase and no row gets green ticks until the last report ends.

**Shiny 1.9 and later**{this_server if CONCURRENT else ""}: outputs
start together, in the same session and across sessions. All three reports
finish after about 2 seconds, and Dan's chart does not stop. In the timeline,
all six output spans start and end together, and Dan's row gets green ticks
the whole time. A person's own chart stops while their report runs, because a
session applies its next update only after its outputs are done. Shiny for R
works the same way.

##### Try it

- Click the button above the panels to start three reports at once.
- Click one panel's “Run report” and watch Dan's chart.
- Open `?user=YourName` in a new window to add one more user.
""")


def control_room_ui(sidebar_open: bool = True):
    panels = [
        ui.card(
            ui.card_body(
                ui.tags.iframe(src=f"?user={name}", data_runs="" if runs else None),
                padding=0,
            )
        )
        for name, runs in USERS
    ]
    return ui.page_sidebar(
        ui.sidebar(
            ui.span(
                f"shiny {shiny.__version__}: {MODE}",
                class_="badge text-bg-secondary text-wrap",
            ),
            explanation(),
            width=360,
            open="desktop" if sidebar_open else "closed",
        ),
        ui.tags.style(STYLE),
        ui.tags.script(RELAY_JS),
        ui.tags.script(CLICK_ALL_JS),
        ui.div(
            ui.input_action_button(
                "everyone",
                "Alice, Bob and Carol click “Run report”",
                class_="btn-primary",
            ),
            ui.span(f"Each report runs two outputs that take {DELAY}s each."),
            class_="d-flex flex-nowrap align-items-center gap-3 text-nowrap",
        ),
        ui.layout_columns(*panels, col_widths=3, class_="half"),
        otel_trace.trace_panel(
            [name for name, _ in USERS],
            {
                "sales": ("output sales", (0.1, 0.48)),
                "forecast": ("output forecast", (0.52, 0.9)),
                "feed": ("output feed", (0.1, 0.9)),
            },
            window_seconds=18,
            fill=True,
            installed=OTEL,
            class_="half",
        ),
        title=ui.div(
            "One app, four users",
            ui.span(VERSION_LABEL, class_="badge text-bg-dark fs-6 ms-auto"),
            class_="d-flex align-items-center w-100",
        ),
        fillable=True,
    )


def app_ui(request):
    name = request.query_params.get("user")
    if name is None:
        # "?sidebar=closed" shows only the main panel, for screen recordings.
        return control_room_ui(
            sidebar_open=request.query_params.get("sidebar") != "closed"
        )
    runs_report = dict(USERS).get(name, True)
    return user_ui(name, runs_report)


def next_point(y: float) -> float:
    return min(1, max(0, y + random.uniform(-0.12, 0.12)))


def classify_span(record: otel_trace.SpanRecord):
    name = otel_trace.session_name(record)
    if name is None or not record.name.startswith("output "):
        return None
    return name, record.name.removeprefix("output ")


async def slow_query():
    """Stand in for a slow database query, and report when it ran."""
    start = time.time()
    await asyncio.sleep(DELAY)
    end = time.time()
    return ui.span(data_start=f"{start:.3f}", data_end=f"{end:.3f}")


def server(input, output, session):
    @reactive.calc
    def user_name():
        query = parse_qs(input[".clientdata_url_search"]().lstrip("?"))
        return query.get("user", [None])[0]

    @reactive.calc
    def is_user_view():
        return user_name() is not None

    @reactive.effect
    def _():
        if is_user_view():
            otel_trace.name_session(session.id, user_name())

    @render.ui
    @reactive.event(input.run)
    async def sales():
        return await slow_query()

    @render.ui
    @reactive.event(input.run)
    async def forecast():
        return await slow_query()

    points = deque([0.5], maxlen=FEED_POINTS)
    for _ in range(FEED_POINTS - 1):
        points.append(next_point(points[-1]))

    @render.ui
    def feed():
        req(is_user_view())
        reactive.invalidate_later(0.2)
        points.append(next_point(points[-1]))
        now = time.strftime("%H:%M:%S") + f".{int(time.time() * 10) % 10}"
        coords = " ".join(f"{i},{20 - 18 * y - 1:.2f}" for i, y in enumerate(points))
        return ui.HTML(
            f'<svg viewBox="0 0 {FEED_POINTS - 1} 20" preserveAspectRatio="none">'
            f'<polyline points="{coords}" fill="none" stroke="#2a78d6" '
            'stroke-width="2" vector-effect="non-scaling-stroke"/></svg>'
            f"<small>Updated {now}</small>"
        )


app = App(app_ui, server)
otel_trace.add_route(app, classify_span)
