---
title: Paint warp
description: Learn how to use the Paint warp filter in Substance 3D Sampler for fine control over warping of your material.
---

# Paint Warp

The **Paint Warp** filter is a powerful tool designed to correct geometric distortions in image-based scans. It is particularly useful for materials with linear patterns—such as corduroy fabric, wood planks, or brickwork—where the natural lines are not perfectly straight or aligned with the axes. By manually defining the flow of the pattern, you can "straighten" the material to ensure seamless tiling and professional-grade texture maps.

> 📸 SCREENSHOT [ID: paint-warp-01]
> Show: The 2D View showing a corduroy fabric scan with slightly crooked vertical lines.
> State: Base Color channel active, Layer Stack visible.
> Annotation: Highlight the misalignment of the fabric ribs at the edges of the texture.

## Aligning Material Patterns

You can add the Paint Warp filter manually to your Layer Stack, but the most efficient workflow for scans is using the dedicated Quick Action.

### Using the Quick Action

1. Open the **Quick Action** tab.
1. Select **Align Material Patterns by Painting**.
* Sampler will automatically add three layers to your stack: **Equalize**, **Horizontal Paint Warp**, and **Vertical Paint Warp**.
1. In the **Layer Stack**, identify which direction your pattern follows.
* *Example:* For corduroy with vertical ribs, keep the **Vertical Paint Warp** and disable or delete the Horizontal version.

> 📸 SCREENSHOT [ID: paint-warp-02]
> Show: The Layer Stack after running the Quick Action.
> State: Equalize, Horizontal Paint Warp, and Vertical Paint Warp layers are present.
> Annotation: Arrow pointing to the Vertical Paint Warp layer being selected.

### Painting the Warp Guides

Once the filter is selected, you must define the current "crooked" path of the pattern so Sampler knows how to straighten it.

1. Go to the **Properties** panel of the Paint Warp filter.
1. Locate the **Image Input** property and click the **Brush** icon next to it to enter painting mode.
1. Adjust the **Brush Size** using the UI widgets or shortcuts.
1. Paint along the lines of your material:
* **Tip:** Hold **Shift** while clicking to create perfectly straight segments between points.
* Trace several lines across the width or height of the texture to provide the algorithm with enough data.
1. In the **Properties** panel, toggle the **Straighten** parameter to **On**. Sampler will warp the image so the painted lines become perfectly parallel to the chosen axis.

> 📸 SCREENSHOT [ID: paint-warp-03]
> Show: The 2D View with blue paint strokes following the ribs of the corduroy.
> State: Paint mode active, Brush tool selected.
> Annotation: Highlight the Shift-click method for creating guide lines.

## Parameters Reference

| Name | Description | Range/Options | Default |
| :--- | :--- | :--- | :--- |
| **Direction** | Determines the axis the warp will align to. | Vertical, Horizontal | Vertical |
| **Straighten** | Toggles the warping effect on or off based on the painted mask. | Toggle (On/Off) | Off |
| **Show Input** | A helper overlay that displays guides to assist in painting accuracy. | Toggle (On/Off) | Off |
| **Smooth Warp** | Controls the falloff and smoothness of the deformation between painted guides. | 0.0 - 1.0 | 0.5 |

## Tips and Best Practices

* **Use Show Input:** Enable the **Show Input** toggle while painting. This provides a grid overlay that makes it easier to see exactly where the original scan deviates from a perfect grid.
* **Don't Over-Paint:** You don't need to trace every single line in a pattern. Usually, 3 to 5 well-placed lines across the texture are sufficient for the algorithm to calculate the necessary deformation.
* **Combine with Tiling:** Use Paint Warp before applying the **Tiling** filter. A straightened pattern is significantly easier to tile without visible seams or "broken" lines at the edges.
* **Equalize First:** As seen in the Quick Action, placing an **Equalize** filter before the Paint Warp helps remove lighting gradients, making it easier to see the pattern details you are trying to align.

> 📸 SCREENSHOT [ID: paint-warp-04]
> Show: The final result in the 2D View with the Straighten toggle active.
> State: The corduroy lines are now perfectly vertical and parallel.
> Annotation: none

## Related Articles

* [Equalize Filter](./equalize)
* [Tiling Filter](./tiling)
* [Quick Actions Overview](./quick-actions)
* [Working with Scans](./working-with-scans)
