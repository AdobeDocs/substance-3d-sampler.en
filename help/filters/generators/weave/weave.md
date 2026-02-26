---
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/filters/generators/weave.html"
breadcrumb-title: ""
description: Use the Weave generator in Substance 3D Sampler to create fabric weave patterns and textile textures for material creation.
helpx_creative_field: ""
helpx_description: Sampler > Filters > Generators > Weave
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Weave
user-guide-description: ""
user-guide-title: ""
---


# Weave

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

**In:** Generators

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

Use the Weave filter to convert images into woven patterns.

</td>
</tr>
</table>

## Parameters

**Presets**

Use presets to quickly change parameters to view different styles of weave

**Basic parameters**

* **Random Seed**:  
  The random seed that all other random parameters in this filter is based on.
* **Image**: image/brush  
  Select an image or paint directly in the **2D view**. The **Weave filter** works best when an image is selected.
* **Color Count**: 1-10  
  The **Weave filter** automatically breaks down the image input into a number of colors based on this parameter. Each Color's parameters can be controlled independently.
* **Area Size (cm)**: 2-50  
  Change the physical size being represented by the 2D space. This will change the number of stitches used to recreate the input image.
* **Density (Stitches per cm)**: 1-105  
  Works with the **Area Size (cm)** control to adjust the number of stitches in the 2D space.
* **Global Roughness**: 0-1.0  
  Adjust the roughness of the material
* **Weft Color Mode**:  
  Select whether the Weft is colored based on the image input or based on custom color selections. If **Override per color** is selected, an additional **Color** parameter will appear in each Color.

**Color X**

The number of colors available to modify depends on **Basic Parameters &gt; Color Count**.

* **Color**: color select  
  Only available if **Basic Parameters &gt; Weft Color Mode** is set to **Override Per Color**. Choose the color of the material for this section.
* **Border Size**: 0-1  
  Add a border on the edges of the selected color. The border increases the length of the weft between warp threads near the edge of the color, avoiding warp stitches to appear close to edge of color sets.
* **Roughness Offset**: 0-1  
  Modify the roughness for this color set
* **Metallic**: 0-1  
  Modify the metallic value for this color set
* **Height Position**: 0-1  
  Adjust the height of this color set. Use this to add depth to the woven version of your image.

**Advanced**

* **Warp Color**: color select  
  Change the color of the warp threads (By default the warp threads run perpendicular to the threads that are most visible.)
* **Warp - Weft Swap**:  
  Swap which threads are warp and which are weft. This has the effect of rotating the stitches by 90 degrees,
* **Warp Shafts**: 1-16  
  Adjust the relative frequency of Warp threads to Weft threads. Can be used to create different jacquard patterns.
* **Warp Size**: 0-1  
  Make the warp threads thicker or thinner
* **Height Difference Blur Intensity**: 0-1  
  Control the slope or blur caused by **Height Position** differences. This has no effect unless you change the **Height Position** slider for at least one Color set.

## Usage Guide

The Weave filter can be a little confusing at first, but with just a few important parameters to get started you'll soon be creating intricate weaves to add to your materials.

>[!NOTE]
>
> If you've used the [Embroidery ](../../../filters/generators/embroidery/embroidery.md)filter before, the Weave filter works in a similar way. They produce different effects, but you can use images with them in the same way.
> 
> Images for weave should be square proportions, high-resolution (2K minimum) and feature at most 10 different colors. The alpha or transparency channel can be used to cut out shapes. Ideally they are vector-based, but exported as PNG bitmap.

To use the Weave filter:

1. Drag and drop an image into
1. Add the Weave filter to your layer stack.
1. Adjust **Basic parameters &gt; Color Count** until the color balance looks correct for your image. With a limit of 10 colors, the Weave filter works best with flat colors and illustrated images.
1. Adjust other parameters to fine tune the appearance of your patch.

These are the basics of how to use the Weave filter.

It's possible to use transparent images in the Weave filter, but by default these will also impact the opacity map of your material - transparent parts of the image will make the material transparent too. To create a patch with the Weave filter and have it sit on top of the layers below it, use the Decal filter.

1. Create a Decal filter.
1. Add the Weave filter to the Decal filter's input slot.
1. Follow the normal steps to adjust the Weave pattern.

The Decal layer converts the Weave input into a Decal - so the Weave layer's transparency tells the decal layer how to mask out the Woven pattern. With the Decal layer you can also move the pattern around on your material or enable functionality like tiling.
