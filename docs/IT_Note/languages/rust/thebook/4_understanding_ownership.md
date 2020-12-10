---
description: Rust `The book` の第4章 Understanding Ownership
---

# [The book] 4. Understanding Ownership

{{ page.meta.description }}

{{link("https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html")}}

所有権を学習する。


## [4.1. Variables and Mutability](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html)

GCや手動メモリ確保ではなく、Rustは所有権を管理するという方法をとっている。  
主なメリットは3つ。

* GCが実行されないためパフォーマンスは落ちない
* allocateによる煩雑さや予期せぬ不具合を生むリスクがない
* コンパイル中に問題を発見できるのが強い。

### StackとHeap

| 項目                 | Stack              | Heap |
| -------------------- | ------------------ | ---- |
| IN/OUT               | Last In, First Out |      |
| コンパイル時のサイズ | 確定               | 未定 |

Stackのイメージはプレート。

プレートは追加するとき上に乗せ、取るときは上から取る。  
下に重ねたり、下から取ることもできるがプレートを持ち上げるのが大変なので普通はやらない。

### 所有権のルール

* Rustの各値にはOwner(所有者)と呼ばれる変数が存在する
* 値は同時に1つのOwnerしか持てない
* Ownerがスコープ外になると値は削除される

### 変数とスコープ

ブロックスコープなど同一のスコープ内なら変数は有効

```rust
{
    let s = "hello";
    //
    // この中であればsは有効
    //
}
```

### String型

`&str`と`String`の違い

| 項目           | &str         | String         |
| -------------- | ------------ | -------------- |
| 格納先         | Stack        | Heap           |
| Mutable        | 不可         | mutをつければ  |
| コンパイル時に | 値が確定する | 値が確定しない |

```rust
fn main() {
    // &str
    let str = "hello";
    // String
    let mut string = String::from("hello");
    string.push_str(" world!")
}
```

### 変数とデータの相互作用: Move

Stackを使う`i32`型は所有権を気にしないので、以下は動く。

```rust
fn main() {
    let x = 5;
    let y = x; // xの値コピーをyに束縛している
    eprintln!("x = {:?}", x);
    eprintln!("y = {:?}", y);
}
```

一方、heapを使うStringでは、以下は動かない。

```rust
fn main() {
    let x = String::from("hello");
    let y = x; // xにおけるheap部分(文字列)の所有権をyに変更する
    
    eprintln!("x = {:?}", x); // xの所有権は失われているのでエラー
}
```

長さなどの基礎データはstackに格納されるが、文字列はheapに格納される。  
以下で説明されている図が分かりやすい。

{{link("https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html#ways-variables-and-data-interact-move")}}

値のOwnerが2つになると、Ownerがそれぞれスコープから抜けたときにdrop(heapのクリア)をする。  
これは`double free`エラーと呼ばれるエラーであり脆弱性などを生む。

所有権を持たない変数はスコープから抜けてもdropされないようになる。  
これにより、値のOwnerが1つと保証されている限り`double free`は起こらない。

先のコードにおける`let y = x`を **`x` was moved into `y`** と呼ぶ。(move)  
xの値から見たとき、Ownerがxからyに変更されたことを意味する。

Rustは暗黙/自動でDeep copyすることはない。

### 変数とデータの相互作用: Clone

`clone()`を呼び出せばheapの値をdeep copyできる。

```rust
fn main() {
    let x = String::from("hello");
    let y = x.clone();  // xのheapをdeep copyした値がyのheapに入る
    eprintln!("x = {:?}", x); // xのheapに入った値のOwnerはxのまま だからOK
    eprintln!("y = {:?}", y);
}
```

`i32`などのいわゆるprimitive型はheapを利用しないため`clone()`の必要はない。

### 所有権と関数

関数の引数にheapを使う型の変数を渡すと所有権が失われる。

```rust
fn main() {
    let s = String::from("hello");
    takes_ownership(s);
    println!("{}", s); // sに所有権はないのでコンパイルエラー

    let x = 5;
    makes_copy(x);
    println!("{}", x); // i32はheapを使わないので所有権は関係ない
}

fn takes_ownership(some_string: String) {
    println!("{}", some_string);
    // sやsome_stringから参照されていたheapに格納された値はこの後dropされる
}

fn makes_copy(some_integer: i32) {
    println!("{}", some_integer);
}
```

関数に渡した値をその後も使いたい場合、戻り値をTupleにして所有権ごと引き戻す方法がある。

```rust
fn main() {
    let s1 = String::from("hello");

    let (s1, len) = calculate_length(s1);
    println!("The length of '{}' is {}.", s1, len);
}

fn calculate_length(s: String) -> (String, usize) {
    let length = s.len();
    (s, length)
}
```

しかし、これはあまりにバカバカしい。  
Rustはreferencesと呼ばれる機能でこれを解消できる。


## [4.2. References and Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)

### 参照と逆参照

`&`を付けると参照、`*`を付けると逆参照。  
変数s1があったとき`&s`は参照であり、逆参照`*&s`はs1である。


```rust
fn main() {
    let s1 = String::from("hello");

    let len = calculate_length(&s1); // 参照`&s1`を渡しても所有権はs1のまま

    println!("The length of '{}' is {}.", s1, len);
}

fn calculate_length(s: &String) -> usize {
    s.len() // 引数パラメータが参照なのでTupleで返却する必要がない
}
```

`calculate_length(s: &String)`のように関数パラメータとして参照を持つことを**borrowing**という。

### Mutable References

実体と参照をそれぞれMutableにすると、参照から実体を直接変更できる。

```rust
fn main() {
    // ❶ 実体のsをmutableにする
    let mut s = String::from("hello");

    // ❷ 参照をMutableな&mut sとして渡す
    change(&mut s);
    eprintln!("s = {:?}", s);
}

fn change(some_string: &mut String) {
    // ❸ Mutableな参照 &mut String を受け取って操作する
    some_string.push_str(", world");
}
```

同一スコープにおいて、ある実体に対するMutableな参照は1つしか持てないので注意。  

```rust
let mut s = String::from("hello");

let r1 = &mut s;
let r2 = &mut s; // Mutableな変数sへのMutableな参照r1が既にあるためエラー

println!("{} {}", r1, r2);
```

また、同一の参照スコープにImmutableな参照が存在するとMutableな参照を持つこともできない。

```rust
let mut s = String::from("hello");

let r1 = &s;
let r2 = &s;
let r3 = &mut s; // Mutableな変数sのImmutableな参照&sが存在するためエラー

println!("{} {}, {}", r1, r2, r3);
```

参照スコープはそれが最後に参照されるまで。  
それゆえ、以下のコードはコンパイルできる。

```rust
let mut s = String::from("hello");

let r1 = &s;
let r2 = &s;
println!("{}, {}", r1, r2);
// sの参照r1, r2が最後に使用されるのはここまでなので、r1, r2の参照スコープはここまで

let r3 = &mut s; // 同一参照スコープにsの参照は存在したためOK
println!("{}", r3);
```

### Dangling References

本来有効だったメモリ領域が、開放などにより無効化されたあとも参照し続けるポイントのことを**Dangling Pointer**と呼ぶ。  
同様に本来有効だったが無効化された参照を**Dangling References**と言う。

RustではコンパイルエラーでDangling Referencesを防ぐことができる。

```rust
fn main() {
    let reference_to_nothing = dangle();
}

fn dangle() -> &String {
    let s = String::from("hello");
    
    &s // sの値は関数を抜けると削除されるので、返却する参照は正しく動かない(エラー)
}
```

### まとめ

* 同一スコープ内では以下いずれかのReferencesを持つことができる
  * 1つのMutable Reference
  * 1つ以上のImmutable References
* 参照は常に有効でなければいけない
