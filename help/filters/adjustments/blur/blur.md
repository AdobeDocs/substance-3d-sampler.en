---
title: Blur
description: Use the Blur filter in Substance 3D Sampler to apply blur effects and reduce image sharpness in textures and material layers.
helpx_description: Sampler > Filters > Adjustments > Blur
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/filters/adjustments/blur.html"
helpx_creative_field:
  - video
  - 3d-immersive
  - photography
helpx_experience_level:
  - any
helpx_learn_topic:
  - effects
  - filters
  - adjustments
---


# Blur

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

![](s-blur-18-n-d.png)

**In:** Adjustments

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

Blur the full material or select specific channels to blur.

In the images below the **Blur filter** has been applied to the base color channel.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](3d-filters-cropped-0055-blur-in.jpg)

</td>
<td style="border: 0;" valign="top">

![](3d-filters-cropped-0054-blur-out.jpg)

</td>
</tr>
</table>

</td>
</tr>
</table>

## Parameters

**Basic parameters**

* **Intensity**: 0-1  
  Adjust the amount of blur applied to all channels

**Custom by Channels**

Adjust the amount of blur for each channel independently using these controls. First, enable the channel specific blur and a slider will appear to control the amount of blur applied to that channel.

>[!NOTE]
>
> Channel specific blur overrides **Basic parameters &gt; Intensity** blur for the full material. So, if you set the material blur intensity to 1, but enable a channel and set it's blur intensity to 0, the channel will not be blurred at all, while all other channels will be blurred.

* ***Channel*** **- Custom Blur Intensity**: toggle  
  Enable channel specific blur value.
* ***Channel*** ***-*** **Blur Intensity**: 0-1  
  Adjust the blur for the specified channel.
