# [Elixir] Top

学習
----

{{link("https://elixirschool.com/ja/")}}


インストール
------------

インストーラーで。

{{link("https://elixir-lang.org/install.html#windows")}}

Chocolatey使うとIDEA使えなくなる。

{{link("https://github.com/KronicDeth/intellij-elixir/issues/1159")}}


### Chocolatey使う場合(非推奨)

Windowsの場合

```
$ cinst elixir
```

インストール場所
`/c/ProgramData/chocolatey/lib/Elixir/bin`


対話型
------

`iex`で開始


Hello World
-----------

`main.ex`を作る。

```elixir
defmodule Main do
  def main do
    IO.puts("Hello, World!")
  end
end

Main.main
```


実行
----

{{link("https://qiita.com/tanaka0325/items/045ce9d9ee9355741c3d")}}

コンパイルしなくても実行できる。  
その場合は拡張子を`exs`にすべきらしいがここでは気にしない。

```
$ elixir main.ex
Hello, World!
```


コンパイル
----------

{{link("https://qiita.com/kazuhikoyamashita/items/fee98aa446a9e71c109c")}}

コンパイルと同時に実行もされる。

```
$ exlixirc main.ex
Hello, World!
```

コンパイルした`beam`ファイルがあると

```
$ elixir -e Main.main
Hello, World!
```

でも実行できるよう.. `beam`ファイルの指定は不要なのか??

