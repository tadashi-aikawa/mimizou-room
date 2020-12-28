# [TypeScript] Top


公式
----

{{link("https://www.typescriptlang.org/")}}


学習
----

### 正確な情報が欲しい

公式が最強。英語に抵抗なければ。

{{link("https://www.typescriptlang.org/docs")}}

JavaScriptの経験があるなら`The TypeScript Handbook`を抑えておけばOK。  
ただし分量は多い。

{{link("https://www.typescriptlang.org/docs/handbook/intro.html")}}

最新情報や歴史的経緯を学ぶならリリースノート。

{{link("https://www.typescriptlang.org/docs/handbook/release-notes/overview.html")}}

本サイトでもリリースノートを自分なりにまとめたページを公開している。

{{link("https://mimizou.mamansoft.net/it-note/languages/typescript/releases/")}}

### 要点を抑えて基礎を効率的に学びたい

冒頭にあるよう`本読者がTypeScriptをすぐに実用できるよう、最短ルートに読者を導く一冊`。

{{link("https://book.yyts.org/")}}

### 仕事ですぐに使える知識を一通り知りたい

未経験だけど仕事で使うことになったんじゃぁぁぁぁという人向け。

{{link("https://future-architect.github.io/typescript-guide/")}}

### 型について詳しく知りたい

ES2015以降やNode.js、npmなどを知っている人向け。

http://typescript.ninja/typescript-in-definitelyland/

!!! warning ""
    対応TypeScriptバージョンは古いので注意 (TypeScript 2.4.2)

### 特有の組み込み型について知りたい

TypeScriptならではの型が紹介されている。

{{link("https://log.pocka.io/posts/typescript-builtin-type-functions/")}}

### 非同期処理について分かりやすく知りたい

非同期でハマった人向け。PromiseとAsync/Awaitを学ぶなら分かりやすく詳しい。

{{link("https://azu.github.io/promises-book/")}}

### JavaScriptをしっかり学習したい

JavaScriptだけでなくプログラミングそのものについても学べる良書。

{{link("https://jsprimer.net/")}}


フレームワーク/ライブラリの選定
-------------------------------

### Pacakge Manager

|  名前  | 採用 | IDEAプラグイン | VSCode拡張 |
| ------ | ---- | -------------- | ---------- |
| [npm]  | O    |                |            |
| [yarn] |      |                |            |

[npm]: https://www.npmjs.com/
[yarn]: https://yarnpkg.com/ja/


### Test

|  名前  | 採用 | IDEAプラグイン | VSCode拡張 |
| ------ | ---- | -------------- | ---------- |
| [Jest] | O    | 不要           |            |
| [AVA]  |      |                |            |

[jest]: https://jestjs.io/ja/
[ava]: https://github.com/avajs/ava


### Linter

|   名前   | 採用 | IDEAプラグイン | VSCode拡張 |
| -------- | ---- | -------------- | ---------- |
| [eslint] | O    |                |            |
| [tslint] |      |                |            |

[eslint]: https://eslint.org/
[tslint]: https://palantir.github.io/tslint/


### Formatter

|    名前    | 採用 | IDEAプラグイン |         VSCode拡張          |
| ---------- | ---- | -------------- | --------------------------- |
| [prettier] | O    |                | [Prettier - Code formatter] |

[prettier]: https://prettier.io/
[Prettier - Code formatter]: https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode


### CLI Framework

|  名前   | 採用 | IDEAプラグイン | VSCode拡張 |
| ------- | ---- | -------------- | ---------- |
| [oclif] | O    |                |            |

[oclif]: https://oclif.io/docs/introduction


### doc

|  名前   | 採用 | IDEAプラグイン | VSCode拡張 |
| ------- | ---- | -------------- | ---------- |
| [tsdoc] | O    |                |            |

[tsdoc]: https://github.com/microsoft/tsdoc

### 暗号/ハッシュ

|    名前     | 採用 | IDEAプラグイン | VSCode拡張 |
| ----------- | ---- | -------------- | ---------- |
| [crypto-js] | O    |                |            |

[crypto-js]: https://github.com/brix/crypto-js

### クリップボード

|          名前          | 採用 |                      備考                      |
| ---------------------- | ---- | ---------------------------------------------- |
| [gforceg/ts-clipboard] | O    | TypeScriptならコレ                             |
| [clipboard-polyfill]   | O    | JavaScriptでタブや改行も上手くコピーしてくれる |

[gforceg/ts-clipboard]: https://github.com/gforceg/ts-clipboard
[clipboard-polyfill]: https://github.com/lgarron/clipboard-polyfill


よく使うビルドオプション
------------------------

### `--incremental`

静的インクリメンタルビルド。  
少なくてもビルド速度が半分以下になるので使ったほうがいい。

キャッシュに使うファイルとして、`--outDir`で指定された場所に`tsconfig.tsbuildinfo`ができる。

{{refer("https://qiita.com/vvakame/items/7f4a55fe15fc9bbe1a63")}}

### `--watch`

動的インクリメンタルビルド。  
スピードは最速だが、一度停止すると次はフルビルドになる。
