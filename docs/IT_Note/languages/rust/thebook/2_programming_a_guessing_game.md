---
description: Rust `The book` の第2章 Programming a Guessing Game
---

# [The book] 2. Programming a Guessing Game

{{ page.meta.description }}

{{link("https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html")}}


## プロジェクトの作成

```
$ cargo new guessing_game
# 実行確認
$ cd guessing_game
$ cargo run
```

## 推測値を入力させる

```rust
use std::io;

fn main() {
    println!("Guess the number!");

    println!("Please input your guess.");

    // Mutableな変数guessを作成し、作成したStringのインスタンス(UTF-8の文字列)を束縛する
    // String::newはStringのstaticメソッド (not constructor)
    // 大抵のTypeは`::new`というstaticメソッドを持つ
    let mut guess = String::new();

    io::stdin() // 標準入力から..
        .read_line(&mut guess) // 書き換え可能なbufferの参照に入力された値を入れたResultを取得
        .expect("Failed to read line"); // 失敗した場合はメッセージを表示して止める (この行はなくても警告は出るが動く)

    println!("You guessed: {}", guess);
}
```

## 乱数createとcreateの扱い方

[rand](https://crates.io/crates/rand) createを使う。

`Cargo.toml`の`[dependencies]`配下に追加する。  
IntelliJ IDEAだとバージョンは補完できる。

```toml
[dependencies]
rand = "0.7.3"
```

バージョンは[Semantic Versioning](http://semver.org/)が採用されている。  
**`0.7.3`は固定バージョンではなく、`^0.7.3`の省略形である。**

`cargo build`や`cargo run`を実行すると、createがダウンロード/コンパイルされる。

`Cargo.lock`ファイルにインストールしたバージョンは記載されている。  
`cargo build`の際は、そのバージョンのcreateを使う。(dependenciesの要件を満たしていれば)

dependenciesを満たす最新のcreateが必要なら`cargo update`を実行する。  
`Cargo.lock`ファイルを無視して条件を満たす最新のcreateを取得する。

## 乱数を作る

```rust
use rand::Rng;
use std::io;

fn main() {
    println!("Guess the number!");

    // 1から100(101-1)の範囲で乱数を作成しsecret_numberに束縛する
    let secret_number = rand::thread_rng().gen_range(1, 101);

    println!("The secret number is: {}", secret_number);

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {}", guess);
}
```

## 乱数を比較する

`guess`はStringに推論されるため、そのままでは比較できない。  
文字列型を数値型に変換するため以下の処理を追加する。

```rust
    // trimはユーザ入力の改行を除去するために必要
    // : u32 で parseの変換後に期待する型がu32であることを示している
    let guess: u32 = guess.trim().parse().expect("Please type a number!");
```

`guess`は既に使用されている変数だがRustではこれが許される。(Shadowing)
型変換で再束縛するケースを想定して同名変数の再利用を許可しているからだ。

## チャレンジを複数回行う

`loop { }`で対象処理を無限ループする。

```rust
// --snip--

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        let guess: u32 = guess.trim().parse().expect("Please type a number!");

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => println!("You win!"),
        }
    }

// --snip--
```

## 正解の場合にゲームを終了する

`break`を差し込む。

```rust
          Ordering::Equal => {
              println!("You win!");
              break;
          }
```

## 不正な入力の例外処理

`guess`の変換にmatch式を用いる。

```rust
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            // _ はすべて(なんでもOK)の意味
            Err(_) => continue,
        };
```

## 最終調整

`secret_number`を非表示にして完成。

```rust
use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1, 101);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
```
