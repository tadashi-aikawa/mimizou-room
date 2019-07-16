# [Vim] FAQ


全体
----

### 全ての設定をOFFにして起動したい

```
$ vim -u NONE -N
```

* `-u`は別の設定を読み込むオプションなので`NONE`にすると`.vimrc`を読み込まない
* `-N`はviとの互換性..`compatible`をオフにする

### ターミナルをVimとシームレスに操作したい

Vimから`:terminal`を呼び出すことで以下のメリットがある。

* `<C-w>N`でターミナルがVimモードになる
* `<C-w>""`でVimとターミナルのyankが共有できる

### git bash vimで`HOME`と`END`が`ÏH`と`ÏF`になる

以下の設定が悪い方向に競合していたので、削除したらなおった。

```
" MetaキーにAltを割り当てる
let c = 'a'
while c <= 'z'
    execute "set <M-" . c . ">=\e" . c
    execute "imap \e" . c . " <M-" . c . ">"
    execute "set <M-S-" . c . ">=\e" . toupper(c)
    execute "imap \e" . toupper(c) . " <M-" . c . ">"
    let c = nr2char(1+char2nr(c))
endw
```


オペレーション
--------------

### ファイル名を貼り付けたい

`"%p`

{{refer("https://vim-jp.org/vim-users-jp/2010/02/01/Hack-121.html")}}

### クリップボードをペーストするとインデントがおかしくなる

`:a!`してからペースト

### MakefileでTABを入力できない

`set expandtab`を`.vimrc`で設定している場合なら、`set noet` で無効にできる。  
今だけ入力したいなら`<C-v><TAB>`の方がよいかも。

### エラーメッセージが1行しか表示されない

`:message`で表される

### 検索や置換を正規表現で指定したい

very magicを利用します。`\v`を頭ににつけるだけ。

### コマンドの実行結果を挿入したい

* `:r!`で次の行に挿入
* `!!`で現在行を置換

### 別のファイルの内容を挿入したい

* `:r`で次の行に指定ファイルを挿入

### 複数ファイルに同じ操作をしたい

#### 複数ファイルの一括置換

確認不要の場合は`c`を外す

```
:args *
:argdo %s/before/after/gc | update
```

#### 複数ファイルの一括操作

```
args *
:argdo exec "norm iTANAHASHI" | update
```


見た目
------

### Vimに色が付かない

`set termguicolors`を外してみる

{{refer("https://qiita.com/foooomio/items/9f5a1948104f8f26d38a")}}


Markdown
--------

### Markdownファイルの編集が重い

`plasticboy/vim-markdown`を使っている場合で`Foldexpr_markdown`が重い場合は以下の設定を追加することで無効化できます。

```
let g:vim_markdown_folding_disabled = 1
```

{{refer("https://osiux.gitlab.io/2018-08-15-realizar-un-profile-en-vim-y-deshabilitar-foldexpr-markdown.html")}}