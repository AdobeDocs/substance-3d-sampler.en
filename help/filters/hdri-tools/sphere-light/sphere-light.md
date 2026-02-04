---
title: "Sphere Light"
description: ""
helpx_description: "Sampler > Filters > HDRI Tools > Sphere Light"
---

# Sphere Light

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

![](s-spherelight-18-n-d.png)

**In:** HDRI Tools

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

Add a sphere light to your environment.

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
  * **Sample Background**  
    * Sample background doesn't make new parameters available - instead it bases the light color on background values.
* **Exposure (EV)**: 0-10  
  Adjust the exposure or brightness of the light.
* **Sphere Radius**: 0-1  
  Adjust the size of the light.
* **Position Mode**:   
  Change the method used to determine the lights position. Parameters in the **Position Coordinates** section will change based on selection.

**Position Coordinates**

Available parameters depend on the selection made for **Basic parameters &gt; Position Mode**. If **Distance from Origin** is selected, the following parameters are available:

* **Distance from Origin**: 0-20  
  Adjust the distance of the light from the camera.
* **Camera Position**: 0-1  
  Adjust the relative position of the camera to the light in the X, Y, and Z axes.

If **World Position** is selected, the following parameters are available:

* **Up Vector**:   
  Change which direction is up.
* **Sphere World Position**: -2 to 2  
  Adjust the position of the sphere light in the X, Y, and Z axes.
* **Distance from Origin**: 0-20  
  Adjust the distance of the light from the camera.
* **Camera Position**: 0-1  
  Adjust the relative position of the camera to the light in the X, Y, and Z axes.

**Shape**

* **Sphere Hardness**: 0-1  
  Soften or harden the edges of the sphere light
* **Shading**:  
  Change the gradient of the light's exposure based on different styles of real world light. With **Shading Light** selected, additional parameters appear:
  * **Shading Light World Position**: -1 to 1  
    Modify the position of the shaded area on the light
  * **Penumbra Transparency**: 0-1  
    Adjust the level of opacity of the shaded area of the light.

**Background**

* **Background Gamma**:  
  Select the color system used to determine background Gamma.
