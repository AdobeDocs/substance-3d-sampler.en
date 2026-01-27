---
title: "Application doesnt start on Linux | Substance 3D Sampler"
description: "Sampler > Technical Support > Technical Issues > Startup issues > Application doesnt start on Linux"
---

# Application doesn't start on Linux

The application may not start on Linux with the following error message in a terminal:

```

error while loading shared libraries: libicui18n.so.50
```


This means the library ICU ([International Components for Unicode](http://site.icu-project.org/)) is either missing or the installed version is too recent. The application needs version 50.

To resolve this issues either install version 50 from the package manager or [manually download](http://mirror.centos.org/centos/7/os/x86_64/Packages/libicu-50.2-4.el7_7.x86_64.rpm) the missing version on install it in **/usr/lib64** .
