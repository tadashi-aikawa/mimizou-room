---
description: PowerShellのFAQ
---

# [PowerShell] FAQ

{{ page.meta.description }}


Aliasに引数を渡したい
---------------------

3つポイントがある。

| ポイント                 | 理由                                 |
| ------------------------ | ------------------------------------ |
| `function`を使う         | `Set-Alias`は引数に対応していない    |
| まず`$input`をパイプする | これを付けないとパイプで連携できない |
| `$args`を付ける          | これが無いと引数が渡らない           |

`wc`を`uutils wc`にエイリアスしたい場合は以下の通り。

```
function wc() {
    $input | uutils wc $args
}
```

