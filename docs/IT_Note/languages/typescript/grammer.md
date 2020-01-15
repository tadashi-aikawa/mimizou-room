# [TypeScript] 文法


リリースノートに記載された仕様
------------------------------

TypeScript2.0から公式リリースノートで紹介されている内容を紹介する。


!!! warning ""
    一部の仕様は後のリリースで変わっているため、過信はしないこと。  
    **現在確認している最新バージョンは <span class="emphasis">2.0</span> **


### [Null- and undefined-aware types](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#null--and-undefined-aware-types) {{minver(2.0)}}

`null`と`undefined`をそれぞれ型として認識できる

#### [--strictNullChecks](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#--strictnullchecks) {{minver(2.0)}}

`--strictNullChecks` でstrict null checking modeが有効になる

|                           | strict null checking mode ON | strict null checking mode OFF |
|---------------------------|------------------------------|-------------------------------|
| `undefined`が代入できる型 | `undefined` `any` `void`     | 全ての型                      |
| `null`が代入できる型      | `null` `any`                 | 全ての型                      |
| `T`と`T | undefined` | 別の型とみなす               | ほぼ同一の型とみなす          |
| `T`と`T | null`      | 別の型とみなす               | ほぼ同一の型とみなす          |

#### [Assigned-before-use checking](taypescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#--strictnullchecks) {{minver(2.0)}}

strict null checking modeが有効のとき、変数の使用前に代入されていることをチェックする。

* `undefined`の場合は代入不要 (未代入が`undefined`相当)
* `null`の場合は代入が必要 (nullはObject)



よく使う型
----------

{{link("https://log.pocka.io/posts/typescript-builtin-type-functions/")}}

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


