decorator
---------

Nuxt(Vue)で使えるデコレータの数々をご紹介。

* [vue-property-decorator]: https://github.com/kaorun343/vue-property-decorator
* [vuex-class]: https://github.com/ktsn/vuex-class

上記は[nuxt-property-decorator](https://github.com/nuxt-community/nuxt-property-decorator)でまとめて使用できます。


### @Prop

```ts
@Prop(Number) readonly propA!: number
@Prop({ default: 'default value' }) readonly propB!: string
@Prop([String, Boolean]) readonly propC!: string | boolean
```

⚠️プロパティに初期値を設定してはいけません。デフォルト値は`default`で設定しましょう。

https://github.com/kaorun343/vue-property-decorator#Prop


### @Watch

```ts
@Watch('child')
onChildChanged(val: string, oldVal: string) { }
@Watch('person', { immediate: true, deep: true })
onPersonChanged1(val: Person, oldVal: Person) { }
```

* `immediate`はwatch開始時に開幕フックが呼ばれる
* `deep`を`true`にしないとネストされたObjectの中が変更された場合に通知されない

https://github.com/kaorun343/vue-property-decorator#Watch


### @Emit

```ts
@Emit()
yourFunctionName() {}
@Emit('your-function-name')
yourFunctionName2() {}
```

* 引数を指定しないと関数名をkebab-caseに変換した名称が使われる

https://github.com/kaorun343/vue-property-decorator#Emit


### @Action

`store.dispatch`の呼び出しと同じ。

```ts
@Action baz
@Action('foo') actionFoo

this.actionFoo({ value: true }) // -> store.dispatch('foo', { value: true })
```

https://github.com/ktsn/vuex-class


### @Mutation

`store.commit`の呼び出しと同じ。

```ts
@Mutation baz
@Mutation('foo') mutationFoo

this.mutationFoo({ value: true }) // -> store.commit('foo', { value: true })
```

https://github.com/ktsn/vuex-class


### @Getter

`store.getter`の呼び出しと同じ。

```ts
@Getter baz
@Getter('foo') getterFoo

this.getterFoo // -> store.getters.foo
```

https://github.com/ktsn/vuex-class


### @State

```ts
@State foo
@State('foo') stateFoo
@State(state => state.bar) stateBar

this.stateFoo // -> store.state.foo
this.stateBar // -> store.state.bar
```

State直下でない場合は引数が必要。

https://github.com/ktsn/vuex-class


CSS(style)の切り替え
--------------------

### bool値の結果によってclassをつける

付けるか付けないかの場合
https://jp.vuejs.org/v2/guide/class-and-style.html
