# [Pipenv] Snippets

{{link("https://pipenv-ja.readthedocs.io/ja/translate-ja/basics.html#example-pipenv-upgrade-workflow")}}


packageのインストール
---------------------

### Pipfileの内容でpackageをインストール

```
$ pipenv install
```

### Pipfileの内容でdev-packageとpackageをインストール

```
$ pipenv install --dev
```

### Pipfile.lockが古い場合はビルドを失敗させるようなインストール

フラグが無いと`Pipfile.lock`を最新にする。

```
$ pipenv install --deploy
```

### Pipfile.lockの指定通りにインストール

再ロックはしない。

```
$ pipenv sync
```

### Pipfile.lockの内容をインストール

Pipfileの内容は無視して完全に同じバージョンをインストールする。

```
$ pipenv install --ignore-pipfile
```

### Pipfile.lockを無視してインストール

Pipfileだけを参考にインストールする。Pipfile.lockも更新しない。

```
$ pipenv install --skip-lock
```

### preversionも対象にしてインストール

```
$ pipenv install --pre
```


packageのアンインストール
-------------------------

### Pipfileは触らずに全てアンインストール

```
$ pipenv uninstall --all
```

### Pipfileも含めて全てアンインストール

```
$ pipenv uninstall --all-dev
```


packageのバージョンアップ
-------------------------

lockファイルで指定されたバージョンより新しいバージョンがある場合に更新する。

{{link("https://pipenv-ja.readthedocs.io/ja/translate-ja/basics.html#example-pipenv-upgrade-workflow")}}

### 更新の確認

```
$ pipenv update --outdated
```

### 全てを更新

```
$ pipenv update
```

### 特定パッケージを更新

```
$ pipenv update <pkg>
```