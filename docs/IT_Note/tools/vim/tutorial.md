# 1時間でVimに惚れるチュートリアル


はじめに
--------

Vim tutorっぽいやつです。

### 対象者

Vimを触ったことがあり簡単な操作はできるが..

* Vimのメリットがイマイチ分からない
* Vimの学習方法が分からない(覚えられない)

という人。


### チュートリアルが終わったら...

Vimの良さが伝わりましたら以下の書籍を是非読んでみて下さい。私の中では聖書です🙏

<a href="https://www.amazon.co.jp/%E5%AE%9F%E8%B7%B5Vim-%E6%80%9D%E8%80%83%E3%81%AE%E3%82%B9%E3%83%94%E3%83%BC%E3%83%89%E3%81%A7%E7%B7%A8%E9%9B%86%E3%81%97%E3%82%88%E3%81%86%EF%BC%81-%E3%82%A2%E3%82%B9%E3%82%AD%E3%83%BC%E6%9B%B8%E7%B1%8D-%EF%BC%A4%EF%BD%92%EF%BD%85%EF%BD%97-%EF%BC%AE%EF%BD%85%EF%BD%89%EF%BD%8C-ebook/dp/B00HWLJI3U" class="card">実践Vim</a>


ウォーミングアップ(5分)
-----------------------

本チュートリアルを進めるために必要になりそうな操作。

### 移動

上下左右はhjklで移動。
指さし確認で使う`人差し指`で`次(下)に移動`って覚えておきましょう。

```
       ^
       k
< h          l >
       j
       v
```


### 指定行に移動

`{行番号}G`. 20行目へ移動なら`20G`。

行番号の表示は `:set nu<CR>`. 非表示は `:set nonu<CR>`


### 直前の場所に戻る

`Ctrl+o`. 逆は`Ctrl+i`


### ワード検索

`/`で後方、`?`で前方。
`n`で次、`N`で前。


### undoとredo

`u`がundo、`ctrl+r`がredo。


### 表示画面の調整

`zz`で現在行が中心に、`z<CR>`で現在行が上方になる。


### 保存と終了

| コマンド |     意味     |    覚え方    |
| -------- | ------------ | ------------ |
| :w       | 保存         | write        |
| :q       | 終了         | quit         |
| :q!      | 保存せず終了 | quit!!!!!    |
| :wq      | 保存して終了 | write & quit |


モーション(10分)
----------------

移動のこと。


### 代表的なモーション

#### 単語単位で移動する`w`

`w`を連続して押してみましょう。

```
▼
You are studying Vim!!
Do you like Vim?
```

wordの`w`と覚える。


#### 同一行の指定した文字まで移動する`f{char}`

`fi`を連続して押してみましょう

```
▼
Aimaime is aimaime for aimaime.
```

findの`f`と覚える


#### `hjkl`で上下左右

`hjkl`の移動も実はモーションです。
だから何?って感じですけど、この後その真意が分かります。


### 回数の指定

モーションの前に回数(数字)を指定できます。
単語の移動を例に.. `3w`と押してみましょう。

```
▼
You are studying Vim!!
Do you like Vim?
```

上下左右や文字への移動でもいけます。
`2j` -> `2fo` と押してみましょう。

```
      ▼
Hello Aimaime!
Hello IMyMeMine!
Hello develop support!
Hello Vim!
```


### オススメモーション

大体の作業はこれでOK。

#### よく使う

|    コマンド     |                  意味                  |    覚え方     |
| --------------- | -------------------------------------- | ------------- |
| `hjkl`          | ←↓↑→                                   | 省略          |
| `w`             | 次の単語に移動                         | word          |
| `W`             | 次の空白で区切られたブロックに移動     | word          |
| `f{char}`       | 同一行の右側に出現する{char}に移動     | find          |
| `t{char}`       | 同一行の右側に出現する{char}直前に移動 | till          |
| `/{string}<CR>` | ファイル後方の{string}開始位置に移動   | 気合い        |
| `?{string}<CR>` | ファイル前方{string}開始位置に移動     | `/`と同じキー |
| `^`             | 行の先頭に移動                         | 正規表現の`^` |
| `$`             | 行の末尾に移動                         | 正規表現の`$` |
| `gg`            | 先頭行に移動                           | goto          |
| `G`             | 最終行に移動                           | Goto          |
| `{num}G`        | 指定行に移動                           | Goto          |


#### そこそこ使う

| コマンド  |                    意味                    |  覚え方  |
| --------- | ------------------------------------------ | -------- |
| `b`       | 前の単語に移動                             | backward |
| `B`       | 前の空白で区切られたブロックに移動         | backward |
| `F{char}` | 同一行の左側に出現する{char}に移動[^3]     | find     |
| `T{char}` | 同一行の左側に出現する{char}直前に移動[^3] | till     |
| `}`       | ファイル後方のカタマリに移動               |          |
| `{`       | ファイル前方のカタマリに移動               |          |
| `H`       | 表示位置の上部へ移動                       | high     |
| `M`       | 表示位置の中部へ移動                       | middle   |
| `L`       | 表示位置の下部へ移動                       | low      |

[^3]: `f{char}`, `t{char}`の行き過ぎは`,`で戻れるため使う機会はやや減る


オペレータ(15分)
----------------

操作方法のこと


### オススメオペレータ

必須なのは以下3つ。

| コマンド |          意味           | 覚え方 |
| -------- | ----------------------- | ------ |
| `d`      | 削除                    | delete |
| `y`      | コピー                  | yank   |
| `c`      | 変更                    | change |

以下4つもよく使います。

| コマンド |          意味           | 覚え方 |
| -------- | ----------------------- | ------ |
| `gU`     | 大文字に変換            |        |
| `gu`     | 小文字に変換            |        |
| `g~`     | 大文字/小文字の切り替え |        |
| `>`      | 右側にインデント        | -->    |
| `<`      | 左側にインデント        | <--    |


### 行全体にオペレータを実行

オペレータコマンドを2連続で入力すると行全体に実行されます。
`dd`って押してみましょう。

```
Hello Aimaime!
      ▼
Hello develop support!
Hello Vim!
```

gから始まる2文字コマンドはgを省略できます。
`gU`の場合、`gUU`って押してみると...

```
Hello Aimaime!
      ▼
Hello develop support!
Hello Vim!
```


### 好きな範囲にオペレータを実行

オペレータは好きな範囲に適応できちゃうんです. モーションと組み合わせることでね.. 😏
`dw`って押してみましょう。

```
▼
Hello Aimaime!
```

`dta`と押してみましょう。

```
  ▼
Hello Aimaime!
```

`{オペレータ}{モーション}`と打てば、`モーション`の先まで`オペレータ`が適応されます。

`d2j`と押してみましょう. (`d`がオペレータ、`2j`がモーション)

```
      ▼
Hello Aimaime!
Hello develop support!
Hello Vim!
Bye Emacs!!
```

`d/vim<CR>`なんてのもたまに使います. (`d`がオペレータ、`/vim<CR>`がモーション)

```
      ▼
Hello Aimaime!
Hello develop support!
Hello Vim!
Bye Emacs!!
```

Vimmerの思考は 『何の操作を』『どこに』するかなんですね😄


### 操作の繰り返し

#### ドットコマンド

`{オペレータ}{モーション}`で実行した操作は繰り返せます。
その名も**ドットコマンド**.. Vimキーバインドが評価される最大の理由と言っても過言ではないでしょう💚

`dw`と押した後に、`.`を何回か押してみましょう。

```
Hello Aimaime!
▼
Hello develop support!
Hello Vim!
Bye Emacs!!
```

#### cオペレータの価値

`c`という変更のオペレータがありました。
`d`オペレータ使ってから`i`で挿入モードに入ればいいじゃん..と思いませんでしたか?

ドットコマンドが登場することにより、`c`の株価は爆上がりします。

ドットコマンドと`c`オペレータを使って、以下の`Hello`を`Good morning,`に変えてみましょう。
`cwGood morning,<ESC>`と押してから、`+.`と2回押してみましょう。

※ `+`は次の行の非空白文字先頭に移動するコマンド

```
▼
Hello Aimaime!
Hello develop support!
Hello Vim!
Bye Emacs!!
```

『何の操作を』『どこに』するか に当てはめると..

>『`Good morning`に変更する処理』を『単語』にする..

この操作を繰り返していたということです。


#### ドットコマンドで繰り返し可能なモノ

`{オペレータ}{モーション}`のカタチでなくてもドットコマンドは使えます。

`A`は行末に文字を挿入するコマンドですが、ドットコマンドで繰り返し可能です。
`A end.<ESC>`と押してから、`j.`を3回押してみましょう。

```
▼
Hello Aimaime!
Hello develop support!
Hello Vim!
Bye Emacs!!
```


テキストオブジェクト(10分)
--------------------------

まとまりを表すモノ。

オペレータの範囲に幅を持たせる用途[^2]で使います。モーションのように単独では使えません。

`di"`と押してみましょう。`d`は削除オペレータですが...

```
▼
I play tennis with "Ichiro" every day!
```

`i"`は`ダブルクォーテーションの内側(inner ")`というまとまりを指すテキストオブジェクトです。

[^2]: オペレータのためだけに存在するわけではない

### `a`と`i`

テキストオブジェクトはほぼ必ず[^1]`a`か`i`から始まります。

* `i`は内側。`inner`の略
* `a`は外側を含む。`a`そのまま

私は`inside`と`around`の方がしっくり来ました。

`da"`と押して、`di"`との挙動が違うことを確認しましょう。

```
▼
I play tennis with "Ichiro" every day!
```

[^1]: https://vim-jp.org/vimdoc-ja/motion.html#text-objects の記載には全てついている

### オススメテキストオブジェクト

`a`と`i`は省略します。

| テキストオブジェクト |           意味           |               備考               |
| -------------------- | ------------------------ | -------------------------------- |
| `w`                  | 単語                     | wordの略                         |
| `W`                  | 空白で区切られたブロック | wordの略                         |
| `p`                  | 段落                     | paragraphの略                    |
| `"`                  | `""`の範囲               | 現在行の次に出現する範囲が対象   |
| `'`                  | `''`の範囲               | 現在行の次に出現する範囲が対象   |
| `)`                  | `()`の範囲               | 現在位置が`()`内であることが必要 |
| `]`                  | `[]`の範囲               | 現在位置が`()`内であることが必要 |
| `}`                  | `{}`の範囲               | 現在位置が`{}`内であることが必要 |


### よく使うオペレータ+テキストオブジェクト

実践的な操作をしてみましょう。

#### Change inner word ---> `ciw`

単語を変更するため、`ciw`と入力してからそのまま好きな単語を書いてみましょう。

```
        ▼
I like Vim the most in the world.
```

#### Change inner "..." ---> `ci"`

ダブルクォーテーションの中身を変更するため、`ci"`と入力してからそのまま好きな単語を書いてみましょう。

```
▼
I like "Vim" the most in the world.
```

#### Delete a "..." ---> `da"`

ダブルクォーテーションで囲まれた単語をダブルクォーテーションごと消すために、`da"`と入力してみましょう。

```
▼
I like "Vim" the most in the world.
```

`c`は`i`と、`d`は`a`と連携することが多いです。

#### Delete a paragraph ---> `dap`

main関数を削除するため、`dap`と入力してみましょう。

```python
#!/bin/env python

def main():
     ▼
    print("hogehoge")
    pass

main()
```

#### Yank a {...} ---> `ya}`

`{}`で囲まれた部分を`{}`を含めてyankするため、`ya}`と入力してみましょう。

```json
{
  "id": 1,
  "name": "Ichiro",
  "favorite": {
        "food": ["apple", "orange"],
        ▼
        "animal": ["dog", "cat"],
  }
}
```

好きなところに移動して`p`を押すと貼り付けられます。


総合問題(5分)
-------------

今まで学んだモーション、オペレータ、テキストオブジェクトを使って問題を解いてみましょう。

### 問題テキスト

問題のyamlファイルに以下の編集を加えて下さい。

* `channel:`の名称を変更する (なんでもOK)
* `one`, `other` を消す
* `output`を一番後ろに持っていく

!!! warning "yamlは新しいファイルとして作成してください"

    本問題は本テキスト内で実施しないでください。
    また、**最終行の改行**も忘れずに追加してください。


```yaml
one:
  name: One
  host: https://raw.githubusercontent.com/tadashi-aikawa/jumeaux-toolbox/master/vagrant/ignore_properties/one

other:
  name: Other
  host: https://raw.githubusercontent.com/tadashi-aikawa/jumeaux-toolbox/master/vagrant/ignore_properties/other

notifiers:
  test:
    type: slack
    channel: "#times_tadashi-aikawa"
    icon_emoji: "innocent"

output:
  response_dir: responses

addons:
  log2reqs:
    name: plain

```

### 回答テキスト (整形後の期待値)

この内容にするため必要なキーの組み合わせを考えてみましょう。

```yaml
notifiers:
  test:
    type: slack
    channel: "#hoge"
    icon_emoji: "innocent"

addons:
  log2reqs:
    name: plain

output:
  response_dir: responses

```

??? info "回答例"

    * `dap./cha<CR>ci"#hoge<ESC>}d}GP`
    * `d8G3jci"#hoge<ESC>3jdapGp`

