---
description: Bitbucket PipelineについてのFAQ
---

# [Bitbucket Pipeline] FAQ

{{ page.meta.description }}



予期せぬ挙動
------------

### 作成したファイルが存在しない

stepが異なっていないかを確認する。  
ファイルは同一step内でしか共有できない。

stepを超えてファイルを共有したい場合は`artifacts`や`cache`を使う。

{{refer("https://ja.confluence.atlassian.com/bitbucket/using-artifacts-in-steps-935389074.html")}}
{{refer("https://ja.confluence.atlassian.com/bitbucket/caching-dependencies-895552876.html")}}


文法エラー
----------

### 文法があっているはずなのにSyntax Errorになる

改行コードがLF改行になっていることを確認する。


成果物について
--------------

### 一時的に保存したい

14日で削除されてもよければ`artifacts`を使う。  
本来`artifacts`はstep間でファイルの受け渡しをする目的で使うが、GUIのstep結果からダウンロードすることもできる。

{{link("https://ja.confluence.atlassian.com/bitbucket/using-artifacts-in-steps-935389074.html")}}

`artifacts`のパスは直前のカレントディレクトリではなく`BITBUCKET_CLONE_DIR`からの相対パスなので注意。  
以下の場合、対象は`${BITBUCKET_CLONE_DIR}/dist/**`になる。`${BITBUCKET_CLONE_DIR}/src/dist/**`ではない。

```yaml
pipelines:
  custom:
    sample:
      - step:
          script:
            - cd src
            - make package
          artifacts:
            - 'dist/**'
```

`artifacts`に保存できるサイズの上限は1GBとのこと。

### 永続的に保存したい

Bitbucketのリポジトリ(ダウンロード)に保存したい場合は`bitbucket-upload-file`を使う。

{{link("https://bitbucket.org/atlassian/bitbucket-upload-file/src/master/")}}


