# [Docker] Snippets


全体
----

### 大掃除

```bash
docker system prune
```

以下を全て削除する。

* 停止中のコンテナ
* 最新のコンテナで利用されていないネットワーク
* ぶらさがりイメージ
* ぶらさがりビルドキャッシュ


ビルド
------

```bash
docker build -t <image_name> <directory in Dockerfile>
```


実行
----

```bash
Usage: docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

!!! warning
    `[OPTIONS]`の位置に注意
    間違えてもエラーにはならず、`[COMMAND]`や`[ARGS]`として認識されるのでハマりやすい。


### 基本

```bash
docker run <container_name>
```

### ttyを割り当てる

```bash
docker run -t <container_name>
```

### 標準入力を開放する

```bash
docker run -i <container_name>
```

### コマンドを指定する

```bash
docker run <container_name> <command>
```

