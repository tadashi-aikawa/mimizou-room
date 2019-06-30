# [Pipenv] Snippets


installのオプション
-------------------

### Pipfile.lockやPythonバージョンを確認してインストール

```
$ pipenv install --deploy
```

### Pipfile.lockの内容をインストール

Pipfileの内容は無視して完全に同じバージョンをインストールする。

```
$ pipenv install --ignore-pipfile
```

### Pipfile.lockはいじらない

```
$ pipenv install --skip-lock
```

### preversionも対象にしてインストール

```
$ pipenv install --pre
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