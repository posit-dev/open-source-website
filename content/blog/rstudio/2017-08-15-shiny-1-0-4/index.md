---
title: Shiny 1.0.4
people:
  - Winston Chang
date: '2017-08-15'
slug: shiny-1-0-4
categories:
  - Interactive Apps
tags:
  - Packages
  - Shiny
  - RStudio
blogcategories:
  - Products and Technology
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
ported_categories:
  - Packages
  - Shiny
---



<p>Shiny 1.0.4 is now available on CRAN. To install it, run:</p>
<pre class="r"><code>install.packages(&quot;shiny&quot;)</code></pre>
<p>For most Shiny users, the most exciting news is that file inputs now support dragging and dropping:</p>
<p>It is now possible to add and remove tabs from a <code>tabPanel</code>, with the new functions <code>insertTab()</code>, <code>appendTab()</code>, <code>prependTab()</code>, and <code>removeTab()</code>. It is also possible to hide and show tabs with <code>hideTab()</code> and <code>showTab()</code>.</p>
<p>Shiny also has a new a function, <code>onStop()</code>, which registers a callback function that will execute when the application exits. (Note that this is different from the existing <code>onSessionEnded()</code>, which registers a callback that executes when a user’s session ends. An application can serve multiple sessions.) This can be useful for cleaning up resources when an application exits, such as database connections.</p>
<p>This release of Shiny also has many minor new features and bug fixes. For a the full set of changes, see the <a href="https://shiny.rstudio.com/reference/shiny/1.0.4/upgrade.html">changelog</a>.</p>
