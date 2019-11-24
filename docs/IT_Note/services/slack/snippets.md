# [Slack] Snippets


お気軽Webhook通知
-----------------

### bash

成功/失敗をアタッチメント込みで送る場合.

git-bash(Windows)でも動く。

```bash
post_slack() {
  # ex: "#times_hoge"
  local channel=$1
  # ex: "hoge"
  local user=$2
  # ex: "smile"
  local emoji=$3
  # ex: "ほげほげ"
  local message=$4
  # list: good / danger
  local color=$5

  file=$(mktemp)
  trap "rm ${file}" EXIT

  cat << EOJ > $file
    {
      "link_names": 1,
      "channel": "${channel}",
      "username": "${user}",
      "icon_emoji": ":${emoji}:",
      "attachments": [
        {
          "color": "${color}",
          "text": "${message}"
        }
      ]
    }
EOJ

  curl -s -S -X POST -d @$file ${SLACK_WEBHOOK_URL}
}
```

* `-d`指定でjsonの改行を認識しないように
* 一時ファイルを使うことでgit-bashの場合に`--url-encode`が`UTF-8`にならない問題を回避
* `trap`で一時ファイルが残らないように
