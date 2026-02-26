---
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/filters/hdri-tools/plane-light.html"
breadcrumb-title: ""
description: Use the Plane Light tool in Substance 3D Sampler to add planar light sources to HDRI environments for area lighting effects.
helpx_creative_field: ""
helpx_description: Sampler > Filters > HDRI Tools > Plane Light
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Plane Light
user-guide-description: ""
user-guide-title: ""
---


# Plane Light

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

![](../../../assets/s-planelight-18-n-d.png)

**In:** HDRI Tools

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

Add a light in the shape of a flat plane to your environment.

![](../../../assets/3d-2d-filters-cropped-0002-plane-light-out.jpg)

</td>
</tr>
</table>

## Parameters

**Basic parameters**

* **Exposure (EV)**: 0-10  
  Adjust the exposure or brightness of the light.
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
* **Position Mode**:   
  Change the method used to determine the lights position. Parameters in the **Position Coordinates** section will change based on selection. With **World Position** selected, the handles will disappear from the **2D view**, instead use the parameters in **Position Coordinates** to modify the light's position.

**Shape**

* **Plane Scale**; 0-1  
  Adjust the scale of the light.
* **Plane Size**: 0-1  
  Adjust the dimensions of the light in the X and Y axes.
* **Plane Rotation**: 0-1  
  Adjust the rotation of the light along the X, Y, and Z axes.
* **Pattern**:  
  Select the shape of the light.
* **Pattern Hardness**: 0-1  
  Soften or blur the edges of the light
* **Pattern UV Mode**:  
  Choose whether transforms stretch the entire shape or only the middle of the shape to maintain edge and corner details.

**Position Coordinates**

Available parameters depend on the selection made for **Basic parameters &gt; Position Mode**. If **Ground/Ceiling** or **Distance from Origin** are selected, the following parameters are available:

* **Line Absolute Height**: 0-1  
  Change how far the light is from the camera.
* **Camera Position**: 0-1  
  Adjust the relative position of the camera to the light in the X, Y, and Z axes.

If **World Position** is chosen in **Basic parameters &gt; Position Mode** the following parameters are available:

* **Up Vector**:   
  Change which direction is up.
* **Point 1 World Position**: -2 to 2  
  Adjust the position of the first point of the line in the X, Y, and Z axes.
* **Point 2 World Position**: -2 to 2  
  Adjust the position of the second point of the line in the X, Y, and Z axes.
* **Camera Position**: 0-1  
  Adjust the relative position of the camera to the light in the X, Y, and Z axes.

**Background**

* **Show Ground Grid**: toggle  
  Display or hide the ground grid.
* **Enable Ground Clipping**: toggle  
  Select whether the light can clip through the ground or not. If enabled, the following control will appear:
  * **Ground Height**: -2 to 2  
    Adjust the height of the ground for the purposes of clipping the light.
* **Background Gamma**:  
  Select the color system used to determine background Gamma.
