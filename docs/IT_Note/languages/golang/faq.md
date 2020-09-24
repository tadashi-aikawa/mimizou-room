---
description: GolangのFAQ
---

# [Golang] FAQ

{{ page.meta.description }}


コマンドでやりたいこと
----------------------

### 配下のpackageすべてにテストを実行したい

targetを`./...`と指定する。

```
go test ./...
```


実装でやりたいこと
------------------

### JSON文字列とstructを相互変換したい

`json.Marshal`と`json.Unmarshall`を使う。

```go
type Human struct {
	Id   int    `json:"id"`
	Name string `json:"name"`
}

const JSON = `
{
  "id": 100,
  "name": "たろう"
}
`

func main() {
	var taro Human
	
	// string -> []byte -> struct
	jsonBytes1 := []byte(JSON)
	_ = json.Unmarshal(jsonBytes1, &taro)

	// struct -> []byte -> string
	jsonBytes2, _ := json.Marshal(taro)
	jsonStr := string(jsonBytes2)
}
```

ただし、UTF-8に限る。

### クエリの値をURLエンコーディングしたい

`url.QueryEscape`を使う。

```go
url.QueryEscape("ほげ")
// %E3%81%BB%E3%81%92
```

URLやクエリパラメータ全体にかけるとおかしくなるので注意。

```go
url.QueryEscape("a=100&b=ほげ")
// a%3D100%26b%3D%E3%81%BB%E3%81%92
```

### SHA256ハッシュ値を計算したい

`sha256`を使う。

```go
h := sha256.New()
h.Write([]byte("あいうえおかきくけこさしすせそ"))
hash := hex.EncodeToString(h.Sum(nil))
// a5185e2f49245929acd85cfb310b395035e9ce0eedda8609a714de9896cc0b47
```

トラブル
--------

### go getでグローバルにインストールできない

* `go.mod`が存在する場所でインストールしてしまっている
    * `go.mod`が存在しない場所でインストールする必要あり
* go moduleがOFFになっている
    * `GO111MODULE=on` or `set GO111MODULE=on&`を`go get`の前に付ける必要あり

