# [Bat] Snippets


shellファイルを実行
-------------------

```bat
"C:\Program Files\Git\bin\bash.exe" <*.sh> <args>
```

batがネットワーク内にあり、cdで移動できない場合は

```bat
"C:\Program Files\Git\bin\bash.exe" %~dp0\<*.sh> %~dp0 <args>
```

shellファイルの第一引数にbatファイルの位置を受け取れば、相対パスのようにコードを書くことができる。

!!! hint "shellファイルからの相対パスが欲しい場合は"
    [bash/snippets](../../bash/snippets)を参照


よく使うもの
------------

### ディレクトリのコピー

```bat
xcopy /is <from> <to>
```

### ディレクトリの削除

```bat
rd /s /q <dir>
```

### カレントディレクトリの特定階層の文字列取得

6番目だったら..

```bat
for /f "usebackq tokens=6 delims==\" %%a in (`echo %CD%`) do set xrf_name=%%a
```
