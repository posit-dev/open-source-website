const {
  React,
  ReactDOM,
  useShinyInput,
  useShinyOutputValue,
  useShinyOutputStatus,
  useShinyInitialized,
} = window.shinyreact;

const h = React.createElement;

// --- histogram chart -------------------------------------------------------

const W = 620;
const H = 380;
const M = { top: 16, right: 16, bottom: 48, left: 56 };
const PLOT_W = W - M.left - M.right;
const PLOT_H = H - M.top - M.bottom;

// Round `max` up to a friendly axis top, using a 1/2/5 × 10^n tick step.
function yTicks(max) {
  const raw = Math.max(max, 1) / 4;
  const mag = Math.pow(10, Math.floor(Math.log10(raw)));
  const step = [1, 2, 5, 10].map((m) => m * mag).find((s) => s >= raw);
  const top = Math.ceil(max / step) * step;
  const ticks = [];
  for (let v = 0; v <= top; v += step) ticks.push(v);
  return { top, ticks };
}

function xTicks(lo, hi) {
  const step = 10;
  const ticks = [];
  for (let v = Math.ceil(lo / step) * step; v <= hi; v += step) ticks.push(v);
  return ticks;
}

function Histogram({ data }) {
  const { breaks, counts } = data;
  const lo = breaks[0];
  const hi = breaks[breaks.length - 1];
  const { top, ticks } = yTicks(Math.max(...counts));

  const x = (v) => M.left + ((v - lo) / (hi - lo)) * PLOT_W;
  const y = (v) => M.top + PLOT_H - (v / top) * PLOT_H;

  return h(
    "svg",
    {
      viewBox: `0 0 ${W} ${H}`,
      width: "100%",
      role: "img",
      "aria-label": `Histogram of Old Faithful waiting times in ${counts.length} bins`,
    },
    // y gridlines + labels
    ticks.map((t) =>
      h(
        "g",
        { key: `y${t}` },
        h("line", {
          x1: M.left,
          x2: M.left + PLOT_W,
          y1: y(t),
          y2: y(t),
          stroke: "#e5e5e5",
        }),
        h(
          "text",
          {
            x: M.left - 10,
            y: y(t),
            textAnchor: "end",
            dominantBaseline: "middle",
            fontSize: 12,
            fill: "#666",
          },
          t,
        ),
      ),
    ),
    // bars
    counts.map((count, i) => {
      const x0 = x(breaks[i]);
      const x1 = x(breaks[i + 1]);
      return h("rect", {
        key: i,
        x: x0,
        width: Math.max(x1 - x0 - 1, 1),
        y: y(count),
        height: M.top + PLOT_H - y(count),
        fill: "#447099",
      });
    }),
    // x axis
    h("line", {
      x1: M.left,
      x2: M.left + PLOT_W,
      y1: M.top + PLOT_H,
      y2: M.top + PLOT_H,
      stroke: "#888",
    }),
    xTicks(lo, hi).map((t) =>
      h(
        "text",
        {
          key: `x${t}`,
          x: x(t),
          y: M.top + PLOT_H + 20,
          textAnchor: "middle",
          fontSize: 12,
          fill: "#666",
        },
        t,
      ),
    ),
    h(
      "text",
      {
        x: M.left + PLOT_W / 2,
        y: H - 8,
        textAnchor: "middle",
        fontSize: 13,
        fill: "#333",
      },
      "Waiting time to next eruption (minutes)",
    ),
    h(
      "text",
      {
        transform: `translate(16 ${M.top + PLOT_H / 2}) rotate(-90)`,
        textAnchor: "middle",
        fontSize: 13,
        fill: "#333",
      },
      "Frequency",
    ),
  );
}

// --- app -------------------------------------------------------------------

function App() {
  const initialized = useShinyInitialized();
  const [bins, setBins] = useShinyInput("bins", 30);
  const data = useShinyOutputValue("dist_data", null);
  const caption = useShinyOutputValue("dist_caption", null);
  const status = useShinyOutputStatus("dist_data");

  if (!initialized) return null;

  return h(
    "main",
    { className: "layout" },
    h(
      "aside",
      { className: "sidebar" },
      h("label", { htmlFor: "bins" }, "Number of bins:"),
      h("input", {
        id: "bins",
        type: "range",
        min: 1,
        max: 50,
        value: bins,
        onChange: (e) => setBins(Number(e.target.value)),
      }),
      h("output", { htmlFor: "bins", className: "bins-value" }, bins),
    ),
    h(
      "section",
      { className: "panel" },
      h("h1", null, "Hello Shiny!"),
      h("p", { className: "caption" }, caption ?? " "),
      // Keep the chart mounted while the server recomputes — only show the
      // placeholder before the first value has ever arrived.
      data
        ? h(
            "div",
            { className: status === "recalculating" ? "recalculating" : "" },
            h(Histogram, { data }),
          )
        : h("div", { className: "placeholder" }, "Loading…"),
    ),
  );
}

// No mount div in the generated page — create the container and append it to <body>.
// The script is deferred, so document.body is parsed by the time this runs.
const root = ReactDOM.createRoot(
  document.body.appendChild(document.createElement("div")),
);
root.render(h(App));
