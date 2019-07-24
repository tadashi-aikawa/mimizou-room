# [Travis CI] Top


`.travis.yml`のTokenを暗号化する
--------------------------------

平文で書くと脆弱すぎるので暗号化する。

{{link("https://docs.travis-ci.com/user/encryption-keys/")}}

### Ruby環境の準備

暗号化ツールを動かすためにRubyが必要なのでDockerで。

```
$ docker run -it ruby bash
```

### travisのインストール

CLIのインストール。公式通り。

```
$ gem install travis
```

### 暗号化

暗号化はプロジェクトがseedに必要なので、カレントディレクトリを**プロジェクトルート**にする。  
`.travis.yml`があるところってこと。

そしてコマンドを実行。

```
$ travis encrypt "<workspace>:<token>" --add notifications.slack
```

`<workspace>:<token>`はSlackのTravis CI Appsの設定開くと載っている。  
`Setup Instructions` > `Encrypting your credentials`

勝手に`.travis.yml`が上書きされるけど、必要なのは`secure: <...>`の部分だけ。  
そこを書き換えてコミットすればOK。
