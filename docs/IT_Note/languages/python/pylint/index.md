# [Pylint] Top


`.pylintrc`ファイル作成
-----------------------

```
$ pylint --generate-rcfile > .pylintrc
```

ドット付けない方が主流なのかもしれぬ...


メッセージと番号
----------------

http://pylint-messages.wikidot.com/ で調べる。

###よく見るもの

| エラーコード |        エラー名        |                     説明                      |
| ------------ | ---------------------- | --------------------------------------------- |
| C0413        | wrong-import-position  | Import文の場所が適切ではない                  |
| W0511        | fixme                  | notesで指定されたprefixのコメントが残っている |
| W0611        | unused-import          | 使われていないimportがある                    |
| R0903        | too-few-public-methods | 公開メソッドが少なすぎる                      |


特定箇所だけ無視
--------------

### 行

行の *最後* に

```bash
yourcode # pylint: disable=W0611
yourcode # pylint: disable=wrong-import-position
```

### ブロック

ブロックの *最後* に

```
# pylint: disable=wrong-import-position
```

### ファイル

ファイルの *最初* に

```
# pylint: disable=wrong-import-position
```


IDEAへの設定
------------

* Scope: `Current File`
* Program: `$PyInterpreterDirectory$\pylint.exe`
* Arguments: `--rcfile $ContentRoot$/.pylintrc $FilePath$`

`Working directory`に`$ContentRoot`を指定しないのは、ターミナルに出力される絶対パスへクリックでリンクできないから。  
それが問題なければ`Working directory`に指定すれば良い。
