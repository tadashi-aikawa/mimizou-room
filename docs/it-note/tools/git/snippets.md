# [Git] Snippets


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
git diff --staged
# --stagedは--cachedのsynonym
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

### ワーキングツリーをあるコミット時点の状態にする

```
git restore -s <hash> <file>
```


変更
----

### ブランチ作成

```
git switch -c <new_branch_name>
# v2.23以前
git checkout -b <new_branch_name>
```

### ブランチ変更

```
git switch <branch_name>
# v2.23以前
git checkout <new_branch_name>
```

### ブランチ名変更

```bash
git branch -m <branch_name> <new_branch_name>
```

### リモートブランチを追跡する形でローカルに作成 (ブランチはorigin弁当!)

```bash
git switch -c <branch_name> <origin_branch_name>
# v2.23以前
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
git restore <file>
# v2.23以前
git checkout <file>
```

### addしたファイルを取り消す

```bash
git restore -S <file>
# long
git restore --staged <file>
# v2.23以前
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

#### リモートに間違えて追加したファイルを取り消す

!!! danger "リモートを直接変更するので、他の人がコミットしていないか注意"

1. `git rebase -i <hash_before_target_commit>`を実行して、やり直したいコミットの1つ前に戻る
2. 開かれたエディタの`pick`を`edit`に書き換えて保存/終了する
3. `git rm <file>` で消したいファイルを削除する
4. `git commit --amend`で上書きコミット
5. `git rebase --continue`
6. 途中でconflictしたら解消してから`git rebase --continue`
7. `git push -f origin master`でforceコミット


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
