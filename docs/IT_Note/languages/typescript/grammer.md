# [TypeScript] 文法


リリースノートに記載された仕様
------------------------------

TypeScript2.0から公式リリースノートで紹介されている内容を紹介する。


!!! warning ""
    一部の仕様は後のリリースで変わっているため、過信はしないこと。  
    **現在確認している最新バージョンは <span class="emphasis">2.0</span> **


### [Null- and undefined-aware types](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#null--and-undefined-aware-types) {{minver(2.0)}}

`null`と`undefined`をそれぞれ型として認識できる

### [--strictNullChecks](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#--strictnullchecks) {{minver(2.0)}}

`--strictNullChecks` でstrict null checking modeが有効になる

|                           | strict null checking mode ON | strict null checking mode OFF |
|---------------------------|------------------------------|-------------------------------|
| `undefined`が代入できる型 | `undefined` `any` `void`     | 全ての型                      |
| `null`が代入できる型      | `null` `any`                 | 全ての型                      |
| `T`と`T | undefined` | 別の型とみなす               | ほぼ同一の型とみなす          |
| `T`と`T | null`      | 別の型とみなす               | ほぼ同一の型とみなす          |

### [Assigned-before-use checking](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#assigned-before-use-checking) {{minver(2.0)}}

strict null checking modeが有効のとき、変数の使用前に代入されていることをチェックする。

* `undefined`の場合は代入不要 (未代入が`undefined`相当)
* `null`の場合は代入が必要 (nullはObject)

### [Optional parameters and properties](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#optional-parameters-and-properties) {{minver(2.0)}}

`value?: T`と表現されたvalueは、型`T | undefined`となる.

### [Non-null and non-undefined type guards](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#non-null-and-non-undefined-type-guards) {{minver(2.0)}}

ifや三項演算子などの条件式でnull/undefinedの可能性がなくなったとき  
型`T | null`や型`T | undefined`は型`T`となる. 逆も同じ.

```ts
let stringOrNull = string | null
if (stringOrNull != null) {
  // この中ではstringOrNullはstring型
} else {
  // この中ではstringOrNullはnull
}
```

### [Dotted names in type guards](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#dotted-names-in-type-guards) {{minver(2.0)}}

Type guardがドット表記名をサポートした.  
`arg`や`param`だけでなく、`arg.x`や`param.y`、`arg.x.y`などでもガードが可能.

strict null checking modeではなくてもType guardは作用する.

### [Expression operators](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#expression-operators) {{minver(2.0)}}

オペランド(演算値)の型が`null`や`undefined`を含むとしても、結果はそれらを含まない。
ただし、`&&`や`||`は例外.

| 左オペランド型 | オペレータ | 右オペランド型 | 結果の型   |
|----------------|------------|----------------|------------|
| `T | null`     | `+`        | `T | null`     | `T`        |
| `T | null`     | `&&`       | `U`            | `U | null` |
| `T | null`     | `||`       | `U`            | `T | U`    |

### [Type widening](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#type-widening) {{minver(2.0)}}

strict null checking modeの有無によって、`null`や`undefined`を代入した変数の型が変わる.

`let x = null`のとき

| strict null checking mode | xの型  |
|---------------------------|--------|
| 有効                      | `null` |
| 無効                      | `any`  |

### [Non-null assertion operator](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#non-null-assertion-operator) {{minver(2.0)}}

`!`をつけると`null`や`undefined`の可能性がある変数から、`null`や`undefined`の可能性を排除できる.
たとえば`x: number | null`に対しては、`x!.`

Type guardsを使って型チェッカーが判断できるならその方がいい.

### [Control flow based type analysis](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#control-flow-based-type-analysis) {{minver(2.0)}}

文(`return`や`break`など)、式により型が限定される場合は絞り込む.

### [Tagged union types](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#non-null-assertion-operator) {{minver(2.0)}}

Discriminated union typesとも言う.

Union型で指定されたそれぞれのinterfaceやclassに固定の文字列リテラル(判別特性)を持たせる.  
if文やswitch文を使い判別特性の値で条件分岐したあと、Union型の候補は絞られる.

以下はShapeというUnion型と`kind`という判別特性を使った例.

```ts
interface Square {
  kind: "square";
  size: number;
}

interface Circle {
  kind: "circle";
  radius: number;
}

type Shape = Square | Circle
```

Shapeのオブジェクト`sh`に対して`if(sh.kind === "square") {...}`が真の場合、`...`の処理内で`sh`は`Square`型として扱われる.

※ 2.0だと判別特性(discriminant properties)はstringリテラルしか使えない


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


