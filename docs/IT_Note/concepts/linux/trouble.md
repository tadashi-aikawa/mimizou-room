# [Linux] FAQ


タイムゾーンを変更したい
------------------------

### Ubuntu18

[timezonectl](../snippets/#timezonectl)を使う。

### Dockerコンテナの場合

ホストと同じでよければ`localtime`をvolumeで読みこみ専用マウントする。

```yaml
  volumes:
    - /etc/localtime:/etc/localtime:ro
```
