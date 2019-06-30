# [VS Code] FAQ


ファイルをクリックしたら新しいタブで開きたい
--------------------------------------------

`Workbench > Editor: Enable Preview` のチェックを外す。

設定だと `"workbench.editor.enablePreview": false`


batファイルをShift-JISで開きたい
--------------------------------

拡張子ごとのエンコーディング指定を設定(`settings.json`)に追加する。

```
  "[bat]": {
    "files.encoding": "shiftjis"
  },
```
