---
title: Adobe Standard Material
description: Learn how to use Adobe Standard Material in Substance 3D Sampler to create materials compatible with Adobe's material standard.
helpx_description: Sampler > Features and workflows > Adobe Standard Material
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/features-and-workflows/adobe-standard-material.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - reflections
  - shading
  - effects
---


# Adobe Standard Material

## Standard material properties

## Base surface properties

**Base color**

The color of the surface.

**Roughness**

How smooth or matte the surface is.

![](surface-roughness.jpg)

**Metallic**

The degree of metallic luster the surface has.

![](surface-metallic.jpg)

**Opacity**

The visibility of the surface.

![](surface-opacity.jpg)

**Ambient occlusion**

Shadows from cavities and creases preventing light from hitting the surface.

**Specular level**

The strength of light reflections on the surface.

![](surface-specularlevel.jpg)

**Specular edge color**

The color of light reflections. Affects glancing angles for metallic materials.

![](surface-specularedgecolor.jpg)

**Normal**

Simulates surface details like bumps and cracks.

**Normal scale**

The strength of the normal effect.

**Combine normal and height**

Applies the normal texture on top of the height texture.

**Height**

Creates surface details using bump or geometry displacement.

**Height scale**

The scale of height in scene units. Applies to both bump and displacement.

**Height level**

The value of the height texture representing zero displacement.

**Anisotropy level**

The amount that reflections stretch in one direction along the surface.

![](surface-anisotropy.jpg)

**Anisotropy angle**

The counterclockwise rotation of the anisotropic effect.

**Emission intensity**

The intensity of light emitted from the surface.

![](surface-emission.jpg)

**Emission color**

The color of emitted light.

![](surface-emissioncolor.jpg)

**Sheen opacity**

Simulates the effect of microscopic fibers or fuzz on the surface.

![](surface-sheen.jpg)

**Sheen color**

The color of the sheen effect.

![](surface-sheencolor.jpg)

**Sheen roughness**

Softness of the sheen effect.

![](surface-sheenroughness.jpg)

## Interior properties

**Translucency**

The amount of light able to transmit through the surface.

![](interior-translucency.jpg)

**Absorption color**

The color light will converge to as it is absorbed.

**Absorption distance**

Approximate distance in scene units that light will travel before reaching absorption color. If set to zero, thickness will not affect absorption color.

![](interior-absorptiondistance.jpg)

**Index of refraction**

The amount light bends as it passes through the object.

![](interior-indexofrefraction.jpg)

**Dispersion**

The amount the color spectrum spreads out when refracted.

**Subsurface scattering**

Scatters light below the surface, rather than passing straight through.

**Scattering color**

The color below the surface that scattered light will become.

![](interior-scattercolor.jpg)

**Scattering distance**

Approximate distance light must travel before reaching full scattering.

![](interior-scatterdistance.jpg)

**Scattering distance scale**

A multiplier of the scatter distance. May be different for each color channel.

![](interior-scatterdistancescale.jpg)

**Red shift**

Sets red light to travel further than other light colors. Useful for skin.

![](interior-scatterredshift.jpg)

**Rayleigh scattering**

Sets orange light to travel further beneath the surface and blue light to travel less.

![](interior-scatterraleigh.jpg)

**Volume thickness**

The thickness of the surface relative to the bounding box of the object. Used for interior effects when the real thickness is not known.

**Volume thickness scale**

Multiplier of the volume thickness.

## Coat properties

**Coat opacity**

Simulates a layer on top of the material. Used to create clear coats, lacquers, and varnishes.

![](coat-coatopacity.jpg)

**Coat color**

The color of the coat.

![](coat-coatcolor.jpg)

**Coat roughness**

How smooth or matte the coat surface is.

![](coat-coatroughness.jpg)

**Coat index of refraction**

The amount light bends as it passes through the coat.

![](cooat-coatior.jpg)

**Coat specular level**

The strength of light reflections on the coat at glancing angles.

![](coat-coatspecular.jpg)

**Coat normal**

Simulate surface details like bumps and cracks on the coat surface.

![](coat-coatnormal.jpg)

**Coat normal scale**

The strength of the coat normal effect.
