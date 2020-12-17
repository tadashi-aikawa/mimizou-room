---
description: Element UIのFAQ
---

# [Element] FAQ

{{ page.meta.description }}



el-popoverを使うとエラーになる
------------------------------

### `Cannot set property 'scrollTop' of undefined` になる場合

el-popoverの中で`slot="reference"`が指定されているかを確認してください


el-selectの要素が正しく選択されない
-----------------------------------

`value`や`v-model`にObjectを指定した場合、`value-key`が正しく設定されているか確認する。


el-inputでEnterが押された時に処理を実行したい
---------------------------------------------

`@keyup.enter.native="callbackFunction"`でいける。  
`.native`がミソ。

{{refer("https://forum.vuejs.org/t/how-to-listen-for-an-enter-on-an-element-ui-form/11631")}}
