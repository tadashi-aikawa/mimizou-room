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

参考: https://qiita.com/koara-local/items/e36bc172a3c36eb67b4f


