# [Haskell] Top


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