---
title: "Known issues, limitations HPZ Captis support"
description: ""
helpx_description: "Substance 3D Sampler"
---

# Known issues and limitations

<b>Version: Sampler 5.1, released on August 7th, 2025</b>

* Sampler with HP Z Captis workflow is available on Windows only for now.

* Physically disconnecting the device while a scan is in progress does not stop the capture. If the device is disconnected during the capture, please wait 30 seconds before reconnecting it so it can reconnect to the ongoing capture session.
* The five maps being exported today are the Base color, Roughness, Normal, Height, Opacity.
* When closing the window during a capture, the metadata that were filled in are lost.
* When clicking on any of the “Browse content” or “Shut down” buttons during the transfer of the data from Captis via USB, the transfer stops.

* If you have TDR issues, please refer to [this documentation page](https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/gpu-issues/gpu-drivers-crash-with-long-computations-tdr-crash.html) from Sustance Painter which should help fix them.
* If the "Preview" step is all black instead of viewing the live feed inside the device, please make sure you have removed the lens cap from inside the device cone.
