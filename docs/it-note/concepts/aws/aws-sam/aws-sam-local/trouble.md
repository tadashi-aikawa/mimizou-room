# [SAM Local] FAQ


`--env-vars` or `-n`で指定した環境変数が有効にならない
------------------------------------------------------

コマンド

```
$ sam local start-api --env-vars env.json
```

### 関数名はあっているか?

テンプレートでLambda関数名が以下のようになっているとき

```yaml
Resources:
  HelloWorldFunction:
```

その名前が`env.json`でそのまま使われているかを確認してください。

```json
{
  "HelloWorldFunction": {
    "VAR_NAME": "hoge"
  }
}
```


### `template.yaml`で該当の変数名は定義されているか?

以下のように`env.json`で指定した変数が定義されているかを確認してください。  
もし`VAR_NAME`が定義されていなければ、`env.json`の値は有効になりません。

```yaml
Resources:
  HelloWorldFunction:
    Properties:
      Environment:
        Variables:
          VAR_NAME: dummy
```