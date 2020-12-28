# [Bash] Snippets


よく使うもの
------------

### シバン

```bash
#!/bin/bash
```

### スクリプトディレクトリの取得

```bash
SCRIPT_DIR=$(cd $(dirname $(readlink $0 || echo $0));pwd)
```

### 検査系

#### Utility

```bash
# Usageを表示して処理終了
function usage_exit() {
    echo "Usage: `basename $0` dierctory" 1>&2
    exit 1
}

# エラーメッセージを表示して処理終了
function error_exit() {
    echo "[ERROR] $1"
    exit 1
}

# コマンドが利用できるかの確認
function can_use() {
    type -p $1 || error_exit "Unable to find $1, please install it and run this script again"
}
```

#### 複雑名引数指定

```bash
while getopts g:c:s:v opt
do
    case $opt in
        g) GROUP=$OPTARG
            ;;
        s) SERVERS=$OPTARG
            ;;
        c) CMD=$OPTARG
            ;;
        v) VERBOSE=true
            ;;
        \?) usage_exit
            ;;
    esac
done

# 組み合わせによるバリデーション
[ -z $GROUP ] && [ -z "$SERVERS" ] && usage_exit
[ $GROUP ] && [ "$SERVERS" ] && usage_exit
[ -z "$CMD" ] && usage_exit
```


#### 引数が1つでない場合にNG

```
if [ $# -ne 1 ]; then
    usage_exit
fi
```
