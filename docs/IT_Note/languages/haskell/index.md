# [Haskell] Top

オススメ文献
------------

### 入門書

{{link("https://www.amazon.co.jp/dp/B009RO80XY/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1")}}

### Haskellでモナド周りを体系的に学ぶ

以下シリーズ全て

{{link("https://qiita.com/7shi/items/145f1234f8ec2af923ef")}}

### Haskellで実際にモノを作る

{{link("https://employment.en-japan.com/engineerhub/entry/2017/09/11/110000")}}
{{link("https://employment.en-japan.com/engineerhub/entry/2017/10/03/110000")}}


API
---

{{link("https://hoogle.haskell.org/")}}


ghci
----

### 起動

stackでインストールした場合。

```
$ stack ghci
```

### hsファイルのロード

```haskell
> :l file
```

fileに`.hs`は含まない。

### 型確認

```haskell
> :t 10
10 :: Num t => t
```

### 型宣言

セミコロンをつけて、その後に実装を続けて書く。

```haskell
> triple :: Int -> Int; triple x = 3*x
> triple 9
27
```

`:{`と`:}`で括ると複数行で書ける。

```haskell
> :{
| lucky :: Int -> String
| lucky 7 = "lucky"
| lucky x = "unlucky"
| :}
>
```