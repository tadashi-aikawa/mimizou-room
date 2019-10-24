# [vue-fontawesome] FAQ


アイコンをクリックすると落ちる
------------------------------

以下のエラー

```txt
"TypeError: Cannot assign to read only property 'className' of object '#'"
```

以下のように`font-awesome-icon`が直接ブロック要素配下にあるとなぜか落ちる。

```html
<div>
  <font-awesome-icon icon="ellipsis-v"></font-awesome-icon>
</div>
```

`<span>`などで括ってあげれば回避できる。

```html
<div>
  <span>
    <font-awesome-icon icon="ellipsis-v"></font-awesome-icon>
  </span>
</div>
```

{{refer("https://github.com/ElemeFE/element/issues/13453")}}


アイコンによって幅が変わるのを統一したい
----------------------------------------

Classに`fa-fw`を指定すればOK.

```html
<font-awesome-icon class="fa-fw" />
```
