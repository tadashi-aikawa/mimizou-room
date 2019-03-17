it-note
=======

tadashi-aikawaのITに関するメモまとめ。


設計方針
--------

* 見た目にはこだわらず本質を追究する
* ディレクトリ/ファイル名は全て小文字
* 技術ごとにディレクトリを区切る。1つしか項目が無くても
* ライブラリディレクトリは言語ディレクトリの下に作る
    * JavaScriptディレクトリは作らない..TypeScriptに包含する


構成
----

ディレクトリ構成はREQUIREDだが、配下のファイルは全てOPTIONAL。


### 最上位階層

| ディレクトリ名 |                 説明                 |
| -------------- | ------------------------------------ |
| languages      | プログラミング言語                   |
| tools          | ローカルで使用するツール             |
| services       | クラウドで使用するWEBサービス/アプリ |
| concepts        | 概念。設計思想とか言語によらないもの |

### languages配下の構成

配下に言語特有のライブラリディレクトリなどが存在する。

|   ファイル名   |                   記載する内容                   |
| -------------- | ------------------------------------------------ |
| index.md       | インストールや動作、オススメリンクなどの基本情報 |
| grammer.md     | 文法や機能に関する情報                           |
| snippets.md    | よく使う表現や設定                               |
| trouble.md     | トラブルシューティング                           |
| performance.md | パフォーマンス測定系                             |

### tools配下の構成

| ファイル名  |                     記載する内容                     |
| ----------- | ---------------------------------------------------- |
| index.md    | インストール方法や動作、オススメリンクなどの基本情報 |
| config.md   | よく使う設定                                         |
| keys.md     | よく使うショートカットキー                           |
| snippets.md | よく使う表現や設定                                   |
| trouble.md  | トラブルシューティング                               |

### services配下の構成

| ファイル名 |                   記載する内容                   |
| ---------- | ------------------------------------------------ |
| index.md   | 利用開始方法や動作、オススメリンクなどの基本情報 |
| config.md  | よく使う設定                                     |
| keys.md    | よく使うショートカットキー                       |
| trouble.md | トラブルシューティング                           |

### concepts配下の構成

配下に書籍などのディレクトリが存在する。

| ファイル名 |       記載する内容       |
| ---------- | ------------------------ |
| index.md   | 基本的な情報はここに集約 |
| trouble.md | トラブルシューティング   |


### 構成イメージ

```
* languages
    * bash
        * index.md
        * grammer.md
        * snippets.md
        * trouble.md
    * python
        * index.md
        * grammer.md
        * snippets.md
        * trouble.md
        * requests
            * index.md
            * snippets.md
            * trouble.md
    * typescript
        * index.md
        * grammer.md
        * snippets.md
        * trouble.md
        * angular
            * index.md
            * grammer.md
            * snippets.md
            * trouble.md
* tools
    * idea
        * index.md
        * config.md
        * key.md
        * trouble.md
    * vscode
        * index.md
        * config.md
        * key.md
        * trouble.md
    * git
        * snippets.md
        * trouble.md
* services
    * sourcegraph
        * index.md
        * config.md
        * key.md
        * trouble.md
    * github
        * index.md
        * config.md
        * key.md
        * trouble.md
* concepts
    * ddd
        * index.md
        * trouble.md
```