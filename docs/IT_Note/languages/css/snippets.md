flexbox
-------

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

⚠️ 中央寄せにならないときはcontainerのwidthを確認してください (`width: 100%;`などを必要に応じて追加)


Linkの色を変更しない
--------------------

visitedの色を指定する。

```
a:visited {
    color: #00F;
}
```