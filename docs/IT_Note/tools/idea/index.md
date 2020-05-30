---
description: Intellij IDEAの設定やプラグインなどを紹介
---

# [IDEA] Top

{{ page.meta.description }}


IntelliJ IDEAとは
-----------------

JetBrains製の統合開発環境。

{{link("https://www.jetbrains.com/idea/")}}

Java中心だが、Ultimate版は様々な言語を使える。


ショートカットキー
------------------

ブログでいくつか記事を書いたのでそちらを参照。

### Must

{{link("https://blog.mamansoft.net/2019/05/18/requirements-idea-actions/")}}

### Should

{{link("https://blog.mamansoft.net/2019/05/20/recommended-idea-actions/")}}

### Have to

{{link("https://blog.mamansoft.net/2019/05/22/idea-actions-if-possible/")}}

### VS Codeとショートカットキーをあわせる

VS Codeも使っている場合はコンテキストスイッチの切り替えコストを下げるため、同じキーバインドが望ましい。

{{link("https://docs.google.com/spreadsheets/d/11KZFwz_KJWeN-zRGRV74pCubN0_k3yDaDDr7tErHPrY/edit#gid=0")}}


プラグイン
----------

言語系のプラグインは各言語ページに記載するため除く。

| プラグイン名                 | 説明                                         |
| ---------------------------- | -------------------------------------------- |
| [Python]                     | Pythonのサポート                             |
| [Rust]                       | Rustのサポート                               |
| [PowerShell]                 | PowerShellのサポート                         |
| [Batch Scripts Support]      | Batchのサポート                              |
| [BashSupport]                | Bashのサポート                               |
| [Vue.js]                     | Vueのサポート                                |
| [File Watchers]              | ファイルが変更されたときに処理を実施できる   |
| [IdeaVim]                    | Vim！！                                      |
| [IdeaVim-EasyMotion]         | vim-easy-motionの再現                        |
| [Paste Images into Markdown] | Markdownファイルにクリップボードの画像を挿入 |
| [String Manipulation]        | 文字列を色々操作できる                       |
| [Prettier]                   | prettierと連携 (保存時自動実行など)          |
| [Markowl]                    | Markdownの便利ツール                         |

[File Watchers]: https://plugins.jetbrains.com/plugin/7177-file-watchers
[IdeaVim]: https://plugins.jetbrains.com/plugin/164-ideavim
[IdeaVim-EasyMotion]: https://plugins.jetbrains.com/plugin/13360-ideavim-easymotion
[Paste Images into Markdown]: https://plugins.jetbrains.com/plugin/8446-paste-images-into-markdown
[String Manipulation]: https://plugins.jetbrains.com/plugin/2162-string-manipulation
[Prettier]: https://plugins.jetbrains.com/plugin/10456-prettier
[Python]: https://plugins.jetbrains.com/plugin/631-python
[Vue.js]: https://plugins.jetbrains.com/plugin/9442-vue-js
[Batch Scripts Support]: https://plugins.jetbrains.com/plugin/265-batch-scripts-support
[BashSupport]: https://plugins.jetbrains.com/plugin/4230-bashsupport
[Markowl]: https://plugins.jetbrains.com/plugin/14116-markowl
[Rust]: https://plugins.jetbrains.com/plugin/8182-rust
[PowerShell]: https://plugins.jetbrains.com/plugin/10249-powershell


File Watchersの設定
-------------------

開いているファイルだけフォーマットしたいので、`Advanced options`のチェックは全て外す。

### Black

リモートインタプリタを使う場合があるので`Program`はグローバル環境の`black`を参照するようにします。

|   項目    |      値      |
| --------- | ------------ |
| File type | Python       |
| Scope     | Current File |
| Program   | black        |
| Arguments | $FilePath$   |
