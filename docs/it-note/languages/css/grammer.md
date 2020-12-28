# [CSS] Grammer


基本
----

{{link("https://developer.mozilla.org/ja/docs/Learn/Getting_started_with_the_web/CSS_basics")}}

![](https://mdn.mozillademos.org/files/9461/css-declaration-small.png)

* セレクタ (selector)
* 宣言 (declaration)
* プロパティ (property)
* プロパティ値 (property value)

セミコロン区切り


ボックス
--------

{{link("https://developer.mozilla.org/ja/docs/Learn/Getting_started_with_the_web/CSS_basics#Boxes_boxes_its_all_about_boxes")}}

![](https://mdn.mozillademos.org/files/9443/box-model.png)

### パディング構文

| 属性値の数 |         意味          |            覚え方            |
| ---------- | --------------------- | ---------------------------- |
| 1          | `padding 上下左右`    |                              |
| 2          | `padding 上下 左右`   | 上下左右                     |
| 3          | `padding 上 左右 下`  | ゲームコントローラを上から.. |
| 4          | `padding 上 右 下 左` | 時計の針が回る方向           |

{{refer("https://developer.mozilla.org/ja/docs/Web/CSS/padding#Syntax")}}


セレクタ
--------

{{link("https://developer.mozilla.org/ja/docs/Web/CSS/CSS_Selectors")}}

### 基本

|     名前     |           表現           |                      対象                      |
| ------------ | ------------------------ | ---------------------------------------------- |
| 要素         | `div`                    | `<div>`                                        |
| id           | `#id`                    | ID=`id`の要素                                  |
| クラス       | `.className`             | `className`クラスの要素                        |
| クラス(複数) | `.className1.className2` | `className1`と`className2`の両クラスを持つ要素 |
| 属性         | `a[href="http:.."]`      | `<a href="http:..."`>`                         |


### 結合子

| 名前 |  表現   |       意味       |
| ---- | ------- | ---------------- |
| 子   | `a > b` | aの直下にあるb   |
| 子孫 | `a b`   | aの配下にあるb   |
| 隣接 | `a + b` | aに隣接しているb |
| 後方 | `a ~ b` | aの後方にあるb   |


### 疑似クラス

|    名前    |       表現       |               意味                |
| ---------- | ---------------- | --------------------------------- |
| アクティブ | `button:active`  | `<button>`が押されている時        |
| 無効       | `input:disabled` | `<input>`が無効な状態             |
| フォーカス | `input:focus`    | `<input>`がフォーカスを持っている |
| ホバー     | `a:hover`        | `<a>`にポインタがあたっている     |
| 訪問済み   | `a:visited`      | `<a>`の先が訪問済み               |

### 属性セレクタ

|      名前      |        表現        |               意味               |
| -------------- | ------------------ | -------------------------------- |
| 属性有無       | `a[title]`         | title属性を持つaタグ             |
| 属性値指定     | `a[title="ほげ"]`  | title属性が`ほげ`のaタグ         |
| 属性値開始指定 | `a[title^="ほげ"]` | title属性が`ほげ`ではじまるaタグ |
| 属性値終了指定 | `a[title$="ほげ"]` | title属性が`ほげ`でおわるaタグ   |
| 属性値部分指定 | `a[title*="ほげ"]` | title属性に`ほげ`を含むaタグ     |

### セレクタの優先順位

{{link("http://creator.aainc.co.jp/archives/4947")}}

よく使うものを優先度高い順

1. `style`: 直接書く
2. `#id`: IDセレクタ
3. `.class`: クラスセレクタ
4. `div`: タイプセレクタ

UIはクラスセレクタで判別させることが多い。その場合は親階層から具体的に指定されている方が強い。


論理演算子
----------

{{link("https://qiita.com/ln-north/items/bbfd0c271594ce7c1536")}}

|             定義              |       記法        |
| ----------------------------- | ----------------- |
| aaクラス または bbクラス      | `.aa, .bb { }`    |
| aaクラス かつ bbクラス        | `.aa.bb { }`      |
| aaクラスではない              | `:not(aa) { }`    |
| (aaクラス かつ bbクラス) 以外 | `:not(.aa.bb) {}` |
