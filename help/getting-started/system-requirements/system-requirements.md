---
title: "System requirements | Substance 3D Sampler"
description: "Sampler > Getting Started > System requirements"
---

# Supported systems

Below is a list of hardware and systems supported by the application:

>[!WARNING]
>
> Please note that some versions of Nvidia drivers (572.42 and 572.47 for GeForce and 572.16 for RTX pro) make Sampler crash at launch.
> 
> Make sure to use a previous or more recent driver if you have any of those GPUs.

## Windows

|  | Minimum | Recommended | Optimal |
| --- | --- | --- | --- |
| <b>OS</b> | Windows 10 64-bit Version 22H2 | Windows 11 64-bit Version 21H2 | Windows 11 64-bit Version 22H2 |
| <b>CPU</b> | Intel Core i5 AMD Ryzen 5 | Intel Core i7 AMD Ryzen 7 | Intel Core i9 AMD Ryzen 9 |
| <b>GPU</b> | NVIDIA GeForce RTX 2060 Super NVIDIA Quadro RTX 4000 AMD Radeon RX 5700 XT AMD Radeon Pro W5700 | NVIDIA GeForce RTX 3080 NVIDIA Quadro RTX A4000 AMD Radeon RX 6800 XT AMD Radeon Pro W7700 | NVIDIA GeForce RTX 4090 NVIDIA Quadro RTX 5000 Ada Generation AMD Radeon RX 7900 XTX AMD Radeon Pro W7800 |
| <b>VRAM</b> | 8 GB | 16 GB | 24 GB |
| <b>RAM</b> | 16 GB | 32 GB | 64 GB |
| <b>Storage</b> | SSD with 30 GB of available space | SSD with 50 GB of available space | SSD with 70 GB of available space |

|  | Minimum | Recommended | Optimal |
| --- | --- | --- | --- |
| <b>OS</b> | Windows 11 64-bit Version 23H2 | Windows 11 64-bit Version 24H1 | Windows 11 64-bit Version 24H2 |
| <b>CPU</b> | Intel Core i5 AMD Ryzen 5 | Intel Core i7 AMD Ryzen 7 | Intel Core i9 AMD Ryzen 9 |
| <b>GPU</b> | NVIDIA GeForce RTX 2060 Super NVIDIA Quadro RTX 4000 AMD Radeon RX 5700 XT AMD Radeon Pro W5700 | NVIDIA GeForce RTX 3080 NVIDIA Quadro RTX A4000 AMD Radeon RX 6800 XT AMD Radeon Pro W7700 | NVIDIA GeForce RTX 4090 NVIDIA Quadro RTX 5000 Ada Generation AMD Radeon RX 7900 XTX AMD Radeon Pro W7800 |
| <b>VRAM</b> | 8 GB | 16 GB | 24 GB |
| <b>RAM</b> | 16 GB | 32 GB | 64 GB |
| <b>Storage</b> | SSD with 30 GB of available space | SSD with 50 GB of available space | SSD with 70 GB of available space |

### macos

|  | Minimum | Recommended | Optimal |
| --- | --- | --- | --- |
| <b>OS</b> | macOS 12 Monterey | macOS 13 Ventura | macOS 14 Sonoma |
| <b>CPU</b> | Apple M1 | Apple M2 Pro | Apple M4 Pro |
| <b>GPU</b> | Apple M1 | Apple M2 Pro | Apple M4 Pro |
| <b>RAM</b> | 16 GB | 32 GB | 64 GB |
| <b>Storage</b> | SSD with 30 GB of available space | SSD with 50 GB of available space | SSD with 70 GB of available space |

### Linux

|  | Minimum | Recommended | Optimal |
| --- | --- | --- | --- |
| <b>OS</b> | <b>Enterprise ETLA</b>  RHEL 8.6 or later or RHEL 9.2 or later <b>Steam</b> Ubuntu 22.04.1 LTS | <b>Enterprise ETLA</b>  RHEL 8.6 or later  or RHEL 9.4 or later  <b>Steam</b> Ubuntu 22.04.1 LTS or later | <b>Enterprise ETLA</b>  RHEL 8.6 or later  or RHEL 9.4 or later  <b>Steam</b> Ubuntu 22.04.1 LTS or later |

>[!NOTE]
>
> If your system meets the system requirements above but performance is still sluggish, Sampler may be using the wrong GPU.
> 
> If you are using an NVIDIA GPU, [change which GPU Sampler uses by following the instructions on this page](../../technical-support/configuration/nvidia-driver-settings/nvidia-driver-settings.md).

## General recommendations

* For working in comfortable conditions we recommend a monitor with a resolution greater than 1 MegaPixel and wider than 1280 pixels.
* Many Substance Apps depend on OpenSSL 1.1.1 for RHEL8/9 compatibility. For systems with newer OpenSSL versions, you will need to provide it manually.

## 3D capture hardware requirements

The 3D Capture is available on Windows, MacOS Monterey and above.

<b>Windows</b>

We recommend:

* GPU with 8GB of VRAM
* 16GB of RAM. Ideally 32GB and 64GB.
* Minimum of 10GB of disc space.

<b>macOS</b>

* Apple Silicon devices are strongly recommended (M1 or M2)
* Intel-based and AMD GPU with at least 4GB of VRAM and raytracing support

## Unsupported configurations

<b>Windows</b>

* Virtual machine are not supported.
* Windows Server is not supported.

<b>Mac</b>

* Only official Apple configurations are supported.
* eGPUs are not currently supported and may have stability issues.

<b>Linux</b>

* Mesa drivers on Linux are not supported.

<b>Any platform</b>

* Integrated GPUs are not supported on x86-64 (Intel, AMD) CPUs.
* Using Sampler in combination with third-party software that intercepts Sampler calls to the graphics drivers is not supported. Such software
  includes:
  * Post-process injectors such as reshaders that apply color grading, camera effects, ...
  * On-screen overlays such as custom crosshairs, GPU performance metrics, skins for video streaming...

## Minimum GPU driver versions

Below is a list of the minimum GPU driver versions required for the application to run without issue. This list is subject to change as new versions are released.

To download new drivers see: [GPU has outdated drivers](https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/gpu-issues/gpu-has-outdated-drivers.html).

| OS | NVIDIA | AMD | Intel |
| --- | --- | --- | --- |
| <b>Windows</b> | GeForce 551.86 Quadro/RTX 538.33 | Radeon 23.8.1 Radeon Pro / FirePro 24.q2 | 31.0.1015590 |
| <b>Linux</b> | 525.116.04 or later *or* 535.54.03 or later | Radeon 23.20 Pro 23.Q3 | Unsupported |

>[!NOTE]
>
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

 