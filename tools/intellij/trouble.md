Python
------

### yapfで保存時にフォーマットしたい

`File Watchers`プラグインがインストールされているうえで

1. `Settings` > `Tools` > `File Watchers`
2. `<Custom>` で作成
3. 以下の様にする
    * `File type`: `Python`
    * `Scope`: `Current File`
    * `Program`: `$PyInterpreterDirectory$\yapf`
    * `Arguments`: `-i $FilePath$`
    * `Advanced Options`
        * `Auto-save edited files to trigger the watcher` を外す
        * `Trigger the watcher on external changes` を外す

### pylintを使いたい

1. `pylint`プラグインをインストール
2. `Settings` > `Other SEttings` > `pylint` で設定

⚠️ `Path to Pylint executable` はWindowsだとpathを指定する必要あり (`/`が解釈されない)

