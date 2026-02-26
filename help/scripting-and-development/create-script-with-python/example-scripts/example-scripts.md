---
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/scripting-and-development/create-a-script-with-python/example-scripts.html"
breadcrumb-title: ""
description: Access example Python scripts for Substance 3D Sampler to learn how to use the API and automate material creation workflows.
helpx_creative_field: ""
helpx_description: Sampler > Scripting and Development > Create a Script with Python > Example Scripts
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Example Scripts
user-guide-description: ""
user-guide-title: ""
---


# Example Scripts

The scripts below can be used to build an understanding of how the Sampler API works. Feel free to use and add to these scripts as needed for your workflow.

## Export all

Export material with various export presets.

### export\_all.py

```

import substance_sampler as ssa 

import os 

import sys 

 

 

## Function to export as SBSAR with default options

def export_as_sbsar(asset_to_export, w_res, h_res, destination_path): 

    asset_to_export.export(w_resolution=w_res, 

                           h_resolution=h_res, 

                           path=destination_path) 

 

 

## Function to export as PNG with Unreal Engine 4 export preset

def export_as_png_with_ue4_preset(asset_to_export, w_res, h_res, destination_path): 

    [ue4_export_preset] = ssa.get_export_presets("Unreal Engine 4") 

    asset_to_export.export(w_resolution=w_res, 

                           h_resolution=h_res, 

                           path=destination_path, 

                           format=ssa.png, 

                           preset=ue4_export_preset) 

 

## Verify if the project is already saved to get its path

if ssa.save_project(): 

    ssa.save_project() 

 

## Get the folder path of the project

    export_path = os.path.dirname(ssa.get_project_path()) 

 

## Get all assets of your project in a list

    all_project_assets = ssa.get_project_assets() 

 

## Go Through the list of all assets

    for asset in all_project_assets: 

## Export each asset with the resolution 2048x2048px next to the project file (.ssa)

        export_as_sbsar(asset, 2048, 2048, export_path) 

 

## Export each asset with the resolution 2048x2048px in a folder "textures" next to the project file (.ssa)

        export_as_png_with_ue4_preset(asset, 2048, 2048, os.path.join(export_path, "textures")) 

else: 

    print("Save first your project", file=sys.stderr) 

 

 


```


## Import Metadata from a CSV file

This script imports and creates custom metadata from a csv file: [material\_physical\_property\_clo.csv](https://helpx.adobe.com/content/dam/help/en/substance-3d/documentation/sadoc/files/234455545/255426646/1/1680276968224/material-physical-property-clo.csv)

### export\_all.py

```

import os 

import csv 

import substance_sampler as ssa 

 

## Set the path where the csv is stored

csv_path = os.path.expanduser('~DocumentsAdobeAdobe Substance 3D Samplermaterial_physical_property_clo.csv') 

print(csv_path) 

 

## Open the CSV file

with open(csv_path, newline='') as csvfile: 

     

## Create a CSV reader object

    reader = csv.DictReader(csvfile) 

     

    current_asset = ssa.get_selected_asset() 

    current_asset.metadata.custom_metadata = {} 

 

## Create an empty dictionnary to store custom metadata

    my_custom_metadata = {} 

## Iterate over each row in the CSV file

    for row in reader: 

        if row['Material'] == current_asset.name: 

            print(current_asset.name) 

 

            for key,value in row.items(): 

## Add a new metadata for each column of the csv file

                my_custom_metadata[key] = value 

                print(key,value) 

            

            current_asset.metadata.custom_metadata = my_custom_metadata   
```


## Expose all color parameters

This script exposes the color parameter of each layer in the layer stack.

### expose\_all\_color\_parameters.py

```

import substance_sampler as ssa 

 

## Get the current asset loaded in the layer stack

my_asset = ssa.get_selected_asset() 

 

## Get all layers of the current asset in the layer stack

my_asset_layers = my_asset.get_layers() 

 

## Go through all layers

for layer in my_asset_layers: 

## Go through all parameters of each layer

    for parameter in layer.parameters: 

## Select color parameters that are visible

        if parameter.widget_type == ssa.color and parameter.visible: 

## Expose the parameter

            parameter.expose(exposed_label=f"{layer.name} - {parameter.label}", exposed_group="") 

 


```


## Layer stack template

This script automatically adds a set of filters (defined within the script) to the current material.

### layer\_stack\_template.py

```

import substance_sampler as ssa 

 

## Get the current asset loaded in the layer stack

my_current_asset = ssa.get_selected_asset() 

 

## Define my list of filters

[equalizer_filter] = ssa.get_filters("Equalize") 

[tiling_filter] = ssa.get_filters("Tiling") 

[brightness_contrast_filter] = ssa.get_filters("Brightness/Contrast") 

[normal_height_adjustment_filter] = ssa.get_filters("Normal/Height Adjustment") 

[height_to_normal_filter] = ssa.get_filters("Height To Normal") 

 

## Create a list of all filters, starting from bottom to top

layer_stack_template = [equalizer_filter, tiling_filter, brightness_contrast_filter, normal_height_adjustment_filter, 

                        height_to_normal_filter] 

 

## Insert all filters of my template on top of the layer stack

for filter_layer in layer_stack_template: 

## Get the number of layers

    number_of_layers = len(my_current_asset.get_layers()) 

## insert a filter on top of the layer stack (position O is bottom, number of layers is top)

    my_current_asset.insert_filter(filter_layer, number_of_layers) 

    print(f"number of layers: {len(my_current_asset.get_layers())}...")  

 

## Get all layers

my_asset_layers = my_current_asset.get_layers() 

 

## Update two parameters of the Tiling Layer

for layer in my_asset_layers: 

## Filter all layers by the layer name

    if layer.name == "Tiling": 

        print("Layer:", layer.name) 

 

## Check the list of all parameters of the Tiling layer

        for parameter in layer.parameters: 

## Filter the parameters list by the parameter name

            if parameter.label in {"Threshold", "Transform"}: 

                print("Parameter:", parameter.label) 

 

                if parameter.label == "Threshold": 

                    print("Before", parameter.value) 

                    parameter.value = 0.1 

                    print("After:", parameter.value) 

 

                elif parameter.label == "Transform": 

                    print("Before:", parameter.value) 

                    parameter.value = (1.1, 0, 0, 1.1) 

                    print("After:", parameter.value)
```
