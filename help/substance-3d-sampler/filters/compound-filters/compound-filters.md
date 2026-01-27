---
title: "Compound Filters | Substance 3D Sampler"
description: "Sampler > Filters > Compound Filters"
---

# Compound Filters

This feature lets you create a new type of filters that are represented as a single layer in the interface and be composed of multiples filters.

>[!NOTE]
>
> Supported since Substance 3D Sampler 3.1.0

## Description

A compound filter is a **.ssafilter** file that is a .7zip compressed folder of:

* a description file using JSON formatting: **myfilter\_name.json**
* a **resources** folder containing:  
  * the filter thumbnail: icon.png
  * external file dependencies

### Description file content

* Name: Label of your compound filter displayed in the interface
* Id: Unique identifier of your compound filter
* Category: Category of your compound filter used in the Assets panel when you group your assets by category
* Version: Incremental number to define the version of your compound filter.
* Node: List of nodes to be used
* Link: List of connections between the different nodes

### Example

```

{ "SamplerFilter":  

 { 

 "Name": "My filter", 

 "Category": "My filter category", 

 "Id": "my_unique_id", 

 "Version": 2, 

 "Node": [ 

        { 

            "Id": "foo", 

            "InternalFilter": "Foo" 

        }, 

        { 

            "Id": "bar", 

            "File": "bar.sbsar" 

        } 

    ], 

    "Link": [ 

        { 

            "From": { "Node": "FilterInput", "Usage": "baseColor" }, 

            "To": { "Node": "foo", "Usage": "baseColor"} 

        }, 

        { 

            "From": { "Node": "FilterInput", "Usage": "normal" }, 

            "To": { "Node": "foo", "Usage": "normal"} 

        }, 

        { 

            "From": { "Node": "foo", "Usage": "baseColor" }, 

            "To": { "Node": "bar", "Usage": "baseColor"} 

        }, 

        { 

            "From": { "Node": "bar", "Usage": "baseColor" }, 

            "To": { "Node": "FilterOutput", "Usage": "baseColor"} 

        }, 

        { 

            "From": { "Node": "foo", "Usage": "normal" }, 

            "To": { "Node": "FilterOutput", "Usage": "normal"} 

        } 

    ] 

}}
```


## Step-by-step creation

1. Create a new file: **my\_new\_filter.json**
1. Define its name, ID, category,...
1. Define the list of nodes you need
1. If you need external files, create **resources** folder next to your **.json**
1. Add your file(s) in the **resources** folder
1. Write the list of links between your nodes
1. Verify that your JSON is valid (no typo, missing coma or missing bracket)
1. If you want a thumbnail, add an image **icon.png** in the **resources** folder
1. Select the **.json** file and the **resources** folder and 7zip them

## Documentation

### Version

Using a version number allows you to keep track of your different iterations. When opening a layer stack done with a previous version of your compound filter, a notification will be showed to suggest you to upgrade to the latest version.

### Node

A node can refer to an internal filter of Substance 3D Sampler. Define a unique identifier **Id** to be used to define links between nodes and the label of the internal filter **InternalFilter**

```

        { 

            "Id": "step1_identifier", 

            "InternalFilter": "Dirt" 

        }
```


A node can refer to a SBSAR file that's not in Substance 3D Sampler. Define a unique identifier **Id** to be used to define links between nodes and the filename **File** of the SBSAR file. The SBSAR file has to be in a **resources** folder next to the .alchfilter file.

```

        { 

            "Id": "step1_identifier", 

            "File": "foo.sbsar" 

        }
```


>[!NOTE]
>
> **filterImg** and **filterMat** can't be used as node Id

### Link

A link is a description of how two nodes are linked and are composed of two elements:

* From: Usage to be used by the node
* To: Usage output of the node

Each element has 3 attributes:

* Node: Declare the **Id** of the node you want to use
  * set the input of the compound filter, the node Id is **FilterInput**
  * set the output of your compound layer, the node Id is **FilterOutput**
* Usage: Declare the usage you want to use. There are 3 options:
  * Single usage at a time and declare link by link (baseColor, normal, height, ambientOcclusion, roughness, metallic, diffuse, specular, glossiness, specularLevel, opacity, emissive, scan1, ...)
  * You can also specify a list &#91;"baseColor", "normal"&#93;. The first item of the list of **From** will match the first item of the list of **To**. etc...
  * Use **\*** to let Substance 3D Sampler do the matching between identical usages of all usages of the From node and the To node (It's not possible to combine **\*** with another link, while single links and list links are possible between same nodes)
* Group: In case of a node has several times the same usage, you can use the Group attribute to select a specific usage. ie: For Blend filters, to get the baseColor of the bottom material use *Material1* and to get the baseColor of the top material use *Material2*

```

Link between two nodes  

 { 

            "From": { "Node": "node1","Usage": "baseColor", "Group": ""}, 

            "To": { "Node": "node2", "Usage": "baseColor"} 

     } 

 

Link between outputs of layers below of the compound filter and the compound filter: 

 

  { 

            "From": { "Node": "FilterInput", "Usage": "*" }, 

            "To": { "Node": "node1", "Usage": "*"} 

     } 

 

Link to declare outputs of the compound filter: 

  { 

            "From": { "Node": "node1", "Usage": "*" }, 

            "To": { "Node": "FilterOutput", "Usage": "*"} 

     }
```
