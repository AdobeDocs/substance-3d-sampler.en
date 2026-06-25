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

### **6.0.2**

*(Released: June 25th, 2026)*

#### Added:

* &lbrack;Assets&rbrack; Check sbsar version and warn users is the engine is too old to read it
* &lbrack;Captis&rbrack; Add back option to save captis photometry in preferences

#### Fixed:

* &lbrack;2D View&rbrack; Do not 'display with physical ratio' if physical size is disabled
* &lbrack;Analytics&rbrack; Missing analytics events
* &lbrack;Analytics&rbrack; Prevent crashpad to report a crash on vk devicelost
* &lbrack;Application&rbrack; Do not destroy vkdevices at exit to avoid a crash in nvidia driver
* &lbrack;Application&rbrack; Fix linked collection watcher exit + channel manager
* &lbrack;Application&rbrack; Prevent a crash at exit
* &lbrack;Content&rbrack; "metal finish" filter does not impact metalness
* &lbrack;Content&rbrack; Add physical size to dynamic filters where it is missing
* &lbrack;Filters&rbrack; Remove content aware fill from hidden assets list
* &lbrack;Layers&rbrack; Clicking 'reset all settings' does not reset the 'applies to' dropdown
* &lbrack;Layers&rbrack; Fix tweak min & max for position widget
* &lbrack;Layers&rbrack; Properly update filter
* &lbrack;Physical Size&rbrack; Ensure physical scale is working everywhere + make physicalsize ok with dynamic filters
* &lbrack;Project&rbrack; Ensure asset resolution is the default one (2k x 2k) when creating a new asset
* &lbrack;Project&rbrack; Re-opening current project used to open previous version
* &lbrack;Project&rbrack; Sampler does not offer to restore a backup of corrupted projects anymore
* &lbrack;Rendering&rbrack; Render material thumbnail at a maximum of 2k resolution
* &lbrack;UI&rbrack; Defensive code to avoid crash if user is faster than UI

### **6.0.1**

*(Released: May 21st, 2026)*

#### **Added:**

* &lbrack;Application&rbrack; Warn user when opening a project with 3D objects or environment lights
* &lbrack;Captis&rbrack; Make the UI adapt to small screens
* &lbrack;Captis&rbrack; Update Captis UI
* &lbrack;Channel Settings&rbrack; Automatically activate SSS when using SSS channel in ASM
* &lbrack;Engine&rbrack; Update Substance Engine to version 9.4.3
* &lbrack;Preset&rbrack; Switch 'apply preset thumbnail values' on by default
* &lbrack;Resources&rbrack; Display 'all libraries' by default instead of 'starter assets' in resources panel
* &lbrack;Scripting&rbrack; Add Python functions to manage 'Applied to' of a layer
* &lbrack;UI&rbrack; Asset list is now responsive: asset size adapts to the container
* &lbrack;UI&rbrack; Display 3D/2D view by default
* &lbrack;UI&rbrack; Display material optimization popup when dropping a material from explorer
* &lbrack;UI&rbrack; Enable flipping of device bar buttons tooltip

#### **Fixed:**

* &lbrack;Application&rbrack; Fix color space issues
* &lbrack;Application&rbrack; Fix settings updater
* &lbrack;Application&rbrack; Make scan channels active when they are set to auto
* &lbrack;Application&rbrack; New project button from home screen no longer erases previous project with same name
* &lbrack;Application&rbrack; Prevent a crash at exit on macOS
* &lbrack;Application&rbrack; Prevent accessing asset of invalid asset references
* &lbrack;Application&rbrack; Prevent crash when accessing surface from VersionedImage in a tweak
* &lbrack;Application&rbrack; Prevent crash when deleting a stage when there is none
* &lbrack;Captis&rbrack; Ensure Captis is disconnected before closing Sampler
* &lbrack;Captis&rbrack; Prevent USB-2 warning from being displayed twice
* &lbrack;Channel Settings&rbrack; Fix OpenPBR channel names
* &lbrack;Channel Settings&rbrack; Update long labels for OpenPBR channels
* &lbrack;Content&rbrack; Update all mesh units from meters to centimeters for SSS values
* &lbrack;Export&rbrack; Ensure default values are plugged to dynamic filters
* &lbrack;Export&rbrack; Images are now saved in a worker thread for improved performance
* &lbrack;Filters&rbrack; Content Aware Fill crashes when switching scale on
* &lbrack;Filters&rbrack; Could not open location of a dynamic filter from asset panel
* &lbrack;Filters&rbrack; Fix reset all in AutoTiling adjustment step
* &lbrack;Filters&rbrack; Restore disable usage processing in tree structures creation
* &lbrack;Filters&rbrack; Set the correct default value for upscale parameter
* &lbrack;Filters&rbrack; Update generators even if they are in a fill layer
* &lbrack;Layers&rbrack; Forbid renaming input layer header or placeholder layers
* &lbrack;Layers&rbrack; Prevent crash during layer insertion due to a dangling pointer
* &lbrack;Layers&rbrack; Wrong number of images in flatten layer name
* &lbrack;Localization&rbrack; Ensure preset names are updated when switching languages
* &lbrack;Localization&rbrack; Multiple translation issues in resources panel
* &lbrack;Localization&rbrack; Quick Actions categories localization issues
* &lbrack;Performance&rbrack; Load tweaks only on opened section
* &lbrack;Preferences&rbrack; Clearing preference cache path resets to previous value
* &lbrack;Rendering&rbrack; Memory leak when using Path Tracer
* &lbrack;Rendering&rbrack; Prevent deleting textures while they may still be accessed by Vulkan
* &lbrack;Rendering&rbrack; Texture rotation was not converted from 0-1 to 0-360
* &lbrack;Scripting&rbrack; Remove nonexistent classes from Python documentation
* &lbrack;Scripting&rbrack; selectedAsset returns None if there is no selected asset
* &lbrack;Tools&rbrack; Resetting a texture value now stops painting and clears patch view
* &lbrack;UI&rbrack; Do not close sections in properties panel whenever something is tweaked
* &lbrack;UI&rbrack; Exposed color tweak label invisible on hover
* &lbrack;UI&rbrack; Fix asset list responsive behavior
* &lbrack;UI&rbrack; Fix binding loop in AssetItem tooltip
* &lbrack;UI&rbrack; Fix doubleclick on selected preset group
* &lbrack;UI&rbrack; Fix drop area in image presenter
* &lbrack;UI&rbrack; Fix label with a button in it for all languages
* &lbrack;UI&rbrack; Fix line height for Japanese in channel list popup
* &lbrack;UI&rbrack; Fix onAccepted signal of length field
* &lbrack;UI&rbrack; Fix popup width with long left control item
* &lbrack;UI&rbrack; Fix preview popup in asset items
* &lbrack;UI&rbrack; Fix rough/reflective picker
* &lbrack;UI&rbrack; Fix string ellipsis
* &lbrack;UI&rbrack; Fix string truncation problem
* &lbrack;UI&rbrack; Fix switch tweak reset button
* &lbrack;UI&rbrack; Hide the Material model dropdown when a custom export preset is selected
* &lbrack;UI&rbrack; Remove resolution in channel list of export popup
* &lbrack;UI&rbrack; Reset to default layout keeps projection viewer settings
* &lbrack;UI&rbrack; Restore 'Edit in Photoshop' and 'Edit in Illustrator' menu items

#### Removed:

* &lbrack;UI&rbrack; Remove 'Applied to' section for image import layers
* &lbrack;UI&rbrack; Remove auto-open quick action tooltip at first launch

## Version 5

### **5.1.3 ÎLE FLOTTANTE**

*(Released: January 6, 2026)*

#### Added:

* &lbrack;Captis&rbrack; Display a warning if the FTP protocol is disabled by the firewall

#### Fixed:

* &lbrack;Captis&rbrack; Aborting during a capture can lead to errors
* &lbrack;Captis&rbrack; Downloading the results at the end of a capture uses to much RAM
* &lbrack;Captis&rbrack; Executing an auto-focus immediately after an auto-intensity can lead to errors
* &lbrack;Captis&rbrack; The display of HDR results in the Summary panel
* &lbrack;UI&rbrack; In some cases, the folder dialog on MacOS does not select the right folder

### **5.1.2 ÎLE FLOTTANTE**

*(Released: November 20th, 2025)*

#### Added:

* &lbrack;Application&rbrack; Detect graphics device loss, warn the user and exit gracefully
* &lbrack;Layers&rbrack; Improved messaging when flattening layers
* &lbrack;Layers&rbrack; Improved thumbnails for Image Import and Flattened Layers layers
* &lbrack;Onboarding&rbrack; Updated learning content on the Home screen
* &lbrack;Project&rbrack; Recover last saved state of session before crash
* &lbrack;UI&rbrack; Application icon update

#### Fixed:

* &lbrack;Application&rbrack; Inserting a material in the layer stack might lead to a crash on macOS
* &lbrack;Application&rbrack; Possible crash on heavy load on macOS
* &lbrack;Application&rbrack; Possible crash when adding layers when video memory is full
* &lbrack;Application&rbrack; Possible crash when opening a project
* &lbrack;Captis&rbrack; Failure if auto focus is run shortly after automatic intensity calibration
* &lbrack;Captis&rbrack; Reliability and performance issues after first capture
* &lbrack;Captis&rbrack; Slowdowns and errors when copying files at the end of a capture
* &lbrack;Captis&rbrack; Small memory leak when querying Captis device information
* &lbrack;Export&rbrack; Multi slider exposed parameters produce corrupted .sbsar files
* &lbrack;Layers&rbrack; Auto tiling pattern is reset to default values when switching assets
* &lbrack;Layers&rbrack; Default custom base color is displayed red
* &lbrack;Layers&rbrack; Partial flattening of Clone Stamp child layers is possible and causes rendering issues
* &lbrack;Layers&rbrack; Possible crash when tweaking a layer stack while rendering is in progress
* &lbrack;Layers&rbrack; Unexpected error in auto tiling region of interest step when changing source channels
* &lbrack;Project&rbrack; Incorrect thumbnail sometimes when creating a new material
* &lbrack;Quick Actions&rbrack; Some quick actions have a wrong input count
* &lbrack;UI&rbrack; Action group button have different widths
* &lbrack;UI&rbrack; Clear button in text fields sometimes triggers focus loss
* &lbrack;UI&rbrack; Combo boxes and text fields are too big
* &lbrack;UI&rbrack; Icons and labels are misaligned
* &lbrack;UI&rbrack; Name field label is incorrectly placed
* &lbrack;UI&rbrack; Quick Actions button labels are misaligned
* &lbrack;UI&rbrack; Sliders show too wany trailing 0s

#### Removed:

* &lbrack;Generative AI&rbrack; Generative AI features removal. *This feature has been removed from the application and the service will stop working in previous versions of Sampler on March 5th.*

### **5.1.1 ÎLE FLOTTANTE**

*(Released: September 18th, 2025)*

#### Added:

* &lbrack;2D View&rbrack; Be able to zoom out more in the 2D view for high resolution textures
* &lbrack;Captis&rbrack; Warn users about issues when copying files
* &lbrack;Layers&rbrack; When duplicating a layer, use an incremental number in the new layer name

#### Fixed:

* &lbrack;2D View&rbrack; When painting strokes after resetting all the properties of Clone Stamp, previously created strokes reappear
* &lbrack;Application&rbrack; "Save current project?" popup uses wrong project name
* &lbrack;Application&rbrack; Crash at exit
* &lbrack;Application&rbrack; Potential crash
* &lbrack;Application&rbrack; Sometimes, a thumbnail is generated with an incorrect material
* &lbrack;Captis&rbrack; On some devices, when performing a scan in high resolution, the height map is black
* &lbrack;Captis&rbrack; The "Start capture" button is not disabled anymore when no capture name is set and when a calibration is running
* &lbrack;Export&rbrack; When exporting a .sbsar file the export can fail without the user being notified
* &lbrack;Filters&rbrack; Advanced parameters screen for the Auto Tiling filter sometimes flicker when tweaking parameters
* &lbrack;Filters&rbrack; Default parameters for the Tiling filter produce gray artifacts in the output
* &lbrack;Filters&rbrack; Sometimes with high resolution inputs, the Auto Tiling filter advanced settings do not show the individual pattern points
* &lbrack;Filters&rbrack; The pattern size for the custom size Auto Tiling parameter has an incorrect default value
* &lbrack;Layers&rbrack; Occasional color issue with the Auto Tiling filter mostly visible on red materials
* &lbrack;Layers&rbrack; Sometimes adding layers will reset some tweaks to their default value
* &lbrack;Physical Size&rbrack; Thumbnail of assets with a physical size have a wrong height scale
* &lbrack;UI&rbrack; Cannot rename exposed parameters
* &lbrack;UI&rbrack; Channel activation button are not square
* &lbrack;UI&rbrack; If a slider label is too long, the reset button is not accessible
* &lbrack;UI&rbrack; Pressing the return key or clicking out does not remove the focus from text fields
* &lbrack;UI&rbrack; Sometimes an unwanted tooltip appears in the Physical Size panel
* &lbrack;UI&rbrack; The 3D view displays an incorrect mesh when creating an empty project
* &lbrack;UI&rbrack; When exposing a color picker input, its label disappears on hover
* &lbrack;UI&rbrack; When exposing parameters, the color dot is sometimes incorrectly positioned

### **5.1.0 ÎLE FLOTTANTE**

*(Released: August 7th, 2025)*

#### Added:

* &lbrack;2D View&rbrack; Brush size now adapts to the current texture resolution
* &lbrack;3D View&rbrack; Toggle Native Display Scale for 3D Rendering in the preferences
* &lbrack;Application&rbrack; Rendering engine update
* &lbrack;Captis&rbrack; Add "make square" possibility during preview
* &lbrack;Captis&rbrack; Automatic physical size detection
* &lbrack;Captis&rbrack; Capturing a new material will create a new asset
* &lbrack;Captis&rbrack; Change resolution selection in dropdown to pixel per inch or centimetre instead of pixel resolution of maximum area
* &lbrack;Captis&rbrack; Contextual help on alignment calibration
* &lbrack;Captis&rbrack; Generate roughness map
* &lbrack;Captis&rbrack; Warn the user if the default calibration files are missing
* &lbrack;Filters&rbrack; Auto Tiling filter for structured materials and scans
* &lbrack;Filters&rbrack; New Fold Remover filter
* &lbrack;Filters&rbrack; New features within the Clone Stamp filter
* &lbrack;Filters&rbrack; New features within the Equalize filter
* &lbrack;Layers&rbrack; Ability to flatten layers
* &lbrack;Layers&rbrack; Context menu when right-clicking on a layer to rename, duplicate, delete or flatten the layer
* &lbrack;Onboarding&rbrack; Update Welcome and What's New screens content
* &lbrack;Performance&rbrack; Better performance when using the Crop filter
* &lbrack;Performance&rbrack; Improve memory usage for the 3D View
* &lbrack;Performance&rbrack; Updating the 3D view is quicker
* &lbrack;Physical Size&rbrack; Enable "display with physical ratio" when working on Substance filters when Physical Size is enabled
* &lbrack;Physical Size&rbrack; When importing images in an empty stack, propose a resolution that is more coherent with the image ratio
* &lbrack;Quick Actions&rbrack; 3 new quick actions for scan processing
* &lbrack;Scripting&rbrack; API to flatten layers
* &lbrack;Scripting&rbrack; Get the filename of each image of an image import layer
* &lbrack;Scripting&rbrack; New function to activate/deactivate a given channel of an asset
* &lbrack;UI&rbrack; Rework icons and buttons in the Layers panel to accommodate for the new features
* &lbrack;UI&rbrack; Warn about environment light authoring deprecation

#### Fixed:

* &lbrack;2D View&rbrack; Selecting 'display with physical ratio' might not work when using Substance filters
* &lbrack;3D Capture&rbrack; Svg files are listed in the file picker but not supported
* &lbrack;3D View&rbrack; Emission intensity parameter in the Shader Settings does not work
* &lbrack;3D View&rbrack; Sometimes the mesh position is incorrect when creating a new asset
* &lbrack;3D View&rbrack; Switching to Path Tracing rendering crashes on unsupported hardware
* &lbrack;Application&rbrack; Application hangs when closing the manual measure popup without setting a size
* &lbrack;Application&rbrack; Crash
* &lbrack;Application&rbrack; Freeze on Windows when displaying the desktop (Windows key + D keyboard shortcut)
* &lbrack;Application&rbrack; Possible crash when switching language
* &lbrack;Captis&rbrack; Crash when the preview data is not valid
* &lbrack;Captis&rbrack; Impossible to fully zoom out after zooming in
* &lbrack;Captis&rbrack; Missing localization on some wizard steps
* &lbrack;Captis&rbrack; Possible crash at exit when using Captis
* &lbrack;Captis&rbrack; Scanning does not work if the device is missing calibration files
* &lbrack;Filters&rbrack; Brush preview when using the Clone Stamp filter may be wrong depending on the texture and brush sizes
* &lbrack;Filters&rbrack; Erroneous output size after using the Upscale filter
* &lbrack;Filters&rbrack; Missing icons for Environment Rotation and Stylization filters
* &lbrack;Filters&rbrack; Updating some filters may lead to incorrect rendering
* &lbrack;Layers&rbrack; Incorrect first render when blending two materials
* &lbrack;Layers&rbrack; The button to update layers shows "Update All" even when there is only one update
* &lbrack;Layers&rbrack; Unnecessary computations when importing images in the layer stack
* &lbrack;Performance&rbrack; Improve normal map format handling to reduce rendering times
* &lbrack;Physical Size&rbrack; Manual measurement popup only works after doing an auto-measure
* &lbrack;Physical Size&rbrack; Wrong export resolution in the Export popup when Physical Size is enabled
* &lbrack;Quick Actions&rbrack; Missing localization on generated asset names
* &lbrack;UI&rbrack; Asset preview on hover may not show
* &lbrack;UI&rbrack; Clicking the Reset to default value button might break some of the controls
* &lbrack;UI&rbrack; Error messages are not cleared when switching projects
* &lbrack;UI&rbrack; Make sure material name in viewport & properties panel are empty when there is no asset
* &lbrack;UI&rbrack; Reset to default value button for the Point of View parameter does not work
* &lbrack;UI&rbrack; Reset to default value button overlap
* &lbrack;UI&rbrack; Some buttons are not clickable when a panel is undocked
* &lbrack;UI&rbrack; Texture tilling V Parameter partially hidden in Viewer Settings and 3D View

#### Removed:

* &lbrack;3D Capture&rbrack; Remove 3D Capture support
* &lbrack;Application&rbrack; Remove macOS x86 support

### **5.0.3 HAZELNUT**

*(Released: Jun 3rd, 2025)*

#### **Added:**

* &lbrack;Captis&rbrack; Allow to give a material same name as an already existing one
* &lbrack;Captis&rbrack; Move error messages to popups instead of toasts
* &lbrack;Filters&rbrack; Update embroidery
* &lbrack;Preferences&rbrack; Add reset in viewer settings and shaders settings
* &lbrack;UI&rbrack; Do not present the 'Show location' menu item on project assets

#### **Fixed:**

* &lbrack;3D Capture&rbrack; Mesh post process filter doesn't output expected maps
* &lbrack;3D View&rbrack; 3D view does not work because of shader cache corruption
* &lbrack;3D View&rbrack; Ground plane and grid are vertical when scene is Z-up
* &lbrack;3D View&rbrack; The mesh sometimes disappears
* &lbrack;Application&rbrack; Closing login window at start-up without logging in sometimes crashes the app
* &lbrack;Application&rbrack; Crash when access to the plugins configuration file is denied
* &lbrack;Application&rbrack; Current material is un-selected when the project is saved
* &lbrack;Application&rbrack; Resetting to default layout sets the resolution to 64x64
* &lbrack;Application&rbrack; Sampler sometimes crashes when rendering a layer stack
* &lbrack;Export&rbrack; Export resolution is sometimes reset to 64x64
* &lbrack;Export&rbrack; It is sometimes not possible to export .sbs/.sbsar files
* &lbrack;Layers&rbrack; Add base material button does nothing when the material is empty
* &lbrack;Layers&rbrack; Texture tiling is changed when duplicating a material
* &lbrack;Physical Size&rbrack; Auto-measure does not work if the Physical Size panel was docked before importing the image
* &lbrack;Scripting&rbrack; Autosave plugin is broken
* &lbrack;UI&rbrack; Incorrect spacing in the Export dialog
* &lbrack;UI&rbrack; Slider animation of tweaks does not work anymore
* &lbrack;UI&rbrack; Sliders don't snap to integer values when needed
* &lbrack;UI&rbrack; Some drop down menus are cropped

### **5.0.2 HAZELNUT**

*(Released: April 22th, 2025)*

#### **Fixed:**

* &lbrack;Application&rbrack; Back button on the Homepage is broken
* &lbrack;Application&rbrack; Sampler sometimes won't launch if corrupted data from previous versions is present on disk
* &lbrack;Application&rbrack; The image imported does not appear in the viewport or the layer stack
* &lbrack;Captis&rbrack; Captis IP address field remains empty even after restarting Sampler
* &lbrack;Captis&rbrack; Live camera preview only works when application language is set to English
* &lbrack;Export&rbrack; Crash during export &lbrack;Layers&rbrack; Painting sometimes does not work in previously saved projects
* &lbrack;Layers&rbrack; Sampler sometimes updates all textures when only one channel is updated
* &lbrack;Layers&rbrack; Unable to use material blends in the layer stack after upgrading to 5.0.x
* &lbrack;Layers&rbrack; Updating a project with an previous Image to Material (AI) version makes material all black
* &lbrack;Layers&rbrack; When trying to import an unsupported image, Sampler creates a broken layer
* &lbrack;Scripting&rbrack; Part of the Python API does not work with an empty project
* &lbrack;UI&rbrack; Menu items sometimes overflow in the File menu

### **5.0.1 HAZELNUT**

*(Released: March 20th, 2025)*

#### **Added**:

* &lbrack;Application&rbrack; Updated graphics driver compatibility list
* &lbrack;Captis&rbrack; Show a popup when usage of HP Z Captis is blocked by operating system policies
* &lbrack;Quick Actions&rbrack; Explain why a Quick Action is disabled in a tooltip
* &lbrack;UI&rbrack; Crash report window UI styling
* &lbrack;UI&rbrack; When copying to clipboard, show a toast to say it is done

#### **Fixed:**

* &lbrack;2D View&rbrack; Exposure slider has no effect when spherical projection is off
* &lbrack;2D View&rbrack; Painting outside of the texture creates a discontinued stroke
* &lbrack;2D View&rbrack; The exposure button has no tooltip
* &lbrack;2D View&rbrack; Zooming on the side of a non square image does not follow the mouse
* &lbrack;3D Capture&rbrack; 3D Capture does not work on Windows 11 24H2
* &lbrack;3D Capture&rbrack; Crash if we quit Sampler during the mesh reconstruction step
* &lbrack;3D View&rbrack; Compute time is sometimes shown as 0ms
* &lbrack;3D View&rbrack; When changing projection from orthographic to perspective, viewport becomes grey
* &lbrack;Application&rbrack; Crash at startup when checking GPU capabilities
* &lbrack;Application&rbrack; Crash during install
* &lbrack;Application&rbrack; Crash on exit after right-clicking a metadata field
* &lbrack;Application&rbrack; Environment light missing when opening an SBSAR from the operating system file explorer
* &lbrack;Application&rbrack; Opening a .sbsar while Sampler is running changes the Texture Tiling setting
* &lbrack;Captis&rbrack; Some metadata might not transfer between the capture steps
* &lbrack;Captis&rbrack; The name of the created asset is not the one entered in the metadata field
* &lbrack;Content&rbrack; Sample project prompts for a filter update but is already up to date
* &lbrack;Filters&rbrack; Normal/height adjustment filter has no icon
* &lbrack;Layers&rbrack; Cannot change images in an image import layer
* &lbrack;Layers&rbrack; Crashes when using the Upscale filter
* &lbrack;Layers&rbrack; Updating a project with an old Image to Material makes the material all black
* &lbrack;Rendering&rbrack; Tweaking a layer stack immediatly after creating an asset breaks the rendering
* &lbrack;Scripting&rbrack; The Autosave pluging crashes when there is no asset in the project
* &lbrack;Tools&rbrack; Brush size value is missing in the Brush Toolbar
* &lbrack;UI&rbrack; Changing the application language doesn't update some of the labels in the Home Screen
* &lbrack;UI&rbrack; Hitting Escape or Enter in Slider text fields won't lose focus
* &lbrack;UI&rbrack; In the Properties panel, the reset all button and the asset name label overlap
* &lbrack;UI&rbrack; Issues when docking and undocking panels
* &lbrack;UI&rbrack; Scrolling in an overlay panel will also scroll in the underlying window
* &lbrack;UI&rbrack; Switching to List view in the Recent Projects section of the Home Screen does not work
* &lbrack;UI&rbrack; Viewport display mode button icon always shows 2D/3D

### **5.0.0 HAZELNUT**

*(Released: February 20th, 2025)*

#### **Added**:

* &lbrack;Onboarding&rbrack; New Homepage with quick access to learning content, sample project, quick actions and recent projects.
* &lbrack;Onboarding&rbrack; Get started quickly with the new Quick Actions, accessible from the homepage and from dedicated panel
* &lbrack;Onboarding&rbrack; &lbrack;Content&rbrack; Quick Actions are predefined workflows that populate the layer stack with most used layers
* &lbrack;Onboarding&rbrack; Possibility to create a new project via a new Quick start menu, via quick actions or Custom Project
* &lbrack;Onboarding&rbrack; Possibility to create empty project directly from homepage via dedicated button
* &lbrack;3D View&rbrack; New advanced rasterizer and pathtracer bringing new rendering capabilites (properties such as coating, sheen, translucency, subsurface scattering) and visual consistency across Substance ecosystem
* &lbrack;3D View&rbrack; Viewer settings are now accessible directly in the 3D view
* &lbrack;3D View&rbrack; Possibility to save a render snapshot in clipboard or in files
* &lbrack;3D View&rbrack; Display a grid to visualize the scene origin
* &lbrack;3D View&rbrack; Enable the ground plane to catch shadows and reflections
* &lbrack;3D View&rbrack; Control how reflective and opaque is your ground plane
* &lbrack;3D Capture&rbrack; Position mesh on ground
* &lbrack;Application&rbrack; Check hardware compatibility on application startup
* &lbrack;Application&rbrack; Crash reporting window now opens right after a crash occurs
* &lbrack;Content&rbrack; Open a sample project to easily get started
* &lbrack;Export&rbrack; Export Adobe Standard Material shader in USD files
* &lbrack;Generative AI&rbrack; Check "Do not infer" tag when using image as an input in Image to Texture workflows
* &lbrack;Project&rbrack; Thumbnails are stored within the project file for faster opening of projects
* &lbrack;Project&rbrack; Setting in the preferences to store cache data within the project file, with different modes (no cache, light cache, full cache)
* &lbrack;Scripting&rbrack; &lbrack;Breaking change&rbrack; Qt migration to Qt6.15 - impact compatibility of existing plugins
* &lbrack;Scripting&rbrack; Default plugins and script folder are now in the Documents folder
* &lbrack;Scripting&rbrack; New UI for plugins for visual consistency with main Sampler panels
* &lbrack;Scripting&rbrack; Access 2 plugin examples to discover Sampler plugin capabilities
* &lbrack;Scripting&rbrack; New open_3d_catpure() function
* &lbrack;Scripting&rbrack; When inserting a layer, control if it is inserted above or below the target position

#### **Fixed:**

* &lbrack;3D Capture&rbrack; Crash if Object Capture cannot be started on macOS
* &lbrack;Application&rbrack; Crash at exit
* &lbrack;Application&rbrack; Hang at exit while adding assets to the project panel
* &lbrack;Application&rbrack; Renaming a project asset does not work unless you press enter
* &lbrack;Application&rbrack; Undo and redo menu entries are not disabled when they should be
* &lbrack;Assets&rbrack; Unable to delete assets from the All Libraries section of the Assets panel
* &lbrack;Content&rbrack; Atlas creator - Use existing opacity map if present
* &lbrack;Content&rbrack; Color ID Blend - Fix color picking in the basecolor
* &lbrack;Layers&rbrack; Avoid useless computation when using generators
* &lbrack;Layers&rbrack; Tweaking a generator may lead to triggering too many computes
* &lbrack;Performance&rbrack; Improve GPU memory management
* &lbrack;Performance&rbrack; Render cache may not be used when restarting the app
* &lbrack;Resources&rbrack; Read only files are not visible in the Assets panel
* &lbrack;Scripting&rbrack; Allow reusing a layer after adding another layer
* &lbrack;Scripting&rbrack; Changing the layer stack structure several times in one script may fail

#### **Removed:**

* &lbrack;Application&rbrack; Remove support for .dng and .nef image files

## Version 4

### **4.5.2 GRUYERE**

*(Released: 07 November 2024)*

#### **Fixed:**

* &lbrack;Content&rbrack; Crop, Embroidery and Height blend filters

### **4.5.1 GRUYERE**

*(Released: 30 July 2024)*

#### **Fixed:**

* &lbrack;Layers&rbrack; Painting greyscale masks does not work, impacting tools like Clone Stamp, Paint Warp, Content Aware Fill

### **4.5.0 GRUYERE**

*(Released: 18 July 2024)*

#### **Added**:

* &lbrack;Interoperability&rbrack; Send materials to UE5, Blender, Maya, 3DsMax Unity
* &lbrack;Content&rbrack; New texture generator category - Gradients
* &lbrack;Content&rbrack; HDRI Tools - new Environment rotation filter

#### **Fixed:**

* &lbrack;Exposed Parameters&rbrack; Exposing .sbsar input values do not work
* &lbrack;Layers&rbrack; Base color turns red with greyscale images
* &lbrack;Rendering&rbrack; Grayscale images used in color channels have wrong color space
* &lbrack;Scripting&rbrack; Using an export preset sometimes doesn't export the expected channels
* &lbrack;Content&rbrack; Dirt - Applying a Dirt filter on top of Image to Material generates a black normal
* &lbrack;Content&rbrack; Emboss - Scaling of a pattern in the emboss filter is not linear between 0 and 1
* &lbrack;Content&rbrack; Make it tile - Improved normal and height consistency

### **4.4.1 FONDUE**

*(Released: 6 June 2024)*

#### **Fixed:**

* &lbrack;Content&rbrack; Dirt filter is missing
* &lbrack;Generative AI&rbrack; Network error sometimes occur when using Image to Texture

### **4.4.0 FONDUE**

*(Released: 23 May 2024)*

#### **Added**:

* &lbrack;Application&rbrack; 3D Capture cache is now stored in a separate sub-folder
* &lbrack;Generative AI&rbrack; Image to Texture (Beta)
* &lbrack;Generative AI&rbrack; Text to Pattern (Beta)
* &lbrack;Generative AI&rbrack; Text to Texture (Beta)
* &lbrack;Scripting&rbrack; Assets now have a 'resource' property
* &lbrack;Scripting&rbrack; Layers now have a 'output_usages' property

#### **Fixed:**

* &lbrack;Application&rbrack; Crash when opening corrupted project file
* &lbrack;Application&rbrack; Crash when project contains corrupted assets
* &lbrack;Application&rbrack; Crash when unplugging a monitor on Windows
* &lbrack;Application&rbrack; Incorrect application icon in the Windows task bar
* &lbrack;Application&rbrack; Main configuration file corruption can lead to files deletion
* &lbrack;Application&rbrack; Panels appear in front of popups
* &lbrack;Content&rbrack; Texture generators have blurry thumbnails
* &lbrack;Export&rbrack; Opacity channel generated from an imported image breaks when exporting a .sbs/.sbsar
* &lbrack;Filters&rbrack; Upscale can crash depending on its input layers
* &lbrack;Generative AI&rbrack; Possible crashes when receiving unexpected results from the service
* &lbrack;Scripting&rbrack; Crash when autoloading a plugin from environment variable
* &lbrack;Scripting&rbrack; Possible crash when assigning Output Usage with the API

### **4.3.3 EMPANADA**

*(Released: 26 March 2024)*

#### **Added:**

* &lbrack;3D Capture&rbrack; New advanced auto-UV parameters during Post Process
* &lbrack;Filters&rbrack; Perforate filter: ability to invert and change the size of the custom pattern

#### **Fixed:**

* &lbrack;3D Capture&rbrack; Base color can be incorrect on macOS
* &lbrack;3D Capture&rbrack; Crash when processing a new version
* &lbrack;3D Capture&rbrack; Post-Process step can crash on macOS
* &lbrack;3D Capture&rbrack; The Mesh Transform layer can lead to incorrect rendering
* &lbrack;Application&rbrack; Crash when starting Sampler while a previous instance is still exporting
* &lbrack;Application&rbrack; Sampler is unresponsive for a moment when started for the first time
* &lbrack;Export&rbrack; Anisotropy Angle map is not exported
* &lbrack;Filters&rbrack; Adding Cloth Weave to the layer stack can lead to a crash
* &lbrack;Filters&rbrack; Adding Emboss to the layer stack can lead to a crash
* &lbrack;Filters&rbrack; Content-Aware Fill crashes when using 32 bit images
* &lbrack;Filters&rbrack; Emboss: Opacity of the layers below aren't completely overriden
* &lbrack;Filters&rbrack; Fill: Blend mode does not work in Designer and Painter
* &lbrack;Filters&rbrack; Embroidery: automatic color selection is broken
* &lbrack;Preferences&rbrack; Prevent setting an unsupported path for 3D Capture cache
* &lbrack;Preferences&rbrack; The Normal Format preference does not work
* &lbrack;Scripting&rbrack; The channels parameters of Asset.export_material is case sensitive

### **4.3.2 EMPANADA**

*(Released: 22 February 2024)*

#### **Fixed:**

* &lbrack;Application&rbrack; Saving a project on a network share on Windows corrupts the project file

### **4.3.1 EMPANADA**

*(Released: 15 February 2024)*

#### **Fixed:**

* &lbrack;3D Capture&rbrack; Crash when image files become inaccessible while batch generating masks
* &lbrack;Export&rbrack; Exporting a material with Crop or relative to input policy layer gives invalid results
* &lbrack;Layers&rbrack; Rare crash when rendering a layer stack
* &lbrack;Filters&rbrack; Embroidery - Fix issue when using material input on MacOS
* &lbrack;Filters&rbrack; Stylization - Support Texture Generators
* &lbrack;Filters&rbrack; Pattern - Fix parameters naming
* &lbrack;Localization&rbrack; "Save as..." in hardware information window under help menu is appearing unlocalized

### **4.3.0 EMPANADA**

*(Released: 25 January 2024)*

#### **Added**:

* &lbrack;Assets&rbrack; New asset type: Texture Generators
* &lbrack;Assets&rbrack; New materials included in the Starter Assets
* &lbrack;Assets&rbrack; New asset picker for image parameters in the Properties panel
* &lbrack;Assets&rbrack; Drag and drop Texture Generators from the Assets panel to the image pickers in the Properties panel
* &lbrack;Assets&rbrack; Drag and drop Texture Generators from the operating system file explorer
* &lbrack;Assets&rbrack; Filters can suggest fitting generators via a user tag on the image input
* &lbrack;Assets&rbrack; Texture Generators can define which filter should suggest them via a user tag
* &lbrack;Content&rbrack; New Perspective Crop filter
* &lbrack;Content&rbrack; New Stylization filter
* &lbrack;Content&rbrack; Blending mode on Fill Filter
* &lbrack;Content&rbrack; Updated Embroidery filter
* &lbrack;Content&rbrack; Updated Paint Wrap filter
* &lbrack;Content&rbrack; Updated all filters to support Texture Generators
* &lbrack;Layers&rbrack; Ability to chose a Texture Generator output channel when adding it to the layer stack
* &lbrack;Layers&rbrack; Ability to easily list and apply presets on Texture Generators
* &lbrack;Layers&rbrack; Display a Texture Generator preview in the image pickers
* &lbrack;Layers&rbrack; Texture Generator parameters can be exposed and exported
* &lbrack;Layers&rbrack; Assign the Base Color usage when importing a single image with the Texture Import Creation Template
* &lbrack;Layers&rbrack; Feedback when trying to drag and drop incompatible files in image pickers in the Properties panel
* &lbrack;Layers&rbrack; Generate an opacity channel from the alpha channel of an imported image
* &lbrack;Layers&rbrack; Image to Material (AI) is faster to compute when changing its category
* &lbrack;Layers&rbrack; Select the most relevant layer after a Creation Template is used
* &lbrack;Layers&rbrack; The position widgets can now be tweaked with a slider in the Advanced Parameters group
* &lbrack;Export&rbrack; Display a percentage in the queue instead of raw numbers
* &lbrack;Interoperability&rbrack; Opacity channel is now recognized as alpha channel when sending to Painter
* &lbrack;Application&rbrack; New dialog to display and save hardware information
* &lbrack;Application&rbrack; New preference to change the default height scale for every project
* &lbrack;Application&rbrack; Improve the way outdated assets are displayed
* &lbrack;Scripting&rbrack; New asset.documentResolution() and asset.setDocumentResolution() functions
* &lbrack;Scripting&rbrack; New select_asset() function
* &lbrack;Scripting&rbrack; Python API for Texture Generators
* &lbrack;Scripting&rbrack; get_project_assets() now returns 3D objects
* &lbrack;UI&rbrack; Asset thumbnail size can be changed in the Assets panel
* &lbrack;UI&rbrack; Updated viewport display icons

#### **Fixed:**

* &lbrack;2D View&rbrack; Zoom with mouse wheel is blocked at 244%
* &lbrack;Application&rbrack; Crash at start when initializing the graphics API
* &lbrack;Application&rbrack; Crash if the project name contains the # character
* &lbrack;Application&rbrack; Possible crash when opening an old project
* &lbrack;Application&rbrack; Re-opening the current project can lead to a crash
* &lbrack;Application&rbrack; Some project changes are not registered and are lost without warning when closing the project if not saved
* &lbrack;Export&rbrack; .sbs/.sbsar export issues when using multiple files with the same name
* &lbrack;Export&rbrack; Wrong color space for exported grayscale images .sbs/.sbsar file
* &lbrack;Filters&rbrack; Opacity blend behavior issues
* &lbrack;Layers&rbrack; .svg files sometimes are not rendered at the correct resolution
* &lbrack;Performance&rbrack; Some project saves on disk are unnecessary
* &lbrack;Project&rbrack; Importing an old project does not load associated presets
* &lbrack;Scripting&rbrack; Unable to get parameters of the first inserted layer
* &lbrack;UI&rbrack; The preview popup when hovering an asset can appear in the wrong location or screen
* &lbrack;UI&rbrack; Undocked panels are visible and usable on top of the Welcome screen

### **4.2.2 DORAYAKI**

*(Released: 5 December 2023)*

#### **Added:**

* &lbrack;3D Capture&rbrack; 3D Capture is now 5% to 10% faster on Windows
* &lbrack;3D Capture&rbrack; Improve mesh cleanup before decimation
* &lbrack;Engine&rbrack; Update Substance Engine to version 9.0.3
* &lbrack;Layers&rbrack; Content-Aware Fill: upstream update, various use case fixes and Linux support

#### **Fixed:**

* &lbrack;3D Capture&rbrack; Clicking "Back" after alignment then "Next" does not update the point cloud
* &lbrack;3D Capture&rbrack; Mesh displayed with holes after being added to project
* &lbrack;Application&rbrack; Crash when exiting fullscreen mode after a 3D capture
* &lbrack;Application&rbrack; Crash with crafted image files
* &lbrack;Application&rbrack; If in "All libraries" when quitting Sampler, the Assets panel becomes empty at restart
* &lbrack;Application&rbrack; Memory leak when exporting material
* &lbrack;Application&rbrack; Opening a project save with previous Sampler versions can lead to a crash
* &lbrack;Application&rbrack; Potential crashes when failing to convert 3D meshes
* &lbrack;Application&rbrack; Silent crash when opening a .sbsar while Sampler is running
* &lbrack;Export&rbrack; Crash when exporting a .sbs/.sbsar file with a custom usage
* &lbrack;Export&rbrack; Exported normal maps are always DirectX regardless of the user setting
* &lbrack;Export&rbrack; Exporting a 3D Object to a FBX file on macos does not work
* &lbrack;Export&rbrack; Inconsistencies when exporting a Layer Stack with an Embroidery filter as a .sbs/.sbsar file
* &lbrack;Export&rbrack; Sometimes exporting .sbs/.sbsar files does not work
* &lbrack;Export&rbrack; Sometimes when exporting an .sbs/.sbsar file images don't have the right bit depth
* &lbrack;Layers&rbrack;  Making a Splatter layer invisible renders its first child instead
* &lbrack;Layers&rbrack; Crash when loading mask in Brigtness/Contrast layer
* &lbrack;Layers&rbrack; Misleading error messages are displayed after deleting layer
* &lbrack;Layers&rbrack; Possible crash when downgrading an asset
* &lbrack;Layers&rbrack; Some outputs are not connected to inputs unless the usage is forced in the Channel Settings panel
* &lbrack;Physical Size&rbrack; Reference layer dropdown can be reset by mistake
* &lbrack;UI&rbrack; Import template info icons needs update
* &lbrack;UI&rbrack; Viewport shortcut tip appears everytime the viewport layout changes

### **4.2.1 DORAYAKI**

*(Released: 21 September 2023)*

#### **Added :**

* &lbrack;Content&rbrack; Image to Material - Improve microdetails generation in normal maps
* &lbrack;Content&rbrack; Image to Material - New delighting intensity parameter
* &lbrack;Layers&rbrack; Images can be added in the Image Import layers
* &lbrack;Layers&rbrack; Images can be removed in the Image Import layers
* &lbrack;Layers&rbrack; Invalid layers can now be deleted
* &lbrack;2D View&rbrack; Shift+C shortcut to cycle back the channels
* &lbrack;3D Capture&rbrack; Display a warning toast when user import less than 20 images
* &lbrack;Application&rbrack; New preferences to set the default material texture tiling value
* &lbrack;Onboarding&rbrack; Updated tutorial UI for Image to Material (AI) and Upscale
* &lbrack;Scripting&rbrack; 3D Capture API: DatasetInfo has more data when Capture3dState is set to aligned
* &lbrack;Scripting&rbrack; New select_asset argument to create_asset(). New functions: wait_for_computation() and clear_render_cache()

#### **Fixed :**

* &lbrack;Layers&rbrack; Crash when Crop region is very small
* &lbrack;Layers&rbrack; Crash when adding or tweaking the Crop filter
* &lbrack;Layers&rbrack; Making crop region square leads to incorrect material output resolution
* &lbrack;Layers&rbrack; Outputs sometimes disappear when several layers are disabled
* &lbrack;Layers&rbrack; Render cache may not properly be invalidated with the Image to Material (AI) and Upscale filters
* &lbrack;Layers&rbrack; Unable to add Upscale filter when selecting "Do not show this message again" in the warning popup
* &lbrack;Layers&rbrack; Unable to restore the image in Embroidery filter once modified
* &lbrack;Export&rbrack; Exported normal map resolution changes when changing normal format
* &lbrack;Export&rbrack; Remove "\_environment" file name suffix when exporting an environment
* &lbrack;Export&rbrack; Unable to export an .sbsar file when there is a Warp Transform layer in the layer stack
* &lbrack;2D View&rbrack; "Fit to screen" does not work when resolution changes
* &lbrack;Application&rbrack; After closing the application window while computing, the application process could still be running
* &lbrack;Application&rbrack; Crash at exit
* &lbrack;Application&rbrack; Invalidate render cache when toggling GPU accelerated neural networks
* &lbrack;Scripting&rbrack; Naming a plugin as an existing panel name causes unexpected behaviors
* &lbrack;UI&rbrack; Clicking on a item with a tooltip will cause the tooltip to disappear until restart
* &lbrack;UI&rbrack; Height scale value may change when switching assets
* &lbrack;UI&rbrack; Incorrect margin in comboboxes

### **4.2 DORAYAKI**

*(Released: 05 September 2023)*

#### **Added:**

* &lbrack;Content&rbrack; Vastly improved Image to Material (AI) and Delighter filters
* &lbrack;Content&rbrack; New Upscale filter
* &lbrack;Content&rbrack; The Crop filter now has dynamic output resolution.
* &lbrack;Material Creation Template&rbrack; Add Document size setting.
* &lbrack;Material Creation Template&rbrack; New "Add a crop" toggle button.
* &lbrack;Material Creation Template&rbrack; New "Upscale Material" toggle
* &lbrack;Material Creation Template&rbrack; Display imported image size
* &lbrack;Material Creation Template&rbrack; Give feedback when some imported images cannot be used
* &lbrack;Material Creation Template&rbrack; Warn when image sizes are inconsistent
* &lbrack;Material Creation Template&rbrack; New warnings and tooltips
* &lbrack;Layers&rbrack; Display the resolution of the layers in the layer stack
* &lbrack;Layers&rbrack; Layer compute resolution can now be either set to Document size or Input size
* &lbrack;Layers&rbrack; Show layers resolution in the layer stack
* &lbrack;Layers&rbrack; Switch a layer resolution policy to Document or Layer Input when applicable
* &lbrack;Layers&rbrack; Warn the user when an Upscale filter is added manually and provide some documentation
* &lbrack;Layers&rbrack; Warn the user when doing a linear upscale, and offer to use the Upscale filter instead
* &lbrack;Layers&rbrack; Computing an Image to Material (AI) layer can now be cancelled quicker, to improve rendering times when tweaking the layer stack
* &lbrack;Layers&rbrack; Computing an Upscale layer can now be cancelled quicker, to improve rendering times when tweaking the layer stack
* &lbrack;Export&rbrack; Allow overriding resolution of exported textures
* &lbrack;Export&rbrack; Channels to export list is now sorted
* &lbrack;Export&rbrack; Display channel resolution in the channels to export list
* &lbrack;Application&rbrack; New preference to enable or disable GPU accelerated neural networks
* &lbrack;UI&rbrack; Improved resolution dropdowns
* &lbrack;UI&rbrack; New icons for Mesh Transform, Mesh Post Process and Weave filters
* &lbrack;UI&rbrack; Rename "Share" panel to "Export"
* &lbrack;Scripting&rbrack; Add layer output resolution support to the export API
* &lbrack;Scripting&rbrack; Added Crop, Upscale and Document size to the image import API
* &lbrack;Onboarding&rbrack; New tutorials
* &lbrack;Onboarding&rbrack; Update Welcome and What's New screens content
* &lbrack;Engine&rbrack; Update Substance Engine to version 9.0.1

#### **Fixed:**

* &lbrack;3D Capture&rbrack; Improve Precision options naming in Alignment settings parameters
* &lbrack;Application&rbrack; Importing images with non-multiple of 16 dimensions can lead to a crash
* &lbrack;Application&rbrack; Crash when duplicating an asset in the Project panel
* &lbrack;Application&rbrack; Crash when switching assets in the Project panel
* &lbrack;Content&rbrack; Painting a custom mask for the Snow filter does not work properly
* &lbrack;Exposed Parameters&rbrack; Exposed parameters changes can be lost when switching materials
* &lbrack;Interoperability&rbrack; Sending a Material from the Export panel can lead to a crash
* &lbrack;Layers&rbrack; Content-Aware Fill stops computing when switching from a single image input to a material input
* &lbrack;Layers&rbrack; Crash after duplicating an Environment Light that contains a material
* &lbrack;Layers&rbrack; Image import layer displays wrong image name in the Properties panel if the image file was renamed
* &lbrack;Layers&rbrack; Sometimes a spinner is displayed on an inactive layer
* &lbrack;Layers&rbrack; Sometimes changing the output usage of an image in an Image import layer does not work
* &lbrack;Layers&rbrack; Typos in the Creation Template Window
* &lbrack;UI&rbrack; 3D viewport onboarding tooltip has focus issues
* &lbrack;UI&rbrack; Image name can overflow if file name is too long
* &lbrack;UI&rbrack; Minor brush toolbar layout issues when using the eraser
* &lbrack;UI&rbrack; Strings are truncated in some languages in the Viewer Settings panel
* &lbrack;UI&rbrack; While the viewport tooltip popup is displayed, pressing "space" creates a new project

### **4.1.2 CANNOLI**

*(Released: June 20, 2023)*

#### **Fixed:**

* &lbrack;Layers&rbrack; Memory leak when tweaking Substance materials and filters causing crashes

### **4.1.1 CANNOLI**

*(Released: June 06, 2023)*

#### **Added**:

* &lbrack;Engine&rbrack; Update Substance Engine to version 9.0
* &lbrack;Interoperability&rbrack; Send 3D Objects to Stager and Painter

#### **Fixed:**

* &lbrack;3D Capture&rbrack; Applications crashes when 3D Capture renderer fails
* &lbrack;3D Capture&rbrack; Crash when an image cannot be loaded
* &lbrack;3D Capture&rbrack; Crash when reaching the Mesh Reconstruction step
* &lbrack;3D Capture&rbrack; Crash when resizing the bounding box
* &lbrack;3D Capture&rbrack; Importing masks following the convention doesn't assign the mask properly
* &lbrack;3D Capture&rbrack; Rendering glitches when adjusting the bounding box
* &lbrack;3D Capture&rbrack; Switching between version and toggling rendering options during 3D capture post process is slow
* &lbrack;3D Capture&rbrack; Switching between versions during 3D Capture Post-Process step is sometimes broken
* &lbrack;Application&rbrack; Crash at startup
* &lbrack;Application&rbrack; Crash when duplicating a renamed material
* &lbrack;Application&rbrack; Crash when opening a legacy .alch project without its dependency folder
* &lbrack;Application&rbrack; Crash when plugging/unplugging a screen, computer goes to sleep, or is accessed remotely
* &lbrack;Application&rbrack; Crashes and memory leaks related to non-persistent assets management
* &lbrack;Export&rbrack; Choosing material format for 3D object file types that embed or reference textures should be disabled
* &lbrack;Export&rbrack; Crash if something goes wrong during 3D Object export
* &lbrack;Export&rbrack; Crash when exporting a .sbs/.sbsar file
* &lbrack;Export&rbrack; Crash when importing custom preset that has the same Label but not the same file name
* &lbrack;Export&rbrack; Exporting an environment light to a .sbs/.sbsar file sometimes does not work
* &lbrack;Export&rbrack; Gltf/Glb export encodes textures in base64
* &lbrack;Export&rbrack; Name text field does not work when refocusing
* &lbrack;Export&rbrack; Preserve tiling does not work when exporting an Image to Material (AI Powered) layer to a .sbs/.sbsar file
* &lbrack;Export&rbrack; When exporting gltf and replacing files, the list of files to be replaced is not correct
* &lbrack;Exposed Parameters&rbrack; Random seed does not work in exported .sbs/.sbsar files
* &lbrack;Layers&rbrack; Content-Aware Fill sometimes crashes when added for the second time
* &lbrack;Layers&rbrack; Crash when computing a layer stack
* &lbrack;Layers&rbrack; Image to Material (AI) disk cache does not work
* &lbrack;Layers&rbrack; Possible crash when tweaking a layer
* &lbrack;Performance&rbrack; Memory leaks
* &lbrack;Project&rbrack; Crash when saving a project
* &lbrack;Project&rbrack; Importing the same project twice in a row duplicates assets
* &lbrack;UI&rbrack; Rounded buttons with only an icon are not rendered correctly

### 4.1.0 Cannoli

*(Released: March 28, 2023)*

#### **Added:**

* &lbrack;Content&rbrack; New Embroidery filter
* &lbrack;Content&rbrack; New Paint Warp filter
* &lbrack;UI&rbrack; Add Export option in File menu
* &lbrack;3D Capture&rbrack; Back button is now available on the alignment step
* &lbrack;3D Capture&rbrack; Images Handle JPEG EXIF orientation
* &lbrack;3D Capture&rbrack; Scripting - New dataset_info.camera property
* &lbrack;3D Capture&rbrack; Add Linux support (see documentation)
* &lbrack;3D Capture&rbrack; Verify read access of the imported images
* &lbrack;Onboarding&rbrack; Learn - 2 new tutorials (Embroidery and Paint Warp)
* &lbrack;Onboarding&rbrack; Updated What's New content

#### **Fixed:**

* &lbrack;3D Capture&rbrack; Keep camera position when changing version
* &lbrack;3D Capture&rbrack; Merge all groups of an object into one
* &lbrack;3D Capture&rbrack; Renamed generated meshes into Original
* &lbrack;Application&rbrack; Crash when trying to generate thumbnail of a non-existent image
* &lbrack;Assets&rbrack; Trash bin icon does nothing in the Assets panel
* &lbrack;Content&rbrack; Updating filters with material slots doesn't work as expected
* &lbrack;Export&rbrack; Possible crash when exporting an asset with specific filters
* &lbrack;Export&rbrack; SBS/SBSAR Export - image import layers had priority over image parameters
* &lbrack;Export&rbrack; UE4 Export preset doesn't work with PNG
* &lbrack;Layers&rbrack; Crash when dropping a material and a filter at the same time from OS explorer
* &lbrack;Layers&rbrack; Crash when dragging any SBSAR file with any image file
* &lbrack;Layers&rbrack; Embroidery opacity channel can be completely white
* &lbrack;Localization&rbrack; Chinese language may be displayed by default on Linux
* &lbrack;Performance&rbrack; Fixed a memory issue when removing a layer from an asset
* &lbrack;Project&rbrack; Possible crash when saving
* &lbrack;UI&rbrack; Add missing spacing on Version's menu button
* &lbrack;UI&rbrack; Cancel button not properly displayed
* &lbrack;UI&rbrack; Disable sliders animation for 3D Capture post-process parameters
* &lbrack;UI&rbrack; The Material Creation Template window does not close itself when clicking outside
* &lbrack;UI&rbrack; The filter quick accessor closes itself when clicking outside

**Known Issues:**

* &lbrack;Color Picker&rbrack; Picking a color on a second monitor with a different resolution may not work
* &lbrack;Content&rbrack; Shape light widget is not working in spherical projection mode
* &lbrack;Interoperability&rbrack; Material with displacement sent to Stager will lose displacement controls

### 4.0.2 Banana

*(Released: March 09, 2023)*

#### **Added:**

* &lbrack;3D Capture&rbrack; Disk usage shows the amount used
* &lbrack;3D Capture&rbrack; Importing photos is asynchronous and faster
* &lbrack;Scripting&rbrack; New classes and functions to script the 3D Capture feature
* &lbrack;Scripting&rbrack; New ExportController class to perform actions when the export is finished, failed or canceled
* &lbrack;Scripting&rbrack; Pass arguments python scripts run with --run-script
* &lbrack;UI&rbrack; UI feedback when dragging an asset over the Layers panel
* &lbrack;Content&rbrack; Color temperature filter is now working on materials
* &lbrack;Content&rbrack; Normal to Height filters has a new option to preserve tiling

#### **Fixed:**

* &lbrack;3D Capture&rbrack; Corrected image size in dataset alignment step
* &lbrack;3D Capture&rbrack; Remove duplicate vertices after UV unwrapping
* &lbrack;3D Capture&rbrack; MacOS - Better detection if 3D Capture is available
* &lbrack;3D Capture&rbrack; Crash when closing the 3D capture window while importing images
* &lbrack;3D Capture&rbrack; Crash when generating a new version
* &lbrack;3D Capture&rbrack; Crash when trying to load the 3D object in the viewer
* &lbrack;3D Capture&rbrack; Crash when using path with non UTF8 characters
* &lbrack;3D Capture&rbrack; Hits & Tips typo
* &lbrack;3D Capture&rbrack; Meshes are no longer scaled to fit into unit cube
* &lbrack;3D Capture&rbrack; Prevent a crash when closing 3D capture while rendering
* &lbrack;3D Capture&rbrack; Removing a mask makes the image disappear
* &lbrack;Application&rbrack; Crash when importing twice an asset simultaneously
* &lbrack;Application&rbrack; Backup previous version of assets when opening a project if they were never back-up
* &lbrack;Application&rbrack; Correctly cache baked maps when not all maps are baked
* &lbrack;Application&rbrack; Fullscreen crashes when a 3D object is displayed.
* &lbrack;Application&rbrack; Last material is duplicated when saving the project
* &lbrack;Application&rbrack; Prevent crash when cancelling the Mesh Post processing compute during the baking step
* &lbrack;Application&rbrack; Reopening current project does not discard changes
* &lbrack;Application&rbrack; Stop generating thumbnails for 3D objects
* &lbrack;2D View&rbrack; Crash when use the brush tool
* &lbrack;Content&rbrack; Content Aware Fill - computation may stuck
* &lbrack;Content&rbrack; Atlas Creator filter is downscaling the Opacity channel
* &lbrack;Export&rbrack; Fix clear Failed exports queue
* &lbrack;Export&rbrack; OBJ export creates object 100 times smaller than expected
* &lbrack;Layers&rbrack; Color images imported as grayscale channels are now considered grayscale
* &lbrack;Export&rbrack; FBX files cannot be imported in third party applications
* &lbrack;Export&rbrack; Shader output names in USD files are not correct
* &lbrack;Layers&rbrack; Image name is not updated when changing its name on the OS explorer
* &lbrack;Scripting&rbrack; Display an error message when reloading an invalid script
* &lbrack;UI&rbrack; Base material button disabled when not available
* &lbrack;UI&rbrack; Crash when accessing the file dialog on the Material Creation Template Window
* &lbrack;UI&rbrack; Quick accessor is accessible even when the Layers panel is closed
* &lbrack;UI&rbrack; Send to icons are misaligned
* &lbrack;UI&rbrack; The layer icon changes when clicking on the Blend icon

#### **Known Issues:**

* &lbrack;Color Picker&rbrack; Picking a color on a second monitor with a different resolution may not work
* &lbrack;Content&rbrack; Shape light widget is not working in spherical projection mode
* &lbrack;Interoperability&rbrack; Material with displacement sent to Stager will lose displacement controls

### 4.0.1 Banana

*(Released: February 07, 2023)*

#### **Fixed:**

* &lbrack;3D Capture&rbrack; When using masks, the texture projection may be broken
* &lbrack;3D Capture&rbrack; Artefacts may appear on your object
* &lbrack;3D Capture&rbrack; The exported mesh may be really small

#### **Known Issues:**

* &lbrack;3D Capture&rbrack; FBX and OBJ exports downscale the result
* &lbrack;3D Capture&rbrack; 3D Capture is available on MacOS even if your hardware is not compatible. Check the documentation.
* &lbrack;3D Capture&rbrack; Crash when the mesh reconstruction is done.
* &lbrack;Layers&rbrack; Content-Aware Fill can be stuck if you tweak layers below
* &lbrack;Color Picker&rbrack; Picking a color on a second monitor with a different resolution may not work
* &lbrack;Content&rbrack; Shape light widget is not working in spherical projection mode
* &lbrack;Interoperability&rbrack; Material with displacement sent to Stager will lose displacement controls

### 4.0.0 Banana

*(Released: January 31, 2023)*

#### **Added:**

* &lbrack;3D Capture&rbrack; Create 3D objects from images
* &lbrack;3D Capture&rbrack; Dedicated 3D Capture wizard
* &lbrack;3D Capture&rbrack; Import or generate black and white masks on your dataset
* &lbrack;3D Capture&rbrack; Alignment result - view all matched features as a point cloud
* &lbrack;3D Capture&rbrack; Alignment result - view and interact with cameras associated with each aligned photo
* &lbrack;3D Capture&rbrack; Define the reconstruction area with a bounding box widget
* &lbrack;3D Capture&rbrack; Scale, translate, and rotate on all axes the bounding box widget
* &lbrack;3D Capture&rbrack; Define the geometry precision for the reconstructed mesh
* &lbrack;3D Capture&rbrack; Optimize your mesh and textures by creating a new version
* &lbrack;3D Capture&rbrack; Each of the versions is automatically decimated to the target faces number set
* &lbrack;3D Capture&rbrack; The post-process step automatically unwraps, re-projects textures, and then bakes the normal height and AO information from the high-poly mesh
* &lbrack;3D Capture&rbrack; Add the original result or a version to the Sampler project
* &lbrack;3D Capture&rbrack; New Mesh Post-Process layer to automatically decimate, unwrap, reproject textures, and bake details of the underlying mesh layer
* &lbrack;3D Capture&rbrack; New Mesh Transform layer to scale, rotate, or translate the underlying mesh layer
* &lbrack;Export&rbrack; New Export window
* &lbrack;Export&rbrack; Dedicated settings and UI depending on the asset type (material, environment light, mesh)
* &lbrack;Export&rbrack; Export the mesh as USD, USDA, USDZ, glTF, glb, obj, fbx, stl
* &lbrack;Export&rbrack; Define the material type when exporting Substance files (SBSAR, SBS)
* &lbrack;UI&rbrack; Move cache settings to a new tab in the Preferences popup
* &lbrack;Application&rbrack; 2D and 3D viewports can now be resized, swapped, and stacked vertically
* &lbrack;Application&rbrack; New SAMPLER_RESOURCES_PATH environment variable to add extra starter assets
* &lbrack;Scripting&rbrack; Added SAMPLER_PLUGIN_PATH and SAMPLER_SCRIPT_PATH environment variables to import plugins and scripts at startup
* &lbrack;Scripting&rbrack; Added export functions for materials, environment lights, and 3d objects
* &lbrack;Scripting&rbrack; Added identifier, default value, min and max values, labels, and enum values to parameters
* &lbrack;Scripting&rbrack; Added import_textures function to enter a customized usage while importing images

#### **Fixed:**

* &lbrack;Application&rbrack; Crash when opening a recent project and saving in confirmation dialog
* &lbrack;Application&rbrack; File dialog prevents opening .ssa files
* &lbrack;Application&rbrack; File dialogs can appear on a background window on macOS
* &lbrack;Application&rbrack; Potential crash when opening 3.2 projects
* &lbrack;Application&rbrack; Selecting a file closes the File dialog before displaying warnings
* &lbrack;Exposed Parameters&rbrack; Exporting parametric environment lights does not work
* &lbrack;Layers&rbrack; "Click here to browse" link in layer stack doesn't work anymore
* &lbrack;Layers&rbrack; Painting several images within the same layer sometimes does not work
* &lbrack;Layers&rbrack; Setting an image in the layer properties does not update the image picker thumbnail
* &lbrack;Layers&rbrack; Tweaking a Sampler asset added as a layer does not work
* &lbrack;Project&rbrack; Unwanted asset update when opening a project
* &lbrack;Scripting&rbrack; Browse to plugin folder sometimes fails on Windows
* &lbrack;Scripting&rbrack; Crash when using 'open_project()' in a Python script
* &lbrack;Scripting&rbrack; JPEG export is missing from the API
* &lbrack;Scripting&rbrack; The log panel is not read-only
* &lbrack;Scripting&rbrack; image_picker parameter value does not work
* &lbrack;UI&rbrack; Missing asset icon for environment lights in the Project panel
* &lbrack;UI&rbrack; Send to Designer Format Dropdown in the Preferences popup can be empty
* &lbrack;UI&rbrack; Some buttons have an incorrect style
* &lbrack;UI&rbrack; The label overlaps the buttons in Button Group widgets
* &lbrack;UI&rbrack; Tooltip position is wrong for "Tools" in Set the physical size menu
* &lbrack;UI&rbrack; When changing language, File menu is misaligned

#### **Known Issues:**

* &lbrack;3D Capture&rbrack; When using masks, the texture projection may be broken
* &lbrack;3D Capture&rbrack; Small artefacts may appear on your object if your scale in the Mesh transform is too small
* &lbrack;3D Capture&rbrack; The exported mesh may be really small. Reset the scale of the Mesh transform and re-export
* &lbrack;Color Picker&rbrack; Picking a color on a second monitor with a different resolution may not work
* &lbrack;Content&rbrack; Shape light widget is not working in spherical projection mode
* &lbrack;Interoperability&rbrack; Material with displacement sent to Stager will lose displacement controls

## Version 3

### 3.4.1 Arancini

*(Released: October 06, 2022)*

**Added:**

* &lbrack;Onboarding&rbrack; New Welcome and What's New screens
* &lbrack;Onboarding&rbrack; Updated Home screen UI
* &lbrack;Onboarding&rbrack; New Learn content in the Home screen
* &lbrack;Scripting&rbrack; Log an error in the Log panel when a method is not recognized
* &lbrack;Scripting&rbrack; New ssa.helpers module to enable printing to the Log panel
* &lbrack;Application&rbrack; Support for the new side-by-side buttons widget from Substance 3D Designer

**Fixed:**

* &lbrack;Export&rbrack; Crash when exporting a .sbsar file referencing a missing image
* &lbrack;Export&rbrack; Crash when exporting an asset referencing a corrupted image file
* &lbrack;Export&rbrack; Exporting a .sbsar file with an Embroidery layer results in a gray material
* &lbrack;Export&rbrack; Exporting a material to a .sbs/sbsar file can generate a fully transparent material
* &lbrack;Export&rbrack; Normal Format parameter is not exposed correctly in .sbs/.sbsar files
* &lbrack;Export&rbrack; Sbs/sbsar export of a layer stack referencing a .svg file is broken
* &lbrack;Export&rbrack; Transform layer is not exported properly / Updated Enscape - Revit export preset
* &lbrack;Exposed Parameters&rbrack; Crash when deleting a layer containing an exposed parameter
* &lbrack;Exposed Parameters&rbrack; Updating an outdated layer in the layer stack can lead to a corrupted list of exposed parameters
* &lbrack;Exposed Parameters&rbrack; Parameters that should not be exported are exported anyway
* &lbrack;Exposed Parameters&rbrack; Removing a blend filter when deleting a layer does not unexpose its parameters
* &lbrack;Exposed Parameters&rbrack; Text parameters break .sbs/.sbsar exports
* &lbrack;Layers&rbrack; Crash when dropping a layer stack in another layer stack
* &lbrack;Layers&rbrack; Crash when failing to load a filter
* &lbrack;Layers&rbrack; Cannot reload the previous image when resetting the Image field
* &lbrack;Layers&rbrack; Cannot undo/redo transform tool changes
* &lbrack;Layers&rbrack; Clone Stamp layer is stuck after clicking "Reset all settings"
* &lbrack;Layers&rbrack; Using any of the reset buttons prevents from drawing in the Image field
* &lbrack;Layers&rbrack; The Reset button does not clear the drawing mask in the Image field
* &lbrack;Layers&rbrack; The Reset button in the Image field does nothing if the user has painted something
* &lbrack;Layers&rbrack; Rendering cache does not work when using the Brush tool
* &lbrack;Layers&rbrack; Deleted layer can still show up in the Properties panel
* &lbrack;Layers&rbrack; Layer computation can stall when switching between project assets
* &lbrack;Project&rbrack; Sometimes Sampler is unable to open a project from disk
* &lbrack;2D View&rbrack; The 2D view always defaults back to Material Output

**Known Issues:**

* &lbrack;Color Picker&rbrack; Picking a color on a second monitor with a different resolution may not work
* &lbrack;Content&rbrack; Shape light widget is not working in spherical projection mode
* &lbrack;Interoperability&rbrack; Material with displacement sent to Stager will lose displacement controls

### 3.4.0 Arancini

*(Released: September 06, 2022)*

**Added:**

* &lbrack;Exposed Parameters&rbrack; New Exposed Parameters panel
* &lbrack;Exposed Parameters&rbrack; New button on parameters hover to expose and unexpose parameters from Properties panel
* &lbrack;Exposed Parameters&rbrack; New right-click context menu on parameters to expose and unexpose parameters from Properties panel
* &lbrack;Exposed Parameters&rbrack; Exposed parameters are listed in the Exposed Parameters panel
* &lbrack;Exposed Parameters&rbrack; Color dots and color discs are added in several places to easily identify exposed parameters
* &lbrack;Exposed Parameters&rbrack; Parameter labels can be edited in the Exposed Parameters panel
* &lbrack;Exposed Parameters&rbrack; Display a warning for non-exportable parameters
* &lbrack;Exposed Parameters&rbrack; Display warning if moving a layer with exposed blend parameters somewhere where they become hidden
* &lbrack;Exposed Parameters&rbrack; Exposed parameters are exported in SBS and SBSAR formats
* &lbrack;Metadata&rbrack; Support Custom Metadata templates
* &lbrack;Metadata&rbrack; New CLO Physical properties metadata template
* &lbrack;Metadata&rbrack; Add icons on hover to add/remove custom metadata
* &lbrack;Python API&rbrack; New Python API
* &lbrack;Python API&rbrack; API for Asset authoring
* &lbrack;Python API&rbrack; API for Layers management
* &lbrack;Python API&rbrack; API for Parameters management
* &lbrack;Python API&rbrack; API for Project management
* &lbrack;Python API&rbrack; A plugin can be enabled and disabled
* &lbrack;Python API&rbrack; Python API documentation accessible in the Help menu
* &lbrack;Scripting&rbrack; New Plugins and Scripts section in the Preferences popup
* &lbrack;Scripting&rbrack; Create and import plugins to customize Sampler interface with your own panels
* &lbrack;Scripting&rbrack; Plugins become part of the Sampler interface and can be docked and moved around like standard Sampler panels
* &lbrack;Scripting&rbrack; Dedicated button bar for the plugins on the Sampler right toolbar
* &lbrack;Scripting&rbrack; Create and import scripts to perform a list of given tasks
* &lbrack;Scripting&rbrack; Launch Python scripts via Scripts menu
* &lbrack;Scripting&rbrack; Plugins and Scripts can be deleted, re-ordered, and reloaded from the Preferences window
* &lbrack;Scripting&rbrack; Added --run-script command line parameters
* &lbrack;Logs&rbrack; New Logs panel
* &lbrack;Logs&rbrack; Enable Logs panel from the Preferences window
* &lbrack;Logs&rbrack; New action bar to clear, copy/paste, export logs
* &lbrack;Properties&rbrack; New button on parameters hover to reset parameter value
* &lbrack;Properties&rbrack; New right-click context menu on parameters to reset parameter value
* &lbrack;Content&rbrack; Image to Material (AI Powered) now works on MacOS
* &lbrack;Engine&rbrack; Update Substance engine to v8.6.0

**Fixed:**

* &lbrack;Application&rbrack; Application could crash at exit when a thumbnail generation was in progress
* &lbrack;Application&rbrack; Application might crash when using 'Save as' at exit
* &lbrack;Application&rbrack; Application might hang during shutdown on MacOS
* &lbrack;Application&rbrack; Saving with the color dialog open doesn't save its changes
* &lbrack;Export&rbrack; Usage naming convention is not correct when exporting
* &lbrack;Layers&rbrack; Dropping a material on top of a filter could crash
* &lbrack;Layers&rbrack; Updating an outdated layer stack could update unrelated layer stacks
* &lbrack;Metadata&rbrack; Empty fields are exported
* &lbrack;Metadata&rbrack; When there is only one metadata item, the UI lets you try to reorder it
* &lbrack;Project&rbrack; Compute never ends after duplicating a material
* &lbrack;Project&rbrack; Project asset is duplicated after initial project save
* &lbrack;Project&rbrack; Unnecessary computations when switching asset
* &lbrack;Rendering&rbrack; Some layer stacks do not render properly after deleting a layer
* &lbrack;Security&rbrack; Fix CVE-2015-20107
* &lbrack;UI&rbrack; 2D Outputs can be blurry depending on the window size
* &lbrack;UI&rbrack; Asset preview can stay opened on top when application loses focus
* &lbrack;UI&rbrack; Splash screen rounded corners have a square opaque background

**Known Issues:**

* &lbrack;Color Picker&rbrack; Picking a color on a second monitor with a different resolution may not work
* &lbrack;Content&rbrack; Shape light widget is not working in spherical projection mode
* &lbrack;Interoperability&rbrack; Material with displacement sent to Stager will lose displacement controls

### 3.3.2 Zucchini

*(Released: June 28, 2022)*

**Fixed:**

* &lbrack;Application&rbrack; Fix potential crash when opening a project
* &lbrack;Export&rbrack; Restarting Sampler breaks imported custom export presets list
* &lbrack;Interoperability&rbrack; Fix crash when a material sent from Designer is deleted and then re-sent from Designer
* &lbrack;Project&rbrack; Impossible to delete the last material or environment light if it's the last asset in the project
* &lbrack;Project&rbrack; Right-click on an environment light makes the "unsaved modifications" asterisk appear

**Known Issues:**

* &lbrack;Color Picker&rbrack; Picking a color on a second monitor with a different resolution may not work
* &lbrack;Content&rbrack; Shape light widget is not working in spherical projection mode
* &lbrack;Interoperability&rbrack; Material with displacement sent to Stager will lose displacement controls

### 3.3.1 Zucchini

*(Released: June 07, 2022)*

**Added:**

* &lbrack;Application&rbrack; Native Apple silicon (M1) support
* &lbrack;UI&rbrack; New shortcut, "C" key, to cycle through channels in the 2D view
* &lbrack;Tools&rbrack; Numerical field to edit grayscale color value in Brush Toolbar

**Fixed:**

* &lbrack;Tools&rbrack; Using the Brush tool on Windows with a fractional UI scale (150%) offsets the strokes
* &lbrack;Performance&rbrack; Improve memory consumption
* &lbrack;Physical Size&rbrack; Physical size information can be missing when enabling the feature
* &lbrack;UI&rbrack; Mouse scrolling sometimes does not work as expected when pressing the Alt key
* &lbrack;Application&rbrack; Application may crash when opening a saved project
* &lbrack;Application&rbrack; Crash when drag and dropping several images and using Texture Import in the Material Creation Template window
* &lbrack;Application&rbrack; Potential crash when saving a project containing a custom filter
* &lbrack;Application&rbrack; Sometimes the Control key state is lost when switching application
* &lbrack;Assets&rbrack; Crash when renaming a local folder

**Known Issues:**

* &lbrack;Color Picker&rbrack; Picking a color on a second monitor with a different resolution may not work
* &lbrack;Content&rbrack; Shape light widget is not working in spherical projection mode
* &lbrack;Interoperability&rbrack; Material with displacement sent to Stager will lose displacement controls

### 3.3.0 Zucchini

*(Released: May 17, 2022)*

**Added:**

* &lbrack;Content&rbrack; New Content-Aware Fill filter (Windows and Mac)
* &lbrack;Content&rbrack; Content-Aware Fill is working on images, PBR materials, and environment lights
* &lbrack;Content&rbrack; Add "Preserve Tiling" parameter to Image to Material (AI Powered)
* &lbrack;Content&rbrack; The Perspective Transform filter can display a grid between its four points
* &lbrack;Interoperability&rbrack; Send materials to Adobe Substance 3D Stager
* &lbrack;Tools&rbrack; Center the transformation by pressing Ctrl when resizing Transform or Crop tool
* &lbrack;Tools&rbrack; Lock the ratio to square by pressing Shift when resizing Transform or Crop tool
* &lbrack;Tools&rbrack; Clone stamp cursor offers a preview of what will be stamped
* &lbrack;Tools&rbrack; Preview original content in the the Eraser cursor when using Clone stamp
* &lbrack;Tools&rbrack; Ctrl+Click creates a new stamp in the Clone Stamp layer
* &lbrack;Tools&rbrack; Successive clone stamps are now grouped within a single layer
* &lbrack;Tools&rbrack; Brush Toolbar UI Revamp
* &lbrack;Tools&rbrack; The Brush Toolbar position is persistent during a session
* &lbrack;Tools&rbrack; New brush tiling options by axis
* &lbrack;Tools&rbrack; Hide/display the overlay over the 2D view when painting
* &lbrack;Tools&rbrack; New shortcut, "X" key, to toggle between Brush and Eraser
* &lbrack;Tools&rbrack; New shortcut, "&lbrack;" "&rbrack;" to change the Brush size
* &lbrack;Tools&rbrack; New shortcut, "E" key, to toggle the Eraser
* &lbrack;2D View&rbrack; New Spherical Projection mode when creating environment light
* &lbrack;2D View&rbrack; Brush tool is supported with the spherical projection mode
* &lbrack;2D View&rbrack; Position tool is supported with the spherical projection mode
* &lbrack;2D View&rbrack; Undo/redo is supported with the spherical projection mode
* &lbrack;2D View&rbrack; In Spherical Projection, set the default position to look at the center of the environment
* &lbrack;2D View&rbrack; New exposure control
* &lbrack;UI&rbrack; In the Properties panel, the Image tweak displays the source of the content (Image or from a layer)
* &lbrack;UI&rbrack; Improved the layer/material outputs dropdown background
* &lbrack;UI&rbrack; New position of the resolution information in the 2D View
* &lbrack;UI&rbrack; New tooltip with 3D view navigation controls shortcuts
* &lbrack;UI&rbrack; New tooltip with brush controls
* &lbrack;UI&rbrack; New tooltip with projection navigation controls shortcuts
* &lbrack;Compound Filters&rbrack; Compound filters handle variations to work on images, PBR materials, and environment lights
* &lbrack;Compound Filters&rbrack; Tweaks order matches the nodes list order in the compound filter
* &lbrack;Compound Filters&rbrack; Tweaks of different nodes with the same group will be merged in one single group in the Properties panel
* &lbrack;Application&rbrack; Have dedicated viewer settings per asset type

**Fixed:**

* &lbrack;Application&rbrack; Application may crash when switching to 2D view
* &lbrack;Application&rbrack; Fix a possible deadlock or crash when exporting multiple times
* &lbrack;Application&rbrack; Make default values for channels consistent with Substance 3D Designer
* &lbrack;Application&rbrack; Loading a project doesn't trigger the material recompute
* &lbrack;Application&rbrack; Updated the URL to texture import documentation
* &lbrack;Content&rbrack; When using a compound filter, it asks to be updated when it shouldn't, on reload
* &lbrack;Content&rbrack; Details in height map disappear when using Opacity Blend
* &lbrack;UI&rbrack; In the Color Dialog, it is possible to get out of range using the slider's text fields
* &lbrack;UI&rbrack; Usage list has a useless vertical scrollbar

**Known Issues:**

* &lbrack;Color Picker&rbrack; Picking a color on a second monitor with a different resolution may not work
* &lbrack;Content&rbrack; Shape light widget is not working in spherical projection mode
* &lbrack;Interoperability&rbrack; Material with displacement sent to Stager will lose displacement controls

### 3.2.1 Yakitori

*(Released: March 08, 2022)*

**Added:**

* &lbrack;Export&rbrack; Export dpi metadata in image files
* &lbrack;Physical Size&rbrack; Keep the ratio with non square textures when editing physical dimensions
* &lbrack;Physical Size&rbrack; Physical size metadata is applied immediatly when physical size changes
* &lbrack;UI&rbrack; Adjust Height scale max slider so it can influence any kind of material when Physical Size is enabled
* &lbrack;UI&rbrack; New tooltips on search filters in the Asset panel
* &lbrack;UI&rbrack; Use tooltips to explain when buttons are disabled in the Assets panel
* &lbrack;Content&rbrack; Brightness contrast filter update

**Fixed:**

* &lbrack;2D View&rbrack; 90 degrees rotation button in the Crop and Transform tools don't work as expected
* &lbrack;2D View&rbrack; Crop widget sometimes goes missing
* &lbrack;Application&rbrack; Clearing an image parameter does not reconnect the underlying layer
* &lbrack;Application&rbrack; Crash at exit after saving a project
* &lbrack;Application&rbrack; Crash when drag and dropping the current material into a collection of the Assets Panel
* &lbrack;Application&rbrack; Drag and dropping an asset in the viewport may crash
* &lbrack;Content&rbrack; Normal blend has a random seed tweak
* &lbrack;Content&rbrack; Snow filter has incorrect normal output depending on fresh and melted snow parameter values
* &lbrack;Content&rbrack; Parquet filter: fixed unexpected seams
* &lbrack;Content&rbrack; Embroidery filter: remove thread in metallic map
* &lbrack;Content&rbrack; Floor tiles filter: fix x and y tiles count
* &lbrack;Content&rbrack; Brick wall filter: output normal and height to 16 bit
* &lbrack;Export&rbrack; Default file name in export popup is not the current material name
* &lbrack;Export&rbrack; Exporting with physical ratio with an export preset gives incorrect dimensions
* &lbrack;Export&rbrack; Metallic is missing in the CLO export preset
* &lbrack;Export&rbrack; When replacing an export custom preset, the display name is not updated
* &lbrack;Layers&rbrack; Custom channels of the first inserted layer are not discovered
* &lbrack;Layers&rbrack; Material is re-evaluated when changing tweaks of a hidden layer
* &lbrack;Localization&rbrack; Tooltips are not localized in Export panel
* &lbrack;Physical Size&rbrack; Disabling Physical Size of an asset does not remove the physical scale
* &lbrack;Physical Size&rbrack; Height Scale value can't be set outside of slider bounds the first time
* &lbrack;Physical Size&rbrack; Importing an image with no physical size prevents opening the project
* &lbrack;Physical Size&rbrack; Physical Size is erroneously set to zero when missing
* &lbrack;Physical Size&rbrack; Physical Size physical scale check box status is not updated when first displayed
* &lbrack;UI&rbrack; Base Material & Normal to Height do not have a category
* &lbrack;UI&rbrack; Cursor is sometimes invisible when painting an image
* &lbrack;UI&rbrack; Disable "Copy All" and "Cut All" options in the edit menu of a text field if it is empty
* &lbrack;UI&rbrack; Filter names have incorrect characters
* &lbrack;UI&rbrack; Physical Size lock button does not have the correct style
* &lbrack;UI&rbrack; The close button in search bar in Asset Panel does not clear the search string

**Known Issues:**

* &lbrack;Color Picker&rbrack; Picking a color on a second monitor with a different resolution may not work

### 3.2.0 Yakitori

*(Released: January 25, 2022)*

**Added:**

* &lbrack;Physical Size&rbrack; New Physical Size panel
* &lbrack;Physical Size&rbrack; Add Physical Size options to the Material Creation Template window
* &lbrack;Physical Size&rbrack; Add Physical Size measurement tool
* &lbrack;Physical Size&rbrack; Add Physical Size auto-measurement tool
* &lbrack;Physical Size&rbrack; Add Physical Size diagnostic tool
* &lbrack;Physical Size&rbrack; Allow setting the z value of the Physical Size
* &lbrack;Physical Size&rbrack; Dropdown widget to set the level of zoom in the 2D view
* &lbrack;Physical Size&rbrack; New "Display with physical ratio" option in the level of zoom dropdown
* &lbrack;Physical Size&rbrack; New "Fit to physical size" option in the level of zoom dropdown
* &lbrack;Physical Size&rbrack; Display the Physical Size in the 2D view
* &lbrack;Physical Size&rbrack; Display the Physical Size in the 3D viewport
* &lbrack;Physical Size&rbrack; In the image import dialog, show physical size depth if there is an imported height map
* &lbrack;Physical Size&rbrack; Show the Physical Size in the asset contextual menu
* &lbrack;Physical Size&rbrack; Set the length unit in the Preferences
* &lbrack;Physical Size&rbrack; Export textures respecting the physical ratio
* &lbrack;Metadata&rbrack; Ability to add custom metadata to a user-authored asset
* &lbrack;Export&rbrack; Export custom metadata to .sbs(ar) files
* &lbrack;Export&rbrack; Export description, category, author, and tags metadata to .sbs(ar) files
* &lbrack;Export&rbrack; Export the Physical Size to .sbs(ar) files
* &lbrack;Export&rbrack; Set .sbsar file compression setting
* &lbrack;Export&rbrack; Export the asset thumbnail to .sbs(ar) files
* &lbrack;Export&rbrack; Set the graph type when exporting a .sbs(ar) file
* &lbrack;Application&rbrack; Realtime Engine 2021 is no longer available
* &lbrack;Application&rbrack; Undo/Redo now supports Tiling (U,V) and height scale slider changes
* &lbrack;Rendering&rbrack; Generate disk cache when the authored asset is saved
* &lbrack;Assets&rbrack; Use Ctrl+click to enable multiple asset type filters in the Resources panel
* &lbrack;UI&rbrack; Ability to lock the Tiling (U,V) sliders
* &lbrack;UI&rbrack; Add a contextual menu with "Copy", "Cut", "Paste", "Copy all" and "Cut all" in text fields
* &lbrack;UI&rbrack; Length unit (meters, inches, parsecs, ...) support in labels and text fields
* &lbrack;UI&rbrack; The user can set the decimal precision used to display numbers
* &lbrack;UI&rbrack; Use units in measure popups everywhere it's relevant
* &lbrack;Localization&rbrack; Default new asset name is now localized
* &lbrack;Content&rbrack; New Cloth Weave generator
* &lbrack;Content&rbrack; New Channel Switch filter
* &lbrack;Content&rbrack; All relevant filters are now aware of the Physical Size
* &lbrack;Content&rbrack; New icons for Wood Finish
* &lbrack;Content&rbrack; All filters are now compatible with Adobe Standard Materials (ASM) channels
* &lbrack;Content&rbrack; Filters can now have an "environment" variation

**Fixed:**

* &lbrack;2D View&rbrack; Channel remains in the list when removed
* &lbrack;Application&rbrack; Cannot duplicate an asset loaded from the operating system file explorer
* &lbrack;Application&rbrack; Crash at exit
* &lbrack;Application&rbrack; Crash sometimes when clicking "Starter Assets" in the Assets panel
* &lbrack;Application&rbrack; Crash when deleting a material
* &lbrack;Application&rbrack; Environment variable "SUBSTANCE_DISABLE_SPECIFIC_FEATURES" is still active when set to "0" or "".
* &lbrack;Application&rbrack; Freeze while saving a project with multiple materials
* &lbrack;Application&rbrack; Importing an image can lead to a crash
* &lbrack;Application&rbrack; Missing some starter assets on first launch
* &lbrack;Export&rbrack; Exporting an asset sometimes leads to a crash
* &lbrack;Layers&rbrack; Cannot import images when the layer panel is closed or invisible
* &lbrack;Layers&rbrack; Changing the language causes the current asset to recompute
* &lbrack;Layers&rbrack; Changing the usage of an imported image does not upate which filter variation to use
* &lbrack;Layers&rbrack; Image to Material (AI) is sometimes not computed when tweaking layers below it
* &lbrack;Layers&rbrack; Image to Material (AI) sometimes recomputes when not needed
* &lbrack;Layers&rbrack; No update is suggested when a custom filter is updated on the disk
* &lbrack;Layers&rbrack; Normal channel sometimes has the wrong pixel format
* &lbrack;Layers&rbrack; Some layers are still computed even when not visible
* &lbrack;Layers&rbrack; The 2D view tools may be broken when toggling a layer visibility
* &lbrack;Layers&rbrack; The UI freezes when using Image to Material (AI)
* &lbrack;Layers&rbrack; Toggling the visibilty of the Transform filter layer breaks the 2D view tool and may lead to a crash
* &lbrack;Layers&rbrack; Too many recomputations when removing a layer from the layer stack
* &lbrack;Layers&rbrack; When a compound filter contains an unusual or custom input/output, Sampler doesn't compute it
* &lbrack;Performance&rbrack; Asset panel is slow to open
* &lbrack;Performance&rbrack; Avoid some unnecessary recomputations of the layer stack
* &lbrack;Performance&rbrack; Loading project assets takes too much time
* &lbrack;Performance&rbrack; Render cache on disk may not be used
* &lbrack;Performance&rbrack; Switching between layers is slow
* &lbrack;Performance&rbrack; Tweaking a material or a filter is slow
* &lbrack;Project&rbrack; Saving a project when exiting may lead to a crash
* &lbrack;Rendering&rbrack; Removing an image may remove all outputs
* &lbrack;Rendering&rbrack; The rendering time displayed in the viewport is wrong when tweaking
* &lbrack;UI&rbrack; Can't scroll vertically in the export popup when needed
* &lbrack;UI&rbrack; It is possible to open the export popup when there is nothing to export
* &lbrack;UI&rbrack; Some popups do not scroll if their content overflows
* &lbrack;UI&rbrack; Text fields are not selected when clicking on it or opening a menu
* &lbrack;UI&rbrack; The name of the blend mode in the properties panel is sometimes not correct
* &lbrack;UI&rbrack; The Save option in the File menu is sometimes grayed out
* &lbrack;UI&rbrack; The text field doesn't go away after renaming two materials
* &lbrack;UI&rbrack; Typo in the preference popup

**Known Issues:**

* &lbrack;Color Picker&rbrack; Picking a color on a second monitor with a different resolution may not work

### 3.1.2 Xocoatl

*(Released: December 14, 2021)*

**Fixed:**

* &lbrack;Interoperability&rbrack; Open .sbsar file with Substance 3D Sampler from Bridge can fail on Windows
* &lbrack;Layers&rbrack; Moving the only layer below itself will crash
* &lbrack;UI&rbrack; Channel settings button disappears when changing language
* &lbrack;UI&rbrack; The material name in Properties panel disappears after saving the project
* &lbrack;Assets&rbrack; Clicking on "All libraries" can lead to a crash

**Known Issues:**

* &lbrack;Realtime Engine 2021&rbrack; Heavy computation can crash the application
* &lbrack;Realtime Engine 2021&rbrack; Realtime Engine 2021 will crash on a Windows machine with both AMD CPU and Nvidia GPU installed
* &lbrack;Color Picker&rbrack; Picking a color on a second monitor with a different resolution may not work

### 3.1.1 Xocoatl

*(Released: November 24, 2021)*

**Added:**

* &lbrack;Interoperability&rbrack; Send assets (SBS or SBSAR) to Substance 3D Designer
* &lbrack;Interoperability&rbrack; Set in preferences the default format for interoperability with Substance 3D Designer
* &lbrack;Interoperability&rbrack; Receive multiple assets from Adobe Bridge
* &lbrack;UI&rbrack; New Random Seed widget
* &lbrack;UI&rbrack; Context menu update
* &lbrack;Assets&rbrack; Drag and drop images from the Assets panel to the Properties panel
* &lbrack;Project&rbrack; Asset names are sanitised to avoid some specific characters
* &lbrack;Branding&rbrack; Update file icon for SBSAR files
* &lbrack;Engine&rbrack; Update Substance Engine version 8.3.0

**Fixed:**

* &lbrack;Content&rbrack; Crop - Preserve ratio when cropping non-square images
* &lbrack;Content&rbrack; Transform - Horizontal transformation is not inverted when using the widget
* &lbrack;Content&rbrack; Gravel - fix custom mask painting on all channels
* &lbrack;Content&rbrack; Floor tiles - fix issues with pattern tiling and repetition
* &lbrack;Assets&rbrack; Grey out Adobe Bridge option if not installed
* &lbrack;Color Picker&rbrack; Escape key closes the Color Picker
* &lbrack;Rendering&rbrack; Fix Scattering Distance Scale when using greyscale input
* &lbrack;Share&rbrack; Send to options are only available with Adobe licenses
* &lbrack;Project&rbrack; Fix a memory performance issue

**Known Issues:**

* &lbrack;Realtime Engine 2021&rbrack; Heavy computation can crash the application
* &lbrack;Realtime Engine 2021&rbrack; Realtime Engine 2021 will crash on a Windows machine with both AMD CPU and Nvidia GPU installed
* &lbrack;Color Picker&rbrack; Picking a color on a second monitor with a different resolution may not work

### 3.1.0 Xocoatl

*(Released: September 28, 2021)*

**Added:**

* &lbrack;Color Picker&rbrack; New Color Picker UI
* &lbrack;Color Picker&rbrack; Preview the current and previous colors side by side
* &lbrack;Color Picker&rbrack; Input your color in Hexadecimal
* &lbrack;Color Picker&rbrack; New eyedropper with color preview
* &lbrack;Color Picker&rbrack; The eyedropper can pick a color outside of Sampler
* &lbrack;Color Picker&rbrack; Tweak your color in RGB or HSV color spaces
* &lbrack;Color Picker&rbrack; Save and manage Swatches
* &lbrack;Interoperability&rbrack; Edit images in Illustrator from Image Import layer or Image parameters
* &lbrack;Interoperability&rbrack; Edit images in Photoshop from Image Import layer or Image parameters
* &lbrack;Widget&rbrack; New Crop Widget
* &lbrack;Widget&rbrack; Press Enter to validate your crop
* &lbrack;Widget&rbrack; The Crop widget reads the image size to fit the widget and keep the ratio when resizing
* &lbrack;UI&rbrack; New gresycale slider UI
* &lbrack;Application&rbrack; Add normal format selection in preferences
* &lbrack;Application&rbrack; The normal format in Image Import layers follows the default normal format set in the preferences
* &lbrack;Application&rbrack; In the 2D view, the normal is displayed following the normal format set in the preferences
* &lbrack;Application&rbrack; The normal is exported in the normal format set in preferences
* &lbrack;Export&rbrack; Add normal format parameter to SBS and SBSAR file exports
* &lbrack;Export&rbrack; Add shader settings to SBS and SBSAR file exports
* &lbrack;Export&rbrack; Set the default resolution of exported SBS graphs
* &lbrack;Compound Filters&rbrack; Package SSA filters with 7z
* &lbrack;Compound Filters&rbrack; Add category metadata in compound filters
* &lbrack;Compound Filters&rbrack; Compound Filters can have an embedded thumbnail
* &lbrack;Compound Filters&rbrack; Added Compound Filters extension (.ssafilter) to the Get Content's file dialog
* &lbrack;Compound Filters&rbrack; Import Compound Filters (.ssafilter) in the Assets panel
* &lbrack;Engine&rbrack; Update substance engine to v8.2.0

**Fixed:**

* &lbrack;Application&rbrack; Connected local folders may hang
* &lbrack;Application&rbrack; Crash at exit
* &lbrack;Application&rbrack; Crash when launching two instances of Sampler
* &lbrack;Content&rbrack; Crop filter has a random seed tweak
* &lbrack;Content&rbrack; Some Substance materials are sometimes not upgraded
* &lbrack;Export&rbrack; Crash when exporting with a newly added custom preset
* &lbrack;Export&rbrack; Estimated size of package is missing in export popup
* &lbrack;Export&rbrack; Fix memory leak when exporting SBS and SBSAR files
* &lbrack;Compound Filters&rbrack; Compound filters may have duplicated inputs
* &lbrack;Compound Filters&rbrack; Crash if a filter has unmet references
* &lbrack;Compound Filters&rbrack; Crash when reordering a layer stack with a compound filter in it
* &lbrack;Compound Filters&rbrack; The render sometimes hangs
* &lbrack;Image Import&rbrack; Importing an image triggers multiple renderings
* &lbrack;Layers&rbrack; Crash on undo/redo
* &lbrack;Layers&rbrack; Crash when adding a Base Material
* &lbrack;Layers&rbrack; Crash when using an invalid image as environment light
* &lbrack;Layers&rbrack; Fix duplicate import when inserting a filter with several graphs
* &lbrack;Layers&rbrack; Reordering layers doesn't always work
* &lbrack;Project&rbrack; Crash when loading an incomplete project file
* &lbrack;Project&rbrack; Crash when opening a corrupted project
* &lbrack;Project&rbrack; Some assets can disappear from a project
* &lbrack;Properties&rbrack; Fix missing filter's presets
* &lbrack;UI&rbrack; Angle parameters cannot be set
* &lbrack;UI&rbrack; Filters metadata display in Asset panel
* &lbrack;UI&rbrack; Grouping by category hides filters
* &lbrack;UI&rbrack; Scroll issue in the Asset panel
* &lbrack;UI&rbrack; The export panel now has a scrollbar
* &lbrack;UI&rbrack; The thumbnail is not displayed for some image formats in image picker

**Known Issues:**

* &lbrack;Realtime Engine 2021&rbrack; Heavy computation can crash the application
* &lbrack;Realtime Engine 2021&rbrack; Realtime Engine 2021 will crash on a Windows machine with both AMD CPU and Nvidia GPU installed
* &lbrack;Color Picker&rbrack; Picking a color on a second monitor with a different resolution may not work

### 3.0.1 Waffle

*(Released: July 27, 2021)*

**Added:**

* &lbrack;Brush&rbrack; Enable colors in brush tool if the image input supports it
* &lbrack;Brush&rbrack; Holding the Shift key in the brush tool draws straight lines
* &lbrack;Brush&rbrack; Show a line preview when holding shift in the brush tool
* &lbrack;Brush&rbrack; Brush tool now supports undo and redo
* &lbrack;2D View&rbrack; Image input default color is used when painting
* &lbrack;Layers&rbrack; Read Substance input default value in SBSAR files
* &lbrack;Rendering&rbrack; Allow to combine height with normal
* &lbrack;Rendering&rbrack; Sub-surface scattering support (not available on MacOS)
* &lbrack;Assets&rbrack; Use SBSAR graph type to determine asset type
* &lbrack;Assets&rbrack; Better performance for search and asset discoverability in the Assets panel
* &lbrack;Assets&rbrack; Added a 'All Libraries' entry in the Assets panel that displays all assets of all your libraries
* &lbrack;Assets&rbrack; User can now choose to group assets by category or type
* &lbrack;Import&rbrack; Auto detect anisotropy, coat, sheen and specular edge color textures at import
* &lbrack;UI&rbrack; Replace elided panel title with an icon
* &lbrack;UI&rbrack; Textfields style update
* &lbrack;UI&rbrack; New description text in The Environment Light Template Creation window
* &lbrack;Application&rbrack; Export assets with the current resolution when sending to external application
* &lbrack;Application&rbrack; Material default resolution is now 2048\*2048 (1024\*1024 on macos)
* &lbrack;Content&rbrack; New patterns in the Floor tiles filter
* &lbrack;Content&rbrack; New Dual Color mode in the Color replace filter

**Fixed:**

* &lbrack;2D View&rbrack; First stroke in brush tool is sometimes broken
* &lbrack;2D View&rbrack; Free resources when brush tool is not visible
* &lbrack;2D View&rbrack; Use the right resize cursor in the transform widget
* &lbrack;2D View&rbrack; Widgets are not displayed if the user has panned in the 2D view before
* &lbrack;Application&rbrack; Crash when opening a project with broken workflow
* &lbrack;Application&rbrack; Fix application shutdown to prevent flooding the log with useless errors
* &lbrack;Application&rbrack; Redo, delete and save keyboard shortcuts don't work on some operating systems
* &lbrack;Application&rbrack; Undo/redo changing image usage in import layer is broken
* &lbrack;Export&rbrack; Emission color exported images have wrong name
* &lbrack;Export&rbrack; Environment is 8bit when using SBSAR export
* &lbrack;Export&rbrack; Remove extra spaces in exported image file names
* &lbrack;Export&rbrack; Replacing or deleting a custom export preset crashes
* &lbrack;Layers&rbrack; Avoid crash when there is an input count mismatch
* &lbrack;Layers&rbrack; Crash when inserting a Base Material layer
* &lbrack;Layers&rbrack; Filter input count is capped to default value
* &lbrack;Layers&rbrack; Redo erroneously changes the Blend type to Height blend
* &lbrack;Layers&rbrack; Remove drop zone above input headers
* &lbrack;Layers&rbrack; Layers are inserted at the wrong place around input headers
* &lbrack;Layers&rbrack; Reset all settings button does not reset drop down widgets values
* &lbrack;Layers&rbrack; Undo/redo when changing an image on the Image Import layer marks the project as modified and so to save
* &lbrack;Layers&rbrack; Usages may be stopped by blend layers
* &lbrack;Project&rbrack; Crash when loading a legacy project with missing dependencies folder
* &lbrack;Project&rbrack; Crash when using undo/redo after saving
* &lbrack;Project&rbrack; Opening a SBSAR file containing an environment light creates a material asset
* &lbrack;Project&rbrack; Renaming a material can trigger a thumbnail generation
* &lbrack;Project&rbrack; Saving after renaming a material marks the project as unmodified
* &lbrack;Project&rbrack; Some changes after renaming a material are not saved
* &lbrack;Rendering&rbrack; Bright dots are visible on the environment with 2020 realtime engine
* &lbrack;Rendering&rbrack; Crash when resizing using Real Time Engine 2021
* &lbrack;Rendering&rbrack; Recompute shadows on height level change
* &lbrack;Assets&rbrack; Connected folders stop indexing new assets when adding an invalid file
* &lbrack;Assets&rbrack; Crash when connecting a local folder with many materials
* &lbrack;UI&rbrack; 2D/3D view buttons missing tooltips
* &lbrack;UI&rbrack; All assets in the Assets panel are highlighted at launch
* &lbrack;UI&rbrack; Breadcrumbs sometimes disapears in the Assets panel when importing materials
* &lbrack;UI&rbrack; Changing language doesn't affect the Project panel
* &lbrack;UI&rbrack; Channel Settings panel shows legacy workflow information
* &lbrack;UI&rbrack; Correctly align "No settings for this item" text for filters with no tweaks in properties panel
* &lbrack;UI&rbrack; Elements are mis-aligned in the welcome screen and the preferences popup
* &lbrack;UI&rbrack; Panel titles have incorrect width
* &lbrack;UI&rbrack; Scrolling is sometimes broken in the Properties panel
* &lbrack;UI&rbrack; Splash screen has incorrect ratio and is blurry
* &lbrack;UI&rbrack; The fullscreen mode is not fullscreen
* &lbrack;UI&rbrack; Undocked panels are always on top even when the application is not active on MacOS
* &lbrack;UI&rbrack; Update welcome screen banner image
* &lbrack;Content&rbrack; Tiling filter doesn't process the ambient occlusion channel
* &lbrack;Content&rbrack; Quilt Stitch issue with the welt assembly seam selection and diamond pattern
* &lbrack;Content&rbrack; Emboss filter works in 256px by 256px
* &lbrack;Content&rbrack; Fix tiling issue with the Floor tiles when the offset is greater than 0

**Known Issues:**

* &lbrack;Realtime Engine 2021&rbrack; Heavy computation, crash the application
* &lbrack;Realtime Engine 2021&rbrack; Realtime Engine 2021 will crash on Windows machine with both AMD CPU and Nvidia GPU

### 3.0.0 Waffle

*(Released: June 23, 2021)*

**Added:**

* &lbrack;Branding&rbrack; Substance Alchemist becomes Adobe Substance 3D Sampler
* &lbrack;Branding&rbrack; New application icons
* &lbrack;UI&rbrack; New User Experience and User Interface
* &lbrack;UI&rbrack; New Splashscreen
* &lbrack;UI&rbrack; Panels are undockable and dockable in the interface
* &lbrack;UI&rbrack; Dock up to 3 panels in the same column
* &lbrack;UI&rbrack; Dock up to 3 panels in the same panel (Tabs)
* &lbrack;UI&rbrack; Undock panels to create a separate window in the same or a different screen
* &lbrack;UI&rbrack; Closed panels pop-over when clicking on their icons
* &lbrack;UI&rbrack; Re-arrange your left and right bar by moving panels icons
* &lbrack;UI&rbrack; New toolbar to access directly specific filters (Crop, Transform, Perspective Transform, Clone Stamp)
* &lbrack;UI&rbrack; New "Get Content" button in the left bar
* &lbrack;UI&rbrack; Import files directly in your assets with the Get Content button
* &lbrack;UI&rbrack; Import files directly to your Layers with the Get Content button
* &lbrack;UI&rbrack; Access directly Adobe Substance 3D Assets website with the Get Content button
* &lbrack;UI&rbrack; Resolution widget is now directly accessible in the viewport
* &lbrack;UI&rbrack; All UI elements now are loaded dynamically
* &lbrack;UI&rbrack; Shortcut - Use "2" to toggle the visibility of the 2D view
* &lbrack;UI&rbrack; Shortcut - Use "3" to toggle the visibility of the 3D view
* &lbrack;Welcome Screen&rbrack; Create a project in one-click with the New button
* &lbrack;Welcome Screen&rbrack; New artwork banner
* &lbrack;Project&rbrack; All projects are now associated to a unique file
* &lbrack;Project&rbrack; New project file extension .ssa
* &lbrack;Project&rbrack; Save as a project will ask you to select where to save your project
* &lbrack;Project&rbrack; Closing Sampler will ask you to save your project if not saved
* &lbrack;Project&rbrack; Closing Sampler will ask you to save your project if there are modifications since the last save
* &lbrack;Project&rbrack; The name of your project is displayed above the viewport
* &lbrack;Project&rbrack; The project name is in italics with a star if it is not saved or if it contains modifications since the last save
* &lbrack;Project&rbrack; Open a .ssa project file directly from your OS explorer
* &lbrack;Project&rbrack; Open a .sbsar from your OS explorer will launch Sampler with a new project with this .sbsar file ready to use
* &lbrack;Project&rbrack; Open a .alch (legacy Substance Alchemist file) from your OS explorer
* &lbrack;Project Panel&rbrack; New panel that will contain all assets created within a project
* &lbrack;Project Panel&rbrack; Create an asset (material or environment light) using the + icon
* &lbrack;Project Panel&rbrack; Right-click on asset opens a context menu
* &lbrack;Project Panel&rbrack; From the right-click context menu, you can delete an asset
* &lbrack;Project Panel&rbrack; From the right-click context menu, you can duplicate an asset
* &lbrack;Project Panel&rbrack; From the right-click context menu, you can rename an asset
* &lbrack;Project Panel&rbrack; Switching between assets won't lose modifications
* &lbrack;Resolution&rbrack; You can now set non-square resolution for all your assets
* &lbrack;Resolution&rbrack; The resolution value is saved by asset within a project
* &lbrack;Environment Light&rbrack; Create environment light within Substance 3D Sampler
* &lbrack;Environment Light&rbrack; When creating an environment light, dragging and dropping image(s) will display the Environment Light Creation Template Window
* &lbrack;Environment Light&rbrack; In the Environment Light Creation Template, select Environment Import to assign your image to the environment in the 3D view
* &lbrack;Environment Light&rbrack; In the Environment Light Creation Template, select HDR merge to create an environment light from several 360-degrees images with different exposure
* &lbrack;Environment Light&rbrack; In the Environment Light Creation Template, select "Use as bitmap" to edit your image(s) before creating an environment light
* &lbrack;Environment Light&rbrack; Assign the environment usage in the Image Import layer to directly assign the image to the environment in the 3D view
* &lbrack;Environment Light&rbrack; In the 2D view for the environment channel, there is an automatic color correction to have the rendering appear the same as in the 3D view
* &lbrack;Environment Light&rbrack; New dedicated content for environment light creation
* &lbrack;Assets Panel&rbrack; The Resources and Filters panels are merged in a new Assets panel
* &lbrack;Assets Panel&rbrack; The Assets panel now supports the following asset types: materials, filters and images
* &lbrack;Assets Panel&rbrack; All Starter Assets are accessible in the Starter Assets section
* &lbrack;Assets Panel&rbrack; Starter Assets section is read-only
* &lbrack;Assets Panel&rbrack; New "Your Assets" section
* &lbrack;Assets Panel&rbrack; "Your Assets" section is the place where you can import all your resources
* &lbrack;Assets Panel&rbrack; All assets in "Your assets" are added in a specific folder in your Documents
* &lbrack;Assets Panel&rbrack; Connect local folders in the Assets panel to add new sections
* &lbrack;Assets Panel&rbrack; The search will search in the current folder and its subfolders
* &lbrack;Assets Panel&rbrack; Navigate between folders and subfolders with breadcrumbs
* &lbrack;Assets Panel&rbrack; Filter the current folder by material, by filter or by image
* &lbrack;Assets Panel&rbrack; Combine several filters to get only materials and images
* &lbrack;Assets Panel&rbrack; Change the display by switching between a grid or a list
* &lbrack;Assets Panel&rbrack; Filters are represented with their icon
* &lbrack;Assets Panel&rbrack; Images are represented with their preview
* &lbrack;Assets Panel&rbrack; Increasing the width will change the layout of the panel with a specific view to navigate between folders
* &lbrack;Assets Panel&rbrack; On non read-only sections, delete an asset by dragging an dropping it on the bin icon
* &lbrack;Assets Panel&rbrack; Right-click on asset opens a context menu
* &lbrack;Assets Panel&rbrack; From the right-click context menu, access the asset metadata (name, category, location)
* &lbrack;Assets Panel&rbrack; From the right-click context menu, delete the asset (only available on non read-only sections)
* &lbrack;Assets Panel&rbrack; From the right-click context menu, browse your asset in Adobe Bridge
* &lbrack;Layers Panel&rbrack; New icon to directly add a base material on top of your layers
* &lbrack;Layers Panel&rbrack; Shortcut - Shift + B will add a base material on top of your layers
* &lbrack;Layers Panel&rbrack; Layers now have a thumbnail preview (Material thumbnail, filter icon or Image preview)
* &lbrack;Properties Panel&rbrack; New design of the Properties panel title with the asset name and the asset thumbnail
* &lbrack;Properties Panel&rbrack; Filter Layers now support presets
* &lbrack;Properties Panel&rbrack; On Image Import Layer, right-click on the image preview to edit the image in Photoshop
* &lbrack;Adobe Bridge&rbrack; Browse your Asset in Adobe Bridge, will launch Bridge at the location of the asset
* &lbrack;Adobe Photoshop&rbrack; Edit in Adobe Photoshop will open the image in Photoshop ready to be edited
* &lbrack;Adobe Photoshop&rbrack; At each save in Adobe Photoshop, the edited image will be reloaded in Sampler
* &lbrack;Substance 3D Designer&rbrack; Assets sent from Adobe Substance 3D Designer will arrive directly in the "Your Assets" section of the Assets panel
* &lbrack;Export&rbrack; Send assets directly to Adobe Substance 3D Painter and Adobe Substance 3D Stager
* &lbrack;Export&rbrack; Send materials and environment lights to Adobe Substance 3D Painter
* &lbrack;Export&rbrack; Send environment lights to Adobe Substance 3D Stager
* &lbrack;Rendering&rbrack; New material properties are now supported and rendered in 3D
* &lbrack;Rendering&rbrack; Adding Sheen support (Sheen color, Sheen opacity and Sheen roughness)
* &lbrack;Rendering&rbrack; Adding Coating support (Coat color, Coat Roughness, Coat Normal, Coat Specular Level and Coat IOR)
* &lbrack;Rendering&rbrack; Adding Anisotropy support (Anisotropy Level and Anisotropy Angle)
* &lbrack;Rendering&rbrack; Adding Specular Edge Color support
* &lbrack;Rendering&rbrack; Activate these new properties in the Channel Settings panel
* &lbrack;Rendering&rbrack; Introduction of a new Realtime Engine (2021) renderer in Beta
* &lbrack;Rendering&rbrack; Switch between the two Renderer versions in the Viewer Settings panel
* &lbrack;Rendering&rbrack; The Realtime Engine (2021) renderer supports translucency, absorption and scattering material properties
* &lbrack;Rendering&rbrack; The Realtime Engine (2021) renderer introduces a new way to compute shadows from the environment light
* &lbrack;Rendering&rbrack; The Realtime Engine (2021) renderer computes in realtime the irradiance of the environment light
* &lbrack;Shader Settings Panel&rbrack; New Shader Settings panel to tweak specific material shader parameters
* &lbrack;Shader Settings Panel&rbrack; New parameters (Normal scale, height scale, height level, Emission intensity, IOR, Coat normal intensity and Coat IOR)
* &lbrack;Shader Settings Panel&rbrack; Specific parameters for the Realtime Engine 2021 (Subsurface Scattering, Scattering Distance, Red Shift and Rayleigh Scattering)
* &lbrack;Shader Settings Panel&rbrack; The settings values are saved per asset
* &lbrack;Viewer Settings Panel&rbrack; Added a preview of the default environment lights
* &lbrack;Viewer Settings Panel&rbrack; Added a preview of the default meshes
* &lbrack;Viewer Settings Panel&rbrack; New environment opacity parameter
* &lbrack;Viewer Settings Panel&rbrack; New environment blur parameter (specific to the Realtime Engine 2021 renderer)
* &lbrack;Localization&rbrack; New translations in German and French
* &lbrack;Content&rbrack; New default starter materials
* &lbrack;Content&rbrack; New default environment lights
* &lbrack;Content&rbrack; All filters have been updated, cleaned, and optimized
* &lbrack;Content&rbrack; The Adjustment filter has been split into several filters
* &lbrack;Content&rbrack; New Brightness/Contrast filter
* &lbrack;Content&rbrack; New Hue/Saturation filter
* &lbrack;Content&rbrack; New Vibrance filter
* &lbrack;Content&rbrack; New Sharpen filter
* &lbrack;Content&rbrack; New Normal/Height adjustment
* &lbrack;Content&rbrack; New Panels filter
* &lbrack;Content&rbrack; New Smudge filter
* &lbrack;Content&rbrack; New Weaves filter
* &lbrack;Content&rbrack; New Warp transform filter
* &lbrack;Content&rbrack; New Height to AO filter
* &lbrack;Content&rbrack; New Height to Normal filter
* &lbrack;Content&rbrack; Color Replace - Replace in new supported channels (Sheen, Coating, Anisotropy,...)
* &lbrack;Content&rbrack; Color variation - Manual mode to select exactly the colors to change
* &lbrack;Content&rbrack; Tiling - option to visualize the seams cut
* &lbrack;Content&rbrack; Tiling - option to paint the seams cut for a perfect tiling
* &lbrack;Content&rbrack; Match - option to add a material to match its color and its roughness
* &lbrack;Content&rbrack; Match - it now works on images to match the color of another image
* &lbrack;Content&rbrack; Environment ligth - New Color Temperature filter
* &lbrack;Content&rbrack; Environment ligth - New Exposure filter
* &lbrack;Content&rbrack; Environment ligth - New Exposure Preview filter
* &lbrack;Content&rbrack; Environment ligth - New Nadir Patch filter
* &lbrack;Content&rbrack; Environment ligth - New Nadir Extract filter
* &lbrack;Content&rbrack; Environment ligth - New Lights filters (Sphere, Line, Shape, Plane)
* &lbrack;Content&rbrack; Environment ligth - New Panorama Patch filter
* &lbrack;Content&rbrack; Environment ligth - New Straighten Horizon filter
* &lbrack;Content&rbrack; Environment ligth - New HDR merge filter

**Known Issues:**

* &lbrack;Realtime Engine 2021&rbrack; Changing the layout, crash the application
* &lbrack;Realtime Engine 2021&rbrack; Heavy computation, crash the application
* &lbrack;Panels&rbrack; MacOS - Undocked panels are in front of all applications
* &lbrack;Widgets&rbrack; Transform and Positions widgets can disappear. Hide and Unhide the layer to make them appear.
* &lbrack;Export&rbrack; SBSAR export of an environment light loses the 32bit depth precision
* &lbrack;Assets Panel&rbrack; Assets can be highlighted when opening a folder
* &lbrack;Properties Panel&rbrack; Resetting the parameters doesn't reset the combobox UI
* &lbrack;Localization&rbrack; Changing language doesn't affect the project panel until it's recreated

## Version 2

### 2.3.2 (2020.3.2) Vermicelli

*(Released: February 23, 2021)*

**Added:**

* &lbrack;Localization&rbrack; Japanese support

**Fixed:**

* &lbrack;Layers&rbrack; Tweaking a material in the embroidery filter loses the embroidery image

**Known Issues:**

* Usage of Image to Material (AI powered) on high resolution images can be slow
* Content Aware Fill filters are slow in high resolution
* Coma or point can be ignored when typing a specific evalue in a slider
* Impossible to save twice the exact same material layer stack

### 2.3.1 (2020.3.1) Vermicelli

*(Released: December 17, 2020)*

**Added:**

* &lbrack;Engine&rbrack; Substance Engine update
* &lbrack;Application&rbrack; Environment variable to disable specific features
* &lbrack;Content&rbrack; Replace color - New Advanced segmentation option
* &lbrack;Content&rbrack; Floor Tiles - new patterns and options available
* &lbrack;Content&rbrack; Embroidery - Complete revamp of the filter
* &lbrack;Content&rbrack; Adjustment - New metallic parameter + opacity safe transform correction

**Fixed:**

* &lbrack;Layers&rbrack; Cannot import twice the same custom filter
* &lbrack;Layers&rbrack; Cannot use image input with the brush tool
* &lbrack;Export&rbrack; Export .jpg instead of .jpeg
* &lbrack;UI&rbrack; Update welcome screen image credits
* &lbrack;UI&rbrack; Fix invisible separator in menus
* &lbrack;UI&rbrack; Radio buttons display a tooltip when they are truncated
* &lbrack;UI&rbrack; Typo: Starter Materials
* &lbrack;Application&rbrack; UTF-8 characters in asset names do not work
* &lbrack;Localization&rbrack; Disable italic font style for chinese locale
* &lbrack;Localization&rbrack; Localized string split into 2 lines
* &lbrack;Localization&rbrack; Adjust folder name and replace with ellipsis if it's too long
* &lbrack;Localization&rbrack; Format numbers with thousand separator
* &lbrack;Localization&rbrack; Localize date and time display
* &lbrack;Localization&rbrack; Localize color picker on Windows
* &lbrack;Content&rbrack; Transform - With the safe transformation activated, the normal rotates correctly every 45°
* &lbrack;Content&rbrack; Surface relief - Fix tiling issue with perlin fractal noise (advanced noise)
* &lbrack;Content&rbrack; Brickwall Pattern - Height input in 16bit
* &lbrack;Content&rbrack; Material Icon Render - Specular reflections issue
* &lbrack;Content&rbrack; Color Variation - No color shift between color inputs and the result
* &lbrack;Content&rbrack; Color Variation - Performance update

**Known Issues:**

* Usage of Image to Material (AI powered) on high resolution images can be slow
* Content Aware Fill filters are slow in high resolution
* Coma or point can be ignored when typing a specific evalue in a slider
* Impossible to save twice the exact same material layer stack

### 2.3.0 (2020.3.0) Vermicelli

*(Released: October 26, 2020)*

**Added:**

* &lbrack;Image to Material&rbrack; Support of NVIDIA RTX 3000 series
* &lbrack;Image to Material&rbrack; New parameters to control the geometry details
* &lbrack;Image to Material&rbrack; New parameters to control the roughness
* &lbrack;Image to Material&rbrack; New parameters to control the delighting intensity
* &lbrack;Thumbnails&rbrack; New thumbnail generator based on Substance Designer's PBR renderer
* &lbrack;Thumbnails&rbrack; Update base materials and atlases to embed their thumbnail
* &lbrack;Thumbnails&rbrack; Retrieve the thumbnail from the .sbsar file if it exists
* &lbrack;Thumbnails&rbrack; Change thumbnail quality in the Preferences
* &lbrack;Engine&rbrack; Updated to Substance Engine version 8
* &lbrack;Localization&rbrack; Chinese localization
* &lbrack;UI&rbrack; Experimental Spot Colors Picker
* &lbrack;Content&rbrack; New Environment Map - Studio 06
* &lbrack;Content&rbrack; Add Atlas Generator filter
* &lbrack;Content&rbrack; Add Atlas Splitter filter
* &lbrack;Content&rbrack; Add Discarded Gums filter
* &lbrack;Content&rbrack; Add Fingerprints filter
* &lbrack;Content&rbrack; Add Scratches filter
* &lbrack;Content&rbrack; Add Surface Relief filter (replace height modulation filter)
* &lbrack;Content&rbrack; Add Warp filter
* &lbrack;Content&rbrack; Add Invert filter
* &lbrack;Content&rbrack; Add Colorize filter
* &lbrack;Content&rbrack; Add Replace Color fitler
* &lbrack;Content&rbrack; Transform - Add the possibility to deactivate the transformation on a specific channel
* &lbrack;Content&rbrack; Transform - Add rotation when safe transform is activated
* &lbrack;Content&rbrack; Color Variation - Add a segmentation option to choose how to distribute the colors

**Fixed:**

* &lbrack;Layers&rbrack; Properly update UI when doing multiple undo/redo actions
* &lbrack;Layers&rbrack; Prevent crashes when doing multiple undo/redo actions
* &lbrack;Layers&rbrack; Crash when using Image to Material (AI Powered), with log: invalid device ordinal
* &lbrack;Filters&rbrack; Improve NVIDIA graphics card detection for NVidia specific features
* &lbrack;Application&rbrack; Crash when closing the application
* &lbrack;Application&rbrack; Fix VRAM amount detection on MacOS
* &lbrack;Export&rbrack; Some export presets are sometimes missing
* &lbrack;Content&rbrack; Oil Paint Effect - Fix height range with high displacement amplitude
* &lbrack;Content&rbrack; Make It Tile Advanced - No washed out basecolor at export
* &lbrack;Content&rbrack; Make It Tile Advanced - White mask on the basecolor when the AO is too strong
* &lbrack;Content&rbrack; Adjustment - It works now on images (scan1, ...)

**Known Issues:**

* Usage of Image to Material (AI powered) on high resolution images can be slow
* Content Aware Fill filters are slow in high resolution
* Coma or point can be ignored when typing a specific evalue in a slider
* Impossible to save twice the exact same material layer stack

### 2.2.1 (2020.2.1) Udon

*(Released: July 21, 2020)*

**Added:**

* &lbrack;Layers&rbrack; In App Error message when Image to Material (AI-Powered) is out of memory

**Fixed:**

* &lbrack;Layers&rbrack; Image to Material (AI-Powered) does not work with Specular/Glossiness workflows
* &lbrack;Layers&rbrack; Crashes when out of video memory while using Image to Material (AI-Powered)
* &lbrack;Layers&rbrack; Disk cache is not used for display when opening a stack
* &lbrack;Layers&rbrack; Detection of Nvidia RTX 8000
* &lbrack;Layers&rbrack; It is sometimes impossible to move a layer outside a Splatter input
* &lbrack;Layers&rbrack; Disk cache is not used when inserting a stack in a stack
* &lbrack;Layers&rbrack; Some channel usages are computed although they are not used
* &lbrack;Layers&rbrack; Blank outputs are created sometimes when importing images
* &lbrack;2D View&rbrack; Switching to another layer with Draw mode active blocks pan and zoom
* &lbrack;Content&rbrack; Snow - 8bit issue on the normal map
* &lbrack;Content&rbrack; Pavement Pattern - 8 bits issue on the normal map
* &lbrack;Content&rbrack; Equalizer - 8 bits issue on the normal map
* &lbrack;Content&rbrack; Gravel Generator - 8 bits issue on the normal map
* &lbrack;Content&rbrack; Floor Tiles - Handle opacity and specular level
* &lbrack;Content&rbrack; Blender cycles eeve export preset - invert normal map
* &lbrack;Content&rbrack; Correct issue with huge images with Image to Material (AI Powered)
* &lbrack;Application&rbrack; Crash when choosing "Backup and Restart" on database error
* &lbrack;Application&rbrack; Crash when clicking quickly on the same asset
* &lbrack;Application&rbrack; Rare crashes on exit
* &lbrack;Application&rbrack; Crash when dropping files on the Welcome screen
* &lbrack;Application&rbrack; Crash when a corrupted environment file is loaded
* &lbrack;Application&rbrack; Rare crash when rapidly switching rendered asset
* &lbrack;Application&rbrack; Freeze when exiting while an asset is computing
* &lbrack;Application&rbrack; Rare crash on startup on macos
* &lbrack;Application&rbrack; Deadlock when closing the application soon after startup
* &lbrack;Rendering&rbrack; 3D view sometimes flickers
* &lbrack;UI&rbrack; Color picker and random seed widgets are not aligned with the rest of the tweaks
* &lbrack;Rendering&rbrack; Wrong computation time displayed
* &lbrack;Export&rbrack; Some export presets are sometimes missing

**Known Issues:**

* Usage of Image to Material (AI powered) on high resolution images can be slow
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Content Aware Fill filters are slow in high resolution
* Coma or point can be ignored when typing a specific evalue in a slider
* Impossible to save twice the exact same material layer stack

### 2.2.0 (2020.2.0) Udon

*(Released: June 15, 2020)*

**Added:**

* &lbrack;Create&rbrack; New Image to Material (AI powered) filter available on Windows and Linux
* &lbrack;Create&rbrack; Rename Bitmap to Material to Image to Material (B2M)
* &lbrack;Image Import&rbrack; New Material Creation Template Pop-up
* &lbrack;Image Import&rbrack; New "Add a base material" option
* &lbrack;Image Import&rbrack; Be able to drag and drop additional images in the Material Creation Template
* &lbrack;Image Import&rbrack; Be able to remove images in the Material Creation Template
* &lbrack;Image Import&rbrack; Assign channel to imported bitmaps automatically based on their filename
* &lbrack;Image Import&rbrack; Be able to invert normal maps
* &lbrack;2D View&rbrack; Introduction of a painting mode
* &lbrack;2D View&rbrack; The painting tiles
* &lbrack;2D View&rbrack; Set a greyscale value for the brush color
* &lbrack;2D View&rbrack; Pan and zoom while painting
* &lbrack;2D View&rbrack; X shortcut to invert brush greyscale value
* &lbrack;2D View&rbrack; &lbrack; and &rbrack; shortcuts to change the brush size
* &lbrack;2D View&rbrack; Ctrl (or Cmd) + Mouse wheel change the brush size
* &lbrack;2D View&rbrack; It is now possible to modify the source position when using Clone Patch
* &lbrack;Layers&rbrack; Shift + drag and drop to auto scatter atlases
* &lbrack;Layers&rbrack; Alt + drag and drop inserts a material as a decal
* &lbrack;Layers&rbrack; Expose easily transform matrices from Substance Designer
* &lbrack;Layers&rbrack; Dropping textures in a non-empty stack automatically assigns to the correct channels
* &lbrack;Layers&rbrack; New type of layer: Compound Filters
* &lbrack;Parameters&rbrack; Support Substance string inputs
* &lbrack;UI&rbrack; Added drop shadows for popups and menus
* &lbrack;UI&rbrack; New Color Widget with right click options (clear, copy, paste)
* &lbrack;UI&rbrack; New Image Widget with Painting tool option
* &lbrack;UI&rbrack; Be able to paint over an imported image in an image widget
* &lbrack;Rendering&rbrack; New default camera position
* &lbrack;Export&rbrack; Substance files are exported for Substance Designer 2020.1.2 (10.1.2)
* &lbrack;Performance&rbrack; Better application startup time
* &lbrack;Performance&rbrack; Improve asynchronous tasks handling
* &lbrack;Performance&rbrack; Improve layer stack performance when adding, removing or moving layers
* &lbrack;Performance&rbrack; Image to Material (AI powered) runs faster on RTX GPUs
* &lbrack;Content&rbrack; New meshes: Female T-Shirt, Male T-Shirt, Shoe
* &lbrack;Content&rbrack; New Blend Mode - Per Channel Blend
* &lbrack;Content&rbrack; Opacity blend height correction with 2 new parameters (height position and height scale)
* &lbrack;Content&rbrack; Add Height Adjustments in Height Blend mode
* &lbrack;Content&rbrack; Use Height information option in the Custom Mask Blend
* &lbrack;Content&rbrack; New Perspective Correction Tool
* &lbrack;Content&rbrack; Pattern Generator - Add a parameter to invert the pattern
* &lbrack;Content&rbrack; Pattern Generator - Add a new parameter Override Material Details
* &lbrack;Content&rbrack; New Decal filter
* &lbrack;Content&rbrack; New Moss filter
* &lbrack;Content&rbrack; New Cracks filter
* &lbrack;Content&rbrack; New PBR Validate filter
* &lbrack;Content&rbrack; New Floor Tiles filter
* &lbrack;Content&rbrack; New Quilt Stich filter
* &lbrack;Content&rbrack; Atlas Scatter - Add Custom Mask input to enable painting option
* &lbrack;Content&rbrack; Dirt - Add Custom Mask input to enable painting option
* &lbrack;Content&rbrack; CLO export preset
* &lbrack;Content&rbrack; VStitcher export preset
* &lbrack;Content&rbrack; Unity HDRP presets export a detailMap

**Fixed:**

* &lbrack;Layers&rbrack; Imported images are loaded too many times
* &lbrack;Layers&rbrack; Crash when creating a clone patch at the bottom of the stack
* &lbrack;Layers&rbrack; Adding a material at the bottom of the stack makes it unstable
* &lbrack;Layers&rbrack; Filter after image import works improperly
* &lbrack;Layers&rbrack; workflow_type value is not updated when switching the workflow between projects with a custom filter
* &lbrack;Layers&rbrack; Disable "remove layer" button when no layer is selected
* &lbrack;Layers&rbrack; Crash when loading an asset containing a Clone Patch
* &lbrack;Layers&rbrack; Normal to Height filter crashes on MacOs
* &lbrack;Application&rbrack; Crash when loading back and forth environment maps
* &lbrack;Application&rbrack; Performance issues when some graphics tablet driver is installed
* &lbrack;Application&rbrack; EXR 32 bits files import are black
* &lbrack;Application&rbrack; Crashes when loading and unloading assets
* &lbrack;Application&rbrack; Crash when switching from explore to create
* &lbrack;Application&rbrack; Target collection when saving a material is not from current project
* &lbrack;Application&rbrack; Fix backup and restart
* &lbrack;Image Import&rbrack; Properly import grayscale images
* &lbrack;Content&rbrack; New filters for new matrix handling
* &lbrack;Content&rbrack; Imported custom filters are visible in the quick access bar
* &lbrack;Content&rbrack; Fix color shift with the Make it tile advanced filter
* &lbrack;Performance&rbrack; Opening a color dialog is slow and recomputes the current layer
* &lbrack;UI&rbrack; Keyboard shortcuts sometimes don't work
* &lbrack;2D View&rbrack; Content Aware Fill needs a useless first click to work
* &lbrack;Resources&rbrack; Folders in local disks are still watched for updates after removing them
* &lbrack;Resources&rbrack; Deleting a linked folder from filesystem doesn't remove it
* &lbrack;Export&rbrack; Custom usages in custom export presets are not exported
* &lbrack;Export&rbrack; Exporting .sbsar file with special characters in path fails

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

* &lbrack;Project&rbrack; Export and import metadata
* &lbrack;Application&rbrack; Ctrl+S now saves a preset in Explore
* &lbrack;Performance&rbrack; Use render cache instead of recomputing saved materials for resolutions up to 2k

**Fixed:**

* &lbrack;UI&rbrack; Fixed computing indicator in the viewport
* &lbrack;UI&rbrack; Entering Negative values in sliders is fixed
* &lbrack;UI&rbrack; Combo boxes: keyboard arrows and scrollbar now work
* &lbrack;UI&rbrack; Keep the selected channel when switching between "Material Outputs" and "Layer Inputs" in the 2D view
* &lbrack;Layers&rbrack; Fixed crash when adding custom channels in Base Material
* &lbrack;Layers&rbrack; Crash when manipulating layers
* &lbrack;Layers&rbrack; Custom channels are not displayed with a saved material
* &lbrack;Application&rbrack; Fixed rare crash when importing an asset
* &lbrack;Application&rbrack; Crash on exit
* &lbrack;Application&rbrack; Combo boxes now show correct values when switching presets
* &lbrack;Export&rbrack; Renamed Enscape preset to Enscape Revit
* &lbrack;Export&rbrack; Importing an export preset after removing it works
* &lbrack;Export&rbrack; Crash at export
* &lbrack;Rendering&rbrack; Fixed rendering when the base color is in 16bit half float format
* &lbrack;Project&rbrack; Do not crash when importing corrupted package
* &lbrack;Project&rbrack; Handle 2019.1.4 to 2.x.x migration when Create has never been opened
* &lbrack;Project&rbrack; Fix a crash when importing the same project twice
* &lbrack;Project&rbrack; Fix a crash when importing projects
* &lbrack;Resources&rbrack; Custom filters imported in previous versions work
* &lbrack;Resources&rbrack; Materials with the same name no longer erase each other
* &lbrack;Resources&rbrack; Crash when linking a local folder
* &lbrack;Resources&rbrack; Starter Materials user-created folders are no longer removed after a restart
* &lbrack;Inspire&rbrack; Fix material/collection drop area and add a warning message if using an unsaved material

**Known Issues:**

* Content Aware Fill filters are slow in high resolution
* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Coma or point can be ignored when typing a specific evalue in a slider

### 2.1.0 (2020.1.0) Tiramisu

*(Released: March 12, 2020)*

**Added:**

* &lbrack;Export&rbrack; Export preset selction to pack your textures for renderers and game engines
* &lbrack;Export&rbrack; Export preset to Unreal Engine 4
* &lbrack;Export&rbrack; Export preset to Unity Standard
* &lbrack;Export&rbrack; Export preset to Unity HDRP
* &lbrack;Export&rbrack; Export preset to Blender Cycles/Eevee
* &lbrack;Export&rbrack; Export preset to Arnold 5
* &lbrack;Export&rbrack; Export preset to Corona Renderer
* &lbrack;Export&rbrack; Export preset to Enscape
* &lbrack;Export&rbrack; Export preset to Keyshot 9
* &lbrack;Export&rbrack; Export preset to Redshift
* &lbrack;Export&rbrack; Export preset to Vray Next
* &lbrack;Export&rbrack; Export preset to Lens Studio
* &lbrack;Export&rbrack; Export preset to Spark AR Studio
* &lbrack;Export&rbrack; Export preset to PBR Specular Glossiness from PBR Metallic Roughness
* &lbrack;Export&rbrack; New export UI
* &lbrack;Export&rbrack; Remember Export settings
* &lbrack;Export&rbrack; Import and manage your custom export presets
* &lbrack;Export&rbrack; Delete and replace your custom export presets
* &lbrack;Export&rbrack; Rename your custom export presets
* &lbrack;Export&rbrack; Set the default export resolution to the current resolution
* &lbrack;Export&rbrack; Add the choice to create a subfolder to the export location
* &lbrack;Export&rbrack; Warning message before replacing existing files
* &lbrack;Application&rbrack; New version numbering scheme
* &lbrack;Application&rbrack; Open Create at launch, and change labs order
* &lbrack;Welcome Screen&rbrack; New welcome banner
* &lbrack;Project&rbrack; Open last project at launch
* &lbrack;UI&rbrack; New combo box style
* &lbrack;2D view&rbrack; F shortcut to focus in the 2d view
* &lbrack;Filters&rbrack; Added support for alchemist::parameterVisibility tag in Substance graphs
* &lbrack;Filters&rbrack; Have a global tweak to manage parameter visibility based on your workflow
* &lbrack;Resources&rbrack; New command line option to setup resources and linked folders with a configuration file
* &lbrack;Version checker&rbrack; Configuration of the version check
* &lbrack;Content&rbrack; New starter materials
* &lbrack;Content&rbrack; Bitmap to Material - Add the possibility to define the metallic channel (uniform, custom image import, color picking)
* &lbrack;Content&rbrack; Adjustment - Add the support of the PBR specular/glossiness workflow
* &lbrack;Content&rbrack; Atlas Scatter - New parameters

**Fixed:**

* &lbrack;Project&rbrack; Crash when importing the same project twice
* &lbrack;Project&rbrack; Fixed crash when importing and opening projects several times
* &lbrack;Application&rbrack; Crash when loading an unnamed material
* &lbrack;Application&rbrack; Recognize missing files when re-importing them
* &lbrack;Application&rbrack; Fix random crash on shutdown
* &lbrack;Application&rbrack; Fixed rare crash when unloading an material in Create
* &lbrack;Application&rbrack; Fixed random crash when using UI controls
* &lbrack;Application&rbrack; Fixed export of log files to the Desktop on Windows 10
* &lbrack;UI&rbrack; Export panel has the wrong size when you open it in Create
* &lbrack;UI&rbrack; Open project with a single click
* &lbrack;UI&rbrack; Correctly set minimum and maximum slider values
* &lbrack;UI&rbrack; Show label of the channel usages instead of ids
* &lbrack;UI&rbrack; Clicking a material always opens/closes the tweak panel
* &lbrack;UI&rbrack; Fix hidden layers colors
* &lbrack;UI&rbrack; Welcome Screen buttons improvements
* &lbrack;Layers&rbrack; Less unnecessary recomputes
* &lbrack;Layers&rbrack; Crashes when using Clone Patch
* &lbrack;Layers&rbrack; Selecting an image import layer no longer triggers a compute
* &lbrack;Layers&rbrack; Clone Patch and Content Aware Fill layers no longer recompute when selected
* &lbrack;Channel settings&rbrack; Enabling or disabling usages now trigger a rendering
* &lbrack;Resources&rbrack; Prevent freeze when mass clicking on a stack in the library
* &lbrack;Resources&rbrack; Performance hit when re-adding a previously added linked folder
* &lbrack;Resources&rbrack; Fixed a crash when trying to open a deleted .sbsar file
* &lbrack;Performance&rbrack; Avoid loading materials to access their parameters
* &lbrack;Performance&rbrack; Backup assets only when used in a project or in an authored material
* &lbrack;Export&rbrack; Fixed materials in export queue sometimes skipped or exported with wrong parameters
* &lbrack;2D View&rbrack; Restored pan and zoom
* &lbrack;Content&rbrack; Parquet Pattern takes into account the Ambient Occlusion channel
* &lbrack;Content&rbrack; Paint - Display mask input when enabling custom mask
* &lbrack;Content&rbrack; Stonewall Pattern - Remove possible banding effects in the normal map
* &lbrack;Content&rbrack; Height Modulation - Correct double base color entries in the 2d view

**Known Issues:**

* Content Aware Fill filters are slow in high resolution
* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Coma or point can be ignored when typing a specific evalue in a slider

## Version 1

### 1.1.4 (2019.1.4) Sesame

*(Released: January 30, 2020)*

**Added:**

* &lbrack;Resources&rbrack; Confirmation prompt when clearing a resources folder

**Fixed:**

* &lbrack;Layers&rbrack; Move layers to two and more layers below or above
* &lbrack;Create&rbrack; Allocation of enough VRAM budget to have good performances

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

* &lbrack;Workflow&rbrack; Support of multiple workflows
* &lbrack;Workflow&rbrack; Support of PBR Specular Glossiness workflow
* &lbrack;Workflow&rbrack; New Channel Settings panel
* &lbrack;Workflow&rbrack; Workflow selection at project creation
* &lbrack;Channel Settings&rbrack; Activate/Deactivate specific channel computation
* &lbrack;Channel Settings&rbrack; Display list of custom channels available in the current material
* &lbrack;Channel Settings&rbrack; Automatic computation of custom channels when required
* &lbrack;Channel Settings&rbrack; Force/Block computation of custom channels
* &lbrack;Layers&rbrack; New UI of material input placeholder in Atlas Scatter and Splatter filters
* &lbrack;Layers&rbrack; Image Input parameter of a filter can be fed by underneath layers
* &lbrack;Layers&rbrack; Display a notification when some layers are out of date
* &lbrack;Layers&rbrack; Possibility to update to the latest version of outdated layers via the notification
* &lbrack;Project&rbrack; New metadata fields at project creation
* &lbrack;Inspire&rbrack; Generated variations are specific to a project
* &lbrack;2D View&rbrack; Switch between the Layer inputs, layer outputs, and the material outputs
* &lbrack;Welcome Screen&rbrack; Add Import project (.alch) option
* &lbrack;Preferences&rbrack; New Preferences window to set cache location and analytics privacy settings
* &lbrack;UI&rbrack; New UI buttons
* &lbrack;Performance&rbrack; Overall improvement of the parallelization system
* &lbrack;Performance&rbrack; Optimization of the number of material computes
* &lbrack;Engine&rbrack; Substance Engine update
* &lbrack;Framework&rbrack; Upgrade to Qt 5.13
* &lbrack;MacOS&rbrack; Global improvements of macOS Catalina support
* &lbrack;Content&rbrack; Adjustment filter - Normal intensity and invert parameters

**Fixed:**

* &lbrack;Layers&rbrack; Unset Image Input parameter when deleting the layer
* &lbrack;Layers&rbrack; Fix a crash when adding a clone patch layer
* &lbrack;Layers&rbrack; Fix some crashes when blending layers stack materials in other layer stack materials
* &lbrack;Export&rbrack; Channels selection for export is now respected
* &lbrack;Resources&rbrack; Do not crash when navigating in the Resources panel
* &lbrack;Resources&rbrack; Fix crash when importing corrupted Substance files
* &lbrack;Resources&rbrack; Reduce the number of crashes when loading large folders
* &lbrack;Thumbnail&rbrack; Thumbnail computation doesn't freeze the interface
* &lbrack;Image Import&rbrack; Uniformization of image type supported across the application
* &lbrack;Preset&rbrack; Save the description when creating a preset from an SBSAR
* &lbrack;Inspire&rbrack; Fix image drag and drop
* &lbrack;Application&rbrack; Fix crashes at exit
* &lbrack;Application&rbrack; Fix crashes at the exit when exporting materials
* &lbrack;UI&rbrack; Fixes and improvements
* &lbrack;UI&rbrack; Rename temporary asset to "unsaved material"
* &lbrack;Content&rbrack; Global update and cleaning of all filters

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

* &lbrack;Layers&rbrack; Save and Save as options are accessible via the interface in the layers stack toolbar
* &lbrack;Resources&rbrack; Clearer breadcrumb in the Resources panel to navigate through folders
* &lbrack;Resources&rbrack; Maintain back button pressed to access all upper folders
* &lbrack;Resources&rbrack; Add reload of imported materials option to update them to the latest version
* &lbrack;Layers&rbrack; Possibility to change the image in the Image import layer
* &lbrack;Layers&rbrack; Possibility to define an image as a channel (base color, normal, height,...) in the Image import layer
* &lbrack;Content&rbrack; New Atlas Scatter filter to scatter new atlas elements from Substance Source
* &lbrack;Content&rbrack; New Oil Paint Effect filter
* &lbrack;Content&rbrack; New Channels Generation filter to generate height, ambient occlusion and roughness from base color and normal maps

**Fixed:**

* &lbrack;UI&rbrack; Reactivate tooltips on Layers stack toolbar
* &lbrack;UI&rbrack; Fix issue when typing two decimals in a slider value
* &lbrack;Performance&rbrack; Fix crash when switching quickly between materials
* &lbrack;Export&rbrack; Switching to another material before the end of an export does not crash anymore
* &lbrack;Resources&rbrack; Context menu is displayed on top of the material when you right-click on it
* &lbrack;Layers&rbrack; The 'Click here' link is working when the layer stack is empty
* &lbrack;Presets&rbrack; Remove save button in the tweak panel when it's a material created in Alchemist
* &lbrack;Tweak&rbrack; Information message displayed when it's a material created in Alchemist
* &lbrack;Viewport&rbrack; Default value of Specular Level texture is corrected to 0.04
* &lbrack;File Menu&rbrack; Fix and rename Save and Save as option
* &lbrack;Engine&rbrack; Update Substance engine version to avoid crash of some SBSAR files during import.
* &lbrack;Content&rbrack; Tiling filter is working on the ambient occlusion channel
* &lbrack;Content&rbrack; Crop filter is working on the ambient occlusion channel
* &lbrack;Content&rbrack; Water filter modifies gain the height map
* &lbrack;Content&rbrack; Correct tiling of the top material in the opacity blend mode
* &lbrack;Content&rbrack; Height of the top material is preserved in the opacity blend mode
* &lbrack;Content&rbrack; Possible to add a custom mask, custom pattern or a scale map in the Perforation filter
* &lbrack;Content&rbrack; Height Modulation filter forces height and normal maps in 16 bits
* &lbrack;Content&rbrack; Adjustment filter forces height and normal maps in 16 bits

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

* &lbrack;Blend&rbrack; New opacity Blend mode
* &lbrack;Engine&rbrack; New Substance Engine version

**Fixed:**

* &lbrack;Layers&rbrack; Fix crash while deleting a layer that is still computing
* &lbrack;Layers&rbrack; Fix crash while removing the bottom layer
* &lbrack;Layers&rbrack; Fix crash while the material name contains special characters
* &lbrack;Layers&rbrack; Stop computing every filters that use a widget
* &lbrack;Layers&rbrack; Avoid crash while using Clone Patch and Content Aware Fill filters
* &lbrack;Layers&rbrack; Fix crash while drag and droping a filter in a splatter input slots
* &lbrack;Resources&rbrack; Fix crash while linking local folders or importing resources in Substance Alchemist
* &lbrack;Collection&rbrack; Fix crash while switching rapidly between materials
* &lbrack;UI&rbrack; Fix crash while value is null or not valid in tiling, displacement sliders on the viewport
* &lbrack;Inspire&rbrack; Fix crash while accessing the Inspire tab
* &lbrack;Inspire&rbrack; Fix crash while inspiring on a just saved layers stack material
* &lbrack;Performance&rbrack; Heavy Substance materials and Filters (Tiling) compute faster
* &lbrack;Help&rbrack; Fix export log file
* &lbrack;Content&rbrack; Randomizer filter works on all channels
* &lbrack;Content&rbrack; Multiangle workflow takes all scans into account
* &lbrack;Content&rbrack; AO Blend correct blending
* &lbrack;Content&rbrack; Curvature Blend correct blending
* &lbrack;Content&rbrack; Color ID Blend correct blending
* &lbrack;Content&rbrack; Custom Mask Blend correct blending
* &lbrack;Content&rbrack; Fix Adjustment filter for roughness modification
* &lbrack;Content&rbrack; Fix Base Material filter for custom normal channels upload
* &lbrack;Content&rbrack; Fix Custom Import pattern of the Embossing filter

**Known Issues:**

* Use of multiple delighters in one material is not recommended
* Delighter crashes with older NVIDIA drivers (Less than 400.x)
* Coma or point can be ignored when typing a specific value in a slider
* Normal to Height filter can crash on MacOS

### 1.1.0 (2019.1.0) Sesame

*(Released: November 04, 2019)*

**Added:**

* &lbrack;Project&rbrack; Creation of a project
* &lbrack;Project&rbrack; Introduction of the .alch file format that contains project data
* &lbrack;Project&rbrack; Export a .alch project containing the collections and their materials
* &lbrack;Project&rbrack; Import a .alch project
* &lbrack;Project&rbrack; Open recent projects
* &lbrack;Welcome Screen&rbrack; A welcome screen is displayed at the launch
* &lbrack;Welcome Screen&rbrack; Create a project from the welcome screen
* &lbrack;Welcome Screen&rbrack; Access the list of all your projects in the welcome screen
* &lbrack;Welcome Screen&rbrack; Quick links to access the documentation, the about popup and license management
* &lbrack;File Menu&rbrack; Integration of a file Menu
* &lbrack;File Menu&rbrack; Access the project commands from the File tab and the save of the layer stack
* &lbrack;File Menu&rbrack; Access the undo and redo commands from the Edit tab
* &lbrack;File Menu&rbrack; The previous help menu moved in the file menu under the Help tab
* &lbrack;Layers&rbrack; New architecture of the layer stack
* &lbrack;Layers&rbrack; New UI of the layer stack
* &lbrack;Layers&rbrack; Select the blend mode directly on the toolbar
* &lbrack;Layers&rbrack; Access separately the blend parameters and the material parameters
* &lbrack;Layers&rbrack; Add materials directly in dedicated inputs of the Splatter filter in the layer stack
* &lbrack;Layers&rbrack; Change scan order directly in the Image import layer
* &lbrack;Viewport&rbrack; Control of the camera field of view
* &lbrack;Viewport&rbrack; Possibility to switch between orthographic or perspective camera
* &lbrack;Viewport&rbrack; Display resolution and bit depth information for each channel
* &lbrack;Resources&rbrack; Base Materials is opened per default
* &lbrack;Cache&rbrack; Locate your thumbnail cache folder
* &lbrack;Cache&rbrack; Locate your render cache folder
* &lbrack;Panels&rbrack; Material Settings panel is temporarily hidden
* &lbrack;Workflow&rbrack; Specular/Glossiness temporarily deactivated
* &lbrack;MacOS&rbrack; Catalina OS version notarization
* &lbrack;Content&rbrack; New version of the Delighter filter
* &lbrack;Content&rbrack; New Image Content Aware Fill filter
* &lbrack;Content&rbrack; New Material Content Aware Fill filter
* &lbrack;Content&rbrack; Transform filter has a safe transform option

**Fixed:**

* All previous bugs related to Create are invalid today with new UI and architecture release
* Tooltips don't hide the icons in the top bar (3D, 2D, 2D/3D)
* &lbrack;Content&rbrack; Splatter filter accepts Atlas with complete height map
* &lbrack;Content&rbrack; Transform filter works on images (scan1, scan2,...)

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

* &lbrack;Create&rbrack; Some filters were listed in the quick accessor but not in the filter panel
* &lbrack;MacOS&rbrack; Fixed some crashes at exit

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

* &lbrack;Resources&rbrack; Connect and mirror your material folders on your local disks
* &lbrack;Resources&rbrack; Browse your materials folders and their subfolders
* &lbrack;Resources&rbrack; Detach your material resources panel in a separate window to see your resources in full screen
* &lbrack;Resources&rbrack; New Resources panel Layout to support folders and subfolders navigation
* &lbrack;Resources&rbrack; Use the breadcrum to navigate through your folders
* &lbrack;Resources&rbrack; Force the synchronization of your local folder with the Sync option accessible via righ-click
* &lbrack;Resources&rbrack; Disconnect your local folder with the Disconnect option accessible via righ-click
* &lbrack;Manage&rbrack; Display embedded tags of Substance files
* &lbrack;Manage&rbrack; Add, edit and delete tags of your materials
* &lbrack;Manage&rbrack; Rate your materials
* &lbrack;Layers&rbrack; Support Panorama output
* &lbrack;Layers&rbrack; You can delete Image inputs in the Image Import layer
* &lbrack;Layers&rbrack; Automatic selection of the new added layer
* &lbrack;Layers&rbrack; Automatic selection of the layer below after a layer deletion
* &lbrack;UX&rbrack; Keep left panels visibility when switching to another Lab
* &lbrack;UX&rbrack; Do not create a base layer or open the Material Workflow popup when importing images in a non-empty layers stack
* &lbrack;UI&rbrack; New Textfield style
* &lbrack;UI&rbrack; New SearchBox style
* &lbrack;UI&rbrack; New Panel header style
* &lbrack;UI&rbrack; New Busy indicator style
* &lbrack;UI&rbrack; New Layers stack background style
* &lbrack;UI&rbrack; Use Adobe Clean font
* &lbrack;UI&rbrack; Remove eyedropper icon placeholder of color input parameter
* &lbrack;Performance&rbrack; Busy indicator optimization
* &lbrack;Content&rbrack; New Pattern Generator filter
* &lbrack;Content&rbrack; New Blur filter

**Fixed:**

* &lbrack;Inspire&rbrack; Fix crash when using more than 10 colors
* &lbrack;2D View&rbrack; Fix scrollbar on the channel list of the 2D view
* &lbrack;Viewer&rbrack; Fix crash when importing a non power of 2 environment map
* &lbrack;Content&rbrack; Fix PNG import for custom pattern of Embossing and Perforation filters
* &lbrack;Export&rbrack; Fix normal and height 16 bits per channel export
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

* &lbrack;Filters&rbrack; Access quickly to your filters by pressing the space bar
* &lbrack;Filters&rbrack; New dedicated panel to manage, browse and import your filters
* &lbrack;Metadata&rbrack; Right click on a material to see its metadata
* &lbrack;Metadata&rbrack; Right click on a material to see its location on your disk
* &lbrack;Sliders&rbrack; Animate sliders when you hover them by pressing Ctrl
* &lbrack;Sliders&rbrack; Stop and restart your sliders animation by pressing P
* &lbrack;Export&rbrack; SBSAR export follows Substance Source guidelines
* &lbrack;License&rbrack; Activate Substance Alchemist using an environment variable
* &lbrack;UX&rbrack; File dialog remembers the last file path selected
* &lbrack;UX&rbrack; Folder dialog remembers the last folder path selected
* &lbrack;UI&rbrack; Update Resources panel UI
* &lbrack;UI&rbrack; Update Search bar UI
* &lbrack;UI&rbrack; Create New material icon is updated
* &lbrack;Help&rbrack; URLs are updated to substance3d.com domain
* &lbrack;Mesh&rbrack; A Cloth mesh is now available
* &lbrack;Content&rbrack; New Corrosion Filter
* &lbrack;Content&rbrack; New Oxydation Filter
* &lbrack;Content&rbrack; New Moss Filter
* &lbrack;Content&rbrack; New Dust Filter
* &lbrack;Content&rbrack; New Brickwall pattern Filter
* &lbrack;Content&rbrack; New Stonewall pattern Filter
* &lbrack;Content&rbrack; New Wood Finish Filter
* &lbrack;Content&rbrack; New Metal Finish Filter
* &lbrack;Content&rbrack; New Snow Filter
* &lbrack;Content&rbrack; New Randomizer Filter
* &lbrack;Content&rbrack; You can now import your textures directly in the Base Material filter

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

* &lbrack;Engine&rbrack; Substance Engine update to be compatible with the latest Substance Designer version
* &lbrack;License&rbrack; Update license folder for first installations
* &lbrack;Layers&rbrack; Reload at any time your layer stack to update your custom filters

**Fixed:**

* &lbrack;Data Compatibility&rbrack; Preventive fix to limit data corruption at upgrade time

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

* &lbrack;Metadata&rbrack; See and fill materials metadata in a dedicated tab
* &lbrack;Collection&rbrack; Create a collection directly from the search results
* &lbrack;Media Publishing&rbrack; Export a board of a collection
* &lbrack;UX&rbrack; Undo a tweak change or image import by pressing Ctrl+Z
* &lbrack;UX&rbrack; Redo a tweak change or image import by pressing Ctrl+Shift+Z
* &lbrack;UI&rbrack; New icons with a new style
* &lbrack;Performance&rbrack; New Session manager to better handle the tabs switching
* &lbrack;Performance&rbrack; Faster opening of the Image Import layer
* &lbrack;Content&rbrack; New Metal generic material
* &lbrack;Content&rbrack; New Rust material
* &lbrack;Content&rbrack; New Stone generic material
* &lbrack;Content&rbrack; Embossing filter update
* &lbrack;Content&rbrack; Embroidery filter update
* &lbrack;Content&rbrack; Paint filter update
* &lbrack;Content&rbrack; Delighter filter update

**Fixed:**

* &lbrack;Content&rbrack; Water filter is working in the Specular/Glossiness workflow
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

* &lbrack;Stack&rbrack; Crash when removing a splatter layer
* &lbrack;Data&rbrack; Asset database gets corrupted when application crashes
* &lbrack;Data&rbrack; Substance Alchemist cannot start when the asset database is corrupted
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
* &lbrack;UI&rbrack; Clone Tool new UI with brush size visualization
* &lbrack;UI&rbrack; Select and delete hidden stages
* &lbrack;UI&rbrack; New Textfield UI
* &lbrack;Help&rbrack; Access Substance Source, Substance Share and Substance academy websites
* &lbrack;Content&rbrack; New default materials with generators and atlas
* &lbrack;Content&rbrack; Bitmap to Material Update
* &lbrack;Content&rbrack; Dirt Update
* &lbrack;Content&rbrack; Rust Update
* &lbrack;Content&rbrack; New Embossing filter
* &lbrack;Content&rbrack; New Embroidery filter
* &lbrack;Content&rbrack; New Erode filter
* &lbrack;Content&rbrack; New Gravel Generator
* &lbrack;Content&rbrack; New Paint filter
* &lbrack;Content&rbrack; New Parquet Pattern filter
* &lbrack;Content&rbrack; New Pavement Pattern filter
* &lbrack;Content&rbrack; New Perforation filter
* &lbrack;Content&rbrack; New Splatter filter
* &lbrack;Content&rbrack; New Textile Wear filter
* &lbrack;Content&rbrack; New Transform filter

**Fixed:**

* &lbrack;Viewport&rbrack; Sphere mesh with tiling x2 on X
* &lbrack;Viewport&rbrack; Crash when loading your own environment
* &lbrack;Viewport&rbrack; Environment map are now using the exposure value too
* &lbrack;Viewport&rbrack; F shortcut doesn't reset camera angle
* &lbrack;Export&rbrack; SBS export works with latest Substance Designer 2018.3.3
* &lbrack;Export&rbrack; SBSAR export respects the same guidelines as Substance Source materials
* &lbrack;UI&rbrack; Scrollbars can be dragged
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

* &lbrack;Layer stack&rbrack; Layer re-ordering
* &lbrack;Layer stack&rbrack; Delete an hidden layer
* &lbrack;Layer stack&rbrack; Import a material directly at the position of your choice
* &lbrack;Layer stack&rbrack; Material input as a new filter parameter type
* &lbrack;Performance&rbrack; Substance Engine budget is dynamic for better performances
* &lbrack;Performance&rbrack; Better OpenGL performances especially on MacOS
* &lbrack;Data&rbrack; Faster data upgrade after a new version is released
* &lbrack;Content&rbrack; AI Delighter available on Windows 7 and Windows 8
* &lbrack;Content&rbrack; AI Delighter available on RTX GPU

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

* &lbrack;Export&rbrack; Substance archive (sbsar) export of your collection
* &lbrack;Export&rbrack; Substance file (sbs) export of your collection
* &lbrack;Export&rbrack; Export queue visible in the Export panel
* &lbrack;Export&rbrack; Name your collection or material before export
* &lbrack;Data&rbrack; Save As your material by pressing Ctrl+Shift+S
* &lbrack;Data&rbrack; Save your material by pressing Ctrl+S
* &lbrack;Data&rbrack; Collections and Materials are compatible across versions
* &lbrack;Data&rbrack; Update your material layer stack with up-to-date filters
* &lbrack;Data&rbrack; Hot reload of imported custom filters
* &lbrack;UI&rbrack; Visual feedback in the viewport while it's computing
* &lbrack;UI&rbrack; New button style
* &lbrack;UI&rbrack; Save pop-up displays the name of the active collection
* &lbrack;UI&rbrack; Modify source images of an Image(s) Import Layer
* &lbrack;Content&rbrack; Custom usages are now supported
* &lbrack;Content&rbrack; More images format are supported in image input parameters
* &lbrack;Content&rbrack; New Tiling Filter named Make It Tile Advanced
* &lbrack;Content&rbrack; Update of the Water filter

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

* &lbrack;Export&rbrack; New Export pop-up
* &lbrack;Export&rbrack; Export an entire collection
* &lbrack;Export&rbrack; Export Bitmaps at the format of your choice
* &lbrack;Export&rbrack; Export Bitmaps at the resolution of your choice
* &lbrack;Export&rbrack; Export only the channels of your choice
* &lbrack;Export&rbrack; Preview the estimation size of your export
* &lbrack;Export&rbrack; Preview the available size on your disk before exporting
* &lbrack;UX&rbrack; Actions on collection accessible using right-click
* &lbrack;UX&rbrack; Allow to unset an image or an asset in Inspire
* &lbrack;UX&rbrack; Substance Alchemist is launched maximized
* &lbrack;Assets&rbrack; New way of saving your materials in order to keep them persistent with next versions
* &lbrack;Help&rbrack; Access to the online documentation via the help menu
* &lbrack;Performance&rbrack; Faster color variations on complex materials created with Substance Alchemist
* &lbrack;Performance&rbrack; Reduce memory leaks when switching Labs
* &lbrack;Content&rbrack; Scale checker to diagnostic the physical size of your material
* &lbrack;Content&rbrack; Update Italien Venice Mosaic tile material
* &lbrack;Content&rbrack; Update Moss splatter

**Fixed:**

* No more default name when saving a material
* Filters parameters are lost after saving a material and reopening Substance Alchemist
* &lbrack;Content&rbrack; Fix from bottom and from top logic for AO and curvature blending

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
* &lbrack;Log&rbrack; Export log file via the help menu
* &lbrack;UI&rbrack;New Sliders Style
* &lbrack;UI&rbrack;Presets and Tweak panels are merged
* &lbrack;UI&rbrack;New Thumbnails style
* Displacement, Tiling and Shadows settings accessible directly in the viewport
* &lbrack;Content&rbrack; New Default Materials
* &lbrack;Content&rbrack; Moss Splatter update
* &lbrack;Framework&rbrack; Update Substance Engine Framework

**Fixed:**

* Deletion of your layer stack by switching Labs is fixed
* Loading time values displayed in the viewport are correct
* Material workflow default channels are correctly initialized
* Disable Custom Mesh Import
* Bitmap export
* &lbrack;MacOS&rbrack; Closing Substance Alchemist can need a "Force to quit"

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
* &lbrack;MacOS&rbrack; Substance Alchemist can be set in full screen
* &lbrack;Filter&rbrack; Import Custom mask to manage the blending between two materials
* &lbrack;Filter&rbrack; Control Moss scale
* &lbrack;Filter&rbrack; Clone Patch update

**Fixed:**

* Add an image in an image input in the parameter list updates outputs
* Import Custom filter doesn't add a black Ambient Occlusion and a black opacity

**Known Issues:**

* Materials created with a previous version won't be available in the new one.
* &lbrack;MacOS&rbrack; Closing Substance Alchemist can need a "Force to quit"
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