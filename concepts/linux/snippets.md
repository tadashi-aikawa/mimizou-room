Linuxコマンド
-------------

### awk

```bash
# 10行おきに取り出す
$ awk 'NR%10==0'
# 区切り文字を指定して表示
$ awk -F: '{print $2}'
# 行ごとに出現文字列の回数を表示
$ akw '{print gsub(/${word}/, "")}'
# 1つ目の要素がwordと一致するもののみ表示
$ awk '$1 == "word"'
# 2つ目の要素にhogeを含むもののみ表示
$ awk '$2 ~ "hoge"'
# 空白区切りの文字列に対し、1つ目と3つ目の要素を「/」で連結して出力する
$ awk '{print $1 "/" $3}'
# 区切りの文字列に対し、1つ目と3つ目の要素を「/」で連結して出力する
$ awk -F":" '{print $1 "/" $3}'
# 改行区切りの数値に対し、値が100より大きいものを出力する
$ awk '$0 > 100 {print $0}'
# 改行区切りの数値に対し、値が100より大きいものの数を出力する
$ awk 'BEGIN{x = 0} $0 > 100 {x += 1} END {print x}'ai
# バッファしない
$ awk '{print $1; fflush()}'
# 空白区切りの数字に対し、平均値を出力する
$ awk '{sum += $1} END{print sum / NR}'
# 空白区切りの数字に対し、1000で割った値を出力する
$ awk '{print $0 / 1000}'
# カンマで区切られたフィールドを2つ持つファイルに対し、1つ目の値をキーとして各キーの最大値を出力
$ awk -F',' '{ if($0 != "" && a[$1] < $2) { a[$1]=$2; } }END{for(i in a)print i","a[i];}'
```

### basename

```bash
# パスからエントリ名のみを抜き出す (/dir/file.txt -> file.txt)
$ basename ${path}
```

### bc

```bash
# 電卓起動
$ bc
# 電卓を起動せず計算
$ bc <<< 10+20
30
```

### cat

```bash
# ファイルの内容を行番号と共に出力
$ cat -n ${file}
# 改行コードを表示 (LFは$, CRは^M)
$ cat -e ${file}
```

### chkconfig

CentOS7では `systemctl` を使用しましょう。

```bash
# 起動オプションを表示する
$ chkconfig --list
# 任意のミドルウェアの起動オプションを表示する
$ chkconfig --list ${middleware_name}
# 任意のミドルウェアを自動起動にする
$ chkconfig ${middleware_name} on
```

### chown

```bash
# 所有者を変更する
$ chwon ${user} ${entry}
# 所有者とグループを変更する
$ chwon ${user}:${group} ${entry}
# 再帰的に所有者を変更する
$ chown -R ${user} ${entry}
```

### cp

```bash
# ディレクトリコピー
$ cp -r ${exist} ${new}
# 上書き確認をしてコピー
$ cp -i ${exist} ${new}
# 上書き確認せずコピー
$ cp -f ${exist} ${new}
# ファイル情報(タイムスタンプ、パーミッション etc)を保持してコピー
$ cp -p ${exist} ${new}
# ${new}のバックアップ${new}~を作成してからコピー
$ cp -b ${exist_file} ${new_file}
# ${new_file} -> ${exist_file}となるシンボリックリンクを作成する
$ cp -s ${exist_file} ${new_file}
```

### crontab

```bash
# crontabファイルの内容を表示
$ crontab -l
# crontabファイルを編集する
$ crontab -e
```

### cut

```bash
# 2～4文字目の文字列のみ抽出
$ cut -c2-4 ${file}
# 空白文字区切りで左から2番目の文字列のみを表示
$ cut -d " " -f 2 ${file}
# 空白文字区切りで左から1,3番目の文字列のみを表示
$ cut -d " " -f 1,3 ${file}
# 空白文字区切りで左から2-3番目の文字列のみを表示
$ cut -d " " -f 2-3 ${file}
# 空白文字区切りで左から2番目の文字列のみを表示、ただしデミリタ(区切り文字)の無い行は表示しない
$ cut -ds " " -f 2 ${file}
```

### curl

```bash
# メータを表示しない
$ curl -s ${url}
# urlにアクセスした結果を保存
$ curl -O ${url}
# urlにアクセスした結果をoutputに保存
$ curl -o ${output} ${url}
# データをPOST (改行は削除)
$ curl ${url} -X POST -d @{file}
# データをPOST (改行は削除しない)
$ curl ${url} -X POST --data-binary @{file}
# ヘッダを付ける
$ curl ${url} -H "Content-Type: text/csv;charset=UTF-8" -d @{file}
# 標準出力をPOST
$ ... | curl ${url} -X POST -d @-
# ステータスコードを取得する
$ curl -s ${URL} -o /dev/null -w %{http_code}
# レスポンスヘッダを表示する
$ curl -i ${URL}
$ curl -i -D - ${URL}
```

https://access.redhat.com/site/documentation/ja-JP/Red_Hat_Enterprise_Virtualization/3.0/html/REST_API_Guide/appe-REST_API_Guide-cURL_Integration.html

### date

```bash
# 1日前をyyyyMMddで表示する
$ date --date '1 days ago' +%Y%m%d
# 標準入力の文字列を時刻フォーマットする
$ echo '2014/07/05 16:19:22' | date +%Y%m%d -f -
```

### declare

```bash
# 関数定義一覧を表示する
$ declare -f
```

### df

```bash
# ディスク容量概要を調べる
$ df -h
```

### diff

```bash
# 再帰的に差分確認
$ diff -r ${old} ${new}
# unified diff形式で出力
$ diff -u ${old} ${new}
# ファイルの差分有無のみを表示する
$ diff -q ${old} ${new}
# 末尾の空白を無視する
$ diff -b ${old} ${new}
# 空白を無視する
$ diff -w ${old} ${new}
# side-by-side形式で出力
$ diff -y ${old} ${new}
# side-by-sideで差分がある場合のみ右側に出力
$ diff -y --left-column ${old} ${new}
# side-by-sideで差分がある行のみ出力
$ diff -y --suppress-common-lines ${old} ${new}
# 条件に部分一致する行を差分対象外
$ diff -I ${regex} ${old} ${new}
# ファイル差分を分かりやすく表示する
$ diff -aur ${old} ${new} | vi -R -
# コマンド通しでdiffをとる
$ diff -aur <(${command1}) <(${command2})
```

### dig

```bash
# ドメイン名 → IPアドレス (正引き)
$ dig ${domain}
# IPアドレス → ドメイン名 (逆引き)
$ dig -x ${ip}
```

### dirname

```bash
# パスからディレクトリを抜き出す (/dir1/dir2/hoge -> dir1/dir2)
$ dirname /dir1/dir2/hoge
# (shファイルに記述したとき)実行ディレクトリを抜き出す
$ dirname $0
```

### du

```bash
# ディレクトリ容量確認
$ du -sh
# バイト表示
$ du -b
# 最終行にTotalを表示
$ du -c
```

### echo

```bash
# エスケープを有効にして表示する
$ echo -e "a\nb"
# 行の最後に改行を含めず表示する
$ echo -n "a"
```

### find
`※ ワイルドカードの指定は必ず「''」で囲みましょう`

```bash
# カレントディレクトリ以下でシンボリックを検索
$ find ./ -type l
# カレントディレクトリ以下でエントリ名に「test」が含まれるものを検索
$ find ./ -name '*test*'
# カレントディレクトリ以下でエントリ名が「test1, test2, ... test5」であるものを検索
$ find ./ -name 'test[1-5]'
# カレントディレクトリ以下でエントリ名が「test?」であるもの、ただし「test2」は除く
# ?は任意の1文字
$ find ./ -name '*test[!2]'
# カレントディレクトリ以下をツリー表示
$ find ${dir} | sort | sed -ne 's/[^\/]*\//+--/g;s/+--+/|  +/g;s/+--+/|  +/g;s/+--|/|  |/g;p'
# カレントディレクトリ以下をAでgrep
$ find ./ type f -print | xargs grep A /dev/null
# 最近3日以内に更新されたファイルを検索
$ find . -mtime -3
# 更新から3日以上経っており、warを含むファイル
$ find . -mtime +3 -name '*war*'
# 更新から3日以上経っている、もしくはwarを含むファイル
$ find . -mtime +3 -or -name '*war*'
# 最近更新された順にディレクトリ配下のファイルを表示
$ find . -type f -print0 | xargs -0 ls -alt
```

### finger

```bash
# ユーザの個人情報を表示する
$ finger
```

### firewall-cmd

CentOS7のファイアウォール

```bash
# 現在のゾーンを表示
$ firewall-cmd --list-all
```

`/etc/firewalld/zones/public.xml`を修正して `systemctl restart firewalld`で設定変更

serviceとportの関係は↓(sshの例)を見れば分かる。
/usr/lib/firewalld/services/ssh.xml


### for

```bash
# ディレクトリに含まれるファイルを全て表示する
$ for s in *; do echo ${s}; done
```

### grep

```bash
# 再帰検索
$ grep -r ${keyword} ${file}
# 大文字小文字を無視
$ grep -i ${keyword} ${file}
# 指定文字を含まない行のみ
$ grep -v ${keyword} ${file}
# 正規表現で検索
$ grep -E ${keyword} ${file}
# 対象の表現のみを表示
$ grep -oE ${keyword} ${file}
# 結果を表示しない(戻り値だけを知りたいとき)
$ grep -q ${keyword}
# ファイル名だけ表示
$ grep -l ${keyword} ${file}
# エスケープを一切せず検索
$ grep -F ${keyword} ${file}
# ヒットした箇所の前後1行を表示
$ grep -1 ${keyword} ${file}
# ヒットした箇所の行数を表示
$ grep -n ${keyword} ${file}
# 指定キーワードの出現箇所を改行して表示
$ grep -o ${keyword} ${file}
# バッファしない
$ grep --line-buffered ${keyword}
```

### groupadd

```bash
# グループを追加する
$ groupadd ${group}
```

### gzip

```bash
# .gzファイルに圧縮する
$ gzip ${file}
# .gzを解凍して圧縮ファイルは削除
$ gzip -d ${file}
# .gzを解凍して圧縮ファイルは削除しない
$ gzip -cd ${file}
```

### hexdump

```bash
# バイナリファイルを表示する
$ hexdump -C ${binary}
```

### hostname

```bash
# ホスト名を表示する
$ hostname
# ホストのIPアドレスを表示する
$ hostname -i
$ vi /sbin/ifconfig
# ホストのエイリアス名を表示する
$ hostname -a
```

### id

```bash
# ユーザID情報を表示する
$ id ${user_name}
```

### ifconfig

```bash
# ネットワーク環境の設定確認
$ ifconfig
```

### jobs

```bash
# バックグランドで実行していたジョブの状態を確認する (終了している場合1度しか表示されない)
$ jobs
```

### join

```bash
# 2ファイルの1つ目のフィールドをキーとしてInner Joinする
$ join -j1 ${file1} ${file2}
# 2ファイルの1つ目のフィールドをキーとしてOuter Joinする
$ join -a 2 -j1 ${file1} ${file2}
```

### kill

```bash
# プロセス番号を指定してTerminateする
$ kill ${process_no}
# ジョブ番号を指定してTerminateする
$ kill %${job_no}
# ジョブをQuitする (Terminateがきかない場合のみ利用)
$ kill -QUIT ${process_no}
# ジョブをKillする (QUITがきかない場合のみ利用)
$ kill -KILL ${process_no}
```

### less

```bash
# 行番号を表示する
$ less -N ${file}
# ANSI colorを適応させる
$ less -R ${file}
# 折り返さずに表示する
$ less -S ${file}
```

### ln

```bash
# ${target} -> ${file} とシンボリックリンクを張る
$ ln -s ${file} ${target}
# ${target} -> ${file} とシンボリックリンクを上書きする
$ ln -sfn ${file} ${target}
```

### ls

```bash
# エントリの最終参照日時を表示する
$ ls -u ${entry}
# ディレクトリの情報を表示する
$ ls -d ${entry}
```

### lscpu

```bash
# CPUの性能を表示
$ lscpu
```

### mpstat

```bash
# 現在のCPU使用状況を表示
$ mpstat
```

### nkf

```bash
# テキストファイルの文字コードを調べる
$ nkf --guess ${file}
# 文字コードの半角 → 全角変換をしない(デフォルトはする)
$ nkf -x ${file}
# 文字コードUTF-8に変更 (EUC-JPは -e, Shift_JISは -s)
$ nkf -w --overwrite ${file}
# 改行コードLFに変更 (CRLFは -Lw)
$ nkf -Lu --overwrite ${file}
# URLデコードする(自動判定)
$ nkf --url-input ${input}
# URLデコードする(指定)
$ nkf --url-input -${FROM} ${to} ${input}
 → ${FROM}と${to}はそれぞれ大文字、小文字で
    (W:utf8, S:shift-jis, E:euc-jp)が入る
# バッファリングせずURLデコードする
$ nkf -u --url-input ${input}
```

### nl

```bash
# ファイルの内容を行番号と共に出力
$ nl ${file}
```

### nohup

```bash
# nohup以外にファイルを出力する
$ nohup ${command} &> ${output} &
```

### od

```bash
# 行ごとの改行コードを確認
$ od -c ${file}
```

### passwd

```bash
# パスワードを変更する
$ passwd ${user_name}
```

### pgrep

```bash
# プロセス名を含むプロセスIDを取得する
pgrep -f ${process_name}
```

### pkill

```bash
# プロセス名を含むプロセスをkillする
pkill -f ${process_name}
```

### printf

```bash
# フォーマットを指定して文字列を出力
$ printf 'I live in %s from %d-year-old.\n' Tokyo 20
I live in Tokyo from 20-year-old.
$ printf '|%10s|%-10s|\n' 12 123456789
|        12|123456789 |
$ printf '|%010d|\n' 12345
|0000012345|
```

### ps

```bash
# プロセスの開始時間を表示
$ ps -eo lstart,cmd
# 特定プロセスだけ表示
$ ps -C ${process}
# 全ユーザのプロセス情報を表示
$ ps a
# プロセス実行ユーザ名と開始時刻も表示
$ ps u
# 制御端末を持たないプロセスも表示 (デーモンなど)
$ ps x
# プロセスの親子関係が分かるように表示
$ ps f
```

### pstree

```bash
# プロセスツリーを表示する
$ pstree
# PIDを指定してプロセスツリーを表示する
$ pstree ${PID}
# PID付でプロセスツリーを表示する
$ pstree -p
# ユーザ付でプロセスツリーを表示する (親プロセスと同じ場合は省略される)
$ pstree -u
```

### rename

```bash
# ${from}を${to}に置換してリネームする
$ rename ${from} ${to} ${files}
```

### route

```bash
# ルーティング設定を表示
$ route
```

### rpm

```bash
# パッケージ ${package_name}内のファイル一覧を表示する
$ rpm -ql ${package_name}
```

### rm

```bash
# -から始まるファイル(-e)を削除
$ rm -- -e
```

### rsync

```bash
# fromディレクトリ配下のエントリを toディレクトリ配下に同期する (hostにuserでアクセス)
$ rsync -av --delete ${from}/ ${user}@${host}:${to}/
# 上記から.htaccessを除外する
$ rsync -av --delete --exclude=.htaccess ${from}/ ${user}@${host}:${to}/
```

### sar

```bash
# ロードアベレージを表示する
$ sar -q
# ロードアベレージを1秒おきに10回表示する
$ sar -q 1 10
# 1分間の最新ロードアベレージを表示する
$ sar -q 1 | tail -2 | head -1 | awk '{print $5}'
# 19:00:00～19:30:00の情報を表示する
$ sar -s 19:00:00 -e 19:30:00
```

### sendmail

```bash
# メールを送る
$ sendmail to@example.com << EOF
From: from@example.com
To: to@example.com
Subject: Test

これはテストです
.
EOF
```

### scp

```bash
# データを転送する
$ scp -pr ${entry} ${user_name}@${host}:${dst}
# ポートを指定してデータを転送する
$ scp -P ${port} ${entry} ${user_name}@${host}:${dst}
# ポートを指定してデータを取得する
$ scp -P ${port} ${user_name}@${host}:${entry} ${dst}
```

### sdiff

```bash
# side-by-side形式で出力
$ sdiff ${old} ${new}
# 空白数の違いを無視する
$ sdiff -b ${old} ${new}
# 空白を無視する
$ sdiff -W ${old} ${new}
# 品質を重視する
$ sdiff -d ${old} ${new}
# 速度を重視する
$ sdiff -H ${old} ${new}
# 差分がある行のみ出力
$ sdiff -s ${old} ${new}
# 差分が無い行は右側に出力しない
$ sdiff -l ${old} ${new}
```

### sed

https://hydrocul.github.io/wiki/commands/sed.html

```bash
# バッファしない
$ sed -u 's/hoge/hoga/g'
# 正規表現を利用する (括弧、ダブルコーテーションもエスケープ不要)
$ sed -r 's/.+GET ([^ ]).+/\1/g'
# 条件の一致に関わらず出力しない
$ sed -n 's/hoge/hoga/g'
# 条件に一致したもののみ出力する
$ sed -n 's/hoge/hoga/gp'
# 50~60行目を表示
$ sed -n '50,60p' ${file}
# 上書き置換する
$ sed -i 's/hoge/hoga/g'
# パターンの前後に文字をくっつける
$ sed -i 's/hoge/--&--/g'
# 改行コードを置換する
$ sed -rz 's/\n/hoge/g'
```

### seq

```bash
# 1～10を出力する
$ seq 1 10
# 1～10をフォーマットして出力する ( -> No.1, No.2, ... ,No.10)
$ seq -f 'No.%g' 1 10
```

### service

```bash
# 起動中のデーモンを確認する
$ service ${service} status
```

### sort

```bash
# 空白区切りの2要素目をキーとしてソート
$ sort -t ' ' -k2 ${file}
# キーを数字としてソート(11と2を昇順ソートすると、2が先頭になる)
$ sort -n ${file}
# 重複表示しない
$ sort -u ${file}
```

### ssh

```bash
# 多段sshログインする
$ ssh ${host1} -t ssh ${host2}
# 複数行コマンドをSSH経由で実行する
$ ssh -T ${host} << EOF
# Command... #
EOF
```

### ssh-keygen

```bash
# ssh keyを作成する (RSA 4096bit)
$ ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa_${identify} -C "Access to rts001d"
```

### ssh-copy-id

```bash
# 鍵交換を行う
$ ssh-copy-id -i ~/.ssh/id_rsa_${identify}.pub ${user_name}@${host}
```

### su

```bash
# 特定ユーザでコマンドを実行する
$ su -l ${user} -c ${command}
```

### systemctl

CentOS7から使用可能です。

```bash
# サービスを起動する
$ systemctl start ${service}
# サービスを終了する
$ systemctl stop ${service}
# サービスを再起動する
$ systemctl restart ${service}
# サービスを設定反映する
$ systemctl reload ${service}
# サービスの状態を取得する
$ systemctl status ${service}
# サービスの自動起動をONにする
$ systemctl enable ${service}
# サービスの自動起動をOFFにする
$ systemctl disable ${service}
# サービスの自動起動状態を確認する
$ systemctl is-enabled ${service}
```

Ubuntuで使うもの

```bash
# DNSサーバ変えた時の再起動
$ systemctl restart systemd-resolved
```

### tar

**絶対パスで圧縮/解凍されるので注意**

```bash
# zzipでアーカイブする
$ tar -czvf ${archive} ${entry}
# zzipアーカイブを解凍する
$ tar -xzvf ${archive}
# 特定のディレクトリ配下に構成を解凍する
$ tar -xzvf ${archive} -C ${dst}
```

### tee

```bash
# 標準出力に加え、ファイルに追記する
$ tee -a ${file}
```

### top

```bash
# 現在のシステム状況を表示
$ top
# 現在のシステム状況を表示 1秒更新
$ top -d 1
# COMMANDをフル表示する
$ top -c
# batchモードで出力する
$ top -b
# 特定ユーザのプロセスだけを出力する
$ top -u ${user}
```

topの並び替え

* CPU(P)
* メモリ(M)
* 実行時間(T)

topの切り替え

* グラフ表示(m)


### tr

```bash
# 1文字単位で置換する
$ tr ${before} ${after}
```

### type

```bash
# 指定文字列の定義一覧を出力する
$ type -a ${word}
```

### uname

```bash
# コンピュータの種類を出力する (i686で32bit, X86_64で64bit)
$ uname -m
```

### unset

```bash
# 関数定義を削除する
$ unset -f ${function}
```

### uptime

```bash
# 現在のロードアベレージを表示する
$ uptime
```

`cat /proc/loadavg` でも最新情報を取得可能。

### useradd

```bash
# ユーザを追加する
$ useradd ${user}
# ログインできないユーザを追加する
$ useradd -s /sbin/nologin ${user}
```

### usermod

```bash
# ログインできないユーザをログインできるようにする
$ usermod -s /bin/bash ${user}
# ユーザを2つのグループに登録する
$ usermod -G ${group},${group} ${user}
```

### wget

```bash
# 結果を標準出力に出力する
$ wget -O - ${URL}
# 結果を任意のファイル名で保存する
$ wget -O ${file} ${URL}
# 上書き保存する
$ wget -N ${URL}
```

### whereis

```bash
# モジュールのインストール場所を出力する
$ whereis ${module}
```

### who

```bash
# ログインユーザを確認する
$ who
# ログインユーザと、最後に端末操作してからの時間を確認する (コマンド実行してからの時間ではない)
$ who -u
# ログインユーザを項目付で確認する
$ who -H
```

### xargs

```bash
# カレントディレクトリのエントリ名を表示
$ ls | xargs -i{} echo {}
# 実行されるコマンド内容を表示(dry runではない)
$ xargs -t
# コマンド実行を対話で確認する
$ xargs -p
# プロセス数を指定する
$ xargs -P 2
# 区切り文字を@に指定
$ xargs -d@

# 改行をデリミタに変換する
$ xargs
# デリミタをnumごとに改行に変換する
$ xargs -n ${num}
```

### xmllint

```bash
# xmlを整形する
$ xmllint --format ${file}
# xmlを整形する (出力エンコーディング指定)
$ xmllint --encode ${encoding} --format ${file}
# xmlを整形する (入力エンコーディング指定)
$ nkf -w | xmllint --format -
```

### xrandr

```bash
# スクリーン情報の取得
$ xrandr
```

### yum

```bash
# インストール済みパッケージ一覧を表示する
$ yum list installed
# 条件に一致するパッケージ一覧を表示する
$ yum list ${package_name}
# ${word} を含むパッケージ一覧を表示する
$ yum list | grep ${word}
# ${word} を概要/パッケージ名に含むパッケージ一覧を表示する
$ yum search ${word}
# パッケージ詳細情報を表示する
$ yum info ${package_name}
# パッケージをインストールする
$ yum install ${package_name}
# 確認無しでパッケージをインストールする
$ yum -y install ${package_name}
# パッケージをアンインストールする
$ yum remove ${package_name}
# パッケージをアップデートする
$ yum update ${package_name}
# アップデートできるパッケージ一覧を表示する
$ yum check-update ${package_name}
```

### zip

```bash
# zip圧縮後に元ファイルを削除
$ zip -m ${zip} ${entry}
# 元ファイルの階層を無視してフラットに圧縮する
$ zip -j ${zip} ${entry}
```
