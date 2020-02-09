# [ESLint] FAQ


Vue.js`<template>`内の警告を無視したい
--------------------------------------

`<!-- eslint-disable-next-line ルール名 -->` を使う.

```html
    <!-- eslint-disable-next-line vue/no-v-html -->
    <p class="post-excerpt" v-html="post.excerpt || post.frontmatter.description || '' " />
```

{{refer("https://github.com/vuejs/eslint-plugin-vue/issues/260#issuecomment-416414771")}}
