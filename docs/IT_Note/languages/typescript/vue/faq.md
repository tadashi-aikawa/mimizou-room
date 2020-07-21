# [Vue] FAQ


`scoped`スタイルの子コンポーネントを指定したい
----------------------------------------------

`XXXComponent`内に`inner`クラスが存在するけど、scoped属性でスタイル指定したい場合に...

```css
<template>
  <XXXComponent />
</template>
<style scoped>
>>> .inner {
  width: 18px;
}
</style>
```

{{refer("https://vue-loader-v14.vuejs.org/ja/features/scoped-css.html#%E3%83%87%E3%82%A3%E3%83%BC%E3%83%97%E3%82%BB%E3%83%AC%E3%82%AF%E3%82%BF")}}


`v-model`で指定したプロパティが同期しない
-----------------------------------------

### `:v-model="hoge"`のように`v-bind`形式になっている

`v-if`や`v-for`と同様、`v-model`に`:`の前置は不要.

### `v-model="_hoge"`のようにアンダースコアで始まった名前になっている

アンダースコアから始まるプロパティはVueで正しく動作しない. (プロキシされない)

{{refer("https://jp.vuejs.org/v2/api/#data")}}


変更があってもcomputed propertyが再計算されない
-----------------------------------------------

computedの式で参照しているプロパティが初期化されているかを確認する。  
`undefined`の代入もNG。

`NGの例`
```
const hoge: string | null;
const hoge: string | undefined = undefined;
```

`OKの例`
```
const hoge: string | null = "";
const hoge: string | null = null;
```


パーツがクリックされたら表示されるダイアログコンポーネントを作りたい
--------------------------------------------------------------------

最小構成で以下のような感じ。  
`<slot></slot>`の部分にトリガーとなるパーツを外側から指定する。

```vue
<template>
  <div>
    <v-dialog v-model="state.visible">
      <template v-slot:activator="{ on, attrs }">
        <div v-bind="attrs" v-on="on">
          <slot></slot>
        </div>
      </template>
      <div>なかみ</div>
    </v-dialog>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from "@vue/composition-api";

export default defineComponent({
  setup(props) {
    const state = reactive({
      visible: false,
    });

    return {
      state,
    };
  },
});
</script>
```

呼び出し側。

```vue
<your-dialog>
    <button>トリガーとなるパーツ</button>
<your-dialog>
```
