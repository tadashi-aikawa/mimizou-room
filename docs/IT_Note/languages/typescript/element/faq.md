---
description: Element UIのFAQ
---

# [Element] FAQ

{{ page.meta.description }}


el-popover
----------

### `Cannot set property 'scrollTop' of undefined` エラーになる

el-popoverの中で`slot="reference"`が指定されているかを確認する。


el-select
---------

### 要素が正しく選択されない

`value`や`v-model`にObjectを指定した場合、`value-key`が正しく設定されているか確認する。


el-input
--------

### Enterが押された時に処理を実行したい

`@keyup.enter.native="callbackFunction"`でいける。  
`.native`がミソ。

{{refer("https://forum.vuejs.org/t/how-to-listen-for-an-enter-on-an-element-ui-form/11631")}}


el-menu
-------

### pathと同期するようにroutingしたい

`router`、`index`のpath指定、`default-active`をルーターのpathと同期がポイント。

```html
<el-menu router :default-active="$route.path">
  <el-menu-item index="top">TOP</el-menu-item>
  <el-menu-item index="config">CONFIG</el-menu-item>
</el-menu>
```

{{refer("https://stackoverflow.com/questions/53764461/element-ui-navmenu-gets-out-of-sync-with-current-route")}}
