# [jq] Snippets


リストに使うコマンド
--------------------

`items`という配列がある想定で進める。

### slice

indexに`begin:end`のような設定

```bash
jq '.items | .[3:5]'
```

### map

idとnameだけを表示

```bash
jq '.items | map({id, name})'
```

`.items[] | {id. name}`という表現だと外側の配列が除外されてしまう。  
一覧で表示する場合はその方がいいかも。

```bash
jq '.items[] | {id, name}'
```

### filter

idが`mzb`のアイテムだけを表示

```bash
jq '.items[] | select(.id == "mzb")'
```

### sort

idでソートする

```bash
jq '.items | sort_by(.id)'
```

降順は`reverse`で表現

```bash
jq '.items | sort_by(.id) | reverse'
```

### uniq

`unique_by`を使う。`uniq`ではないので注意

```bash
jq '.items | uniq_by(.season)'
```

### group_by

ObjectではなくArrayになる。

```bash
jq '.items | group_by(.season)'
```

### CSV/TSVに変換

```bash
jq -r '.items[] | [.id, .name] | @csv'
jq -r '.items[] | [.id, .name] | @tsv'
```
