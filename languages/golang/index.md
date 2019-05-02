インストール
------------

Chocolateyで1.12.2をインストール

```
$ cinst golang
```

`C:\Go`配下にインストールされる。  
`%GOROOT%`も勝手にそこへ設定される。はず。


module
------

`${GOPATH}`配下にプロジェクトを配置しなくてもOKになった。

⚠️`${GOPATH}`配下は引き続き、moduleの管理体系として使用される

### 初期化

`go.mod`が作成される。


#### dep使っているプロジェクト

`go mod init`

Gopkg.lockからイイ感じにやってくれる

#### 真っ新なプロジェクト

`go mod init github.com/<your_account>/<your_repository>`


### 依存関係

#### インストール

`go run`の時に自動でやってくれる。

ℹ️ VSCode使っているなら保存時にやってくれたりもする

#### 最適化

`go mod tidy`

* 不要パッケージのprune
* 必要なパッケージのダウンロード

#### 検証

`go mod verify`

ダウンロードした依存パッケージが正しいものであることを検証。

#### 依存関係も含めた全パッケージのテスト実行

`go test all`

ベストプラクティスではやった方がいいらしいけど時間がかかるからケースバイケースか..。

#### 依存モジュールの削除

`${GOPATH}/pkg/mod`配下を削除。

キャッシュクリアだけなら `go clean -cache`
