# [IntelliJ] FAQ


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

### pylintを使いたい

1. `pylint`プラグインをインストール
2. `Settings` > `Other SEttings` > `pylint` で設定

!!! warning "`Path to Pylint executable` はWindowsだとpathを指定する必要あり (`/`が解釈されない)"


### リモートのPython環境を開発したい

!!! warning "有料版のみ"

{{link("https://blog.mamansoft.net/2019/06/29/develop-python-in-virtual-machine-with-intellij-idea/")}}
