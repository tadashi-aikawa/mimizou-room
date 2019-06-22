全般
----

### カッコ、クォート、タグのペアが勝手に補完されるのをやめたい

設定にて

1. `Editor` > `General` > `Smart Kes` を開く
2. 以下のチェックを外す

* `Insert paired brackets`
* `Insert pair quote`
* `Insert closing tag on tag completion`


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

!!! warning "`Path to Pylint executable` はWindowsだとpathを指定する必要あり (`/`が解釈されない)"

