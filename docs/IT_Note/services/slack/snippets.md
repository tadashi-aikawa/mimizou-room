# [Slack] Top


Message Format
--------------

### URLリンク埋め込み

```text
<https://example.com|Overlook Hotel>
```


お気軽Webhook通知
-----------------

### bash

成功/失敗をアタッチメント込みで送る場合

```bash
post_slack() {
  local channel=$1
  local user=$2
  local emoji=$3
  local message=$4
  # good / danger
  local color=$5
  curl -X POST --data-urlencode 'payload={"link_names": 1, "channel": "'"${channel}"'", "username": "'"${user}"'", "icon_emoji": "'":${emoji}:"'", "attachments": [{"color": "'"${color}"'", "text": "'"${message}"'"}]}' ${SLACK_WEBHOOK_URL}
}
```
