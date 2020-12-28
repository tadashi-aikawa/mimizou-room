# [Pipenv] FAQ


`pipenv run`で警告が出る
------------------------

以下のような警告。

```
Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
```

`Pipfile`のある場所で実行したとき、既に現在別の仮想環境がActiveである場合は警告が出る。
`PIPENV_VERBOSITY=1`を付けることで抑制できる。

!!! warning ""
    テストで期待値を確認するときなど問題ないケースのみ抑制すること
