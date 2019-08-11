# [VS Code] FAQ


ファイルをクリックしたら新しいタブで開きたい
--------------------------------------------

`Workbench > Editor: Enable Preview` のチェックを外す。

設定だと `"workbench.editor.enablePreview": false`


特定ファイルのPrettierをオフにしたい
--------------------------------

設定に`"prettier.disableLanguages": [...]`を追加。

Markdownの場合は`"prettier.disableLanguages": ["markdown"]`。

{{refer("https://qiita.com/the_red/items/e121cbb659c52a60bca6")}}


batファイルをShift-JISで開きたい
--------------------------------

拡張子ごとのエンコーディング指定を設定(`settings.json`)に追加する。

```
  "[bat]": {
    "files.encoding": "shiftjis"
  },
```
