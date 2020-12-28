# [shellcheck] FAQ

### 特定行のエラーを無視したい

以下のように`disable`アノテーションを指定する。

```bash
# shellcheck disable=SC1091
```

disableするコードが分からない場合は公式にチェッカーにスクリプトを貼り付ける。  
下の出力画面にSCから始まるエラーコードが表示される。

{{link("https://www.shellcheck.net/")}}

