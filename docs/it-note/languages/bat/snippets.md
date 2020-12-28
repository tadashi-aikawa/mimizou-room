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

```batch
xcopy /is <from> <to>
```

### ディレクトリの削除

```batch
rd /s /q <dir>
```

### 一定時間後にコマンド実行

```batch
timeout /T ${コマンド}
```

### 別プロセスで実行

```batch
start ${コマンド}
```

### ブラウザでURLを開く

```batch
start ${URL}
```

### カレントディレクトリの特定階層の文字列取得

6番目だったら..

```batch
for /f "usebackq tokens=6 delims==\" %%a in (`echo %CD%`) do set xrf_name=%%a
```
