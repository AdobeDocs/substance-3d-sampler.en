---
title: "Corona Renderer | Substance 3D Sampler"
description: "Sampler > Getting Started > Export > Default Presets > Corona Renderer"
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
