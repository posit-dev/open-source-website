---
title: "useR! 2026"
event_type: conference
location: "Warsaw, Poland"
start_date: 2026-07-06
end_date: 2026-07-09
image: user-2026.jpeg
website: https://user2026.r-project.org/
description: "useR! conferences have been the premier global venue for the R community since 2004, bringing together R developers, users, and enthusiasts from around the world."
people:
- Charlie Gao
- Tomasz Kalinowski
software:
- shiny-r
languages:
- R
---

useR! Conference in 2026 is being hosted in Warsaw, bringing together data scientists, statisticians, and researchers from across the world.

Charlie Gao will present on "CRDTs for R: Conflict-Free Data Structures for Real-Time Collaboration".

Description:

Collaborative data analysis presents a fundamental concurrency problem: when multiple users modify the same data simultaneously, how should conflicts be resolved? Traditional approaches rely on locking or central arbitration, but conflict-free replicated data types (CRDTs) offer a principled alternative. A CRDT is a data structure whose concurrent operations are guaranteed to converge to the same state, regardless of the order in which they are applied. This mathematical property — strong eventual consistency — eliminates the need for conflict resolution logic entirely.

We introduce CRDTs to the R ecosystem through automerge, an open-source package developed at Posit that natively bridges R's data model with the Automerge Rust CRDT engine. Collaborative documents — maps, lists, and text — appear as familiar R objects, but every edit is tracked as an individual operation under the hood. When documents are modified concurrently, changes merge automatically.

Beyond real-time document editing, CRDTs open up new possibilities for the R ecosystem: shared annotation of datasets across a research team, collaborative model specification, or any workflow where multiple analysts need to work on the same objects without coordination overhead. We make this concrete with a live demonstration: audience members will open a Shiny application on their own devices and edit shared state together, watching changes from every participant merge seamlessly in real time.

Tomasz Kalinowski will present on mcp-repl.

Description: R is an interactive environment. Working effectively with R means being able to interact with a live session to inspect objects, view and iterate on plots, access help, and step through running code in the debugger. Making LLMs effective in R therefore means more than giving them a way to execute code: it means exposing R’s interactive affordances in a form the model can use.

This talk introduces mcp-repl, an open-source front end to R that plugs into existing agents such as Claude and Codex. It provides a long-lived REPL with persistent state, in-band help, plot capture, support for debugger- and readline-based workflows, guardrails for large outputs, responsive handling of both interactive and long-running computations, and OS-level sandboxing. In practice, mcp-repl makes general-purpose coding agents much more capable at package development, Shiny debugging, and iterative analysis, especially in long-running autonomous tasks without a human in the loop.

Because mcp-repl plugs into existing agents, it also reflects the constraints of a plug-in architecture. To make that contrast concrete, this talk also looks at Posit Assistant as an example of what becomes possible when the interface is integrated into an IDE for data analysis and designed to keep the human in the loop.

Together, Posit Assistant and mcp-repl illustrate two ways to bring R’s interactive affordances to an LLM: one through an integrated experience designed for close human collaboration, the other through a plug-in front end designed for autonomous work in a private runtime.
