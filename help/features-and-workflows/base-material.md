---
hold: true
breadcrumb-title: ""
description: Learn how to use the Base Material in Sampler, a great starting point for efficient material editing.
title: Use As Bitmap
user-guide-description: ""
user-guide-title: ""
---

# Base Material

The **Base Material** is a foundational material layer designed to give you a fast, flexible starting point when creating materials in Sampler. It exposes a comprehensive set of parameters that adapt automatically to the **material model** used by your material (OpenPBR or ASM), allowing you to build anything from simple surfaces to complex, physically rich materials.
Whether you are starting from a preset or building a material from scratch, the Base Material ensures you always begin from a **clear, predictable, and editable foundation**.

## Material Model Awareness (OpenPBR vs ASM)

The Base Material is **material‑model aware**.
This means its available properties and default values change depending on whether your material is created using:

* OpenPBR
* ASM (Adobe Standard Material)

While both versions serve the same purpose, they expose **different parameter groups and behaviours**, matching the underlying material model:

### OpenPBR Base Material

The parameter groups include:

* Base
* Specular
* Transmission
* Subsurface
* Coat
* Fuzz
* Emission
* Thin Film
* Geometry
* Misc

These parameters align with OpenPBR's unified, physically‑based representation and are designed for interoperability across the wider 3D ecosystem.

### ASM Base Material

The parameter groups include:

* Surface
* Absorption
* Scatter
* Translucency
* Coat
* Sheen
* Emission
* Geometry

This layout mirrors the ASM shading model and ensures continuity with existing ASM‑based workflows.

>[!NOTE]
>
>The Base Material always adapts to the material model of the material it is applied to. A Base Material applied to an OpenPBR material will not expose ASM parameters, and vice versa.

## Uniform Values and Custom Maps

For every exposed parameter, the Base Material provides two ways of working:

### Uniform values (default)

By default, parameters use uniform values (sliders or colour pickers).
This allows you to quickly define the overall look of your material without any texture inputs.

Uniform values are ideal for:

* Blocking out materials
* Creating clean, simple surfaces
* Establishing a visual starting point

### Custom maps

If you already have texture maps, you can **override any uniform value** by enabling its **custom map input**.

* Toggle the custom map option for the parameter
* Plug in your existing texture
* The map completely replaces the uniform value

## Presets

The Base Material includes a set of **presets**, visible as thumbnails at the top of the Properties panel.
Presets provide:

* Preconfigured Base Material values
* A fast way to start from a visually meaningful setup
* Consistent, readable starting points for common surface types

Selecting a preset does not lock the material. All parameters remain fully editable.

## "Apply preset values" when creating a material

When creating a new material, you can choose to apply preset values from the Create New Material panel.
What this does

* Replaces the Base Material's default values with the values represented by the selected preset thumbnail
* Gives you an immediate visual starting point, instead of neutral defaults
* Helps reduce the "blank page" effect when beginning a new material

What it does not do

* It does not bake or freeze values
* It does not prevent further editing
* It does not add texture maps automatically

You can think of it as choosing where you start, not limiting where you can go.

## Channel Activation: A Critical Step

For a Base Material parameter to have a visible effect, the corresponding channel must be enabled in your material's Channel Settings.

### Best practice

Before tweaking a parameter, check that its channel is enabled
Enable only the channels you need to keep your material clean and efficient