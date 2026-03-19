---
title: leaflet 2.0.0
people:
  - Barret Schloerke
date: '2018-05-10'
slug: leaflet-2-0-0
# output:
#   blogdown::html_page:
#     mathjax: null
#     self_contained: true
tags:
  - leaflet
  - data visualization
  - Packages
editor_options: 
  chunk_output_type: console
blogcategories:
- Products and Technology
- Open Source
ported_from: rstudio
port_status: in-progress
software: ["leaflet"]
languages: ["R"]
categories:
  - Visualization
  - Interactive Apps
ported_categories:
  - Packages
---



<p><a href="http://rstudio.github.io/leaflet/">leaflet</a> 2.0.0 is now on CRAN!</p>
<p>The leaflet R package wraps the <a href="https://leafletjs.com/">Leaflet.js</a> JavaScript library, and this release of the R package marks a major upgrade from the outdated Leaflet.js 0.7.x to the current Leaflet.js 1.x (specifically, 1.3.1).</p>
<p>Leaflet.js 1.x includes some non-backward-compatible API changes versus 0.7.x. If you’re using only R code to create your Leaflet maps, these changes should not affect you. If you are using custom JavaScript, some changes may be required to your code. Please see the Leaflet.js <a href="http://leafletjs.com/reference-1.3.0.html">reference documentation</a> and <a href="https://github.com/Leaflet/Leaflet/blob/master/CHANGELOG.md">changelog</a>.</p>
<p>Big thanks to <a href="https://twitter.com/timelyportfolio">@timelyportfolio</a> and <a href="https://www.karambelkar.info/about/">Bhaskar Karambelkar</a> for their significant contributions to this release!</p>
<div id="leaflet.extras-and-leaflet.esri" class="section level2">
<h2>leaflet.extras and leaflet.esri</h2>
<p>Two additional packages by Bhaskar, leaflet.extras and leaflet.esri, have been updated on CRAN to utilize the latest Leaflet.js library bindings. leaflet.extras extends the Leaflet R package using various Leaflet.js plugins, offering features like heatmaps, additional marker icons, and drawing tools. leaflet.esri provides access to ArcGIS services, based on the <a href="https://esri.github.io/esri-leaflet/">ESRI leaflet plugin</a>.</p>
<pre class="r"><code>library(leaflet)
library(leaflet.extras)

leaflet(quakes) %&gt;%
  addTiles() %&gt;%
  addHeatmap(lng = ~long, lat = ~lat, radius = 8)</code></pre>
<!-- content of http://rpubs.com/barret/leaflet-2-0-0-quakes of the above code -->
<iframe src="https://rstudio-pubs-static.s3.amazonaws.com/388042_d0a5b2ee3b2d44858e9cfc55edb109bf.html" width="100%" height="400px" frameborder="0">
</iframe>
</div>
<div id="full-changelog" class="section level2">
<h2>Full changelog</h2>
<div id="breaking-changes" class="section level3">
<h3>Breaking Changes</h3>
<ul>
<li>Update to latest Leaflet.js 1.x (v1.3.1). Please see the Leaflet.js <a href="http://leafletjs.com/reference-1.3.0.html">reference documentation</a> and <a href="https://github.com/Leaflet/Leaflet/blob/master/CHANGELOG.md">change log</a>.</li>
<li>Previously, labels were implemented using the 3rd party extension <a href="https://github.com/Leaflet/Leaflet.labelExtension">Leaflet.label</a>. Leaflet.js 1.x now provides this functionality naively. There are some minor differences to note:</li>
<li>If you are using custom JavaScript to create labels, you’ll need to change references to <code>L.Label</code> to <code>L.Tooltip</code>.</li>
<li>Tooltips are now displayed with default Leaflet.js styling.</li>
<li>In custom javascript extensions, change all <code>*.bindLabel()</code> to <code>*.bindTooltip()</code>.</li>
<li>All Leaflet.js plugins updated to versions compatible with Leaflet.js 1.x.</li>
</ul>
</div>
<div id="known-issues" class="section level3">
<h3>Known Issues</h3>
<ul>
<li>The default CSS z-index of the Leaflet map has changed; for some Shiny applications, the map now covers elements that are intended to be displayed on top of the map. This issue has been fixed on GitHub (<code>devtools::install_github(&quot;rstudio/leaflet&quot;)</code>). For now, you can work around this in the CRAN version by including this line in your application UI:</li>
</ul>
<pre class="r"><code>tags$style(&quot;.leaflet-map-pane { z-index: auto; }&quot;)</code></pre>
</div>
<div id="features" class="section level3">
<h3>Features</h3>
<ul>
<li>Added more providers for <code>addProviderTiles()</code>: OpenStreetMap.CH, OpenInfraMap, OpenInfraMap.Power, OpenInfraMap.Telecom, OpenInfraMap.Petroleum, OpenInfraMap.Water, OpenPtMap, OpenRailwayMap, OpenFireMap, SafeCast.</li>
<li>Add <code>groupOptions</code> function. Currently the only option is letting you specify zoom levels at which a group should be visible.</li>
<li>Added support for drag events.</li>
<li>Added <code>method</code> argument to <code>addRasterImage()</code> to enable nearest neighbor interpolation when projecting categorical rasters.</li>
<li>Added an <code>'auto'</code> method for <code>addRasterImage()</code>. Projected factor results are coerced into factors.</li>
<li>Added <code>data</code> parameter to remaining <code>addXXX()</code> methods, including addLegend.</li>
<li>Added <code>preferCanvas</code> argument to <code>leafletOptions()</code>. ### Bug Fixes and Improvements</li>
<li>Relative protocols are used where possible when adding tiles. In RStudio 1.1.x on linux and windows, a known issue of ‘<a href="https://" class="uri">https://</a>’ routes fail to load, but works within browsers (rstudio/rstudio#2661).</li>
<li><code>L.multiPolyline</code> was absorbed into <code>L.polyline</code>, which also accepts an <a href="http://leafletjs.com/reference-1.3.0.html#polyline">array of polyline information</a>.</li>
<li>Fixed bug where icons were anchored to the top-center by default, not center-center.</li>
<li>Fixed bug where markers would not appear in self contained knitr files.</li>
<li><code>L.Label</code> is now <code>L.tooltip</code> in Leaflet.js. <code>labelOptions()</code> now translates old options <code>clickable</code> to <code>interactive</code> and <code>noHide</code> to <code>permanent</code>.</li>
<li>Fix a bug where the default <code>addTiles()</code> would not work with .html files served directly from the filesystem.</li>
<li>Fix bug with accessing columns in formulas when the data source is a Crosstalk SharedData object wrapping a spatial data frame or sf object.</li>
<li>Fix strange wrapping behavior for legend, especially common for Chrome when browser zoom level is not 100%.</li>
<li>Fix incorrect opacity on NA entry in legend.</li>
<li>Ensure type safety of <code>.indexOf(stamp)</code>.</li>
<li><code>validateCoords()</code> warns on invalid polygon data.</li>
</ul>
</div>
</div>
