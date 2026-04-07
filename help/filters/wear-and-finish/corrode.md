---
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/filters/wear-and-finish/corrode.html"
breadcrumb-title: ""
description: Use the Corrode filter in Substance 3D Sampler to add corrosion and chemical degradation effects to metal materials.
helpx_creative_field: ""
helpx_description: Sampler > Filters > Wear and Finish > Corrode
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Corrode
user-guide-description: ""
user-guide-title: ""
---

# Corrode

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

![](../../assets/corrode-filter-icon.png)

**In:** Wear and Finish

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

The corrode filter mimics the effect of acid eating away at your material, leaving holes and damage to the surface.

</td>
</tr>
</table>

## Parameters

**Basic parameters**

* **Random Seed**:  
  The random seed determines the random values of other parameters that use randomness in this filter.
* **Affected Areas**:  
  Select how the curvature of the surface impacts the effect of the filter.
* **Perforation Level**: 0-1  
  Adjust the number of holes created.
* **Curvature Position**: 0-1  
  Modify the curvature range to be affected.
* **Curvature Smooth**: 0-1  
  Smooth the curvature map.
* **Damage Distance**: 0-1  
  Control the damage radius around the corroded areas.
* **Damage Intensity**: 0-1  
  Adjust the amount of damage in the impacted areas.
* **Height Intensity**: 0-1  
  Control the impact of the damage to the height map.
* **Extrude Position**: toggle  
  Switch the direction of the damage on the height map. When disabled, the damage eats into the surface; when enabled, the damage builds outwards from the surface.

**Mask**

* **Use Custom Mask**: toggle  
  Enable or disable the use of a custom mask. If enabled the following parameters appear:
  * **Mask**: image/brush  
    Select an image to use as a mask or use the brush to paint a custom mask directly in the 2D view.
  * **Custom Mask - Blur**: 0-1  
    Blur the mask.
  * **Custom Mask - Invert**: toggle  
    Invert the mask.

**Advanced Parameters**

Some of the Advanced Parameters impact the full material rather than just the areas modified by this filter.

* **Luminosity**: 0-1  
  Adjust luminosity or lightness for the full material.
* **Contrast**: -1 to 1  
  Adjust albedo contrast for the full material.
* **Hue Shift**: 0-1  
  Offset the hue value of colors in the full material.
* **Saturation**: 0-1  
  Adjust the Saturation for the full material.
* **Normal Intensity**: 0-1  
  Adjust the intensity of the normal map where it has been impacted by the **Corrode filter**.
* **Height Range**: 0-1  
  Increase the range of values in the height map for the full material.
* **Height Position**: 0-1  
  Offset the height of the full material.
* **Ambient Occlusion Intensity**: 0-1  
  Adjust the strength of the AO impact due to the **Corrode filter**.
