# [Docker] Top


ツール
------

### docui

CLIでGUIっぽい操作ができる。

{{link("https://github.com/skanehira/docui")}}

#### バイナリ

インストール

```bash
version=2.0.0
wget https://github.com/skanehira/docui/releases/download/${version}/docui_${version}_Linux_x86_64.tar.gz
tar fxzv docui*.tar.gz
sudo mv docui /usr/local/bin/
```

#### Docker

エイリアスがオススメ

```bash
alias docui="docker run --rm -itv /var/run/docker.sock:/var/run/docker.sock skanehira/docui"
```
