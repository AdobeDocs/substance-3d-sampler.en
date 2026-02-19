---
title: Flatten layers
description: Learn how to flatten layers in Substance 3D Sampler to improve performance and simplify your layer stack while understanding the impact.
helpx_description: Substance 3D Sampler
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/features-and-workflows/flatten-layers.html"
helpx_creative_field:
  - 3d
helpx_experience_level:
  - all-skill-levels
  - any
helpx_tags:
  - SG_SUBSTANCE_ALCHEMIST
---


# Flatten layers

Flattening layers is a helpful way to improve performance and simplify the layer stack, but it's important to be aware of the impact that Flattening layers can have on your project.

## What does the Flatten layers button do?

Flatten layers merges all layers under the currently selected layer into a single layer. The resulting flattened layer has the same appearance as the original layers, but you can no longer make adjustments to the original individual layers.

### Why Flatten layers?

Whenever you change a layer in the Layer stack, Sampler needs to recalculate the output of that layer and all the layers above it. Each additional layer to calculate means additional processing time and memory usage. Flattening multiple layers decreases the amount of time and memory needed to process those layers. For example, instead of recalculating 10 layers, Sampler only needs to process a single layer.

Additionally, flattening layers results in a simpler layer stack, which is easier to navigate and understand.

### When shouldn't I flatten layers?

Any layers that are flattened can't be accessed individually in the layer stack, so you won't be able to make any changes to parameters in the flattened result. As a result, you should only flatten layers if you no longer need to make changes to the result of those layers.

## Flattened layer parameters

While the parameters from the original layers are lost, Flattened layers have their own set of parameters that you can adjust to control how each resulting channel is used.

For each channel, you can:

* <b>Output usage</b>: Change which channel the output is used for. When you flatten layers, a TIFF is created and named for each channel, and automatically assigned to that channel.
* <b>Opacity from alpha channel</b>: Toggle whether the opacity is based on the Alpha channel result.
* <b>Remove</b>: remove the channel from this layer. This can be useful for channels that don't contain useful information. For example, it's a good idea to remove an all white opacity channel, as doing so will free up memory without affecting the visual results.
