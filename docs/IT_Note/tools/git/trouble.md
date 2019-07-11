# [Git] FAQ


ブランチとタグが同じ名前になってしまいエラーが出る
--------------------------------------------------

```
src refspec <tag_name> matches more than one.
```

```
タグを消したい場合
git push origin :refs/tags/<tag_name>
```

```
ブランチを消したい場合
git push origin :refs/heads/<branch_name>
```

{{refer("https://qiita.com/koara-local/items/e36bc172a3c36eb67b4f")}}


`warning: LF will be replaced by CRLF in`
-----------------------------------------

gitのconfigで`core.autoCRLF`が`true`になっていないか確認する。

```
$ git config --global core.autoCRLF
```

`true`になっていたら`false`にする。

```
$ git config --global core.autoCRLF false
```

{{refer("https://normalblog.net/system/lf_replaced_crlf/")}}


改行コードを強制したい
----------------------

autocrlf設定によって変わってしまう改行コードを抑制したい場合。

`.gitattributes`に設定する。

`例`
```
* text=auto

*.bat  text eol=crlf
*.vbs  text eol=crlf
*.sh   text eol=lf
*.txt  -text
```

* `text`属性を付けるとautocrlfによって自動で改行変換する
* `text eol=..`で改行コードを指定すると、必ずその改行コードに変換する
* `-text`で`text`属性を外すと改行変換しない


{{refer("https://qiita.com/nacam403/items/23511637335fc221bba2")}}