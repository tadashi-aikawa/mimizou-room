# [Git] Config


gitconfig
---------

### core

```
[core]
  # 改行コードを自動変換しない
  autocrlf = false
  # 編集にVimを使う
  editor = vim
```

### alias

```
[alias]
  # ログを綺麗に出力する
  logs = log --pretty=format:'%C(red)[%h] %C(bold blue)%an %C(yellow)%d > %C(white)%s %C(green) -- %cr'
  # コミットグラフを綺麗に出力する
  graph = log --all --graph --abbrev-commit --date=relative --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'
```

### color

```
[color]
  # ???
  ui = auto
```
