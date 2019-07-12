# [Nuxt] FAQ


Actionが上手く動かない
--------------------

### dispatchをawaitしていない場合

dispatchはActionを呼び出すものです。  
Actionは非同期前提の処理なので、戻り値は`Promise<any>`です。

以下2点を確認してみてください。

* action functionをasyncしていること
* dispatchをawaitしていること


v-ifやv-forが上手く動かない
---------------------------

コロンがついていないことを確認してください。 `:v-for`や`:v-if`はNG。


外部packageのコンポーネントが無いと言われる
-------------------------------------------

`nuxt.config.ts`の`plugins`に追加されていることを確認してください。

