# [Python] TOP

<a href="https://www.python.org/" class="card">Python</a>


学習
----

公式ドキュメントやソースコードを読むキッカケに..

<a href="https://python.ms/" class="card">Mastering Python</a>


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

[pylint]: http://pylint.pycqa.org/en/latest/
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


Gitリポジトリにあるパッケージのインストール
-------------------------------------------

📖 https://www.lifewithpython.com/2018/07/python-install-package-dev-versions.html
