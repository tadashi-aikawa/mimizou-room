# [Jenkins] Snippets

主に以下を参照。

{{link("https://jenkins.io/doc/book/pipeline/jenkinsfile/")}}

{{link("https://jenkins.io/doc/book/pipeline/syntax/")}}


よく使うコマンド
----------------

### トリガー (定期実行など)

```groovy
pipeline {
    triggers {
        cron('H */4 * * 1-5')
    }
```

{{refer("https://jenkins.io/doc/book/pipeline/syntax/#triggers")}}


### パラメータ

```groovy
pipeline {
    agent any
    parameters {
        string(name: 'Greeting', defaultValue: 'Hello', description: 'How should I greet the world?')
    }
    stages {
        stage('Example') {
            steps {
                echo "${params.Greeting} World!"
            }
```

!!! warning
    shの内部で呼び出す時は `${params.Greeting}` ではなく `${Greeting}` なので注意

{{refer("https://jenkins.io/doc/book/pipeline/jenkinsfile/#handling-parameters")}}


独自関数
--------

### Slack通知

```groovy
def sendToSlack(channel, username, icon_emoji, color, text) {
        sh "curl -s -S -X POST --data-urlencode 'payload={\"link_names\": 1, \"channel\": \"$channel\", \"username\": \"$username\", \"icon_emoji\": \":$icon_emoji:\", \"attachments\": [{\"color\": \"$color\", \"text\": \"$text\"}]}' $SLACK_INCOMING_WEBHOOKS_URL"
}
```

