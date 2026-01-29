---
title: "Splatter | Substance 3D Sampler"
description: "Sampler > Filters > Generators > Splatter"
---

# Splatter

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

![](s-splatter-18-n-d.png)

**In:** Generators

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

Splatter instances of other materials across your material.

>[!NOTE]
>
> For atlas materials, use the Atlas Scatter filter instead.

</td>
</tr>
</table>

## Parameters

**Basic parameters**

* **Random Seed**:   
  The random seed determines the random values of other parameters that use randomness in this filter.
* **Material Input**:   
  Select the number of materials to use as inputs. Note: a Splatter layer with 3 input slots but only one slot filled with an input, will appear differently to a Splatter layer with 1 input slot and that slot filled with the same input. For this reason it is recommended to only use as many inputs as are needed.
* **Grid Size**: 1-64  
  The grid size determines the number of instances created by the Splatter filter.
* **AO Height Depth**: 0-1  
  Adjust the strength of the AO for instances created by the filter.

**Shape**

* **Scale**: 0-5  
  Adjust the base size of all instances
* **Scale Random**: 0-1  
  Adjust the randomness of the scale value for each instance
* **Scale No Overlap**: 0-1  
  Modify the size of instances to avoid overlap
* **Position Random**: 0-2  
  Control the randomness of the scattering of instances
* **Rotation Random**: 0-1  
  Control the randomness of the rotation of instances
* **Rotation from Background Slope**: 0-1  
  Modify how much of an impact the normals of the underlying material has on the rotation of instances.

**Base Color**

* **Albedo Matching**: 0-1  
  Match the color of instances to the color of the underlying material
* **HSL Adjustment**: 0-1  
  Adjust the Hue, Saturation, and Lightness of instances
* **HSL Random**: 0-1  
  Control the randomness of the Hue, Sautration, and Lightness of each instance

**Normal**

* **Normal from** **Background**: 0-1  
  Adjust how much the normal of the material under each instance impacts the normal of the instance.
* **Normal Angle Random**: 0-1  
  Slant the normals of each instance at a random angle.

**Roughness**

* **Roughness Adjustment**: -1 to 1  
  Add or subtract from the roughness value uniformly across instances
* **Roughness Random**: -1 to 1  
  Add or subtract randomly from the roughness value of each instance
* **Roughness From Background**: 0-1  
  Adjust how much the roughness value of the underlying material impacts the roughness value of each instance

**Height**

* **Height Offset**: -1 to 1  
  Offset the height of instances. This can impact how instances blend with the underlying material.
* **Height Offset Random**: 0-1  
  Add a random value to the height offset of each instance
* **Height Scale**: 0-2  
  Adjust the height of all instances.
* **Height Scale Random**: 0-1  
  Add a random value to the height of each instance
* **Skew from Bg Slope**: 0-1  
  Add a slope to each instance to match the slope of the underlying material
* **Background Slope Smoothness**: 0-2  
  Adjust the slope of the background for the purposes of the **Skew from Bg Slope** parameter
* **Conform to Background**: 0-1  
  Control how much the background height map impacts the instances height map. This lets you shrink-wrap instances around the background details
* **Smooth Conformed Background**: 0-1  
  Adjust how much detail is visible due to **Conform to Background**

**Metallic**

* **Metallic Adjustment**: -1 to 1  
  Control the metallic values of instances
* **Metallic Random**: -1 to 1  
  Add or subtract random values from the metallic of each instance
* **Metallic from Background**: 0-1  
  Adjust how much impact the background metallic values have on each instance

**Mask**

* **Use Custom Mask**: toggle  
  Enable this to use a custom mask and access the custom mask controls:
  * **Custom Mask**: image/brush  
    Import an image to use as a custom mask or paint directly in the **2D view**
  * **Custom Mask Blur**: 0-1  
    Blur the edges of the custom mask
  * **Custom Mask Invert**: toggle
  * **Custom Mask Opacity**: 0-1  
    Adjust the strength of the custom mask

Usage Guide

The Splatter filter is a useful way to scatter assets across your material such as leaves, stones, or trash.

To use the Splatter filter:

1. Add the Splatter filter to your layer stack
1. Under the Splatter layer, Input slots will appear
1. Optionally change the number of input slots available with **Basic parameters &gt; Material Input**
1. Drag materials into the Splatter input slots

You can adjust the scatter parameters in the **Properties panel** by selecting the Splatter layer.

You can adjust the parameters of the input materials in the **Properties panel** by selecting the material in the input slot.

 