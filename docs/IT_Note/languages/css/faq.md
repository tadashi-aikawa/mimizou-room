# [CSS] FAQ


画像の色合いを変化させたい
--------------------------

`filter`を使って画像や要素の色合いをさせる。

{{link("http://www-creators.com/css-prop/filter")}}

* 背景を暗くするなら `filter:brightness(...)`


親要素の中央に配置したい
------------------------

親要素に `text-align: center` を追加する。


リンク(aタグ)の範囲を親要素まで広げたい
---------------------------------------

TODO: リンク先が消えた..


Linkの色を変更せずにaタグを使いたい(リンクしたい)
-------------------------------------------------

`inherit`で親のスタイルを引き継げばOK.

```css
a {
  color: inherit;
  text-decoration: inherit;
}
```


縦横比を維持したまま画像の大きさを調整したい
--------------------------------------------

`object-fit: contain`を使う。

{{refer("https://on-ze.com/archives/2296")}}


iframeのコンテンツを拡大/縮小したい
-----------------------------------

transformを使う。

```css
.inline-page {
  height: 600px;
  width: 1920px;
  transform: scale(0.55);
  transform-origin: 0 0;
  overflow: scroll;
}
```

```html
<iframe src="..." class="inline-page">
```

{{refer("https://blog.asial.co.jp/1314")}}


HTMLの記載順とDOMの配置順を変えたい
----------------------------------

`display: flex;`と`order`を使う。

```html
<div style="display: flex;">
  <div style="order: 2;">2つ目</div>
  <div style="order: 3;">3つ目</div>
  <div style="order: 1;">1つ目</div>
</div>
```

↓ 結果

<div style="display: flex;">
  <div style="order: 2;">2つ目</div>
  <div style="order: 3;">3つ目</div>
  <div style="order: 1;">1つ目</div>
</div>
