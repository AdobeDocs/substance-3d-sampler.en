---
title: Normal Format
description: Learn how to configure normal map format preferences in Substance 3D Sampler to switch between DirectX and OpenGL formats.
helpx_description: Sampler > Interface > Preferences > Normal Format
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/interface/preferences/normal-format.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - normal-maps
  - printing
  - channels
---


# Normal Format

Normal maps are processed using the <b>DirectX</b> format, keep an<b> OpenGL</b> workflow to import and export OpenGL format by changing the normal format preference.

*Default: DirectX*

The normal format preference impacts:

* Image Import Layer
* Export

## Image Import Layer

When importing a normal texture, the normal format is set to the format selected in Preferences.

### Export

#### SBSAR and SBS

The normal format is an exposed parameter. This parameter can be tweaked by the host application to generate the normal in the format it needs.

#### Image formats

The normal is exported in the format selected in Preferences.
