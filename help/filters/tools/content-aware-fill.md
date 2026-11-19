---
title: Content-Aware Fill
description: Learn how to use the Content-Aware Fill filter in Substance 3D Sampler to fix problems in repeating patterns or remove unwanted dirt or grime.
---

# Content-Aware Fill

<table>
  <tr>
    <td><br><strong>In:</strong> Tools</td>
    <td>Description<br>Content-Aware fill makes it possible to seamlessly remove elements like dirt, text, or other unwanted objects from your materials.<br>In the forest floor example below, the stick stands out in the repeating pattern. With Content-Aware Fill, we’re able to remove the twig, making the repetition a little less noticeable. <br><br><img src="../../assets/content-aware-fill-before.png" alt=""/><br><em>Before removal</em><br><br><img src="../../assets/content-aware-fill-after.png" alt=""/><br><em>After removal</em></td>
  </tr>
</table>

## Parameters

* **Channels Selection:** Select which channels to run the filter on. By default, this is set to all channels; however, you can also choose to only run on the Height or Base Color channels.
* **Mirror:** For symmetric materials or patterns, this setting guides the Content Aware Fill to incorporate mirroring content across the material.
* **Scale:** For geometric patterns such as tiles or bricks, this setting can help to maintain the structure of the pattern.

### Technical Parameters

* **Custom mask:** Apply a mask using a texture, or use the brush to paint your own mask in the **2D Viewport**.
* **Search Crop Factor:** Crop the sample area used by the filter. By default, the sample area covers the full texture except the masked area - increasing the **Search Crop Factor** decreases the sample area which can help limit the samples to pixels that are closer to the masked area.

### Fill Settings

* **Color Adaptation:** Adjust how much the fill attempts to adapt to surrounding colors. This setting can be useful with materials that
* **Rotation Adaptation:** For patterns where rotation of elements are important, such as the petals of a flower or spokes of a wheel, this setting can help to create more consistent results.
