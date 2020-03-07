# [TypeScript] FAQ


targetやmodule系の設定違いが分からない
------------------------------------------------

|      設定名      |                     意味                      |                  個人的推奨                  |
| ---------------- | --------------------------------------------- | -------------------------------------------- |
| target           | コンパイル後のjsコードをどの仕様にするか      | es2015. レガシー環境ならes5                  |
| module           | moduleの読みこみをどのように表現するか        | nodejsならcommon. それ以外ならデフォルト[^1] |
| moduleResolution | module解決方法の指定                          | デフォルト[^2]                               |
| esModuleInterop  | `import * as A from 'a'` の `* as` を省略可能 | `true`                                       |

[^1]: targetがES2015より前なら`CommonJS`、そうでないなら`ES6`
[^2]: targetがAMD or System or ES6なら`Classic`、そうでないなら`Node`

{{refer("https://www.typescriptlang.org/docs/handbook/compiler-options.html")}}


tsconfig.jsonが読み込まれない
-----------------------------

`tsc`コマンドでファイルを指定した場合、古いバージョンのtscでは`tsconfig.json`が暗黙的に読み込まれない。

!!! TODO "どうしても指定したい場合の方法は分からず.."


`TS2307: Cannot find module 'lodash'.`
--------------------------------------

### グローバルの古いtscを使っているケース

間違ってグローバルの古いtscを使っている場合はプロジェクトのtscを使うこと。(npm or npx)

### 定義ファイルを読み込んでいないケース

```
$ npm i -D @types/lodash
```

jsonファイルをインポートしたい
------------------------------

`tsconfig.json`の`compilerOptions`に以下を記載する。

```json
  "resolveJsonModule": true,`
```

こんな感じ。

```ts
import * as pkg from '~/package.json';
```
