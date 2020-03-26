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

```ts
declare module "your-import-module"
```

型定義ファイルはないが、とりあえず動かしたいときに有効.

### [Wildcard character in module names](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#wildcard-character-in-module-names) {{minver(2.0)}}

型定義のmodule宣言対象にワイルドカードを指定できる.  
たとえば`declare module '*.json'`のようにすると、全てのjsonファイルがインポート対象になる.

`*!text`や`json!*`でprefix/suffix指定表現にも対応できる.  
ただ実行時までの間にパスを解決する必要があるためWebpackなどのツールチェーンが必要なはず.

### [Optional class properties](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#optional-class-properties) {{minver(2.0)}}

strict null checking modeが有効のとき、クラスプロパティに`?`をつけると` | undefined`になる.

```ts
class Hoge {
  a?: number
  b?(): string
}
```

* `a`は`number | undefined`になる
* `b`は`(() => string) | undefined`になる

### [Private and Protected Constructors](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#private-and-protected-constructors) {{minver(2.0)}}

privateやprotectedのコンストラクタを作ることができる.

| 可視性    | 外部からの呼び出し(new) | 継承 |
|-----------|-------------------------|------|
| private   | O                       | X    |
| protected | O                       | O    |
| public    | O                       | O    |

### [Abstract properties and accessors](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#abstract-properties-and-accessors) {{minver(2.0)}}

abstractクラスには以下を定義できる.

* abstract プロパティ
* abstract getter
* abstract setter

### [Implicit index signatures](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#implicit-index-signatures) {{minver(2.0)}}

index signature (`{[key: string]: number}`など) にObject literalを割り当てることができる.  
ただし、値の型が等しい場合のみ.  
※ 今回のケースでは`number`

```ts
function func(arg: { [key: string]: number }) {
  console.log(arg);
}

const obj = {
  key1: 1,
  key2: 1,
  3: 1,
};

func(obj);
```

keyは型が一致していなくても動作する.

### [Including built-in type declarations with --lib](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#including-built-in-type-declarations-with---lib) {{minver(2.0)}}

`--lib`や`compilerOptions.lib`でランタイムに含まれるAPIを指定できる.  
たとえば、`dom`を追加すると`document`などの型が認識される.

`tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "es2018",
    "lib": ["es2018", "dom"]
  }
}
```

### [Flag unused declarations with --noUnusedParameters and --noUnusedLocals](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#flag-unused-declarations-with---nounusedparameters-and---nounusedlocals) {{minver(2.0)}}

使われていないパラメータやローカル変数があるとエラーになる.

| パラメータ             | エラーの対象                                                 |
|------------------------|--------------------------------------------------------------|
| `--noUnusedParameters` | 使われていない関数やメソッドの引数                           |
| `--noUnusedLocals`     | 使われていない/exportされていない宣言(変数/関数/クラス..etc) |

パラメータ/変数の名前を`_`から始めると検査対象から除外される.


### [Module identifiers allow for .js extension](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#module-identifiers-allow-for-js-extension) {{minver(2.0)}}

`import d from "./moduleA.js"`のように`.js`拡張子を付けてインポートできるようになった.

* 2.0以前
    * `moduleA.js.ts` or `moduleA.js.d.ts` を探しにいく
* 2.0以降
    * `moduleA.ts` or `moduleA.d.ts` を探しにいく

### [Support ‘target : es5’ with ‘module: es6’](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#support-target--es5-with-module-es6) {{minver(2.0)}}

`target: es5`と`module: es6`の組み合わせが不正ではなくなった.

!!! question "メリットは分からず..."

### [Trailing commas in function parameter and argument lists](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#trailing-commas-in-function-parameter-and-argument-lists) {{minver(2.0)}}

関数定義の引数リストや、関数の引数リストに末尾カンマが許容されるようになった.

```ts
function hoge(
  a: int,
  b: int,
) {
  return a + b
}

hoge(
  1,
  2,
)
```

改行で区切って無くてもOK. ただ末尾カンマをつけたいのは通常改行時 (diffを見やすくするため)

### [New --skipLibCheck](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#new---skiplibcheck) {{minver(2.0)}}

`--skiplibcheck`をコンパイル時にオプションとして付けると、`d.ts`ファイルの型検査をスキップする.

!!! question "...↑と書いてあるのだけどスキップしてくれない。。なぜ。。。"

### [Allow duplicate identifiers across declarations](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#allow-duplicate-identifiers-across-declarations) {{minver(2.0)}}

複数の同一名称型において、重複する識別子を許容する.

以下は問題なしとなる。

```ts
interface Hoge {
  hoge1: string;
}

interface Hoge {
  hoge1: string;
  hoge2: string;
}

const hoge = {
  hoge1: '11',
  hoge2: '22',
}
```

一方、同一ブロック内の重複はNG.

```ts
interface Hoge {
  hoge1: string;
  hoge2: string;
  hoge1: string;  // これはエラー
}
```

### [New --declarationDir](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#new---declarationdir) {{minver(2.0)}}

`.d.ts`ファイルの出力ディレクトリを指定できる.

```console
tsc --declaration --declarationDir ${dirname}
```

もちろん`tsconfig.json`の`declaration`と`declarationDir`を指定してもOK.


### [keyof and Lookup Types] {{minver(2.1)}}

[keyof and Lookup Types]: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-1.html#keyof-and-lookup-types

* `keyof T`で`TのプロパティからなるUnion Type`を表現できる
* `T[K]`はlookup typesと呼ばれ、`T`のプロパティ`K`と同様の型と判断される.

`<T, K extends keyof T>`のような構文は頻出する.  

stringのUnion typeはstringのsubtypeである.  
同じく、UnionType`T1`が別のUnionType`T2`に完全に包含される場合、`T1`は`T2`のsubtypeであり`T1 extends T2`である.

`T`を以下のように定義したとき

```ts
class T {
  p1: string
  p2: number
}
```

* `keyof T`は`"p1" | "p2"`である
* 型`"p1"`は`"p1" | "p2"`のsubtypeである
* 型`"p2"`は`"p1" | "p2"`のsubtypeである

それゆえ

`<T, "p1">` または `<T, "p2">` => `<T, K extends "p1" | "p2">` => `<T, K extends keyof T>`

といえる.


### [Mapped Types] {{minver(2.1)}}

[Mapped Types]: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-1.html#mapped-types

`[P in keyof T]`と書くと、ある型のプロパティを利用して型を定義できる.

たとえば、ある型`T`に対して、すべてのプロパティをOptionalにする型を以下のように作成できる.

```ts
type Partial<T> = {
  [P in keyof T]?: T[P]
}
```


Tが`interface Human { id: number, name: string }`のとき、Pythonのような疑似表記を交えて書くと..

↓ `keyof T`は`T`のUnion Typeなので

```ts
type Partial<Human> = {
  for P in ['id', 'name']:
    P?: Human[P]
}
```

↓ for文を回すと..

```ts
type Partial<Human> = {
  id?: Human['id']
  name?: Human['name']
}
```

↓ Lookup Typesより..

```ts
type Partial<Human> = {
  id?: number
  name?: string
}
```

となる.



### [Partial, Readonly, Record, and Pick] {{minver(2.1)}}

[Partial, Readonly, Record, and Pick]: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-1.html#partial-readonly-record-and-pick

|               型               |                     意味                     |
| ------------------------------ | -------------------------------------------- |
| Partial<T>                     | TのプロパティがすべてOptionalになった型      |
| Readonly<T>                    | Tのプロパティがすべて読みこみ専用になった型  |
| Pick<T, K extends keyof T>     | TのプロパティからKのプロパティのみを残す     |
| Record<K extends keyof any, T> | Kのプロパティ名を持ち、その型全てがTとなる型 |

#### Humanを使った例

```ts
interface Human {
  id: number;
  name: string;
  age?: number;
}
```

それぞれ以下のようになる。

```ts
type Partial<Human> = {
  id?: number;
  name?: string;
  age?: number;
}

type Readonly<Human> = {
  readonly id: number;
  readonly name: string;
  readonly age?: number;
}

type Pick<Human, "id" | "name"> = {
  id: number;
  name: string;
}

type Record<keyof Human, number> = {
  id: number;
  name: number;
  age?: number;
}
```

#### Pickの補足

`Pick<T, K>`型を返す`pick(...)`について、Tが`Human`のときを考える。

```ts
function pick<T, K extends keyof T>(obj: T, ...keys: K[]): Pick<T, K>;
```

↓ T = Humanより

```ts
function pick<Human, K extends "id" | "name" | "age">(obj: Human, ...keys: K[]): Pick<Human, K>
```

`K extends "id" | "name" | "age"`は以下のいずれか。

* `"id"`
* `"name"`
* `"age"`
* `"id" | "name"`
* `"id" | "age"`
* `"name" | "age"`
* `"id" | "name" | "age"`

ここで、`K = "id" | "name"`のケースを考えると..

↓

```ts
function pick<Human, "id" | "name">(obj: Human, ...keys: ("id" | "name")[]): Pick<Human, "id" | "name">
```

↓ Rest Parameterを展開すると...

```ts
function pick<Human, "id" | "name">(obj: Human, id: "id", name: "name")[]): Pick<Human, "id" | "name">
```

よって以下は成立する。

```ts
pick({id: 1, name: 'ichiro', age: 11}, "id", "name")
// -> {id: 1, name: 'ichiro'}
```

### [Object Spread and Rest] {{minver(2.1)}}

[Object Spread and Rest]: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-1.html#object-spread-and-rest

`...`をオブジェクトの前に付けると展開される。  
`...{x: 1, y: 2}`は`x: 1, y: 2`のイメージ。

#### Shallow copyとして使う

```typescript
const obj = { id: 1, name: "Ichiro" };
const copied = { ...obj };

console.log(obj);
// -> { id: 1, name: 'Ichiro' }
console.log(copied);
// -> { id: 1, name: 'Ichiro' }
console.log(obj === copied);
// -> false
```

#### Objectのマージに使う

あるものは上書き、無いものは追加される。

```typescript
const ichiro = { id: 1, name: "Ichiro" };
const nanashi = { id: 2, favorite: "Japan" };

console.log({ ...ichiro, ...nanashi });
// -> { id: 2, name: 'Ichiro', favorite: 'Japan' }
console.log({ ...nanashi, ...ichiro });
// -> { id: 1, favorite: 'Japan', name: 'Ichiro' }
```

#### Restとして使う

restは`{id: number, favorite: string}`型と判断される。

```typescript
function main() {
  const ichiro = { id: 1, name: "Ichiro", favorite: "Japan" };
  const { name, ...rest } = ichiro;
  console.log(name);
  // -> Ichiro
  console.log(rest);
  // -> { id: 1, favorite: 'Japan' }
}

main();
```

### [Downlevel Async Functions] {{minver(2.1)}}

[Downlevel Async Functions]: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-1.html#downlevel-async-functions

TargetがES3/ES5でもasync functionが使えるようになった。

!!! warning "Promiseは必要です"

### [Support for external helpers library (tslib)] {{minver(2.1)}}

[Support for external helpers library (tslib)]: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-1.html#support-for-external-helpers-library-tslib

`--importHelpers`オプションを付けると、`__extends`や`__assign`、`__awaiter`などのヘルプ関数を`tslib`から読み込まれるようになる。  
以下のようなメリットがある。

* ファイルサイズが削減する
  * 全てのjavascriptファイルに上記関数の実装が埋め込まれなくなるため
* 上記ファイルサイズ削減のために独自Helperライブラリ管理をしていた場合、解放される

たとえば、以下の`sub.ts`と`main.ts`があったとき。

`sub.ts`

```typescript
export const o = { a: 1, name: "o" };
export const copy = { ...o };
```

`main.ts`

```typescript
import * as sub from "./sub";

export const o = { a: 1, name: "o" };
export const copy = { ...o };
```

`--importHelpers`の有無によって、ビルドされた結果のjsファイルは以下のように変わる。

=== "--importHelpersなし"
    ```typescript
    "use strict";
    var __assign = (this && this.__assign) || function () {
        __assign = Object.assign || function(t) {
            for (var s, i = 1, n = arguments.length; i < n; i++) {
                s = arguments[i];
                for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                    t[p] = s[p];
            }
            return t;
        };
        return __assign.apply(this, arguments);
    };
    Object.defineProperty(exports, "__esModule", { value: true });
    exports.o = { a: 1, name: "o" };
    exports.copy = __assign({}, exports.o);
    ```

=== "--importHelpersあり"
    ```typescript
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var tslib_1 = require("tslib");
    exports.o = { a: 1, name: "o" };
    exports.copy = tslib_1.__assign({}, exports.o);
    ```


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



