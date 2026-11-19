"""
A live view of the OpenTelemetry spans that Shiny emits, for the multi-user demo.

`install()` adds a span processor that keeps recent spans in memory, and
`add_route()` serves them as JSON at "spans". `trace_panel()` draws them in the
browser, one lane per session or output, and polls the route every 0.1s.

The panel fetches spans over plain HTTP instead of through a Shiny output. An
HTTP request does not wait for Shiny's reactive lock, so the view keeps updating
even when the lock blocks every session (before Shiny 1.9), the same as an
external tracing backend.
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass
from typing import Callable

import starlette.routing
from starlette.requests import Request
from starlette.responses import Response

from shiny import App, ui

try:
    from opentelemetry import trace
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import ReadableSpan, Span, SpanProcessor, TracerProvider
except ImportError:
    trace = None

KEEP_SECONDS = 60

# Light-mode categorical slots 1 to 3 of the dataviz reference palette.
KIND_COLORS = ["#2a78d6", "#eb6834", "#1baf7a"]


@dataclass
class SpanRecord:
    name: str
    session: str | None
    start: int
    end: int | None = None


RECORDS: dict[int, SpanRecord] = {}
SESSION_NAMES: dict[str, str] = {}

Classify = Callable[[SpanRecord], "tuple[str, str] | None"]


if trace is not None:

    class RecentSpans(SpanProcessor):
        """Keep each span from its start, so the view can draw spans that are running."""

        def on_start(self, span: Span, parent_context=None) -> None:
            session = (span.attributes or {}).get("session.id")
            if session is None and span.parent is not None:
                parent = RECORDS.get(span.parent.span_id)
                session = parent.session if parent else None
            RECORDS[span.context.span_id] = SpanRecord(
                name=span.name,
                session=str(session) if session is not None else None,
                start=span.start_time or time.time_ns(),
            )

        def on_end(self, span: ReadableSpan) -> None:
            record = RECORDS.get(span.context.span_id)
            if record is not None:
                record.end = span.end_time or time.time_ns()
            cutoff = time.time_ns() - KEEP_SECONDS * 1_000_000_000
            for span_id in [k for k, r in RECORDS.items() if r.end and r.end < cutoff]:
                del RECORDS[span_id]


def install() -> bool:
    """Record Shiny's spans. Returns False when opentelemetry-sdk is missing."""
    if trace is None:
        return False
    provider = trace.get_tracer_provider()
    if not isinstance(provider, TracerProvider):
        # An explicit resource skips resource detection, which fails in Pyodide.
        provider = TracerProvider(resource=Resource({"service.name": "shiny-demo"}))
        trace.set_tracer_provider(provider)
    provider.add_span_processor(RecentSpans())
    return True


def name_session(session_id: str, name: str) -> None:
    SESSION_NAMES[session_id] = name


def session_name(record: SpanRecord) -> str | None:
    return SESSION_NAMES.get(record.session) if record.session else None


def add_route(app: App, classify: Classify) -> None:
    """Serve recent spans at "spans", as seconds relative to now.

    `classify` returns a (lane, kind) pair for each span to draw, or None to skip it.
    """

    async def spans(request: Request) -> Response:
        now = time.time_ns()
        rows = []
        for record in list(RECORDS.values()):
            placed = classify(record)
            if placed is None:
                continue
            lane, kind = placed
            rows.append(
                {
                    "lane": lane,
                    "kind": kind,
                    "start": (record.start - now) / 1e9,
                    "end": None if record.end is None else (record.end - now) / 1e9,
                }
            )
        return Response(json.dumps(rows), media_type="application/json")

    app.starlette_app.router.routes.insert(
        0, starlette.routing.Route("/spans", spans, methods=["GET"])
    )


PANEL_JS = """
(() => {
  const root = document.getElementById("otel-trace");
  const lanes = JSON.parse(root.dataset.lanes);
  const kinds = JSON.parse(root.dataset.kinds);
  const windowSeconds = Number(root.dataset.window);
  const fill = root.dataset.fill === "true";
  const labelWidth = 70, axisHeight = 22;
  const svg = root.querySelector("svg");
  let anchor = null;
  // Pages call this when the user starts a run.
  window.traceAnchor = () => { anchor = performance.now() / 1000; };

  function draw(rows) {
    const width = svg.clientWidth;
    const rowHeight = fill
      ? Math.max(20, (root.clientHeight - axisHeight) / lanes.length)
      : 26;
    const height = lanes.length * rowHeight + axisHeight;
    svg.setAttribute("height", height);
    const plotWidth = width - labelWidth - 12;
    const now = performance.now() / 1000;
    // After a click, pin the axis to the click so new spans appear from left to
    // right. Otherwise, and once the run is past the window, scroll with "now".
    const pinned = anchor !== null && now - anchor < windowSeconds - 1;
    const left = pinned ? anchor - 1 : now - windowSeconds;
    const x = (t) => labelWidth + ((t - left) / windowSeconds) * plotWidth;
    let out = "";
    const origin = pinned ? anchor : now;
    for (let s = pinned ? 0 : -windowSeconds; s <= windowSeconds; s += 2) {
      const t = origin + s;
      if (t < left || t > left + windowSeconds) continue;
      const gx = x(t);
      const label = s === 0 ? (pinned ? "click" : "now") : `${s}s`;
      out += `<line x1="${gx}" x2="${gx}" y1="0" y2="${height - axisHeight}"
        stroke="#e4e3df" stroke-width="1"/>
        <text x="${gx}" y="${height - 6}" text-anchor="middle" font-size="11"
        fill="#52514e">${label}</text>`;
    }
    if (pinned) {
      out += `<line x1="${x(anchor)}" x2="${x(anchor)}" y1="0"
        y2="${height - axisHeight}" stroke="#0b0b0b" stroke-width="1.5"/>`;
    }
    lanes.forEach((lane, i) => {
      out += `<text x="0" y="${i * rowHeight + rowHeight / 2 + 4}" font-size="12"
        fill="#0b0b0b">${lane}</text>`;
    });
    // Draw the kinds listed last first, so the ones listed first stay on top.
    const placed = rows
      .map((row) => ({ ...row, kind: kinds.findIndex((k) => k.kind === row.kind) }))
      .filter((row) => row.kind >= 0 && lanes.includes(row.lane))
      .sort((a, b) => b.kind - a.kind);
    for (const row of placed) {
      const lane = lanes.indexOf(row.lane);
      const kind = kinds[row.kind];
      const start = now + row.start;
      const end = now + (row.end === null ? 0 : row.end);
      if (end < left || start > left + windowSeconds) continue;
      const x0 = x(Math.max(start, left));
      const w = Math.max(2, x(Math.min(end, left + windowSeconds)) - x0);
      const y = lane * rowHeight + kind.band[0] * rowHeight;
      const h = (kind.band[1] - kind.band[0]) * rowHeight;
      out += `<rect x="${x0}" y="${y}" width="${w}" height="${h}" rx="2"
        fill="${kind.color}" ${row.end === null ? 'fill-opacity="0.55"' : ""}/>`;
    }
    svg.innerHTML = out;
  }

  async function tick() {
    try {
      const response = await fetch(root.dataset.url, { cache: "no-store" });
      draw(await response.json());
    } catch (e) {}
    setTimeout(tick, 100);
  }
  tick();
})();
"""


def trace_panel(
    lanes: list[str],
    kinds: dict[str, str | tuple[str, tuple[float, float]]],
    *,
    window_seconds: int = 10,
    fill: bool = False,
    installed: bool = True,
    class_: str | None = None,
):
    """A card that draws the spans from `add_route()`.

    `kinds` maps each kind to its legend label, or to a (label, band) pair, where
    band is the (top, bottom) part of the row's height that its bars cover, from 0
    to 1. With `fill=True`, the rows grow to fill the card.
    """
    if not installed:
        return ui.card(
            ui.card_header("OpenTelemetry spans"),
            ui.p("Install opentelemetry-sdk to see the spans that Shiny emits."),
        )
    kind_list = []
    for i, (kind, spec) in enumerate(kinds.items()):
        label, band = (spec, (0.2, 0.8)) if isinstance(spec, str) else spec
        kind_list.append(
            {"kind": kind, "label": label, "band": band, "color": KIND_COLORS[i]}
        )
    legend = ui.span(
        *[
            ui.span(
                ui.span(
                    style=(
                        f"display: inline-block; width: 12px; height: 12px; "
                        f"border-radius: 2px; background: {k['color']}; "
                        "margin-right: 4px; vertical-align: -1px;"
                    )
                ),
                k["label"],
                class_="me-3",
            )
            for k in kind_list
        ],
        class_="fw-normal small text-body-secondary ms-3",
    )
    return ui.card(
        ui.card_header(
            "OpenTelemetry spans from Shiny (live)", legend
        ),
        ui.div(
            ui.tags.svg(style="width: 100%; display: block;"),
            id="otel-trace",
            data_url="spans",
            data_lanes=json.dumps(lanes),
            data_kinds=json.dumps(kind_list),
            data_window=str(window_seconds),
            data_fill=json.dumps(fill),
            style="flex: 1 1 auto; min-height: 0;" if fill else None,
        ),
        ui.tags.script(PANEL_JS),
        fill=fill,
        class_=class_,
    )
