---
description: Review release notes for Substance 3D Sampler version 6.1 to learn about new features, improvements, and workflow enhancements.
title: Version 6.1
hold:true
---

# Version 6.1

Kouign amann

![alt text](Sampler_splash_large.jpg)

This release introduces Performance mode, giving anyone the ability to turn off settings that can slow down their workflow, and automatic stability improvements that protect users on lighter hardware.

The main new features include:

## Performance mode

Get a faster, more responsive experience in Sampler. New **Performance mode** brings together every setting that can slow down your workflow: resolution limits, shadows, displacement quality, and path tracing. Turn off features you don't need to improve performance and responsiveness.

More info [*here*](https://www.adobe.com/go/substance-3d-sampler-6.1-performance-mode)

![](../assets/v6.1/6_1-Performance_Mode.png)

## Improved support for minimum spec machines

If your hardware falls below the [minimum specs](../getting-started/system-requirements.md), Sampler now automatically adjusts to keep things stable. The features most likely to slow things down or cause a crash are automatically turned off.

More info [*here*](https://www.adobe.com/go/substance-3d-sampler-6.1-low-specs-mode)

![](../assets/v6.1/6_1-Checked.png)

## V6.1 Release Notes

*(Released: November 19th, 2026)*

## Added

* &lbrack;Application&rbrack; New way to report minimal hardware requirements warnings
* &lbrack;Captis&rbrack; Add an option to choose between 4 and 8 polarization angles
* &lbrack;Captis&rbrack; New Captis quick action
* &lbrack;Export&rbrack; Properly report export failures to user
* &lbrack;Export&rbrack; Update Unreal Engine 4 export preset (renamed to Unreal Engine 5)
* &lbrack;Performance&rbrack; Asset creation from file is now asynchronous
* &lbrack;Performance&rbrack; Move workload from main thread to worker threads
* &lbrack;Performance&rbrack; New performance mode
* &lbrack;Project&rbrack; Warn user if project save failed
* &lbrack;Scripting&rbrack; New generate_thumbnail method for assets and new type property for resources
* &lbrack;Scripting&rbrack; Render a 3D view snapshot to file from the Python module
* &lbrack;UI&rbrack; Clicking anywhere on a drop zone opens the file dialog
* &lbrack;UI&rbrack; Left navigation bar shortcuts to tools (equalize, crop, tiling, transform, repair, color, ...)
* &lbrack;UI&rbrack; Upgrade qt-spectrum to get the latest icons

## Fixed

* &lbrack;3D View&rbrack; Fix immediate UV offset and rotation, remove normal scale for OpenPBR
* &lbrack;3D View&rbrack; Prevent a crash by ensuring no stage edit happens while the viewport is deleted
* &lbrack;3D View&rbrack; Properly remove displacement (height) info when changing the displayed asset
* &lbrack;3D View&rbrack; Properly update document when deleting mesh
* &lbrack;Application&rbrack; Ensure surface stays alive when computing dynamic filter debug info
* &lbrack;Application&rbrack; Fix crash at exit in Scene
* &lbrack;Application&rbrack; Fix potential crash when deleting an asset while the asset database service is shutting down
* &lbrack;Application&rbrack; Make cache debug info thread safe to prevent a crash
* &lbrack;Application&rbrack; Prevent a crash by testing node is not null before accessing it
* &lbrack;Application&rbrack; Prevent a crash caused by accessing the first element of an empty vector
* &lbrack;Application&rbrack; Prevent a crash in invalidateVisibleIfs
* &lbrack;Application&rbrack; Prevent a crash when creating assets while the database service is shut down
* &lbrack;Application&rbrack; Prevent race condition at exit
* &lbrack;Assets&rbrack; Ensure resources are properly secured behind the right lock
* &lbrack;Captis&rbrack; Bug with intensity value in manual mode
* &lbrack;Captis&rbrack; Prevent the user from selecting a zone larger than the backend allows
* &lbrack;Channel Settings&rbrack; Double occurrence of SpecularColor in ASM
* &lbrack;Channel Settings&rbrack; Fix the id of a usage created from a string
* &lbrack;Content&rbrack; Atlas Scatter opacity issue
* &lbrack;Content&rbrack; Embroidery filter is missing metallic feature
* &lbrack;Content&rbrack; Fix Perforation filter
* &lbrack;Content&rbrack; Fix category of Stylization filter and few fixes in resources panel
* &lbrack;Content&rbrack; Update Fill filter
* &lbrack;Creative Cloud&rbrack; Fix path to 3D assets in Creative Cloud
* &lbrack;Engine&rbrack; Prevent a crash when accessing engine data while the job has been cancelled
* &lbrack;Export&rbrack; Add defensive code to check structure's tree is not null
* &lbrack;Export&rbrack; Defensive code to avoid crashes in SBS generation
* &lbrack;Export&rbrack; Enable outputting custom usages, even if they are known by the engine
* &lbrack;Export&rbrack; Fix export presets
* &lbrack;Export&rbrack; Normal maps are exported as raw in USD
* &lbrack;Export&rbrack; Use output labels instead of usages when exporting with a preset
* &lbrack;Exposed Parameters&rbrack; Fix exposed parameters on dynamic filters
* &lbrack;Exposed Parameters&rbrack; Fix update of exposed parameter when its name changes
* &lbrack;Filters&rbrack; Ensure dynamic filters tweaks identifiers are identical between every run on every platform
* &lbrack;Filters&rbrack; Hide unsupported usages in AutoTiling map selection
* &lbrack;Layers&rbrack; Changing layer visibility always recreates structures
* &lbrack;Layers&rbrack; Crash when flattening a Clone Stamp over something
* &lbrack;Layers&rbrack; Inserting a generator directly on the stack now properly sets tweaks and node name
* &lbrack;Layers&rbrack; Inserting a generator with Fill properly displays the texture in the picker
* &lbrack;Localization&rbrack; Fix Chinese charset compliance to GB18030
* &lbrack;Project&rbrack; Crash when saving after painting on a Clone Stamp
* &lbrack;Project&rbrack; Ensure session and project names are actually saved
* &lbrack;Project&rbrack; Prevent a crash when saving a tree
* &lbrack;Project&rbrack; Restoring a corrupted project from database is back
* &lbrack;Quick Actions&rbrack; Display the image selection popup when there is no image in the stack
* &lbrack;Quick Actions&rbrack; Fix quick actions problems; cancelling a quick action no longer closes quick start
* &lbrack;Quick Actions&rbrack; Import textures asks to enable some channels and should not
* &lbrack;Quick Actions&rbrack; Prevent a crash if a quick action fails to load
* &lbrack;Quick Actions&rbrack; Update quick actions content
* &lbrack;Rendering&rbrack; Fix combineNormalAndHeight for ASM materials
* &lbrack;Rendering&rbrack; Fix usages of displayable textures with Vulkan
* &lbrack;Rendering&rbrack; Mark tree dirty when unique usage output changed
* &lbrack;Rendering&rbrack; Use the correct reference structure to compute the tree nodes to be computed
* &lbrack;Scripting&rbrack; Do not stall if something goes wrong during an export
* &lbrack;Scripting&rbrack; Ensure import_images() returns the imported layer
* &lbrack;Scripting&rbrack; Setting an image tweak to an image asset reference fails
* &lbrack;Scripting&rbrack; get_filters() does not return dynamic filters
* &lbrack;Thumbnail&rbrack; Fix potential crashes when generating thumbnail
* &lbrack;Thumbnail&rbrack; Recreate the thumbnail generator when layout changes
* &lbrack;UI&rbrack; Changing asset could set height scale to slider max value
* &lbrack;UI&rbrack; Drawing in a texture updates the texture picker in real time
* &lbrack;UI&rbrack; Entering fullscreen mode while not maximized now fills the entire window
* &lbrack;UI&rbrack; Fix broken link to Substance Magazine
* &lbrack;UI&rbrack; Fix export popup margins
* &lbrack;UI&rbrack; Fix section title size
* &lbrack;UI&rbrack; Fix typo in a string
* &lbrack;UI&rbrack; Linux file dialog now uses GTK plugin
* &lbrack;UI&rbrack; Prevent crash when displaying an emoji
* &lbrack;UI&rbrack; Rename .ssa files as 'Adobe Substance 3D Sampler archive' (without version or Beta)
* &lbrack;UI&rbrack; Restore flickable deceleration when using mouse
* &lbrack;UI&rbrack; Small fixes in 'Create new material' dialog