---
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/filters/tools/tiling.html"
breadcrumb-title: ""
description: Use the Tiling tool in Substance 3D Sampler to create seamless tiling patterns from textures for repeatable material surfaces.
helpx_creative_field: ""
helpx_description: Sampler > Filters > Tools > Tiling
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Tiling
user-guide-description: ""
user-guide-title: ""
---

# Tiling

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

![](../../../assets/s-tiling-18-n-d.png)

**In:** Tools

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

Use the **Tiling filter** to make your material tileable. The **Make it Tile filter** also makes your material tileable, but each filter works in a different way. If you find that the **Tiling filter** isn't working for you, try the **Make it Tile filter**.

</td>
</tr>
</table>

## Parameters

**Basic parameters**

* **Show Seam**: toggle  
  Choose whether to display the seam
* **Use Mask**: toggle  
  If enabled, you can create a custom mask to control the seam location
  * **Mask**: image/brush  
    Import an image to use as a mask or use the brush to paint a mask directly in the **2D view**

**Edge**

* **Detect Edges**: toggle  
  Toggle whether to detect edges based on the material channels to create a more organic transition between material layers. If Enabled the following additional parameters appear:
  * **Use Threshold Per Channel**: toggle  
    If enabled, additional parameters appear to adjust the threshold of each channel individually.
    * **Threshold Base Color**: 0-1
    * **Threshold Normal**: 0-1
    * **Threshold Height**: 0-1
  * **Threshold**: 0-1  
    Adjust the threshold value use to find the seam.
  * **Blur**: 0-1  
    Blur the area around the seam
  * **Smoothness**: 0-2  
    Adjust the smoothness of the seam. This can help avoid artifacts
  * **Grid Resolution**: 1-11  
    Adjust the resolution of the grid on which the seam is drawn. Lower resolution can improve performance but decrease seam quality
  * **Use Base color**: toggle  
    Switch whether base color information is considered in seam generation
  * **Use Normal**: toggle  
    Switch whether normal information is considered in seam generation
  * **Use Height**: toggle  
    Switch whether height information is considered in seam generation
  * **Cut Offset**: 0-0.5  
    Adjust the offset of the seam on the X and Y axes

**Advanced Parameters**

* **Transform**: 0-2  
  Adjust the matrix transform values. Increase X and W values to adjust how much of an overlap there is between the underlying and overlaid material.
* **Offset**: 0-1  
  offset the material on the X and Y axes
* **Filtering**:  
  Select the filtering method to use on resized pixels. Bilinear filtering blurs pixels, while nearest filtering maintains the hard edge between pixels.
* **Input Size**: 0-8192  
  Adjust the size of the input in pixels on the X and Y axes.

## Usage Guide

The **Tiling filter** works in two steps:

1. It scales and offsets your material to generate an overlap.
1. Then it varies the overlapping edge to hide the seam.

So, to use the **Tiling filter**, adjusting these two parts of the process can get you the best results.

1. Add the **Tiling filter** to the top of the layer stack
1. Use the handles to transform the material so that there is sufficient overlap to hide the seam.
   1. Scaling the material can be helpful to create an overlap, but can also result in loss of detail.
1. Adjust the parameters in the **Edge** section to adjust the seam.

For some materials using the **Tiling filter** alone will still result in artifacts or problems along the seam. In this case it's a good idea to use other filters such as **Clone Stamp** to fix seam and tiling problems.

It's a good practice to work on tiling the material early in the material creation process - as soon as a non-tiling element is added to the material it's a good idea to ensure it tiles before working further. Sampler's filters are designed so that they don't break tiling materials. This means that, once the underlying material tiles, you can keep working with filters and Sampler's included materials and your material will still tile.
