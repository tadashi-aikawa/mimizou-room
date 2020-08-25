# [Element] FAQ


el-popoverを使うとエラーになる
------------------------------

### `Cannot set property 'scrollTop' of undefined` になる場合

el-popoverの中で`slot="reference"`が指定されているかを確認してください


el-selectの要素が正しく選択されない
-----------------------------------

`value`や`v-model`にObjectを指定した場合、`value-key`が正しく設定されているか確認する。

