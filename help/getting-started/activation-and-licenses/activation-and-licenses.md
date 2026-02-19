---
title: Activation and licenses
description: Learn how to activate and manage licenses for Substance 3D Sampler to start using the application and access all features.
helpx_description: Sampler > Getting Started > Activation and licenses
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/getting-started/activation-and-licenses.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - cross-product-workflows
  - download-and-install
  - preflight
helpx_tags:
  - SG_SUBSTANCE_ALCHEMIST
---


# Activation and licenses

This page has information on how to activate and manage your licenses so you can start using Sampler.

## Activation process per application type

The activation process depends on where you purchased or have access to Sampler:

| Application Type | Activation process |
| --- | --- |
| Creative Cloud Desktop | See the dedicated page in the [HelpX documentation](https://helpx.adobe.com/support/substance-3d-sampler.html).In case there are any issues the [Creative Cloud documentation](https://helpx.adobe.com/creative-cloud/user-guide.html) may provide additional answers. |
| Steam | Launch the product directly from the Steam library. |
| Substance 3D standalone | See the activation process described below. |

## Activation steps

### The activation wizard

![](activation-wizard.png){width="350px"}

Three choices are available:

* **Evaluate this product**: Legacy trials are no longer available. Instead, you can start a 30 day trial for each Substance 3D application [here](https://www.adobe.com/creativecloud/3d-augmented-reality.html) or with Creative Cloud Desktop. Each trial is independent of the other Substance 3D applications, so you can try them one at a time or all at once.
* **Activate using a license file**: activate the product with a license file (**\*.key**) downloaded from your account page on the [Substance 3D website](https://store.substance3d.com/user) before 30 Sep 2022.
* **Activate using your account**: Legacy substance accounts can no longer be used for activation. [More information about Substance accounts is available here](https://helpx.adobe.com/substance-3d/unlisted/faq-end-of-life-accounts.html).

>[!WARNING]
>
> To install the license file with the Activation Wizard, make sure you run Sampler as an administrator and temporarily disable your anti-virus.

### Manual activation

It is possible to manually activate Sampler by putting the **license.key** file in the following folder:

<table data-preserve-html="true"><colgroup> <col/> <col/> <col/> <col/> </colgroup><tbody><tr><th>Platform</th><th>Version</th><th colspan="2">Path</th></tr><tr><td rowspan="4"><strong>Windows</strong></td><td rowspan="2"><strong>3.0</strong> or newer</td><td colspan="1">App Data (local)</td><td colspan="1">C:&#92;Users&#92;&#91;username&#93;&#92;AppData&#92;Local&#92;Adobe&#92;Adobe Substance 3D Sampler</td></tr><tr><td colspan="1">App Data (roaming)</td><td colspan="1">C:&#92;Users&#92;&#91;username&#93;&#92;AppData&#92;Roaming&#92;Adobe&#92;Adobe Substance 3D Sampler</td></tr><tr><td rowspan="2">Legacy</td><td colspan="1">App Data (local)</td><td colspan="1">C:&#92;Users&#92;&#91;username&#93;&#92;AppData&#92;Local&#92;Allegorithmic&#92;Substance Alchemist</td></tr><tr><td colspan="1">App Data (roaming)</td><td colspan="1">C:&#92;Users&#92;&#91;username&#93;&#92;AppData&#92;Roaming&#92;Allegorithmic&#92;Substance Alchemist</td></tr><tr><td rowspan="2"><strong>Mac</strong></td><td colspan="1"><strong>3.0</strong> or newer</td><td colspan="2">/Users/&#91;username&#93;/Library/Application Support/Adobe/Adobe Substance 3D Sampler</td></tr><tr><td colspan="1">Legacy</td><td colspan="2">/Users/&#91;username&#93;/Library/Application Support/Allegorithmic/Substance Alchemist</td></tr><tr><td rowspan="2"><strong>Linux</strong></td><td colspan="1"><strong>3.0</strong> or newer</td><td colspan="2">/home/&#91;username&#93;/.local/share/Adobe/Adobe Substance 3D Sampler</td></tr><tr><td>Legacy</td><td colspan="2">/home/&#91;username&#93;/.local/share/Allegorithmic/Substance Alchemist</td></tr></tbody></table>

>[!NOTE]
>
> Some of the directories in the paths mentioned above may be hidden by default. Type the path manually in the file explorer or display hidden files to view them.

>[!NOTE]
>
> Make sure that the file is called **license.key** otherwise the application will not be able to find it.

### Environment variable

You can override the location that Sampler checks for the **license.key** file with an [Environment Variable](../../help/pipeline-and-integrations/environment-variables/environment-variables.md).
