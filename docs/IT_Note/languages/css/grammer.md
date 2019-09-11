# [CSS] Grammer


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

| 名前 |  表現   |      意味      |
| ---- | ------- | -------------- |
| 子   | `a > b` | aの直下にあるb |
| 子孫 | `a b`   | aの配下にあるb |



### 疑似クラス

|    名前    |       表現       |               意味                |
| ---------- | ---------------- | --------------------------------- |
| アクティブ | `button:active`  | `<button>`が押されている時        |
| 無効       | `input:disabled` | `<input>`が無効な状態             |
| フォーカス | `input:focus`    | `<input>`がフォーカスを持っている |
| ホバー     | `a:hover`        | `<a>`にポインタがあたっている     |
| 訪問済み   | `a:visited`      | `<a>`の先が訪問済み               |