---
description: ターミナルで動く対話型gitクライアント
---

# [tig] Top

{{ page.meta.description }}

{{link("https://jonas.github.io/tig/")}}


インストール
------------

バージョン`2.5.1`の場合。

{{link("https://jonas.github.io/tig/INSTALL.html")}}


### ソースコードの取得

```
$ wget https://github.com/jonas/tig/releases/download/tig-2.5.1/tig-2.5.1.tar.gz
$ tar zvfx *.tar.gz
$ cd tig-2.5.1
```

### ビルド

#### 日本語不要の場合

```
$ make
```

#### 日本語必要の場合

```
$ make LDLIBS=-lncursesw CPPFLAGS=-DHAVE_NCURSESW_CURSES_H
```

### インストール(配置)

```
$ make install
```

`~/bin`配下に`tig`がインストールされる。

