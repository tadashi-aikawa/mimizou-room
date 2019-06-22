基本文法
--------

クセがあるものだけを記載し、他言語によくあるものは省略します。

### Not equal

`a /= b`

### 関数

* 前置関数と中置関数がある
* 呼び出しは全てスペース区切り

#### 前置関数

```
関数名 引数1 引数2
```

ほとんどのケースは前置関数。

#### 中置関数

```
引数1 関数名 引数2
```

関数名が特殊文字だけからなる場合、デフォルトで中置関数となる。

```
> a !!! b = a*b
> 10 !!! 2
20
```

### 前置関数と中置換数の変換

前置関数をバッククォートで括ると中置換数になる。

```
> max 16 5
16
> 16 `max` 5
16
```

ℹ️ 関数定義の時も使える


中置関数を`()`で括ると前置関数になる。

```
> 5 == 3
False
> (==) 5 3
False
```


### 命名

* camelCase
  * PascalCaseにはそもそもできない (❓)
* アポストロフィ`'`が付く場合、その関数は **正格** であることが多い

### 三項演算子

` = if ... then ... else ...`

elseは必須


命名規約
--------

### 変数

camelCase

* 使わない変数は`_`

### 型

PascalCase

### 型変数

camelCase.. ただ基本的に1文字

### 関数

camelCase


エラー
------

`error <メッセージ>`でランタイムエラーを発生させる。

```
> error "hogehoge"
*** Exception: hogehoge
```


リスト
------

`[1, 2, 3]`

### 連結

`[1, 2] ++ [3, 4]`

左側のリストは最後まで走査されてしまうので、結合は **cons演算子** を使った方がよい。

`1:2:[3, 4]`

なお、`[3, 4]`は`3:4:[]`の糖衣構文。


### アクセス

`[1, 2, 3] !! 1`


### 比較

`==`, `>`, `<` などが使える。

### レンジ

範囲指定の簡略表記ができる。

* `[1,2,3,4,5]`は`[1..5]`
* `[1,3,5,7,9]`は`[1,3..9]`
* 要素1の無限リストは`[1,1..]`
* `abcdfeghijklmnopqrstuvwxyz`は`['a','b'..'z']`
* `[5,4,3,2,1]`は`[5,4..1]` (`[5..1]`はダメ)

上限数を指定する場合は後述の`take`を使う。  
無限リストは遅延評価なのでHaskellっぽい。

⚠️浮動小数点は精度の問題でうまくいかないときがある


### 基本的なリスト関数

|   関数    |              意味              |        記載例        |    結果     |
| --------- | ------------------------------ | -------------------- | ----------- |
| head      | 先頭の要素を取得               | head [1..5]          | 1           |
| take      | 先頭から指定数の要素を取得     | take 3 [1..]         | [1,2,3]     |
| init      | 末尾の要素以外を取得           | init [1..5]          | [1,2,3,4]   |
| tail      | 先頭の要素以外を取得           | tail [1..5]          | [2,3,4,5]   |
| drop      | 先頭から指定数の要素以外を取得 | drop 3 [1..5]        | [4,5]       |
| last      | 末尾の要素を取得               | last [1..5]          | 5           |
| length    | 長さを取得                     | length [1..5]        | 5           |
| null      | 空であるか判定                 | null []              | True        |
| reverse   | 逆順を取得                     | reverse [1..5]       | [5,4,3,2,1] |
| maximum   | 最大値を取得                   | maximum [1..5]       | 5           |
| minimum   | 最小値を取得                   | minimum [1..5]       | 1           |
| sum       | 全ての和を取得                 | sum [1..5]           | 15          |
| product   | 全ての積を取得                 | product [1..5]       | 120         |
| elem      | 要素が含まれているかどうか     | elem 3 [1..5]        | True        |
| cycle     | リストを無限に繰り返す         | take 5 $ cycle [1,2] | [1,2,1,2,1] |
| repeat    | 要素を無限に繰り返す           | take 5 $ repeat 2    | [2,2,2,2,2] |
| replicate | 要素を複製する                 | replicate 3 5        | [5,5,5]     |

`elem`は中置で使われることが多い。


### 内包表記

```haskell
> [x*10 | x <- [1..5], x /= 1, x /= 4]
[20,30,50]

> [x*y | x <- [1..5], y <- [1,10,100]]
[1,10,100,2,20,200,3,30,300,4,40,400,5,50,500]
```

`x <- [1..5]`のような部分を**ジェネレータ**と呼ぶ。


タプル
------

`(1, 1.1, 'a')`

* 複数の違う型の要素を1つの値として扱う (ヘテロである)
* サイズが固定

### 取り出し

ペア(要素が2つ)のタプルには以下がある。

* `fst` で1つ目の要素取り出し
* `snd` で2つ目の要素取り出し

### 2つのリストからタプルのリストを作る

`zip`を使う。

```haskell
> zip [1..5] ['a'..'e']
[(1,'a'),(2,'b'),(3,'c'),(4,'d'),(5,'e')]
```

リストの長さが違う場合は短い方にあわせる。  
無限リストとzipするとｶｯｺｲｲ

### 空タプル

`()`は空タプル。Unitと呼ばれている。


型
--

### 型宣言

`関数名 :: 引数の型 -> 戻り値の型`

複数引数がある場合は`->`で繋ぐ

`関数名 :: 引数1の型 -> 引数2の型 -> 引数3の型 -> 戻り値の型`


### 一般的な型

|  型名   |        意味        |          備考          |
| ------- | ------------------ | ---------------------- |
| Int     | 有界な整数         |                        |
| Integer | 有界ではない整数   | 効率的ではない         |
| Float   | 浮動小数点数       | 小数点以下第7桁まで    |
| Double  | 倍精度浮動小数点数 | 小数点以下第15桁まで   |
| Bool    | 真理値型           | True or False          |
| Char    | Unicode文字        | シングルクォートで括る |


### 型変数

* ジェネリクスのようなもの
* 小文字から始まる
* 慣例的に一文字であることが多い (a, bなど)

headの場合

```haskell
> :t head
head :: [a] -> a
```

型変数を用いた関数を**多相的関数**と呼ぶ。


### 型クラス

* 振る舞いを定義するインタフェース
* 型はある型クラスのインスタンスになり得る
* ある型クラスに属する関数 = **その型クラスのメソッド**

`==`の具体例

```haskell
> :t (==)
(==) :: Eq a => a -> a -> Bool
```

* 型クラス`Eq`のインスタンスとなる型`a`の変数を2つ受け取り、`Bool`を返す ということ
* `=>`の前にあるものは**型クラス制約**
* 型クラス制約が複数の場合は `(Eq a, Num b) => a -> b)` のように書く

⚠️型クラスはオブジェクト指向のクラスとは全く関係ない


#### Eq型クラス

| 実装すべき関数 |       型       |     説明     |
| -------------- | -------------- | ------------ |
| ==             | a -> a -> Bool | 等しいか     |
| /=             | a -> a -> Bool | 等しくないか |


#### Ord型クラス

順序づけ

| 実装すべき関数 |         型         |                    説明                     |
| -------------- | ------------------ | ------------------------------------------- |
| compare        | a -> a -> Ordering | 2値の 大きい(GT)/小さい(LT)/等しい(EQ) 判定 |


#### Show型クラス

文字列としての表現

| 実装すべき関数 |     型      | 説明 |
| -------------- | ----------- | ---- |
| show           | a -> String |      |


#### Read型クラス

文字列を受け取り、Readのインスタンスの型の値を返す。

| 実装すべき関数 |     型      | 説明 |
| -------------- | ----------- | ---- |
| read           | String -> a |      |

⚠️型注釈を使って明示的に`a`が何型であるか.. 指定しなければいけないケースもある


#### Enum型クラス

順場に並んだ列挙できる型

| 実装すべき関数 |   型   |      説明      |
| -------------- | ------ | -------------- |
| succ           | a -> a | 連続する次の値 |
| pred           | a -> a | 連続する前の値 |

Char, Int, など


#### Bounded型クラス

上限と下限を持つ

| 実装すべき関数 | 型  |  説明  |
| -------------- | --- | ------ |
| minBound       | a   | 最小値 |
| maxBound       | a   | 最大値 |

❓ 多相定数

#### Num型クラス

実数全て

#### Floating型クラス

浮動小数点

#### Integral型クラス

整数のみ

### 型注釈

`... :: 型`

型を教えてあげる。

```
> read "5"
*** Exception: Prelude.read: no parse
> read "5" :: Int
5
```


パターンマッチ
--------------

全体としては分割代入に近いかもしれない。

上から順番にパターンを試し、一致するパターンの処理が実行される。

```haskell
factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n - 1)
```

### タプルのパターンマッチ

`OK`
```haskell
addVectors :: (Double, Double) -> (Double, Double) -> (Double, Double)
addVectors a b = (fst a + fst b, snd a + snd b)
```

`GOOD`
```haskell
addVectors :: (Double, Double) -> (Double, Double) -> (Double, Double)
addVectors (x1, y1) (x2, y2) = (x1 + x2, y1 + y2)
```

### リストのパターンマッチ

secondが3のタプルに対してのみfilterし、fstに100をかけた値に変換する。  
関数型の場合、filterとmapがいる処理。

```haskell
> xs = [(1,3),(4,3),(2,4),(5,3),(5,6),(3,1)]
> [a*100 | (a, 3) <- xs]
[100,400,500]
```

headの再実装hd

```haskell
hd :: [a] -> a
hd [] = error "Invalid"
hd (x:_) = x
```

複数変数に束縛する場合は丸カッコで囲まないとシンタックスエラーになる。  
つまり、 `hd x:_ = x` だとダメ。

* `x:_ = [1,2,3]`のような代入はできる
* `(x:[])`や`(x:y:[])`は`[x]`や`[x,y]`とも書ける
  * ただし、`(x:_)`や`(x:y:_)`は角カッコで表現できない
* `++`は使えない

### asパターン

`all@(x:xs)`のようにすると、`all = (x:xs)`とみなして扱える。

```haskell
> duplicateHead :: [a] -> [a]
> duplicateHead all@(x:xs) = x:all
> duplicateHead [3,2,4]
[3,3,2,4]
```

### case式のパターンマッチ

上で登場したこのパターンマッチ..

```haskell
hd :: [a] -> a
hd [] = error "Invalid"
hd (x:_) = x
```

caseを使うとこうなる

```haskell
hd :: [a] -> a
hd xs = case xs of [] -> error "Invalid"
                (x:_) -> x
```

上で登場したパターンマッチとの違いは、関数定義のとき以外も使えること。  
三項演算子みたいなノリで式の途中に出現可能。

```haskell
len :: [a] -> String
len xs = "Length is" ++ case xs of
  [] -> "empty"
  [x] -> "only"
  xs -> "many"
```


ガード
------

* パターンマッチで絞り込まれた後の引数チェック
* パイプ文字で繋ぎ、左辺:真理値式 & 右辺:結果 を書く
  * パイプ = caseのノリ
* 主に範囲を示す場合。値の一致ならパターンマッチでも可能

```haskell
humanKind :: Int -> String
humanKind age
  | age < 35 = "若者"
  | age < 65 = "おっさん"
  | otherwise = "じっちゃん"
```

`otherwise`が無ければ次のパターン(≠ガード)に移る。


where
-----

説明変数代入のようなもの。

```haskell
bmiTell :: Double -> Double -> String
bmiTell weight height
  | bmi < 15.0 = "too low"
  | bmi < 22.5 = "ok"
  | otherwise = "too high"
  where bmi = weight / height^2
```

計算量も減るし可読性も上がるので計算が重複する場合は使おう。

whereのスコープは同一パターン内。別パターンでは解決しない。


let
---

whereと似ているが最初に束縛する。

```haskell
sum3 :: Num a => a -> a -> a -> a
sum3 a b c =
  let ab = a + b
  in ab + c
```

😄whereと違いletは式であるから以下のような表現も可能。

```haskell
> 1 + (let a = 2; b = 3 in a*b)
7
```

😢whereと違いletはガードと併用できない(ガードの中まで束縛できない)  
ガードしたければletを使うこと。内包表記で条件指定するときに便利。

```haskell
calcBmis :: [(Double, Double)] -> [Double]
calcBmis xs = [bmi | (w, h) <- xs, let bmi = w / h^2, bmi > 25.0]
```



