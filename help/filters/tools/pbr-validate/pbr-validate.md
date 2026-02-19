---
title: PBR Validate
description: Use the PBR Validate tool in Substance 3D Sampler to validate and ensure materials meet physically based rendering standards.
helpx_description: Sampler > Filters > Tools > PBR Validate
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/filters/tools/pbr-validate.html"
helpx_creative_field:
  - video
  - graphic-design
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - pbr
  - color-grading
  - materials
---


# PBR Validate

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

![](s-pbrvalidate-18-n-d.png)

**In:** Tools

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

Use the **PBR Validate filter** to ensure that the PBR values of your material are correct. Unlike most filters, the **PBR Validate filter** is not meant to be a permanent part of the layer stack - instead, use it to validate your material and then remove it so it doesn't modify your material.

</td>
</tr>
</table>

## Parameters

**Basic parameters**

* **Validation Mode**:  
  Select whether to validate albedo (base color or diffuse) values, metallic values, or both albedo and metallic values. Other parameters will update based on this selection
  * **Validation Mode: Albedo**  
    * **Albedo Dark Range Threshold**:   
      Set the threshold for dark values to be picked up by the filter as invalid.
    * **Overlay Map**: toggle  
      Switch between overlay mode - if enabled, the base color map will be overlaid with the invalid pixels.
    * **Hide Validation in Base color**: toggle  
      Hide the validation information from the base color channel.
  * **Validation Mode: Metal**
    * **Metal Reflectance Range**:  
      Set the range of reflectance values to be picked up by the filter as invalid.
    * **Overlay Map**: toggle  
      Switch between overlay mode - if enabled, the base color map will be overlaid with the invalid pixels.
    * **Hide Validation in Base color**: toggle  
      Hide the validation information from the base color channel.
  * **Validation Mode: Combined**
    * **Albedo Dark Range Threshold**:   
      Set the threshold for dark values to be picked up by the filter as invalid.
    * **Metal Reflectance Range**:  
      Set the range of reflectance values to be picked up by the filter as invalid.
    * **Hide Validation in Base color**: toggle  
      Hide the validation information from the base color channel.

## Usage Guide

The **PBR Validate** **filter** helps avoid issues with albedo and metallic values in a material. To understand how the **PBR Validate filter** works, it helps to first talk a little about what PBR is.

## What is PBR?

PBR stands for Physically Based Rendering, and is a method of rendering objects and materials by representing physical properties of a surface with various channels. PBR was created to more accurately represent the real, physical world than previous rendering and shading methods.

In the real world, there are some colors and combinations of properties that are either impossible or incredibly rare. For example, almost nothing in the real world has a pure white or pure black albedo or base color.

So, since PBR is trying to represent real world values, and since some values don't appear or rarely appear in the real world, it's possible to have 'incorrect' PBR values. This is what the **PBR Validate filter** is designed to find.

## How to use PBR Validate

To use **PBR Validate**, add it to the top of your layer stack. You should see a drastic change to the appearance of your material - this is because the **PBR Validate filter** displays the results of the validation in the albedo channel.

The filter uses a red to green scale to show where errors are. If the entire material is green, then there is nothing wrong with the colors or metallic values of your material. However, if you see yellow, orange, or red areas, then there are issues with your material.

If you're using the color validation mode, non-green areas generally mean that there are values in your base color that are close to either completely black or completely white. Use adjustment filters like **Hue/Saturation** or **Brightness/Contrast** to adjust the values of your color channel until the **PBR Validate filter** shows no more errors.

If you're using the metal validation mode, non-green areas generally mean that the combination of your color, roughness, and metallic maps in those areas is unrealistic. Usually this happens with dark color values, 0 roughness, and 1 metallic values. To fix these errors, you can modify the roughness, the metallic, or the color values until the **PBR Validate filter** shows no more errors.
