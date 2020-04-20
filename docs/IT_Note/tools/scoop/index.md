# [Scoop] Top


Scoopとは
---------

Windowsのためのpackage manager。

{{link("https://scoop.sh/")}}

[Chocolatey](../chocolatey)と比較すると、以下の点で優れている。

* 管理者権限不要
* 複数バージョンを安全に管理
* 安全なアンインストール
* LinuxツールのようなCLI Interface
* CLIコマンドが充実

一方、GUIやインストーラーに関するツールのラインナップは[Chocolatey](../Chocolatey)の方が上。


よく使う表現
------------

### パッケージインストール (最新)

```
scoop install <package_name>
```

### パッケージインストール (バージョン指定)

```
scoop install <package_name>@<version>
```

{{refer("https://github.com/lukesampson/scoop/wiki/FAQ")}}

### パッケージアンインストール

```
scoop uninstall <package_name>
```

### 対応パッケージ検索

```
scoop search <package_name>
```

### インストール済みパッケージ一覧

```
scoop list
```

### パッケージアップデート

```
scoop update <package_name>
```

全てアップデートする場合は

```
scoop update *
```

{{refer("https://github.com/lukesampson/scoop/wiki/FAQ")}}

### パッケージのデフォルトパスを変更

複数バージョンをインストールして、バージョン未指定を選びたい場合。

```
scoop reset <package_name>
```

`python`でpython3.7を参照させるには

```
scoop reset python37
```

{{refer("https://github.com/lukesampson/scoop/wiki/Switching-Ruby-And-Python-Versions")}}

### バケットの追加

```
scoop bucket add <bucket_name>
```

{{refer("https://github.com/lukesampson/scoop/wiki/Buckets")}}

### 追加したBucket一覧

```
scoop bucket known
```

{{refer("https://github.com/lukesampson/scoop/wiki/Buckets")}}

