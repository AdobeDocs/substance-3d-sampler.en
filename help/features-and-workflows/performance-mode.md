---
description: Learn how to use Performance mode in Substance 3D Sampler to improve performance, or even run Sampler on machines below the minimum system requirements.
title: Performance mode
hold: true
---

# Performance mode

Performance mode brings together every setting that can slow down your workflow: resolution limits, shadows, displacement quality, and path tracing. Turn off what you don’t need, and get the responsiveness you want, especially on lighter hardware.

>[!NOTE]
>
> Performance mode is automatically turned on with maximum limitations if your hardware does not meet Sampler’s [minimum requirements](../getting-started/system-requirements.md). This makes it possible to continue using Sampler on less powerful hardware.

## Toggle Performance mode

Performance mode can be toggled with the **Performance mode button** at the top right of the **Sampler window**.

![](../assets/performance-mode-button.png)

## Change Performance mode settings

Use the dropdown next to the **Performance mode button** to control the limits the Performance mode enables.

![](../assets/performance-mode-settings.png)

| Setting | Description |
| --- | --- |
| **Maximum preview resolution** | Performance mode lowers the preview resolution for faster rendering. This doesn’t change the resolution of imported assets or of your document; instead, this changes the quality of the viewport renderer. |
| **Disable displacement quality** | When this setting is enabled, **Performance mode** locks the **Displacement quality value** to 0, disabling the displacement effect in the viewport. For smooth materials such as tiles or fine fabrics, this has minimal visual impact, but can substantially improve performance. |
| **Disable shadows** | Meshes and displaced materials can cast shadows, creating a more realistic image at the cost of performance. With **Disable shadows** turned on, Performance mode disables all shadow processing, improving performance. |
| **Disable path tracing** | Path tracing is a powerful rendering method that follows light paths as they bounce through the scene, creating photorealistic renders. However, Path tracing is expensive. When **Disable path tracing** is turned on, Performance mode disables the option to turn on path tracing in the **3D Viewport**. |

>[!NOTE]
>
> Path tracing can be accessed from the **3D Viewport toolbar**.
>
> ![](../assets/enable-path-tracing.png)
>
> If Path tracing is not enabled, turning on Performance mode with only **Disable path tracing** toggled on will have no effect.
