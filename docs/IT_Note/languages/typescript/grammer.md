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

### [The never type](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#the-never-type) {{minver(2.0)}}

発生しない値の型 `never`型 (primitive)

* `never`型の変数は、すべての型に割り当てることができる (すべてsubtype)
* `never`型でない変数は、`never`型に割り当てることができない

出現するケース

* 関数の最後に到達しない関数 (必ずthrowするなど)

関数が`never`以外を返す可能性があるとき、戻り値の型に`never`は出現しない.  
なぜなら、すべての型のsubtypeであるから.

### [Read-only properties and index signatures](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#read-only-properties-and-index-signatures) {{minver(2.0)}}

`readonly`を付けると、プロパティやインデックスを読み取り専用にできる.  
すると代入ができなくなる(コンストラクタは例外).

*readonlyのプロパティが持つプロパティは自動でreadonlyにならないので注意*

```ts
class Human {
  constructor(public readonly readArg: number, public name: string, public readonly favorite?: Human){}
}

const tatsuwo = new Human(100, "tatsuwo", new Human(330, "mimizou"))

tatsuwo.readArg = 5   // Error
tatsuwo.name = "hoge" // OK
tatsuwo.favorite = new Human(333, "mitsuwo") // Error
tatsuwo.favorite.name = "MITSUWO" // OK
```

### [Specifying the type of this for functions](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#specifying-the-type-of-this-for-functions) {{minver(2.0)}}

関数内で使うthisの型を指定できる. (Classの場合だけ?)

普通に書くとcはany型になる. 

??? question "this型になった?"

    cがany型ではなくthis型と判断された..後のリリースで仕様が変わった?


```ts
class Caluculator {
  add(x: number, y: number): number {
    const c = this; // c: any
    return x + y;
  }
}

const calc = new Caluculator();
console.log(calc.add(1, 2));
```

Pythonのselfみたいに第1引数にthisを指定すると、thisの型を強制できる.

```ts
class Caluculator {
  add(this: Caluculator, x: number, y: number): number {
    const c = this; // c: Caluculator
    return x + y;
  }
}

const calc = new Caluculator();
console.log(calc.add(1, 2));      // 第1引数のthisはスルーされる
```

### [this parameters in callbacks](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#this-parameters-in-callbacks) {{minver(2.0)}}

コールバック関数の第1引数に`this: void`を指定することで、`this`の禁止を強要できる.  
※ コールバックの`this`はバグの温床だからね！

`onclick: (e: Event) => ...`ではなく`onclick: (this: void, e: Event) => ...`にすると..

```ts
interface UIElement {
  addClickListener(onclick: (this: void, e: Event) => void): void;
}
```

どのような形で`this`を使おうとしても、type checkの時点でエラーになる.

```ts
class Handler {
  info: string;

  // `this: Handler` としたとき
  onClickBad(this: Handler, e: Event) {
    this.info = e.message;
  }
}
// Error: `onClickBad(this: Handler, e: Event)` に `(this: void, e: Event) => void` は代入できない
({} as UIElement).addClickListener((new Handler()).onClickBad);
```

```ts
class Handler {
  info: string;

  // `this: void` としたとき
  onClickBad(this: void, e: Event) {
    // Error: infoはvoid型に存在しない！
    this.info = e.message;
  }
}
({} as UIElement).addClickListener((new Handler()).onClickBad);
```

### [--noImplicitThis](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#--noimplicitthis) {{minver(2.0)}}

`--noImplicitThis`を有効にすると、`this`の方が明示されていない場合エラーになる.

??? question "this型になった?"

    エラーにならず`this`型と判断された.. 後のリリースで`this`型に対応したから?)

### [Base URL](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#base-url) {{minver(2.0)}}

`compilerOptions.baseUrl`にパスを指定すると、相対名のないimportは`tsconfig.json`を基点とした指定値からの相対パスとなる.  
`tsconfig.json`の場所を`~/typescript-sample`としたとき、`"baseUrl": "./foo/bar"`なら以下は同じ.

* `import "foo/bar"`
* `import "~/typescript-sample/foo/bar"`

AMD moduleをロードする場合に使う.

### [Path mapping](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#path-mapping) {{minver(2.0)}}

特定のmoduleだけ`baseUrl`配下の特定ファイルを読み込みたい場合、`paths`にkey-value形式で指定できる.

`import "moduleName"`のような簡潔表記が可能になる.

Nuxt.jsの`tsconfig.json`では以下のようにRoot直下のパスをどこからでも`~/...`や`@/...`で指定可能になっている.

```
    "baseUrl": ".",
    "paths": {
      "~/*": ["./*"],
      "@/*": ["./*"]
    },
```

### [Virtual Directories with rootDirs](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#virtual-directories-with-rootdirs) {{minver(2.0)}}

複数のディレクトリがあたかも同じディレクトリであるかのように見せてimportができる.

ファイル構成

```
* src
  * one
    * one1.ts
  * other
    * other1.ts
```

`tsconfig.json`の設定に`rootDirs`を入れる.

```
    "rootDirs": [
      "src/one",
      "src/other"
    ]
```

すると、`one1.ts`と`other1.ts`はお互いがカレントディレクトリにいるものとしてimportできる.

`one1.ts`

```ts
import { add } from './other1';  // src/one と src/other は同ディレクトリと判断されるためOK
export function add3(a: number, b: number, c: number): number {
  return add(add(a, b), c);
}
```

`other1.ts`

```ts
export function add(a: number, b: number): number {
  return a + b;
}
```

### [Tracing module resolution](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#tracing-module-resolution) {{minver(2.0)}}

`--traceResolution`オプションを付けると、コンパイラがモジュールの依存関係をどう解決したか表示できる.

### [Shorthand ambient module declarations](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#shorthand-ambient-module-declarations) {{minver(2.0)}}

以下のような`index.d.ts`のような型定義ファイルを作成すると、any型としてmoduleをインポートできる.

```
declare module "your-import-module"
```

型定義ファイルはないが、とりあえず動かしたいときに有効.


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


