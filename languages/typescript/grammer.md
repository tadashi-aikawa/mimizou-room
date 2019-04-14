よく使う型
----------

https://log.pocka.io/posts/typescript-builtin-type-functions/

### Partial (2.1から)

すべてのプロパティをOptional(`|undefined`)にする。

### Required (2.8から)

すべてのプロパティをRequired(必須)にする。

### Readonly (2.1から)

すべてのプロパティを読みこみ専用(`readonly`)にする。

### Pick (2.1から)

ある型から特定のプロパティのみを抜き取った型を作る。

`type Pick<T, K extends keyof T>`と表現する。  
具体例は`Pick<Human, 'id' | 'name'>`のような感じ。


