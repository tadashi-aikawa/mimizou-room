# [Pytest] FAQ


doctestも一緒に実行したい
-------------------------

`--doctest-modules`フラグを付ければ、対象エントリにdoctestが含まれると一緒に実行する。

同一テスト対象(関数など)に2つ以上テストがあり、1つ目で失敗した場合はそこで処理が止まってしまう。  
`--doctest-continue-on-failure`フラグを付けるとそれを回避できる。

全部盛り

```bash
pytest --doctest-modules --doctest-continue-on-failure
```

{{refer("http://doc.pytest.org/en/latest/doctest.html")}}


複数のディレクトリを無視したい
------------------------------

`omit`をカンマ区切りで複数指定する。

```
[run]
omit = tests/*,buspar/tmp.py
```
