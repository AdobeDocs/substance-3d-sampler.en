---
hold: true
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/features-and-workflows/texture-import.html"
breadcrumb-title: ""
description: Learn how to import textures into Substance 3D Sampler to use existing image files in your material creation workflows.
helpx_creative_field: ""
helpx_description: Sampler > Features and workflows > Texture Import
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Texture Import
user-guide-description: ""
user-guide-title: ""
---

# Texture Import

![](../assets/Capture-decran-2025-02-19-162128.png.img.png)

The **Texture Import** template loads multiple images and automatically connects them to the correct output channels based on their filenames.

Channel matching is based on the specific naming conventions detailed below. In case of duplicates or textures without a match, images will be marked as such in the interface.

## OpenPBR

Sampler will match files with the following OpenPBR identifiers with the equivalent channel in the material.

>[!NOTE]
>
> Height channel identifiers are the same as those used for ASM.


| OpenPBR Identifier | SBSAR Usage |
| --- | --- |
| base_weight | baseWeight |
| base_color | baseColor |
| base_metalness | metalness/metallic |
| base_diffuse_roughness | baseDiffuseRoughness |
| specular_weight | specularWeight |
| specular_color | specularColor |
| specular_roughness | specularRoughness/roughness |
| specular_roughness_anisotropy | specularRoughnessAnisotropy/anisotropyLevel |
| specular_ior | specularIOR/IOR |
| transmission_weight | transmissionWeight |
| transmission_color | transmissionColor/absorptionColor |
| transmission_depth | transmissionDepth/absorptionDistance |
| transmission_scatter | transmissionScatter |
| transmission_scatter_anisotropy | transmissionScatterAnisotropy |
| transmission_dispersion_scale | transmissionDispersionScale |
| transmission_dispersion_abbe_number | transmissionDispersionAbbeNumber |
| subsurface_weight | subsurfaceWeight/translucency |
| subsurface_color | subsurfaceColor/scatteringColor |
| subsurface_radius | subsurfaceRadius/scatteringDistance |
| subsurface_radius_scale | subsurfaceRadiusScale/scatteringDistanceScale |
| subsurface_scatter_anisotropy | subsurfaceScatterAnisotropy |
| coat_weight | coatWeight/coatOpacity |
| coat_color | coatColor |
| coat_roughness | coatRoughness |
| coat_roughness_anisotropy | coatRoughnessAnisotropy |
| coat_ior | coatIOR |
| coat_darkening | coatDarkening |
| fuzz_weight | fuzzWeight/sheenOpacity |
| fuzz_color | fuzzColor/sheenColor |
| fuzz_roughness | fuzzRoughness/sheenRoughness |
| emission_weight | emissionWeight |
| emission_luminance | emissionLuminance |
| emission_color | emissionColor/emisive |
| thin_film_weight | thinFilmWeight |
| thin_film_thickness | thinFilmThickness |
| thin_film_ior | thinFilmIOR |
| opacity | opacity |
| thin_walled | thinWalled |
| normal | normal |
| tangent | tangent |
| coat_normal | coatNormal |
| coat_tangent | coatTangent |

## Adobe Standard Material

Below is a list of the supported file naming conventions for each channel:

| **Channel** | **Adobe Standard Material** |
| --- | --- |
| **Ambient Occlusion** | <ul><li>ambientocclusion</li><li>ao</li><li>occlusion</li><li>ambient&#95;occlusion</li></ul> |
| **Base Color** | <ul><li>basecolor</li><li>color</li><li>albedo</li><li>base&#95;color</li><li>base</li><li>col</li><li>colour</li><li>base&#95;colour</li><li>basecolour</li></ul> |
| **Diffuse** | <ul><li>diffuse</li><li>diff</li></ul> |
| **Emissive** | <ul><li>emissive</li></ul> |
| **Glossiness** | <ul><li>glossiness</li><li>gloss</li></ul> |
| **Height** | <ul><li>height</li><li>heightmap</li><li>displacement</li><li>disp</li></ul> |
| **Metallic** | <ul><li>metallic</li><li>mtl</li><li>metalness</li></ul> |
| **Normal** | <ul><li>normal</li><li>nrm</li></ul> |
| **Opacity** | <ul><li>opacity</li><li>alpha</li></ul> |
| **Roughness** | <ul><li>roughness</li><li>rough</li></ul> |
| **Specular** | <ul><li>specular</li><li>spec</li></ul> |
| **Specular Level** | <ul><li>specularlevel</li><li>specular&#95;level</li></ul> |

