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


mp4からgifに変換したい
----------------------

```
ffmpeg -i input.mp4 output.gif
```

画質低下によるノイズが気になる場合はパレットを指定する。

```
ffmpeg -i input.mp4 -filter_complex "[0:v] split [a][b];[a] palettegen [p];[b][p] paletteuse" output.gif
```
