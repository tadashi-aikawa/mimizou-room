# [Jest] FAQ


テストの実行方式について
-----------------------

### 1テストSuiteずつ直列に実行したい

`--runInBand`オプションをつける


テストの書き方について
----------------------

### テスト対象の中でimportしているモジュールのMockを作りたい

`companyService.fetch`が`clients/api`を使っているケース。  
`clients/api`をMock化して、副作用の無い状態で`companyService.fetch`をテストしたい。

`jest.mock`でモック化すれば、それをimportしている箇所全てに影響が出る。

```ts
import * as companyService from './company';
import * as api from '../clients/api';
jest.mock('../clients/api');

describe('companyService.fetch', () => {
  beforeAll(() => {
    (svn as any).list.mockReturnValue(['dummy1', 'dummy2']);
  });
  test('テスト', async () => {
    const actual = await companyService.fetch();
    expect(actual).toStrictEqual(['dummy1, dummy2']);
  });
});
```

モック化した`モジュール.プロパティ`に対して、`mockReturnValue(...)`で任意の値をreturnさせる。  
`mockImplementation((arg1, arg2) => arg1 + arg2)`のようにすると任意のfunctionを定義できる。

### 一定時間内で何度か確認してOKかを判定したい

`wait-for-except`を使う.

{{link("https://github.com/TheBrainFamily/wait-for-expect#readme")}}


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
