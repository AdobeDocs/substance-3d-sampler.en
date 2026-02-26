---
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/technical-support/configuration/retrieving-the-installation-path.html"
breadcrumb-title: ""
description: Learn how to retrieve the installation path for Substance 3D Sampler on different platforms for scripting and configuration purposes.
helpx_creative_field: ""
helpx_description: Sampler > Technical Support > Configuration > Retrieving the installation path
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Retrieving the installation path
user-guide-description: ""
user-guide-title: ""
---


# Retrieving the installation path

This page regroups information on ways to retrieve the installation path of the application depending on the version and platform.

## Windows

### Creative Cloud Desktop

1. Open Windows registry editor (**regedit**).
1. Navigate to the registry key: **HKEY\_LOCAL\_MACHINE\Software\Microsoft\Windows\CurrentVersion\App Paths\**
1. Open the sub-key named **Adobe Substance 3D Sampler.exe**
1. The value of the key contains the path to the application executable where it is installed

>[!NOTE]
>
> This registry key is only available since version 3.  
> For older versions, the installation path can be retrieved from the file associations in **HKEY\_CURRENT\_USER\Software\Microsoft\Windows\CurrentVersion\ Explorer\FileExts**.

### Substance 3D Standalone

1. Open Windows registry editor (**regedit**).
1. Navigate to the registry key: **HKEY\_LOCAL\_MACHINE\ SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall**
1. Find the sub-key matching the AppID of your application version (see the table below)
1. The value of the key contains the path to the application installation location

| Version | AppId |
| --- | --- |
| **1.x (2019.x) to 2.x** | {B3506E85-E98F-4D48-A010-BE4DEE27D108} |
| **3.x (or newer)** | {ED4A4ABC-9B7D-44B8-984A-C8A994B69CFD} |

### Steam

The application is installed in the **steamapps/common/** sub-folder of the Steam installation folder.

## Mac

On Mac the application is installed in the following:

| Version | Path |
| --- | --- |
| **3.x or newer** | **/Applications/Adobe Substance 3D Sampler.app** |
| **Legacy** | **/Applications/Substance Alchemist.app** |

## Linux

On Linux the rpm package is installed in the following path:

| Version | Path |
| --- | --- |
| **3.x or newer** | **/opt/Adobe/Adobe\_Substance\_3D\_Sampler** |
| **Legacy** | **/opt/Allegorithmic/Substance\_Alchemist** |
