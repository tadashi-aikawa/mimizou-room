# [Jest] FAQ


Decorators are not enabled エラーになる
---------------------------------------

### エラーケース1

以下の場合

```
If you are using ["@babel/plugin-proposal-decorators", { "legacy": true }], make sure it comes *before* "@babel/plugin-proposal-class-properties" and enable loose mode, like so:
    ["@babel/plugin-proposal-decorators", { "legacy": true }]
    ["@babel/plugin-proposal-class-properties", { "loose": true }]
```

`babel.config.js`の`plugins`配下を以下の順で定義する。  
**順番が違うと動かない。**

```
{
  "plugins": [
    ["@babel/plugin-proposal-decorators", { "legacy": true }],
    ["@babel/plugin-proposal-class-properties", { "loose" : true }]
  ]
}
```

{{refer("https://babeljs.io/docs/en/babel-plugin-proposal-decorators#legacy")}}

!!! TODO "legacyとlooseの理由を調べる"

もちろん該当pluginのインストールは必要。

### エラーケース2

以下の場合

```
Namespaces are not supported.
```

TypeScriptのnamespaceにデフォルトで対応していないから。

`babel.config.js`の`plugins`配下に以下を追加する。

```
  "plugins": [
    ["@babel/plugin-transform-typescript", {"allowNamespaces": true}],
  ]
```

{{refer("https://babeljs.io/docs/en/babel-plugin-transform-typescript")}}

デフォルトでは `allowNamespaces: false` なので明示的指定が必要。  
将来は`true`になるらしい。

{{refer("https://babeljs.io/docs/en/babel-plugin-transform-typescript#allownamespaces")}}

もちろん該当pluginのインストールは必要。


electronからimportできずエラーになる
------------------------------------

Jestはmainを通してelectronを起動していないので当然失敗する。  
処理がテストに関係なければ、Mockを作って凌ぐ。

`package.json`
```json
  # moduleNameMapperに追加
  "jest": {
    "moduleNameMapper": {
      "electron": "<rootDir>/electron-mock.ts"
    }
  }
```

`electron-mock.ts`
```ts
# `{remote.require("exec").exec`まで呼ばれることを想定
export const remote = {
  require: (required_but_ignored: string) => ({
    exec: undefined
  })
};
```

{{refer("https://stackoverflow.com/questions/46898185/electron-jest-ipcrenderer-is-undefined-in-unit-tests")}}
