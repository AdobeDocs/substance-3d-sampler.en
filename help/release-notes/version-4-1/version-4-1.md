---
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/release-notes/version-4-1.html"
breadcrumb-title: ""
description: Review release notes for Substance 3D Sampler version 4.1 to learn about Paint Warp filter, Embroidery filter updates, and 3D Capture improvements.
helpx_creative_field: ""
helpx_description: Sampler > Release Notes > Version 4.1
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Version 4.1
user-guide-description: ""
user-guide-title: ""
---


# Version 4.1

<b>Substance 3D Sampler 4.1.0 </b>introduces new content with the <b>Paint Warp </b>filter and an improved version of the <b>Embroidery </b>filter. This update includes some 3D Capture improvements.

*Release date: 28 March, 2023*

## Paint Warp

The Paint Warp filter lets you warp materials by drawing curves on the 2D view.  
The Straighten option lets you realign materials for an easy seamless tiling workflow.

## Embroidery

The new Embroidery generator lets you create embroidery patches from a single image vector file, or a drawing.  
It can embroider up to 6 colors and combines several stitching technics.

## Tutorials

## Release Note

<b>4.1.2 CANNOLI</b>

*(Released: June 20, 2023)*

<b>Fixed:</b>

* &#91;Layers&#93; Memory leak when tweaking Substance materials and filters causing crashes

<b>4.1.1 CANNOLI</b>

*(Released: June 06, 2023)*

<b>Added</b>:

* &#91;Engine&#93; Update Substance Engine to version 9.0
* &#91;Interoperability&#93; Send 3D Objects to Stager and Painter

<b>Fixed:</b>

* &#91;3D Capture&#93; Applications crashes when 3D Capture renderer fails
* &#91;3D Capture&#93; Crash when an image cannot be loaded
* &#91;3D Capture&#93; Crash when reaching the Mesh Reconstruction step
* &#91;3D Capture&#93; Crash when resizing the bounding box
* &#91;3D Capture&#93; Importing masks following the convention doesn't assign the mask properly
* &#91;3D Capture&#93; Rendering glitches when adjusting the bounding box
* &#91;3D Capture&#93; Switching between version and toggling rendering options during 3D capture post process is slow
* &#91;3D Capture&#93; Switching between versions during 3D Capture Post-Process step is sometimes broken
* &#91;Application&#93; Crash at startup
* &#91;Application&#93; Crash when duplicating a renamed material
* &#91;Application&#93; Crash when opening a legacy .alch project without its dependency folder
* &#91;Application&#93; Crash when plugging/unplugging a screen, computer goes to sleep, or is accessed remotely
* &#91;Application&#93; Crashes and memory leaks related to non-persistent assets management
* &#91;Export&#93; Choosing material format for 3D object file types that embed or reference textures should be disabled
* &#91;Export&#93; Crash if something goes wrong during 3D Object export
* &#91;Export&#93; Crash when exporting a .sbs/.sbsar file
* &#91;Export&#93; Crash when importing custom preset that has the same Label but not the same file name
* &#91;Export&#93; Exporting an environment light to a .sbs/.sbsar file sometimes does not work
* &#91;Export&#93; Gltf/Glb export encodes textures in base64
* &#91;Export&#93; Name text field does not work when refocusing
* &#91;Export&#93; Preserve tiling does not work when exporting an Image to Material (AI Powered) layer to a .sbs/.sbsar file
* &#91;Export&#93; When exporting gltf and replacing files, the list of files to be replaced is not correct
* &#91;Exposed Parameters&#93; Random seed does not work in exported .sbs/.sbsar files
* &#91;Layers&#93; Content-Aware Fill sometimes crashes when added for the second time
* &#91;Layers&#93; Crash when computing a layer stack
* &#91;Layers&#93; Image to Material (AI) disk cache does not work
* &#91;Layers&#93; Possible crash when tweaking a layer
* &#91;Performance&#93; Memory leaks
* &#91;Project&#93; Crash when saving a project
* &#91;Project&#93; Importing the same project twice in a row duplicates assets
* &#91;UI&#93; Rounded buttons with only an icon are not rendered correctly

### 4.1.0 Cannoli

*(Released: March 28, 2023)*

<b>Added:</b>

* &#91;Content&#93; New Embroidery filter
* &#91;Content&#93; New Paint Warp filter
* &#91;UI&#93; Add Export option in File menu
* &#91;3D Capture&#93; Back button is now available on the alignment step
* &#91;3D Capture&#93; Images Handle JPEG EXIF orientation
* &#91;3D Capture&#93; Scripting - New dataset\_info.camera property
* &#91;3D Capture&#93; Add Linux support (see documentation)
* &#91;3D Capture&#93; Verify read access of the imported images
* &#91;Onboarding&#93; Learn - 2 new tutorials (Embroidery and Paint Warp)
* &#91;Onboarding&#93; Updated What's New content

<b>Fixed:</b>

* &#91;3D Capture&#93; Keep camera position when changing version
* &#91;3D Capture&#93; Merge all groups of an object into one
* &#91;3D Capture&#93; Renamed generated meshes into Original
* &#91;Application&#93; Crash when trying to generate thumbnail of a non-existent image
* &#91;Assets&#93; Trash bin icon does nothing in the Assets panel
* &#91;Content&#93; Updating filters with material slots doesn't work as expected
* &#91;Export&#93; Possible crash when exporting an asset with specific filters
* &#91;Export&#93; SBS/SBSAR Export - image import layers had priority over image parameters
* &#91;Export&#93; UE4 Export preset doesn't work with PNG
* &#91;Layers&#93; Crash when dropping a material and a filter at the same time from OS explorer
* &#91;Layers&#93; Crash when dragging any SBSAR file with any image file
* &#91;Layers&#93; Embroidery opacity channel can be completely white
* &#91;Localization&#93; Chinese language may be displayed by default on Linux
* &#91;Performance&#93; Fixed a memory issue when removing a layer from an asset
* &#91;Project&#93; Possible crash when saving
* &#91;UI&#93; Add missing spacing on Version's menu button
* &#91;UI&#93; Cancel button not properly displayed
* &#91;UI&#93; Disable sliders animation for 3D Capture post-process parameters
* &#91;UI&#93; The Material Creation Template window does not close itself when clicking outside
* &#91;UI&#93; The filter quick accessor closes itself when clicking outside

<b>Known Issues:</b>

* &#91;Color Picker&#93; Picking a color on a second monitor with a different resolution may not work
* &#91;Content&#93; Shape light widget is not working in spherical projection mode
* &#91;Interoperability&#93; Material with displacement sent to Stager will lose displacement controls
