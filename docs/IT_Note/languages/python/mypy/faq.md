# [mypy] FAQ


クラスや関数のtype checkを無効化したい
--------------------------------------

`@typing.no_type_check`を使う.

{{refer("https://docs.python.org/ja/3/library/typing.html#typing.no_type_check_decorator")}}


Skipping analyzingというエラーが出る
------------------------------------

`mypy.ini`に以下を追加する。

```ini
[mypy]
ignore_missing_imports = True
```
