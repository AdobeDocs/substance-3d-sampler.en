---
helpx_url: 'https://helpx.adobe.com/substance-3d-sampler/getting-started/system-requirements.html'
breadcrumb-title: ''
description: Review system requirements for Substance 3D Sampler to ensure your hardware and software meet compatibility standards.
helpx_creative_field: ''
helpx_description: Sampler > Getting Started > System requirements
helpx_experience_level: ''
helpx_learn_topic: ''
helpx_tags: ''
title: System requirements
user-guide-description: ''
user-guide-title: ''
---

# Supported systems

Below is a list of hardware and systems supported by the application:

>[!WARNING]
>
> Please note that some versions of Nvidia drivers (572.42 and 572.47 for GeForce and 572.16 for RTX pro) make Sampler crash at launch.
> Make sure to use a previous or more recent driver if you have any of those GPUs.

## Windows

|  | Minimum | Recommended | Optimal |
| --- | --- | --- | --- |
| **OS** | Windows 11 64-bit Version 23H2 | Windows 11 64-bit Version 24H1 | Windows 11 64-bit Version 24H2 |
| **CPU** | Intel Core i5 AMD Ryzen 5 | Intel Core i7 AMD Ryzen 7 | Intel Core i9 AMD Ryzen 9 |
| **GPU** | NVIDIA GeForce RTX 2060 Super NVIDIA Quadro RTX 4000 AMD Radeon RX 5700 XT AMD Radeon Pro W5700 | NVIDIA GeForce RTX 3080 NVIDIA Quadro RTX A4000 AMD Radeon RX 6800 XT AMD Radeon Pro W7700 | NVIDIA GeForce RTX 4090 NVIDIA Quadro RTX 5000 Ada Generation AMD Radeon RX 7900 XTX AMD Radeon Pro W7800 |
| **VRAM** | 8 GB | 16 GB | 24 GB |
| **RAM** | 16 GB | 32 GB | 64 GB |
| **Storage** | SSD with 30 GB of available space | SSD with 50 GB of available space | SSD with 70 GB of available space |

### macOS

|  | Minimum | Recommended | Optimal |
| --- | --- | --- | --- |
| **OS** | macOS 13 Ventura | macOS 14 Sonoma | macOS 26 Tahoe |
| **CPU** | Apple M1 | Apple M2 Pro | Apple M4 Pro |
| **GPU** | Apple M1 | Apple M2 Pro | Apple M4 Pro |
| **RAM** | 24 GB | 32 GB | 64 GB |
| **Storage** | SSD with 30 GB of available space | SSD with 50 GB of available space | SSD with 70 GB of available space |

### Linux

| Enterprise | Steam |
| --- | --- |
| RHEL 8 <br>RHEL 9 | Ubuntu 22.04 |

>[!NOTE]
>
> If your system meets the system requirements above but performance is still sluggish, Sampler may be using the wrong GPU.
>
> If you are using an NVIDIA GPU, [change which GPU Sampler uses by following the instructions on this page](../technical-support/configuration/nvidia-driver-settings.md).

## General recommendations

* For working in comfortable conditions we recommend a monitor with a resolution greater than 1 MegaPixel and wider than 1280 pixels.
* Many Substance Apps depend on OpenSSL 1.1.1 for RHEL8/9 compatibility. For systems with newer OpenSSL versions, you will need to provide it manually.

## Unsupported configurations

**Windows**

* Virtual machine are not supported.
* Windows Server is not supported.

**Mac**

* Only official Apple configurations are supported.
* eGPUs are not currently supported and may have stability issues.

**Linux**

* Mesa drivers on Linux are not supported.

**Any platform**

* Integrated GPUs are not supported on x86-64 (Intel, AMD) CPUs.
* Using Sampler in combination with third-party software that intercepts Sampler calls to the graphics drivers is not supported. Such software includes:
  * Post-process injectors such as reshaders that apply color grading, camera effects, ...
  * On-screen overlays such as custom crosshairs, GPU performance metrics, skins for video streaming...

## Minimum GPU driver versions

Below is a list of the minimum GPU driver versions required for the application to run without issue. This list is subject to change as new versions are released.

To download new drivers see: [GPU has outdated drivers](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/technical-support/technical-issues/gpu-issues/gpu-has-outdated-drivers).

| OS | NVIDIA | AMD | Intel |
| --- | --- | --- | --- |
| **Windows** | GeForce 551.86 Quadro/RTX 538.33 | Radeon 23.8.1 Radeon Pro / FirePro 24.q2 | 31.0.1015590 |
| **Linux** | 525.116.04 or later *or* 535.54.03 or later | Radeon 23.20 Pro 23.Q3 | Unsupported |

>[!NOTE]
> On **Mac OS** the GPU driver is provided by the operating system itself. Update to the latest version of your OS to access the newest driver.

## Languages

The software interface is available in the following languages:

* English
* German
* French
* Japanese
* Korean
* Chinese
* Italian
* Portuguese
* Spanish
