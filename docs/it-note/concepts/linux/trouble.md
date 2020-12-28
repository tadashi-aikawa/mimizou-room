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


差集合を求めたい
----------------

`a.txt`から`b.txt`の内容を引いた結果を取得したい場合のコマンド.

```
sort a.txt b.txt b.txt | uniq -u
```

`uniq -u`は2回以上出現するものを削除するのでうまくいく.

* `a.txt`だけにしか出現しないものは1回なので残る
* `a.txt`と`b.txt`の両方に出現するものは必ず2回出力されるので全て消える
* `b.txt`は必ず2回出力されるので全て消える

