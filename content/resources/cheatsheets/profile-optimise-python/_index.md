---
title: Profiling and Optimising in Python
image: page-1.png
resource_type: cheatsheet
by: community
date: '2026-04-01'
description: Measure Python code performance with cProfile and line_profiler, and apply practical optimisation techniques.
download_url: profile_optimise_py.pdf
people:
- Saranjeet Kaur Bhogal
- Jost Migenda
thumbnails:
- page-1.png
languages:
- Python
source_files:
- file: profile_optimise_py.pptx
  format: PowerPoint
---

This cheat sheet covers profiling and optimisation of Python code. It explains when profiling is worthwhile, describes function-level profiling with `cProfile` and line-level profiling with `line_profiler`, and provides practical tips for speeding up Python code including using NumPy, built-in functions, and appropriate data structures.

## What's covered
- Basics – what profiling is and when it is (and is not) needed
- Types of profiling – manual, function-level, line-level, timeline, and hardware-metric profiling
- Function-level profiling – `cProfile` with `python -m cProfile` and `snakeviz` visualization
- Line-level profiling – `line_profiler` with `@profile` decorator and `kernprof`
- Optimisation risks – readability tradeoffs, new bugs, diminishing returns
- Optimisation tips – built-in functions, list comprehensions, NumPy broadcasting, latest Python version, avoid object churn
