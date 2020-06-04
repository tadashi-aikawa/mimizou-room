# [Make] Snippets


お決まりのやつ
--------------

### Linux

```
MAKEFLAGS += --warn-undefined-variables
SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
```

### Windows

```
MAKEFLAGS += --warn-undefined-variables
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
```


ガード
------

変数が定義されていない場合、処理開始前に終了する書き方。

### bash版

```
.SHELLFLAGS := -eu -o pipefail -c

guard-%:
	@ if [ "${${*}}" = "" ]; then \
		echo "[ERROR] Required: $* !!"; \
		echo "[ERROR] Please set --> $*"; \
		exit 1; \
	fi
```

### PowerShell版

```
.SHELLFLAGS := -eu -o pipefail -c

guard-%:
	powershell if ( '$($*)' -eq '' ) {\
		echo '[ERROR] $* is required!!';\
		exit 1;\
	}
```

### 使い方

`version`を指定しない場合エラーにするなら。

```
release: guard-version
	@echo Start $@
```


ブラウザでURLを開く
----------------------

`Windowsの場合`

```
"C:\Program Files\Git\bin\bash" -c 'start ${URL}'
```
