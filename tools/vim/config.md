必須の.vimrc
------------

```vim
" 行番号表示
set number
" 検索結果ハイライト
set hlsearch
" 折りたたみ無効
set nofoldenable
" 挿入モードと編集モードでカーソルの形を変更
let &t_ti.="\e[2 q"
let &t_SI.="\e[5 q"
let &t_EI.="\e[2 q"
let &t_te.="\e[0 q"
" TABの可視化
set list
set listchars=tab:»˙,trail:˙,eol:,extends:»,precedes:«,nbsp:%
set showtabline=2
" タブのデザイン変更
:hi TabLine     ctermfg=White ctermbg=240
:hi TabLineFill ctermfg=Black ctermbg=Black
:hi TabLineSel  ctermfg=White ctermbg=196
" コマンドを待たない
set ttimeoutlen=1
" タブの代わりにスペースを使う
set expandtab
" インデント設定
set autoindent
set smartindent
" 行末に必ず1文字空ける
set virtualedit=onemore
" インクリメンタルサーチ
set incsearch
" 大文字/小文字の無視
set ignorecase
" 大文字がある場合は大文字/小文字を考慮
set smartcase
" 前後5行は必ず表示
set scrolloff=5
" swapファイルを作らない
set noswapfile
```
