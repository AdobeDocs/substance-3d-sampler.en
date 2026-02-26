---
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/release-notes/old-versions/version-0-7-0.html"
breadcrumb-title: ""
description: Review release notes for Substance 3D Sampler version 0.7.0 to learn about updates, improvements, and bug fixes.
helpx_creative_field: ""
helpx_description: Sampler > Release Notes > Old Versions > Version 0.7.0
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Version 0.7.0
user-guide-description: ""
user-guide-title: ""
---


# Version 0.7.0

Release date: **2019/06/13**   
  
Added:

* &#91;Filters&#93; Access quickly to your filters by pressing the space bar
* &#91;Filters&#93; New dedicated panel to manage, browse and import your filters
* &#91;Metadata&#93; Right click on a material to see its metadata
* &#91;Metadata&#93; Right click on a material to see its location on your disk
* &#91;Sliders&#93; Animate sliders when you hover them by pressing Ctrl
* &#91;Sliders&#93; Stop and restart your sliders animation by pressing P
* &#91;Export&#93; SBSAR export follows Substance Source guidelines
* &#91;License&#93; Activate Substance Alchemist using an environment variable
* &#91;UX&#93; File dialog remembers the last file path selected
* &#91;UX&#93; Folder dialog remembers the last folder path selected
* &#91;UI&#93; Update Resources panel UI
* &#91;UI&#93; Update Search bar UI
* &#91;UI&#93; Create New material icon is updated
* &#91;Help&#93; URLs are updated to [substance3d.com](http://substance3d.com) domain
* &#91;Mesh&#93; A Cloth mesh is now available
* &#91;Content&#93; New Corrosion Filter
* &#91;Content&#93; New Oxydation Filter
* &#91;Content&#93; New Moss Filter
* &#91;Content&#93; New Dust Filter
* &#91;Content&#93; New Brickwall pattern Filter
* &#91;Content&#93; New Stonewall pattern Filter
* &#91;Content&#93; New Wood Finish Filter
* &#91;Content&#93; New Metal Finish Filter
* &#91;Content&#93; New Snow Filter
* &#91;Content&#93; New Randomizer Filter
* &#91;Content&#93; You can now import your textures directly in the Base Material filter

Fixed:

* Fix a crash when saving the layer stack
* Possible to add a value above 1 in the environment rotation slider
* Do not lose blend parameters when a blend layer is transformed back and forth from blend layer to material layer
* Fix duplicates when generating variations of the same layer stack multiple times
* When re-opening a material, Alchemist remembers the modified ranges (min and max) of your sliders

Known Issues:

* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Fast visibility toggle of a Delighter stage is not recommended
* Custom Environment Import can become black
* Tif images are not showing in Properties panel in the Image import layer
* Coma or point can be ignored when typing a specific value in a slider
* Normal to height filter can crash on MacOS
