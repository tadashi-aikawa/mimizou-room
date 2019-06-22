確認
----

### 全てのブランチを確認

```bash
git branch -a
```

### ignoreされたファイルの確認

```bash
git check-ignore ${path}
```

### ワークスペースとインデックス登録済みの差分

```bash
git diff
```

### インデックス登録済みとコミット済みの差分

```bash
git diff --cached
```

### コミット済みとリモートの差分

```bash
git diff HEAD^
```

### タグ一覧表示

```bash
# 一覧
git tag -l
# コミットメッセージ付き
git tag -n
```

### ログの詳細情報を表示

```bash
git log --pretty=fuller
```

### コミットメッセージをgrepしてログを探す

```bash
git log --grep <word>
```

### ファイルの変更情報を表示

```
git log --name-status
```

### ファイルの過去の歴史を確認

```bash
git log -p $file
```

### HEADのhashを取得する

```bash
git rev-parse HEAD
```

### カレントブランチ名を取得する

```bash
git rev-parse --abbrev-ref HEAD
```

### 特定コミット時点の特定ファイルを閲覧する

```
git show <hash>:<file>
```

### branchがmasterのどこから分岐しているかを調べる

```bash
git show-branch --sha1-name branch master
```


変更
----

### ブランチ名変更

```bash
git branch -m <branch_name> <new_branch_name>
```

### ブランチをローカルにチェックアウト (ブランチはorigin弁当!)

```bash
git checkout -b <branch_name> <origin_branch_name>
```

### タグをブランチとしてチェックアウト

```bash
git checkout -b <branch_name> refs/tags/<tag_name>
```

### リモートで削除されたブランチを削除

```bash
git fetch -p
```

### remote

リモートURLの変更をするコマンド

### タグをつける

```
# local
git tag 1.0.0
# remote
git push origin 1.0.0
```

### 注釈つきタグをつける

```
# local
git tag -m '${message}' 1.0.0
# remote (if `followTags = true`)
git push
```


とりけし
--------

### ローカルの変更を戻す (addしていない場合)

```bash
git checkout .
```

### addしたファイルを取り消す

```bash
git reset HEAD <file>
```

HEADがない場合は

```bash
git rm --cached <file>
```

### ある時点のコミットに戻す

```bash
git reset --hard <commit_id>
```

### 履歴を改ざんする

* editで改ざん

#### 時間も含めて改ざんする場合

```bash
# 先頭(HEAD)から2つ分改ざんする
git rebase -i HEAD~2
# 日付を改ざんしたamend commit
git commit --amend --date="Sun Feb 4 19:37:11 2017 +0900"
# commit dateをauthor dateにあわせる
git rebase HEAD~2 --committer-date-is-author-date
```



削除
----

### 管理されていないエントリを削除する

```bash
git clean -f
```

### ローカルブランチ削除

```bash
git branch -d <branch_name>
```

### リモートブランチを削除

```bash
git push --delete origin <branch_name>
# または
git push origin :<branch_name>
```

### マージ済みのローカルブランチを全て削除

```bash
git branch --merged master | grep -vE '^\*|master$|develop$' | xargs git branch -d
```

### タグを消す

```
# local
git tag -d 1.0.0
# remote
git push --delete origin 1.0.0
```

### 1つ前にコミットしたpushを強制的に取り消す

```bash
git push -f origin HEAD~:master
```


設定
----

### ユーザ情報を設定

```bash
# ユーザ名
git config --global user.name <user_name>
# メールアドレス
git config --global user.email <mail_address>
```

### 毎回認証情報でユーザ名を入力しないようにする

```bash
git remote set-url origin https://<user_name>@<github.com以降のURL>
```


全体
----

### 特定のタグを指定してshallow clone

```bash
git clone --depth=1 -b ${tag} ${URL}
```

### サブモジュール(sub module)を含めてclone

```bash
git clone --recursive
```

### パッチを作る/あてる

```bash
# パッチをあてる (事前にgit diffの結果をdiff.patchに出力しておく)
patch -p1 < diff.patch

# ワンライナー
git diff <target_commit> | patch -p1
```