---
description: Pytestのfixtureについて
---

# [Pytest] Fixture

{{ page.meta.description }}

以下の記事を参考にしている。

{{link("https://qiita.com/_akiyama_/items/9ead227227d669b0564e#%E3%83%86%E3%82%B9%E3%83%88%E3%82%AF%E3%83%A9%E3%82%B9%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E5%85%A8%E4%BD%93%E3%81%AB%E3%83%95%E3%82%A3%E3%82%AF%E3%82%B9%E3%83%81%E3%83%A3%E3%82%92%E8%87%AA%E5%8B%95%E6%91%98%E8%A6%81%E3%81%99%E3%82%8B")}}


fixtureのサンプル
-----------------

`conftest.py`を同階層に配置する。  
他にも色々方法はあるが、一番よく使うのがこれ。

以下はJumeauxサーバを立ち上げる例。

```python
@pytest.fixture(scope="module")
def boot_server():
    print("fixture: boot_server start")
    p = subprocess.Popen(["python", "jumeaux/main.py", "server"])
    yield

    pid = p.pid
    print(f"boot_server returned: {pid}")
    p.kill()
    print(f"boot_server killed: {pid}")
```

yiledの前後で意味合いが変わる。

* `yieldの前` scopeに入る前の処理
* `yieldの後` scopeを出た後の処理

yieldに値を指定すると、テストケースで返却値を受け取り処理できる。


Scope
-----

`@pytest.fixture(scope="module")`のようにデコレータで定義する。  
デフォルトは`function`。

| scope    | 実行ルール                           |
| -------- | ------------------------------------ |
| function | テスト関数ごとに実行される           |
| class    | クラスごとに実行される               |
| module   | モジュール(ファイル)ごとに実行される |
| session  | 1度だけ実行される                    |

`boot_server`の場合は各テストファイルごとに実行される。
