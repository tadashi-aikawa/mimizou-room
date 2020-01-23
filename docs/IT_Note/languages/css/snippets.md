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
