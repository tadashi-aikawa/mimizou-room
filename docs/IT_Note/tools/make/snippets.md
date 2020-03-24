# [Make] Snippets


ガード
------

変数が定義されていない場合、処理開始前に終了する書き方。

```
guard-%:
	@ if [ "${${*}}" = "" ]; then \
		echo "[ERROR] Required: $* !!"; \
		echo "[ERROR] Please set --> $*"; \
		exit 1; \
	fi
```

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
