# [Golang] FAQ


go getでグローバルにインストールできない
----------------------------------------

* `go.mod`が存在する場所でインストールしてしまっている
    * `go.mod`が存在しない場所でインストールする必要あり
* go moduleがOFFになっている
    * `GO111MODULE=on` or `set GO111MODULE=on&`を`go get`の前に付ける必要あり

