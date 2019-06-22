基本
----

### 変数の宣言

#### 基本

`declare` 推奨。

```bash
declare -r HOGE='hogehoge'
```

よく使うオプション

| オプション |     意味     |
|------------|--------------|
| -a         | 配列         |
| -f         | 関数名       |
| -i         | 整数         |
| -r         | 読み取り専用 |
| -u         | 大文字       |
| -l         | 小文字       |

※ `declare -r` は `readonly` で代用可能

#### スコープ

関数などでスコープを制限する場合は `local` を付ける。

```bash
local var1=2
declare -i local var2=2
```


### 変数へ値を代入

```bash
a=10
```

※ イコールの前後に空白を入れるとエラーになる

変数は先頭に `$` を付ける。

```
echo $a
echo ${a}
```


### 変数へ変数を代入

```
a=$b
```

*文字列演算子構文* を使うことでより簡潔な記述が可能。


### 配列の宣言

```
array=(a1 a2 a3)
```


### 条件判定

 |       記述例       |                                     意味                                    |
 |--------------------|-----------------------------------------------------------------------------|
 | -a file            | file が存在する                                                             |
 | -b file            | file が存在し、かつブロックデバイスファイルである                           |
 | -c file            | file が存在し、かつキャラクタデバイスファイルである                         |
 | -d file            | file が存在し、かつディレクトリである                                       |
 | -e file            | file が存在する (-aと同じ)                                                  |
 | -f file            | file が存在し、かつ通常ファイルである                                       |
 | -g file            | file が存在し、かつsetgidビットがセットされている                           |
 | -G file            | file が存在し、かつ実行グループIDによって所有されている                     |
 | -h file            | file が存在し、かつシンボリックリンクである                                 |
 | -k file            | file が存在し、かつstickyビットがセットされている                           |
 | -L file            | file が存在し、かつシンボリックリンクである                                 |
 | -n string          | string がnullではない                                                       |
 | -N file            | file が最後の読み取りの後に変更されている                                   |
 | -O file            | file が存在し、かつ実行ユーザーIDによって所有されている                     |
 | -p file            | file が存在し、かつパイプまたは名前付きパイプ(FIFOファイルである)           |
 | -r file            | file が存在し、かつ読み取り可能である                                       |
 | -s file            | file が存在し、空ではない                                                   |
 | -S file            | file が存在し、かつソケットである                                           |
 | -t N               | ファイルディスクリプタNが端末を指している                                   |
 | -u file            | file が存在し、かつsetuidビットがセットされている                           |
 | -w file            | file が存在し、かつ書き込み可能である                                       |
 | -x file            | file が存在し、ファイルの場合は実行可能、ディレクトリの場合は検索可能である |
 | -z string          | string の長さがゼロ                                                         |
 | fileA -nt fileB    | fileA が fileB よりも新しい                                                 |
 | fileA -ot fileB    | fileA が fileB よりも古い                                                   |
 | fileA -ef fileB    | fileA と fileB が同じファイルを指している                                   |
 | stringA = stringB  | stringA が stringB に等しい (POSIXバージョン)                               |
 | stringA == stringB | stringA が stringB に等しい                                                 |
 | stringA != stringB | stringA と stringB が一致しない                                             |
 | stringA =~ regexp  | stringA が 拡張正規表現 regexp と一致する                                   |
 | stringA < stringB  | 語彙の順番では stringA は stringB よりも前にある                            |
 | stringA > stringB  | 語彙の順番では stringA は stringB よりも後ろにある                          |
 | exprA -eq exprB    | 算術演算子 exprA と exprB は等しい                                          |
 | exprA -ne exprB    | 算術演算子 exprA と exprB は等しくない                                      |
 | exprA -lt exprB    | 算術演算子 exprA は exprB よりも小さい                                      |
 | exprA -gt exprB    | 算術演算子 exprA は exprB よりも大きい                                      |
 | exprA -le exprB    | 算術演算子 exprA は exprB 以下である                                        |
 | exprA -ge exprB    | 算術演算子 exprA は exprB 以上である                                        |
 | exprA -a exprB     | 算術演算子 exprA および exprB はともに真である                              |
 | exprA -o exprB     | 算術演算子 exprA または exprB は真である                                    |


記述例

```bash
if [ $1 -eq 8 ]
then
    echo 'yes'
elif [ $1 -eq 7 ]
then
    echo 'yeah'
else
    echo 'no'
fi
```

セミコロンをつけるとthenを同一行にすることも可能

```bash
if [ $1 -eq 8 ]; then
    echo 'yes'
elif [ $1 -eq 7 ]; then
    echo 'yeah'
else
    echo 'no'
fi
```


### 繰り返し文

#### 配列

```bash
array=(a1 a2 a3)
for i in ${array[@]}
do
    echo ${i}
done
```

#### リストもどき

```bash
list='1 2 3'
for i in ${list}
do
    echo ${i}
done
```

#### csv

```bash
list=$(echo '1,2,3' | sed -e 's/,/ /g')
for i in ${list}
do
    echo ${i}
done
```

#### 可変長引数

```bash
for arg in $*
do
    echo ${arg}
done
```

#### 実行ディレクトリのファイル一覧

```bash
for i in *
do
    echo ${i}
done
```

#### コマンド結果

引数のファイルをcatした結果を取得し、順番に表示する。

```bash
for i in $(cat $1)
do
    echo ${i}
done
```


### 文字列の分解と結合

#### 文字列の結合

```bash
str1='Lo'
str2='ve'
union=${str1}${str2}

echo ${union}
```

#### 文字列の分解

`variable` の a番目から、b文字を切り出す方法

```bash
sliced=${variable:a-1:b}
```

例えば、以下の出力結果は `567` になる。

```bash
variable="1234567890"
echo ${variable:4:3}
```



応用
----

### ヒアドキュメント

コマンドの入力を標準入力にすることができる。  
スクリプト内で別ファイルを作成するときなどに有効。

```bash
# ラベル(下記ではEOF)が登場するまでが標準入力
$ cat << EOF
> a
> b
> EOF
a
b
```

また、ラベルをコーテーションで括ると、変数展開やコマンド置換が無効になる。

```bash
$ HOGE=hogehogeeeee
# コーテーション無しでは${HOGE}も`ls | wc -c`も展開される
$ cat << EOF
${HOGE}
`ls | wc -c`
EOF
hogehogeeeee
62

# コーテーション有りでは${HOGE}も`ls | wc -c`もそのまま
$ cat << 'EOF'
${HOGE}
`ls | wc -c`
EOF
${HOGE}
`ls | wc -c`
```

一部だけ展開したくない場合は `\${HOGE}` と記述する。


頻出表現
--------

### ログの装飾

```bash
# ログ出力設定
readonly INFO="\x1b[32;01m"
readonly WARN="\x1b[35;01m"
readonly ERROR="\x1b[31;01m"
readonly NORMAL="\x1b[0m"
info() {
  echo -e ${INFO}[INFO]: $1${NORMAL}
}
warn() {
  echo -e ${WARN}[WARN]: $1${NORMAL}
}
error() {
  echo -e ${ERROR}[ERROR]: $1${NORMAL}
}
```


### 例外処理

例外処理は ``$?`` の戻り値を確認する。

```bash
# 直前のコマンドに対して例外処理を行う
if [ $? != 0 ]; then
    echo 'error'
    exit 1
fi
```

複数箇所で使用する場合は関数化する方が便利。

```bash
# 直前のコマンドが正常終了していない場合にメッセージを表示して異常を返却
ErrCheck()
{
    if [ $? != 0 ]; then
        echo $1
        return 1
    fi
}
```


### URLデコード

```bash
echo -n "ふがふが　ほげほげ" | nkf -wMQ | sed 's/=$//g' | tr = % | tr -d "\n"
```


### バックアップ作成

```bash
# ${dirs}配下の${file}を${dst}配下に階層付でコピー
$ find ${dirs} -name ${file} -print | cpio -pdv ${dst}
```


デバッグ
--------

### デバッグログを出す

`-x` オプションを指定すると全てのコマンドを出力する。

```bash
sh -x test.sh
```


コマンドライン処理の流れ
------------------------

コマンドラインに入力された文字列は以下のフローで処理される。  
各フローの詳細は別途説明する。

```
1. トークンに分解
    + シングルコーテーションで囲まれている
        - 11へ
    + ダブルコーテーションで囲まれている
        - 6へ
    + その他
        - 2へ
2. 1つ目のトークンを確認
    + 開始キーワード
        - 1に戻り、次のコマンドを読み込む
    + その他のキーワード
        - 構文エラー
    + キーワードではない
        - 3へ
3. 1つ目のトークンを確認
    + エイリアスである
        - エイリアスを展開して、1へ
    + エイリアスではない
        - 4へ
4. {}展開
5. チルダ展開
6. パラメータ展開
7. コマンド置換
8. 算術置換
    + ダブルコーテーションで囲まれている
        - 11へ
9. ワードの抽出
10. パス名展開
11. コマンド検索 (関数、組み込みコマンド、実行可能ファイル)
12. コマンドの実行

    + evalがある
        - 引数を次のコマンドにする
    + evalがない
        - コマンドを実行
```


### 1. トークンに分解

下記規定のメタ文字でトークンに分解する。

* スペース
* タブ
* 改行
* ;
* (
* )
* <
* >
* \|
* &

トークンの種類は以下

* ワード
* キーワード
* 入出力リダイレクタ
* セミコロン


### 2. 1つ目のトークンを確認

1つ目のトークンがキーワードかを判定する。

開始キーワードは以下

* if
* function
* {
* (

開始キーワードではないキーワードは以下

* then
* else
* or
* do
* fi
* done


### 3. 1つ目のトークンを確認

1つ目のトークンがエイリアスの場合展開する。


### 4. {}展開

`{}` を展開する。

例: `a{b,c}` → `ab ac`


### 5. チルダ展開

`~user` のような `~` を展開する。

例: `~` → `/home`


### 6. パラメータ展開

変数を展開する。

例: `${FILES}` → `file1 file2`


### 7. コマンド置換

`$(command)` や `command` を展開する。

例: \`pwd\` → `/home/user`


### 8. 算術置換

`$((expression))` を展開する。

例: `$((1+3))` → `4`


### 9. ワードの抽出

`$IFS` の文字を使用してワードに分解する。


### 10. パス名展開

`\*`, `?`, `[` & `]` の組に対し、パス名展開またはワイルドカード展開する。

例: `ls /usr/\*` → `/usr/bin /usr/local`


### 11. コマンド検索

1つ目のワードを以下のいずれかと見なし、コマンドを特定する。

* 関数
* 組み込みコマンド
* `$PATH` 環境変数のいずれかのディレクトリにあるファイル

例: `ls /usr` → `ls` を `/usr/bin/ls` と認識


### 12. コマンド実行

入出力リダイレクトなどを設定した後、コマンドを実行する。  
evalがある場合は1に戻る。


### 具体的な実行例

以下の前提の元、各フローで実施される処理を記述する。

* `alias ll="ls -l"` が設定されている
* ユーザaliceのホームディレクトリ `/home/alice` に `.hist537` というファイルが存在する
* `$$` の値が `2537` である
* コマンドは `ll $(type -path cc) ~alice/.*$(($$%1000))` である

1. 1で 入力を `ll`, `$(type -path cc)`, `~alice/.*$(($$%1000))` の3ワードに分解する
2. 2で `ll` はキーワードではないため3へ
3. 3で `ll` は `ls -l` のエイリアスなので、分解して1へ
4. 1で 入力を `ls`, `-l`, `$(type -path cc)`, `~alice/.*$(($$%1000))` の4ワードに分解する
5. 2で `ls` はキーワードではないため3へ
6. 3で `ls` はエイリアスではないため4へ
7. 4で `ls -l $(type -path cc) ~alice/.*$(($$%1000))` は `{}` を含まないので5へ
8. 5で `ls -l $(type -path cc) /home/alice/.*$(($$%1000))` とチルダ展開して6へ
9. 6で `ls -l $(type -path cc) /home/alice/.*$((2537%1000))` とパラメータ展開して7へ
10. 7で `ls -l /usr/bin/cc /home/alice/.*$((2537%1000))` とコマンド展開して8へ
11. 8で `ls -l /usr/bin/cc /home/alice/.*537` と算術展開して9へ
12. 9で `ls -l /usr/bin/cc /home/alice/.*537` はワード展開が不要のため10へ
13. 10で `ls -l /usr/bin/cc /home/alice/.hist537` とパス名展開して11へ
14. 11で `ls` が `/usr/bin/ls` のコマンドであると検索され12へ
15. 12で `/usr/bin/ls` が `-l` オプション かつ 引数 `/usr/bin/cc` `/home/alice/.hist537` として実行される
16. 12の実行にはevalが存在しないため終了



文字列演算子構文
----------------

変数で使用する演算子の構文一覧

### `${variable:-word}`

変数が未定義の場合にデフォルト値を返す。

* varialbeが存在し、かつnullでない場合に、その値を返す
* それ以外の場合は、wordを返す。

`${count:-0}` は `count` が未定義であれば `0` と評価される。

### `${variable:=word}`

変数が未定義の場合にデフォルト値を設定する。

* variableが存在し、かつnullでない場合に、その値を返す。
* それ以外の場合は、variableにwordを設定して返すが、位置パラメータや特殊なパラメータをこの方法で代入することはできない

`${count:=0}` は `count` が未定義であれば `0` を設定する。

### `${variable:?message}`

変数が未定義の場合に発生するエラーを補足する。

* varialbeが存在し、かつnullでない場合に、その値を返す
* それ以外の場合は、variable:に続いてmessageを出力し、(対話型のシェルでは無い場合にのみ)現在のコマンドあるいはスクリプトを中止する
* messageを省略すると、デフォルトで「parameter null or not set」が出力される

`${count:?"undefined!"}` は `count` が未定義であれば `count: undefined!` を出力して終了する。

### `${variable:+word}`

変数の存在を評価する。

* varialbeが存在し、かつnullでない場合に、wordを返す
* それ以外の場合は、nullを返す

`${count:+1}` は `count` が未定義であれば `1` (「真」を意味する) を返す。

### `${variable:offset:length}`

文字列の一部を返す (部分文字列またはスライスと言う)

* 部分文字列を展開する。
* `$variable` の値から、offsetの位置からlength文字の長さの部分文字列を取り出す
* 文字の位置は0から数える。
* lengthを省略すると、offsetの位置から `$variable` の終わりまでの部分文字列が返される。
* offsetが0未満の場合は `$variable` の末尾から位置が数えられる。
* variableが `@` の場合、lengthはoffsetを先頭とする位置パラメータの番号となる

`count` が `frogfootman` と設定されている場合 `${count:4}` は `footman` を返し `${count:4:4}` は `foot` を返す。


パターンとパターン照合
----------------------

変数から特定パターンを抽出する一覧

### `${variable#pattern}`

variableの値の始めの部分とpatternが一致した場合、最も短く一致した部分を削除し、残りの部分を返す

### `${variable##pattern}`

variableの値の始めの部分とpatternが一致した場合、最も長く一致した部分を削除し、残りの部分を返す

### `${variable%pattern}`

variableの値の終わりの部分とpatternが一致した場合、最も短く一致した部分を削除し、残りの部分を返す

### `${variable%%pattern}`

variableの値の終わりの部分とpatternが一致した場合、最も長く一致した部分を削除し、残りの部分を返す

### `${variable/pattern/string}`

variableの値でpatternと最も長く一致した部分をstringと置換する。

* 最初に一致した部分だけが置換される
* patternが `#` で始まる場合は、variableの始めの部分と一致しなければならない
* stringがnullの場合は、一致した部分が削除される
* variableが `@` または `*` の場合には、位置パラメータが順番に処理され、展開結果がそのリストとなる

### `${variable//pattern/string}`

variableの値でpatternと最も長く一致した部分をstringと置換する。

* 一致する部分は全て置換される
* patternが `#` で始まる場合は、variableの始めの部分と一致しなければならない
* stringがnullの場合は、一致した部分が削除される
* variableが `@` または `*` の場合には、位置パラメータが順番に処理され、展開結果がそのリストとなる


入出力リダイレクタ
------------------

入出力リダイレクタの一覧

|    記述例          |     意味                                                                     |
|--------------------|------------------------------------------------------------------------------|
|    `cmd1 | cmd2`   | パイプ(cmd1の標準出力をcmd2の標準入力にする)                                 |
|    `> file`        | 標準出力をfileに切り替える                                                   |
|    `< file`        | 標準入力をfileに切り替える                                                   |
|    `>> file`       | 標準出力をfileに切り替える (fileが既に存在する場合は追加する)                |
|    `>| file`       | 標準出力をfileへ強制する (noclobberの設定を無視する)                         |
|    `n>| file`      | ファイルディスクリプタnの出力をfielへ強制する (noclobberの設定を無視する)    |
|    `<> file`       | fileを標準入力および標準出力として使用する                                   |
|    `n<> file`      | ファイルディスクリプタnの標準入力および標準出力としてfileを使用する          |
|    `<< label`      | ヒアドキュメント                                                             |
|    `n> file`       | ファイルディスクリプタnをfileに切り替える                                    |
|    `n< file`       | ファイルディスクリプタnとしてfileを設定する                                  |
|    `n>> file`      | ファイルディスクリプタnをfileに切り替える (fileが既に存在する場合は追加する) |
|    `n>&`           | 標準出力をファイルディスクリプタnに複製する                                  |
|    `n<&`           | 標準入力をファイルディスクリプタnから複製する                                |
|    `n>&m`          | ファイルディスクリプタnを出力ファイルディスクリプタのコピーにする            |
|    `n<&m`          | ファイルディスクリプタnを入力ファイルディスクリプタのコピーにする            |
|    `&> file`       | 標準出力および標準エラーをfileに切り替える                                   |
|    `<&-`           | 標準入力を停止する                                                           |
|    `>&-`           | 標準出力を停止する                                                           |
|    `n>&-`          | ファイルディスクリプタnからの出力を停止する                                  |
|    `n<&-`          | ファイルディスクリプタnからの入力を停止する                                  |

