# [Docker] Snippets

{{link("https://docs.docker.com/engine/reference/commandline/docker/")}}


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

### 環境変数を指定する

```bash
docker run --env VARNAME=<value>
```

### 環境変数をファイルで指定する

```bash
docker run --env-file <file_name>
```

指定ファイルの中身は以下の様な感じ。

```ini
VARNAME=<value>
```

### コマンドを指定する

```bash
docker run <container_name> <command>
```

