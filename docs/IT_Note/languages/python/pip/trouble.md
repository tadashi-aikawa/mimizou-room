# [Pip] FAQ


全般
----

### パッケージ(package)のインストール先ディレクトリを知りたい

```bash
pip show <package_name>
```

{{refer("https://qiita.com/t-fuku/items/83c721ed7107ffe5d8ff")}}

### Pipfileを使ってpip installしたい

pipenvを使います。

```bash
pipenv lock -r > requirements.txt
```

{{refer("https://pipenv-ja.readthedocs.io/ja/translate-ja/advanced.html#generating-a-requirements-txt")}}

pipenvを使いたくない場合は、pipfile-requirementsを使います。  
ただし、こちらはエッジケースに対応していません。非推奨です。

```bash
pipfile2req > requirements.txt && pip install -r requirements.txt
```

{{link("https://pypi.org/project/pipfile-requirements/")}}
