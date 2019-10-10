# [VimT] Visualモード

テキストを選択して操作するモード。 `想定時間: 15分`


思想の違い
----------

Normalモードとは思想が違います。

| モード |           思想            |
| ------ | ------------------------- |
| Normal | `オペレータ`+`モーション` |
| Visual | `範囲指定` + `オペレータ` |

Vimに慣れていない場合はVisualモードの方が直感的かもしれません。  

### 2行削除してWelcomeを入力する例

Normalモードの場合は`cjWelcome`ですね。

```txt
▼
moyasu
tagayasu
okoshiyasu
```

Visualモードの場合は以下のフローです。

1. `Vj`で範囲選択
2. `c`で選択範囲を編集(削除して文字を入力)
3. `Welcome`

`VjcWelcome`と入力してみましょう。

```txt
▼
moyasu
tagayasu
okoshiyasu
```


サブモード
----------

Visualモードには選択範囲の種類によって3つのサブモードがあります。

* 文字
* 行
* 矩形


### 文字

文字単位で範囲を指定します。`v`でスタート。

`vwwhhgU`と入力してみましょう。

```txt
▼
moyasu tagayasu okoshiyasu
```


### 行

行単位で範囲を指定します。`V`でスタート。

冒頭の例はこのサブモードです。  
もう少し高度な例を試してみましょう。

Markdownの見出しを挿入する例です。  
`yypVr-`と入力してみてください。

```txt
▼
Header2

* aaa
* bbb
```

Visualモードと置換オペレータの相性は抜群ですね😄


### 矩形

矩形で範囲を選択します。`<C-v>`でスタート。

選択することより、その後の一斉編集で使うことが多いです。  
特にテーブルの編集と相性がいいです。

`ww<C-v>4jI<space>|<space><ESC>`

```txt
▼
| name age |
| -------- |
| Tom  18  |
| Merry23  |
| Yasu 33  |
```

２行目以降が遅れて反映されるのは仕様です。


Normalモードとの使い分け
------------------------

得意分野が違うため、以下のケースに合致する場合だけVisualモードを使います。

* 視覚的フィードバックが欲しいとき
* 特定の範囲をyankされたデータで置換したいとき
* 矩形で編集したいとき

特に2つ目は大事なので例を示します。

箇条書きの`Yasu`を`Tagayasu`に変更したいケースです。  

```txt
▼
<Students>

* Tom
* Merry
* Yasu

--

Todo: Yasu -> Tagayasu
```

以下のコマンドを実行してみましょう。

* `/Ta<CR>yw`でテキストをyank
* `4kh`で移動
* `viwp`で貼り付け

```txt
▼
<Students>

* Tom
* Merry
* Yasu

--

Todo: Yasu -> Tagayasu
```

Normalモードで同じことをやる場合は最後のコマンドを`diwp`にすれば良いと思うでしょうか。  
是非やってみてください。

```txt
▼
<Students>

* Tom
* Merry
* Yasu

--

Todo: Yasu -> Tagayasu
```

実は`diw"0p`とやらなければダメなんですね😈  
興味がある方はレジスタについて調べてみてください。


おまけ
------

覚えておくと便利な範囲選択ショートカットです。

|         キー         |             意味             |   覚え方   |
| -------------------- | ---------------------------- | ---------- |
| Visualモード中に`o`  | 範囲の反対側を拡張する       | Opposite   |
| Normalモード中に`gv` | 最後に選択した範囲を指定する | God Visual |

以下の順にコマンドを打って試してみましょう。

1. `vwobgUG`
2. `gvgu`

```txt
"ari" "ori" "haberi" "imasugari"
             ▼
"moyasu" "tagayasu" "yatagarasu"
"hoge" "hoga" "hogu" "hoho" "homi"
```
