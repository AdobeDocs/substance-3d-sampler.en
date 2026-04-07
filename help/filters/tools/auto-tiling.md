---
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/filters/tools/auto-tiling.html"
breadcrumb-title: ""
description: Use the Auto Tiling tool in Substance 3D Sampler to automatically create seamless tiling patterns from textures using AI technology.
helpx_creative_field: ""
helpx_description: Substance 3D Sampler
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Auto tiling
user-guide-description: ""
user-guide-title: ""
---

# Auto Tiling

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

![](../../assets/s-tiling-18-n-d.png)

**In:** Tools

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

The <b>Auto Tiling filter</b> looks for repetitive structures in your material and uses them to create a tiling material. Unlike the <b>Make it tile filter</b> or the <b>Tiling filter</b>, <b>Auto Tiling</b> focuses on isolating the smallest area of the material that can be made to tile.

<b>Auto Tiling </b>is particularly useful for textiles.

</td>
</tr>
</table>

>[!NOTE]
>
> In order for the Auto Tiling filter to work, a minimum of 3x3 repetitions is required in the source image or material.

## Auto tiling filter tutorial

## About Auto Tiling

When you add it to your layer stack, <b>Auto Tiling</b> will try to automatically find repeating patterns and generate a tiling material. If this isn't successful, you can use the <b>Advanced settings </b>button to manually adjust the process.

If you're planning to create a tiling material from an image, it's better to use the <b>Auto Tiling filter</b> first, and then use the <b>Image to Material filter</b>.

<b>Auto Tiling</b> runs completely on your device, no content is sent to the cloud.

## Parameters

Unlike most filters, <b>Auto Tiling</b> does not have parameters. Instead there is an <b>Advanced settings </b>button, that will take you through the process of configuring the filter. You don't need to make manual adjustments of every step, and you can skip forwards or backwards by selecting a step at the top of the window.

This process consists of the following steps:

1. <b>Introduction</b>: Explains how the filter works. Use the Checkbox to hide this screen in future.
1. <b>Map selection</b>: Select which channel the filter should use. The channel with the most visible repeating pattern is recommended. This is usually the Base Color or Height channel, but other channels can be useful depending on your material.
1. <b>Sample settings</b>: Make changes to the input material in order to get the best results. This includes choosing a resolution, and rotating or warping the input. If your pattern is very small, it can be useful to select a higher resolution to make sure the pattern is visible. However for larger patterns, a lower resolution can provide better and faster results.
1. <b>Pattern size</b>: At this step the filter looks for the smallest pattern it can find. You can select between a larger or smaller automatic detection, or select custom size to specify your own size. For the best results, select the smallest size that has the pattern repeat once per box.  
   If the boxes are all irregularly shaped and don't seem to match the pattern, use the custom size to try get more regular results.
1. <b>Pattern detection</b>: Position the points so that each point is at the same location in the pattern. For example in a black and white checkerboard pattern, you might want the points to be at the center of black squares.
1. <b>Region of interest</b>: Select the area of the material to use to create the final pattern. Using a larger region will decrease the amount of visible repetition, but including areas with artifacts or visible lighting differences can increase the amount of visible repetition.
1. <b>Seam removal</b>: Adjust the settings to minimize seam visibility. <b>Cut smoothness </b>controls how smooth the line of the seam is, while <b>Blend width </b>blurs the seam between tiles.

Once you've been through all the steps, use <b>Apply</b> to confirm your choices. The <b>Auto Tiling</b> filter will process the material to generate a final result.
