# [Make] Snippets


前提
----

シェルはbashを使用すること。  
WindowsならWSLかgit bashに含まれるMigGWにPathを通す。

```
%USERPROFILE%\scoop\apps\git\current\usr\bin
```


テンプレ
--------

とりあえず貼っとく用

```makefile
MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help

.PHONY: $(shell egrep -oh ^[a-zA-Z0-9][a-zA-Z0-9_-]+: $(MAKEFILE_LIST) | sed 's/://')

help: ## Print this help
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9][a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

guard-%:
	@ if [ "${${*}}" = "" ]; then \
		echo "[REQUIRED ERROR] \`$*\` is required."; \
		exit 1; \
	fi
```


詳細
----

### フラグ

```makefile
MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
```

### PHONY

`.PHONY`を自動生成する。

```makefile
.PHONY: $(shell egrep -oh ^[a-zA-Z0-9][a-zA-Z0-9_-]+: $(MAKEFILE_LIST) | sed 's/://')
```

### help

ヘルプメッセージを自動生成する。

```makefile
help: ## Print this help
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9][a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
```

### ブランチ名からバージョンを変数に代入

```makefile
version := $(shell git rev-parse --abbrev-ref HEAD)
```


### ガード

変数が定義されていない場合、処理開始前に終了する書き方。

```makefile
guard-%:
	@ if [ "${${*}}" = "" ]; then \
		echo "[REQUIRED ERROR] \`$*\` is required."; \
		exit 1; \
	fi
```

利用例。 `version`を指定しない場合エラーにするなら。

```makefile
release: guard-version
	@echo Start $@
```


### ブラウザでURLを開く

```makefile
start ${URL}
```
