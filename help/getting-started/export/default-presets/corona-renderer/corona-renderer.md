---
title: Corona Renderer
description: Learn how to export materials from Substance 3D Sampler using the Corona Renderer preset for architectural visualization workflows.
helpx_description: Sampler > Getting Started > Export > Default Presets > Corona Renderer
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/getting-started/export/default-presets/corona-renderer.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - reflections
  - color
  - materials
---


# Corona Renderer

| Preset | Compatibility | Packing Output Description |
| --- | --- | --- |
| Corona Renderer | <ul data-preserve-html="true"><li data-preserve-html="true">PBR Metallic/Roughness</li><li data-preserve-html="true">PBR Specular/Glossiness</li></ul> | **Diffuse****ReflectionGlossiness** (\*)**ReflectionColor** (\*\*)**FresnelIOR** (\*\*\*)**Normal****Displacement****Emissive****Opacity** |

>[!NOTE]
>
> **(\*)** Reflection Glossiness: Square version of the glossiness channel (Glossiness \* Glossiness)
> 
> **(\*\*)** Reflection Color: Export a map where white indicate a dielectric materials and other colors for metallic materials
> 
> **(\*\*\*)** Frenesl IOR: 1 divided by the ior value, ior is generated from the metallic map : 1.4 for dielectrics, 100 for metals (black color)
