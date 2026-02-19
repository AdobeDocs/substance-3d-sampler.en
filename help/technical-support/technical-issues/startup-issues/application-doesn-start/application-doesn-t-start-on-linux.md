---
title: Application doesnt start on Linux
description: Learn how to fix Substance 3D Sampler startup issues on Linux to resolve application launch problems and error messages.
helpx_description: Sampler > Technical Support > Technical Issues > Startup issues > Application doesnt start on Linux
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/technical-support/technical-issues/startup-issues/application-doesn-t-start-on-linux.html"
helpx_creative_field:
  - video
  - graphic-design
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - troubleshooting
  - known-issues
  - system-requirements
---


# Application doesn't start on Linux

The application may not start on Linux with the following error message in a terminal:

```

error while loading shared libraries: libicui18n.so.50
```


This means the library ICU ([International Components for Unicode](http://site.icu-project.org/)) is either missing or the installed version is too recent. The application needs version 50.

To resolve this issues either install version 50 from the package manager or [manually download](http://mirror.centos.org/centos/7/os/x86_64/Packages/libicu-50.2-4.el7_7.x86_64.rpm) the missing version on install it in **/usr/lib64** .
