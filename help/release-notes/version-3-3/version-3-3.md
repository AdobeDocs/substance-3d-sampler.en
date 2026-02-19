---
title: Version 3.3
description: Review release notes for Substance 3D Sampler version 3.3 to learn about new tools, content, and material creation features.
helpx_description: Sampler > Release Notes > Version 3.3
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/release-notes/version-3-3.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - xr
  - virtual-photography
  - creative-effects
---


# Version 3.3

**Substance 3D Sampler 3.3.0** introduces a series of new tools, content, and features to more easily create and edit materials and environment lights.

*Release date: 17 May, 2022*

## Major features

## Content-Aware Fill

Content-Aware Fill is a popular technology found in Adobe Photoshop, used to remove details in a picture while maintaining the integrity of the surrounding area.

Substance 3D Sampler now uses this same technology, allowing you to clean PBR materials and environment lights. On PBR materials, Content-Aware Fill is applied across all channels. There is no need to process each channel separately.

Content-Aware Fill can help remove large elements to avoid repetition when tiling a material or remove small imperfections on your scanned fabric.

When capturing 360 panoramas, you may not have control of all the elements in the scene and therefore you need to remove small objects on the ground, paintings on a wall or a person standing in the background. Content-Aware Fill now makes this easier.

## IBL Authoring

### Spherical projection

Editing environment lights and 360 images can be challenging when they are displayed as regular images. All elements are distorted making it nearly impossible to edit. With the new spherical projection, you can navigate in 360° and edit with dedicated tools like Nadir Patch, Content-Aware Fill, and all procedural lights with no distortion. It is now easier, for example, to edit or clean straight lines, remove the tripod of the camera, and place line lights perfectly.

Check out new tutorial to [create environment lights](https://www.youtube.com/watch?v=cfW9IyoTXQ8) using this new mode.

### Exposure slider

In the 2D view, you can temporarily modify the exposure to help you better see details or objects on underexposed or overexposed parts of the environment you are editing.

### Dedicated viewer settings

The viewer settings are persistent per type of asset (material or environment light). You can set the mesh, default textures, or camera field of view for each asset type for easier switching between them to work in the right context.

## Improved Widgets

### Clone Stamp

With this Clone Stamp update, you can paint multiple stamp strokes with various sources in a single layer and access the stamp history in the layer stack. Also, you can now see the stamp result directly in the brush preview before painting. This makes material cleaning easier and avoids a lot of back and forth between views.

### Crop and Transform

This update introduces new shortcuts for the Crop and Transform widgets manipulation.

### Brush Toolbar

The new UI, similar to the most recent Adobe products like Fresco, allows you to move the toolbar anywhere in the 2D view, displayed vertically or horizontally. While painting, switch between brush and eraser with the E key and use the new tiling options to better control what you paint.

## Image to Material (AI powered)

### Preserve tiling

Image to Material (AI Powered) gets a new option: It can now preserve the tiling of your tileable image reducing the time to tile the material after.

## Interoperability

Send materials to Stager

It was already possible to send environment lights to Stager. Now you can send your materials to Stager in one click, just as you can with Designer and Painter. Thanks to this feature, you no longer need to publish your materials and load them into Stager as individual files (requires Stager version 1.2.0 with the new material manager).

## Release Notes

### 3.3.0 Zucchini

*(Released 17 May, 2022)*

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
