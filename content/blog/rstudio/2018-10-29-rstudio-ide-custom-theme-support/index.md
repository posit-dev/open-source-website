---
title: RStudio IDE Custom Theme Support
people:
  - RStudio Team
date: '2018-10-29'
slug: rstudio-ide-custom-theme-support
categories:
- RStudio IDE
tags:
- RStudio
- Themes
- Custom Themes
- RStudio IDE
blogcategories:
- Products and Technology
- Open Source
events: blog
ported_from: rstudio
port_status: raw
---


We're excited to announce that RStudio v1.2 has added support for custom editor themes. Custom editor themes will allow you to adjust the background color of the editor and syntax highlighting of code in RStudio to better suit your own personal style.

New editor themes can be added to RStudio by importing a tmTheme or sharing an existing rstheme file. The tmTheme file format was first introduced for the TextMate editor, and has since become a standard theme format. The rstheme format is specific to RStudio.

## Importing a Custom Theme
Before you can add a theme to RStudio, you'll have to find a theme in the right format. This [online tmTheme editor](https://tmtheme-editor.herokuapp.com) will allow you to create your own tmThemes or download an existing theme from a large collection of themes. If you are interested in writing your own theme be sure to read this [RStudio Extensions article about writing themes](https://rstudio.github.io/rstudio-extensions/rstudio-theme-creation.html).

Once you have a tmTheme or rstheme file for your favorite theme or themes, you can import it to RStudio. Follow the instructions below to import a theme.

1. In the menu bar, open the "Tools" menu.

2. From the drop down menu, choose "Global Options".
<img src="/blog-images/2018-10-29-import-theme-steps-1-and-2.png" align="center"/>

3. In the pane on the left hand side of the options window, click "Appearance".

4. To import a theme, click on the "Add..." button.
<img src="/blog-images/2018-10-29-import-theme-steps-3-and-4.png" align="center"/>

5. In the file browser, navigate to the location where you've saved your theme file.
<img src="/blog-images/2018-10-29-import-theme-step-5.png" align="center"/>

6. If prompted to install R packages, select "Yes".
<img src="/blog-images/2018-10-29-import-theme-step-6.png" align="center"/>

7. You should now see your newly added theme in the list of editor themes. Simply click the "Apply" button to apply your theme to RStudio.
<img src="/blog-images/2018-10-29-import-theme-step-7.png" align="center"/>

<img src="/blog-images/2018-10-29-night-owl.png" align="center"/>

The theme pictured in these examples is called Night Owlish, and was adapted from the Night Owl theme by RStudio's own Mara Averick. It can be found on [her github page](https://github.com/batpigandme/night-owlish).

## Removing a Custom Theme
If you accidentally added a theme, or you want to add an updated version, you can remove the theme from RStudio. To do so, follow the instructions below.

1. As above, navigate to the Appearance Preferences Pane in the Global Options.

2. If the theme you wish to remove is the active theme, be sure to switch to a different theme first.

3. Select the theme you wish to remove from the list of themes and click the "Remove" button.
<img src="/blog-images/2018-10-29-remove-theme-step-1.png" align="center"/>

4. Select "Yes" when prompted for confirmation.
<img src="/blog-images/2018-10-29-remove-theme-step-2.png" align="center"/>

## Sharing Themes
If you've found (or made) a really cool theme that you want to share, you can do so just by sharing the tmTheme or rstheme file. Then the recipient can import it as per the instructions in the [Importing a Custom Theme section](#importing-a-custom-theme). There is no difference between sharing the tmTheme file, or the rstheme file that is generated after the theme gets imported to RStudio, unless you or someone else has made changes to the rstheme file itself.

rstheme files can be found in the `.R` directory under your home directory. On Windows, the path is `C:\Users\<your user account>\Documents\.R\rstudio\themes`. On all other operating systems, the path is `~/.R/rstudio/themes`.

## Some of Our Favorite Themes
To find out more about themes in RStudio, check out this [support article about themes](https://support.rstudio.com/hc/en-us/articles/115011846747-Using-RStudio-Themes). In the meantime, here is RStudio styled using some of our favorite themes:

[Ayu Dark, Light, and Mirage by dempfi](https://github.com/dempfi/ayu):
<img src="/blog-images/2018-10-29-ayu-dark.png" align="center"/>
Ayu Dark

<img src="/blog-images/2018-10-29-ayu-mirage.png" align="center"/>
Ayu Mirage

<img src="/blog-images/2018-10-29-ayu-light.png" align="center"/>
Ayu Light

[Candy Brights](https://tmtheme-editor.herokuapp.com/#!/editor/theme/Candy%20Brights):
<img src="/blog-images/2018-10-29-candy-brights.png" align="center"/>

[Wombat, by randy3k](https://github.com/randy3k/dotfiles/blob/master/.R/rstudio/themes/Wombat.rstheme):
<img src="/blog-images/2018-10-29-wombat.png" align="center"/>

This theme is an example of a theme where the rstheme file was modified directly. Without editing the rstheme file, it wouldn't have been possible to change the style of non-editor elements of RStudio, like the tabs above the different panes. To learn more about creating new custom themes for RStudio, take a look at this [RStudio Extensions article about writing themes](https://rstudio.github.io/rstudio-extensions/rstudio-theme-creation.html).

We look forward to seeing what great new themes the RStudio community comes up with!

You can download the RStudio 1.2 Preview Release at <https://www.rstudio.com/products/rstudio/download/preview/>. If you have any questions or comments, please get in touch with us on the [community forums](https://community.rstudio.com/c/rstudio-ide).

