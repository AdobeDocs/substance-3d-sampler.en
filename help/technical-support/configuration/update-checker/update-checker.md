---
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/technical-support/configuration/update-checker.html"
breadcrumb-title: ""
description: Learn how to use the update checker in Substance 3D Sampler to stay informed about new versions and release notes.
helpx_creative_field: ""
helpx_description: Sampler > Technical Support > Configuration > Update Checker
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Update Checker
user-guide-description: ""
user-guide-title: ""
---


# Update Checker

The Update window indicates if a new version of Substance Alchemist is available and displays as well the latest [Release Notes](../../../release-notes/release-notes.md).

This window automatically appears during the startup of Substance Alchemist if a new version is available to download.

It is possible to avoid displaying this window during the startup with the following methods:

* Use the "Don't remind me until next version" setting in the window to temporarily skip the display of the window until the next version.
* Disable the "**Check for updates**" setting in Edit &gt; Preferences &gt; Check for updates
* Using the command line **--skip-version-check** It won't check if a new version of the application is available when Substance Alchemist is starting up
* Using an environment variable **SUBSTANCE\_ALCHEMIST\_SKIP\_CHECK\_FOR\_UPDATES**:Value 0 or 1 (1 = Disable update check)

>[!NOTE]
>
> Supported since Substance Alchemist 2020.1 (2.1)
