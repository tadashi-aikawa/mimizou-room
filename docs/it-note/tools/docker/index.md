---
description: Docker
---

# [Docker] Top

{{ page.meta.description }}


インストール
------------

### Ubuntu on WSL2

{{link("https://docs.docker.com/engine/install/ubuntu/")}}

```bash
# 不要なものを消す
$ sudo apt-get remove docker docker-engine docker.io containerd runc

# インストール作業に必要な依存関係の構築
$ sudo apt-get update
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

# リポジトリの準備
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

# Docker一式をインストール
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```

```bash
# サービス起動
$ sudo service docker start
   * Starting Docker: docker

# 確認
$ sudo docker run hello-world
```

```bash
# root以外のユーザで使えるようにする
$ sudo usermod -aG docker <your-name>
# systemdを使っていないWSLの場合限定
$ sudo cgroupfs-mount

# 再起動 + ログアウト
$ sudo service docker restart
$ logout
```

次回ログイン後は使えるようになっている。



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
