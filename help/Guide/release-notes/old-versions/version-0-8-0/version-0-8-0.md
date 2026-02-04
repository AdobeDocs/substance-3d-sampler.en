---
title: "Version 0.8.0"
description: ""
helpx_description: "Sampler > Release Notes > Old Versions > Version 0.8.0"
---

# Version 0.8.0

**Added:**

* &#91;Resources&#93; Connect and mirror your material folders on your local disks
* &#91;Resources&#93; Browse your materials folders and their subfolders
* &#91;Resources&#93; Detach your material resources panel in a separate window to see your resources in full screen
* &#91;Resources&#93; New Resources panel Layout to support folders and subfolders navigation
* &#91;Resources&#93; Use the breadcrum to navigate through your folders
* &#91;Resources&#93; Force the synchronization of your local folder with the Sync option accessible via righ-click
* &#91;Resources&#93; Disconnect your local folder with the Disconnect option accessible via righ-click
* &#91;Manage&#93; Display embedded tags of Substance files
* &#91;Manage&#93; Add, edit and delete tags of your materials
* &#91;Manage&#93; Rate your materials
* &#91;Layers&#93; Support Panorama output
* &#91;Layers&#93; You can delete Image inputs in the Image Import layer
* &#91;Layers&#93; Automatic selection of the new added layer
* &#91;Layers&#93; Automatic selection of the layer below after a layer deletion
* &#91;UX&#93; Keep left panels visibility when switching to another Lab
* &#91;UX&#93; Do not create a base layer or open the Material Workflow popup when importing images in a non-empty layers stack
* &#91;UI&#93; New Textfield style
* &#91;UI&#93; New SearchBox style
* &#91;UI&#93; New Panel header style
* &#91;UI&#93; New Busy indicator style
* &#91;UI&#93; New Layers stack background style
* &#91;UI&#93; Use Adobe Clean font
* &#91;UI&#93; Remove eyedropper icon placeholder of color input parameter
* &#91;Performance&#93; Busy indicator optimization
* &#91;Content&#93; New Pattern Generator filter
* &#91;Content&#93; New Blur filter

**Fixed:**

* &#91;Inspire&#93; Fix crash when using more than 10 colors
* &#91;2D View&#93; Fix scrollbar on the channel list of the 2D view
* &#91;Viewer&#93; Fix crash when importing a non power of 2 environment map
* &#91;Content&#93; Fix PNG import for custom pattern of Embossing and Perforation filters
* &#91;Export&#93; Fix normal and height 16 bits per channel export
* Fix an infinite loop when importing a material with two presets that have the same name
* Fix long file path display in the Base Material Layer

**Known Issues:**

* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Fast visibility toggle of a Delighter stage is not recommended
* Tif images are not showing in Properties panel in the Image import layer
* Coma or point can be ignored when typing a specific value in a slider
* Normal to height filter can crash on MacOS
* Can crash randomly when exiting on MacOS
