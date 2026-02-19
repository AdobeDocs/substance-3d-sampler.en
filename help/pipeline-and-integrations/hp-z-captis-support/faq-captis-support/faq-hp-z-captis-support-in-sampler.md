---
title: FAQ for HP Z Captis support in Sampler
description: Access frequently asked questions about HP Z Captis support in Substance 3D Sampler to find answers about hardware integration and usage.
helpx_description: Substance 3D Sampler
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/pipeline-and-integrations/hp-z-captis-support/faq-hp-z-captis-support-in-sampler.html"
helpx_tags:
  - SG_SUBSTANCE_ALCHEMIST
---


# Most frequently asked questions

## Material samples

+++What use cases does Captis cover?
The solution covers cross-industries use cases (Automotive, Apparel, Product Design, Media &amp; Entertainement, Architecture…). The Studio Mode enables desktop capture (repeatable, efficient and simple) while the Explorer Mode enables mobile capture 'flexible, on the go, adapting to every situation).

+++

+++What material types can be scanned and captured with Captis?
Any material types can be scanned and capture except with multiple clear coat layers (car paints are excluded from Captis scope). Some specific materials may require additional processing in Sampler to optimize the results. Please note that the processing algorithms will be continuously optimized over time.

+++

+++What are the restrictions on material sample size or shape – do samples need to be flat?
Captis can scan a large variety of material samples size or shape. It is delivered with magnets to flaten the samples on the sample tray. There are several modes to capture a material sample with Captis:

* Studio Mode: with the studio base on your desk, in the studio, or in the factory, Captis will take samples up to 30cm x 30cm - with backlighting for opacity. Depth of the sample tray is 1.8 CM.

* Explorer Mode: you can utilize the explorer ring in the field, on set, or in unique environments and enable flexible capture for samples larger than 30cm x 30cm. Current limitation: please note that the Explorer Mode is still an early version and is not optimized yet (as of July 29th, 2024 release).

+++

## Software

+++Does the HP Z Captis device require a software subscription or license for use?
The Captis device requires an active Substance 3D Sampler Enterprise, Teams or University license, available in the Substance 3D Collection under the same conditions and terms of use as any Substance 3D subscription.

The device (HP Z Captis) and the licence (Substance 3D Sampler) are sold separately.

+++

+++What level of integration exists with Adobe’s Substance suite?
HP Z Captis device is fully controlled and operated through Adobe Substance 3D Sampler: you can preview and launch the capture from Substance 3D Sampler, and once the capture is completed, it will automatically load the PBR channels as a layer and create a 3d material. You can continue processing your materials with all tools and filters available in Sampler.

Once your captured material is in Substance 3D Sampler, you can export it to any application of the Substance 3D suite (Substance 3D Designer, Painter, Stager) and to any 3rd-party application supporting Substance, including 3DS Max, Maya, Blender, Unreal Engine, CLO, Browzwear, VRED, Rhino, Cinema4D and many more (see the full list here: <https://www.adobe.com/products/substance3d/plugins.html>).

+++

+++What are the recommended specifications to use Substance 3D Sampler with Captis?
Sampler hardware specifications are available [here](../../../help/pipeline-and-integrations/hp-z-captis-support/system-requirements-use/system-requirements-to-use-hp-z-captis.md).

+++

+++Is the HP Z Captis workflow available on both Windows and Mac?
As of the February 20th, 2025 release, Sampler with HP Z Captis workflow is available on Windows only.

+++

+++Where can I find the version of Substance 3D Sampler with HP Z Captis workflow?
As of the February 20th, 2025 release, you can access Adobe Substance 3D Sampler with Captis workflow as part of the regular builds of Substance 3D Sampler, downloaded from the Creative Cloud desktop app. It is not necessary to download them from Adobe Prerelease anymore.

+++

+++What is not available yet?
*Limitations as of August, 2025 (Sampler 5.1.0 build):*

* Sampler with HP Z Captis workflow is available on Windows only for now.

* The five maps being exported today are the Base color, Roughness, Normal, Height, Opacity.

* Explorer Mode is still an early version and is not optimized yet.

* Tiling is performed in Sampler layer stack using current tiling filters.

+++

+++What PBR channels are available?
As of August 7th, 2025 release, the five maps being exported are the Base color, Roughness, Normal, Height, Opacity. The current processing pipeline does not handle yet the Metalness map.

+++

+++Is tiling automatically done?
Tiling is performed in the Sampler layer stack using current tiling filters.

The Auto tiling filter can be used to tile automatically materials with a defined repetitive structure or small patterns, with a minimum of 3 patterns in each direction. Learn more about this filter in the [dedicated section of the documentation](../../../help/filters/tools/auto-tiling/auto-tiling.md).

+++

+++Which formats can the scanned materials be exported as?
HP Z Captis is natively operated by Adobe Substance 3D Sampler. HP Z Captis captures 64 raw images (that can be retrieved from your local folder) and PBR maps (that are processed from the raw captured images and that are loaded automatically in Substance 3D Sampler). Substance 3D Sampler will create a 3d material based on the PBR channels that are automatically loaded in Sampler layer stack after the capture.

From Adobe Substance 3D Sampler, you can export your digital material in any export format available in Substance 3D Sampler: as Substance files (.SBS and .SBSAR files) or as bitmap textures including .PNG, .JPG, .TIFF… (see the details on Sampler documentation webpage: [https://helpx.adobe.com/substance-3d-sampler/getting-started/export.html](../../../help/getting-started/export/export.md)).

+++

+++What is the difference between LDR and HDR during capture?
During the preview, you have the possibility to choose the output type between LDR (low dynamic range) and HDR (high dynamic range).  
Even if LDR is chosen, the HDR maps will be captured and saved on your device.  
It is advised that you select the LDR, as that will make the size of the project more manageable in Sampler and in any third party app where the sbsar file will be used.

+++

## Processing

+++How can I use Captis in my current 3D pipeline if I use specific file formats, standards and specifications or 3rd-party applications?
HP Z Captis is natively operated by Adobe Substance 3D Sampler. Once you have capture and digitize your material sample in Substance 3D Sampler, you can export seamlessly your digital materials:

In any applications of the Substance 3D ecosystem (including Substance 3D Designer or Substance 3D Painter that support various exports formats: https://helpx.adobe.com/substance-3d-general/ecosystem/import-and-export-formats.html).

In any applications integrating Substance file format as 3DS Max, Maya, Blender, C4D, Rhino, Browzwear, CLO... (see the full list here: <https://www.adobe.com/products/substance3d/plugins.html>). If you are using an application that is not listed there, you can always export PBR texture images and plug them manually in any applications that does not support the Substance file format natively.

+++

+++How many pictures are being taken to create the maps?
&#91;8 light panels + 1 backlight&#93; x &#91;8 polarization states&#93; x &#91;8 bracketing exposures for HDR&#93; x &#91;4 overdraws to reduce noise&#93; = 2048 + 256 (for backlight)

+++

## Device management

Learn more about the device and its specs on the [HP website](https://www.hp.com/us-en/workstations/z-captis.html "HP Z Captis").

+++Can I change the IP Address of the device?
To change the IP address of the device you can modify the Windows file C:\Windows\System32\drivers\etc\hosts.txt by adding an extra line:

For example you can add 192.168.55.1 captis-device and then in <b>Sampler&#39;s settings &gt; Storage and Cache &gt; Material capture &gt; Captis address</b> replace the IP with captis-device

+++

## Usage issues

+++Sampler does not detect HP Z Captis.
Make sure that the HP Z Captis is connected to a USB 3.0 port.

Make sure that the USB cable is connected to the base of the HP Z Captis, not to the cone.

+++

+++My preview is completely black in Sampler window.
Make sure you have the camera protection removed.

+++

+++Copying files from the HP Z Captis to my computer is slow.
Make sure that the HP Z Captis is connected to a USB 3.0 port.

If you asked to retrieve both the material and photometry images, it is normal that the copy takes more time.

+++

+++Sampler did not copy the images to my computer. Do I have to restart the scan?
No, you do not. You can browse the content of the device and copy the images found in the Adobe folder using the file explorer of your OS.

+++

+++The menu indicates that the device is in recovery mode.
Press the power button a few seconds to turn it off. Turn it on again.

+++

+++I moved the cone from its base to the explorer ring and I cannot scan anymore.
It is recommended to turn off the HP Z Captis before unplugging it from its base or from the explorer ring.

+++

+++Exporting my material in SBSAR is slow.
Make sure that the images are not in 32bit float format in the Properties panel.

You can also set the compression level to “none” to make the export faster.

+++

+++I want to change the saving path for the captured materials and photometry images.
It is now possible to edit the location where the captured materials and photometry images will be saved, in Edit &gt; Preferences &gt; Storage and Cache &gt; Material capture.

+++

+++The window is bigger than my screen and I cannot resize it.
The Captis window is indeed not resizable. You might be using a screen magnification that is not handled. Captis supports the following:

* Resolution: 1920x1080
  * Maximum magnification: 100%

* Maximum magnification: 100%

* Resolution: 2560x1440
  * Maximum magnification: 125%

* Maximum magnification: 125%

* Resolution: 3840x2160
  * Maximum magnification: 200%

* Maximum magnification: 200%

* Resolutions below 1920x1080 are unsupported.



+++
