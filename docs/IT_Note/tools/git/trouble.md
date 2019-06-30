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