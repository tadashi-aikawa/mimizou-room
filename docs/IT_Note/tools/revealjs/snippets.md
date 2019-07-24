# [REVEAL.JS] Snippets


ヘッダ
------

アニメーションはslide一択。  
highlightThemeはなんでも良い。

### 白背景

```yaml
theme : "white"
customTheme: "theme"
transition: "slide"
highlightTheme: "monokai"
logoImg: "TODO: Image URL"
slideNumber: true
```


よくある構成
------------

### タイトル

```markdown
# Title  
Sub title

----

### tadashi-aikawa
2019-07-22 (Mon)

<!-- .slide: class="title"  data-background="http://background" -->
```

### 中央に寄せて2列並べる

!!! todo "後でCSSに寄せたい"

```html
<div style="display: flex; justify-content: space-around;">
    <div>1</div>
    <div>2</div>
</div>
```

### 中央に9分割でタイル表示

!!! todo "後でCSSに寄せたい"

```html
<div style="text-align: center;">
    <div style="display: grid;
        width: 600px;
        align-items: center;
        justify-items: center;
        margin: auto;
        grid-template-rows: 33% 33% 33%;
        grid-template-columns: 33% 33% 33%;"
        >
        <div>1</div>
        <div>2</div>
        <div>3</div>
        <div>4</div>
        <div>5</div>
        <div>6</div>
        <div>7</div>
        <div>8</div>
        <div>9</div>
    </div>
</div>
```

### 参考文献(refer)表示

```html
<div class="refer">http://hogehoge</div>
```

### アニメーションのフェード表示

```markdown
### hoge <!-- .element class="fragment" -->
```


CSS
---

普段はコレ。

* `*補色*`
* `**強調色**`

### white用

```css
.reveal {
    font-size: 200%;
}

.reveal section img {
    border: none;
    box-shadow: none;
}

.reveal .title h1 {
    color: white;
    text-shadow:  3px 3px 3px #37474F;
}

.reveal .title h3 {
    color: white;
    text-shadow:  3px 3px 3px #37474F;
}

.reveal .title {
    color: white;
    text-shadow:  3px 3px 3px #37474F;
}

.reveal h1 {
    color: #37474F;
    text-transform: none;
}

.reveal h2 {
    color: #37474F;
    text-transform: none;
}

.reveal h3 {
    color: #37474F;
    text-transform: none;
}

.reveal h4 {
    color: #37474F;
    text-transform: none;
}

.reveal strong {
    color: #F06292;
}

.reveal em {
    color: #42A5F5;
}

.reveal ol li {
    font-weight: bolder;
    font-size: 75%;
}

.reveal ul li {
    font-weight: bolder;
    font-size: 75%;
}

.reveal pre {
    padding: 15px;
    background-color: #37474F;
}

.reveal .small-table {
    font-size: 75%;
}

.reveal .refer {
    font-size: 12px;
}

.reveal .refer:before {
    content: "🔗";
}
```