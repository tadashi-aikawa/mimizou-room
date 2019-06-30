# [CSS] Snippets


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
