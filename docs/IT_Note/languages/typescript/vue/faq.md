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
