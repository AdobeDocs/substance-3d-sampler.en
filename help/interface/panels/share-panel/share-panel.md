---
title: "Export panel"
description: ""
helpx_description: "Sampler > Interface > Panels > Export panel"
---

# Export panel

The <b>Export panel</b> is where you can export your assets as general files or send assets directly to other applications.

## Send to...

The Send to... options allow you to directly send your asset to other applications installed on your system. This is generally much faster than importing and exporting assets.

Currently Sampler supports sending to:

* **Substance 3D Painter**: import materials and environments that you can use while texturing your assets.
* **Substance 3D Stager**: imports environment lights to change the mood of your scene. Only available with environment lights, disabled for materials.

Materials are always sent as SBSAR, environments as EXR.

## Export

Click **Export as...** to export the asset you're currently working on. In the window that appears there are some options to adjust your export:

| Setting | Description |
| --- | --- |
| Name | Change the name of your asset. |
| Destination path | Change the save location. |
| Format | Choose whether to export as an SBS, SBSAR, or as a collection of images. |
| Preset | Select a preset to automatically organize your export for a specific application. [More information about presets is available here](../../../getting-started/export/default-presets/default-presets.md). |
| Resolution | Change the resolution of your export. |
| Channels | Toggle which channels should be exported as part of your asset. |

>[!NOTE]
>
> For more information on the Export dialog options and other information like file formats, see the [Export article](../../../getting-started/export/export.md) and its [sub-article on the Export Window](../../../getting-started/export/export-window/export-window.md).

Once you're happy with the export settings, click **Export**. Your export will appear in the export queue which shows a list of recent exports. Click the folder icon on any export to open the file location of that export.
