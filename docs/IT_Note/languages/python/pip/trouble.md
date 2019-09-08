# [Pip] FAQ


全般
----

### パッケージ(package)のインストール先ディレクトリを知りたい

```
$ pip show <package_name>
```

{{refer("https://qiita.com/t-fuku/items/83c721ed7107ffe5d8ff")}}

### Pipfileを使ってpip installしたい

pipはPipfileに対応していないため、`pipfile-requirements`を使います。

{{link("https://pypi.org/project/pipfile-requirements/")}}

```
pipfile2req > requirements.txt && pip install -r requirements.txt
```
