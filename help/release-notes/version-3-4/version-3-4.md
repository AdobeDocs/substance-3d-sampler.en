---
title: "Version 3.4"
description: ""
helpx_description: "Sampler > Release Notes > Version 3.4"
---

# Version 3.4

**Substance 3D Sampler 3.4.0** introduces a series of new features designed to boost speed and quality in 3D workflows.

*Release date: 6 September, 2022*

## Major features

## Exposed Parameters

Modify parametric materials within any software that supports SBSAR files, such as CLO, UE5, Blender, Photoshop, and Illustrator, among others.   
This is now possible thanks to Sampler’s new ability to expose asset parameters, allowing you to speed iterations and get rid of goings and comings between Sampler and others softwares.

Expose the parameters of your material by just clicking on a pin.

Color dots will help you navigate into your exposed parameters and your different panels.

## Python Authoring

You can now create plugins and scripts, this gives you the ability to customize your interface, making it easy to integrate Sampler into your pipeline, and to set up your workflow overall, in any way you wish.   
This could allow you, for instance, to create a script allowing you to automate repetitive tasks as exporting multiple materials in one click.

Discover how to create your first plugin or script [here](../../scripting-and-development/scripting-and-development.md).

## CLO Physical Properties

You can now create textiles which behave realistically with physics simulations. This is achieved by inputting physical properties of the fabric, such as Bending, Shear, and Friction.   
With this update, the SBSAR will contain the physics information in it's metadata, which are used by CLO to ensure that the material react realistically.

## Image to Material (AI Powered)

Image to Material (AI Powered) is now available on MacOS and runs natively on Apple Silicon devices.

## Release Notes

### 3.4.0 Arancini

*(Release date: 6 September, 2022)*

**Added:**

&#91;Exposed Parameters&#93; New Exposed Parameters panel   
&#91;Exposed Parameters&#93; New button on parameters hover to expose and unexpose parameters from Properties panel   
&#91;Exposed Parameters&#93; New right-click context menu on parameters to expose and unexpose parameters from Properties panel   
&#91;Exposed Parameters&#93; Exposed parameters are listed in the Exposed Parameters panel   
&#91;Exposed Parameters&#93; Color dots and color discs are added in several places to easily identify exposed parameters   
&#91;Exposed Parameters&#93; Parameter labels can be edited in the Exposed Parameters panel   
&#91;Exposed Parameters&#93; Display a warning for non-exportable parameters   
&#91;Exposed Parameters&#93; Display warning if moving a layer with exposed blend parameters somewhere where they become hidden   
&#91;Exposed Parameters&#93; Exposed parameters are exported in SBS and SBSAR formats   
&#91;Metadata&#93; Support Custom Metadata templates   
&#91;Metadata&#93; New CLO Physical properties metadata template   
&#91;Metadata&#93; Add icons on hover to add/remove custom metadata   
&#91;Python API&#93; New Python API   
&#91;Python API&#93; API for Asset authoring   
&#91;Python API&#93; API for Layers management   
&#91;Python API&#93; API for Parameters management   
&#91;Python API&#93; API for Project management   
&#91;Python API&#93; A plugin can be enabled and disabled   
&#91;Python API&#93; Python API documentation accessible in the Help menu   
&#91;Scripting&#93; New Plugins and Scripts section in the Preferences popup   
&#91;Scripting&#93; Create and import plugins to customize Sampler interface with your own panels   
&#91;Scripting&#93; Plugins become part of the Sampler interface and can be docked and moved around like standard Sampler panels   
&#91;Scripting&#93; Dedicated button bar for the plugins on the Sampler right toolbar   
&#91;Scripting&#93; Create and import scripts to perform a list of given tasks   
&#91;Scripting&#93; Launch Python scripts via Scripts menu   
&#91;Scripting&#93; Plugins and Scripts can be deleted, re-ordered, and reloaded from the Preferences window   
&#91;Scripting&#93; Added --run-script command line parameters   
&#91;Logs&#93; New Logs panel   
&#91;Logs&#93; Enable Logs panel from the Preferences window   
&#91;Logs&#93; New action bar to clear, copy/paste, export logs   
&#91;Properties&#93; New button on parameters hover to reset parameter value   
&#91;Properties&#93; New right-click context menu on parameters to reset parameter value   
&#91;Content&#93; Image to Material (AI Powered) now works on MacOS   
&#91;Engine&#93; Update Substance engine to v8.6.0   
  
**Fixed:**

&#91;Application&#93; Application could crash at exit when a thumbnail generation was in progress   
&#91;Application&#93; Application might crash when using 'Save as' at exit   
&#91;Application&#93; Application might hang during shutdown on MacOS   
&#91;Application&#93; Saving with the color dialog open doesn't save its changes   
&#91;Export&#93; Usage naming convention is not correct when exporting   
&#91;Layers&#93; Dropping a material on top of a filter could crash   
&#91;Layers&#93; Updating an outdated layer stack could update unrelated layer stacks   
&#91;Metadata&#93; Empty fields are exported   
&#91;Metadata&#93; When there is only one metadata item, the UI lets you try to reorder it   
&#91;Project&#93; Compute never ends after duplicating a material   
&#91;Project&#93; Project asset is duplicated after initial project save   
&#91;Project&#93; Unnecessary computations when switching asset   
&#91;Rendering&#93; Some layer stacks do not render properly after deleting a layer   
&#91;Security&#93; Fix CVE-2015-20107   
&#91;UI&#93; 2D Outputs can be blurry depending on the window size   
&#91;UI&#93; Asset preview can stay opened on top when application loses focus   
&#91;UI&#93; Splash screen rounded corners have a square opaque background

**Known issues:**

&#91;Color Picker&#93; Picking a color on a second monitor with a different resolution may not work   
&#91;Content&#93; Shape light widget is not working in spherical projection mode   
&#91;Interoperability&#93; Material with displacement sent to Stager will lose displacement controls
