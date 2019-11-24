# [Markdown] FAQ


テーブルの中でパイプをエスケープしたい
--------------------------------------

`&＃124;`を使用する。

{{refer("https://codeday.me/jp/qa/20190101/101563.html")}}


コンテンツを折りたたみたい
--------------------------

`<details>`と`<summary>`を使う。  
以下の条件を満たすと、`<details>`タグの内部にMarkdownを書ける。

* `<details>`タグ直下に`<div>`タグを配置する
* `<div>`タグ内のはじめに空行をいれる

例

```markdown
<details>
    <summary><b>(ﾟ∀ﾟ) v5.0 have breaking changes</b></summary>
    <div>

* `TIterator#group_by`
  * Return `TDict[TList[T]]` instead of `TDict[TIterator[T]]`
    </div>

</details>
```
