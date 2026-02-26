---
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/filters/hdri-tools/shape-light.html"
breadcrumb-title: ""
description: Use the Shape Light tool in Substance 3D Sampler to add custom-shaped light sources to HDRI environments for creative lighting.
helpx_creative_field: ""
helpx_description: Sampler > Filters > HDRI Tools > Shape Light
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Shape Light
user-guide-description: ""
user-guide-title: ""
---

# Shape Light

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

![](../../../assets/s-shapelight-18-n-d.png)

**In:** HDRI Tools

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

Create a light in the shape of a rectangle or disc.

</td>
</tr>
</table>

## Parameters

**Basic parameters**

* **Shape Color Mode**:   
  Select which method to use to determine the light's color. Available parameters will change based on this selection.
  * **Temperature (Kelvin)**
    * **Temperature**: 1000 - 27000  
      Adjust the temperature of the light.
  * **RGB**
    * **Color**: color select  
      Select the color of the light.
  * **Image Input**
    * **Shape Image Input**: image/brush  
      Import an image to use as the color. You can use the brush tool to paint directly in the **2D view**, but this can have unpredictable results with this filter.
* **Hotspot Exposure (EV)**: 0-10  
  Adjust the exposure of the hotspot. The hotspot can sometimes be difficult or impossible to see - in a new **Shape Light filter** set the **Shape Temperature** to 1000 and the **Hotspot Exposure** **(EV)** to 10 to see the hotspot in the center of the shape.
* **Shape**:  
  Set the shape of your light.

**Position**

* **Hotspot Position**: 0-1  
  Offset the hotspot's position
* **Matrix Offset**: -2 to 2  
  Change the position of the shape light. You can also drag the light in the **2D view** to reposition it.

**Shape**

* **Shape Exposure (EV)**: 0-10  
  Adjust the exposure of the light
* **Shape Hardness**: 0-1  
  Soften the edges of the light
* **Hotspot Size**: 0-1
* **Hotspot Falloff**: 0-1  
  Adjust the softness of the edges of the hotspot.

**Background**

* **Background Gamma**:  
  Select the color system used to determine background Gamma.
