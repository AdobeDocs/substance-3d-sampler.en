---
title: "All Changes | Substance 3D Sampler"
description: "Sampler > Release Notes > All Changes"
---

# All Changes

This page regroups all the changes that happened to Substance 3D Sampler, from new features to bug fixes.

## Version 5

<b>5.1.3 ÎLE FLOTTANTE</b>

*(Released: January 6, 2026)*

### <b>Added:</b>

* &#91;Captis&#93; Display a warning if the FTP protocol is disabled by the firewall

#### Fixed:

* &#91;Captis&#93; Aborting during a capture can lead to errors
* &#91;Captis&#93; Downloading the results at the end of a capture uses to much RAM
* &#91;Captis&#93; Executing an auto-focus immediately after an auto-intensity can lead to errors
* &#91;Captis&#93; The display of HDR results in the Summary panel
* &#91;UI&#93; In some cases, the folder dialog on MacOS does not select the right folder

<b>5.1.2 ÎLE FLOTTANTE</b>

*(Released: November 20th, 2025)*

#### <b>Added:</b>

* &#91;Application&#93; Detect graphics device loss, warn the user and exit gracefully
* &#91;Layers&#93; Improved messaging when flattening layers
* &#91;Layers&#93; Improved thumbnails for Image Import and Flattened Layers layers
* &#91;Onboarding&#93; Updated learning content on the Home screen
* &#91;Project&#93; Recover last saved state of session before crash
* &#91;UI&#93; Application icon update

#### Fixed:

* &#91;Application&#93; Inserting a material in the layer stack might lead to a crash on macOS
* &#91;Application&#93; Possible crash on heavy load on macOS
* &#91;Application&#93; Possible crash when adding layers when video memory is full
* &#91;Application&#93; Possible crash when opening a project
* &#91;Captis&#93; Failure if auto focus is run shortly after automatic intensity calibration
* &#91;Captis&#93; Reliability and performance issues after first capture
* &#91;Captis&#93; Slowdowns and errors when copying files at the end of a capture
* &#91;Captis&#93; Small memory leak when querying Captis device information
* &#91;Export&#93; Multi slider exposed parameters produce corrupted .sbsar files
* &#91;Layers&#93; Auto tiling pattern is reset to default values when switching assets
* &#91;Layers&#93; Default custom base color is displayed red
* &#91;Layers&#93; Partial flattening of Clone Stamp child layers is possible and causes rendering issues
* &#91;Layers&#93; Possible crash when tweaking a layer stack while rendering is in progress
* &#91;Layers&#93; Unexpected error in auto tiling region of interest step when changing source channels
* &#91;Project&#93; Incorrect thumbnail sometimes when creating a new material
* &#91;Quick Actions&#93; Some quick actions have a wrong input count
* &#91;UI&#93; Action group button have different widths
* &#91;UI&#93; Clear button in text fields sometimes triggers focus loss
* &#91;UI&#93; Combo boxes and text fields are too big
* &#91;UI&#93; Icons and labels are misaligned
* &#91;UI&#93; Name field label is incorrectly placed
* &#91;UI&#93; Quick Actions button labels are misaligned
* &#91;UI&#93; Sliders show too wany trailing 0s

#### Removed:

* &#91;Generative AI&#93; Generative AI features removal

<b>5.1.1 ÎLE FLOTTANTE</b>

*(Released: September 18th, 2025)*

#### <b>Added:</b>

* &#91;2D View&#93; Be able to zoom out more in the 2D view for high resolution textures
* &#91;Captis&#93; Warn users about issues when copying files
* &#91;Layers&#93; When duplicating a layer, use an incremental number in the new layer name

#### Fixed:

* &#91;2D View&#93; When painting strokes after resetting all the properties of Clone Stamp, previously created strokes reappear
* &#91;Application&#93; "Save current project?" popup uses wrong project name
* &#91;Application&#93; Crash at exit
* &#91;Application&#93; Potential crash
* &#91;Application&#93; Sometimes, a thumbnail is generated with an incorrect material
* &#91;Captis&#93; On some devices, when performing a scan in high resolution, the height map is black
* &#91;Captis&#93; The "Start capture" button is not disabled anymore when no capture name is set and when a calibration is running
* &#91;Export&#93; When exporting a .sbsar file the export can fail without the user being notified
* &#91;Filters&#93; Advanced parameters screen for the Auto Tiling filter sometimes flicker when tweaking parameters
* &#91;Filters&#93; Default parameters for the Tiling filter produce gray artifacts in the output
* &#91;Filters&#93; Sometimes with high resolution inputs, the Auto Tiling filter advanced settings do not show the individual pattern points
* &#91;Filters&#93; The pattern size for the custom size Auto Tiling parameter has an incorrect default value
* &#91;Layers&#93; Occasional color issue with the Auto Tiling filter mostly visible on red materials
* &#91;Layers&#93; Sometimes adding layers will reset some tweaks to their default value
* &#91;Physical Size&#93; Thumbnail of assets with a physical size have a wrong height scale
* &#91;UI&#93; Cannot rename exposed parameters
* &#91;UI&#93; Channel activation button are not square
* &#91;UI&#93; If a slider label is too long, the reset button is not accessible
* &#91;UI&#93; Pressing the return key or clicking out does not remove the focus from text fields
* &#91;UI&#93; Sometimes an unwanted tooltip appears in the Physical Size panel
* &#91;UI&#93; The 3D view displays an incorrect mesh when creating an empty project
* &#91;UI&#93; When exposing a color picker input, its label disappears on hover
* &#91;UI&#93; When exposing parameters, the color dot is sometimes incorrectly positioned

<b>5.1.0 ÎLE FLOTTANTE</b>

*(Released: August 7th, 2025)*

#### <b>Added:</b>

* &#91;2D View&#93; Brush size now adapts to the current texture resolution
* &#91;3D View&#93; Toggle Native Display Scale for 3D Rendering in the preferences
* &#91;Application&#93; Rendering engine update
* &#91;Captis&#93; Add "make square" possibility during preview
* &#91;Captis&#93; Automatic physical size detection
* &#91;Captis&#93; Capturing a new material will create a new asset
* &#91;Captis&#93; Change resolution selection in dropdown to pixel per inch or centimetre instead of pixel resolution of maximum area
* &#91;Captis&#93; Contextual help on alignment calibration
* &#91;Captis&#93; Generate roughness map
* &#91;Captis&#93; Warn the user if the default calibration files are missing
* &#91;Filters&#93; Auto Tiling filter for structured materials and scans
* &#91;Filters&#93; New Fold Remover filter
* &#91;Filters&#93; New features within the Clone Stamp filter
* &#91;Filters&#93; New features within the Equalize filter
* &#91;Layers&#93; Ability to flatten layers
* &#91;Layers&#93; Context menu when right-clicking on a layer to rename, duplicate, delete or flatten the layer
* &#91;Onboarding&#93; Update Welcome and What's New screens content
* &#91;Performance&#93; Better performance when using the Crop filter
* &#91;Performance&#93; Improve memory usage for the 3D View
* &#91;Performance&#93; Updating the 3D view is quicker
* &#91;Physical Size&#93; Enable "display with physical ratio" when working on Substance filters when Physical Size is enabled
* &#91;Physical Size&#93; When importing images in an empty stack, propose a resolution that is more coherent with the image ratio
* &#91;Quick Actions&#93; 3 new quick actions for scan processing
* &#91;Scripting&#93; API to flatten layers
* &#91;Scripting&#93; Get the filename of each image of an image import layer
* &#91;Scripting&#93; New function to activate/deactivate a given channel of an asset
* &#91;UI&#93; Rework icons and buttons in the Layers panel to accommodate for the new features
* &#91;UI&#93; Warn about environment light authoring deprecation

#### Fixed:

* &#91;2D View&#93; Selecting 'display with physical ratio' might not work when using Substance filters
* &#91;3D Capture&#93; Svg files are listed in the file picker but not supported
* &#91;3D View&#93; Emission intensity parameter in the Shader Settings does not work
* &#91;3D View&#93; Sometimes the mesh position is incorrect when creating a new asset
* &#91;3D View&#93; Switching to Path Tracing rendering crashes on unsupported hardware
* &#91;Application&#93; Application hangs when closing the manual measure popup without setting a size
* &#91;Application&#93; Crash
* &#91;Application&#93; Freeze on Windows when displaying the desktop (Windows key + D keyboard shortcut)
* &#91;Application&#93; Possible crash when switching language
* &#91;Captis&#93; Crash when the preview data is not valid
* &#91;Captis&#93; Impossible to fully zoom out after zooming in
* &#91;Captis&#93; Missing localization on some wizard steps
* &#91;Captis&#93; Possible crash at exit when using Captis
* &#91;Captis&#93; Scanning does not work if the device is missing calibration files
* &#91;Filters&#93; Brush preview when using the Clone Stamp filter may be wrong depending on the texture and brush sizes
* &#91;Filters&#93; Erroneous output size after using the Upscale filter
* &#91;Filters&#93; Missing icons for Environment Rotation and Stylization filters
* &#91;Filters&#93; Updating some filters may lead to incorrect rendering
* &#91;Layers&#93; Incorrect first render when blending two materials
* &#91;Layers&#93; The button to update layers shows "Update All" even when there is only one update
* &#91;Layers&#93; Unnecessary computations when importing images in the layer stack
* &#91;Performance&#93; Improve normal map format handling to reduce rendering times
* &#91;Physical Size&#93; Manual measurement popup only works after doing an auto-measure
* &#91;Physical Size&#93; Wrong export resolution in the Export popup when Physical Size is enabled
* &#91;Quick Actions&#93; Missing localization on generated asset names
* &#91;UI&#93; Asset preview on hover may not show
* &#91;UI&#93; Clicking the Reset to default value button might break some of the controls
* &#91;UI&#93; Error messages are not cleared when switching projects
* &#91;UI&#93; Make sure material name in viewport &amp; properties panel are empty when there is no asset
* &#91;UI&#93; Reset to default value button for the Point of View parameter does not work
* &#91;UI&#93; Reset to default value button overlap
* &#91;UI&#93; Some buttons are not clickable when a panel is undocked
* &#91;UI&#93; Texture tilling V Parameter partially hidden in Viewer Settings and 3D View

#### Removed:

* &#91;3D Capture&#93; Remove 3D Capture support
* &#91;Application&#93; Remove macOS x86 support

<b>5.0.3 HAZELNUT</b>

*(Released: Jun 3rd, 2025)*

<b>Added:</b>

* &#91;Captis&#93; Allow to give a material same name as an already existing one
* &#91;Captis&#93; Move error messages to popups instead of toasts
* &#91;Filters&#93; Update embroidery
* &#91;Preferences&#93; Add reset in viewer settings and shaders settings
* &#91;UI&#93; Do not present the 'Show location' menu item on project assets

<b>Fixed:</b>

* &#91;3D Capture&#93; Mesh post process filter doesn't output expected maps
* &#91;3D View&#93; 3D view does not work because of shader cache corruption
* &#91;3D View&#93; Ground plane and grid are vertical when scene is Z-up
* &#91;3D View&#93; The mesh sometimes disappears
* &#91;Application&#93; Closing login window at start-up without logging in sometimes crashes the app
* &#91;Application&#93; Crash when access to the plugins configuration file is denied
* &#91;Application&#93; Current material is un-selected when the project is saved
* &#91;Application&#93; Resetting to default layout sets the resolution to 64x64
* &#91;Application&#93; Sampler sometimes crashes when rendering a layer stack
* &#91;Export&#93; Export resolution is sometimes reset to 64x64
* &#91;Export&#93; It is sometimes not possible to export .sbs/.sbsar files
* &#91;Layers&#93; Add base material button does nothing when the material is empty
* &#91;Layers&#93; Texture tiling is changed when duplicating a material
* &#91;Physical Size&#93; Auto-measure does not work if the Physical Size panel was docked before importing the image
* &#91;Scripting&#93; Autosave plugin is broken
* &#91;UI&#93; Incorrect spacing in the Export dialog
* &#91;UI&#93; Slider animation of tweaks does not work anymore
* &#91;UI&#93; Sliders don't snap to integer values when needed
* &#91;UI&#93; Some drop down menus are cropped

<b>5.0.2 HAZELNUT</b>

*(Released: April 22th, 2025)*

<b>Fixed:</b>

* &#91;Application&#93; Back button on the Homepage is broken
* &#91;Application&#93; Sampler sometimes won't launch if corrupted data from previous versions is present on disk
* &#91;Application&#93; The image imported does not appear in the viewport or the layer stack
* &#91;Captis&#93; Captis IP address field remains empty even after restarting Sampler
* &#91;Captis&#93; Live camera preview only works when application language is set to English
* &#91;Export&#93; Crash during export &#91;Layers&#93; Painting sometimes does not work in previously saved projects
* &#91;Layers&#93; Sampler sometimes updates all textures when only one channel is updated
* &#91;Layers&#93; Unable to use material blends in the layer stack after upgrading to 5.0.x
* &#91;Layers&#93; Updating a project with an previous Image to Material (AI) version makes material all black
* &#91;Layers&#93; When trying to import an unsupported image, Sampler creates a broken layer
* &#91;Scripting&#93; Part of the Python API does not work with an empty project
* &#91;UI&#93; Menu items sometimes overflow in the File menu

<b>5.0.1 HAZELNUT</b>

*(Released: March 20th, 2025)*

<b>Added</b>:



* &#91;Application&#93; Updated graphics driver compatibility list
* &#91;Captis&#93; Show a popup when usage of HP Z Captis is blocked by operating system policies
* &#91;Quick Actions&#93; Explain why a Quick Action is disabled in a tooltip
* &#91;UI&#93; Crash report window UI styling
* &#91;UI&#93; When copying to clipboard, show a toast to say it is done

<b>Fixed:</b>

* &#91;2D View&#93; Exposure slider has no effect when spherical projection is off
* &#91;2D View&#93; Painting outside of the texture creates a discontinued stroke
* &#91;2D View&#93; The exposure button has no tooltip
* &#91;2D View&#93; Zooming on the side of a non square image does not follow the mouse
* &#91;3D Capture&#93; 3D Capture does not work on Windows 11 24H2
* &#91;3D Capture&#93; Crash if we quit Sampler during the mesh reconstruction step
* &#91;3D View&#93; Compute time is sometimes shown as 0ms
* &#91;3D View&#93; When changing projection from orthographic to perspective, viewport becomes grey
* &#91;Application&#93; Crash at startup when checking GPU capabilities
* &#91;Application&#93; Crash during install
* &#91;Application&#93; Crash on exit after right-clicking a metadata field
* &#91;Application&#93; Environment light missing when opening an SBSAR from the operating system file explorer
* &#91;Application&#93; Opening a .sbsar while Sampler is running changes the Texture Tiling setting
* &#91;Captis&#93; Some metadata might not transfer between the capture steps
* &#91;Captis&#93; The name of the created asset is not the one entered in the metadata field
* &#91;Content&#93; Sample project prompts for a filter update but is already up to date
* &#91;Filters&#93; Normal/height adjustment filter has no icon
* &#91;Layers&#93; Cannot change images in an image import layer
* &#91;Layers&#93; Crashes when using the Upscale filter
* &#91;Layers&#93; Updating a project with an old Image to Material makes the material all black
* &#91;Rendering&#93; Tweaking a layer stack immediatly after creating an asset breaks the rendering
* &#91;Scripting&#93; The Autosave pluging crashes when there is no asset in the project
* &#91;Tools&#93; Brush size value is missing in the Brush Toolbar
* &#91;UI&#93; Changing the application language doesn't update some of the labels in the Home Screen
* &#91;UI&#93; Hitting Escape or Enter in Slider text fields won’t lose focus
* &#91;UI&#93; In the Properties panel, the reset all button and the asset name label overlap
* &#91;UI&#93; Issues when docking and undocking panels
* &#91;UI&#93; Scrolling in an overlay panel will also scroll in the underlying window
* &#91;UI&#93; Switching to List view in the Recent Projects section of the Home Screen does not work
* &#91;UI&#93; Viewport display mode button icon always shows 2D/3D

<b>5.0.0 HAZELNUT</b>

*(Released: February 20th, 2025)*

<b>Added</b>:



* &#91;Onboarding&#93; New Homepage with quick access to learning content, sample project, quick actions and recent projects.
* &#91;Onboarding&#93; Get started quickly with the new Quick Actions, accessible from the homepage and from dedicated panel
* &#91;Onboarding&#93; &#91;Content&#93; Quick Actions are predefined workflows that populate the layer stack with most used layers
* &#91;Onboarding&#93; Possibility to create a new project via a new Quick start menu, via quick actions or Custom Project
* &#91;Onboarding&#93; Possibility to create empty project directly from homepage via dedicated button
* &#91;3D View&#93; New advanced rasterizer and pathtracer bringing new rendering capabilites (properties such as coating, sheen, translucency, subsurface scattering) and visual consistency across Substance ecosystem
* &#91;3D View&#93; Viewer settings are now accessible directly in the 3D view
* &#91;3D View&#93; Possibility to save a render snapshot in clipboard or in files
* &#91;3D View&#93; Display a grid to visualize the scene origin
* &#91;3D View&#93; Enable the ground plane to catch shadows and reflections
* &#91;3D View&#93; Control how reflective and opaque is your ground plane
* &#91;3D Capture&#93; Position mesh on ground
* &#91;Application&#93; Check hardware compatibility on application startup
* &#91;Application&#93; Crash reporting window now opens right after a crash occurs
* &#91;Content&#93; Open a sample project to easily get started
* &#91;Export&#93; Export Adobe Standard Material shader in USD files
* &#91;Generative AI&#93; Check "Do not infer" tag when using image as an input in Image to Texture workflows
* &#91;Project&#93; Thumbnails are stored within the project file for faster opening of projects
* &#91;Project&#93; Setting in the preferences to store cache data within the project file, with different modes (no cache, light cache, full cache)
* &#91;Scripting&#93; &#91;Breaking change&#93; Qt migration to Qt6.15 - impact compatibility of existing plugins
* &#91;Scripting&#93; Default plugins and script folder are now in the Documents folder
* &#91;Scripting&#93; New UI for plugins for visual consistency with main Sampler panels
* &#91;Scripting&#93; Access 2 plugin examples to discover Sampler plugin capabilities
* &#91;Scripting&#93; New open\_3d\_catpure() function
* &#91;Scripting&#93; When inserting a layer, control if it is inserted above or below the target position

<b>Fixed:</b>

* &#91;3D Capture&#93; Crash if Object Capture cannot be started on macOS
* &#91;Application&#93; Crash at exit
* &#91;Application&#93; Hang at exit while adding assets to the project panel
* &#91;Application&#93; Renaming a project asset does not work unless you press enter
* &#91;Application&#93; Undo and redo menu entries are not disabled when they should be
* &#91;Assets&#93; Unable to delete assets from the All Libraries section of the Assets panel
* &#91;Content&#93; Atlas creator - Use existing opacity map if present
* &#91;Content&#93; Color ID Blend - Fix color picking in the basecolor
* &#91;Layers&#93; Avoid useless computation when using generators
* &#91;Layers&#93; Tweaking a generator may lead to triggering too many computes
* &#91;Performance&#93; Improve GPU memory management
* &#91;Performance&#93; Render cache may not be used when restarting the app
* &#91;Resources&#93; Read only files are not visible in the Assets panel
* &#91;Scripting&#93; Allow reusing a layer after adding another layer
* &#91;Scripting&#93; Changing the layer stack structure several times in one script may fail

<b>Removed:</b>

* &#91;Application&#93; Remove support for .dng and .nef image files

## Version 4

<b>4.5.2 GRUYERE</b>

*(Released: 07 November 2024)*

<b>Fixed:</b>

* &#91;Content&#93; Crop, Embroidery and Height blend filters

<b>4.5.1 GRUYERE</b>

*(Released: 30 July 2024)*

<b>Fixed:</b>

* &#91;Layers&#93; Painting greyscale masks does not work, impacting tools like Clone Stamp, Paint Warp, Content Aware Fill

<b>4.5.0 GRUYERE</b>

*(Released: 18 July 2024)*

<b>Added</b>:

* &#91;Interoperability&#93; Send materials to UE5, Blender, Maya, 3DsMax Unity
* &#91;Content&#93; New texture generator category - Gradients
* &#91;Content&#93; HDRI Tools - new Environment rotation filter

<b>Fixed:</b>

* &#91;Exposed Parameters&#93; Exposing .sbsar input values do not work
* &#91;Layers&#93; Base color turns red with greyscale images
* &#91;Rendering&#93; Grayscale images used in color channels have wrong color space
* &#91;Scripting&#93; Using an export preset sometimes doesn't export the expected channels
* &#91;Content&#93; Dirt - Applying a Dirt filter on top of Image to Material generates a black normal
* &#91;Content&#93; Emboss - Scaling of a pattern in the emboss filter is not linear between 0 and 1
* &#91;Content&#93; Make it tile - Improved normal and height consistency

<b>4.4.1 FONDUE</b>

*(Released: 6 June 2024)*

<b>Fixed:</b>

* &#91;Content&#93; Dirt filter is missing
* &#91;Generative AI&#93; Network error sometimes occur when using Image to Texture

<b>4.4.0 FONDUE</b>

*(Released: 23 May 2024)*

<b>Added</b>:

* &#91;Application&#93; 3D Capture cache is now stored in a separate sub-folder
* &#91;Generative AI&#93; Image to Texture (Beta)
* &#91;Generative AI&#93; Text to Pattern (Beta)
* &#91;Generative AI&#93; Text to Texture (Beta)
* &#91;Scripting&#93; Assets now have a 'resource' property
* &#91;Scripting&#93; Layers now have a 'output\_usages' property

<b>Fixed:</b>

* &#91;Application&#93; Crash when opening corrupted project file
* &#91;Application&#93; Crash when project contains corrupted assets
* &#91;Application&#93; Crash when unplugging a monitor on Windows
* &#91;Application&#93; Incorrect application icon in the Windows task bar
* &#91;Application&#93; Main configuration file corruption can lead to files deletion
* &#91;Application&#93; Panels appear in front of popups
* &#91;Content&#93; Texture generators have blurry thumbnails
* &#91;Export&#93; Opacity channel generated from an imported image breaks when exporting a .sbs/.sbsar
* &#91;Filters&#93; Upscale can crash depending on its input layers
* &#91;Generative AI&#93; Possible crashes when receiving unexpected results from the service
* &#91;Scripting&#93; Crash when autoloading a plugin from environment variable
* &#91;Scripting&#93; Possible crash when assigning Output Usage with the API

<b>4.3.3 EMPANADA</b>

*(Released: 26 March 2024)*

<b>Added:</b>

* &#91;3D Capture&#93; New advanced auto-UV parameters during Post Process
* &#91;Filters&#93; Perforate filter: ability to invert and change the size of the custom pattern

<b>Fixed:</b>

* &#91;3D Capture&#93; Base color can be incorrect on macOS
* &#91;3D Capture&#93; Crash when processing a new version
* &#91;3D Capture&#93; Post-Process step can crash on macOS
* &#91;3D Capture&#93; The Mesh Transform layer can lead to incorrect rendering
* &#91;Application&#93; Crash when starting Sampler while a previous instance is still exporting
* &#91;Application&#93; Sampler is unresponsive for a moment when started for the first time
* &#91;Export&#93; Anisotropy Angle map is not exported
* &#91;Filters&#93; Adding Cloth Weave to the layer stack can lead to a crash
* &#91;Filters&#93; Adding Emboss to the layer stack can lead to a crash
* &#91;Filters&#93; Content-Aware Fill crashes when using 32 bit images
* &#91;Filters&#93; Emboss: Opacity of the layers below aren't completely overriden
* &#91;Filters&#93; Fill: Blend mode does not work in Designer and Painter
* &#91;Filters&#93; Embroidery: automatic color selection is broken
* &#91;Preferences&#93; Prevent setting an unsupported path for 3D Capture cache
* &#91;Preferences&#93; The Normal Format preference does not work
* &#91;Scripting&#93; The channels parameters of Asset.export\_material is case sensitive

<b>4.3.2 EMPANADA</b>

*(Released: 22 February 2024)*

<b>Fixed:</b>

* &#91;Application&#93; Saving a project on a network share on Windows corrupts the project file

<b>4.3.1 EMPANADA</b>

*(Released: 15 February 2024)*

<b>Fixed:</b>

* &#91;3D Capture&#93; Crash when image files become inaccessible while batch generating masks
* &#91;Export&#93; Exporting a material with Crop or relative to input policy layer gives invalid results
* &#91;Layers&#93; Rare crash when rendering a layer stack
* &#91;Filters&#93; Embroidery - Fix issue when using material input on MacOS
* &#91;Filters&#93; Stylization - Support Texture Generators
* &#91;Filters&#93; Pattern - Fix parameters naming
* &#91;Localization&#93; "Save as..." in hardware information window under help menu is appearing unlocalized

<b>4.3.0 EMPANADA</b>

*(Released: 25 January 2024)*

<b>Added</b>:

* &#91;Assets&#93; New asset type: Texture Generators
* &#91;Assets&#93; New materials included in the Starter Assets
* &#91;Assets&#93; New asset picker for image parameters in the Properties panel
* &#91;Assets&#93; Drag and drop Texture Generators from the Assets panel to the image pickers in the Properties panel
* &#91;Assets&#93; Drag and drop Texture Generators from the operating system file explorer
* &#91;Assets&#93; Filters can suggest fitting generators via a user tag on the image input
* &#91;Assets&#93; Texture Generators can define which filter should suggest them via a user tag
* &#91;Content&#93; New Perspective Crop filter
* &#91;Content&#93; New Stylization filter
* &#91;Content&#93; Blending mode on Fill Filter
* &#91;Content&#93; Updated Embroidery filter
* &#91;Content&#93; Updated Paint Wrap filter
* &#91;Content&#93; Updated all filters to support Texture Generators
* &#91;Layers&#93; Ability to chose a Texture Generator output channel when adding it to the layer stack
* &#91;Layers&#93; Ability to easily list and apply presets on Texture Generators
* &#91;Layers&#93; Display a Texture Generator preview in the image pickers
* &#91;Layers&#93; Texture Generator parameters can be exposed and exported
* &#91;Layers&#93; Assign the Base Color usage when importing a single image with the Texture Import Creation Template
* &#91;Layers&#93; Feedback when trying to drag and drop incompatible files in image pickers in the Properties panel
* &#91;Layers&#93; Generate an opacity channel from the alpha channel of an imported image
* &#91;Layers&#93; Image to Material (AI) is faster to compute when changing its category
* &#91;Layers&#93; Select the most relevant layer after a Creation Template is used
* &#91;Layers&#93; The position widgets can now be tweaked with a slider in the Advanced Parameters group
* &#91;Export&#93; Display a percentage in the queue instead of raw numbers
* &#91;Interoperability&#93; Opacity channel is now recognized as alpha channel when sending to Painter
* &#91;Application&#93; New dialog to display and save hardware information
* &#91;Application&#93; New preference to change the default height scale for every project
* &#91;Application&#93; Improve the way outdated assets are displayed
* &#91;Scripting&#93; New asset.documentResolution() and asset.setDocumentResolution() functions
* &#91;Scripting&#93; New select\_asset() function
* &#91;Scripting&#93; Python API for Texture Generators
* &#91;Scripting&#93; get\_project\_assets() now returns 3D objects
* &#91;UI&#93; Asset thumbnail size can be changed in the Assets panel
* &#91;UI&#93; Updated viewport display icons

<b>Fixed:</b>

* &#91;2D View&#93; Zoom with mouse wheel is blocked at 244%
* &#91;Application&#93; Crash at start when initializing the graphics API
* &#91;Application&#93; Crash if the project name contains the # character
* &#91;Application&#93; Possible crash when opening an old project
* &#91;Application&#93; Re-opening the current project can lead to a crash
* &#91;Application&#93; Some project changes are not registered and are lost without warning when closing the project if not saved
* &#91;Export&#93; .sbs/.sbsar export issues when using multiple files with the same name
* &#91;Export&#93; Wrong color space for exported grayscale images .sbs/.sbsar file
* &#91;Filters&#93; Opacity blend behavior issues
* &#91;Layers&#93; .svg files sometimes are not rendered at the correct resolution
* &#91;Performance&#93; Some project saves on disk are unnecessary
* &#91;Project&#93; Importing an old project does not load associated presets
* &#91;Scripting&#93; Unable to get parameters of the first inserted layer
* &#91;UI&#93; The preview popup when hovering an asset can appear in the wrong location or screen
* &#91;UI&#93; Undocked panels are visible and usable on top of the Welcome screen

<b>4.2.2 DORAYAKI</b>

*(Released: 5 December 2023)*

<b>Added:</b>

* &#91;3D Capture&#93; 3D Capture is now 5% to 10% faster on Windows
* &#91;3D Capture&#93; Improve mesh cleanup before decimation
* &#91;Engine&#93; Update Substance Engine to version 9.0.3
* &#91;Layers&#93; Content-Aware Fill: upstream update, various use case fixes and Linux support

<b>Fixed:</b>

* &#91;3D Capture&#93; Clicking "Back" after alignment then "Next" does not update the point cloud
* &#91;3D Capture&#93; Mesh displayed with holes after being added to project
* &#91;Application&#93; Crash when exiting fullscreen mode after a 3D capture
* &#91;Application&#93; Crash with crafted image files
* &#91;Application&#93; If in "All libraries" when quitting Sampler, the Assets panel becomes empty at restart
* &#91;Application&#93; Memory leak when exporting material
* &#91;Application&#93; Opening a project save with previous Sampler versions can lead to a crash
* &#91;Application&#93; Potential crashes when failing to convert 3D meshes
* &#91;Application&#93; Silent crash when opening a .sbsar while Sampler is running
* &#91;Export&#93; Crash when exporting a .sbs/.sbsar file with a custom usage
* &#91;Export&#93; Exported normal maps are always DirectX regardless of the user setting
* &#91;Export&#93; Exporting a 3D Object to a FBX file on macos does not work
* &#91;Export&#93; Inconsistencies when exporting a Layer Stack with an Embroidery filter as a .sbs/.sbsar file
* &#91;Export&#93; Sometimes exporting .sbs/.sbsar files does not work
* &#91;Export&#93; Sometimes when exporting an .sbs/.sbsar file images don't have the right bit depth
* &#91;Layers&#93;  Making a Splatter layer invisible renders its first child instead
* &#91;Layers&#93; Crash when loading mask in Brigtness/Contrast layer
* &#91;Layers&#93; Misleading error messages are displayed after deleting layer
* &#91;Layers&#93; Possible crash when downgrading an asset
* &#91;Layers&#93; Some outputs are not connected to inputs unless the usage is forced in the Channel Settings panel
* &#91;Physical Size&#93; Reference layer dropdown can be reset by mistake
* &#91;UI&#93; Import template info icons needs update
* &#91;UI&#93; Viewport shortcut tip appears everytime the viewport layout changes

<b>4.2.1 DORAYAKI</b>

*(Released: 21 September 2023)*

<b>Added :</b>

* &#91;Content&#93; Image to Material - Improve microdetails generation in normal maps
* &#91;Content&#93; Image to Material - New delighting intensity parameter
* &#91;Layers&#93; Images can be added in the Image Import layers
* &#91;Layers&#93; Images can be removed in the Image Import layers
* &#91;Layers&#93; Invalid layers can now be deleted
* &#91;2D View&#93; Shift+C shortcut to cycle back the channels
* &#91;3D Capture&#93; Display a warning toast when user import less than 20 images
* &#91;Application&#93; New preferences to set the default material texture tiling value
* &#91;Onboarding&#93; Updated tutorial UI for Image to Material (AI) and Upscale
* &#91;Scripting&#93; 3D Capture API: DatasetInfo has more data when Capture3dState is set to aligned
* &#91;Scripting&#93; New select\_asset argument to create\_asset(). New functions: wait\_for\_computation() and clear\_render\_cache()

<b>Fixed :</b>

* &#91;Layers&#93; Crash when Crop region is very small
* &#91;Layers&#93; Crash when adding or tweaking the Crop filter
* &#91;Layers&#93; Making crop region square leads to incorrect material output resolution
* &#91;Layers&#93; Outputs sometimes disappear when several layers are disabled
* &#91;Layers&#93; Render cache may not properly be invalidated with the Image to Material (AI) and Upscale filters
* &#91;Layers&#93; Unable to add Upscale filter when selecting "Do not show this message again" in the warning popup
* &#91;Layers&#93; Unable to restore the image in Embroidery filter once modified
* &#91;Export&#93; Exported normal map resolution changes when changing normal format
* &#91;Export&#93; Remove "\_environment" file name suffix when exporting an environment
* &#91;Export&#93; Unable to export an .sbsar file when there is a Warp Transform layer in the layer stack
* &#91;2D View&#93; "Fit to screen" does not work when resolution changes
* &#91;Application&#93; After closing the application window while computing, the application process could still be running
* &#91;Application&#93; Crash at exit
* &#91;Application&#93; Invalidate render cache when toggling GPU accelerated neural networks
* &#91;Scripting&#93; Naming a plugin as an existing panel name causes unexpected behaviors
* &#91;UI&#93; Clicking on a item with a tooltip will cause the tooltip to disappear until restart
* &#91;UI&#93; Height scale value may change when switching assets
* &#91;UI&#93; Incorrect margin in comboboxes

<b>4.2 DORAYAKI</b>

*(Released: 05 September 2023)*

<b>Added:</b>

* &#91;Content&#93; Vastly improved Image to Material (AI) and Delighter filters
* &#91;Content&#93; New Upscale filter
* &#91;Content&#93; The Crop filter now has dynamic output resolution.
* &#91;Material Creation Template&#93; Add Document size setting.
* &#91;Material Creation Template&#93; New "Add a crop" toggle button.
* &#91;Material Creation Template&#93; New "Upscale Material" toggle
* &#91;Material Creation Template&#93; Display imported image size
* &#91;Material Creation Template&#93; Give feedback when some imported images cannot be used
* &#91;Material Creation Template&#93; Warn when image sizes are inconsistent
* &#91;Material Creation Template&#93; New warnings and tooltips
* &#91;Layers&#93; Display the resolution of the layers in the layer stack
* &#91;Layers&#93; Layer compute resolution can now be either set to Document size or Input size
* &#91;Layers&#93; Show layers resolution in the layer stack
* &#91;Layers&#93; Switch a layer resolution policy to Document or Layer Input when applicable
* &#91;Layers&#93; Warn the user when an Upscale filter is added manually and provide some documentation
* &#91;Layers&#93; Warn the user when doing a linear upscale, and offer to use the Upscale filter instead
* &#91;Layers&#93; Computing an Image to Material (AI) layer can now be cancelled quicker, to improve rendering times when tweaking the layer stack
* &#91;Layers&#93; Computing an Upscale layer can now be cancelled quicker, to improve rendering times when tweaking the layer stack
* &#91;Export&#93; Allow overriding resolution of exported textures
* &#91;Export&#93; Channels to export list is now sorted
* &#91;Export&#93; Display channel resolution in the channels to export list
* &#91;Application&#93; New preference to enable or disable GPU accelerated neural networks
* &#91;UI&#93; Improved resolution dropdowns
* &#91;UI&#93; New icons for Mesh Transform, Mesh Post Process and Weave filters
* &#91;UI&#93; Rename "Share" panel to "Export"
* &#91;Scripting&#93; Add layer output resolution support to the export API
* &#91;Scripting&#93; Added Crop, Upscale and Document size to the image import API
* &#91;Onboarding&#93; New tutorials
* &#91;Onboarding&#93; Update Welcome and What's New screens content
* &#91;Engine&#93; Update Substance Engine to version 9.0.1

<b>Fixed:</b>

* &#91;3D Capture&#93; Improve Precision options naming in Alignment settings parameters
* &#91;Application&#93; Importing images with non-multiple of 16 dimensions can lead to a crash
* &#91;Application&#93; Crash when duplicating an asset in the Project panel
* &#91;Application&#93; Crash when switching assets in the Project panel
* &#91;Content&#93; Painting a custom mask for the Snow filter does not work properly
* &#91;Exposed Parameters&#93; Exposed parameters changes can be lost when switching materials
* &#91;Interoperability&#93; Sending a Material from the Export panel can lead to a crash
* &#91;Layers&#93; Content-Aware Fill stops computing when switching from a single image input to a material input
* &#91;Layers&#93; Crash after duplicating an Environment Light that contains a material
* &#91;Layers&#93; Image import layer displays wrong image name in the Properties panel if the image file was renamed
* &#91;Layers&#93; Sometimes a spinner is displayed on an inactive layer
* &#91;Layers&#93; Sometimes changing the output usage of an image in an Image import layer does not work
* &#91;Layers&#93; Typos in the Creation Template Window
* &#91;UI&#93; 3D viewport onboarding tooltip has focus issues
* &#91;UI&#93; Image name can overflow if file name is too long
* &#91;UI&#93; Minor brush toolbar layout issues when using the eraser
* &#91;UI&#93; Strings are truncated in some languages in the Viewer Settings panel
* &#91;UI&#93; While the viewport tooltip popup is displayed, pressing "space" creates a new project

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

### 4.0.2 Banana

*(Released: March 09, 2023)*

**Added:**

* &#91;3D Capture&#93; Disk usage shows the amount used
* &#91;3D Capture&#93; Importing photos is asynchronous and faster
* &#91;Scripting&#93; New classes and functions to script the 3D Capture feature
* &#91;Scripting&#93; New ExportController class to perform actions when the export is finished, failed or canceled
* &#91;Scripting&#93; Pass arguments python scripts run with --run-script
* &#91;UI&#93; UI feedback when dragging an asset over the Layers panel
* &#91;Content&#93; Color temperature filter is now working on materials
* &#91;Content&#93; Normal to Height filters has a new option to preserve tiling

**Fixed:**

* &#91;3D Capture&#93; Corrected image size in dataset alignment step
* &#91;3D Capture&#93; Remove duplicate vertices after UV unwrapping
* &#91;3D Capture&#93; MacOS - Better detection if 3D Capture is available
* &#91;3D Capture&#93; Crash when closing the 3D capture window while importing images
* &#91;3D Capture&#93; Crash when generating a new version
* &#91;3D Capture&#93; Crash when trying to load the 3D object in the viewer
* &#91;3D Capture&#93; Crash when using path with non UTF8 characters
* &#91;3D Capture&#93; Hits &amp; Tips typo
* &#91;3D Capture&#93; Meshes are no longer scaled to fit into unit cube
* &#91;3D Capture&#93; Prevent a crash when closing 3D capture while rendering
* &#91;3D Capture&#93; Removing a mask makes the image disappear
* &#91;Application&#93; Crash when importing twice an asset simultaneously
* &#91;Application&#93; Backup previous version of assets when opening a project if they were never back-up
* &#91;Application&#93; Correctly cache baked maps when not all maps are baked
* &#91;Application&#93; Fullscreen crashes when a 3D object is displayed.
* &#91;Application&#93; Last material is duplicated when saving the project
* &#91;Application&#93; Prevent crash when cancelling the Mesh Post processing compute during the baking step
* &#91;Application&#93; Reopening current project does not discard changes
* &#91;Application&#93; Stop generating thumbnails for 3D objects
* &#91;2D View&#93; Crash when use the brush tool
* &#91;Content&#93; Content Aware Fill - computation may stuck
* &#91;Content&#93; Atlas Creator filter is downscaling the Opacity channel
* &#91;Export&#93; Fix clear Failed exports queue
* &#91;Export&#93; OBJ export creates object 100 times smaller than expected
* &#91;Layers&#93; Color images imported as grayscale channels are now considered grayscale
* &#91;Export&#93; FBX files cannot be imported in third party applications
* &#91;Export&#93; Shader output names in USD files are not correct
* &#91;Layers&#93; Image name is not updated when changing its name on the OS explorer
* &#91;Scripting&#93; Display an error message when reloading an invalid script
* &#91;UI&#93; Base material button disabled when not available
* &#91;UI&#93; Crash when accessing the file dialog on the Material Creation Template Window
* &#91;UI&#93; Quick accessor is accessible even when the Layers panel is closed
* &#91;UI&#93; Send to icons are misaligned
* &#91;UI&#93; The layer icon changes when clicking on the Blend icon

**Known Issues:**

* &#91;Color Picker&#93; Picking a color on a second monitor with a different resolution may not work
* &#91;Content&#93; Shape light widget is not working in spherical projection mode
* &#91;Interoperability&#93; Material with displacement sent to Stager will lose displacement controls

### 4.0.1 Banana

*(Released: February 07, 2023)*

**Fixed:**

* &#91;3D Capture&#93; When using masks, the texture projection may be broken
* &#91;3D Capture&#93; Artefacts may appear on your object
* &#91;3D Capture&#93; The exported mesh may be really small

**Known Issues:**

* &#91;3D Capture&#93; FBX and OBJ exports downscale the result
* &#91;3D Capture&#93; 3D Capture is available on MacOS even if your hardware is not compatible. Check the documentation.
* &#91;3D Capture&#93; Crash when the mesh reconstruction is done.
* &#91;Layers&#93; Content-Aware Fill can be stuck if you tweak layers below
* &#91;Color Picker&#93; Picking a color on a second monitor with a different resolution may not work
* &#91;Content&#93; Shape light widget is not working in spherical projection mode
* &#91;Interoperability&#93; Material with displacement sent to Stager will lose displacement controls

### 4.0.0 Banana

*(Released: January 31, 2023)*

**Added:**

* &#91;3D Capture&#93; Create 3D objects from images
* &#91;3D Capture&#93; Dedicated 3D Capture wizard
* &#91;3D Capture&#93; Import or generate black and white masks on your dataset
* &#91;3D Capture&#93; Alignment result - view all matched features as a point cloud
* &#91;3D Capture&#93; Alignment result - view and interact with cameras associated with each aligned photo
* &#91;3D Capture&#93; Define the reconstruction area with a bounding box widget
* &#91;3D Capture&#93; Scale, translate, and rotate on all axes the bounding box widget
* &#91;3D Capture&#93; Define the geometry precision for the reconstructed mesh
* &#91;3D Capture&#93; Optimize your mesh and textures by creating a new version
* &#91;3D Capture&#93; Each of the versions is automatically decimated to the target faces number set
* &#91;3D Capture&#93; The post-process step automatically unwraps, re-projects textures, and then bakes the normal height and AO information from the high-poly mesh
* &#91;3D Capture&#93; Add the original result or a version to the Sampler project
* &#91;3D Capture&#93; New Mesh Post-Process layer to automatically decimate, unwrap, reproject textures, and bake details of the underlying mesh layer
* &#91;3D Capture&#93; New Mesh Transform layer to scale, rotate, or translate the underlying mesh layer
* &#91;Export&#93; New Export window
* &#91;Export&#93; Dedicated settings and UI depending on the asset type (material, environment light, mesh)
* &#91;Export&#93; Export the mesh as USD, USDA, USDZ, glTF, glb, obj, fbx, stl
* &#91;Export&#93; Define the material type when exporting Substance files (SBSAR, SBS)
* &#91;UI&#93; Move cache settings to a new tab in the Preferences popup
* &#91;Application&#93; 2D and 3D viewports can now be resized, swapped, and stacked vertically
* &#91;Application&#93; New SAMPLER\_RESOURCES\_PATH environment variable to add extra starter assets
* &#91;Scripting&#93; Added SAMPLER\_PLUGIN\_PATH and SAMPLER\_SCRIPT\_PATH environment variables to import plugins and scripts at startup
* &#91;Scripting&#93; Added export functions for materials, environment lights, and 3d objects
* &#91;Scripting&#93; Added identifier, default value, min and max values, labels, and enum values to parameters
* &#91;Scripting&#93; Added import\_textures function to enter a customized usage while importing images

**Fixed:**

* &#91;Application&#93; Crash when opening a recent project and saving in confirmation dialog
* &#91;Application&#93; File dialog prevents opening .ssa files
* &#91;Application&#93; File dialogs can appear on a background window on macOS
* &#91;Application&#93; Potential crash when opening 3.2 projects
* &#91;Application&#93; Selecting a file closes the File dialog before displaying warnings
* &#91;Exposed Parameters&#93; Exporting parametric environment lights does not work
* &#91;Layers&#93; "Click here to browse" link in layer stack doesn't work anymore
* &#91;Layers&#93; Painting several images within the same layer sometimes does not work
* &#91;Layers&#93; Setting an image in the layer properties does not update the image picker thumbnail
* &#91;Layers&#93; Tweaking a Sampler asset added as a layer does not work
* &#91;Project&#93; Unwanted asset update when opening a project
* &#91;Scripting&#93; Browse to plugin folder sometimes fails on Windows
* &#91;Scripting&#93; Crash when using 'open\_project()' in a Python script
* &#91;Scripting&#93; JPEG export is missing from the API
* &#91;Scripting&#93; The log panel is not read-only
* &#91;Scripting&#93; image\_picker parameter value does not work
* &#91;UI&#93; Missing asset icon for environment lights in the Project panel
* &#91;UI&#93; Send to Designer Format Dropdown in the Preferences popup can be empty
* &#91;UI&#93; Some buttons have an incorrect style
* &#91;UI&#93; The label overlaps the buttons in Button Group widgets
* &#91;UI&#93; Tooltip position is wrong for "Tools" in Set the physical size menu
* &#91;UI&#93; When changing language, File menu is misaligned

**Known Issues:**

* &#91;3D Capture&#93; When using masks, the texture projection may be broken
* &#91;3D Capture&#93; Small artefacts may appear on your object if your scale in the Mesh transform is too small
* &#91;3D Capture&#93; The exported mesh may be really small. Reset the scale of the Mesh transform and re-export
* &#91;Color Picker&#93; Picking a color on a second monitor with a different resolution may not work
* &#91;Content&#93; Shape light widget is not working in spherical projection mode
* &#91;Interoperability&#93; Material with displacement sent to Stager will lose displacement controls

## Version 3

### 3.4.1 Arancini

*(Released: October 06, 2022)*

**Added:**

* &#91;Onboarding&#93; New Welcome and What's New screens
* &#91;Onboarding&#93; Updated Home screen UI
* &#91;Onboarding&#93; New Learn content in the Home screen
* &#91;Scripting&#93; Log an error in the Log panel when a method is not recognized
* &#91;Scripting&#93; New ssa.helpers module to enable printing to the Log panel
* &#91;Application&#93; Support for the new side-by-side buttons widget from Substance 3D Designer

**Fixed:**

* &#91;Export&#93; Crash when exporting a .sbsar file referencing a missing image
* &#91;Export&#93; Crash when exporting an asset referencing a corrupted image file
* &#91;Export&#93; Exporting a .sbsar file with an Embroidery layer results in a gray material
* &#91;Export&#93; Exporting a material to a .sbs/sbsar file can generate a fully transparent material
* &#91;Export&#93; Normal Format parameter is not exposed correctly in .sbs/.sbsar files
* &#91;Export&#93; Sbs/sbsar export of a layer stack referencing a .svg file is broken
* &#91;Export&#93; Transform layer is not exported properly / Updated Enscape - Revit export preset
* &#91;Exposed Parameters&#93; Crash when deleting a layer containing an exposed parameter
* &#91;Exposed Parameters&#93; Updating an outdated layer in the layer stack can lead to a corrupted list of exposed parameters
* &#91;Exposed Parameters&#93; Parameters that should not be exported are exported anyway
* &#91;Exposed Parameters&#93; Removing a blend filter when deleting a layer does not unexpose its parameters
* &#91;Exposed Parameters&#93; Text parameters break .sbs/.sbsar exports
* &#91;Layers&#93; Crash when dropping a layer stack in another layer stack
* &#91;Layers&#93; Crash when failing to load a filter
* &#91;Layers&#93; Cannot reload the previous image when resetting the Image field
* &#91;Layers&#93; Cannot undo/redo transform tool changes
* &#91;Layers&#93; Clone Stamp layer is stuck after clicking "Reset all settings"
* &#91;Layers&#93; Using any of the reset buttons prevents from drawing in the Image field
* &#91;Layers&#93; The Reset button does not clear the drawing mask in the Image field
* &#91;Layers&#93; The Reset button in the Image field does nothing if the user has painted something
* &#91;Layers&#93; Rendering cache does not work when using the Brush tool
* &#91;Layers&#93; Deleted layer can still show up in the Properties panel
* &#91;Layers&#93; Layer computation can stall when switching between project assets
* &#91;Project&#93; Sometimes Sampler is unable to open a project from disk
* &#91;2D View&#93; The 2D view always defaults back to Material Output

**Known Issues:**

* &#91;Color Picker&#93; Picking a color on a second monitor with a different resolution may not work
* &#91;Content&#93; Shape light widget is not working in spherical projection mode
* &#91;Interoperability&#93; Material with displacement sent to Stager will lose displacement controls

### 3.4.0 Arancini

*(Released: September 06, 2022)*

**Added:**

* &#91;Exposed Parameters&#93; New Exposed Parameters panel
* &#91;Exposed Parameters&#93; New button on parameters hover to expose and unexpose parameters from Properties panel
* &#91;Exposed Parameters&#93; New right-click context menu on parameters to expose and unexpose parameters from Properties panel
* &#91;Exposed Parameters&#93; Exposed parameters are listed in the Exposed Parameters panel
* &#91;Exposed Parameters&#93; Color dots and color discs are added in several places to easily identify exposed parameters
* &#91;Exposed Parameters&#93; Parameter labels can be edited in the Exposed Parameters panel
* &#91;Exposed Parameters&#93; Display a warning for non-exportable parameters
* &#91;Exposed Parameters&#93; Display warning if moving a layer with exposed blend parameters somewhere where they become hidden
* &#91;Exposed Parameters&#93; Exposed parameters are exported in SBS and SBSAR formats
* &#91;Metadata&#93; Support Custom Metadata templates
* &#91;Metadata&#93; New CLO Physical properties metadata template
* &#91;Metadata&#93; Add icons on hover to add/remove custom metadata
* &#91;Python API&#93; New Python API
* &#91;Python API&#93; API for Asset authoring
* &#91;Python API&#93; API for Layers management
* &#91;Python API&#93; API for Parameters management
* &#91;Python API&#93; API for Project management
* &#91;Python API&#93; A plugin can be enabled and disabled
* &#91;Python API&#93; Python API documentation accessible in the Help menu
* &#91;Scripting&#93; New Plugins and Scripts section in the Preferences popup
* &#91;Scripting&#93; Create and import plugins to customize Sampler interface with your own panels
* &#91;Scripting&#93; Plugins become part of the Sampler interface and can be docked and moved around like standard Sampler panels
* &#91;Scripting&#93; Dedicated button bar for the plugins on the Sampler right toolbar
* &#91;Scripting&#93; Create and import scripts to perform a list of given tasks
* &#91;Scripting&#93; Launch Python scripts via Scripts menu
* &#91;Scripting&#93; Plugins and Scripts can be deleted, re-ordered, and reloaded from the Preferences window
* &#91;Scripting&#93; Added --run-script command line parameters
* &#91;Logs&#93; New Logs panel
* &#91;Logs&#93; Enable Logs panel from the Preferences window
* &#91;Logs&#93; New action bar to clear, copy/paste, export logs
* &#91;Properties&#93; New button on parameters hover to reset parameter value
* &#91;Properties&#93; New right-click context menu on parameters to reset parameter value
* &#91;Content&#93; Image to Material (AI Powered) now works on MacOS
* &#91;Engine&#93; Update Substance engine to v8.6.0

**Fixed:**

* &#91;Application&#93; Application could crash at exit when a thumbnail generation was in progress
* &#91;Application&#93; Application might crash when using 'Save as' at exit
* &#91;Application&#93; Application might hang during shutdown on MacOS
* &#91;Application&#93; Saving with the color dialog open doesn't save its changes
* &#91;Export&#93; Usage naming convention is not correct when exporting
* &#91;Layers&#93; Dropping a material on top of a filter could crash
* &#91;Layers&#93; Updating an outdated layer stack could update unrelated layer stacks
* &#91;Metadata&#93; Empty fields are exported
* &#91;Metadata&#93; When there is only one metadata item, the UI lets you try to reorder it
* &#91;Project&#93; Compute never ends after duplicating a material
* &#91;Project&#93; Project asset is duplicated after initial project save
* &#91;Project&#93; Unnecessary computations when switching asset
* &#91;Rendering&#93; Some layer stacks do not render properly after deleting a layer
* &#91;Security&#93; Fix CVE-2015-20107
* &#91;UI&#93; 2D Outputs can be blurry depending on the window size
* &#91;UI&#93; Asset preview can stay opened on top when application loses focus
* &#91;UI&#93; Splash screen rounded corners have a square opaque background

**Known Issues:**

* &#91;Color Picker&#93; Picking a color on a second monitor with a different resolution may not work
* &#91;Content&#93; Shape light widget is not working in spherical projection mode
* &#91;Interoperability&#93; Material with displacement sent to Stager will lose displacement controls

### 3.3.2 Zucchini

*(Released: June 28, 2022)*

**Fixed:**

* &#91;Application&#93; Fix potential crash when opening a project
* &#91;Export&#93; Restarting Sampler breaks imported custom export presets list
* &#91;Interoperability&#93; Fix crash when a material sent from Designer is deleted and then re-sent from Designer
* &#91;Project&#93; Impossible to delete the last material or environment light if it's the last asset in the project
* &#91;Project&#93; Right-click on an environment light makes the "unsaved modifications" asterisk appear

**Known Issues:**

* &#91;Color Picker&#93; Picking a color on a second monitor with a different resolution may not work
* &#91;Content&#93; Shape light widget is not working in spherical projection mode
* &#91;Interoperability&#93; Material with displacement sent to Stager will lose displacement controls

### 3.3.1 Zucchini

*(Released: June 07, 2022)*

**Added:**

* &#91;Application&#93; Native Apple silicon (M1) support
* &#91;UI&#93; New shortcut, "C" key, to cycle through channels in the 2D view
* &#91;Tools&#93; Numerical field to edit grayscale color value in Brush Toolbar

**Fixed:**

* &#91;Tools&#93; Using the Brush tool on Windows with a fractional UI scale (150%) offsets the strokes
* &#91;Performance&#93; Improve memory consumption
* &#91;Physical Size&#93; Physical size information can be missing when enabling the feature
* &#91;UI&#93; Mouse scrolling sometimes does not work as expected when pressing the Alt key
* &#91;Application&#93; Application may crash when opening a saved project
* &#91;Application&#93; Crash when drag and dropping several images and using Texture Import in the Material Creation Template window
* &#91;Application&#93; Potential crash when saving a project containing a custom filter
* &#91;Application&#93; Sometimes the Control key state is lost when switching application
* &#91;Assets&#93; Crash when renaming a local folder

**Known Issues:**

* &#91;Color Picker&#93; Picking a color on a second monitor with a different resolution may not work
* &#91;Content&#93; Shape light widget is not working in spherical projection mode
* &#91;Interoperability&#93; Material with displacement sent to Stager will lose displacement controls

### 3.3.0 Zucchini

*(Released: May 17, 2022)*

**Added:**

* &#91;Content&#93; New Content-Aware Fill filter (Windows and Mac)
* &#91;Content&#93; Content-Aware Fill is working on images, PBR materials, and environment lights
* &#91;Content&#93; Add "Preserve Tiling" parameter to Image to Material (AI Powered)
* &#91;Content&#93; The Perspective Transform filter can display a grid between its four points
* &#91;Interoperability&#93; Send materials to Adobe Substance 3D Stager
* &#91;Tools&#93; Center the transformation by pressing Ctrl when resizing Transform or Crop tool
* &#91;Tools&#93; Lock the ratio to square by pressing Shift when resizing Transform or Crop tool
* &#91;Tools&#93; Clone stamp cursor offers a preview of what will be stamped
* &#91;Tools&#93; Preview original content in the the Eraser cursor when using Clone stamp
* &#91;Tools&#93; Ctrl+Click creates a new stamp in the Clone Stamp layer
* &#91;Tools&#93; Successive clone stamps are now grouped within a single layer
* &#91;Tools&#93; Brush Toolbar UI Revamp
* &#91;Tools&#93; The Brush Toolbar position is persistent during a session
* &#91;Tools&#93; New brush tiling options by axis
* &#91;Tools&#93; Hide/display the overlay over the 2D view when painting
* &#91;Tools&#93; New shortcut, "X" key, to toggle between Brush and Eraser
* &#91;Tools&#93; New shortcut, "&#91;" "&#93;" to change the Brush size
* &#91;Tools&#93; New shortcut, "E" key, to toggle the Eraser
* &#91;2D View&#93; New Spherical Projection mode when creating environment light
* &#91;2D View&#93; Brush tool is supported with the spherical projection mode
* &#91;2D View&#93; Position tool is supported with the spherical projection mode
* &#91;2D View&#93; Undo/redo is supported with the spherical projection mode
* &#91;2D View&#93; In Spherical Projection, set the default position to look at the center of the environment
* &#91;2D View&#93; New exposure control
* &#91;UI&#93; In the Properties panel, the Image tweak displays the source of the content (Image or from a layer)
* &#91;UI&#93; Improved the layer/material outputs dropdown background
* &#91;UI&#93; New position of the resolution information in the 2D View
* &#91;UI&#93; New tooltip with 3D view navigation controls shortcuts
* &#91;UI&#93; New tooltip with brush controls
* &#91;UI&#93; New tooltip with projection navigation controls shortcuts
* &#91;Compound Filters&#93; Compound filters handle variations to work on images, PBR materials, and environment lights
* &#91;Compound Filters&#93; Tweaks order matches the nodes list order in the compound filter
* &#91;Compound Filters&#93; Tweaks of different nodes with the same group will be merged in one single group in the Properties panel
* &#91;Application&#93; Have dedicated viewer settings per asset type

**Fixed:**

* &#91;Application&#93; Application may crash when switching to 2D view
* &#91;Application&#93; Fix a possible deadlock or crash when exporting multiple times
* &#91;Application&#93; Make default values for channels consistent with Substance 3D Designer
* &#91;Application&#93; Loading a project doesn't trigger the material recompute
* &#91;Application&#93; Updated the URL to texture import documentation
* &#91;Content&#93; When using a compound filter, it asks to be updated when it shouldn't, on reload
* &#91;Content&#93; Details in height map disappear when using Opacity Blend
* &#91;UI&#93; In the Color Dialog, it is possible to get out of range using the slider's text fields
* &#91;UI&#93; Usage list has a useless vertical scrollbar

**Known Issues:**

* &#91;Color Picker&#93; Picking a color on a second monitor with a different resolution may not work
* &#91;Content&#93; Shape light widget is not working in spherical projection mode
* &#91;Interoperability&#93; Material with displacement sent to Stager will lose displacement controls

### 3.2.1 Yakitori

*(Released: March 08, 2022)*

**Added:**

* &#91;Export&#93; Export dpi metadata in image files
* &#91;Physical Size&#93; Keep the ratio with non square textures when editing physical dimensions
* &#91;Physical Size&#93; Physical size metadata is applied immediatly when physical size changes
* &#91;UI&#93; Adjust Height scale max slider so it can influence any kind of material when Physical Size is enabled
* &#91;UI&#93; New tooltips on search filters in the Asset panel
* &#91;UI&#93; Use tooltips to explain when buttons are disabled in the Assets panel
* &#91;Content&#93; Brightness contrast filter update

**Fixed:**

* &#91;2D View&#93; 90 degrees rotation button in the Crop and Transform tools don't work as expected
* &#91;2D View&#93; Crop widget sometimes goes missing
* &#91;Application&#93; Clearing an image parameter does not reconnect the underlying layer
* &#91;Application&#93; Crash at exit after saving a project
* &#91;Application&#93; Crash when drag and dropping the current material into a collection of the Assets Panel
* &#91;Application&#93; Drag and dropping an asset in the viewport may crash
* &#91;Content&#93; Normal blend has a random seed tweak
* &#91;Content&#93; Snow filter has incorrect normal output depending on fresh and melted snow parameter values
* &#91;Content&#93; Parquet filter: fixed unexpected seams
* &#91;Content&#93; Embroidery filter: remove thread in metallic map
* &#91;Content&#93; Floor tiles filter: fix x and y tiles count
* &#91;Content&#93; Brick wall filter: output normal and height to 16 bit
* &#91;Export&#93; Default file name in export popup is not the current material name
* &#91;Export&#93; Exporting with physical ratio with an export preset gives incorrect dimensions
* &#91;Export&#93; Metallic is missing in the CLO export preset
* &#91;Export&#93; When replacing an export custom preset, the display name is not updated
* &#91;Layers&#93; Custom channels of the first inserted layer are not discovered
* &#91;Layers&#93; Material is re-evaluated when changing tweaks of a hidden layer
* &#91;Localization&#93; Tooltips are not localized in Export panel
* &#91;Physical Size&#93; Disabling Physical Size of an asset does not remove the physical scale
* &#91;Physical Size&#93; Height Scale value can't be set outside of slider bounds the first time
* &#91;Physical Size&#93; Importing an image with no physical size prevents opening the project
* &#91;Physical Size&#93; Physical Size is erroneously set to zero when missing
* &#91;Physical Size&#93; Physical Size physical scale check box status is not updated when first displayed
* &#91;UI&#93; Base Material &amp; Normal to Height do not have a category
* &#91;UI&#93; Cursor is sometimes invisible when painting an image
* &#91;UI&#93; Disable "Copy All" and "Cut All" options in the edit menu of a text field if it is empty
* &#91;UI&#93; Filter names have incorrect characters
* &#91;UI&#93; Physical Size lock button does not have the correct style
* &#91;UI&#93; The close button in search bar in Asset Panel does not clear the search string

**Known Issues:**

* &#91;Color Picker&#93; Picking a color on a second monitor with a different resolution may not work

### 3.2.0 Yakitori

*(Released: January 25, 2022)*

**Added:**

* &#91;Physical Size&#93; New Physical Size panel
* &#91;Physical Size&#93; Add Physical Size options to the Material Creation Template window
* &#91;Physical Size&#93; Add Physical Size measurement tool
* &#91;Physical Size&#93; Add Physical Size auto-measurement tool
* &#91;Physical Size&#93; Add Physical Size diagnostic tool
* &#91;Physical Size&#93; Allow setting the z value of the Physical Size
* &#91;Physical Size&#93; Dropdown widget to set the level of zoom in the 2D view
* &#91;Physical Size&#93; New "Display with physical ratio" option in the level of zoom dropdown
* &#91;Physical Size&#93; New "Fit to physical size" option in the level of zoom dropdown
* &#91;Physical Size&#93; Display the Physical Size in the 2D view
* &#91;Physical Size&#93; Display the Physical Size in the 3D viewport
* &#91;Physical Size&#93; In the image import dialog, show physical size depth if there is an imported height map
* &#91;Physical Size&#93; Show the Physical Size in the asset contextual menu
* &#91;Physical Size&#93; Set the length unit in the Preferences
* &#91;Physical Size&#93; Export textures respecting the physical ratio
* &#91;Metadata&#93; Ability to add custom metadata to a user-authored asset
* &#91;Export&#93; Export custom metadata to .sbs(ar) files
* &#91;Export&#93; Export description, category, author, and tags metadata to .sbs(ar) files
* &#91;Export&#93; Export the Physical Size to .sbs(ar) files
* &#91;Export&#93; Set .sbsar file compression setting
* &#91;Export&#93; Export the asset thumbnail to .sbs(ar) files
* &#91;Export&#93; Set the graph type when exporting a .sbs(ar) file
* &#91;Application&#93; Realtime Engine 2021 is no longer available
* &#91;Application&#93; Undo/Redo now supports Tiling (U,V) and height scale slider changes
* &#91;Rendering&#93; Generate disk cache when the authored asset is saved
* &#91;Assets&#93; Use Ctrl+click to enable multiple asset type filters in the Resources panel
* &#91;UI&#93; Ability to lock the Tiling (U,V) sliders
* &#91;UI&#93; Add a contextual menu with "Copy", "Cut", "Paste", "Copy all" and "Cut all" in text fields
* &#91;UI&#93; Length unit (meters, inches, parsecs, ...) support in labels and text fields
* &#91;UI&#93; The user can set the decimal precision used to display numbers
* &#91;UI&#93; Use units in measure popups everywhere it's relevant
* &#91;Localization&#93; Default new asset name is now localized
* &#91;Content&#93; New Cloth Weave generator
* &#91;Content&#93; New Channel Switch filter
* &#91;Content&#93; All relevant filters are now aware of the Physical Size
* &#91;Content&#93; New icons for Wood Finish
* &#91;Content&#93; All filters are now compatible with Adobe Standard Materials (ASM) channels
* &#91;Content&#93; Filters can now have an "environment" variation

**Fixed:**

* &#91;2D View&#93; Channel remains in the list when removed
* &#91;Application&#93; Cannot duplicate an asset loaded from the operating system file explorer
* &#91;Application&#93; Crash at exit
* &#91;Application&#93; Crash sometimes when clicking "Starter Assets" in the Assets panel
* &#91;Application&#93; Crash when deleting a material
* &#91;Application&#93; Environment variable "SUBSTANCE\_DISABLE\_SPECIFIC\_FEATURES" is still active when set to "0" or "".
* &#91;Application&#93; Freeze while saving a project with multiple materials
* &#91;Application&#93; Importing an image can lead to a crash
* &#91;Application&#93; Missing some starter assets on first launch
* &#91;Export&#93; Exporting an asset sometimes leads to a crash
* &#91;Layers&#93; Cannot import images when the layer panel is closed or invisible
* &#91;Layers&#93; Changing the language causes the current asset to recompute
* &#91;Layers&#93; Changing the usage of an imported image does not upate which filter variation to use
* &#91;Layers&#93; Image to Material (AI) is sometimes not computed when tweaking layers below it
* &#91;Layers&#93; Image to Material (AI) sometimes recomputes when not needed
* &#91;Layers&#93; No update is suggested when a custom filter is updated on the disk
* &#91;Layers&#93; Normal channel sometimes has the wrong pixel format
* &#91;Layers&#93; Some layers are still computed even when not visible
* &#91;Layers&#93; The 2D view tools may be broken when toggling a layer visibility
* &#91;Layers&#93; The UI freezes when using Image to Material (AI)
* &#91;Layers&#93; Toggling the visibilty of the Transform filter layer breaks the 2D view tool and may lead to a crash
* &#91;Layers&#93; Too many recomputations when removing a layer from the layer stack
* &#91;Layers&#93; When a compound filter contains an unusual or custom input/output, Sampler doesn't compute it
* &#91;Performance&#93; Asset panel is slow to open
* &#91;Performance&#93; Avoid some unnecessary recomputations of the layer stack
* &#91;Performance&#93; Loading project assets takes too much time
* &#91;Performance&#93; Render cache on disk may not be used
* &#91;Performance&#93; Switching between layers is slow
* &#91;Performance&#93; Tweaking a material or a filter is slow
* &#91;Project&#93; Saving a project when exiting may lead to a crash
* &#91;Rendering&#93; Removing an image may remove all outputs
* &#91;Rendering&#93; The rendering time displayed in the viewport is wrong when tweaking
* &#91;UI&#93; Can't scroll vertically in the export popup when needed
* &#91;UI&#93; It is possible to open the export popup when there is nothing to export
* &#91;UI&#93; Some popups do not scroll if their content overflows
* &#91;UI&#93; Text fields are not selected when clicking on it or opening a menu
* &#91;UI&#93; The name of the blend mode in the properties panel is sometimes not correct
* &#91;UI&#93; The Save option in the File menu is sometimes grayed out
* &#91;UI&#93; The text field doesn't go away after renaming two materials
* &#91;UI&#93; Typo in the preference popup

**Known Issues:**

* &#91;Color Picker&#93; Picking a color on a second monitor with a different resolution may not work

### 3.1.2 Xocoatl

*(Released: December 14, 2021)*

**Fixed:**

* &#91;Interoperability&#93; Open .sbsar file with Substance 3D Sampler from Bridge can fail on Windows
* &#91;Layers&#93; Moving the only layer below itself will crash
* &#91;UI&#93; Channel settings button disappears when changing language
* &#91;UI&#93; The material name in Properties panel disappears after saving the project
* &#91;Assets&#93; Clicking on "All libraries" can lead to a crash

**Known Issues:**

* &#91;Realtime Engine 2021&#93; Heavy computation can crash the application
* &#91;Realtime Engine 2021&#93; Realtime Engine 2021 will crash on a Windows machine with both AMD CPU and Nvidia GPU installed
* &#91;Color Picker&#93; Picking a color on a second monitor with a different resolution may not work

### 3.1.1 Xocoatl

*(Released: November 24, 2021)*

**Added:**

* &#91;Interoperability&#93; Send assets (SBS or SBSAR) to Substance 3D Designer
* &#91;Interoperability&#93; Set in preferences the default format for interoperability with Substance 3D Designer
* &#91;Interoperability&#93; Receive multiple assets from Adobe Bridge
* &#91;UI&#93; New Random Seed widget
* &#91;UI&#93; Context menu update
* &#91;Assets&#93; Drag and drop images from the Assets panel to the Properties panel
* &#91;Project&#93; Asset names are sanitised to avoid some specific characters
* &#91;Branding&#93; Update file icon for SBSAR files
* &#91;Engine&#93; Update Substance Engine version 8.3.0

**Fixed:**

* &#91;Content&#93; Crop - Preserve ratio when cropping non-square images
* &#91;Content&#93; Transform - Horizontal transformation is not inverted when using the widget
* &#91;Content&#93; Gravel - fix custom mask painting on all channels
* &#91;Content&#93; Floor tiles - fix issues with pattern tiling and repetition
* &#91;Assets&#93; Grey out Adobe Bridge option if not installed
* &#91;Color Picker&#93; Escape key closes the Color Picker
* &#91;Rendering&#93; Fix Scattering Distance Scale when using greyscale input
* &#91;Share&#93; Send to options are only available with Adobe licenses
* &#91;Project&#93; Fix a memory performance issue

**Known Issues:**

* &#91;Realtime Engine 2021&#93; Heavy computation can crash the application
* &#91;Realtime Engine 2021&#93; Realtime Engine 2021 will crash on a Windows machine with both AMD CPU and Nvidia GPU installed
* &#91;Color Picker&#93; Picking a color on a second monitor with a different resolution may not work

### 3.1.0 Xocoatl

*(Released: September 28, 2021)*

**Added:**

* &#91;Color Picker&#93; New Color Picker UI
* &#91;Color Picker&#93; Preview the current and previous colors side by side
* &#91;Color Picker&#93; Input your color in Hexadecimal
* &#91;Color Picker&#93; New eyedropper with color preview
* &#91;Color Picker&#93; The eyedropper can pick a color outside of Sampler
* &#91;Color Picker&#93; Tweak your color in RGB or HSV color spaces
* &#91;Color Picker&#93; Save and manage Swatches
* &#91;Interoperability&#93; Edit images in Illustrator from Image Import layer or Image parameters
* &#91;Interoperability&#93; Edit images in Photoshop from Image Import layer or Image parameters
* &#91;Widget&#93; New Crop Widget
* &#91;Widget&#93; Press Enter to validate your crop
* &#91;Widget&#93; The Crop widget reads the image size to fit the widget and keep the ratio when resizing
* &#91;UI&#93; New gresycale slider UI
* &#91;Application&#93; Add normal format selection in preferences
* &#91;Application&#93; The normal format in Image Import layers follows the default normal format set in the preferences
* &#91;Application&#93; In the 2D view, the normal is displayed following the normal format set in the preferences
* &#91;Application&#93; The normal is exported in the normal format set in preferences
* &#91;Export&#93; Add normal format parameter to SBS and SBSAR file exports
* &#91;Export&#93; Add shader settings to SBS and SBSAR file exports
* &#91;Export&#93; Set the default resolution of exported SBS graphs
* &#91;Compound Filters&#93; Package SSA filters with 7z
* &#91;Compound Filters&#93; Add category metadata in compound filters
* &#91;Compound Filters&#93; Compound Filters can have an embedded thumbnail
* &#91;Compound Filters&#93; Added Compound Filters extension (.ssafilter) to the Get Content's file dialog
* &#91;Compound Filters&#93; Import Compound Filters (.ssafilter) in the Assets panel
* &#91;Engine&#93; Update substance engine to v8.2.0

**Fixed:**

* &#91;Application&#93; Connected local folders may hang
* &#91;Application&#93; Crash at exit
* &#91;Application&#93; Crash when launching two instances of Sampler
* &#91;Content&#93; Crop filter has a random seed tweak
* &#91;Content&#93; Some Substance materials are sometimes not upgraded
* &#91;Export&#93; Crash when exporting with a newly added custom preset
* &#91;Export&#93; Estimated size of package is missing in export popup
* &#91;Export&#93; Fix memory leak when exporting SBS and SBSAR files
* &#91;Compound Filters&#93; Compound filters may have duplicated inputs
* &#91;Compound Filters&#93; Crash if a filter has unmet references
* &#91;Compound Filters&#93; Crash when reordering a layer stack with a compound filter in it
* &#91;Compound Filters&#93; The render sometimes hangs
* &#91;Image Import&#93; Importing an image triggers multiple renderings
* &#91;Layers&#93; Crash on undo/redo
* &#91;Layers&#93; Crash when adding a Base Material
* &#91;Layers&#93; Crash when using an invalid image as environment light
* &#91;Layers&#93; Fix duplicate import when inserting a filter with several graphs
* &#91;Layers&#93; Reordering layers doesn't always work
* &#91;Project&#93; Crash when loading an incomplete project file
* &#91;Project&#93; Crash when opening a corrupted project
* &#91;Project&#93; Some assets can disappear from a project
* &#91;Properties&#93; Fix missing filter's presets
* &#91;UI&#93; Angle parameters cannot be set
* &#91;UI&#93; Filters metadata display in Asset panel
* &#91;UI&#93; Grouping by category hides filters
* &#91;UI&#93; Scroll issue in the Asset panel
* &#91;UI&#93; The export panel now has a scrollbar
* &#91;UI&#93; The thumbnail is not displayed for some image formats in image picker

**Known Issues:**

* &#91;Realtime Engine 2021&#93; Heavy computation can crash the application
* &#91;Realtime Engine 2021&#93; Realtime Engine 2021 will crash on a Windows machine with both AMD CPU and Nvidia GPU installed
* &#91;Color Picker&#93; Picking a color on a second monitor with a different resolution may not work

### 3.0.1 Waffle

*(Released: July 27, 2021)*

**Added:**

* &#91;Brush&#93; Enable colors in brush tool if the image input supports it
* &#91;Brush&#93; Holding the Shift key in the brush tool draws straight lines
* &#91;Brush&#93; Show a line preview when holding shift in the brush tool
* &#91;Brush&#93; Brush tool now supports undo and redo
* &#91;2D View&#93; Image input default color is used when painting
* &#91;Layers&#93; Read Substance input default value in SBSAR files
* &#91;Rendering&#93; Allow to combine height with normal
* &#91;Rendering&#93; Sub-surface scattering support (not available on MacOS)
* &#91;Assets&#93; Use SBSAR graph type to determine asset type
* &#91;Assets&#93; Better performance for search and asset discoverability in the Assets panel
* &#91;Assets&#93; Added a 'All Libraries' entry in the Assets panel that displays all assets of all your libraries
* &#91;Assets&#93; User can now choose to group assets by category or type
* &#91;Import&#93; Auto detect anisotropy, coat, sheen and specular edge color textures at import
* &#91;UI&#93; Replace elided panel title with an icon
* &#91;UI&#93; Textfields style update
* &#91;UI&#93; New description text in The Environment Light Template Creation window
* &#91;Application&#93; Export assets with the current resolution when sending to external application
* &#91;Application&#93; Material default resolution is now 2048\*2048 (1024\*1024 on macos)
* &#91;Content&#93; New patterns in the Floor tiles filter
* &#91;Content&#93; New Dual Color mode in the Color replace filter

**Fixed:**

* &#91;2D View&#93; First stroke in brush tool is sometimes broken
* &#91;2D View&#93; Free resources when brush tool is not visible
* &#91;2D View&#93; Use the right resize cursor in the transform widget
* &#91;2D View&#93; Widgets are not displayed if the user has panned in the 2D view before
* &#91;Application&#93; Crash when opening a project with broken workflow
* &#91;Application&#93; Fix application shutdown to prevent flooding the log with useless errors
* &#91;Application&#93; Redo, delete and save keyboard shortcuts don't work on some operating systems
* &#91;Application&#93; Undo/redo changing image usage in import layer is broken
* &#91;Export&#93; Emission color exported images have wrong name
* &#91;Export&#93; Environment is 8bit when using SBSAR export
* &#91;Export&#93; Remove extra spaces in exported image file names
* &#91;Export&#93; Replacing or deleting a custom export preset crashes
* &#91;Layers&#93; Avoid crash when there is an input count mismatch
* &#91;Layers&#93; Crash when inserting a Base Material layer
* &#91;Layers&#93; Filter input count is capped to default value
* &#91;Layers&#93; Redo erroneously changes the Blend type to Height blend
* &#91;Layers&#93; Remove drop zone above input headers
* &#91;Layers&#93; Layers are inserted at the wrong place around input headers
* &#91;Layers&#93; Reset all settings button does not reset drop down widgets values
* &#91;Layers&#93; Undo/redo when changing an image on the Image Import layer marks the project as modified and so to save
* &#91;Layers&#93; Usages may be stopped by blend layers
* &#91;Project&#93; Crash when loading a legacy project with missing dependencies folder
* &#91;Project&#93; Crash when using undo/redo after saving
* &#91;Project&#93; Opening a SBSAR file containing an environment light creates a material asset
* &#91;Project&#93; Renaming a material can trigger a thumbnail generation
* &#91;Project&#93; Saving after renaming a material marks the project as unmodified
* &#91;Project&#93; Some changes after renaming a material are not saved
* &#91;Rendering&#93; Bright dots are visible on the environment with 2020 realtime engine
* &#91;Rendering&#93; Crash when resizing using Real Time Engine 2021
* &#91;Rendering&#93; Recompute shadows on height level change
* &#91;Assets&#93; Connected folders stop indexing new assets when adding an invalid file
* &#91;Assets&#93; Crash when connecting a local folder with many materials
* &#91;UI&#93; 2D/3D view buttons missing tooltips
* &#91;UI&#93; All assets in the Assets panel are highlighted at launch
* &#91;UI&#93; Breadcrumbs sometimes disapears in the Assets panel when importing materials
* &#91;UI&#93; Changing language doesn't affect the Project panel
* &#91;UI&#93; Channel Settings panel shows legacy workflow information
* &#91;UI&#93; Correctly align "No settings for this item" text for filters with no tweaks in properties panel
* &#91;UI&#93; Elements are mis-aligned in the welcome screen and the preferences popup
* &#91;UI&#93; Panel titles have incorrect width
* &#91;UI&#93; Scrolling is sometimes broken in the Properties panel
* &#91;UI&#93; Splash screen has incorrect ratio and is blurry
* &#91;UI&#93; The fullscreen mode is not fullscreen
* &#91;UI&#93; Undocked panels are always on top even when the application is not active on MacOS
* &#91;UI&#93; Update welcome screen banner image
* &#91;Content&#93; Tiling filter doesn't process the ambient occlusion channel
* &#91;Content&#93; Quilt Stitch issue with the welt assembly seam selection and diamond pattern
* &#91;Content&#93; Emboss filter works in 256px by 256px
* &#91;Content&#93; Fix tiling issue with the Floor tiles when the offset is greater than 0

**Known Issues:**

* &#91;Realtime Engine 2021&#93; Heavy computation, crash the application
* &#91;Realtime Engine 2021&#93; Realtime Engine 2021 will crash on Windows machine with both AMD CPU and Nvidia GPU

### 3.0.0 Waffle

*(Released: June 23, 2021)*

**Added:**

* &#91;Branding&#93; Substance Alchemist becomes Adobe Substance 3D Sampler
* &#91;Branding&#93; New application icons
* &#91;UI&#93; New User Experience and User Interface
* &#91;UI&#93; New Splashscreen
* &#91;UI&#93; Panels are undockable and dockable in the interface
* &#91;UI&#93; Dock up to 3 panels in the same column
* &#91;UI&#93; Dock up to 3 panels in the same panel (Tabs)
* &#91;UI&#93; Undock panels to create a separate window in the same or a different screen
* &#91;UI&#93; Closed panels pop-over when clicking on their icons
* &#91;UI&#93; Re-arrange your left and right bar by moving panels icons
* &#91;UI&#93; New toolbar to access directly specific filters (Crop, Transform, Perspective Transform, Clone Stamp)
* &#91;UI&#93; New "Get Content" button in the left bar
* &#91;UI&#93; Import files directly in your assets with the Get Content button
* &#91;UI&#93; Import files directly to your Layers with the Get Content button
* &#91;UI&#93; Access directly Adobe Substance 3D Assets website with the Get Content button
* &#91;UI&#93; Resolution widget is now directly accessible in the viewport
* &#91;UI&#93; All UI elements now are loaded dynamically
* &#91;UI&#93; Shortcut - Use "2" to toggle the visibility of the 2D view
* &#91;UI&#93; Shortcut - Use "3" to toggle the visibility of the 3D view
* &#91;Welcome Screen&#93; Create a project in one-click with the New button
* &#91;Welcome Screen&#93; New artwork banner
* &#91;Project&#93; All projects are now associated to a unique file
* &#91;Project&#93; New project file extension .ssa
* &#91;Project&#93; Save as a project will ask you to select where to save your project
* &#91;Project&#93; Closing Sampler will ask you to save your project if not saved
* &#91;Project&#93; Closing Sampler will ask you to save your project if there are modifications since the last save
* &#91;Project&#93; The name of your project is displayed above the viewport
* &#91;Project&#93; The project name is in italics with a star if it is not saved or if it contains modifications since the last save
* &#91;Project&#93; Open a .ssa project file directly from your OS explorer
* &#91;Project&#93; Open a .sbsar from your OS explorer will launch Sampler with a new project with this .sbsar file ready to use
* &#91;Project&#93; Open a .alch (legacy Substance Alchemist file) from your OS explorer
* &#91;Project Panel&#93; New panel that will contain all assets created within a project
* &#91;Project Panel&#93; Create an asset (material or environment light) using the + icon
* &#91;Project Panel&#93; Right-click on asset opens a context menu
* &#91;Project Panel&#93; From the right-click context menu, you can delete an asset
* &#91;Project Panel&#93; From the right-click context menu, you can duplicate an asset
* &#91;Project Panel&#93; From the right-click context menu, you can rename an asset
* &#91;Project Panel&#93; Switching between assets won't lose modifications
* &#91;Resolution&#93; You can now set non-square resolution for all your assets
* &#91;Resolution&#93; The resolution value is saved by asset within a project
* &#91;Environment Light&#93; Create environment light within Substance 3D Sampler
* &#91;Environment Light&#93; When creating an environment light, dragging and dropping image(s) will display the Environment Light Creation Template Window
* &#91;Environment Light&#93; In the Environment Light Creation Template, select Environment Import to assign your image to the environment in the 3D view
* &#91;Environment Light&#93; In the Environment Light Creation Template, select HDR merge to create an environment light from several 360-degrees images with different exposure
* &#91;Environment Light&#93; In the Environment Light Creation Template, select "Use as bitmap" to edit your image(s) before creating an environment light
* &#91;Environment Light&#93; Assign the environment usage in the Image Import layer to directly assign the image to the environment in the 3D view
* &#91;Environment Light&#93; In the 2D view for the environment channel, there is an automatic color correction to have the rendering appear the same as in the 3D view
* &#91;Environment Light&#93; New dedicated content for environment light creation
* &#91;Assets Panel&#93; The Resources and Filters panels are merged in a new Assets panel
* &#91;Assets Panel&#93; The Assets panel now supports the following asset types: materials, filters and images
* &#91;Assets Panel&#93; All Starter Assets are accessible in the Starter Assets section
* &#91;Assets Panel&#93; Starter Assets section is read-only
* &#91;Assets Panel&#93; New "Your Assets" section
* &#91;Assets Panel&#93; "Your Assets" section is the place where you can import all your resources
* &#91;Assets Panel&#93; All assets in "Your assets" are added in a specific folder in your Documents
* &#91;Assets Panel&#93; Connect local folders in the Assets panel to add new sections
* &#91;Assets Panel&#93; The search will search in the current folder and its subfolders
* &#91;Assets Panel&#93; Navigate between folders and subfolders with breadcrumbs
* &#91;Assets Panel&#93; Filter the current folder by material, by filter or by image
* &#91;Assets Panel&#93; Combine several filters to get only materials and images
* &#91;Assets Panel&#93; Change the display by switching between a grid or a list
* &#91;Assets Panel&#93; Filters are represented with their icon
* &#91;Assets Panel&#93; Images are represented with their preview
* &#91;Assets Panel&#93; Increasing the width will change the layout of the panel with a specific view to navigate between folders
* &#91;Assets Panel&#93; On non read-only sections, delete an asset by dragging an dropping it on the bin icon
* &#91;Assets Panel&#93; Right-click on asset opens a context menu
* &#91;Assets Panel&#93; From the right-click context menu, access the asset metadata (name, category, location)
* &#91;Assets Panel&#93; From the right-click context menu, delete the asset (only available on non read-only sections)
* &#91;Assets Panel&#93; From the right-click context menu, browse your asset in Adobe Bridge
* &#91;Layers Panel&#93; New icon to directly add a base material on top of your layers
* &#91;Layers Panel&#93; Shortcut - Shift + B will add a base material on top of your layers
* &#91;Layers Panel&#93; Layers now have a thumbnail preview (Material thumbnail, filter icon or Image preview)
* &#91;Properties Panel&#93; New design of the Properties panel title with the asset name and the asset thumbnail
* &#91;Properties Panel&#93; Filter Layers now support presets
* &#91;Properties Panel&#93; On Image Import Layer, right-click on the image preview to edit the image in Photoshop
* &#91;Adobe Bridge&#93; Browse your Asset in Adobe Bridge, will launch Bridge at the location of the asset
* &#91;Adobe Photoshop&#93; Edit in Adobe Photoshop will open the image in Photoshop ready to be edited
* &#91;Adobe Photoshop&#93; At each save in Adobe Photoshop, the edited image will be reloaded in Sampler
* &#91;Substance 3D Designer&#93; Assets sent from Adobe Substance 3D Designer will arrive directly in the "Your Assets" section of the Assets panel
* &#91;Export&#93; Send assets directly to Adobe Substance 3D Painter and Adobe Substance 3D Stager
* &#91;Export&#93; Send materials and environment lights to Adobe Substance 3D Painter
* &#91;Export&#93; Send environment lights to Adobe Substance 3D Stager
* &#91;Rendering&#93; New material properties are now supported and rendered in 3D
* &#91;Rendering&#93; Adding Sheen support (Sheen color, Sheen opacity and Sheen roughness)
* &#91;Rendering&#93; Adding Coating support (Coat color, Coat Roughness, Coat Normal, Coat Specular Level and Coat IOR)
* &#91;Rendering&#93; Adding Anisotropy support (Anisotropy Level and Anisotropy Angle)
* &#91;Rendering&#93; Adding Specular Edge Color support
* &#91;Rendering&#93; Activate these new properties in the Channel Settings panel
* &#91;Rendering&#93; Introduction of a new Realtime Engine (2021) renderer in Beta
* &#91;Rendering&#93; Switch between the two Renderer versions in the Viewer Settings panel
* &#91;Rendering&#93; The Realtime Engine (2021) renderer supports translucency, absorption and scattering material properties
* &#91;Rendering&#93; The Realtime Engine (2021) renderer introduces a new way to compute shadows from the environment light
* &#91;Rendering&#93; The Realtime Engine (2021) renderer computes in realtime the irradiance of the environment light
* &#91;Shader Settings Panel&#93; New Shader Settings panel to tweak specific material shader parameters
* &#91;Shader Settings Panel&#93; New parameters (Normal scale, height scale, height level, Emission intensity, IOR, Coat normal intensity and Coat IOR)
* &#91;Shader Settings Panel&#93; Specific parameters for the Realtime Engine 2021 (Subsurface Scattering, Scattering Distance, Red Shift and Rayleigh Scattering)
* &#91;Shader Settings Panel&#93; The settings values are saved per asset
* &#91;Viewer Settings Panel&#93; Added a preview of the default environment lights
* &#91;Viewer Settings Panel&#93; Added a preview of the default meshes
* &#91;Viewer Settings Panel&#93; New environment opacity parameter
* &#91;Viewer Settings Panel&#93; New environment blur parameter (specific to the Realtime Engine 2021 renderer)
* &#91;Localization&#93; New translations in German and French
* &#91;Content&#93; New default starter materials
* &#91;Content&#93; New default environment lights
* &#91;Content&#93; All filters have been updated, cleaned, and optimized
* &#91;Content&#93; The Adjustment filter has been split into several filters
* &#91;Content&#93; New Brightness/Contrast filter
* &#91;Content&#93; New Hue/Saturation filter
* &#91;Content&#93; New Vibrance filter
* &#91;Content&#93; New Sharpen filter
* &#91;Content&#93; New Normal/Height adjustment
* &#91;Content&#93; New Panels filter
* &#91;Content&#93; New Smudge filter
* &#91;Content&#93; New Weaves filter
* &#91;Content&#93; New Warp transform filter
* &#91;Content&#93; New Height to AO filter
* &#91;Content&#93; New Height to Normal filter
* &#91;Content&#93; Color Replace - Replace in new supported channels (Sheen, Coating, Anisotropy,...)
* &#91;Content&#93; Color variation - Manual mode to select exactly the colors to change
* &#91;Content&#93; Tiling - option to visualize the seams cut
* &#91;Content&#93; Tiling - option to paint the seams cut for a perfect tiling
* &#91;Content&#93; Match - option to add a material to match its color and its roughness
* &#91;Content&#93; Match - it now works on images to match the color of another image
* &#91;Content&#93; Environment ligth - New Color Temperature filter
* &#91;Content&#93; Environment ligth - New Exposure filter
* &#91;Content&#93; Environment ligth - New Exposure Preview filter
* &#91;Content&#93; Environment ligth - New Nadir Patch filter
* &#91;Content&#93; Environment ligth - New Nadir Extract filter
* &#91;Content&#93; Environment ligth - New Lights filters (Sphere, Line, Shape, Plane)
* &#91;Content&#93; Environment ligth - New Panorama Patch filter
* &#91;Content&#93; Environment ligth - New Straighten Horizon filter
* &#91;Content&#93; Environment ligth - New HDR merge filter

**Known Issues:**

* &#91;Realtime Engine 2021&#93; Changing the layout, crash the application
* &#91;Realtime Engine 2021&#93; Heavy computation, crash the application
* &#91;Panels&#93; MacOS - Undocked panels are in front of all applications
* &#91;Widgets&#93; Transform and Positions widgets can disappear. Hide and Unhide the layer to make them appear.
* &#91;Export&#93; SBSAR export of an environment light loses the 32bit depth precision
* &#91;Assets Panel&#93; Assets can be highlighted when opening a folder
* &#91;Properties Panel&#93; Resetting the parameters doesn't reset the combobox UI
* &#91;Localization&#93; Changing language doesn't affect the project panel until it's recreated

## Version 2

### 2.3.2 (2020.3.2) Vermicelli

*(Released: February 23, 2021)*

**Added:**

* &#91;Localization&#93; Japanese support

**Fixed:**

* &#91;Layers&#93; Tweaking a material in the embroidery filter loses the embroidery image

**Known Issues:**

* Usage of Image to Material (AI powered) on high resolution images can be slow
* Content Aware Fill filters are slow in high resolution
* Coma or point can be ignored when typing a specific evalue in a slider
* Impossible to save twice the exact same material layer stack

### 2.3.1 (2020.3.1) Vermicelli

*(Released: December 17, 2020)*

**Added:**

* &#91;Engine&#93; Substance Engine update
* &#91;Application&#93; Environment variable to disable specific features
* &#91;Content&#93; Replace color - New Advanced segmentation option
* &#91;Content&#93; Floor Tiles - new patterns and options available
* &#91;Content&#93; Embroidery - Complete revamp of the filter
* &#91;Content&#93; Adjustment - New metallic parameter + opacity safe transform correction

**Fixed:**

* &#91;Layers&#93; Cannot import twice the same custom filter
* &#91;Layers&#93; Cannot use image input with the brush tool
* &#91;Export&#93; Export .jpg instead of .jpeg
* &#91;UI&#93; Update welcome screen image credits
* &#91;UI&#93; Fix invisible separator in menus
* &#91;UI&#93; Radio buttons display a tooltip when they are truncated
* &#91;UI&#93; Typo: Starter Materials
* &#91;Application&#93; UTF-8 characters in asset names do not work
* &#91;Localization&#93; Disable italic font style for chinese locale
* &#91;Localization&#93; Localized string split into 2 lines
* &#91;Localization&#93; Adjust folder name and replace with ellipsis if it's too long
* &#91;Localization&#93; Format numbers with thousand separator
* &#91;Localization&#93; Localize date and time display
* &#91;Localization&#93; Localize color picker on Windows
* &#91;Content&#93; Transform - With the safe transformation activated, the normal rotates correctly every 45°
* &#91;Content&#93; Surface relief - Fix tiling issue with perlin fractal noise (advanced noise)
* &#91;Content&#93; Brickwall Pattern - Height input in 16bit
* &#91;Content&#93; Material Icon Render - Specular reflections issue
* &#91;Content&#93; Color Variation - No color shift between color inputs and the result
* &#91;Content&#93; Color Variation - Performance update

**Known Issues:**

* Usage of Image to Material (AI powered) on high resolution images can be slow
* Content Aware Fill filters are slow in high resolution
* Coma or point can be ignored when typing a specific evalue in a slider
* Impossible to save twice the exact same material layer stack

### 2.3.0 (2020.3.0) Vermicelli

*(Released: October 26, 2020)*

**Added:**

* &#91;Image to Material&#93; Support of NVIDIA RTX 3000 series
* &#91;Image to Material&#93; New parameters to control the geometry details
* &#91;Image to Material&#93; New parameters to control the roughness
* &#91;Image to Material&#93; New parameters to control the delighting intensity
* &#91;Thumbnails&#93; New thumbnail generator based on Substance Designer's PBR renderer
* &#91;Thumbnails&#93; Update base materials and atlases to embed their thumbnail
* &#91;Thumbnails&#93; Retrieve the thumbnail from the .sbsar file if it exists
* &#91;Thumbnails&#93; Change thumbnail quality in the Preferences
* &#91;Engine&#93; Updated to Substance Engine version 8
* &#91;Localization&#93; Chinese localization
* &#91;UI&#93; Experimental Spot Colors Picker
* &#91;Content&#93; New Environment Map - Studio 06
* &#91;Content&#93; Add Atlas Generator filter
* &#91;Content&#93; Add Atlas Splitter filter
* &#91;Content&#93; Add Discarded Gums filter
* &#91;Content&#93; Add Fingerprints filter
* &#91;Content&#93; Add Scratches filter
* &#91;Content&#93; Add Surface Relief filter (replace height modulation filter)
* &#91;Content&#93; Add Warp filter
* &#91;Content&#93; Add Invert filter
* &#91;Content&#93; Add Colorize filter
* &#91;Content&#93; Add Replace Color fitler
* &#91;Content&#93; Transform - Add the possibility to deactivate the transformation on a specific channel
* &#91;Content&#93; Transform - Add rotation when safe transform is activated
* &#91;Content&#93; Color Variation - Add a segmentation option to choose how to distribute the colors

**Fixed:**

* &#91;Layers&#93; Properly update UI when doing multiple undo/redo actions
* &#91;Layers&#93; Prevent crashes when doing multiple undo/redo actions
* &#91;Layers&#93; Crash when using Image to Material (AI Powered), with log: invalid device ordinal
* &#91;Filters&#93; Improve NVIDIA graphics card detection for NVidia specific features
* &#91;Application&#93; Crash when closing the application
* &#91;Application&#93; Fix VRAM amount detection on MacOS
* &#91;Export&#93; Some export presets are sometimes missing
* &#91;Content&#93; Oil Paint Effect - Fix height range with high displacement amplitude
* &#91;Content&#93; Make It Tile Advanced - No washed out basecolor at export
* &#91;Content&#93; Make It Tile Advanced - White mask on the basecolor when the AO is too strong
* &#91;Content&#93; Adjustment - It works now on images (scan1, ...)

**Known Issues:**

* Usage of Image to Material (AI powered) on high resolution images can be slow
* Content Aware Fill filters are slow in high resolution
* Coma or point can be ignored when typing a specific evalue in a slider
* Impossible to save twice the exact same material layer stack

### 2.2.1 (2020.2.1) Udon

*(Released: July 21, 2020)*

**Added:**

* &#91;Layers&#93; In App Error message when Image to Material (AI-Powered) is out of memory

**Fixed:**

* &#91;Layers&#93; Image to Material (AI-Powered) does not work with Specular/Glossiness workflows
* &#91;Layers&#93; Crashes when out of video memory while using Image to Material (AI-Powered)
* &#91;Layers&#93; Disk cache is not used for display when opening a stack
* &#91;Layers&#93; Detection of Nvidia RTX 8000
* &#91;Layers&#93; It is sometimes impossible to move a layer outside a Splatter input
* &#91;Layers&#93; Disk cache is not used when inserting a stack in a stack
* &#91;Layers&#93; Some channel usages are computed although they are not used
* &#91;Layers&#93; Blank outputs are created sometimes when importing images
* &#91;2D View&#93; Switching to another layer with Draw mode active blocks pan and zoom
* &#91;Content&#93; Snow - 8bit issue on the normal map
* &#91;Content&#93; Pavement Pattern - 8 bits issue on the normal map
* &#91;Content&#93; Equalizer - 8 bits issue on the normal map
* &#91;Content&#93; Gravel Generator - 8 bits issue on the normal map
* &#91;Content&#93; Floor Tiles - Handle opacity and specular level
* &#91;Content&#93; Blender cycles eeve export preset - invert normal map
* &#91;Content&#93; Correct issue with huge images with Image to Material (AI Powered)
* &#91;Application&#93; Crash when choosing "Backup and Restart" on database error
* &#91;Application&#93; Crash when clicking quickly on the same asset
* &#91;Application&#93; Rare crashes on exit
* &#91;Application&#93; Crash when dropping files on the Welcome screen
* &#91;Application&#93; Crash when a corrupted environment file is loaded
* &#91;Application&#93; Rare crash when rapidly switching rendered asset
* &#91;Application&#93; Freeze when exiting while an asset is computing
* &#91;Application&#93; Rare crash on startup on macos
* &#91;Application&#93; Deadlock when closing the application soon after startup
* &#91;Rendering&#93; 3D view sometimes flickers
* &#91;UI&#93; Color picker and random seed widgets are not aligned with the rest of the tweaks
* &#91;Rendering&#93; Wrong computation time displayed
* &#91;Export&#93; Some export presets are sometimes missing

**Known Issues:**

* Usage of Image to Material (AI powered) on high resolution images can be slow
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Content Aware Fill filters are slow in high resolution
* Coma or point can be ignored when typing a specific evalue in a slider
* Impossible to save twice the exact same material layer stack

### 2.2.0 (2020.2.0) Udon

*(Released: June 15, 2020)*

**Added:**

* &#91;Create&#93; New Image to Material (AI powered) filter available on Windows and Linux
* &#91;Create&#93; Rename Bitmap to Material to Image to Material (B2M)
* &#91;Image Import&#93; New Material Creation Template Pop-up
* &#91;Image Import&#93; New "Add a base material" option
* &#91;Image Import&#93; Be able to drag and drop additional images in the Material Creation Template
* &#91;Image Import&#93; Be able to remove images in the Material Creation Template
* &#91;Image Import&#93; Assign channel to imported bitmaps automatically based on their filename
* &#91;Image Import&#93; Be able to invert normal maps
* &#91;2D View&#93; Introduction of a painting mode
* &#91;2D View&#93; The painting tiles
* &#91;2D View&#93; Set a greyscale value for the brush color
* &#91;2D View&#93; Pan and zoom while painting
* &#91;2D View&#93; X shortcut to invert brush greyscale value
* &#91;2D View&#93; &#91; and &#93; shortcuts to change the brush size
* &#91;2D View&#93; Ctrl (or Cmd) + Mouse wheel change the brush size
* &#91;2D View&#93; It is now possible to modify the source position when using Clone Patch
* &#91;Layers&#93; Shift + drag and drop to auto scatter atlases
* &#91;Layers&#93; Alt + drag and drop inserts a material as a decal
* &#91;Layers&#93; Expose easily transform matrices from Substance Designer
* &#91;Layers&#93; Dropping textures in a non-empty stack automatically assigns to the correct channels
* &#91;Layers&#93; New type of layer: Compound Filters
* &#91;Parameters&#93; Support Substance string inputs
* &#91;UI&#93; Added drop shadows for popups and menus
* &#91;UI&#93; New Color Widget with right click options (clear, copy, paste)
* &#91;UI&#93; New Image Widget with Painting tool option
* &#91;UI&#93; Be able to paint over an imported image in an image widget
* &#91;Rendering&#93; New default camera position
* &#91;Export&#93; Substance files are exported for Substance Designer 2020.1.2 (10.1.2)
* &#91;Performance&#93; Better application startup time
* &#91;Performance&#93; Improve asynchronous tasks handling
* &#91;Performance&#93; Improve layer stack performance when adding, removing or moving layers
* &#91;Performance&#93; Image to Material (AI powered) runs faster on RTX GPUs
* &#91;Content&#93; New meshes: Female T-Shirt, Male T-Shirt, Shoe
* &#91;Content&#93; New Blend Mode - Per Channel Blend
* &#91;Content&#93; Opacity blend height correction with 2 new parameters (height position and height scale)
* &#91;Content&#93; Add Height Adjustments in Height Blend mode
* &#91;Content&#93; Use Height information option in the Custom Mask Blend
* &#91;Content&#93; New Perspective Correction Tool
* &#91;Content&#93; Pattern Generator - Add a parameter to invert the pattern
* &#91;Content&#93; Pattern Generator - Add a new parameter Override Material Details
* &#91;Content&#93; New Decal filter
* &#91;Content&#93; New Moss filter
* &#91;Content&#93; New Cracks filter
* &#91;Content&#93; New PBR Validate filter
* &#91;Content&#93; New Floor Tiles filter
* &#91;Content&#93; New Quilt Stich filter
* &#91;Content&#93; Atlas Scatter - Add Custom Mask input to enable painting option
* &#91;Content&#93; Dirt - Add Custom Mask input to enable painting option
* &#91;Content&#93; CLO export preset
* &#91;Content&#93; VStitcher export preset
* &#91;Content&#93; Unity HDRP presets export a detailMap

**Fixed:**

* &#91;Layers&#93; Imported images are loaded too many times
* &#91;Layers&#93; Crash when creating a clone patch at the bottom of the stack
* &#91;Layers&#93; Adding a material at the bottom of the stack makes it unstable
* &#91;Layers&#93; Filter after image import works improperly
* &#91;Layers&#93; workflow\_type value is not updated when switching the workflow between projects with a custom filter
* &#91;Layers&#93; Disable "remove layer" button when no layer is selected
* &#91;Layers&#93; Crash when loading an asset containing a Clone Patch
* &#91;Layers&#93; Normal to Height filter crashes on MacOs
* &#91;Application&#93; Crash when loading back and forth environment maps
* &#91;Application&#93; Performance issues when some graphics tablet driver is installed
* &#91;Application&#93; EXR 32 bits files import are black
* &#91;Application&#93; Crashes when loading and unloading assets
* &#91;Application&#93; Crash when switching from explore to create
* &#91;Application&#93; Target collection when saving a material is not from current project
* &#91;Application&#93; Fix backup and restart
* &#91;Image Import&#93; Properly import grayscale images
* &#91;Content&#93; New filters for new matrix handling
* &#91;Content&#93; Imported custom filters are visible in the quick access bar
* &#91;Content&#93; Fix color shift with the Make it tile advanced filter
* &#91;Performance&#93; Opening a color dialog is slow and recomputes the current layer
* &#91;UI&#93; Keyboard shortcuts sometimes don't work
* &#91;2D View&#93; Content Aware Fill needs a useless first click to work
* &#91;Resources&#93; Folders in local disks are still watched for updates after removing them
* &#91;Resources&#93; Deleting a linked folder from filesystem doesn't remove it
* &#91;Export&#93; Custom usages in custom export presets are not exported
* &#91;Export&#93; Exporting .sbsar file with special characters in path fails

**Known Issues:**

* Repetetive recomputations of Image to Material (AI powered) can trigger a crash (out of memory)
* Repetetive recomputations of the Delighter can trigger a crash (out of memory)
* Usage of Image to Material (AI powered) on high resolution images can be slow
* Usage of Image to Material (AI powered) on GPU with low VRAM can trigger a crash (out of memory)
* Image to Material (AI powered) is not available on PBR Specular/Glossiness
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Content Aware Fill filters are slow in high resolution
* Coma or point can be ignored when typing a specific evalue in a slider
* Impossible to save twice the exact same material layer stack

### 2.1.1 (2020.1.1) Tiramisu

*(Released: April 01, 2020)*

**Added:**

* &#91;Project&#93; Export and import metadata
* &#91;Application&#93; Ctrl+S now saves a preset in Explore
* &#91;Performance&#93; Use render cache instead of recomputing saved materials for resolutions up to 2k

**Fixed:**

* &#91;UI&#93; Fixed computing indicator in the viewport
* &#91;UI&#93; Entering Negative values in sliders is fixed
* &#91;UI&#93; Combo boxes: keyboard arrows and scrollbar now work
* &#91;UI&#93; Keep the selected channel when switching between "Material Outputs" and "Layer Inputs" in the 2D view
* &#91;Layers&#93; Fixed crash when adding custom channels in Base Material
* &#91;Layers&#93; Crash when manipulating layers
* &#91;Layers&#93; Custom channels are not displayed with a saved material
* &#91;Application&#93; Fixed rare crash when importing an asset
* &#91;Application&#93; Crash on exit
* &#91;Application&#93; Combo boxes now show correct values when switching presets
* &#91;Export&#93; Renamed Enscape preset to Enscape Revit
* &#91;Export&#93; Importing an export preset after removing it works
* &#91;Export&#93; Crash at export
* &#91;Rendering&#93; Fixed rendering when the base color is in 16bit half float format
* &#91;Project&#93; Do not crash when importing corrupted package
* &#91;Project&#93; Handle 2019.1.4 to 2.x.x migration when Create has never been opened
* &#91;Project&#93; Fix a crash when importing the same project twice
* &#91;Project&#93; Fix a crash when importing projects
* &#91;Resources&#93; Custom filters imported in previous versions work
* &#91;Resources&#93; Materials with the same name no longer erase each other
* &#91;Resources&#93; Crash when linking a local folder
* &#91;Resources&#93; Starter Materials user-created folders are no longer removed after a restart
* &#91;Inspire&#93; Fix material/collection drop area and add a warning message if using an unsaved material

**Known Issues:**

* Content Aware Fill filters are slow in high resolution
* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Coma or point can be ignored when typing a specific evalue in a slider

### 2.1.0 (2020.1.0) Tiramisu

*(Released: March 12, 2020)*

**Added:**

* &#91;Export&#93; Export preset selction to pack your textures for renderers and game engines
* &#91;Export&#93; Export preset to Unreal Engine 4
* &#91;Export&#93; Export preset to Unity Standard
* &#91;Export&#93; Export preset to Unity HDRP
* &#91;Export&#93; Export preset to Blender Cycles/Eevee
* &#91;Export&#93; Export preset to Arnold 5
* &#91;Export&#93; Export preset to Corona Renderer
* &#91;Export&#93; Export preset to Enscape
* &#91;Export&#93; Export preset to Keyshot 9
* &#91;Export&#93; Export preset to Redshift
* &#91;Export&#93; Export preset to Vray Next
* &#91;Export&#93; Export preset to Lens Studio
* &#91;Export&#93; Export preset to Spark AR Studio
* &#91;Export&#93; Export preset to PBR Specular Glossiness from PBR Metallic Roughness
* &#91;Export&#93; New export UI
* &#91;Export&#93; Remember Export settings
* &#91;Export&#93; Import and manage your custom export presets
* &#91;Export&#93; Delete and replace your custom export presets
* &#91;Export&#93; Rename your custom export presets
* &#91;Export&#93; Set the default export resolution to the current resolution
* &#91;Export&#93; Add the choice to create a subfolder to the export location
* &#91;Export&#93; Warning message before replacing existing files
* &#91;Application&#93; New version numbering scheme
* &#91;Application&#93; Open Create at launch, and change labs order
* &#91;Welcome Screen&#93; New welcome banner
* &#91;Project&#93; Open last project at launch
* &#91;UI&#93; New combo box style
* &#91;2D view&#93; F shortcut to focus in the 2d view
* &#91;Filters&#93; Added support for alchemist::parameterVisibility tag in Substance graphs
* &#91;Filters&#93; Have a global tweak to manage parameter visibility based on your workflow
* &#91;Resources&#93; New command line option to setup resources and linked folders with a configuration file
* &#91;Version checker&#93; Configuration of the version check
* &#91;Content&#93; New starter materials
* &#91;Content&#93; Bitmap to Material - Add the possibility to define the metallic channel (uniform, custom image import, color picking)
* &#91;Content&#93; Adjustment - Add the support of the PBR specular/glossiness workflow
* &#91;Content&#93; Atlas Scatter - New parameters

**Fixed:**

* &#91;Project&#93; Crash when importing the same project twice
* &#91;Project&#93; Fixed crash when importing and opening projects several times
* &#91;Application&#93; Crash when loading an unnamed material
* &#91;Application&#93; Recognize missing files when re-importing them
* &#91;Application&#93; Fix random crash on shutdown
* &#91;Application&#93; Fixed rare crash when unloading an material in Create
* &#91;Application&#93; Fixed random crash when using UI controls
* &#91;Application&#93; Fixed export of log files to the Desktop on Windows 10
* &#91;UI&#93; Export panel has the wrong size when you open it in Create
* &#91;UI&#93; Open project with a single click
* &#91;UI&#93; Correctly set minimum and maximum slider values
* &#91;UI&#93; Show label of the channel usages instead of ids
* &#91;UI&#93; Clicking a material always opens/closes the tweak panel
* &#91;UI&#93; Fix hidden layers colors
* &#91;UI&#93; Welcome Screen buttons improvements
* &#91;Layers&#93; Less unnecessary recomputes
* &#91;Layers&#93; Crashes when using Clone Patch
* &#91;Layers&#93; Selecting an image import layer no longer triggers a compute
* &#91;Layers&#93; Clone Patch and Content Aware Fill layers no longer recompute when selected
* &#91;Channel settings&#93; Enabling or disabling usages now trigger a rendering
* &#91;Resources&#93; Prevent freeze when mass clicking on a stack in the library
* &#91;Resources&#93; Performance hit when re-adding a previously added linked folder
* &#91;Resources&#93; Fixed a crash when trying to open a deleted .sbsar file
* &#91;Performance&#93; Avoid loading materials to access their parameters
* &#91;Performance&#93; Backup assets only when used in a project or in an authored material
* &#91;Export&#93; Fixed materials in export queue sometimes skipped or exported with wrong parameters
* &#91;2D View&#93; Restored pan and zoom
* &#91;Content&#93; Parquet Pattern takes into account the Ambient Occlusion channel
* &#91;Content&#93; Paint - Display mask input when enabling custom mask
* &#91;Content&#93; Stonewall Pattern - Remove possible banding effects in the normal map
* &#91;Content&#93; Height Modulation - Correct double base color entries in the 2d view

**Known Issues:**

* Content Aware Fill filters are slow in high resolution
* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Coma or point can be ignored when typing a specific evalue in a slider

## Version 1

### 1.1.4 (2019.1.4) Sesame

*(Released: January 30, 2020)*

**Added:**

* &#91;Resources&#93; Confirmation prompt when clearing a resources folder

**Fixed:**

* &#91;Layers&#93; Move layers to two and more layers below or above
* &#91;Create&#93; Allocation of enough VRAM budget to have good performances

**Known Issues:**

* Importing a lot of resources can really slow down Substance Alchemist
* Content Aware Fill filters are slow in high resolution
* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Coma or point can be ignored when typing a specific evalue in a slider
* Normal to Height filter can crash on MacOS

### 1.1.3 (2019.1.3) Sesame

*(Released: January 28, 2020)*

**Added:**

* &#91;Workflow&#93; Support of multiple workflows
* &#91;Workflow&#93; Support of PBR Specular Glossiness workflow
* &#91;Workflow&#93; New Channel Settings panel
* &#91;Workflow&#93; Workflow selection at project creation
* &#91;Channel Settings&#93; Activate/Deactivate specific channel computation
* &#91;Channel Settings&#93; Display list of custom channels available in the current material
* &#91;Channel Settings&#93; Automatic computation of custom channels when required
* &#91;Channel Settings&#93; Force/Block computation of custom channels
* &#91;Layers&#93; New UI of material input placeholder in Atlas Scatter and Splatter filters
* &#91;Layers&#93; Image Input parameter of a filter can be fed by underneath layers
* &#91;Layers&#93; Display a notification when some layers are out of date
* &#91;Layers&#93; Possibility to update to the latest version of outdated layers via the notification
* &#91;Project&#93; New metadata fields at project creation
* &#91;Inspire&#93; Generated variations are specific to a project
* &#91;2D View&#93; Switch between the Layer inputs, layer outputs, and the material outputs
* &#91;Welcome Screen&#93; Add Import project (.alch) option
* &#91;Preferences&#93; New Preferences window to set cache location and analytics privacy settings
* &#91;UI&#93; New UI buttons
* &#91;Performance&#93; Overall improvement of the parallelization system
* &#91;Performance&#93; Optimization of the number of material computes
* &#91;Engine&#93; Substance Engine update
* &#91;Framework&#93; Upgrade to Qt 5.13
* &#91;MacOS&#93; Global improvements of macOS Catalina support
* &#91;Content&#93; Adjustment filter - Normal intensity and invert parameters

**Fixed:**

* &#91;Layers&#93; Unset Image Input parameter when deleting the layer
* &#91;Layers&#93; Fix a crash when adding a clone patch layer
* &#91;Layers&#93; Fix some crashes when blending layers stack materials in other layer stack materials
* &#91;Export&#93; Channels selection for export is now respected
* &#91;Resources&#93; Do not crash when navigating in the Resources panel
* &#91;Resources&#93; Fix crash when importing corrupted Substance files
* &#91;Resources&#93; Reduce the number of crashes when loading large folders
* &#91;Thumbnail&#93; Thumbnail computation doesn't freeze the interface
* &#91;Image Import&#93; Uniformization of image type supported across the application
* &#91;Preset&#93; Save the description when creating a preset from an SBSAR
* &#91;Inspire&#93; Fix image drag and drop
* &#91;Application&#93; Fix crashes at exit
* &#91;Application&#93; Fix crashes at the exit when exporting materials
* &#91;UI&#93; Fixes and improvements
* &#91;UI&#93; Rename temporary asset to "unsaved material"
* &#91;Content&#93; Global update and cleaning of all filters

**Known Issues:**

* Importing a lot of resources can really slow down Substance Alchemist
* Content Aware Fill filters are slow in high resolution
* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Coma or point can be ignored when typing a specific evalue in a slider
* Normal to Height filter can crash on MacOS

### 1.1.2 (2019.1.2) Sesame

*(Released: December 11, 2019)*

**Added:**

* &#91;Layers&#93; Save and Save as options are accessible via the interface in the layers stack toolbar
* &#91;Resources&#93; Clearer breadcrumb in the Resources panel to navigate through folders
* &#91;Resources&#93; Maintain back button pressed to access all upper folders
* &#91;Resources&#93; Add reload of imported materials option to update them to the latest version
* &#91;Layers&#93; Possibility to change the image in the Image import layer
* &#91;Layers&#93; Possibility to define an image as a channel (base color, normal, height,...) in the Image import layer
* &#91;Content&#93; New Atlas Scatter filter to scatter new atlas elements from Substance Source
* &#91;Content&#93; New Oil Paint Effect filter
* &#91;Content&#93; New Channels Generation filter to generate height, ambient occlusion and roughness from base color and normal maps

**Fixed:**

* &#91;UI&#93; Reactivate tooltips on Layers stack toolbar
* &#91;UI&#93; Fix issue when typing two decimals in a slider value
* &#91;Performance&#93; Fix crash when switching quickly between materials
* &#91;Export&#93; Switching to another material before the end of an export does not crash anymore
* &#91;Resources&#93; Context menu is displayed on top of the material when you right-click on it
* &#91;Layers&#93; The 'Click here' link is working when the layer stack is empty
* &#91;Presets&#93; Remove save button in the tweak panel when it's a material created in Alchemist
* &#91;Tweak&#93; Information message displayed when it's a material created in Alchemist
* &#91;Viewport&#93; Default value of Specular Level texture is corrected to 0.04
* &#91;File Menu&#93; Fix and rename Save and Save as option
* &#91;Engine&#93; Update Substance engine version to avoid crash of some SBSAR files during import.
* &#91;Content&#93; Tiling filter is working on the ambient occlusion channel
* &#91;Content&#93; Crop filter is working on the ambient occlusion channel
* &#91;Content&#93; Water filter modifies gain the height map
* &#91;Content&#93; Correct tiling of the top material in the opacity blend mode
* &#91;Content&#93; Height of the top material is preserved in the opacity blend mode
* &#91;Content&#93; Possible to add a custom mask, custom pattern or a scale map in the Perforation filter
* &#91;Content&#93; Height Modulation filter forces height and normal maps in 16 bits
* &#91;Content&#93; Adjustment filter forces height and normal maps in 16 bits

**Known Issues:**

* Importing a lot of resources can really slow down Substance Alchemist
* Content Aware Fill filters are slow in high resolution
* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Coma or point can be ignored when typing a specific evalue in a slider
* Normal to Height filter can crash on MacOS

### 1.1.1 (2019.1.1) Sesame

*(Released: November 26, 2019)*

**Added:**

* &#91;Blend&#93; New opacity Blend mode
* &#91;Engine&#93; New Substance Engine version

**Fixed:**

* &#91;Layers&#93; Fix crash while deleting a layer that is still computing
* &#91;Layers&#93; Fix crash while removing the bottom layer
* &#91;Layers&#93; Fix crash while the material name contains special characters
* &#91;Layers&#93; Stop computing every filters that use a widget
* &#91;Layers&#93; Avoid crash while using Clone Patch and Content Aware Fill filters
* &#91;Layers&#93; Fix crash while drag and droping a filter in a splatter input slots
* &#91;Resources&#93; Fix crash while linking local folders or importing resources in Substance Alchemist
* &#91;Collection&#93; Fix crash while switching rapidly between materials
* &#91;UI&#93; Fix crash while value is null or not valid in tiling, displacement sliders on the viewport
* &#91;Inspire&#93; Fix crash while accessing the Inspire tab
* &#91;Inspire&#93; Fix crash while inspiring on a just saved layers stack material
* &#91;Performance&#93; Heavy Substance materials and Filters (Tiling) compute faster
* &#91;Help&#93; Fix export log file
* &#91;Content&#93; Randomizer filter works on all channels
* &#91;Content&#93; Multiangle workflow takes all scans into account
* &#91;Content&#93; AO Blend correct blending
* &#91;Content&#93; Curvature Blend correct blending
* &#91;Content&#93; Color ID Blend correct blending
* &#91;Content&#93; Custom Mask Blend correct blending
* &#91;Content&#93; Fix Adjustment filter for roughness modification
* &#91;Content&#93; Fix Base Material filter for custom normal channels upload
* &#91;Content&#93; Fix Custom Import pattern of the Embossing filter

**Known Issues:**

* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Coma or point can be ignored when typing a specific value in a slider
* Normal to Height filter can crash on MacOS

### 1.1.0 (2019.1.0) Sesame

*(Released: November 04, 2019)*

**Added:**

* &#91;Project&#93; Creation of a project
* &#91;Project&#93; Introduction of the .alch file format that contains project data
* &#91;Project&#93; Export a .alch project containing the collections and their materials
* &#91;Project&#93; Import a .alch project
* &#91;Project&#93; Open recent projects
* &#91;Welcome Screen&#93; A welcome screen is displayed at the launch
* &#91;Welcome Screen&#93; Create a project from the welcome screen
* &#91;Welcome Screen&#93; Access the list of all your projects in the welcome screen
* &#91;Welcome Screen&#93; Quick links to access the documentation, the about popup and license management
* &#91;File Menu&#93; Integration of a file Menu
* &#91;File Menu&#93; Access the project commands from the File tab and the save of the layer stack
* &#91;File Menu&#93; Access the undo and redo commands from the Edit tab
* &#91;File Menu&#93; The previous help menu moved in the file menu under the Help tab
* &#91;Layers&#93; New architecture of the layer stack
* &#91;Layers&#93; New UI of the layer stack
* &#91;Layers&#93; Select the blend mode directly on the toolbar
* &#91;Layers&#93; Access separately the blend parameters and the material parameters
* &#91;Layers&#93; Add materials directly in dedicated inputs of the Splatter filter in the layer stack
* &#91;Layers&#93; Change scan order directly in the Image import layer
* &#91;Viewport&#93; Control of the camera field of view
* &#91;Viewport&#93; Possibility to switch between orthographic or perspective camera
* &#91;Viewport&#93; Display resolution and bit depth information for each channel
* &#91;Resources&#93; Base Materials is opened per default
* &#91;Cache&#93; Locate your thumbnail cache folder
* &#91;Cache&#93; Locate your render cache folder
* &#91;Panels&#93; Material Settings panel is temporarily hidden
* &#91;Workflow&#93; Specular/Glossiness temporarily deactivated
* &#91;MacOS&#93; Catalina OS version notarization
* &#91;Content&#93; New version of the Delighter filter
* &#91;Content&#93; New Image Content Aware Fill filter
* &#91;Content&#93; New Material Content Aware Fill filter
* &#91;Content&#93; Transform filter has a safe transform option

**Fixed:**

* All previous bugs related to Create are invalid today with new UI and architecture release
* Tooltips don't hide the icons in the top bar (3D, 2D, 2D/3D)
* &#91;Content&#93; Splatter filter accepts Atlas with complete height map
* &#91;Content&#93; Transform filter works on images (scan1, scan2,...)

**Known Issues:**

* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Coma or point can be ignored when typing a specific value in a slider
* Normal to Height filter can crash on MacOS

## Beta

### 0.8.1-beta Quinoa

*(Released: August 19, 2019)*

**Added:**

* Ability to send Substance Source assets from the launcher to Project Substance Alchemist

**Fixed:**

* &#91;Create&#93; Some filters were listed in the quick accessor but not in the filter panel
* &#91;MacOS&#93; Fixed some crashes at exit

**Known Issues:**

* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Fast visibility toggle of a Delighter stage is not recommended
* Tif images are not showing in Properties panel in the Image import layer
* Coma or point can be ignored when typing a specific value in a slider
* Normal to height filter can crash on MacOS
* Can still crash randomly when exiting on MacOS

### 0.8.0-beta Quinoa

*(Released: August 08, 2019)*

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

### 0.7.0-beta Pepper

*(Released: June 13, 2019)*

**Added:**

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
* &#91;Help&#93; URLs are updated to substance3d.com domain
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

**Fixed:**

* Fix a crash when saving the layer stack
* Possible to add a value above 1 in the environment rotation slider
* Do not lose blend parameters when a blend layer is transformed back and forth from blend layer to material layer
* Fix duplicates when generating variations of the same layer stack multiple times
* When re-opening a material, Alchemist remembers the modified ranges (min and max) of your sliders

**Known Issues:**

* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Fast visibility toggle of a Delighter stage is not recommended
* Custom Environment Import can become black
* Tif images are not showing in Properties panel in the Image import layer
* Coma or point can be ignored when typing a specific value in a slider
* Normal to height filter can crash on MacOS

### 0.6.1-beta Orange

*(Released: June 13, 2019)*

**Added:**

* &#91;Engine&#93; Substance Engine update to be compatible with the latest Substance Designer version
* &#91;License&#93; Update license folder for first installations
* &#91;Layers&#93; Reload at any time your layer stack to update your custom filters

**Fixed:**

* &#91;Data Compatibility&#93; Preventive fix to limit data corruption at upgrade time

**Known Issues:**

* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Fast visibility toggle of a Delighter stage is not recommended
* Custom Environment Import can become black
* Tif images are not showing in Properties panel in the Image import layer
* Coma or point can be ignored when typing a specific value in a slider

### 0.6.0-beta Orange

*(Released: April 18, 2019)*

**Added:**

* &#91;Metadata&#93; See and fill materials metadata in a dedicated tab
* &#91;Collection&#93; Create a collection directly from the search results
* &#91;Media Publishing&#93; Export a board of a collection
* &#91;UX&#93; Undo a tweak change or image import by pressing Ctrl+Z
* &#91;UX&#93; Redo a tweak change or image import by pressing Ctrl+Shift+Z
* &#91;UI&#93; New icons with a new style
* &#91;Performance&#93; New Session manager to better handle the tabs switching
* &#91;Performance&#93; Faster opening of the Image Import layer
* &#91;Content&#93; New Metal generic material
* &#91;Content&#93; New Rust material
* &#91;Content&#93; New Stone generic material
* &#91;Content&#93; Embossing filter update
* &#91;Content&#93; Embroidery filter update
* &#91;Content&#93; Paint filter update
* &#91;Content&#93; Delighter filter update

**Fixed:**

* &#91;Content&#93; Water filter is working in the Specular/Glossiness workflow
* Fix greyscale radio button in the activation pop-up
* Accept files containing coma character
* Fix small font issues on pop-up windows
* Fix transparency UI issue due to a conflict with the FXAA parameter of some NVIDIA cards
* Remove the focus of the field after entenring a value in a slider
* Allocate the minimum amount of VRAM to the delighter to reduce crashes
* Fix window freeze when resizing the application window
* Fixed a crash when the layer stack was deleted while being evaluated

**Known Issues:**

* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Fast visibility toggle of a Delighter stage is not recommended
* Custom Environment Import can become black
* Tif images are not showing in Properties panel in the Image import layer
* Coma or point can be ignored when typing a specific value in a slider

### 0.5.4-beta Nacho

*(Released: March 26, 2019)*

**Fixed:**

* &#91;Stack&#93; Crash when removing a splatter layer
* &#91;Data&#93; Asset database gets corrupted when application crashes
* &#91;Data&#93; Substance Alchemist cannot start when the asset database is corrupted
* Random crash when importing Substance materials

**Known Issues:**

* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Fast visibility toggle of a Delighter stage will affect performance
* Custom Environment Import can become black
* Tif images are not showing in Properties panel in the Image import layer
* Coma or point can be ignored when typing a specific value in a slider
* Default collection to save to can be empty

### 0.5.3-beta Nacho

*(Released: March 19, 2019)*

**Added:**

* Search by material name in the Resources panel
* &#91;UI&#93; Clone Tool new UI with brush size visualization
* &#91;UI&#93; Select and delete hidden stages
* &#91;UI&#93; New Textfield UI
* &#91;Help&#93; Access Substance Source, Substance Share and Substance academy websites
* &#91;Content&#93; New default materials with generators and atlas
* &#91;Content&#93; Bitmap to Material Update
* &#91;Content&#93; Dirt Update
* &#91;Content&#93; Rust Update
* &#91;Content&#93; New Embossing filter
* &#91;Content&#93; New Embroidery filter
* &#91;Content&#93; New Erode filter
* &#91;Content&#93; New Gravel Generator
* &#91;Content&#93; New Paint filter
* &#91;Content&#93; New Parquet Pattern filter
* &#91;Content&#93; New Pavement Pattern filter
* &#91;Content&#93; New Perforation filter
* &#91;Content&#93; New Splatter filter
* &#91;Content&#93; New Textile Wear filter
* &#91;Content&#93; New Transform filter

**Fixed:**

* &#91;Viewport&#93; Sphere mesh with tiling x2 on X
* &#91;Viewport&#93; Crash when loading your own environment
* &#91;Viewport&#93; Environment map are now using the exposure value too
* &#91;Viewport&#93; F shortcut doesn't reset camera angle
* &#91;Export&#93; SBS export works with latest Substance Designer 2018.3.3
* &#91;Export&#93; SBSAR export respects the same guidelines as Substance Source materials
* &#91;UI&#93; Scrollbars can be dragged
* Special characters are supported on folder and file paths
* Thumbnail is re-generated when you're saving your material

**Known Issues:**

* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Fast visibility toggle of a Delighter stage will affect performance
* Custom Environment Import can become black
* Tif images are not showing in Properties panel in the Image import layer
* Coma or point can be ignored when typing a specific value in a slider
* Default collection to save to can be empty

### 0.5.2-beta Nacho

*(Released: March 07, 2019)*

**Added:**

* Detection and usage of the high profile GPU

**Fixed:**

* Rotation parameter has a proper slider widget
* Fix the blue color line visiblity when drag and dropping materials
* Fix materials blending when dropping a material below the first layer
* Plug image inputs only if a custom image path is not set

**Known Issues:**

* Special characters in filepath prevent for saving of a material
* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Fast visibility toggle of a Delighter stage will affect performance
* Crash when loading your own environment

### 0.5.1-beta Nacho

*(Released: March 04, 2019)*

**Fixed:**

* Fix Crash report, bug report and licenses pop-ups

**Known Issues:**

* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Fast visibility toggle of a Delighter stage will affect performance
* Crash when loading your own environment

### 0.5.0-beta Nacho

*(Released: February 28, 2019)*

**Added:**

* &#91;Layer stack&#93; Layer re-ordering
* &#91;Layer stack&#93; Delete an hidden layer
* &#91;Layer stack&#93; Import a material directly at the position of your choice
* &#91;Layer stack&#93; Material input as a new filter parameter type
* &#91;Performance&#93; Substance Engine budget is dynamic for better performances
* &#91;Performance&#93; Better OpenGL performances especially on MacOS
* &#91;Data&#93; Faster data upgrade after a new version is released
* &#91;Content&#93; AI Delighter available on Windows 7 and Windows 8
* &#91;Content&#93; AI Delighter available on RTX GPU

**Fixed:**

* Fix possible crashes when quitting the application
* Export Pop-up opens faster when exporting large collections

**Known Issues:**

* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Fast visibility toggle of a Delighter stage will affect performance
* Crash when loading your own environment

### 0.4.0-beta Muffin

*(Released: January 17, 2019)*

**Added:**

* &#91;Export&#93; Substance archive (sbsar) export of your collection
* &#91;Export&#93; Substance file (sbs) export of your collection
* &#91;Export&#93; Export queue visible in the Export panel
* &#91;Export&#93; Name your collection or material before export
* &#91;Data&#93; Save As your material by pressing Ctrl+Shift+S
* &#91;Data&#93; Save your material by pressing Ctrl+S
* &#91;Data&#93; Collections and Materials are compatible across versions
* &#91;Data&#93; Update your material layer stack with up-to-date filters
* &#91;Data&#93; Hot reload of imported custom filters
* &#91;UI&#93; Visual feedback in the viewport while it's computing
* &#91;UI&#93; New button style
* &#91;UI&#93; Save pop-up displays the name of the active collection
* &#91;UI&#93; Modify source images of an Image(s) Import Layer
* &#91;Content&#93; Custom usages are now supported
* &#91;Content&#93; More images format are supported in image input parameters
* &#91;Content&#93; New Tiling Filter named Make It Tile Advanced
* &#91;Content&#93; Update of the Water filter

**Fixed:**

* Bitmap to Material handles the Specular/Glossiness workflow

**Known Issues:**

* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Delighter is not supported on RTX GPU card
* Fast visibility toggle of a Delighter stage will affect performance

### 0.3.1-beta Lasagna

*(Released: December 17, 2018)*

**Fixed:**

* Generate a color variation with 10 color extracted crashes
* Generate a color variation with a just saved layer stack crashes
* Incorrect links on the Substance Alchemist version update pop-up

**Known Issues:**

* Bitmap to Material doesn't handle the Specular/Roughness workflow
* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Fast visibility toggle of a Delighter stage will affect performance

### 0.3.0-beta Lasagna

*(Released: December 12, 2018)*

**Added:**

* &#91;Export&#93; New Export pop-up
* &#91;Export&#93; Export an entire collection
* &#91;Export&#93; Export Bitmaps at the format of your choice
* &#91;Export&#93; Export Bitmaps at the resolution of your choice
* &#91;Export&#93; Export only the channels of your choice
* &#91;Export&#93; Preview the estimation size of your export
* &#91;Export&#93; Preview the available size on your disk before exporting
* &#91;UX&#93; Actions on collection accessible using right-click
* &#91;UX&#93; Allow to unset an image or an asset in Inspire
* &#91;UX&#93; Substance Alchemist is launched maximized
* &#91;Assets&#93; New way of saving your materials in order to keep them persistent with next versions
* &#91;Help&#93; Access to the online documentation via the help menu
* &#91;Performance&#93; Faster color variations on complex materials created with Substance Alchemist
* &#91;Performance&#93; Reduce memory leaks when switching Labs
* &#91;Content&#93; Scale checker to diagnostic the physical size of your material
* &#91;Content&#93; Update Italien Venice Mosaic tile material
* &#91;Content&#93; Update Moss splatter

**Fixed:**

* No more default name when saving a material
* Filters parameters are lost after saving a material and reopening Substance Alchemist
* &#91;Content&#93; Fix from bottom and from top logic for AO and curvature blending

**Known Issues:**

* Materials created with a previous version won't be available in the new one.
* Bitmap to Material doesn't handle the Specular/Roughness workflow
* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Fast visibility toggle of a Delighter stage will affect performance

### 0.2.0-beta Kiwi

*(Released: November 09, 2018)*

**Added:**

* Viewer Settings are saved from one session to another
* Material Settings are saved from one session to another
* Fast loading of the Properties Panel
* &#91;Log&#93; Export log file via the help menu
* &#91;UI&#93;New Sliders Style
* &#91;UI&#93;Presets and Tweak panels are merged
* &#91;UI&#93;New Thumbnails style
* Displacement, Tiling and Shadows settings accessible directly in the viewport
* &#91;Content&#93; New Default Materials
* &#91;Content&#93; Moss Splatter update
* &#91;Framework&#93; Update Substance Engine Framework

**Fixed:**

* Deletion of your layer stack by switching Labs is fixed
* Loading time values displayed in the viewport are correct
* Material workflow default channels are correctly initialized
* Disable Custom Mesh Import
* Bitmap export
* &#91;MacOS&#93; Closing Substance Alchemist can need a "Force to quit"

**Known Issues:**

* Materials created with a previous version won't be available in the new one.
* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Fast visibility toggle of a Delighter stage will affect performance

### 0.1.1-beta Jam

*(Released: October 24, 2018)*

**Added:**

* BaseColor Delighter is now available
* Access Substance Alchemist information via the Help menu
* Get notified when a new version of Substance Alchemist is available
* The console is not visible anymore on Windows
* New Thumbnails style
* &#91;MacOS&#93; Substance Alchemist can be set in full screen
* &#91;Filter&#93; Import Custom mask to manage the blending between two materials
* &#91;Filter&#93; Control Moss scale
* &#91;Filter&#93; Clone Patch update

**Fixed:**

* Add an image in an image input in the parameter list updates outputs
* Import Custom filter doesn't add a black Ambient Occlusion and a black opacity

**Known Issues:**

* Materials created with a previous version won't be available in the new one.
* &#91;MacOS&#93; Closing Substance Alchemist can need a "Force to quit"
* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Fast visibility toggle of a Delighter stage will affect performance
* Material export can crash

### 0.1.0-beta IceCream

*(Released: October 17, 2018)*

**Added:**

* Material Blend with 4 blend types (Height Blend, Sample Blend, Curvature Blend, AO Blend)
* Introduce Caching mechanism to optimize layer stack re-calculations
* Auto-selection of a material in Inspire if presents in the viewport
* Normal format centralized in the Material Settings panel
* Crop and Tiling Widgets controls (-90xB0,+90xB0, make square,...) cleaning
* New Snow filter

**Fixed:**

* Panel UI cleaning
* Viewport flickering when resizing window and panels
* Layer stack not recalculated when saved
* Assets naming in the interface use labels instead of graph names

**Known Issues:**

* Stretched liure by switching the layer visibility quickly
* Focus resets Camera angle
