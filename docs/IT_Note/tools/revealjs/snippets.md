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

!!! warning "本ページの`theme.css`を使っていることが条件"

### タイトル

```html
# みみぞうとレイアウト  
~ Grid Layout ~

----

### tadashi-aikawa
2019-07-24 (Wed)

<!-- .slide: class="title"  data-background="https://dl.dropboxusercontent.com/s/c2qdld24ynb7boz/emiliano-vittoriosi-aTHqiz_sosU-unsplash.jpg" -->

```

### 中央に寄せて2列並べる

```html
<div class="grid-2x1">
    <img src="https://avatars0.githubusercontent.com/u/9500018?s=400&v=4" />
    <img src="https://avatars0.githubusercontent.com/u/9500018?s=400&v=4" />
</div>
```

### 中央に4分割でタイル表示

```html
<div class="grid-2x2" style="width: 500px; height: 500px;">
    <img src="https://avatars0.githubusercontent.com/u/9500018?s=400&v=4" />
    <img src="https://avatars0.githubusercontent.com/u/9500018?s=400&v=4" />
    <img src="https://avatars0.githubusercontent.com/u/9500018?s=400&v=4" />
    <img src="https://avatars0.githubusercontent.com/u/9500018?s=400&v=4" />
</div>
```

### 中央に9分割でタイル表示

```html
<div class="grid-3x3" style="width: 500px; height: 500px;">
    <img src="https://avatars0.githubusercontent.com/u/9500018?s=400&v=4" />
    <img src="https://avatars0.githubusercontent.com/u/9500018?s=400&v=4" />
    <img src="https://avatars0.githubusercontent.com/u/9500018?s=400&v=4" />
    <img src="https://avatars0.githubusercontent.com/u/9500018?s=400&v=4" />
    <img src="https://avatars0.githubusercontent.com/u/9500018?s=400&v=4" />
    <img src="https://avatars0.githubusercontent.com/u/9500018?s=400&v=4" />
    <img src="https://avatars0.githubusercontent.com/u/9500018?s=400&v=4" />
    <img src="https://avatars0.githubusercontent.com/u/9500018?s=400&v=4" />
    <img src="https://avatars0.githubusercontent.com/u/9500018?s=400&v=4" />
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

`theme.css`
```css
/* Base font options */
.reveal {
    font-size: 250%;
}

/* Images */
.reveal section img {
    border: none;
    box-shadow: none;
}

/* Title */
.reveal .title {
    font-size: 80%;
    color: white;
    text-shadow:  3px 3px 3px #37474F;
}

/* Title image */
.reveal .slide-background.present {
    filter: brightness(50%) grayscale(20%) sepia(40%) blur(5px);
}

/* Title headers */
.reveal .title h1 {
    color: white;
    text-shadow:  3px 3px 3px #37474F;
}

.reveal .title h3 {
    color: white;
    text-shadow:  3px 3px 3px #37474F;
}

/* Headers */
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

/* Emphasis */
.reveal strong {
    color: #F06292;
}

.reveal em {
    color: #42A5F5;
}

/* List */
.reveal ol li {
    font-weight: bolder;
    font-size: 75%;
}

.reveal ul li {
    font-weight: bolder;
    font-size: 75%;
}

/* Code */
.reveal pre {
    padding: 15px;
    background-color: #37474F;
}

/* Table */
.reveal .small-table {
    font-size: 75%;
}

/* Refer */
.reveal .refer {
    font-size: 12px;
}

.reveal .refer:before {
    content: "🔗";
}

/***********/
/* Layouts */
/***********/
.reveal .central-2 {
    display: flex;
    justify-content: space-around;
}

/* Need to specify width & height */
.reveal .grid-2x1 {
    display: grid;
    align-content: center;
    justify-content: center;
    align-items: center;
    justify-items: center;
    margin: auto;
    grid-column-gap: 5%;
    grid-template-columns: 40% 40%;
}

.reveal .grid-2x2 {
    display: grid;
    align-content: center;
    justify-content: center;
    align-items: center;
    justify-items: center;
    margin: auto;
    grid-row-gap: 5%;
    grid-column-gap: 5%;
    grid-template-rows: 40% 40%;
    grid-template-columns: 40% 40%;
}

.reveal .grid-3x3 {
    display: grid;
    align-content: center;
    justify-content: center;
    align-items: center;
    justify-items: center;
    margin: auto;
    grid-row-gap: 3%;
    grid-column-gap: 3%;
    grid-template-rows: 30% 30% 30%;
    grid-template-columns: 30% 30% 30%;
}
```