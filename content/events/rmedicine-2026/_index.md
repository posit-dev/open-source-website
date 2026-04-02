---
title: "R/Medicine 2026"
event_type: conference
location: "Virtual"
start_date: 2026-05-05
end_date: 2026-05-08
image: rmedicine-2026.jpeg
website: https://rconsortium.github.io/RMedicine_website/
description: "The R/Medicine conference provides a forum for sharing R based tools and approaches used to analyze and gain insights from health data."
people:
- Charlotte Wickham
- François Michonneau
- Sara Altman
software:
- Quarto
languages:
- R
---

The R/Medicine conference provides a forum for sharing R based tools and approaches used to analyze and gain insights from health data.

Charlotte Wickham will be leading a workshop on "Building Accessible, On-Brand Documents with Quarto".

Description: Come see practical strategies for producing Quarto documents that meet organizational standards for both design and accessibility. You’ll learn how to implement consistent organizational branding using brand.yml, plus customization techniques for cases where you need more control. You’ll also learn about recent accessibility improvements for both PDF and HTML outputs.

François Michonneau will be leading a workshop on "Working with Larger than Memory Data in R".

Description: As datasets continue to grow in size and complexity, R users increasingly encounter data that exceeds their system’s memory capacity. This hands-on workshop provides practical strategies for efficiently analyzing larger-than-memory datasets using modern open source tools, with a focus on DuckDB and Apache Arrow—all while maintaining familiar tidyverse workflows.

Participants will learn when and why to move beyond traditional in-memory data frames, and how to choose the right tool for their specific data challenges. Through a combination of presentation and hands-on exercises, we’ll explore how DuckDB enables SQL-based analytics on large datasets without loading them entirely into memory, and how Arrow provides a high-performance columnar data format for efficient data interchange and processing. We’ll also introduce duckplyr, which brings DuckDB’s performance optimizations directly to your existing dplyr code with minimal syntax changes.

The workshop covers essential workflows including reading and querying large CSV and Parquet files, performing aggregations and joins on data that won’t fit in RAM, and leveraging duckplyr to accelerate familiar tidyverse operations on larger datasets. Participants will gain practical experience through real-world examples and learn decision frameworks for selecting appropriate tools based on data size, query patterns, and performance requirements—all without abandoning the tidyverse syntax they already know.

Sara Altman will be presenting a workshop on "LLMs for Data Analysis in R".

Description: LLMs are transforming how we write code, build tools, and analyze data. This workshop will introduce participants to programming with LLM APIs in R using ellmer, an open-source package that makes it easy to work with LLMs from R. We’ll cover the basics of calling LLMs from R, system prompt design, tool calling, and evaluation, and show how to use LLM-powered tools to support common data analysis tasks like exploratory data analysis. Participants will leave with example scripts they can adapt to their own data analysis projects.
