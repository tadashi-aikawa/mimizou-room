# [IDEA] FAQ


全般
----

### カッコ、クォート、タグのペアが勝手に補完されるのをやめたい

設定にて

1. `Editor` > `General` > `Smart Keys` を開く
2. 以下のチェックを外す

* `Insert paired brackets`
* `Insert pair quote`
* `Insert closing tag on tag completion`

### 未保存のファイルが分かりにくい

`Editor` > `General` > `Editor Tabs` の `Mark modified` にチェックをつける。

{{refer("http://xblood.hatenablog.com/entry/2017/06/06/230000")}}

### 自動インポートのフォーマットを変更したい

`Code Style`から変更する。
linterなどと設定がすれ違うと面倒..  

#### クォーテーション

![](images/2020-01-01-13-21-06.png)

#### import前後のスペース

![](images/2020-01-01-13-21-00.png)

### クイックフィックスなしで自動インポートしたい

`Editor` > `General` > `Auto Import` の `Unambiguous imports on the fly` にチェックをつける。

### ファイルの最終行以降もスクロールしたい

1. 設定の `Editor` > `General`
2. `Virtual Space`セクション の `Show virtual space at the bottom of the file` にチェックをつける。


Python
------

### pylintを使いたい

1. `pylint`プラグインをインストール
2. `Settings` > `Other SEttings` > `pylint` で設定

!!! warning "`Path to Pylint executable` はWindowsだとpathを指定する必要あり (`/`が解釈されない)"


### リモートのPython環境を開発したい

**有料版のみ**であれば

{{link("https://blog.mamansoft.net/2019/06/29/develop-python-in-virtual-machine-with-intellij-idea/")}}


### Doctestを全ての対象ファイルに対して実行したい

pytestの`--doctest-modules`を指定すればOK。

1. `Run/Debug Configurations`
2. `Python tests > pytest` を作成
3. `Target:` を `Custom` にする
4. `Additional Arguments` に `--doctest-modules` を指定 (ついでに`--doctest-continue-on-failure` `-vv`とかも好みで)

`Working directory`に注意。配下をテストしにいくので


CLIコマンド
----------

### ターミナルから指定ディレクトリ/ファイルをIDEAで開きたい

`idea`コマンドを使えばできる.  
ファイルは単体で開き、ディレクトリはプロジェクトで開く.

以下のようなbin配下をPATHに追加しておけばどこからでも呼び出せる.

```
C:\Program Files (x86)\JetBrains\IntelliJ IDEA 2019.2\bin
```

!!! hint "自分の環境ではJDKなどの問題もあり、`idea64.exe`を使っている"

{{refer("https://pleiades.io/help/idea/opening-files-from-command-line.html")}}


Run/Debug Configurations
------------------------

### WindowsでMakeコマンドを実行したい

#### 前提条件

Windowの場合、`Settings` > `Make`の設定で`Path to Make executable`に`make.exe`の絶対パスを指定する必要あり。

```
# 例
C:\Users\tadashi-aikawa\scoop\shims\make.exe
```

方法は2通りある。

#### Makefileテンプレートを使う

| 項目              | 値                        |
| ----------------- | ------------------------- |
| Makefile          | Makefileのパス            |
| Targets           | makeのターゲット(devなど) |
| Working directory | Makefileの場所            |


#### Batchテンプレートを使う

Makefileテンプレートで動かないときはこちら..

| 項目              | 値                        |
| ----------------- | ------------------------- |
| Script            | make                      |
| Script parameters | makeのターゲット(devなど) |
| Working directory | Makefileの場所            |

