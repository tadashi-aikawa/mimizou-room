---
description: ffmpegのFAQ
---

# [ffmpeg] FAQ

{{ page.meta.description }}


mp4のサイズをより小さくしたい
-----------------------------

コーデックを`libx264`にすると1/3くらいになる。

```
ffmpeg -i input.mp4 -vcodec libx264 -crf 20 output.mp4
```
