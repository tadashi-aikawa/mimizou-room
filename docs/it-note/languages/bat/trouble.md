# [Bat] FAQ


for文やif文の中で変数が期待通りにならない
-----------------------------------------

遅延環境変数が即時展開されていないかを確認する。以下２点の対応がされているか。

* `setlocal enabledelayedexpansion` の文がある
* forやifの中で`!ARG!`のような変数指定をしている (`%ARG%`ではなく)

参考: https://wa3.i-3-i.info/word12518.html


glob表記を含めた可変長引数の処理をしたい
----------------------------------------

```bat
for %%f in (%*) do (
  echo %%f
)
```

第n引数より後を可変長glob表記に対応させる場合は黒魔術が必要。

```bat
set /A ARGI=1
for %%f in (%*) do (
    if not !ARGI! GTR n (
      echo %%f
    )
    set /A ARGI=ARGI+1
)
```

`n`に数字を入れる。
