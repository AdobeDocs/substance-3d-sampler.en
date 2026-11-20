---
description: Use the Clone Stamp tool in Substance 3D Sampler to clone and paint texture areas for seamless material editing and repair.
title: Clone Stamp
---

# Clone Stamp

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

![](../../assets/s-clonestamp-18-n-d.png)

**In:** Tools

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

The **Clone Stamp** tool lets you manually duplicate or patch parts of your material. It is primarily used to fix seams and remove errors from scanned materials, such as debris, shadows, or artifacts. You can paint multiple stamp strokes from different source areas within a single Clone Stamp layer, and manage each stamp individually in the **Layers panel**.

The images below show the **Clone Stamp** being used to remove debris from a snow material.

![](../../assets/3d-2d-filters-cropped-0049-clone-stamp-in.jpg)

The snow material includes a number of twigs and other debris scattered around.

![](../../assets/3d-2d-filters-cropped-0048-clone-stamp-out.jpg)

After using the **Clone Stamp** tool, the twigs are replaced with clean snow.

</td>
</tr>
</table>

## Parameters

**Basic parameters**

* **Expand mask**: 0–1

  Adjust how far around the painted area the filter will attempt to match the underlying material.

* **Fade blending**: 0–1

  Soften the edge of the cloned area to blend more naturally with the surrounding material.

* **Blur mask**: 0–1

  Adjust the amount of edge detail on the clone stamp. Higher values produce smoother, more blob-like edges.

* **Keep ratio**: toggle

  When disabled, allows you to adjust the horizontal and vertical proportions of the stamped area independently.

  * **Horizontal**: 0–2
  * **Vertical**: 0–2
* **Rotation**: -180 to 180

  Rotate the stamped area to match the surrounding material's direction or grain.

* **Flip Horizontal**: toggle

  Mirror the stamped area along a horizontal axis.

* **Flip Vertical**: toggle

  Mirror the stamped area along a vertical axis.

**Fade blending**

Use the per-channel Fade blending controls to independently adjust blending strength for each material channel.

**Advanced**

* **Normal intensity**: 0–2

  Adjust the strength of the normal map in the stamped area to control how the cloned surface responds to lighting.

* **Source position**:
  * Horizontal: 0–1 — Adjust the horizontal position of the clone source.
  * Vertical: 0–1 — Adjust the vertical position of the clone source.
* **Target position**:
  * Horizontal: 0–1 — Adjust the horizontal position of the paint target.
  * Vertical: 0–1 — Adjust the vertical position of the paint target.
* **Tiling mode**: dropdown

  Enable or disable tiling when cloning near material borders.

## How to use Clone Stamp

1. Click **Clone Stamp** in the left sidebar or add it from the **Add a layer** button in the **Layers panel**. A new Clone Stamp layer appears at the top of the layer stack and the **2D view** opens automatically.

1. **Set a source point**: Hold `Ctrl` (`Cmd` on macOS) and click a clean area of the material in the **2D view**. This defines the region that will be copied.

   > 📸 SCREENSHOT [ID: clone-stamp-001]
   > Show: 2D viewport with a source point crosshair visible on a clean area of a snow material
   > State: Clone Stamp layer selected; Ctrl held down; source indicator visible
   > Annotation: Label the source crosshair

1. **Paint over the problem area**: Click and drag over the area you want to fix. The material from the source point replaces the painted area in real time.

   ![](../../assets/alchemist-2020-2-clone.gif){width="300px"}

1. Adjust **Fade blending** and **Expand mask** in the **Properties panel** to fine-tune how the cloned area blends with its surroundings.

>[!NOTE]
>
> Avoid placing the source point close to the area you are cloning. If the source overlaps the problem area, the artefact can be cloned along with the clean content.

## Working with multiple sources

You can add multiple source points within a single Clone Stamp layer, each with its own position, rotation, and blending settings. This allows you to fix several different areas — or draw from several different clean regions — without stacking multiple layers.

To add a new source, hold `Ctrl` (`Cmd` on macOS) and click a new area in the **2D view**. A new stamp entry appears beneath the Clone Stamp layer in the **Layers panel**.

> 📸 SCREENSHOT [ID: clone-stamp-002]
> Show: The Layers panel with a Clone Stamp layer expanded, showing three individual stamp entries nested beneath it
> State: Clone Stamp layer expanded; three stamps visible with different source positions
> Annotation: Arrow pointing to the nested stamp entries in the Layers panel

Select any individual stamp entry in the **Layers panel** to adjust its parameters independently in the **Properties panel** — including its source position, rotation, and blending settings.

>[!TIP]
>
> Use the **brush preview** in the **2D view** to see the stamp result before committing a stroke. This helps you verify that the source region matches the surrounding area before painting.

## Toolbar

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

![](../../assets/CloneStampBrushToolbar.png)

</td>
<td width="83.33%" style="border: 0;" valign="top">

While a Clone Stamp layer is selected, a toolbar appears in the **2D view**.

* Select **Brush tool** to add to the mask.
* Select **Erase tool** to remove from the mask.
* Set the size of the currently selected tool.
* Access additional controls:
  * **Brush tiling**: Toggle X and Y brush tiling.
  * **Overlay**: Toggle the overlay visibility while hovering over the 2D view.
* View **2D view controls**.

</td>
</tr>
</table>

>[!NOTE]
>
> Like other viewport toolbars, you can drag the handle at the top of the toolbar to reposition it, double-click the handle to switch between vertical and horizontal layout, or use the double chevron to hide or expand it.

## Shortcuts

| Action | Windows + Linux | macOS |
| --- | --- | --- |
| Increase brush size | `]` or `Ctrl` + Mouse Wheel | `]` or `Cmd` + Mouse Wheel |
| Decrease brush size | `[` or `Ctrl` + Mouse Wheel | `[` or `Cmd` + Mouse Wheel |
| Set the source | `Ctrl` + Left click | `Cmd` + Left click |

## Related

* [Warp](./warp.md)
* [Make it Tile](./make-it-tile.md)
* [Image to Material](./image-to-material.md)
