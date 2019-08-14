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

