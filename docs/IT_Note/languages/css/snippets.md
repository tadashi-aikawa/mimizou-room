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

### 横並び

```
|■■■        |
```

```css
.container {
    display: flex;
}
```

### 水平中央揃え

```
|    ■■■    |
```

```css
.container {
    display: flex;
    justify-content: center;
}
```

!!! question "中央寄せにならないときは..."

    containerのwidthを確認する。
    `width: 100%;`などを必要に応じて追加。


### 水平右揃え

```
|        ■■■|
```

```css
.container {
    display: flex;
    justify-content: flex-end;
}
```

### 両脇とその間に等間隔

```
|■    ■    ■|
```

2つの要素を左と右に寄せたいとき便利。

```css
.container {
    display: flex;
    justify-content: space-between;
}
```


色合い変化
----------

`filter`を使って画像や要素の色合いをさせる。

{{link("http://www-creators.com/css-prop/filter")}}

* 背景を暗くするなら `filter:brightness(...)`


親要素の中央に配置する
----------------------

親要素に `text-align: center` を追加する。


Linkの色を変更しない
--------------------

visitedの色を指定する。

```
a:visited {
    color: #00F;
}
```


親要素にリンク(aタグ)の範囲を広げる
-----------------------------------

{{link("https://webcode-lab.com/topics/blogid/9/")}}


縦横比を維持したまま画像の大きさを調整する
------------------------------------------

`object-fit: contain`を使う。

{{refer("https://on-ze.com/archives/2296")}}
