# [IntelliJ] FAQ

hoge

<div class="link-card">
            <div>
                <img src="https://avatars1.githubusercontent.com/u/9500018?s=460&v=4" width=20 class="link-card-site-icon"/>
                <span class="link-card-site-name">MAMANのITブログ</span>
            </div>
    <div class="link-card-body">
        <div class="link-card-content">
            <div>
                <p class="link-card-title">仮想マシン内のPython開発をIDEAで</p>
            </div>
            <div class="link-card-description">てすとのですくりぷしょんふつうはこのあとにいろいろなせつめいがあるとおもうのでそこまでちゃんとよみましょうね</div>
        </div>
        <img src="https://dl.dropboxusercontent.com/s/1ly6ljj1rgna7sy/asian-1839802_1280.jpg" class="link-card-image"/>
    </div>
    <a href="https://blog.mamansoft.net/2019/05/18/requirements-idea-actions/"></a>
</div>

huga

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

{{summary("https://blog.mamansoft.net/2019/06/29/develop-python-in-virtual-machine-with-intellij-idea/")}}
