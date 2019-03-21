Actionが上手く動かない
--------------------

### dispatchをawaitしていない場合

dispatchはActionを呼び出すものです。  
Actionは非同期前提の処理なので、戻り値は`Promise<any>`です。

以下2点を確認してみてください。

* action functionをasyncしていること
* dispatchをawaitしていること
