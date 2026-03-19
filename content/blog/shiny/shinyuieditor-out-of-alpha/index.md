---
title: 'ShinyUiEditor: Out of Alpha'
description: >-
  We're excited to announce that ShinyUiEditor, a drag-and-drop interface for
  building Shiny apps, is officially out of its "alpha" stage.
date: 2023-10-30T00:00:00.000Z
people:
  - Nick Strayer
image: out-of-alpha-main.jpeg
image-alt: Code next to the ShinyUIEditor that generated it
ported_from: shiny
port_status: in-progress
software: ["shinyuieditor", "shiny-r"]
languages: ["R"]
categories:
  - Interactive Apps
---


<style>

.blog-image-container> img {
  /* from openprops */
  --shadow-color: 220 3% 15%;
  --shadow-strength: 1%;
  --inner-shadow-highlight: inset 0 -.5px 0 0 #fff, inset 0 .5px 0 0 #0001;
  
  /* Give the headline image a bit of a shadow to make its boundaries 
     clear from the background which has the same color
  */
  box-shadow: 0 -1px 3px 0 hsl(var(--shadow-color) / calc(var(--shadow-strength) + 2%)),
    0 1px 2px -5px hsl(var(--shadow-color) / calc(var(--shadow-strength) + 2%)),
    0 2px 5px -5px hsl(var(--shadow-color) / calc(var(--shadow-strength) + 4%)),
    0 4px 12px -5px hsl(var(--shadow-color) / calc(var(--shadow-strength) + 5%)),
    0 12px 15px -5px hsl(var(--shadow-color) / calc(var(--shadow-strength) + 7%));
}

.demo-video {
    --video-width: 80%;
    width: var(--video-width);
    margin-block: 2rem;
    margin-inline: calc((100% - var(--video-width))/2);
}

.demo-video> video {
  width: 100%;
}

</style>

## What's New?

We're excited to announce that [ShinyUiEditor,](https://rstudio.github.io/shinyuieditor/) a drag-and-drop interface for building Shiny apps, is officially out of its "alpha" stage. With a year of rigorous development and community feedback behind us, the editor is more robust, feature-rich, and ready for you to try it out!

## The Journey So Far

ShinyUiEditor [debuted at RStudioConf::2022,](https://www.youtube.com/watch?v=UIaigpCAIqE) offering an initial glimpse and hands-on experience for adventurous users. Since then, we have made significant advancements, including the addition of server awareness functionality, and reducing friction for users when adding and updating input and outputs in their apps.

<video autoplay loop muted playsinline>
<source src="synced-ids-small.mp4" type="video/mp4">
Inputs and outputs are synced between the UI and Server code.
</video>
</div>

### New ways of running

We have also introduced two new ways of running the UI editor.

The first is a "static" mode that runs [directly on the editor's website](https://rstudio.github.io/shinyuieditor/live-demo/) with no need to install anything. This eliminates the need for installation and provides copy-and-pastable code for your app once you're done.

The second is a [VSCode extension,](https://marketplace.visualstudio.com/items?itemName=Posit.shinyuieditor) allowing you to open the editor right next to your app's script to instantly see updates.

### Better looking apps

To ensure apps created with the UI editor look great, we have added new bslib components like [value boxes](https://rstudio.github.io/bslib/articles/value-boxes/index.html) and [cards.](https://rstudio.github.io/bslib/articles/cards/index.html)

On the less exciting -- but very important -- front, we have also focused on [bug fixes, stability improvements, and overall performance enhancements.](https://rstudio.github.io/shinyuieditor/change-log/)

<video autoplay loop muted playsinline>
<source src="render-function-cleanup-small.mp4" type="video/mp4">
Now if you delete an element with server bindings, the editor will ask if you want to delete the bindings as well. This results in cleaner app code, especially when starting from a template.
</video>
</div>

## The Road Ahead

Just because we're out of alpha doesn't mean we're done adding features and generally improving the editor. Some upcoming features include exciting components like `bslib::sidebar_layout()` and `bslib::accordian()`, and a greater variety of templates to start from. Keep an eye on the [GitHub repository](https://github.com/rstudio/shinyuieditor) and [editor website](https://rstudio.github.io/shinyuieditor/) to stay up-to-date with the latest.

## We're Listening

Feedback isn't just appreciated---it's crucial. Your insights and suggestions will greatly influence ShinyUiEditor's continued development. Join the conversation through [our Discord channel](https://discord.gg/FNMwts4DsF) or raise an issue on [our GitHub page](https://github.com/rstudio/shinyuieditor/issues).

We can't wait to see what you build!
