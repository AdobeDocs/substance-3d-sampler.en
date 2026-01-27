---
title: "Create a Script with Python | Substance 3D Sampler"
description: "Sampler > Scripting and Development > Create a Script with Python"
---

# Create a Script with Python

This guide describes how to create a simple autosave plugin with Python.

## Script structure

Scripts require a single PY file in order to be imported to Sampler. You can save the example script below as a PY file and import it to Sampler.

## Example script

The script below automatically creates variations of your material by selecting a new random seed for each layer in the material. This is useful to ensure that your material can be used in a general case instead of relying on specific random seeds.

### random\_seed\_variations.py

```

import substance_sampler as ssa 

from random import randrange 

 

## Get the current asset loaded in the layer stack

my_asset = ssa.get_selected_asset() 

 

## Create a list of all layers of the current asset

my_asset_layers = my_asset.get_layers() 

 

## Go through the layers list

for layer in my_asset_layers: 

## Go through all parameters of each layer

    for parameter in layer.parameters: 

## if the parameter is Random Seed, change is value

        if parameter.label == "$randomseed": 

            parameter.value = randrange(10000) 

            print(f"Random Seed for layer {layer.name}: {parameter.value}") 

 


```


The code above includes comments to explain what is happening on each line.

## Import the script

Once you've saved the script above as a PY file on your machine, you can import it with Edit &gt; Preferences &gt; Plugins and Scripts. Once imported, a **Scripts** option will appear in the menu bar alongside **File** and **Edit**. From here you can run the script.

You can find out more about managing your scripts [here](../manage-installed-plugins/manage-installed-plugins-and-scripts.md).
