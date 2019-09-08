# [YAML] Grammer

文法チェック + パース後の値が確認できるサイト

{{link("http://yaml-online-parser.appspot.com/")}}

ここで確認しよう。


複数行テキストと改行
--------------------

以下の`???`に何が入るかでパース結果は変わる。

```yaml
text: ???
  aaa
  bbb


eof: eof
```

| `???`に入るリテラル  |  パース後のtext  |                  備考                  |
| -------------------- | ---------------- | -------------------------------------- |
| <code>&#124;</code>  | `aaa\nbbb\n`     | 文中の改行は改行                       |
| <code>&#124;+</code> | `aaa\nbbb\n\n\n` | 次の項目が出現するまでを改行として扱う |
| <code>&#124;-</code> | `aaa\nbbb`       | 項目の完了後は改行として扱わない       |
| <code>></code>       | `aaa bbb\n`      | 文中の改行は空白区切り                 |
| <code>>+</code>      | `aaa bbb\n\n\n`  | 次の項目が出現するまでを改行として扱う |
| <code>>-</code>      | `aaa bbb`        | 項目の完了後は改行として扱わない       |


アンカーとエイリアス
--------------------

* `&hoge`でアンカー
* `*hoge`でエイリアス
* `<<: *hoge`でマージ

こんな感じ。

<div class="flex">

```yaml
created_by: &created_by tadashi-aikawa
basic: &nationally
  nationally: japanese
companies:
  mamansoft: &mamansoft
    company_id: 100
    options:
      - Full flex
      - Remote work

members:
  - id: 1
    name: Ichiro
    company: *mamansoft
    <<: *nationally
    author: *created_by
  - id: 2
    name: Jiro
    author: *created_by
```

<div class="flex-item">----></div>

```json
{
  "companies": {
    "mamansoft": {
      "company_id": 100,
      "options": [
        "Full flex",
        "Remote work"
      ]
    }
  },
  "created_by": "tadashi-aikawa",
  "members": [
    {
      "id": 1,
      "company": {
        "company_id": 100,
        "options": [
          "Full flex",
          "Remote work"
        ]
      },
      "nationally": "japanese",
      "name": "Ichiro",
      "author": "tadashi-aikawa"
    },
    {
      "id": 2,
      "name": "Jiro",
      "author": "tadashi-aikawa"
    }
  ],
  "basic": {
    "nationally": "japanese"
  }
}
```

</div>
