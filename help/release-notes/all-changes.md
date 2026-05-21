---
helpx_url: 'https://helpx.adobe.com/substance-3d-sampler/release-notes/all-changes.html'
breadcrumb-title: ''
description: Review all changes and updates across Substance 3D Sampler versions to track feature evolution and improvements over time.
helpx_description: Sampler > Release Notes > All Changes
title: All Changes
user-guide-description: ''
user-guide-title: ''
---

# All Changes

This page regroups all the changes that happened to Substance 3D Sampler, from new features to bug fixes.

## Version 6

### **6.0.1**

*(Released: May 21st, 2026)*

#### **Added:**

* \[Application\] Warn user when opening a project with 3D objects or environment lights
* \[Captis\] Make the UI adapt to small screens
* \[Captis\] Update Captis UI
* \[Channel Settings\] Automatically activate SSS when using SSS channel in ASM
* \[Engine\] Update Substance Engine to version 9.4.3
* \[Preset\] Switch 'apply preset thumbnail values' on by default
* \[Resources\] Display 'all libraries' by default instead of 'starter assets' in resources panel
* \[Scripting\] Add Python functions to manage 'Applied to' of a layer
* \[UI\] Asset list is now responsive: asset size adapts to the container
* \[UI\] Display 3D/2D view by default
* \[UI\] Display material optimization popup when dropping a material from explorer
* \[UI\] Enable flipping of device bar buttons tooltip

#### **Fixed:**

* \[Application\] Fix color space issues
* \[Application\] Fix settings updater
* \[Application\] Make scan channels active when they are set to auto
* \[Application\] New project button from home screen no longer erases previous project with same name
* \[Application\] Prevent a crash at exit on macOS
* \[Application\] Prevent accessing asset of invalid asset references
* \[Application\] Prevent crash when accessing surface from VersionedImage in a tweak
* \[Application\] Prevent crash when deleting a stage when there is none
* \[Captis\] Ensure Captis is disconnected before closing Sampler
* \[Captis\] Prevent USB-2 warning from being displayed twice
* \[Channel Settings\] Fix OpenPBR channel names
* \[Channel Settings\] Update long labels for OpenPBR channels
* \[Content\] Update all mesh units from meters to centimeters for SSS values
* \[Export\] Ensure default values are plugged to dynamic filters
* \[Export\] Images are now saved in a worker thread for improved performance
* \[Filters\] Content Aware Fill crashes when switching scale on
* \[Filters\] Could not open location of a dynamic filter from asset panel
* \[Filters\] Fix reset all in AutoTiling adjustment step
* \[Filters\] Restore disable usage processing in tree structures creation
* \[Filters\] Set the correct default value for upscale parameter
* \[Filters\] Update generators even if they are in a fill layer
* \[Layers\] Forbid renaming input layer header or placeholder layers
* \[Layers\] Prevent crash during layer insertion due to a dangling pointer
* \[Layers\] Wrong number of images in flatten layer name
* \[Localization\] Ensure preset names are updated when switching languages
* \[Localization\] Multiple translation issues in resources panel
* \[Localization\] Quick Actions categories localization issues
* \[Performance\] Load tweaks only on opened section
* \[Preferences\] Clearing preference cache path resets to previous value
* \[Rendering\] Memory leak when using Path Tracer
* \[Rendering\] Prevent deleting textures while they may still be accessed by Vulkan
* \[Rendering\] Texture rotation was not converted from 0-1 to 0-360
* \[Scripting\] Remove nonexistent classes from Python documentation
* \[Scripting\] selectedAsset returns None if there is no selected asset
* \[Tools\] Resetting a texture value now stops painting and clears patch view
* \[UI\] Do not close sections in properties panel whenever something is tweaked
* \[UI\] Exposed color tweak label invisible on hover
* \[UI\] Fix asset list responsive behavior
* \[UI\] Fix binding loop in AssetItem tooltip
* \[UI\] Fix doubleclick on selected preset group
* \[UI\] Fix drop area in image presenter
* \[UI\] Fix label with a button in it for all languages
* \[UI\] Fix line height for Japanese in channel list popup
* \[UI\] Fix onAccepted signal of length field
* \[UI\] Fix popup width with long left control item
* \[UI\] Fix preview popup in asset items
* \[UI\] Fix rough/reflective picker
* \[UI\] Fix string ellipsis
* \[UI\] Fix string truncation problem
* \[UI\] Fix switch tweak reset button
* \[UI\] Hide the Material model dropdown when a custom export preset is selected
* \[UI\] Remove resolution in channel list of export popup
* \[UI\] Reset to default layout keeps projection viewer settings
* \[UI\] Restore 'Edit in Photoshop' and 'Edit in Illustrator' menu items

#### Removed:

* \[UI\] Remove 'Applied to' section for image import layers
* \[UI\] Remove auto-open quick action tooltip at first launch

## Version 5

### **5.1.3 ÎLE FLOTTANTE**

*(Released: January 6, 2026)*

#### Added:

* \[Captis\] Display a warning if the FTP protocol is disabled by the firewall

#### Fixed:

* \[Captis\] Aborting during a capture can lead to errors
* \[Captis\] Downloading the results at the end of a capture uses to much RAM
* \[Captis\] Executing an auto-focus immediately after an auto-intensity can lead to errors
* \[Captis\] The display of HDR results in the Summary panel
* \[UI\] In some cases, the folder dialog on MacOS does not select the right folder

### **5.1.2 ÎLE FLOTTANTE**

*(Released: November 20th, 2025)*

#### Added:

* \[Application\] Detect graphics device loss, warn the user and exit gracefully
* \[Layers\] Improved messaging when flattening layers
* \[Layers\] Improved thumbnails for Image Import and Flattened Layers layers
* \[Onboarding\] Updated learning content on the Home screen
* \[Project\] Recover last saved state of session before crash
* \[UI\] Application icon update

#### Fixed:

* \[Application\] Inserting a material in the layer stack might lead to a crash on macOS
* \[Application\] Possible crash on heavy load on macOS
* \[Application\] Possible crash when adding layers when video memory is full
* \[Application\] Possible crash when opening a project
* \[Captis\] Failure if auto focus is run shortly after automatic intensity calibration
* \[Captis\] Reliability and performance issues after first capture
* \[Captis\] Slowdowns and errors when copying files at the end of a capture
* \[Captis\] Small memory leak when querying Captis device information
* \[Export\] Multi slider exposed parameters produce corrupted .sbsar files
* \[Layers\] Auto tiling pattern is reset to default values when switching assets
* \[Layers\] Default custom base color is displayed red
* \[Layers\] Partial flattening of Clone Stamp child layers is possible and causes rendering issues
* \[Layers\] Possible crash when tweaking a layer stack while rendering is in progress
* \[Layers\] Unexpected error in auto tiling region of interest step when changing source channels
* \[Project\] Incorrect thumbnail sometimes when creating a new material
* \[Quick Actions\] Some quick actions have a wrong input count
* \[UI\] Action group button have different widths
* \[UI\] Clear button in text fields sometimes triggers focus loss
* \[UI\] Combo boxes and text fields are too big
* \[UI\] Icons and labels are misaligned
* \[UI\] Name field label is incorrectly placed
* \[UI\] Quick Actions button labels are misaligned
* \[UI\] Sliders show too wany trailing 0s

#### Removed:

* \[Generative AI\] Generative AI features removal. *This feature has been removed from the application and the service will stop working in previous versions of Sampler on March 5th.*

### **5.1.1 ÎLE FLOTTANTE**

*(Released: September 18th, 2025)*

#### Added:

* \[2D View\] Be able to zoom out more in the 2D view for high resolution textures
* \[Captis\] Warn users about issues when copying files
* \[Layers\] When duplicating a layer, use an incremental number in the new layer name

#### Fixed:

* \[2D View\] When painting strokes after resetting all the properties of Clone Stamp, previously created strokes reappear
* \[Application\] "Save current project?" popup uses wrong project name
* \[Application\] Crash at exit
* \[Application\] Potential crash
* \[Application\] Sometimes, a thumbnail is generated with an incorrect material
* \[Captis\] On some devices, when performing a scan in high resolution, the height map is black
* \[Captis\] The "Start capture" button is not disabled anymore when no capture name is set and when a calibration is running
* \[Export\] When exporting a .sbsar file the export can fail without the user being notified
* \[Filters\] Advanced parameters screen for the Auto Tiling filter sometimes flicker when tweaking parameters
* \[Filters\] Default parameters for the Tiling filter produce gray artifacts in the output
* \[Filters\] Sometimes with high resolution inputs, the Auto Tiling filter advanced settings do not show the individual pattern points
* \[Filters\] The pattern size for the custom size Auto Tiling parameter has an incorrect default value
* \[Layers\] Occasional color issue with the Auto Tiling filter mostly visible on red materials
* \[Layers\] Sometimes adding layers will reset some tweaks to their default value
* \[Physical Size\] Thumbnail of assets with a physical size have a wrong height scale
* \[UI\] Cannot rename exposed parameters
* \[UI\] Channel activation button are not square
* \[UI\] If a slider label is too long, the reset button is not accessible
* \[UI\] Pressing the return key or clicking out does not remove the focus from text fields
* \[UI\] Sometimes an unwanted tooltip appears in the Physical Size panel
* \[UI\] The 3D view displays an incorrect mesh when creating an empty project
* \[UI\] When exposing a color picker input, its label disappears on hover
* \[UI\] When exposing parameters, the color dot is sometimes incorrectly positioned

### **5.1.0 ÎLE FLOTTANTE**

*(Released: August 7th, 2025)*

#### Added:

* \[2D View\] Brush size now adapts to the current texture resolution
* \[3D View\] Toggle Native Display Scale for 3D Rendering in the preferences
* \[Application\] Rendering engine update
* \[Captis\] Add "make square" possibility during preview
* \[Captis\] Automatic physical size detection
* \[Captis\] Capturing a new material will create a new asset
* \[Captis\] Change resolution selection in dropdown to pixel per inch or centimetre instead of pixel resolution of maximum area
* \[Captis\] Contextual help on alignment calibration
* \[Captis\] Generate roughness map
* \[Captis\] Warn the user if the default calibration files are missing
* \[Filters\] Auto Tiling filter for structured materials and scans
* \[Filters\] New Fold Remover filter
* \[Filters\] New features within the Clone Stamp filter
* \[Filters\] New features within the Equalize filter
* \[Layers\] Ability to flatten layers
* \[Layers\] Context menu when right-clicking on a layer to rename, duplicate, delete or flatten the layer
* \[Onboarding\] Update Welcome and What's New screens content
* \[Performance\] Better performance when using the Crop filter
* \[Performance\] Improve memory usage for the 3D View
* \[Performance\] Updating the 3D view is quicker
* \[Physical Size\] Enable "display with physical ratio" when working on Substance filters when Physical Size is enabled
* \[Physical Size\] When importing images in an empty stack, propose a resolution that is more coherent with the image ratio
* \[Quick Actions\] 3 new quick actions for scan processing
* \[Scripting\] API to flatten layers
* \[Scripting\] Get the filename of each image of an image import layer
* \[Scripting\] New function to activate/deactivate a given channel of an asset
* \[UI\] Rework icons and buttons in the Layers panel to accommodate for the new features
* \[UI\] Warn about environment light authoring deprecation

#### Fixed:

* \[2D View\] Selecting 'display with physical ratio' might not work when using Substance filters
* \[3D Capture\] Svg files are listed in the file picker but not supported
* \[3D View\] Emission intensity parameter in the Shader Settings does not work
* \[3D View\] Sometimes the mesh position is incorrect when creating a new asset
* \[3D View\] Switching to Path Tracing rendering crashes on unsupported hardware
* \[Application\] Application hangs when closing the manual measure popup without setting a size
* \[Application\] Crash
* \[Application\] Freeze on Windows when displaying the desktop (Windows key + D keyboard shortcut)
* \[Application\] Possible crash when switching language
* \[Captis\] Crash when the preview data is not valid
* \[Captis\] Impossible to fully zoom out after zooming in
* \[Captis\] Missing localization on some wizard steps
* \[Captis\] Possible crash at exit when using Captis
* \[Captis\] Scanning does not work if the device is missing calibration files
* \[Filters\] Brush preview when using the Clone Stamp filter may be wrong depending on the texture and brush sizes
* \[Filters\] Erroneous output size after using the Upscale filter
* \[Filters\] Missing icons for Environment Rotation and Stylization filters
* \[Filters\] Updating some filters may lead to incorrect rendering
* \[Layers\] Incorrect first render when blending two materials
* \[Layers\] The button to update layers shows "Update All" even when there is only one update
* \[Layers\] Unnecessary computations when importing images in the layer stack
* \[Performance\] Improve normal map format handling to reduce rendering times
* \[Physical Size\] Manual measurement popup only works after doing an auto-measure
* \[Physical Size\] Wrong export resolution in the Export popup when Physical Size is enabled
* \[Quick Actions\] Missing localization on generated asset names
* \[UI\] Asset preview on hover may not show
* \[UI\] Clicking the Reset to default value button might break some of the controls
* \[UI\] Error messages are not cleared when switching projects
* \[UI\] Make sure material name in viewport & properties panel are empty when there is no asset
* \[UI\] Reset to default value button for the Point of View parameter does not work
* \[UI\] Reset to default value button overlap
* \[UI\] Some buttons are not clickable when a panel is undocked
* \[UI\] Texture tilling V Parameter partially hidden in Viewer Settings and 3D View

#### Removed:

* \[3D Capture\] Remove 3D Capture support
* \[Application\] Remove macOS x86 support

### **5.0.3 HAZELNUT**

*(Released: Jun 3rd, 2025)*

#### **Added:**

* \[Captis\] Allow to give a material same name as an already existing one
* \[Captis\] Move error messages to popups instead of toasts
* \[Filters\] Update embroidery
* \[Preferences\] Add reset in viewer settings and shaders settings
* \[UI\] Do not present the 'Show location' menu item on project assets

#### **Fixed:**

* \[3D Capture\] Mesh post process filter doesn't output expected maps
* \[3D View\] 3D view does not work because of shader cache corruption
* \[3D View\] Ground plane and grid are vertical when scene is Z-up
* \[3D View\] The mesh sometimes disappears
* \[Application\] Closing login window at start-up without logging in sometimes crashes the app
* \[Application\] Crash when access to the plugins configuration file is denied
* \[Application\] Current material is un-selected when the project is saved
* \[Application\] Resetting to default layout sets the resolution to 64x64
* \[Application\] Sampler sometimes crashes when rendering a layer stack
* \[Export\] Export resolution is sometimes reset to 64x64
* \[Export\] It is sometimes not possible to export .sbs/.sbsar files
* \[Layers\] Add base material button does nothing when the material is empty
* \[Layers\] Texture tiling is changed when duplicating a material
* \[Physical Size\] Auto-measure does not work if the Physical Size panel was docked before importing the image
* \[Scripting\] Autosave plugin is broken
* \[UI\] Incorrect spacing in the Export dialog
* \[UI\] Slider animation of tweaks does not work anymore
* \[UI\] Sliders don't snap to integer values when needed
* \[UI\] Some drop down menus are cropped

### **5.0.2 HAZELNUT**

*(Released: April 22th, 2025)*

#### **Fixed:**

* \[Application\] Back button on the Homepage is broken
* \[Application\] Sampler sometimes won't launch if corrupted data from previous versions is present on disk
* \[Application\] The image imported does not appear in the viewport or the layer stack
* \[Captis\] Captis IP address field remains empty even after restarting Sampler
* \[Captis\] Live camera preview only works when application language is set to English
* \[Export\] Crash during export \[Layers\] Painting sometimes does not work in previously saved projects
* \[Layers\] Sampler sometimes updates all textures when only one channel is updated
* \[Layers\] Unable to use material blends in the layer stack after upgrading to 5.0.x
* \[Layers\] Updating a project with an previous Image to Material (AI) version makes material all black
* \[Layers\] When trying to import an unsupported image, Sampler creates a broken layer
* \[Scripting\] Part of the Python API does not work with an empty project
* \[UI\] Menu items sometimes overflow in the File menu

### **5.0.1 HAZELNUT**

*(Released: March 20th, 2025)*

#### **Added**:

* \[Application\] Updated graphics driver compatibility list
* \[Captis\] Show a popup when usage of HP Z Captis is blocked by operating system policies
* \[Quick Actions\] Explain why a Quick Action is disabled in a tooltip
* \[UI\] Crash report window UI styling
* \[UI\] When copying to clipboard, show a toast to say it is done

#### **Fixed:**

* \[2D View\] Exposure slider has no effect when spherical projection is off
* \[2D View\] Painting outside of the texture creates a discontinued stroke
* \[2D View\] The exposure button has no tooltip
* \[2D View\] Zooming on the side of a non square image does not follow the mouse
* \[3D Capture\] 3D Capture does not work on Windows 11 24H2
* \[3D Capture\] Crash if we quit Sampler during the mesh reconstruction step
* \[3D View\] Compute time is sometimes shown as 0ms
* \[3D View\] When changing projection from orthographic to perspective, viewport becomes grey
* \[Application\] Crash at startup when checking GPU capabilities
* \[Application\] Crash during install
* \[Application\] Crash on exit after right-clicking a metadata field
* \[Application\] Environment light missing when opening an SBSAR from the operating system file explorer
* \[Application\] Opening a .sbsar while Sampler is running changes the Texture Tiling setting
* \[Captis\] Some metadata might not transfer between the capture steps
* \[Captis\] The name of the created asset is not the one entered in the metadata field
* \[Content\] Sample project prompts for a filter update but is already up to date
* \[Filters\] Normal/height adjustment filter has no icon
* \[Layers\] Cannot change images in an image import layer
* \[Layers\] Crashes when using the Upscale filter
* \[Layers\] Updating a project with an old Image to Material makes the material all black
* \[Rendering\] Tweaking a layer stack immediatly after creating an asset breaks the rendering
* \[Scripting\] The Autosave pluging crashes when there is no asset in the project
* \[Tools\] Brush size value is missing in the Brush Toolbar
* \[UI\] Changing the application language doesn't update some of the labels in the Home Screen
* \[UI\] Hitting Escape or Enter in Slider text fields won't lose focus
* \[UI\] In the Properties panel, the reset all button and the asset name label overlap
* \[UI\] Issues when docking and undocking panels
* \[UI\] Scrolling in an overlay panel will also scroll in the underlying window
* \[UI\] Switching to List view in the Recent Projects section of the Home Screen does not work
* \[UI\] Viewport display mode button icon always shows 2D/3D

### **5.0.0 HAZELNUT**

*(Released: February 20th, 2025)*

#### **Added**:

* \[Onboarding\] New Homepage with quick access to learning content, sample project, quick actions and recent projects.
* \[Onboarding\] Get started quickly with the new Quick Actions, accessible from the homepage and from dedicated panel
* \[Onboarding\] \[Content\] Quick Actions are predefined workflows that populate the layer stack with most used layers
* \[Onboarding\] Possibility to create a new project via a new Quick start menu, via quick actions or Custom Project
* \[Onboarding\] Possibility to create empty project directly from homepage via dedicated button
* \[3D View\] New advanced rasterizer and pathtracer bringing new rendering capabilites (properties such as coating, sheen, translucency, subsurface scattering) and visual consistency across Substance ecosystem
* \[3D View\] Viewer settings are now accessible directly in the 3D view
* \[3D View\] Possibility to save a render snapshot in clipboard or in files
* \[3D View\] Display a grid to visualize the scene origin
* \[3D View\] Enable the ground plane to catch shadows and reflections
* \[3D View\] Control how reflective and opaque is your ground plane
* \[3D Capture\] Position mesh on ground
* \[Application\] Check hardware compatibility on application startup
* \[Application\] Crash reporting window now opens right after a crash occurs
* \[Content\] Open a sample project to easily get started
* \[Export\] Export Adobe Standard Material shader in USD files
* \[Generative AI\] Check "Do not infer" tag when using image as an input in Image to Texture workflows
* \[Project\] Thumbnails are stored within the project file for faster opening of projects
* \[Project\] Setting in the preferences to store cache data within the project file, with different modes (no cache, light cache, full cache)
* \[Scripting\] \[Breaking change\] Qt migration to Qt6.15 - impact compatibility of existing plugins
* \[Scripting\] Default plugins and script folder are now in the Documents folder
* \[Scripting\] New UI for plugins for visual consistency with main Sampler panels
* \[Scripting\] Access 2 plugin examples to discover Sampler plugin capabilities
* \[Scripting\] New open_3d_catpure() function
* \[Scripting\] When inserting a layer, control if it is inserted above or below the target position

#### **Fixed:**

* \[3D Capture\] Crash if Object Capture cannot be started on macOS
* \[Application\] Crash at exit
* \[Application\] Hang at exit while adding assets to the project panel
* \[Application\] Renaming a project asset does not work unless you press enter
* \[Application\] Undo and redo menu entries are not disabled when they should be
* \[Assets\] Unable to delete assets from the All Libraries section of the Assets panel
* \[Content\] Atlas creator - Use existing opacity map if present
* \[Content\] Color ID Blend - Fix color picking in the basecolor
* \[Layers\] Avoid useless computation when using generators
* \[Layers\] Tweaking a generator may lead to triggering too many computes
* \[Performance\] Improve GPU memory management
* \[Performance\] Render cache may not be used when restarting the app
* \[Resources\] Read only files are not visible in the Assets panel
* \[Scripting\] Allow reusing a layer after adding another layer
* \[Scripting\] Changing the layer stack structure several times in one script may fail

#### **Removed:**

* \[Application\] Remove support for .dng and .nef image files

## Version 4

### **4.5.2 GRUYERE**

*(Released: 07 November 2024)*

#### **Fixed:**

* \[Content\] Crop, Embroidery and Height blend filters

### **4.5.1 GRUYERE**

*(Released: 30 July 2024)*

#### **Fixed:**

* \[Layers\] Painting greyscale masks does not work, impacting tools like Clone Stamp, Paint Warp, Content Aware Fill

### **4.5.0 GRUYERE**

*(Released: 18 July 2024)*

#### **Added**:

* \[Interoperability\] Send materials to UE5, Blender, Maya, 3DsMax Unity
* \[Content\] New texture generator category - Gradients
* \[Content\] HDRI Tools - new Environment rotation filter

#### **Fixed:**

* \[Exposed Parameters\] Exposing .sbsar input values do not work
* \[Layers\] Base color turns red with greyscale images
* \[Rendering\] Grayscale images used in color channels have wrong color space
* \[Scripting\] Using an export preset sometimes doesn't export the expected channels
* \[Content\] Dirt - Applying a Dirt filter on top of Image to Material generates a black normal
* \[Content\] Emboss - Scaling of a pattern in the emboss filter is not linear between 0 and 1
* \[Content\] Make it tile - Improved normal and height consistency

### **4.4.1 FONDUE**

*(Released: 6 June 2024)*

#### **Fixed:**

* \[Content\] Dirt filter is missing
* \[Generative AI\] Network error sometimes occur when using Image to Texture

### **4.4.0 FONDUE**

*(Released: 23 May 2024)*

#### **Added**:

* \[Application\] 3D Capture cache is now stored in a separate sub-folder
* \[Generative AI\] Image to Texture (Beta)
* \[Generative AI\] Text to Pattern (Beta)
* \[Generative AI\] Text to Texture (Beta)
* \[Scripting\] Assets now have a 'resource' property
* \[Scripting\] Layers now have a 'output_usages' property

#### **Fixed:**

* \[Application\] Crash when opening corrupted project file
* \[Application\] Crash when project contains corrupted assets
* \[Application\] Crash when unplugging a monitor on Windows
* \[Application\] Incorrect application icon in the Windows task bar
* \[Application\] Main configuration file corruption can lead to files deletion
* \[Application\] Panels appear in front of popups
* \[Content\] Texture generators have blurry thumbnails
* \[Export\] Opacity channel generated from an imported image breaks when exporting a .sbs/.sbsar
* \[Filters\] Upscale can crash depending on its input layers
* \[Generative AI\] Possible crashes when receiving unexpected results from the service
* \[Scripting\] Crash when autoloading a plugin from environment variable
* \[Scripting\] Possible crash when assigning Output Usage with the API

### **4.3.3 EMPANADA**

*(Released: 26 March 2024)*

#### **Added:**

* \[3D Capture\] New advanced auto-UV parameters during Post Process
* \[Filters\] Perforate filter: ability to invert and change the size of the custom pattern

#### **Fixed:**

* \[3D Capture\] Base color can be incorrect on macOS
* \[3D Capture\] Crash when processing a new version
* \[3D Capture\] Post-Process step can crash on macOS
* \[3D Capture\] The Mesh Transform layer can lead to incorrect rendering
* \[Application\] Crash when starting Sampler while a previous instance is still exporting
* \[Application\] Sampler is unresponsive for a moment when started for the first time
* \[Export\] Anisotropy Angle map is not exported
* \[Filters\] Adding Cloth Weave to the layer stack can lead to a crash
* \[Filters\] Adding Emboss to the layer stack can lead to a crash
* \[Filters\] Content-Aware Fill crashes when using 32 bit images
* \[Filters\] Emboss: Opacity of the layers below aren't completely overriden
* \[Filters\] Fill: Blend mode does not work in Designer and Painter
* \[Filters\] Embroidery: automatic color selection is broken
* \[Preferences\] Prevent setting an unsupported path for 3D Capture cache
* \[Preferences\] The Normal Format preference does not work
* \[Scripting\] The channels parameters of Asset.export_material is case sensitive

### **4.3.2 EMPANADA**

*(Released: 22 February 2024)*

#### **Fixed:**

* \[Application\] Saving a project on a network share on Windows corrupts the project file

### **4.3.1 EMPANADA**

*(Released: 15 February 2024)*

#### **Fixed:**

* \[3D Capture\] Crash when image files become inaccessible while batch generating masks
* \[Export\] Exporting a material with Crop or relative to input policy layer gives invalid results
* \[Layers\] Rare crash when rendering a layer stack
* \[Filters\] Embroidery - Fix issue when using material input on MacOS
* \[Filters\] Stylization - Support Texture Generators
* \[Filters\] Pattern - Fix parameters naming
* \[Localization\] "Save as..." in hardware information window under help menu is appearing unlocalized

### **4.3.0 EMPANADA**

*(Released: 25 January 2024)*

#### **Added**:

* \[Assets\] New asset type: Texture Generators
* \[Assets\] New materials included in the Starter Assets
* \[Assets\] New asset picker for image parameters in the Properties panel
* \[Assets\] Drag and drop Texture Generators from the Assets panel to the image pickers in the Properties panel
* \[Assets\] Drag and drop Texture Generators from the operating system file explorer
* \[Assets\] Filters can suggest fitting generators via a user tag on the image input
* \[Assets\] Texture Generators can define which filter should suggest them via a user tag
* \[Content\] New Perspective Crop filter
* \[Content\] New Stylization filter
* \[Content\] Blending mode on Fill Filter
* \[Content\] Updated Embroidery filter
* \[Content\] Updated Paint Wrap filter
* \[Content\] Updated all filters to support Texture Generators
* \[Layers\] Ability to chose a Texture Generator output channel when adding it to the layer stack
* \[Layers\] Ability to easily list and apply presets on Texture Generators
* \[Layers\] Display a Texture Generator preview in the image pickers
* \[Layers\] Texture Generator parameters can be exposed and exported
* \[Layers\] Assign the Base Color usage when importing a single image with the Texture Import Creation Template
* \[Layers\] Feedback when trying to drag and drop incompatible files in image pickers in the Properties panel
* \[Layers\] Generate an opacity channel from the alpha channel of an imported image
* \[Layers\] Image to Material (AI) is faster to compute when changing its category
* \[Layers\] Select the most relevant layer after a Creation Template is used
* \[Layers\] The position widgets can now be tweaked with a slider in the Advanced Parameters group
* \[Export\] Display a percentage in the queue instead of raw numbers
* \[Interoperability\] Opacity channel is now recognized as alpha channel when sending to Painter
* \[Application\] New dialog to display and save hardware information
* \[Application\] New preference to change the default height scale for every project
* \[Application\] Improve the way outdated assets are displayed
* \[Scripting\] New asset.documentResolution() and asset.setDocumentResolution() functions
* \[Scripting\] New select_asset() function
* \[Scripting\] Python API for Texture Generators
* \[Scripting\] get_project_assets() now returns 3D objects
* \[UI\] Asset thumbnail size can be changed in the Assets panel
* \[UI\] Updated viewport display icons

#### **Fixed:**

* \[2D View\] Zoom with mouse wheel is blocked at 244%
* \[Application\] Crash at start when initializing the graphics API
* \[Application\] Crash if the project name contains the # character
* \[Application\] Possible crash when opening an old project
* \[Application\] Re-opening the current project can lead to a crash
* \[Application\] Some project changes are not registered and are lost without warning when closing the project if not saved
* \[Export\] .sbs/.sbsar export issues when using multiple files with the same name
* \[Export\] Wrong color space for exported grayscale images .sbs/.sbsar file
* \[Filters\] Opacity blend behavior issues
* \[Layers\] .svg files sometimes are not rendered at the correct resolution
* \[Performance\] Some project saves on disk are unnecessary
* \[Project\] Importing an old project does not load associated presets
* \[Scripting\] Unable to get parameters of the first inserted layer
* \[UI\] The preview popup when hovering an asset can appear in the wrong location or screen
* \[UI\] Undocked panels are visible and usable on top of the Welcome screen

### **4.2.2 DORAYAKI**

*(Released: 5 December 2023)*

#### **Added:**

* \[3D Capture\] 3D Capture is now 5% to 10% faster on Windows
* \[3D Capture\] Improve mesh cleanup before decimation
* \[Engine\] Update Substance Engine to version 9.0.3
* \[Layers\] Content-Aware Fill: upstream update, various use case fixes and Linux support

#### **Fixed:**

* \[3D Capture\] Clicking "Back" after alignment then "Next" does not update the point cloud
* \[3D Capture\] Mesh displayed with holes after being added to project
* \[Application\] Crash when exiting fullscreen mode after a 3D capture
* \[Application\] Crash with crafted image files
* \[Application\] If in "All libraries" when quitting Sampler, the Assets panel becomes empty at restart
* \[Application\] Memory leak when exporting material
* \[Application\] Opening a project save with previous Sampler versions can lead to a crash
* \[Application\] Potential crashes when failing to convert 3D meshes
* \[Application\] Silent crash when opening a .sbsar while Sampler is running
* \[Export\] Crash when exporting a .sbs/.sbsar file with a custom usage
* \[Export\] Exported normal maps are always DirectX regardless of the user setting
* \[Export\] Exporting a 3D Object to a FBX file on macos does not work
* \[Export\] Inconsistencies when exporting a Layer Stack with an Embroidery filter as a .sbs/.sbsar file
* \[Export\] Sometimes exporting .sbs/.sbsar files does not work
* \[Export\] Sometimes when exporting an .sbs/.sbsar file images don't have the right bit depth
* \[Layers\]  Making a Splatter layer invisible renders its first child instead
* \[Layers\] Crash when loading mask in Brigtness/Contrast layer
* \[Layers\] Misleading error messages are displayed after deleting layer
* \[Layers\] Possible crash when downgrading an asset
* \[Layers\] Some outputs are not connected to inputs unless the usage is forced in the Channel Settings panel
* \[Physical Size\] Reference layer dropdown can be reset by mistake
* \[UI\] Import template info icons needs update
* \[UI\] Viewport shortcut tip appears everytime the viewport layout changes

### **4.2.1 DORAYAKI**

*(Released: 21 September 2023)*

#### **Added :**

* \[Content\] Image to Material - Improve microdetails generation in normal maps
* \[Content\] Image to Material - New delighting intensity parameter
* \[Layers\] Images can be added in the Image Import layers
* \[Layers\] Images can be removed in the Image Import layers
* \[Layers\] Invalid layers can now be deleted
* \[2D View\] Shift+C shortcut to cycle back the channels
* \[3D Capture\] Display a warning toast when user import less than 20 images
* \[Application\] New preferences to set the default material texture tiling value
* \[Onboarding\] Updated tutorial UI for Image to Material (AI) and Upscale
* \[Scripting\] 3D Capture API: DatasetInfo has more data when Capture3dState is set to aligned
* \[Scripting\] New select_asset argument to create_asset(). New functions: wait_for_computation() and clear_render_cache()

#### **Fixed :**

* \[Layers\] Crash when Crop region is very small
* \[Layers\] Crash when adding or tweaking the Crop filter
* \[Layers\] Making crop region square leads to incorrect material output resolution
* \[Layers\] Outputs sometimes disappear when several layers are disabled
* \[Layers\] Render cache may not properly be invalidated with the Image to Material (AI) and Upscale filters
* \[Layers\] Unable to add Upscale filter when selecting "Do not show this message again" in the warning popup
* \[Layers\] Unable to restore the image in Embroidery filter once modified
* \[Export\] Exported normal map resolution changes when changing normal format
* \[Export\] Remove "\_environment" file name suffix when exporting an environment
* \[Export\] Unable to export an .sbsar file when there is a Warp Transform layer in the layer stack
* \[2D View\] "Fit to screen" does not work when resolution changes
* \[Application\] After closing the application window while computing, the application process could still be running
* \[Application\] Crash at exit
* \[Application\] Invalidate render cache when toggling GPU accelerated neural networks
* \[Scripting\] Naming a plugin as an existing panel name causes unexpected behaviors
* \[UI\] Clicking on a item with a tooltip will cause the tooltip to disappear until restart
* \[UI\] Height scale value may change when switching assets
* \[UI\] Incorrect margin in comboboxes

### **4.2 DORAYAKI**

*(Released: 05 September 2023)*

#### **Added:**

* \[Content\] Vastly improved Image to Material (AI) and Delighter filters
* \[Content\] New Upscale filter
* \[Content\] The Crop filter now has dynamic output resolution.
* \[Material Creation Template\] Add Document size setting.
* \[Material Creation Template\] New "Add a crop" toggle button.
* \[Material Creation Template\] New "Upscale Material" toggle
* \[Material Creation Template\] Display imported image size
* \[Material Creation Template\] Give feedback when some imported images cannot be used
* \[Material Creation Template\] Warn when image sizes are inconsistent
* \[Material Creation Template\] New warnings and tooltips
* \[Layers\] Display the resolution of the layers in the layer stack
* \[Layers\] Layer compute resolution can now be either set to Document size or Input size
* \[Layers\] Show layers resolution in the layer stack
* \[Layers\] Switch a layer resolution policy to Document or Layer Input when applicable
* \[Layers\] Warn the user when an Upscale filter is added manually and provide some documentation
* \[Layers\] Warn the user when doing a linear upscale, and offer to use the Upscale filter instead
* \[Layers\] Computing an Image to Material (AI) layer can now be cancelled quicker, to improve rendering times when tweaking the layer stack
* \[Layers\] Computing an Upscale layer can now be cancelled quicker, to improve rendering times when tweaking the layer stack
* \[Export\] Allow overriding resolution of exported textures
* \[Export\] Channels to export list is now sorted
* \[Export\] Display channel resolution in the channels to export list
* \[Application\] New preference to enable or disable GPU accelerated neural networks
* \[UI\] Improved resolution dropdowns
* \[UI\] New icons for Mesh Transform, Mesh Post Process and Weave filters
* \[UI\] Rename "Share" panel to "Export"
* \[Scripting\] Add layer output resolution support to the export API
* \[Scripting\] Added Crop, Upscale and Document size to the image import API
* \[Onboarding\] New tutorials
* \[Onboarding\] Update Welcome and What's New screens content
* \[Engine\] Update Substance Engine to version 9.0.1

#### **Fixed:**

* \[3D Capture\] Improve Precision options naming in Alignment settings parameters
* \[Application\] Importing images with non-multiple of 16 dimensions can lead to a crash
* \[Application\] Crash when duplicating an asset in the Project panel
* \[Application\] Crash when switching assets in the Project panel
* \[Content\] Painting a custom mask for the Snow filter does not work properly
* \[Exposed Parameters\] Exposed parameters changes can be lost when switching materials
* \[Interoperability\] Sending a Material from the Export panel can lead to a crash
* \[Layers\] Content-Aware Fill stops computing when switching from a single image input to a material input
* \[Layers\] Crash after duplicating an Environment Light that contains a material
* \[Layers\] Image import layer displays wrong image name in the Properties panel if the image file was renamed
* \[Layers\] Sometimes a spinner is displayed on an inactive layer
* \[Layers\] Sometimes changing the output usage of an image in an Image import layer does not work
* \[Layers\] Typos in the Creation Template Window
* \[UI\] 3D viewport onboarding tooltip has focus issues
* \[UI\] Image name can overflow if file name is too long
* \[UI\] Minor brush toolbar layout issues when using the eraser
* \[UI\] Strings are truncated in some languages in the Viewer Settings panel
* \[UI\] While the viewport tooltip popup is displayed, pressing "space" creates a new project

### **4.1.2 CANNOLI**

*(Released: June 20, 2023)*

#### **Fixed:**

* \[Layers\] Memory leak when tweaking Substance materials and filters causing crashes

### **4.1.1 CANNOLI**

*(Released: June 06, 2023)*

#### **Added**:

* \[Engine\] Update Substance Engine to version 9.0
* \[Interoperability\] Send 3D Objects to Stager and Painter

#### **Fixed:**

* \[3D Capture\] Applications crashes when 3D Capture renderer fails
* \[3D Capture\] Crash when an image cannot be loaded
* \[3D Capture\] Crash when reaching the Mesh Reconstruction step
* \[3D Capture\] Crash when resizing the bounding box
* \[3D Capture\] Importing masks following the convention doesn't assign the mask properly
* \[3D Capture\] Rendering glitches when adjusting the bounding box
* \[3D Capture\] Switching between version and toggling rendering options during 3D capture post process is slow
* \[3D Capture\] Switching between versions during 3D Capture Post-Process step is sometimes broken
* \[Application\] Crash at startup
* \[Application\] Crash when duplicating a renamed material
* \[Application\] Crash when opening a legacy .alch project without its dependency folder
* \[Application\] Crash when plugging/unplugging a screen, computer goes to sleep, or is accessed remotely
* \[Application\] Crashes and memory leaks related to non-persistent assets management
* \[Export\] Choosing material format for 3D object file types that embed or reference textures should be disabled
* \[Export\] Crash if something goes wrong during 3D Object export
* \[Export\] Crash when exporting a .sbs/.sbsar file
* \[Export\] Crash when importing custom preset that has the same Label but not the same file name
* \[Export\] Exporting an environment light to a .sbs/.sbsar file sometimes does not work
* \[Export\] Gltf/Glb export encodes textures in base64
* \[Export\] Name text field does not work when refocusing
* \[Export\] Preserve tiling does not work when exporting an Image to Material (AI Powered) layer to a .sbs/.sbsar file
* \[Export\] When exporting gltf and replacing files, the list of files to be replaced is not correct
* \[Exposed Parameters\] Random seed does not work in exported .sbs/.sbsar files
* \[Layers\] Content-Aware Fill sometimes crashes when added for the second time
* \[Layers\] Crash when computing a layer stack
* \[Layers\] Image to Material (AI) disk cache does not work
* \[Layers\] Possible crash when tweaking a layer
* \[Performance\] Memory leaks
* \[Project\] Crash when saving a project
* \[Project\] Importing the same project twice in a row duplicates assets
* \[UI\] Rounded buttons with only an icon are not rendered correctly

### 4.1.0 Cannoli

*(Released: March 28, 2023)*

#### **Added:**

* \[Content\] New Embroidery filter
* \[Content\] New Paint Warp filter
* \[UI\] Add Export option in File menu
* \[3D Capture\] Back button is now available on the alignment step
* \[3D Capture\] Images Handle JPEG EXIF orientation
* \[3D Capture\] Scripting - New dataset_info.camera property
* \[3D Capture\] Add Linux support (see documentation)
* \[3D Capture\] Verify read access of the imported images
* \[Onboarding\] Learn - 2 new tutorials (Embroidery and Paint Warp)
* \[Onboarding\] Updated What's New content

#### **Fixed:**

* \[3D Capture\] Keep camera position when changing version
* \[3D Capture\] Merge all groups of an object into one
* \[3D Capture\] Renamed generated meshes into Original
* \[Application\] Crash when trying to generate thumbnail of a non-existent image
* \[Assets\] Trash bin icon does nothing in the Assets panel
* \[Content\] Updating filters with material slots doesn't work as expected
* \[Export\] Possible crash when exporting an asset with specific filters
* \[Export\] SBS/SBSAR Export - image import layers had priority over image parameters
* \[Export\] UE4 Export preset doesn't work with PNG
* \[Layers\] Crash when dropping a material and a filter at the same time from OS explorer
* \[Layers\] Crash when dragging any SBSAR file with any image file
* \[Layers\] Embroidery opacity channel can be completely white
* \[Localization\] Chinese language may be displayed by default on Linux
* \[Performance\] Fixed a memory issue when removing a layer from an asset
* \[Project\] Possible crash when saving
* \[UI\] Add missing spacing on Version's menu button
* \[UI\] Cancel button not properly displayed
* \[UI\] Disable sliders animation for 3D Capture post-process parameters
* \[UI\] The Material Creation Template window does not close itself when clicking outside
* \[UI\] The filter quick accessor closes itself when clicking outside

**Known Issues:**

* \[Color Picker\] Picking a color on a second monitor with a different resolution may not work
* \[Content\] Shape light widget is not working in spherical projection mode
* \[Interoperability\] Material with displacement sent to Stager will lose displacement controls

### 4.0.2 Banana

*(Released: March 09, 2023)*

#### **Added:**

* \[3D Capture\] Disk usage shows the amount used
* \[3D Capture\] Importing photos is asynchronous and faster
* \[Scripting\] New classes and functions to script the 3D Capture feature
* \[Scripting\] New ExportController class to perform actions when the export is finished, failed or canceled
* \[Scripting\] Pass arguments python scripts run with --run-script
* \[UI\] UI feedback when dragging an asset over the Layers panel
* \[Content\] Color temperature filter is now working on materials
* \[Content\] Normal to Height filters has a new option to preserve tiling

#### **Fixed:**

* \[3D Capture\] Corrected image size in dataset alignment step
* \[3D Capture\] Remove duplicate vertices after UV unwrapping
* \[3D Capture\] MacOS - Better detection if 3D Capture is available
* \[3D Capture\] Crash when closing the 3D capture window while importing images
* \[3D Capture\] Crash when generating a new version
* \[3D Capture\] Crash when trying to load the 3D object in the viewer
* \[3D Capture\] Crash when using path with non UTF8 characters
* \[3D Capture\] Hits & Tips typo
* \[3D Capture\] Meshes are no longer scaled to fit into unit cube
* \[3D Capture\] Prevent a crash when closing 3D capture while rendering
* \[3D Capture\] Removing a mask makes the image disappear
* \[Application\] Crash when importing twice an asset simultaneously
* \[Application\] Backup previous version of assets when opening a project if they were never back-up
* \[Application\] Correctly cache baked maps when not all maps are baked
* \[Application\] Fullscreen crashes when a 3D object is displayed.
* \[Application\] Last material is duplicated when saving the project
* \[Application\] Prevent crash when cancelling the Mesh Post processing compute during the baking step
* \[Application\] Reopening current project does not discard changes
* \[Application\] Stop generating thumbnails for 3D objects
* \[2D View\] Crash when use the brush tool
* \[Content\] Content Aware Fill - computation may stuck
* \[Content\] Atlas Creator filter is downscaling the Opacity channel
* \[Export\] Fix clear Failed exports queue
* \[Export\] OBJ export creates object 100 times smaller than expected
* \[Layers\] Color images imported as grayscale channels are now considered grayscale
* \[Export\] FBX files cannot be imported in third party applications
* \[Export\] Shader output names in USD files are not correct
* \[Layers\] Image name is not updated when changing its name on the OS explorer
* \[Scripting\] Display an error message when reloading an invalid script
* \[UI\] Base material button disabled when not available
* \[UI\] Crash when accessing the file dialog on the Material Creation Template Window
* \[UI\] Quick accessor is accessible even when the Layers panel is closed
* \[UI\] Send to icons are misaligned
* \[UI\] The layer icon changes when clicking on the Blend icon

#### **Known Issues:**

* \[Color Picker\] Picking a color on a second monitor with a different resolution may not work
* \[Content\] Shape light widget is not working in spherical projection mode
* \[Interoperability\] Material with displacement sent to Stager will lose displacement controls

### 4.0.1 Banana

*(Released: February 07, 2023)*

#### **Fixed:**

* \[3D Capture\] When using masks, the texture projection may be broken
* \[3D Capture\] Artefacts may appear on your object
* \[3D Capture\] The exported mesh may be really small

#### **Known Issues:**

* \[3D Capture\] FBX and OBJ exports downscale the result
* \[3D Capture\] 3D Capture is available on MacOS even if your hardware is not compatible. Check the documentation.
* \[3D Capture\] Crash when the mesh reconstruction is done.
* \[Layers\] Content-Aware Fill can be stuck if you tweak layers below
* \[Color Picker\] Picking a color on a second monitor with a different resolution may not work
* \[Content\] Shape light widget is not working in spherical projection mode
* \[Interoperability\] Material with displacement sent to Stager will lose displacement controls

### 4.0.0 Banana

*(Released: January 31, 2023)*

#### **Added:**

* \[3D Capture\] Create 3D objects from images
* \[3D Capture\] Dedicated 3D Capture wizard
* \[3D Capture\] Import or generate black and white masks on your dataset
* \[3D Capture\] Alignment result - view all matched features as a point cloud
* \[3D Capture\] Alignment result - view and interact with cameras associated with each aligned photo
* \[3D Capture\] Define the reconstruction area with a bounding box widget
* \[3D Capture\] Scale, translate, and rotate on all axes the bounding box widget
* \[3D Capture\] Define the geometry precision for the reconstructed mesh
* \[3D Capture\] Optimize your mesh and textures by creating a new version
* \[3D Capture\] Each of the versions is automatically decimated to the target faces number set
* \[3D Capture\] The post-process step automatically unwraps, re-projects textures, and then bakes the normal height and AO information from the high-poly mesh
* \[3D Capture\] Add the original result or a version to the Sampler project
* \[3D Capture\] New Mesh Post-Process layer to automatically decimate, unwrap, reproject textures, and bake details of the underlying mesh layer
* \[3D Capture\] New Mesh Transform layer to scale, rotate, or translate the underlying mesh layer
* \[Export\] New Export window
* \[Export\] Dedicated settings and UI depending on the asset type (material, environment light, mesh)
* \[Export\] Export the mesh as USD, USDA, USDZ, glTF, glb, obj, fbx, stl
* \[Export\] Define the material type when exporting Substance files (SBSAR, SBS)
* \[UI\] Move cache settings to a new tab in the Preferences popup
* \[Application\] 2D and 3D viewports can now be resized, swapped, and stacked vertically
* \[Application\] New SAMPLER_RESOURCES_PATH environment variable to add extra starter assets
* \[Scripting\] Added SAMPLER_PLUGIN_PATH and SAMPLER_SCRIPT_PATH environment variables to import plugins and scripts at startup
* \[Scripting\] Added export functions for materials, environment lights, and 3d objects
* \[Scripting\] Added identifier, default value, min and max values, labels, and enum values to parameters
* \[Scripting\] Added import_textures function to enter a customized usage while importing images

#### **Fixed:**

* \[Application\] Crash when opening a recent project and saving in confirmation dialog
* \[Application\] File dialog prevents opening .ssa files
* \[Application\] File dialogs can appear on a background window on macOS
* \[Application\] Potential crash when opening 3.2 projects
* \[Application\] Selecting a file closes the File dialog before displaying warnings
* \[Exposed Parameters\] Exporting parametric environment lights does not work
* \[Layers\] "Click here to browse" link in layer stack doesn't work anymore
* \[Layers\] Painting several images within the same layer sometimes does not work
* \[Layers\] Setting an image in the layer properties does not update the image picker thumbnail
* \[Layers\] Tweaking a Sampler asset added as a layer does not work
* \[Project\] Unwanted asset update when opening a project
* \[Scripting\] Browse to plugin folder sometimes fails on Windows
* \[Scripting\] Crash when using 'open_project()' in a Python script
* \[Scripting\] JPEG export is missing from the API
* \[Scripting\] The log panel is not read-only
* \[Scripting\] image_picker parameter value does not work
* \[UI\] Missing asset icon for environment lights in the Project panel
* \[UI\] Send to Designer Format Dropdown in the Preferences popup can be empty
* \[UI\] Some buttons have an incorrect style
* \[UI\] The label overlaps the buttons in Button Group widgets
* \[UI\] Tooltip position is wrong for "Tools" in Set the physical size menu
* \[UI\] When changing language, File menu is misaligned

#### **Known Issues:**

* \[3D Capture\] When using masks, the texture projection may be broken
* \[3D Capture\] Small artefacts may appear on your object if your scale in the Mesh transform is too small
* \[3D Capture\] The exported mesh may be really small. Reset the scale of the Mesh transform and re-export
* \[Color Picker\] Picking a color on a second monitor with a different resolution may not work
* \[Content\] Shape light widget is not working in spherical projection mode
* \[Interoperability\] Material with displacement sent to Stager will lose displacement controls

## Version 3

### 3.4.1 Arancini

*(Released: October 06, 2022)*

**Added:**

* \[Onboarding\] New Welcome and What's New screens
* \[Onboarding\] Updated Home screen UI
* \[Onboarding\] New Learn content in the Home screen
* \[Scripting\] Log an error in the Log panel when a method is not recognized
* \[Scripting\] New ssa.helpers module to enable printing to the Log panel
* \[Application\] Support for the new side-by-side buttons widget from Substance 3D Designer

**Fixed:**

* \[Export\] Crash when exporting a .sbsar file referencing a missing image
* \[Export\] Crash when exporting an asset referencing a corrupted image file
* \[Export\] Exporting a .sbsar file with an Embroidery layer results in a gray material
* \[Export\] Exporting a material to a .sbs/sbsar file can generate a fully transparent material
* \[Export\] Normal Format parameter is not exposed correctly in .sbs/.sbsar files
* \[Export\] Sbs/sbsar export of a layer stack referencing a .svg file is broken
* \[Export\] Transform layer is not exported properly / Updated Enscape - Revit export preset
* \[Exposed Parameters\] Crash when deleting a layer containing an exposed parameter
* \[Exposed Parameters\] Updating an outdated layer in the layer stack can lead to a corrupted list of exposed parameters
* \[Exposed Parameters\] Parameters that should not be exported are exported anyway
* \[Exposed Parameters\] Removing a blend filter when deleting a layer does not unexpose its parameters
* \[Exposed Parameters\] Text parameters break .sbs/.sbsar exports
* \[Layers\] Crash when dropping a layer stack in another layer stack
* \[Layers\] Crash when failing to load a filter
* \[Layers\] Cannot reload the previous image when resetting the Image field
* \[Layers\] Cannot undo/redo transform tool changes
* \[Layers\] Clone Stamp layer is stuck after clicking "Reset all settings"
* \[Layers\] Using any of the reset buttons prevents from drawing in the Image field
* \[Layers\] The Reset button does not clear the drawing mask in the Image field
* \[Layers\] The Reset button in the Image field does nothing if the user has painted something
* \[Layers\] Rendering cache does not work when using the Brush tool
* \[Layers\] Deleted layer can still show up in the Properties panel
* \[Layers\] Layer computation can stall when switching between project assets
* \[Project\] Sometimes Sampler is unable to open a project from disk
* \[2D View\] The 2D view always defaults back to Material Output

**Known Issues:**

* \[Color Picker\] Picking a color on a second monitor with a different resolution may not work
* \[Content\] Shape light widget is not working in spherical projection mode
* \[Interoperability\] Material with displacement sent to Stager will lose displacement controls

### 3.4.0 Arancini

*(Released: September 06, 2022)*

**Added:**

* \[Exposed Parameters\] New Exposed Parameters panel
* \[Exposed Parameters\] New button on parameters hover to expose and unexpose parameters from Properties panel
* \[Exposed Parameters\] New right-click context menu on parameters to expose and unexpose parameters from Properties panel
* \[Exposed Parameters\] Exposed parameters are listed in the Exposed Parameters panel
* \[Exposed Parameters\] Color dots and color discs are added in several places to easily identify exposed parameters
* \[Exposed Parameters\] Parameter labels can be edited in the Exposed Parameters panel
* \[Exposed Parameters\] Display a warning for non-exportable parameters
* \[Exposed Parameters\] Display warning if moving a layer with exposed blend parameters somewhere where they become hidden
* \[Exposed Parameters\] Exposed parameters are exported in SBS and SBSAR formats
* \[Metadata\] Support Custom Metadata templates
* \[Metadata\] New CLO Physical properties metadata template
* \[Metadata\] Add icons on hover to add/remove custom metadata
* \[Python API\] New Python API
* \[Python API\] API for Asset authoring
* \[Python API\] API for Layers management
* \[Python API\] API for Parameters management
* \[Python API\] API for Project management
* \[Python API\] A plugin can be enabled and disabled
* \[Python API\] Python API documentation accessible in the Help menu
* \[Scripting\] New Plugins and Scripts section in the Preferences popup
* \[Scripting\] Create and import plugins to customize Sampler interface with your own panels
* \[Scripting\] Plugins become part of the Sampler interface and can be docked and moved around like standard Sampler panels
* \[Scripting\] Dedicated button bar for the plugins on the Sampler right toolbar
* \[Scripting\] Create and import scripts to perform a list of given tasks
* \[Scripting\] Launch Python scripts via Scripts menu
* \[Scripting\] Plugins and Scripts can be deleted, re-ordered, and reloaded from the Preferences window
* \[Scripting\] Added --run-script command line parameters
* \[Logs\] New Logs panel
* \[Logs\] Enable Logs panel from the Preferences window
* \[Logs\] New action bar to clear, copy/paste, export logs
* \[Properties\] New button on parameters hover to reset parameter value
* \[Properties\] New right-click context menu on parameters to reset parameter value
* \[Content\] Image to Material (AI Powered) now works on MacOS
* \[Engine\] Update Substance engine to v8.6.0

**Fixed:**

* \[Application\] Application could crash at exit when a thumbnail generation was in progress
* \[Application\] Application might crash when using 'Save as' at exit
* \[Application\] Application might hang during shutdown on MacOS
* \[Application\] Saving with the color dialog open doesn't save its changes
* \[Export\] Usage naming convention is not correct when exporting
* \[Layers\] Dropping a material on top of a filter could crash
* \[Layers\] Updating an outdated layer stack could update unrelated layer stacks
* \[Metadata\] Empty fields are exported
* \[Metadata\] When there is only one metadata item, the UI lets you try to reorder it
* \[Project\] Compute never ends after duplicating a material
* \[Project\] Project asset is duplicated after initial project save
* \[Project\] Unnecessary computations when switching asset
* \[Rendering\] Some layer stacks do not render properly after deleting a layer
* \[Security\] Fix CVE-2015-20107
* \[UI\] 2D Outputs can be blurry depending on the window size
* \[UI\] Asset preview can stay opened on top when application loses focus
* \[UI\] Splash screen rounded corners have a square opaque background

**Known Issues:**

* \[Color Picker\] Picking a color on a second monitor with a different resolution may not work
* \[Content\] Shape light widget is not working in spherical projection mode
* \[Interoperability\] Material with displacement sent to Stager will lose displacement controls

### 3.3.2 Zucchini

*(Released: June 28, 2022)*

**Fixed:**

* \[Application\] Fix potential crash when opening a project
* \[Export\] Restarting Sampler breaks imported custom export presets list
* \[Interoperability\] Fix crash when a material sent from Designer is deleted and then re-sent from Designer
* \[Project\] Impossible to delete the last material or environment light if it's the last asset in the project
* \[Project\] Right-click on an environment light makes the "unsaved modifications" asterisk appear

**Known Issues:**

* \[Color Picker\] Picking a color on a second monitor with a different resolution may not work
* \[Content\] Shape light widget is not working in spherical projection mode
* \[Interoperability\] Material with displacement sent to Stager will lose displacement controls

### 3.3.1 Zucchini

*(Released: June 07, 2022)*

**Added:**

* \[Application\] Native Apple silicon (M1) support
* \[UI\] New shortcut, "C" key, to cycle through channels in the 2D view
* \[Tools\] Numerical field to edit grayscale color value in Brush Toolbar

**Fixed:**

* \[Tools\] Using the Brush tool on Windows with a fractional UI scale (150%) offsets the strokes
* \[Performance\] Improve memory consumption
* \[Physical Size\] Physical size information can be missing when enabling the feature
* \[UI\] Mouse scrolling sometimes does not work as expected when pressing the Alt key
* \[Application\] Application may crash when opening a saved project
* \[Application\] Crash when drag and dropping several images and using Texture Import in the Material Creation Template window
* \[Application\] Potential crash when saving a project containing a custom filter
* \[Application\] Sometimes the Control key state is lost when switching application
* \[Assets\] Crash when renaming a local folder

**Known Issues:**

* \[Color Picker\] Picking a color on a second monitor with a different resolution may not work
* \[Content\] Shape light widget is not working in spherical projection mode
* \[Interoperability\] Material with displacement sent to Stager will lose displacement controls

### 3.3.0 Zucchini

*(Released: May 17, 2022)*

**Added:**

* \[Content\] New Content-Aware Fill filter (Windows and Mac)
* \[Content\] Content-Aware Fill is working on images, PBR materials, and environment lights
* \[Content\] Add "Preserve Tiling" parameter to Image to Material (AI Powered)
* \[Content\] The Perspective Transform filter can display a grid between its four points
* \[Interoperability\] Send materials to Adobe Substance 3D Stager
* \[Tools\] Center the transformation by pressing Ctrl when resizing Transform or Crop tool
* \[Tools\] Lock the ratio to square by pressing Shift when resizing Transform or Crop tool
* \[Tools\] Clone stamp cursor offers a preview of what will be stamped
* \[Tools\] Preview original content in the the Eraser cursor when using Clone stamp
* \[Tools\] Ctrl+Click creates a new stamp in the Clone Stamp layer
* \[Tools\] Successive clone stamps are now grouped within a single layer
* \[Tools\] Brush Toolbar UI Revamp
* \[Tools\] The Brush Toolbar position is persistent during a session
* \[Tools\] New brush tiling options by axis
* \[Tools\] Hide/display the overlay over the 2D view when painting
* \[Tools\] New shortcut, "X" key, to toggle between Brush and Eraser
* \[Tools\] New shortcut, "\[" "\]" to change the Brush size
* \[Tools\] New shortcut, "E" key, to toggle the Eraser
* \[2D View\] New Spherical Projection mode when creating environment light
* \[2D View\] Brush tool is supported with the spherical projection mode
* \[2D View\] Position tool is supported with the spherical projection mode
* \[2D View\] Undo/redo is supported with the spherical projection mode
* \[2D View\] In Spherical Projection, set the default position to look at the center of the environment
* \[2D View\] New exposure control
* \[UI\] In the Properties panel, the Image tweak displays the source of the content (Image or from a layer)
* \[UI\] Improved the layer/material outputs dropdown background
* \[UI\] New position of the resolution information in the 2D View
* \[UI\] New tooltip with 3D view navigation controls shortcuts
* \[UI\] New tooltip with brush controls
* \[UI\] New tooltip with projection navigation controls shortcuts
* \[Compound Filters\] Compound filters handle variations to work on images, PBR materials, and environment lights
* \[Compound Filters\] Tweaks order matches the nodes list order in the compound filter
* \[Compound Filters\] Tweaks of different nodes with the same group will be merged in one single group in the Properties panel
* \[Application\] Have dedicated viewer settings per asset type

**Fixed:**

* \[Application\] Application may crash when switching to 2D view
* \[Application\] Fix a possible deadlock or crash when exporting multiple times
* \[Application\] Make default values for channels consistent with Substance 3D Designer
* \[Application\] Loading a project doesn't trigger the material recompute
* \[Application\] Updated the URL to texture import documentation
* \[Content\] When using a compound filter, it asks to be updated when it shouldn't, on reload
* \[Content\] Details in height map disappear when using Opacity Blend
* \[UI\] In the Color Dialog, it is possible to get out of range using the slider's text fields
* \[UI\] Usage list has a useless vertical scrollbar

**Known Issues:**

* \[Color Picker\] Picking a color on a second monitor with a different resolution may not work
* \[Content\] Shape light widget is not working in spherical projection mode
* \[Interoperability\] Material with displacement sent to Stager will lose displacement controls

### 3.2.1 Yakitori

*(Released: March 08, 2022)*

**Added:**

* \[Export\] Export dpi metadata in image files
* \[Physical Size\] Keep the ratio with non square textures when editing physical dimensions
* \[Physical Size\] Physical size metadata is applied immediatly when physical size changes
* \[UI\] Adjust Height scale max slider so it can influence any kind of material when Physical Size is enabled
* \[UI\] New tooltips on search filters in the Asset panel
* \[UI\] Use tooltips to explain when buttons are disabled in the Assets panel
* \[Content\] Brightness contrast filter update

**Fixed:**

* \[2D View\] 90 degrees rotation button in the Crop and Transform tools don't work as expected
* \[2D View\] Crop widget sometimes goes missing
* \[Application\] Clearing an image parameter does not reconnect the underlying layer
* \[Application\] Crash at exit after saving a project
* \[Application\] Crash when drag and dropping the current material into a collection of the Assets Panel
* \[Application\] Drag and dropping an asset in the viewport may crash
* \[Content\] Normal blend has a random seed tweak
* \[Content\] Snow filter has incorrect normal output depending on fresh and melted snow parameter values
* \[Content\] Parquet filter: fixed unexpected seams
* \[Content\] Embroidery filter: remove thread in metallic map
* \[Content\] Floor tiles filter: fix x and y tiles count
* \[Content\] Brick wall filter: output normal and height to 16 bit
* \[Export\] Default file name in export popup is not the current material name
* \[Export\] Exporting with physical ratio with an export preset gives incorrect dimensions
* \[Export\] Metallic is missing in the CLO export preset
* \[Export\] When replacing an export custom preset, the display name is not updated
* \[Layers\] Custom channels of the first inserted layer are not discovered
* \[Layers\] Material is re-evaluated when changing tweaks of a hidden layer
* \[Localization\] Tooltips are not localized in Export panel
* \[Physical Size\] Disabling Physical Size of an asset does not remove the physical scale
* \[Physical Size\] Height Scale value can't be set outside of slider bounds the first time
* \[Physical Size\] Importing an image with no physical size prevents opening the project
* \[Physical Size\] Physical Size is erroneously set to zero when missing
* \[Physical Size\] Physical Size physical scale check box status is not updated when first displayed
* \[UI\] Base Material & Normal to Height do not have a category
* \[UI\] Cursor is sometimes invisible when painting an image
* \[UI\] Disable "Copy All" and "Cut All" options in the edit menu of a text field if it is empty
* \[UI\] Filter names have incorrect characters
* \[UI\] Physical Size lock button does not have the correct style
* \[UI\] The close button in search bar in Asset Panel does not clear the search string

**Known Issues:**

* \[Color Picker\] Picking a color on a second monitor with a different resolution may not work

### 3.2.0 Yakitori

*(Released: January 25, 2022)*

**Added:**

* \[Physical Size\] New Physical Size panel
* \[Physical Size\] Add Physical Size options to the Material Creation Template window
* \[Physical Size\] Add Physical Size measurement tool
* \[Physical Size\] Add Physical Size auto-measurement tool
* \[Physical Size\] Add Physical Size diagnostic tool
* \[Physical Size\] Allow setting the z value of the Physical Size
* \[Physical Size\] Dropdown widget to set the level of zoom in the 2D view
* \[Physical Size\] New "Display with physical ratio" option in the level of zoom dropdown
* \[Physical Size\] New "Fit to physical size" option in the level of zoom dropdown
* \[Physical Size\] Display the Physical Size in the 2D view
* \[Physical Size\] Display the Physical Size in the 3D viewport
* \[Physical Size\] In the image import dialog, show physical size depth if there is an imported height map
* \[Physical Size\] Show the Physical Size in the asset contextual menu
* \[Physical Size\] Set the length unit in the Preferences
* \[Physical Size\] Export textures respecting the physical ratio
* \[Metadata\] Ability to add custom metadata to a user-authored asset
* \[Export\] Export custom metadata to .sbs(ar) files
* \[Export\] Export description, category, author, and tags metadata to .sbs(ar) files
* \[Export\] Export the Physical Size to .sbs(ar) files
* \[Export\] Set .sbsar file compression setting
* \[Export\] Export the asset thumbnail to .sbs(ar) files
* \[Export\] Set the graph type when exporting a .sbs(ar) file
* \[Application\] Realtime Engine 2021 is no longer available
* \[Application\] Undo/Redo now supports Tiling (U,V) and height scale slider changes
* \[Rendering\] Generate disk cache when the authored asset is saved
* \[Assets\] Use Ctrl+click to enable multiple asset type filters in the Resources panel
* \[UI\] Ability to lock the Tiling (U,V) sliders
* \[UI\] Add a contextual menu with "Copy", "Cut", "Paste", "Copy all" and "Cut all" in text fields
* \[UI\] Length unit (meters, inches, parsecs, ...) support in labels and text fields
* \[UI\] The user can set the decimal precision used to display numbers
* \[UI\] Use units in measure popups everywhere it's relevant
* \[Localization\] Default new asset name is now localized
* \[Content\] New Cloth Weave generator
* \[Content\] New Channel Switch filter
* \[Content\] All relevant filters are now aware of the Physical Size
* \[Content\] New icons for Wood Finish
* \[Content\] All filters are now compatible with Adobe Standard Materials (ASM) channels
* \[Content\] Filters can now have an "environment" variation

**Fixed:**

* \[2D View\] Channel remains in the list when removed
* \[Application\] Cannot duplicate an asset loaded from the operating system file explorer
* \[Application\] Crash at exit
* \[Application\] Crash sometimes when clicking "Starter Assets" in the Assets panel
* \[Application\] Crash when deleting a material
* \[Application\] Environment variable "SUBSTANCE_DISABLE_SPECIFIC_FEATURES" is still active when set to "0" or "".
* \[Application\] Freeze while saving a project with multiple materials
* \[Application\] Importing an image can lead to a crash
* \[Application\] Missing some starter assets on first launch
* \[Export\] Exporting an asset sometimes leads to a crash
* \[Layers\] Cannot import images when the layer panel is closed or invisible
* \[Layers\] Changing the language causes the current asset to recompute
* \[Layers\] Changing the usage of an imported image does not upate which filter variation to use
* \[Layers\] Image to Material (AI) is sometimes not computed when tweaking layers below it
* \[Layers\] Image to Material (AI) sometimes recomputes when not needed
* \[Layers\] No update is suggested when a custom filter is updated on the disk
* \[Layers\] Normal channel sometimes has the wrong pixel format
* \[Layers\] Some layers are still computed even when not visible
* \[Layers\] The 2D view tools may be broken when toggling a layer visibility
* \[Layers\] The UI freezes when using Image to Material (AI)
* \[Layers\] Toggling the visibilty of the Transform filter layer breaks the 2D view tool and may lead to a crash
* \[Layers\] Too many recomputations when removing a layer from the layer stack
* \[Layers\] When a compound filter contains an unusual or custom input/output, Sampler doesn't compute it
* \[Performance\] Asset panel is slow to open
* \[Performance\] Avoid some unnecessary recomputations of the layer stack
* \[Performance\] Loading project assets takes too much time
* \[Performance\] Render cache on disk may not be used
* \[Performance\] Switching between layers is slow
* \[Performance\] Tweaking a material or a filter is slow
* \[Project\] Saving a project when exiting may lead to a crash
* \[Rendering\] Removing an image may remove all outputs
* \[Rendering\] The rendering time displayed in the viewport is wrong when tweaking
* \[UI\] Can't scroll vertically in the export popup when needed
* \[UI\] It is possible to open the export popup when there is nothing to export
* \[UI\] Some popups do not scroll if their content overflows
* \[UI\] Text fields are not selected when clicking on it or opening a menu
* \[UI\] The name of the blend mode in the properties panel is sometimes not correct
* \[UI\] The Save option in the File menu is sometimes grayed out
* \[UI\] The text field doesn't go away after renaming two materials
* \[UI\] Typo in the preference popup

**Known Issues:**

* \[Color Picker\] Picking a color on a second monitor with a different resolution may not work

### 3.1.2 Xocoatl

*(Released: December 14, 2021)*

**Fixed:**

* \[Interoperability\] Open .sbsar file with Substance 3D Sampler from Bridge can fail on Windows
* \[Layers\] Moving the only layer below itself will crash
* \[UI\] Channel settings button disappears when changing language
* \[UI\] The material name in Properties panel disappears after saving the project
* \[Assets\] Clicking on "All libraries" can lead to a crash

**Known Issues:**

* \[Realtime Engine 2021\] Heavy computation can crash the application
* \[Realtime Engine 2021\] Realtime Engine 2021 will crash on a Windows machine with both AMD CPU and Nvidia GPU installed
* \[Color Picker\] Picking a color on a second monitor with a different resolution may not work

### 3.1.1 Xocoatl

*(Released: November 24, 2021)*

**Added:**

* \[Interoperability\] Send assets (SBS or SBSAR) to Substance 3D Designer
* \[Interoperability\] Set in preferences the default format for interoperability with Substance 3D Designer
* \[Interoperability\] Receive multiple assets from Adobe Bridge
* \[UI\] New Random Seed widget
* \[UI\] Context menu update
* \[Assets\] Drag and drop images from the Assets panel to the Properties panel
* \[Project\] Asset names are sanitised to avoid some specific characters
* \[Branding\] Update file icon for SBSAR files
* \[Engine\] Update Substance Engine version 8.3.0

**Fixed:**

* \[Content\] Crop - Preserve ratio when cropping non-square images
* \[Content\] Transform - Horizontal transformation is not inverted when using the widget
* \[Content\] Gravel - fix custom mask painting on all channels
* \[Content\] Floor tiles - fix issues with pattern tiling and repetition
* \[Assets\] Grey out Adobe Bridge option if not installed
* \[Color Picker\] Escape key closes the Color Picker
* \[Rendering\] Fix Scattering Distance Scale when using greyscale input
* \[Share\] Send to options are only available with Adobe licenses
* \[Project\] Fix a memory performance issue

**Known Issues:**

* \[Realtime Engine 2021\] Heavy computation can crash the application
* \[Realtime Engine 2021\] Realtime Engine 2021 will crash on a Windows machine with both AMD CPU and Nvidia GPU installed
* \[Color Picker\] Picking a color on a second monitor with a different resolution may not work

### 3.1.0 Xocoatl

*(Released: September 28, 2021)*

**Added:**

* \[Color Picker\] New Color Picker UI
* \[Color Picker\] Preview the current and previous colors side by side
* \[Color Picker\] Input your color in Hexadecimal
* \[Color Picker\] New eyedropper with color preview
* \[Color Picker\] The eyedropper can pick a color outside of Sampler
* \[Color Picker\] Tweak your color in RGB or HSV color spaces
* \[Color Picker\] Save and manage Swatches
* \[Interoperability\] Edit images in Illustrator from Image Import layer or Image parameters
* \[Interoperability\] Edit images in Photoshop from Image Import layer or Image parameters
* \[Widget\] New Crop Widget
* \[Widget\] Press Enter to validate your crop
* \[Widget\] The Crop widget reads the image size to fit the widget and keep the ratio when resizing
* \[UI\] New gresycale slider UI
* \[Application\] Add normal format selection in preferences
* \[Application\] The normal format in Image Import layers follows the default normal format set in the preferences
* \[Application\] In the 2D view, the normal is displayed following the normal format set in the preferences
* \[Application\] The normal is exported in the normal format set in preferences
* \[Export\] Add normal format parameter to SBS and SBSAR file exports
* \[Export\] Add shader settings to SBS and SBSAR file exports
* \[Export\] Set the default resolution of exported SBS graphs
* \[Compound Filters\] Package SSA filters with 7z
* \[Compound Filters\] Add category metadata in compound filters
* \[Compound Filters\] Compound Filters can have an embedded thumbnail
* \[Compound Filters\] Added Compound Filters extension (.ssafilter) to the Get Content's file dialog
* \[Compound Filters\] Import Compound Filters (.ssafilter) in the Assets panel
* \[Engine\] Update substance engine to v8.2.0

**Fixed:**

* \[Application\] Connected local folders may hang
* \[Application\] Crash at exit
* \[Application\] Crash when launching two instances of Sampler
* \[Content\] Crop filter has a random seed tweak
* \[Content\] Some Substance materials are sometimes not upgraded
* \[Export\] Crash when exporting with a newly added custom preset
* \[Export\] Estimated size of package is missing in export popup
* \[Export\] Fix memory leak when exporting SBS and SBSAR files
* \[Compound Filters\] Compound filters may have duplicated inputs
* \[Compound Filters\] Crash if a filter has unmet references
* \[Compound Filters\] Crash when reordering a layer stack with a compound filter in it
* \[Compound Filters\] The render sometimes hangs
* \[Image Import\] Importing an image triggers multiple renderings
* \[Layers\] Crash on undo/redo
* \[Layers\] Crash when adding a Base Material
* \[Layers\] Crash when using an invalid image as environment light
* \[Layers\] Fix duplicate import when inserting a filter with several graphs
* \[Layers\] Reordering layers doesn't always work
* \[Project\] Crash when loading an incomplete project file
* \[Project\] Crash when opening a corrupted project
* \[Project\] Some assets can disappear from a project
* \[Properties\] Fix missing filter's presets
* \[UI\] Angle parameters cannot be set
* \[UI\] Filters metadata display in Asset panel
* \[UI\] Grouping by category hides filters
* \[UI\] Scroll issue in the Asset panel
* \[UI\] The export panel now has a scrollbar
* \[UI\] The thumbnail is not displayed for some image formats in image picker

**Known Issues:**

* \[Realtime Engine 2021\] Heavy computation can crash the application
* \[Realtime Engine 2021\] Realtime Engine 2021 will crash on a Windows machine with both AMD CPU and Nvidia GPU installed
* \[Color Picker\] Picking a color on a second monitor with a different resolution may not work

### 3.0.1 Waffle

*(Released: July 27, 2021)*

**Added:**

* \[Brush\] Enable colors in brush tool if the image input supports it
* \[Brush\] Holding the Shift key in the brush tool draws straight lines
* \[Brush\] Show a line preview when holding shift in the brush tool
* \[Brush\] Brush tool now supports undo and redo
* \[2D View\] Image input default color is used when painting
* \[Layers\] Read Substance input default value in SBSAR files
* \[Rendering\] Allow to combine height with normal
* \[Rendering\] Sub-surface scattering support (not available on MacOS)
* \[Assets\] Use SBSAR graph type to determine asset type
* \[Assets\] Better performance for search and asset discoverability in the Assets panel
* \[Assets\] Added a 'All Libraries' entry in the Assets panel that displays all assets of all your libraries
* \[Assets\] User can now choose to group assets by category or type
* \[Import\] Auto detect anisotropy, coat, sheen and specular edge color textures at import
* \[UI\] Replace elided panel title with an icon
* \[UI\] Textfields style update
* \[UI\] New description text in The Environment Light Template Creation window
* \[Application\] Export assets with the current resolution when sending to external application
* \[Application\] Material default resolution is now 2048\*2048 (1024\*1024 on macos)
* \[Content\] New patterns in the Floor tiles filter
* \[Content\] New Dual Color mode in the Color replace filter

**Fixed:**

* \[2D View\] First stroke in brush tool is sometimes broken
* \[2D View\] Free resources when brush tool is not visible
* \[2D View\] Use the right resize cursor in the transform widget
* \[2D View\] Widgets are not displayed if the user has panned in the 2D view before
* \[Application\] Crash when opening a project with broken workflow
* \[Application\] Fix application shutdown to prevent flooding the log with useless errors
* \[Application\] Redo, delete and save keyboard shortcuts don't work on some operating systems
* \[Application\] Undo/redo changing image usage in import layer is broken
* \[Export\] Emission color exported images have wrong name
* \[Export\] Environment is 8bit when using SBSAR export
* \[Export\] Remove extra spaces in exported image file names
* \[Export\] Replacing or deleting a custom export preset crashes
* \[Layers\] Avoid crash when there is an input count mismatch
* \[Layers\] Crash when inserting a Base Material layer
* \[Layers\] Filter input count is capped to default value
* \[Layers\] Redo erroneously changes the Blend type to Height blend
* \[Layers\] Remove drop zone above input headers
* \[Layers\] Layers are inserted at the wrong place around input headers
* \[Layers\] Reset all settings button does not reset drop down widgets values
* \[Layers\] Undo/redo when changing an image on the Image Import layer marks the project as modified and so to save
* \[Layers\] Usages may be stopped by blend layers
* \[Project\] Crash when loading a legacy project with missing dependencies folder
* \[Project\] Crash when using undo/redo after saving
* \[Project\] Opening a SBSAR file containing an environment light creates a material asset
* \[Project\] Renaming a material can trigger a thumbnail generation
* \[Project\] Saving after renaming a material marks the project as unmodified
* \[Project\] Some changes after renaming a material are not saved
* \[Rendering\] Bright dots are visible on the environment with 2020 realtime engine
* \[Rendering\] Crash when resizing using Real Time Engine 2021
* \[Rendering\] Recompute shadows on height level change
* \[Assets\] Connected folders stop indexing new assets when adding an invalid file
* \[Assets\] Crash when connecting a local folder with many materials
* \[UI\] 2D/3D view buttons missing tooltips
* \[UI\] All assets in the Assets panel are highlighted at launch
* \[UI\] Breadcrumbs sometimes disapears in the Assets panel when importing materials
* \[UI\] Changing language doesn't affect the Project panel
* \[UI\] Channel Settings panel shows legacy workflow information
* \[UI\] Correctly align "No settings for this item" text for filters with no tweaks in properties panel
* \[UI\] Elements are mis-aligned in the welcome screen and the preferences popup
* \[UI\] Panel titles have incorrect width
* \[UI\] Scrolling is sometimes broken in the Properties panel
* \[UI\] Splash screen has incorrect ratio and is blurry
* \[UI\] The fullscreen mode is not fullscreen
* \[UI\] Undocked panels are always on top even when the application is not active on MacOS
* \[UI\] Update welcome screen banner image
* \[Content\] Tiling filter doesn't process the ambient occlusion channel
* \[Content\] Quilt Stitch issue with the welt assembly seam selection and diamond pattern
* \[Content\] Emboss filter works in 256px by 256px
* \[Content\] Fix tiling issue with the Floor tiles when the offset is greater than 0

**Known Issues:**

* \[Realtime Engine 2021\] Heavy computation, crash the application
* \[Realtime Engine 2021\] Realtime Engine 2021 will crash on Windows machine with both AMD CPU and Nvidia GPU

### 3.0.0 Waffle

*(Released: June 23, 2021)*

**Added:**

* \[Branding\] Substance Alchemist becomes Adobe Substance 3D Sampler
* \[Branding\] New application icons
* \[UI\] New User Experience and User Interface
* \[UI\] New Splashscreen
* \[UI\] Panels are undockable and dockable in the interface
* \[UI\] Dock up to 3 panels in the same column
* \[UI\] Dock up to 3 panels in the same panel (Tabs)
* \[UI\] Undock panels to create a separate window in the same or a different screen
* \[UI\] Closed panels pop-over when clicking on their icons
* \[UI\] Re-arrange your left and right bar by moving panels icons
* \[UI\] New toolbar to access directly specific filters (Crop, Transform, Perspective Transform, Clone Stamp)
* \[UI\] New "Get Content" button in the left bar
* \[UI\] Import files directly in your assets with the Get Content button
* \[UI\] Import files directly to your Layers with the Get Content button
* \[UI\] Access directly Adobe Substance 3D Assets website with the Get Content button
* \[UI\] Resolution widget is now directly accessible in the viewport
* \[UI\] All UI elements now are loaded dynamically
* \[UI\] Shortcut - Use "2" to toggle the visibility of the 2D view
* \[UI\] Shortcut - Use "3" to toggle the visibility of the 3D view
* \[Welcome Screen\] Create a project in one-click with the New button
* \[Welcome Screen\] New artwork banner
* \[Project\] All projects are now associated to a unique file
* \[Project\] New project file extension .ssa
* \[Project\] Save as a project will ask you to select where to save your project
* \[Project\] Closing Sampler will ask you to save your project if not saved
* \[Project\] Closing Sampler will ask you to save your project if there are modifications since the last save
* \[Project\] The name of your project is displayed above the viewport
* \[Project\] The project name is in italics with a star if it is not saved or if it contains modifications since the last save
* \[Project\] Open a .ssa project file directly from your OS explorer
* \[Project\] Open a .sbsar from your OS explorer will launch Sampler with a new project with this .sbsar file ready to use
* \[Project\] Open a .alch (legacy Substance Alchemist file) from your OS explorer
* \[Project Panel\] New panel that will contain all assets created within a project
* \[Project Panel\] Create an asset (material or environment light) using the + icon
* \[Project Panel\] Right-click on asset opens a context menu
* \[Project Panel\] From the right-click context menu, you can delete an asset
* \[Project Panel\] From the right-click context menu, you can duplicate an asset
* \[Project Panel\] From the right-click context menu, you can rename an asset
* \[Project Panel\] Switching between assets won't lose modifications
* \[Resolution\] You can now set non-square resolution for all your assets
* \[Resolution\] The resolution value is saved by asset within a project
* \[Environment Light\] Create environment light within Substance 3D Sampler
* \[Environment Light\] When creating an environment light, dragging and dropping image(s) will display the Environment Light Creation Template Window
* \[Environment Light\] In the Environment Light Creation Template, select Environment Import to assign your image to the environment in the 3D view
* \[Environment Light\] In the Environment Light Creation Template, select HDR merge to create an environment light from several 360-degrees images with different exposure
* \[Environment Light\] In the Environment Light Creation Template, select "Use as bitmap" to edit your image(s) before creating an environment light
* \[Environment Light\] Assign the environment usage in the Image Import layer to directly assign the image to the environment in the 3D view
* \[Environment Light\] In the 2D view for the environment channel, there is an automatic color correction to have the rendering appear the same as in the 3D view
* \[Environment Light\] New dedicated content for environment light creation
* \[Assets Panel\] The Resources and Filters panels are merged in a new Assets panel
* \[Assets Panel\] The Assets panel now supports the following asset types: materials, filters and images
* \[Assets Panel\] All Starter Assets are accessible in the Starter Assets section
* \[Assets Panel\] Starter Assets section is read-only
* \[Assets Panel\] New "Your Assets" section
* \[Assets Panel\] "Your Assets" section is the place where you can import all your resources
* \[Assets Panel\] All assets in "Your assets" are added in a specific folder in your Documents
* \[Assets Panel\] Connect local folders in the Assets panel to add new sections
* \[Assets Panel\] The search will search in the current folder and its subfolders
* \[Assets Panel\] Navigate between folders and subfolders with breadcrumbs
* \[Assets Panel\] Filter the current folder by material, by filter or by image
* \[Assets Panel\] Combine several filters to get only materials and images
* \[Assets Panel\] Change the display by switching between a grid or a list
* \[Assets Panel\] Filters are represented with their icon
* \[Assets Panel\] Images are represented with their preview
* \[Assets Panel\] Increasing the width will change the layout of the panel with a specific view to navigate between folders
* \[Assets Panel\] On non read-only sections, delete an asset by dragging an dropping it on the bin icon
* \[Assets Panel\] Right-click on asset opens a context menu
* \[Assets Panel\] From the right-click context menu, access the asset metadata (name, category, location)
* \[Assets Panel\] From the right-click context menu, delete the asset (only available on non read-only sections)
* \[Assets Panel\] From the right-click context menu, browse your asset in Adobe Bridge
* \[Layers Panel\] New icon to directly add a base material on top of your layers
* \[Layers Panel\] Shortcut - Shift + B will add a base material on top of your layers
* \[Layers Panel\] Layers now have a thumbnail preview (Material thumbnail, filter icon or Image preview)
* \[Properties Panel\] New design of the Properties panel title with the asset name and the asset thumbnail
* \[Properties Panel\] Filter Layers now support presets
* \[Properties Panel\] On Image Import Layer, right-click on the image preview to edit the image in Photoshop
* \[Adobe Bridge\] Browse your Asset in Adobe Bridge, will launch Bridge at the location of the asset
* \[Adobe Photoshop\] Edit in Adobe Photoshop will open the image in Photoshop ready to be edited
* \[Adobe Photoshop\] At each save in Adobe Photoshop, the edited image will be reloaded in Sampler
* \[Substance 3D Designer\] Assets sent from Adobe Substance 3D Designer will arrive directly in the "Your Assets" section of the Assets panel
* \[Export\] Send assets directly to Adobe Substance 3D Painter and Adobe Substance 3D Stager
* \[Export\] Send materials and environment lights to Adobe Substance 3D Painter
* \[Export\] Send environment lights to Adobe Substance 3D Stager
* \[Rendering\] New material properties are now supported and rendered in 3D
* \[Rendering\] Adding Sheen support (Sheen color, Sheen opacity and Sheen roughness)
* \[Rendering\] Adding Coating support (Coat color, Coat Roughness, Coat Normal, Coat Specular Level and Coat IOR)
* \[Rendering\] Adding Anisotropy support (Anisotropy Level and Anisotropy Angle)
* \[Rendering\] Adding Specular Edge Color support
* \[Rendering\] Activate these new properties in the Channel Settings panel
* \[Rendering\] Introduction of a new Realtime Engine (2021) renderer in Beta
* \[Rendering\] Switch between the two Renderer versions in the Viewer Settings panel
* \[Rendering\] The Realtime Engine (2021) renderer supports translucency, absorption and scattering material properties
* \[Rendering\] The Realtime Engine (2021) renderer introduces a new way to compute shadows from the environment light
* \[Rendering\] The Realtime Engine (2021) renderer computes in realtime the irradiance of the environment light
* \[Shader Settings Panel\] New Shader Settings panel to tweak specific material shader parameters
* \[Shader Settings Panel\] New parameters (Normal scale, height scale, height level, Emission intensity, IOR, Coat normal intensity and Coat IOR)
* \[Shader Settings Panel\] Specific parameters for the Realtime Engine 2021 (Subsurface Scattering, Scattering Distance, Red Shift and Rayleigh Scattering)
* \[Shader Settings Panel\] The settings values are saved per asset
* \[Viewer Settings Panel\] Added a preview of the default environment lights
* \[Viewer Settings Panel\] Added a preview of the default meshes
* \[Viewer Settings Panel\] New environment opacity parameter
* \[Viewer Settings Panel\] New environment blur parameter (specific to the Realtime Engine 2021 renderer)
* \[Localization\] New translations in German and French
* \[Content\] New default starter materials
* \[Content\] New default environment lights
* \[Content\] All filters have been updated, cleaned, and optimized
* \[Content\] The Adjustment filter has been split into several filters
* \[Content\] New Brightness/Contrast filter
* \[Content\] New Hue/Saturation filter
* \[Content\] New Vibrance filter
* \[Content\] New Sharpen filter
* \[Content\] New Normal/Height adjustment
* \[Content\] New Panels filter
* \[Content\] New Smudge filter
* \[Content\] New Weaves filter
* \[Content\] New Warp transform filter
* \[Content\] New Height to AO filter
* \[Content\] New Height to Normal filter
* \[Content\] Color Replace - Replace in new supported channels (Sheen, Coating, Anisotropy,...)
* \[Content\] Color variation - Manual mode to select exactly the colors to change
* \[Content\] Tiling - option to visualize the seams cut
* \[Content\] Tiling - option to paint the seams cut for a perfect tiling
* \[Content\] Match - option to add a material to match its color and its roughness
* \[Content\] Match - it now works on images to match the color of another image
* \[Content\] Environment ligth - New Color Temperature filter
* \[Content\] Environment ligth - New Exposure filter
* \[Content\] Environment ligth - New Exposure Preview filter
* \[Content\] Environment ligth - New Nadir Patch filter
* \[Content\] Environment ligth - New Nadir Extract filter
* \[Content\] Environment ligth - New Lights filters (Sphere, Line, Shape, Plane)
* \[Content\] Environment ligth - New Panorama Patch filter
* \[Content\] Environment ligth - New Straighten Horizon filter
* \[Content\] Environment ligth - New HDR merge filter

**Known Issues:**

* \[Realtime Engine 2021\] Changing the layout, crash the application
* \[Realtime Engine 2021\] Heavy computation, crash the application
* \[Panels\] MacOS - Undocked panels are in front of all applications
* \[Widgets\] Transform and Positions widgets can disappear. Hide and Unhide the layer to make them appear.
* \[Export\] SBSAR export of an environment light loses the 32bit depth precision
* \[Assets Panel\] Assets can be highlighted when opening a folder
* \[Properties Panel\] Resetting the parameters doesn't reset the combobox UI
* \[Localization\] Changing language doesn't affect the project panel until it's recreated

## Version 2

### 2.3.2 (2020.3.2) Vermicelli

*(Released: February 23, 2021)*

**Added:**

* \[Localization\] Japanese support

**Fixed:**

* \[Layers\] Tweaking a material in the embroidery filter loses the embroidery image

**Known Issues:**

* Usage of Image to Material (AI powered) on high resolution images can be slow
* Content Aware Fill filters are slow in high resolution
* Coma or point can be ignored when typing a specific evalue in a slider
* Impossible to save twice the exact same material layer stack

### 2.3.1 (2020.3.1) Vermicelli

*(Released: December 17, 2020)*

**Added:**

* \[Engine\] Substance Engine update
* \[Application\] Environment variable to disable specific features
* \[Content\] Replace color - New Advanced segmentation option
* \[Content\] Floor Tiles - new patterns and options available
* \[Content\] Embroidery - Complete revamp of the filter
* \[Content\] Adjustment - New metallic parameter + opacity safe transform correction

**Fixed:**

* \[Layers\] Cannot import twice the same custom filter
* \[Layers\] Cannot use image input with the brush tool
* \[Export\] Export .jpg instead of .jpeg
* \[UI\] Update welcome screen image credits
* \[UI\] Fix invisible separator in menus
* \[UI\] Radio buttons display a tooltip when they are truncated
* \[UI\] Typo: Starter Materials
* \[Application\] UTF-8 characters in asset names do not work
* \[Localization\] Disable italic font style for chinese locale
* \[Localization\] Localized string split into 2 lines
* \[Localization\] Adjust folder name and replace with ellipsis if it's too long
* \[Localization\] Format numbers with thousand separator
* \[Localization\] Localize date and time display
* \[Localization\] Localize color picker on Windows
* \[Content\] Transform - With the safe transformation activated, the normal rotates correctly every 45°
* \[Content\] Surface relief - Fix tiling issue with perlin fractal noise (advanced noise)
* \[Content\] Brickwall Pattern - Height input in 16bit
* \[Content\] Material Icon Render - Specular reflections issue
* \[Content\] Color Variation - No color shift between color inputs and the result
* \[Content\] Color Variation - Performance update

**Known Issues:**

* Usage of Image to Material (AI powered) on high resolution images can be slow
* Content Aware Fill filters are slow in high resolution
* Coma or point can be ignored when typing a specific evalue in a slider
* Impossible to save twice the exact same material layer stack

### 2.3.0 (2020.3.0) Vermicelli

*(Released: October 26, 2020)*

**Added:**

* \[Image to Material\] Support of NVIDIA RTX 3000 series
* \[Image to Material\] New parameters to control the geometry details
* \[Image to Material\] New parameters to control the roughness
* \[Image to Material\] New parameters to control the delighting intensity
* \[Thumbnails\] New thumbnail generator based on Substance Designer's PBR renderer
* \[Thumbnails\] Update base materials and atlases to embed their thumbnail
* \[Thumbnails\] Retrieve the thumbnail from the .sbsar file if it exists
* \[Thumbnails\] Change thumbnail quality in the Preferences
* \[Engine\] Updated to Substance Engine version 8
* \[Localization\] Chinese localization
* \[UI\] Experimental Spot Colors Picker
* \[Content\] New Environment Map - Studio 06
* \[Content\] Add Atlas Generator filter
* \[Content\] Add Atlas Splitter filter
* \[Content\] Add Discarded Gums filter
* \[Content\] Add Fingerprints filter
* \[Content\] Add Scratches filter
* \[Content\] Add Surface Relief filter (replace height modulation filter)
* \[Content\] Add Warp filter
* \[Content\] Add Invert filter
* \[Content\] Add Colorize filter
* \[Content\] Add Replace Color fitler
* \[Content\] Transform - Add the possibility to deactivate the transformation on a specific channel
* \[Content\] Transform - Add rotation when safe transform is activated
* \[Content\] Color Variation - Add a segmentation option to choose how to distribute the colors

**Fixed:**

* \[Layers\] Properly update UI when doing multiple undo/redo actions
* \[Layers\] Prevent crashes when doing multiple undo/redo actions
* \[Layers\] Crash when using Image to Material (AI Powered), with log: invalid device ordinal
* \[Filters\] Improve NVIDIA graphics card detection for NVidia specific features
* \[Application\] Crash when closing the application
* \[Application\] Fix VRAM amount detection on MacOS
* \[Export\] Some export presets are sometimes missing
* \[Content\] Oil Paint Effect - Fix height range with high displacement amplitude
* \[Content\] Make It Tile Advanced - No washed out basecolor at export
* \[Content\] Make It Tile Advanced - White mask on the basecolor when the AO is too strong
* \[Content\] Adjustment - It works now on images (scan1, ...)

**Known Issues:**

* Usage of Image to Material (AI powered) on high resolution images can be slow
* Content Aware Fill filters are slow in high resolution
* Coma or point can be ignored when typing a specific evalue in a slider
* Impossible to save twice the exact same material layer stack

### 2.2.1 (2020.2.1) Udon

*(Released: July 21, 2020)*

**Added:**

* \[Layers\] In App Error message when Image to Material (AI-Powered) is out of memory

**Fixed:**

* \[Layers\] Image to Material (AI-Powered) does not work with Specular/Glossiness workflows
* \[Layers\] Crashes when out of video memory while using Image to Material (AI-Powered)
* \[Layers\] Disk cache is not used for display when opening a stack
* \[Layers\] Detection of Nvidia RTX 8000
* \[Layers\] It is sometimes impossible to move a layer outside a Splatter input
* \[Layers\] Disk cache is not used when inserting a stack in a stack
* \[Layers\] Some channel usages are computed although they are not used
* \[Layers\] Blank outputs are created sometimes when importing images
* \[2D View\] Switching to another layer with Draw mode active blocks pan and zoom
* \[Content\] Snow - 8bit issue on the normal map
* \[Content\] Pavement Pattern - 8 bits issue on the normal map
* \[Content\] Equalizer - 8 bits issue on the normal map
* \[Content\] Gravel Generator - 8 bits issue on the normal map
* \[Content\] Floor Tiles - Handle opacity and specular level
* \[Content\] Blender cycles eeve export preset - invert normal map
* \[Content\] Correct issue with huge images with Image to Material (AI Powered)
* \[Application\] Crash when choosing "Backup and Restart" on database error
* \[Application\] Crash when clicking quickly on the same asset
* \[Application\] Rare crashes on exit
* \[Application\] Crash when dropping files on the Welcome screen
* \[Application\] Crash when a corrupted environment file is loaded
* \[Application\] Rare crash when rapidly switching rendered asset
* \[Application\] Freeze when exiting while an asset is computing
* \[Application\] Rare crash on startup on macos
* \[Application\] Deadlock when closing the application soon after startup
* \[Rendering\] 3D view sometimes flickers
* \[UI\] Color picker and random seed widgets are not aligned with the rest of the tweaks
* \[Rendering\] Wrong computation time displayed
* \[Export\] Some export presets are sometimes missing

**Known Issues:**

* Usage of Image to Material (AI powered) on high resolution images can be slow
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Content Aware Fill filters are slow in high resolution
* Coma or point can be ignored when typing a specific evalue in a slider
* Impossible to save twice the exact same material layer stack

### 2.2.0 (2020.2.0) Udon

*(Released: June 15, 2020)*

**Added:**

* \[Create\] New Image to Material (AI powered) filter available on Windows and Linux
* \[Create\] Rename Bitmap to Material to Image to Material (B2M)
* \[Image Import\] New Material Creation Template Pop-up
* \[Image Import\] New "Add a base material" option
* \[Image Import\] Be able to drag and drop additional images in the Material Creation Template
* \[Image Import\] Be able to remove images in the Material Creation Template
* \[Image Import\] Assign channel to imported bitmaps automatically based on their filename
* \[Image Import\] Be able to invert normal maps
* \[2D View\] Introduction of a painting mode
* \[2D View\] The painting tiles
* \[2D View\] Set a greyscale value for the brush color
* \[2D View\] Pan and zoom while painting
* \[2D View\] X shortcut to invert brush greyscale value
* \[2D View\] \[ and \] shortcuts to change the brush size
* \[2D View\] Ctrl (or Cmd) + Mouse wheel change the brush size
* \[2D View\] It is now possible to modify the source position when using Clone Patch
* \[Layers\] Shift + drag and drop to auto scatter atlases
* \[Layers\] Alt + drag and drop inserts a material as a decal
* \[Layers\] Expose easily transform matrices from Substance Designer
* \[Layers\] Dropping textures in a non-empty stack automatically assigns to the correct channels
* \[Layers\] New type of layer: Compound Filters
* \[Parameters\] Support Substance string inputs
* \[UI\] Added drop shadows for popups and menus
* \[UI\] New Color Widget with right click options (clear, copy, paste)
* \[UI\] New Image Widget with Painting tool option
* \[UI\] Be able to paint over an imported image in an image widget
* \[Rendering\] New default camera position
* \[Export\] Substance files are exported for Substance Designer 2020.1.2 (10.1.2)
* \[Performance\] Better application startup time
* \[Performance\] Improve asynchronous tasks handling
* \[Performance\] Improve layer stack performance when adding, removing or moving layers
* \[Performance\] Image to Material (AI powered) runs faster on RTX GPUs
* \[Content\] New meshes: Female T-Shirt, Male T-Shirt, Shoe
* \[Content\] New Blend Mode - Per Channel Blend
* \[Content\] Opacity blend height correction with 2 new parameters (height position and height scale)
* \[Content\] Add Height Adjustments in Height Blend mode
* \[Content\] Use Height information option in the Custom Mask Blend
* \[Content\] New Perspective Correction Tool
* \[Content\] Pattern Generator - Add a parameter to invert the pattern
* \[Content\] Pattern Generator - Add a new parameter Override Material Details
* \[Content\] New Decal filter
* \[Content\] New Moss filter
* \[Content\] New Cracks filter
* \[Content\] New PBR Validate filter
* \[Content\] New Floor Tiles filter
* \[Content\] New Quilt Stich filter
* \[Content\] Atlas Scatter - Add Custom Mask input to enable painting option
* \[Content\] Dirt - Add Custom Mask input to enable painting option
* \[Content\] CLO export preset
* \[Content\] VStitcher export preset
* \[Content\] Unity HDRP presets export a detailMap

**Fixed:**

* \[Layers\] Imported images are loaded too many times
* \[Layers\] Crash when creating a clone patch at the bottom of the stack
* \[Layers\] Adding a material at the bottom of the stack makes it unstable
* \[Layers\] Filter after image import works improperly
* \[Layers\] workflow_type value is not updated when switching the workflow between projects with a custom filter
* \[Layers\] Disable "remove layer" button when no layer is selected
* \[Layers\] Crash when loading an asset containing a Clone Patch
* \[Layers\] Normal to Height filter crashes on MacOs
* \[Application\] Crash when loading back and forth environment maps
* \[Application\] Performance issues when some graphics tablet driver is installed
* \[Application\] EXR 32 bits files import are black
* \[Application\] Crashes when loading and unloading assets
* \[Application\] Crash when switching from explore to create
* \[Application\] Target collection when saving a material is not from current project
* \[Application\] Fix backup and restart
* \[Image Import\] Properly import grayscale images
* \[Content\] New filters for new matrix handling
* \[Content\] Imported custom filters are visible in the quick access bar
* \[Content\] Fix color shift with the Make it tile advanced filter
* \[Performance\] Opening a color dialog is slow and recomputes the current layer
* \[UI\] Keyboard shortcuts sometimes don't work
* \[2D View\] Content Aware Fill needs a useless first click to work
* \[Resources\] Folders in local disks are still watched for updates after removing them
* \[Resources\] Deleting a linked folder from filesystem doesn't remove it
* \[Export\] Custom usages in custom export presets are not exported
* \[Export\] Exporting .sbsar file with special characters in path fails

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

* \[Project\] Export and import metadata
* \[Application\] Ctrl+S now saves a preset in Explore
* \[Performance\] Use render cache instead of recomputing saved materials for resolutions up to 2k

**Fixed:**

* \[UI\] Fixed computing indicator in the viewport
* \[UI\] Entering Negative values in sliders is fixed
* \[UI\] Combo boxes: keyboard arrows and scrollbar now work
* \[UI\] Keep the selected channel when switching between "Material Outputs" and "Layer Inputs" in the 2D view
* \[Layers\] Fixed crash when adding custom channels in Base Material
* \[Layers\] Crash when manipulating layers
* \[Layers\] Custom channels are not displayed with a saved material
* \[Application\] Fixed rare crash when importing an asset
* \[Application\] Crash on exit
* \[Application\] Combo boxes now show correct values when switching presets
* \[Export\] Renamed Enscape preset to Enscape Revit
* \[Export\] Importing an export preset after removing it works
* \[Export\] Crash at export
* \[Rendering\] Fixed rendering when the base color is in 16bit half float format
* \[Project\] Do not crash when importing corrupted package
* \[Project\] Handle 2019.1.4 to 2.x.x migration when Create has never been opened
* \[Project\] Fix a crash when importing the same project twice
* \[Project\] Fix a crash when importing projects
* \[Resources\] Custom filters imported in previous versions work
* \[Resources\] Materials with the same name no longer erase each other
* \[Resources\] Crash when linking a local folder
* \[Resources\] Starter Materials user-created folders are no longer removed after a restart
* \[Inspire\] Fix material/collection drop area and add a warning message if using an unsaved material

**Known Issues:**

* Content Aware Fill filters are slow in high resolution
* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Coma or point can be ignored when typing a specific evalue in a slider

### 2.1.0 (2020.1.0) Tiramisu

*(Released: March 12, 2020)*

**Added:**

* \[Export\] Export preset selction to pack your textures for renderers and game engines
* \[Export\] Export preset to Unreal Engine 4
* \[Export\] Export preset to Unity Standard
* \[Export\] Export preset to Unity HDRP
* \[Export\] Export preset to Blender Cycles/Eevee
* \[Export\] Export preset to Arnold 5
* \[Export\] Export preset to Corona Renderer
* \[Export\] Export preset to Enscape
* \[Export\] Export preset to Keyshot 9
* \[Export\] Export preset to Redshift
* \[Export\] Export preset to Vray Next
* \[Export\] Export preset to Lens Studio
* \[Export\] Export preset to Spark AR Studio
* \[Export\] Export preset to PBR Specular Glossiness from PBR Metallic Roughness
* \[Export\] New export UI
* \[Export\] Remember Export settings
* \[Export\] Import and manage your custom export presets
* \[Export\] Delete and replace your custom export presets
* \[Export\] Rename your custom export presets
* \[Export\] Set the default export resolution to the current resolution
* \[Export\] Add the choice to create a subfolder to the export location
* \[Export\] Warning message before replacing existing files
* \[Application\] New version numbering scheme
* \[Application\] Open Create at launch, and change labs order
* \[Welcome Screen\] New welcome banner
* \[Project\] Open last project at launch
* \[UI\] New combo box style
* \[2D view\] F shortcut to focus in the 2d view
* \[Filters\] Added support for alchemist::parameterVisibility tag in Substance graphs
* \[Filters\] Have a global tweak to manage parameter visibility based on your workflow
* \[Resources\] New command line option to setup resources and linked folders with a configuration file
* \[Version checker\] Configuration of the version check
* \[Content\] New starter materials
* \[Content\] Bitmap to Material - Add the possibility to define the metallic channel (uniform, custom image import, color picking)
* \[Content\] Adjustment - Add the support of the PBR specular/glossiness workflow
* \[Content\] Atlas Scatter - New parameters

**Fixed:**

* \[Project\] Crash when importing the same project twice
* \[Project\] Fixed crash when importing and opening projects several times
* \[Application\] Crash when loading an unnamed material
* \[Application\] Recognize missing files when re-importing them
* \[Application\] Fix random crash on shutdown
* \[Application\] Fixed rare crash when unloading an material in Create
* \[Application\] Fixed random crash when using UI controls
* \[Application\] Fixed export of log files to the Desktop on Windows 10
* \[UI\] Export panel has the wrong size when you open it in Create
* \[UI\] Open project with a single click
* \[UI\] Correctly set minimum and maximum slider values
* \[UI\] Show label of the channel usages instead of ids
* \[UI\] Clicking a material always opens/closes the tweak panel
* \[UI\] Fix hidden layers colors
* \[UI\] Welcome Screen buttons improvements
* \[Layers\] Less unnecessary recomputes
* \[Layers\] Crashes when using Clone Patch
* \[Layers\] Selecting an image import layer no longer triggers a compute
* \[Layers\] Clone Patch and Content Aware Fill layers no longer recompute when selected
* \[Channel settings\] Enabling or disabling usages now trigger a rendering
* \[Resources\] Prevent freeze when mass clicking on a stack in the library
* \[Resources\] Performance hit when re-adding a previously added linked folder
* \[Resources\] Fixed a crash when trying to open a deleted .sbsar file
* \[Performance\] Avoid loading materials to access their parameters
* \[Performance\] Backup assets only when used in a project or in an authored material
* \[Export\] Fixed materials in export queue sometimes skipped or exported with wrong parameters
* \[2D View\] Restored pan and zoom
* \[Content\] Parquet Pattern takes into account the Ambient Occlusion channel
* \[Content\] Paint - Display mask input when enabling custom mask
* \[Content\] Stonewall Pattern - Remove possible banding effects in the normal map
* \[Content\] Height Modulation - Correct double base color entries in the 2d view

**Known Issues:**

* Content Aware Fill filters are slow in high resolution
* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Coma or point can be ignored when typing a specific evalue in a slider

## Version 1

### 1.1.4 (2019.1.4) Sesame

*(Released: January 30, 2020)*

**Added:**

* \[Resources\] Confirmation prompt when clearing a resources folder

**Fixed:**

* \[Layers\] Move layers to two and more layers below or above
* \[Create\] Allocation of enough VRAM budget to have good performances

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

* \[Workflow\] Support of multiple workflows
* \[Workflow\] Support of PBR Specular Glossiness workflow
* \[Workflow\] New Channel Settings panel
* \[Workflow\] Workflow selection at project creation
* \[Channel Settings\] Activate/Deactivate specific channel computation
* \[Channel Settings\] Display list of custom channels available in the current material
* \[Channel Settings\] Automatic computation of custom channels when required
* \[Channel Settings\] Force/Block computation of custom channels
* \[Layers\] New UI of material input placeholder in Atlas Scatter and Splatter filters
* \[Layers\] Image Input parameter of a filter can be fed by underneath layers
* \[Layers\] Display a notification when some layers are out of date
* \[Layers\] Possibility to update to the latest version of outdated layers via the notification
* \[Project\] New metadata fields at project creation
* \[Inspire\] Generated variations are specific to a project
* \[2D View\] Switch between the Layer inputs, layer outputs, and the material outputs
* \[Welcome Screen\] Add Import project (.alch) option
* \[Preferences\] New Preferences window to set cache location and analytics privacy settings
* \[UI\] New UI buttons
* \[Performance\] Overall improvement of the parallelization system
* \[Performance\] Optimization of the number of material computes
* \[Engine\] Substance Engine update
* \[Framework\] Upgrade to Qt 5.13
* \[MacOS\] Global improvements of macOS Catalina support
* \[Content\] Adjustment filter - Normal intensity and invert parameters

**Fixed:**

* \[Layers\] Unset Image Input parameter when deleting the layer
* \[Layers\] Fix a crash when adding a clone patch layer
* \[Layers\] Fix some crashes when blending layers stack materials in other layer stack materials
* \[Export\] Channels selection for export is now respected
* \[Resources\] Do not crash when navigating in the Resources panel
* \[Resources\] Fix crash when importing corrupted Substance files
* \[Resources\] Reduce the number of crashes when loading large folders
* \[Thumbnail\] Thumbnail computation doesn't freeze the interface
* \[Image Import\] Uniformization of image type supported across the application
* \[Preset\] Save the description when creating a preset from an SBSAR
* \[Inspire\] Fix image drag and drop
* \[Application\] Fix crashes at exit
* \[Application\] Fix crashes at the exit when exporting materials
* \[UI\] Fixes and improvements
* \[UI\] Rename temporary asset to "unsaved material"
* \[Content\] Global update and cleaning of all filters

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

* \[Layers\] Save and Save as options are accessible via the interface in the layers stack toolbar
* \[Resources\] Clearer breadcrumb in the Resources panel to navigate through folders
* \[Resources\] Maintain back button pressed to access all upper folders
* \[Resources\] Add reload of imported materials option to update them to the latest version
* \[Layers\] Possibility to change the image in the Image import layer
* \[Layers\] Possibility to define an image as a channel (base color, normal, height,...) in the Image import layer
* \[Content\] New Atlas Scatter filter to scatter new atlas elements from Substance Source
* \[Content\] New Oil Paint Effect filter
* \[Content\] New Channels Generation filter to generate height, ambient occlusion and roughness from base color and normal maps

**Fixed:**

* \[UI\] Reactivate tooltips on Layers stack toolbar
* \[UI\] Fix issue when typing two decimals in a slider value
* \[Performance\] Fix crash when switching quickly between materials
* \[Export\] Switching to another material before the end of an export does not crash anymore
* \[Resources\] Context menu is displayed on top of the material when you right-click on it
* \[Layers\] The 'Click here' link is working when the layer stack is empty
* \[Presets\] Remove save button in the tweak panel when it's a material created in Alchemist
* \[Tweak\] Information message displayed when it's a material created in Alchemist
* \[Viewport\] Default value of Specular Level texture is corrected to 0.04
* \[File Menu\] Fix and rename Save and Save as option
* \[Engine\] Update Substance engine version to avoid crash of some SBSAR files during import.
* \[Content\] Tiling filter is working on the ambient occlusion channel
* \[Content\] Crop filter is working on the ambient occlusion channel
* \[Content\] Water filter modifies gain the height map
* \[Content\] Correct tiling of the top material in the opacity blend mode
* \[Content\] Height of the top material is preserved in the opacity blend mode
* \[Content\] Possible to add a custom mask, custom pattern or a scale map in the Perforation filter
* \[Content\] Height Modulation filter forces height and normal maps in 16 bits
* \[Content\] Adjustment filter forces height and normal maps in 16 bits

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

* \[Blend\] New opacity Blend mode
* \[Engine\] New Substance Engine version

**Fixed:**

* \[Layers\] Fix crash while deleting a layer that is still computing
* \[Layers\] Fix crash while removing the bottom layer
* \[Layers\] Fix crash while the material name contains special characters
* \[Layers\] Stop computing every filters that use a widget
* \[Layers\] Avoid crash while using Clone Patch and Content Aware Fill filters
* \[Layers\] Fix crash while drag and droping a filter in a splatter input slots
* \[Resources\] Fix crash while linking local folders or importing resources in Substance Alchemist
* \[Collection\] Fix crash while switching rapidly between materials
* \[UI\] Fix crash while value is null or not valid in tiling, displacement sliders on the viewport
* \[Inspire\] Fix crash while accessing the Inspire tab
* \[Inspire\] Fix crash while inspiring on a just saved layers stack material
* \[Performance\] Heavy Substance materials and Filters (Tiling) compute faster
* \[Help\] Fix export log file
* \[Content\] Randomizer filter works on all channels
* \[Content\] Multiangle workflow takes all scans into account
* \[Content\] AO Blend correct blending
* \[Content\] Curvature Blend correct blending
* \[Content\] Color ID Blend correct blending
* \[Content\] Custom Mask Blend correct blending
* \[Content\] Fix Adjustment filter for roughness modification
* \[Content\] Fix Base Material filter for custom normal channels upload
* \[Content\] Fix Custom Import pattern of the Embossing filter

**Known Issues:**

* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Coma or point can be ignored when typing a specific value in a slider
* Normal to Height filter can crash on MacOS

### 1.1.0 (2019.1.0) Sesame

*(Released: November 04, 2019)*

**Added:**

* \[Project\] Creation of a project
* \[Project\] Introduction of the .alch file format that contains project data
* \[Project\] Export a .alch project containing the collections and their materials
* \[Project\] Import a .alch project
* \[Project\] Open recent projects
* \[Welcome Screen\] A welcome screen is displayed at the launch
* \[Welcome Screen\] Create a project from the welcome screen
* \[Welcome Screen\] Access the list of all your projects in the welcome screen
* \[Welcome Screen\] Quick links to access the documentation, the about popup and license management
* \[File Menu\] Integration of a file Menu
* \[File Menu\] Access the project commands from the File tab and the save of the layer stack
* \[File Menu\] Access the undo and redo commands from the Edit tab
* \[File Menu\] The previous help menu moved in the file menu under the Help tab
* \[Layers\] New architecture of the layer stack
* \[Layers\] New UI of the layer stack
* \[Layers\] Select the blend mode directly on the toolbar
* \[Layers\] Access separately the blend parameters and the material parameters
* \[Layers\] Add materials directly in dedicated inputs of the Splatter filter in the layer stack
* \[Layers\] Change scan order directly in the Image import layer
* \[Viewport\] Control of the camera field of view
* \[Viewport\] Possibility to switch between orthographic or perspective camera
* \[Viewport\] Display resolution and bit depth information for each channel
* \[Resources\] Base Materials is opened per default
* \[Cache\] Locate your thumbnail cache folder
* \[Cache\] Locate your render cache folder
* \[Panels\] Material Settings panel is temporarily hidden
* \[Workflow\] Specular/Glossiness temporarily deactivated
* \[MacOS\] Catalina OS version notarization
* \[Content\] New version of the Delighter filter
* \[Content\] New Image Content Aware Fill filter
* \[Content\] New Material Content Aware Fill filter
* \[Content\] Transform filter has a safe transform option

**Fixed:**

* All previous bugs related to Create are invalid today with new UI and architecture release
* Tooltips don't hide the icons in the top bar (3D, 2D, 2D/3D)
* \[Content\] Splatter filter accepts Atlas with complete height map
* \[Content\] Transform filter works on images (scan1, scan2,...)

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

* \[Create\] Some filters were listed in the quick accessor but not in the filter panel
* \[MacOS\] Fixed some crashes at exit

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

* \[Resources\] Connect and mirror your material folders on your local disks
* \[Resources\] Browse your materials folders and their subfolders
* \[Resources\] Detach your material resources panel in a separate window to see your resources in full screen
* \[Resources\] New Resources panel Layout to support folders and subfolders navigation
* \[Resources\] Use the breadcrum to navigate through your folders
* \[Resources\] Force the synchronization of your local folder with the Sync option accessible via righ-click
* \[Resources\] Disconnect your local folder with the Disconnect option accessible via righ-click
* \[Manage\] Display embedded tags of Substance files
* \[Manage\] Add, edit and delete tags of your materials
* \[Manage\] Rate your materials
* \[Layers\] Support Panorama output
* \[Layers\] You can delete Image inputs in the Image Import layer
* \[Layers\] Automatic selection of the new added layer
* \[Layers\] Automatic selection of the layer below after a layer deletion
* \[UX\] Keep left panels visibility when switching to another Lab
* \[UX\] Do not create a base layer or open the Material Workflow popup when importing images in a non-empty layers stack
* \[UI\] New Textfield style
* \[UI\] New SearchBox style
* \[UI\] New Panel header style
* \[UI\] New Busy indicator style
* \[UI\] New Layers stack background style
* \[UI\] Use Adobe Clean font
* \[UI\] Remove eyedropper icon placeholder of color input parameter
* \[Performance\] Busy indicator optimization
* \[Content\] New Pattern Generator filter
* \[Content\] New Blur filter

**Fixed:**

* \[Inspire\] Fix crash when using more than 10 colors
* \[2D View\] Fix scrollbar on the channel list of the 2D view
* \[Viewer\] Fix crash when importing a non power of 2 environment map
* \[Content\] Fix PNG import for custom pattern of Embossing and Perforation filters
* \[Export\] Fix normal and height 16 bits per channel export
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

* \[Filters\] Access quickly to your filters by pressing the space bar
* \[Filters\] New dedicated panel to manage, browse and import your filters
* \[Metadata\] Right click on a material to see its metadata
* \[Metadata\] Right click on a material to see its location on your disk
* \[Sliders\] Animate sliders when you hover them by pressing Ctrl
* \[Sliders\] Stop and restart your sliders animation by pressing P
* \[Export\] SBSAR export follows Substance Source guidelines
* \[License\] Activate Substance Alchemist using an environment variable
* \[UX\] File dialog remembers the last file path selected
* \[UX\] Folder dialog remembers the last folder path selected
* \[UI\] Update Resources panel UI
* \[UI\] Update Search bar UI
* \[UI\] Create New material icon is updated
* \[Help\] URLs are updated to substance3d.com domain
* \[Mesh\] A Cloth mesh is now available
* \[Content\] New Corrosion Filter
* \[Content\] New Oxydation Filter
* \[Content\] New Moss Filter
* \[Content\] New Dust Filter
* \[Content\] New Brickwall pattern Filter
* \[Content\] New Stonewall pattern Filter
* \[Content\] New Wood Finish Filter
* \[Content\] New Metal Finish Filter
* \[Content\] New Snow Filter
* \[Content\] New Randomizer Filter
* \[Content\] You can now import your textures directly in the Base Material filter

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

* \[Engine\] Substance Engine update to be compatible with the latest Substance Designer version
* \[License\] Update license folder for first installations
* \[Layers\] Reload at any time your layer stack to update your custom filters

**Fixed:**

* \[Data Compatibility\] Preventive fix to limit data corruption at upgrade time

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

* \[Metadata\] See and fill materials metadata in a dedicated tab
* \[Collection\] Create a collection directly from the search results
* \[Media Publishing\] Export a board of a collection
* \[UX\] Undo a tweak change or image import by pressing Ctrl+Z
* \[UX\] Redo a tweak change or image import by pressing Ctrl+Shift+Z
* \[UI\] New icons with a new style
* \[Performance\] New Session manager to better handle the tabs switching
* \[Performance\] Faster opening of the Image Import layer
* \[Content\] New Metal generic material
* \[Content\] New Rust material
* \[Content\] New Stone generic material
* \[Content\] Embossing filter update
* \[Content\] Embroidery filter update
* \[Content\] Paint filter update
* \[Content\] Delighter filter update

**Fixed:**

* \[Content\] Water filter is working in the Specular/Glossiness workflow
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

* \[Stack\] Crash when removing a splatter layer
* \[Data\] Asset database gets corrupted when application crashes
* \[Data\] Substance Alchemist cannot start when the asset database is corrupted
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
* \[UI\] Clone Tool new UI with brush size visualization
* \[UI\] Select and delete hidden stages
* \[UI\] New Textfield UI
* \[Help\] Access Substance Source, Substance Share and Substance academy websites
* \[Content\] New default materials with generators and atlas
* \[Content\] Bitmap to Material Update
* \[Content\] Dirt Update
* \[Content\] Rust Update
* \[Content\] New Embossing filter
* \[Content\] New Embroidery filter
* \[Content\] New Erode filter
* \[Content\] New Gravel Generator
* \[Content\] New Paint filter
* \[Content\] New Parquet Pattern filter
* \[Content\] New Pavement Pattern filter
* \[Content\] New Perforation filter
* \[Content\] New Splatter filter
* \[Content\] New Textile Wear filter
* \[Content\] New Transform filter

**Fixed:**

* \[Viewport\] Sphere mesh with tiling x2 on X
* \[Viewport\] Crash when loading your own environment
* \[Viewport\] Environment map are now using the exposure value too
* \[Viewport\] F shortcut doesn't reset camera angle
* \[Export\] SBS export works with latest Substance Designer 2018.3.3
* \[Export\] SBSAR export respects the same guidelines as Substance Source materials
* \[UI\] Scrollbars can be dragged
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

* \[Layer stack\] Layer re-ordering
* \[Layer stack\] Delete an hidden layer
* \[Layer stack\] Import a material directly at the position of your choice
* \[Layer stack\] Material input as a new filter parameter type
* \[Performance\] Substance Engine budget is dynamic for better performances
* \[Performance\] Better OpenGL performances especially on MacOS
* \[Data\] Faster data upgrade after a new version is released
* \[Content\] AI Delighter available on Windows 7 and Windows 8
* \[Content\] AI Delighter available on RTX GPU

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

* \[Export\] Substance archive (sbsar) export of your collection
* \[Export\] Substance file (sbs) export of your collection
* \[Export\] Export queue visible in the Export panel
* \[Export\] Name your collection or material before export
* \[Data\] Save As your material by pressing Ctrl+Shift+S
* \[Data\] Save your material by pressing Ctrl+S
* \[Data\] Collections and Materials are compatible across versions
* \[Data\] Update your material layer stack with up-to-date filters
* \[Data\] Hot reload of imported custom filters
* \[UI\] Visual feedback in the viewport while it's computing
* \[UI\] New button style
* \[UI\] Save pop-up displays the name of the active collection
* \[UI\] Modify source images of an Image(s) Import Layer
* \[Content\] Custom usages are now supported
* \[Content\] More images format are supported in image input parameters
* \[Content\] New Tiling Filter named Make It Tile Advanced
* \[Content\] Update of the Water filter

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

* \[Export\] New Export pop-up
* \[Export\] Export an entire collection
* \[Export\] Export Bitmaps at the format of your choice
* \[Export\] Export Bitmaps at the resolution of your choice
* \[Export\] Export only the channels of your choice
* \[Export\] Preview the estimation size of your export
* \[Export\] Preview the available size on your disk before exporting
* \[UX\] Actions on collection accessible using right-click
* \[UX\] Allow to unset an image or an asset in Inspire
* \[UX\] Substance Alchemist is launched maximized
* \[Assets\] New way of saving your materials in order to keep them persistent with next versions
* \[Help\] Access to the online documentation via the help menu
* \[Performance\] Faster color variations on complex materials created with Substance Alchemist
* \[Performance\] Reduce memory leaks when switching Labs
* \[Content\] Scale checker to diagnostic the physical size of your material
* \[Content\] Update Italien Venice Mosaic tile material
* \[Content\] Update Moss splatter

**Fixed:**

* No more default name when saving a material
* Filters parameters are lost after saving a material and reopening Substance Alchemist
* \[Content\] Fix from bottom and from top logic for AO and curvature blending

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
* \[Log\] Export log file via the help menu
* \[UI\]New Sliders Style
* \[UI\]Presets and Tweak panels are merged
* \[UI\]New Thumbnails style
* Displacement, Tiling and Shadows settings accessible directly in the viewport
* \[Content\] New Default Materials
* \[Content\] Moss Splatter update
* \[Framework\] Update Substance Engine Framework

**Fixed:**

* Deletion of your layer stack by switching Labs is fixed
* Loading time values displayed in the viewport are correct
* Material workflow default channels are correctly initialized
* Disable Custom Mesh Import
* Bitmap export
* \[MacOS\] Closing Substance Alchemist can need a "Force to quit"

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
* \[MacOS\] Substance Alchemist can be set in full screen
* \[Filter\] Import Custom mask to manage the blending between two materials
* \[Filter\] Control Moss scale
* \[Filter\] Clone Patch update

**Fixed:**

* Add an image in an image input in the parameter list updates outputs
* Import Custom filter doesn't add a black Ambient Occlusion and a black opacity

**Known Issues:**

* Materials created with a previous version won't be available in the new one.
* \[MacOS\] Closing Substance Alchemist can need a "Force to quit"
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