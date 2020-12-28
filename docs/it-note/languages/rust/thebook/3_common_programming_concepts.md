---
description: Rust `The book` の第3章 Common Programming Concepts
---

# [The book] 3. Common Programming Concepts

{{ page.meta.description }}

{{link("https://doc.rust-lang.org/book/ch03-00-common-programming-concepts.html")}}

他言語でも共通のコンセプトを学習する。


## [3.1. Variables and Mutability](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html)

変数は基本的にImmutableだが、Mutableにすることもできる。  
Immutableが基本である理由を説明するためプロジェクトを作る。

```
cargo new variables
```

### mutは変数をMutableにする

これはコンパイルエラーになる。

```rust
let x = 5;
x = 6;
```

`mut`をつけるとMutableになるのでコンパイルは通る。

```rust
let mut x = 5;
x = 6;
```

### Mutableのメリットとデメリット

巨大なデータを扱う時、Immutable構造体のコピーを生成するよりMutable構造体の一部を変更したほうがパフォーマンスが良いことがある。  
しかし、これはバグの起こりやすさ、可読性などとのトレードオフになる。

### Immutable variablesとConstantsの違い

| 項目                 | Immutable variables | Constants |
| -------------------- | ------------------- | --------- |
| `mut`                | 使える              | 使えない  |
| 宣言子               | `let`               | `const`   |
| 型注釈               | 任意                | 必須      |
| グローバルスコープで | 使えない            | 使える    |
| 実行時に評価         | できる              | できない  |

### Shadowing

同じ変数名をletで再束縛しているかのようなケースをShadowingという。  

```rust
fn main() {
    let x = 5;
    // First variable is shadowed by the second. と言われる
    let x = x + 1;
    let x = x * 2;
    println!("The value of x is: {}", x);
    // -> The value of x is: 12
}
```

Mutableな変数との違いは以下。

* Shadowingの実行文以外では再束縛できない
* 同名変数に異なる型を入れられる


## [3.2. Data Types](https://doc.rust-lang.org/book/ch03-02-data-types.html#data-types)

### Scalar Types

#### Integer Types

整数型。

* iがsigned、uがunsignedのPrefix
* isizeとusizeのbit数は実行環境に依存する
* 基本的に`i32`を使うといい
    * 64bitシステムでも`i32`の方が速いから

```rust
// i32で推論される
let x = 2;
```

型の範囲を超えた場合、デバッグモードではpanic!になるがリリースモードでは輪廻する。  
意図的に輪廻させたい場合は標準ライブラリの`Wrapping`を使うといい。

#### Floating-Point Types

* 基本的に`f64`を使うといい
    * `f32`より精度が高く、速度もほぼ同じため

```rust
// f64で推論される
let x = 2.0;
```

#### The Character Type

Rustの`char`は4byteでUnicodeを表現できる。  
stringリテラルとは異なりシングルクォーテーションを使う。

```rust
fn main() {
    let c = 'z';
    let z = 'ℤ';
    let heart_eyed_cat = '😻';

    println!("{} {} {}", c, z, heart_eyed_cat);
    // -> z ℤ 😻
}
```

### Compound Types

tuplesとarraysがある。

#### The Tuple Type

* Tupleは`(i32, f64)`のように丸括弧で表現する
* destructuring
* ドットアクセス

```rust
fn main() {
    let tup: (i32, f64, i32) = (500, 6.4, 1);
    // destructuring
    let (a, b, c) = tup;

    println!("{} is {}");
}
```

#### The Array Type

他の言語と異なり長さは固定。  
型注釈は`[型; 数]`のように書く。同一の値で初期化する場合も同様。

```rust
// 長さ4、値の型がi32のArray
let a: [i32; 4] = [1, 2, 3, 4];
// 長さ5、値がすべて"hoge"のArray
let b = ["hoge"; 5];
```

アクセスは`[i]`を使う。

```rust
fn main() {
    let a: [i32; 4] = [1, 2, 3, 4];
    println!("a[2] is {}", a[2]);
    // -> a[2] is 3
}
```

indexがArrayのサイズを超えていると、コンパイルエラーになる。

```rust
fn main() {
    let a = [1, 2, 3, 4, 5];
    let index = 10;

    let element = a[index];

    println!("The value of element is: {}", element);
}
```

The bookにはコンパイルは通ると書いてあるが..コンパイラが強化されたのかな.. 🤔

> The compilation didn’t produce any errors, but the program resulted in a runtime error and didn’t exit successfully.


## [3.3. Functions](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html)

### 関数定義

`fn`で関数定義。命名規約はsnake_case。  
言語によって違うのでややこしい..。

| 言語       | 宣言子     |
| ---------- | ---------- |
| Rust       | `fn`       |
| Kotlin     | `fun`      |
| Go         | `func`     |
| TypeScript | `function` |
| Bash       | `function` |
| Scala      | `def`      |
| Python     | `def`      |
| Elixir     | `def`      |
| Nim        | `proc`     |
| Haskell    | なし       |
| Java       | なし       |
| C++        | なし       |

関数の定義と呼び出しについて、コードの登場順としては順不同。  
コードとして先に定義する必要はない。

```rust
fn main() {
    println!("Hello, world!");

    another_function();
}

fn another_function() {
    println!("Another function.");
}
```

### 関数の構成

関数の引数と戻り値はPythonと同じ書き方。

```rust
fn plus_one(x: i32) -> i32 {
    x + 1
}
```

戻り値は関数本体の最後にあるExpressionの結果となる。

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {}", x);
    // -> The value of x is: 6
}

fn plus_one(x: i32) -> i32 {
    x + 1
}
```

early returnをする場合は`return`キーワードを使う。

```rust
fn main() {
    let x = plus_one_if_x_is_positive(-3);
    println!("The value of x is: {}", x);
    // -> The value of x is: -3
}

fn plus_one_if_x_is_positive(x: i32) -> i32 {
    if x < 0 {
        return x;
    }

    x + 1
}
```

### StatementとExpression

関数は複数のStatementと最後のExpressionで構成される。  
Statement(文)とExpression(式)の違いは以下の通り。

|          | Statement(文) | Expression(式) |
| -------- | ------------- | -------------- |
| 値の返却 | しない        | する           |


```rust
fn main() {
    // Statementは値を返却しないため束縛できない
    // let x = (let y = 6);
}
```

Pythonは`x = y = 6`のような表現ができる。  
これは`y = 6`が`6`を返すExpressionだからである。

また、ExpressionはStatementの一部である。


```rust
fn main() {
    // 5はExpression
    let x = 5;

    // { ... }はExpressionであり、その戻り値は`x + 1`
    // よって、yには4が束縛される
    let y = {
        let x = 3;
        // セミコロンがないので`x + 1`はExpression
        // セミコロンをつけると`x + 1;`はStatementになる
        x + 1
    };

    println!("The value of y is: {}", y);
    // -> The value of y is: 4
}
```


## [3.4. Comments](https://doc.rust-lang.org/book/ch03-04-comments.html)

`//`から先はコメント


## [3.5. Control Flow](https://doc.rust-lang.org/book/ch03-05-control-flow.html)

条件式、ループの理解用にそれぞれプロジェクトを作る。

```
cargo new branches
cargo new loops
```


### if文

if文やswitch文が呼び出す`{...}` はしばしば`arms`と呼ばれる。

```rust
fn main() {
    let number = 4;

    if number > 5 {
        println!("5 < {}", number);
    } else if number > 3 {
        println!("3 < {} <= 5", number);
    } else {
        println!("others");
    }
}
```

ifの条件句はbool型でなければならない。  
他言語のように暗黙的な変換は認めず、明示的にbool型を示す必要がある。

つまり、`if number { ... }`のようなケースはエラーになる。

条件が多い場合はmatchを使った方がいい。

### if式

Rustのifは式でもある。つまり右辺に指定して変数に束縛できる。

```rust
fn main() {
    let condition = true;
    // 三項演算子のように使える
    let number = if condition { 5 } else { 6 };

    println!("The value of number is: {}", number);
    // -> The value of number is: 5
}
```

### ループによる繰り返し

#### 無限ループ

```rust
loop {
    println!("Infinite loop!");
}
```

Loopを抜けたいときは`break`を使う。  
`break`は式であり、loop式の結果として値を返すことができる。

```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            // resultに指定した値が束縛される
            break counter * 2;
        }
    };

    println!("The result is {}", result);
    // -> The result is 20
}
```

#### 条件付きループ

while文を使う。

```rust
fn main() {
    let mut number = 3;

    while number != 0 {
        println!("{}!", number);

        number -= 1;
    }

    println!("LIFTOFF!!!");
}
```

#### for in ループ

Pythonと似てる。  
Arrayは明示的にイテレータへ変換してから回す。

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];

    for element in a.iter() {
        println!("the value is: {}", element);
    }
}
```

格好良く書くとこんな感じ。

```rust
fn main() {
    for number in (1..4).rev() {
        println!("{}!", number);
    }

    println!("LIFTOFF!!!");
}
```
