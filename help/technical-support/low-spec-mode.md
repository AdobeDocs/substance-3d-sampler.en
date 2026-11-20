---
title: Low specification mode
description: Learn about low specification mode, which Sampler enables when hardware doesn't meet minimum system requirements.
hold: true
---

# Low specification mode

![](../assets/v6.1/6_1-Checked.png)

If your hardware does not meet Sampler’s [minimum requirements](../getting-started/system-requirements.md), Sampler will automatically launch in Low specification mode, which behaves like [Performance mode](performance-mode.md) without the option to change settings.

## Low specification mode limitations

Low specification mode automatically turns on **Performance mode** with all features disabled and a maximum preview resolution of 2048 × 2048.

Low specification mode disables:

* **Displacement**
* **Shadows**
* **Path tracing**

Additionally, Low specification mode prevents exports above 2048px × 2048px.

![](../assets/low-spec-mode-export-message.png)

*This message appears in the **Export window** while in **Low specification mode** to provide extra information.*

## How can I tell if Low specifications mode is enabled?

When you launch Sampler, if your hardware does not meet the minimum requirements, a window will appear indicating which requirements are not met and offering you the option to continue launching Sampler.

The image below shows an example of a machine with less than 8GB of VRAM.

![](../assets/low-device-specs-popup.png)

If you choose to **Launch anyway**, Sampler will launch in **Low specification mode**. If you have used the checkbox in the message above to not show and launch anyway, you will still see the following banner on subsequent launches.

![](../assets/low-spec-mode-banner.png)

Finally, while **Low specification mode** is enabled, it’s not possible to turn off Performance mode or adjust Performance mode settings.

![](../assets/performance-mode-locked.png)
