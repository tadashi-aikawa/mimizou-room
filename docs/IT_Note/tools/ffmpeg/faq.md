---
description: ffmpegのFAQ
---

# [ffmpeg] FAQ

{{ page.meta.description }}


リサイズしたい
--------------

```
ffmpeg -i input.png -vf "scale=640:-1" out.png
```

`-filter_complex`を指定する複雑なケースは別項目を参照。


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

更にリサイズする場合は `[0:v]scale=360:-1 [s]; [s]` のようにscale filterを通してから変換する。

```
ffmpeg -i input.mp4 -filter_complex "[0:v]scale=360:-1 [s]; [s] split [a][b];[a] palettegen [p];[b][p] paletteuse" output.gif }
```


