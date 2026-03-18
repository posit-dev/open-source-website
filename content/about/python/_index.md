---
title: "Our Python work"
layout: single
---

From data visualization to web applications, we’re building tools that make Python data science more accessible.

At Posit, we’re committed to advancing Python as a powerful language for data science and technical communication. Our tools are built from the ground up to respect Pythonic idioms and integrate with core libraries like Ibis, polars, scikit-learn, and matplotlib.

\[[Browse all Python packages](/software/?lang=Python&filters=show) \-\>\] \[[Explore learning resources](/resources) \-\>\]

## Featured Python projects

Our most popular Python tools right now, ranked by community adoption and GitHub stars.

{{< query-items path="/software/.*" filter=`{"and": [{"contains_any": [{"var": "languages"}, ["Python"]]}, {"!=": [{"var": "title"}, "Positron"]}]}` sort-by="external.stars" limit="5" cols="5" format="card" hide-badge="true" >}}

<br>
<br>

{{< columns >}}

## A data science IDE built for Python

Positron is a polyglot IDE designed specifically for data science. Built on Code \- OSS, it provides a purpose-built environment for executing Python code in an integrated console, inspecting dataframes and objects via data viewers, and visualizing plots in a dedicated, high-fidelity pane.

\[[Vist the Positron site](https://positron.posit.co/) \-\>\]

---

{{< insert-item item="software/positron" >}}

{{< /columns >}}

<br>

{{< columns >}}

## Familiar concepts, Python-native implementation

We bring proven data science patterns to the Python ecosystem. If you’re a Python-first developer, these tools are built as native Python libraries to fit your existing workflows. If you’re transitioning from R to Python, we provide familiar touchpoints to make your move more productive.

---

{{< insert-items cols="2" format="tile" hide-badge=true >}}
- software/querychat
- software/chatlas
- software/shinychat
- software/orbital
- software/gt-extras
- software/brand-yml
{{< /insert-items>}}

{{< /columns >}}

## Showing up for the Python community

As proud sponsors of the PSF and NumFocus, we're active members of the Python community: sharing our work and learning from yours.

{{< query-items path="/events/.*" filter=`{"contains_any": [{"var": "languages"}, ["Python"]]}` sort-by="date" limit="3" cols="3" format="card" >}}

\[[View all events](/events) \-\>\]
