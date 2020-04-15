# [CSS] Snippets


Grid Layout
-----------

{{link("https://qiita.com/kura07/items/486c19045aab8090d6d9")}}

!!! todo "align/justify, items/content などの挙動違いはまとめたい"


### justify/align items/self/content の違い

以下の動きを見ながら学ぶ。

{{link("https://developer.mozilla.org/ja/docs/Web/CSS/align-content")}}


flexbox
-------

チートシート

{{link("https://www.webcreatorbox.com/tech/css-flexbox-cheat-sheet")}}

サンドボックス

{{link("http://www.cssdesk.com/mTw7Q")}}

### 用語

本記事では領域をエリア、領域に配置する要素をアイテムと呼びます。

### アイテムを並べる方向

`flex-direction`を指定します。

| アイテムを並べる方向 | flex-direction   | イメージ         |
| -------------------- | ---------------- | ---------------- |
| 横                   | row (デフォルト) | ■■■           |
| 縦                   | column           | ■<br/>■<br/>■ |

### アイテムの並べ方を指定する

アイテムを並べるには`justify-content`を指定します。

| アイテムの並び方 | justify-content   | イメージ(flex-direction: rowの場合) |
| ---------------- | ----------------- | ----------------------------------- |
| 中央寄せ         | center            | `___■■■___`                      |
| 終点に寄せ       | flex-end          | `______■■■`                      |
| 等間隔(両端密着) | space-between     | `■___■___■`                      |
| 等間隔(両端空き) | space-around      | `_■__■__■_`                      |
| 等間隔(両端空き) | space-evenly      | `__■__■__■__`                    |

!!! question "中央寄せにならないときは..."

    containerのwidthを確認する。
    `width: 100%;`などを必要に応じて追加。

!!! warning "`space-evenly`について"

    IEは未対応なので要注意。
    
    {{refer("https://developer.mozilla.org/ja/docs/Web/CSS/justify-content")}}

### エリアの揃え方を指定する

エリアの揃え方は`align-items`を指定します。  
アイテムの並べる方向とは必ず別になります。

| アイテムの並び方 | align-items       | イメージ(flex-direction: rowの場合)            |
| ---------------- | ----------------- | ---------------------------------------------- |
| 中央揃え         | center            | `_________`<br/>`■■■______`<br/>`_________` |
| 終点揃え         | flex-end          | `_________`<br/>`_________`<br/>`■■■______` |


Elegant scrollbar
-----------------

```css
/* */
::-webkit-scrollbar {
  width: 10px;
  height: 10px;
}

::-webkit-scrollbar-track {
  border-radius: 10px;
  box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.1);
}

::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 50, 0.5);
  border-radius: 10px;
  box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.3);
}
```
