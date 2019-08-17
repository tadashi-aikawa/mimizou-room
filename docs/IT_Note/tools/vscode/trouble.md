# [VS Code] FAQ


全般
----

### ファイルをクリックしたら新しいタブで開きたい

`Workbench > Editor: Enable Preview` のチェックを外す。

設定だと `"workbench.editor.enablePreview": false`


### 特定ファイルのPrettierをオフにしたい

設定に`"prettier.disableLanguages": [...]`を追加。

Markdownの場合は`"prettier.disableLanguages": ["markdown"]`。

{{refer("https://qiita.com/the_red/items/e121cbb659c52a60bca6")}}


### batファイルをShift-JISで開きたい

拡張子ごとのエンコーディング指定を設定(`settings.json`)に追加する。

```
  "[bat]": {
    "files.encoding": "shiftjis"
  },
```


JavaScript系
------------

### node.jsのVSCode外プロセスに対してデバッグしたい

デバッガから実行できないケース。

* `node`は`--inspect=<port>`オプションを指定して実行する
* VSCodeのActionで`Debug: Nodeのプロセスにアタッチ`を選択肢、上記プロセスを選ぶ

{{refer("https://nodejs.org/ja/docs/guides/debugging-getting-started/#header-")}}

### aws-sam-localでTypeScriptをデバッグしたい

構成が以下の場合。

```
.
├── event.json
├── yourapp
│   ├── dist  (build後にできる)
│   │   └── index.js
│   ├── index.ts
│   ├── package.json
│   ├── package-lock.json
│   ├── src
│   │   ├── clients
│   │   └── services
│   ├── tests
│   │   └── unit
│   │       └── test-handler.js
│   ├── tsconfig.json
│   └── webpack.config.js
└── template.yaml
```


#### `tsconfig.json`

`outDir`に注意。  
`sourceMap: true` をつける。

```json
{
  "compilerOptions": {
    "target": "es6",
    "module": "commonjs",
    "sourceMap": true,
    "strict": true,
    "esModuleInterop": true
  }
}
```

#### `webpack.config.js`

`target`と`libraryTarget`に注意。

```js
// inline-source-mapにできる?
module.exports = {
  devtool: 'inline-source-map',
  entry: './index.ts',
  target: 'node',
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: ['.ts', '.js'],
  },
  output: {
    filename: 'index.js',
    path: path.resolve(__dirname, 'dist'),
    libraryTarget: 'commonjs2',
  },
};
```

#### `launch.json`

* `outFiles`を指定しないとTypeScriptソースのブレイクポイントで停止しない
* `localRoot`と`remoteRoot`配下それぞれにjsファイル(with sourcemap)が必要
* `sourceMap`はデフォルトで`true`なので設定不要
* Webpack利用時は`sourceMapPathOverrides`の指定が必要

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "AWS SAM start-api",
      "type": "node",
      "request": "attach",
      "address": "localhost",
      "port": 5858,
      "localRoot": "${workspaceRoot}/yourapp/dist",
      "remoteRoot": "/var/task",
      "protocol": "inspector",
      "stopOnEntry": false,
      "smartStep": true,
      "sourceMapPathOverrides": {
        "webpack:///./~/*": "${workspaceRoot}/yourapp/node_modules/*",
        "webpack:///./*": "${workspaceRoot}/yourapp/*",
        "webpack:///*": "*"
      },
      "outFiles": ["${workspaceRoot}/yourapp/dist/*.js"]
    }
  ]
}
```

#### 実行

`webpack --watch & sam local start-api --template ../template.yaml -d 5858`


拡張機能
--------

### REST Clientで環境変数を使いたい(秘密情報として)

`{{$processEnv 環境変数名}}` でOK。

`rest-client.environmentVariables`に指定した環境変数を使いたいなら

```
{{$processEnv %キー名}}
```

{{refer("https://marketplace.visualstudio.com/items?itemName=humao.rest-client")}}
