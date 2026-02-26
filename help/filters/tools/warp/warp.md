---
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/filters/tools/warp.html"
breadcrumb-title: ""
description: Use the Warp tool in Substance 3D Sampler to apply directional warping and distortion effects to textures and material layers.
helpx_creative_field: ""
helpx_description: Sampler > Filters > Tools > Warp
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Warp
user-guide-description: ""
user-guide-title: ""
---

# Warp

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

![](../../../assets/s-warp-18-n-d.png)

**In:** Tools

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

The **Warp filter** allows you to warp your material based on a number of generated noises.

</td>
</tr>
</table>

## Parameters

**Basic parameters**

* **Random Seed**:  
  The random seed determines the random values of other parameters that use randomness in this filter.
* **Noise Selection**:  
  Select which noise to base the warp on. Different noises can create different effects.
* **Noise Scale**: 0-10  
  Adjust the scale of the source noise. The noise will always tile.
* **Type**:   
  Select which method is used to warp the material. If **Directional Warp** or **Multi Directional Warp** are selected, an additional parameter will appear:
  * **Warp Angle**: 0-1  
    Adjust the direction along which the warp happens
* **Intensity**: 0-1  
  Adjust the strength of the warp.
* **Custom Noise**: toggle  
  Enable to use a custom noise instead of the selection under **Noise Selection**. Available parameters will change based on whether **Custom Noise** is enabled or disabled. If enabled, the following parameters will appear:
  * **Custom Noise Blur**: 0-1  
    Blur the custom noise
  * **Custom Noise**: image/brush  
    Import a custom noise map to use as the warp source.
* **Warp per channel**: toggle  
  When enabled, additional sections will appear to control the warp of each channel independently. For each channel the following parameters are available:
  * ***Channel name***: toggle  
    Toggle whether this channel is impacted by the **Warp filter**.
  * **Blending Mode**:   
    Select how the results of the warp for this channel are blended with the underlying layer
  * **Opacity**: 0-1  
    Change the opacity of the filter results for this channel.
