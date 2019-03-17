decorator
---------

Nuxt(Vue)で使えるデコレータの数々をご紹介。

* [vue-property-decorator]: https://github.com/kaorun343/vue-property-decorator


### @Prop

```ts
@Prop(Number) readonly propA!: number
@Prop({ default: 'default value' }) readonly propB!: string
@Prop([String, Boolean]) readonly propC!: string | boolean
```

⚠️プロパティに初期値を設定してはいけません。デフォルト値は`default`で設定しましょう。

https://github.com/kaorun343/vue-property-decorator#-propoptions-propoptions--constructor--constructor---decorator
