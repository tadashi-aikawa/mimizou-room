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

コロンがついていないことを確認する。 `:v-for`や`:v-if`はNG。


イベントハンドラが上手く動かない
--------------------------------

`:click`のように間違えて`:`を付けていないか確認する。  
正解は`@click`


Vueクラスのdataを変更してもViewが更新されない(再計算されない)
-------------------------------------------------------------

以下のように初期値の代入忘れがないか確認する。  

```
name: str
```

初期値が無いとVueのdataとは見なされずに更新されない。

nullでも以下のように明示的指定が必要。

```
name: str | null = null
```


外部packageのコンポーネントが無いと言われる
-------------------------------------------

`nuxt.config.ts`の`plugins`に追加されていることを確認する。


コンポーネントにHTMLやコンポーネントをネストさせたい
----------------------------------------------------

`slot`を使う。

{{link("https://jp.vuejs.org/v2/guide/components-slots.html")}}

以下のような`InnerComponent`を差し込みたい場合...

```html
<YourComponent key=value>
    <InnerComponent />
</YourComponent>
```

以下のように書くと...

```vue
<template>
    <div>
        <p>コンポーネントの中身</p>
        <slot></slot>
    </div>
</template>
```

`<slot></slot>`の部分に`<InnerComponent />`が差し込まれる。

名前付きもできる。
