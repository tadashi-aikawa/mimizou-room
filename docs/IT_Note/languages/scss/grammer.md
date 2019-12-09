# [SCSS] Grammer


基本
----

{{link("https://dev.classmethod.jp/slide/scss-tutorial/")}}

### ネスト

```scss
div {
    width: 100px;

    a {
        color: red;
    }
}
```

### インポート

拡張子不要

```scss
@import "http://hoge/scssfile"
```

### 変数

```scss
$var: value
```

* 呼び出しも`$var`
* セレクタやプロパティに使う場合は `#{$var}`
* valueの後に`!default`をつけると変数のデフォルト値

### コメント

```scss
// comment
```

