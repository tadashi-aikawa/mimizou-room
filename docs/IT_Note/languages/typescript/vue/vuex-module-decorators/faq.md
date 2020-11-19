---
description: vuex-module-decoratorsのFAQ
---

# [vuex-module-decorators] FAQ

{{ page.meta.description }}


ERR_ACTION_ACCESS_UNDEFINEDになる
---------------------------------

以下のようなエラーになるが、Actionの中で直接値変更などはしていない場合。

```
index.js:363 Uncaught (in promise) Error: ERR_ACTION_ACCESS_UNDEFINED: Are you trying to access this.someMutation() or this.someGetter inside an @Action? 
That works only in dynamic modules. 
If not dynamic use this.context.commit("mutationName", payload) and this.context.getters["getterName"]
Error: Could not perform action updateSlackConfig
```

Actionアノテーションに`rawError: true`を指定する。  
これを付けないとAction内で発生したエラーが正しく表示されない。

```
@Action({ rawError: true })
```

基本的に必ず付けた方がいいからglobal設定の方がオススメ。

{{link("https://github.com/championswimmer/vuex-module-decorators#configuration-1")}}
