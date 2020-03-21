---
title: はじめに
---

思考の速度[^1]でエンジニアリングを回すために必要な**自分用**メモです。

![](https://i0.wp.com/nlv.jp/wp-content/uploads/2017/02/4992967e799f4a17aee055a5d9a119f4.jpg)

!!! danger "記載された情報を過信しないで下さい"

    本ページに記載の情報は正しいことを保証しません。
    記載時点では最新でも現時点では古くなっている恐れがあります。[^2]

    また、本ページの情報によって生じた不都合に対して一切の責任を持ちません。


設計方針
--------

見た目にはこだわらず本質を追究する。

* ディレクトリ/ファイル名は全て小文字
* 技術ごとにディレクトリを区切る
* ライブラリディレクトリは言語ディレクトリの下に作る


構成
----

ディレクトリ構成はREQUIREDだが、配下のファイルは全てOPTIONAL。

※ 古いファイルの`faq.md`は`trouble.md`となっている

=== "最上位"

    | ディレクトリ名 |                 説明                 |
    | -------------- | ------------------------------------ |
    | languages      | プログラミング言語                   |
    | tools          | ローカルで使用するツール             |
    | services       | クラウドで使用するWEBサービス/アプリ |
    | concepts        | 概念。設計思想とか言語によらないもの |

=== "languages"

    配下に言語特有のライブラリディレクトリなどが存在する。

    |   ファイル名   |                   記載する内容                   |
    | -------------- | ------------------------------------------------ |
    | index.md       | インストールや動作、オススメリンクなどの基本情報 |
    | grammer.md     | 文法や機能に関する情報                           |
    | snippets.md    | よく使う表現や設定                               |
    | trouble.md     | トラブルシューティング                           |
    | performance.md | パフォーマンス測定系                             |

=== "tools"

    | ファイル名  |                     記載する内容                     |
    | ----------- | ---------------------------------------------------- |
    | index.md    | インストール方法や動作、オススメリンクなどの基本情報 |
    | config.md   | よく使う設定                                         |
    | keys.md     | よく使うショートカットキー                           |
    | snippets.md | よく使う表現や設定                                   |
    | faq.md      | トラブルシューティング                               |

=== "services"

    | ファイル名 |                   記載する内容                   |
    | ---------- | ------------------------------------------------ |
    | index.md   | 利用開始方法や動作、オススメリンクなどの基本情報 |
    | config.md  | よく使う設定                                     |
    | keys.md    | よく使うショートカットキー                       |
    | faq.md     | トラブルシューティング                           |

=== "concepts"

    配下に書籍などのディレクトリが存在する。

    | ファイル名 |       記載する内容       |
    | ---------- | ------------------------ |
    | index.md   | 基本的な情報はここに集約 |
    | faq.md     | トラブルシューティング   |


### 構成イメージ

??? example "クリックで展開"

    * languages
        * bash
            * index.md
            * grammer.md
            * snippets.md
            * faq.md
        * python
            * index.md
            * grammer.md
            * snippets.md
            * faq.md
            * requests
                * index.md
                * snippets.md
                * faq.md
        * typescript
            * index.md
            * grammer.md
            * snippets.md
            * faq.md
            * angular
                * index.md
                * grammer.md
                * snippets.md
                * faq.md
    * tools
        * idea
            * index.md
            * config.md
            * key.md
            * faq.md
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



[^1]: [分裂勘違い君劇場]の影響を受けています。
[^2]: 最終更新日を知りたい場合はGitHubのコミット履歴を参照してください。

[分裂勘違い君劇場]: https://www.furomuda.com/entry/20070212/1171244226
[mkdocs]: https://www.mkdocs.org
