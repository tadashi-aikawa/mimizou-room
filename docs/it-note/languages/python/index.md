# [Python] TOP

{{link("https://www.python.org/")}}


学習
----

### 公式ドキュメントをピックアップして超分かりやすく

{{link("https://python.ms/")}}

### package管理の歴史 (～2019年)

{{link("https://www.m3tech.blog/entry/python-packaging")}}


フレームワーク/ライブラリの選定
-------------------------------

### Pacakge Manager

|   名前   | 採用 | IDEAプラグイン | VSCode拡張 |
| -------- | ---- | -------------- | ---------- |
| [Pipenv] | O    | 不要           | 不要       |
| [Poetry] |      |                |            |

[Pipenv]: https://docs.pipenv.org/en/latest/
[Poetry]: https://poetry.eustace.io/


### Test

|   名前   | 採用 | IDEAプラグイン | VSCode拡張 |
| -------- | ---- | -------------- | ---------- |
| [Pytest] | O    | 不要           | 不要       |

[Pytest]: https://docs.pytest.org/en/latest/

Doctestも併用する


### Linter

|   名前   | 採用 | IDEAプラグイン | VSCode拡張 |
| -------- | ---- | -------------- | ---------- |
| [Pylint] | O    | [pylint-idea]  |            |
| flake8   |      |                |            |

[pylint]: https://pylint.readthedocs.io/en/latest/
[pylint-idea]: https://plugins.jetbrains.com/plugin/11084-pylint

### Formatter

|    名前    | 採用 |   IDEAプラグイン   | VSCode拡張 |
| ---------- | ---- | ------------------ | ---------- |
| [black]    | O    | あるが使わない[^1] | 不要       |
| [yapf]     |      | あるが使わない[^2] | 不要       |
| [autopep8] |      |                    |            |

[black]: https://github.com/python/black
[yapf]: https://github.com/google/yapf
[autopep8]: https://pypi.org/project/autopep8/

[^1]: File Wathersプラグインを使っているため
[^2]: 日本語が文字化けするため


### CLI

|  名前   | 採用 | IDEAプラグイン | VSCode拡張 |
| ------- | ---- | -------------- | ---------- |
| [owcli] | O    |                |            |

[owcli]: https://github.com/tadashi-aikawa/owcli


### 関数型系

|  名前   | 採用 | IDEAプラグイン | VSCode拡張 |                  備考                  |
| ------- | ---- | -------------- | ---------- | -------------------------------------- |
| [fn.py] | O    |                |            | `pip install fn` -> `from fn import _` |

[fn.py]: https://github.com/kachayev/fn.py



Gitリポジトリにあるパッケージのインストール
-------------------------------------------

```
$ pip install git+<リポジトリ URL>
```

{{refer("https://www.lifewithpython.com/2018/07/python-install-package-dev-versions.html")}}


よくやる環境構築
----------------

### 環境構築と開発ツールのインストール

#### owcli使わない場合

```
$ pipenv install --python 3.7
$ pipenv install --dev --pre black pylint
$ pipenv shell
```

#### owcli使う場合

```
$ owcli init <app_name>
$ pipenv install --python 3.7
# ここまでowcliのPipfileに記載してしまってもいいかも。。
$ pipenv install --dev --pre black pylint
$ pipenv shell
```

### `.pylintrc`作成

`owcli init` 内で生成してしまうのもアリ?

```
$ pylint --generate-rcfile > .pylintrc
```

### `pyproject.toml`作成

テンプレートに含めてしまうのもアリ?

<script src="https://gist.github.com/tadashi-aikawa/697f228f7b0c1d333e15d887deff8a96.js?file=pyproject.toml"></script>

### .gitignore作成

owcliに組み込んでしまった方がいいかも。。
gitも初期化してしまった方がいいかも。。

```
$ curl "https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore" > .gitignore
$ echo /.idea >> .gitignore
```

### .editorconfigの作成

<script src="https://gist.github.com/tadashi-aikawa/697f228f7b0c1d333e15d887deff8a96.js?file=.editorconfig"></script>
