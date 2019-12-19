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

{{link("https://webcode-lab.com/topics/blogid/9/")}}


Linkの色を変更せずにaタグを使いたい(リンクしたい)
-------------------------------------------------

visitedの色を指定する。

```
a:visited {
    color: #00F;
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