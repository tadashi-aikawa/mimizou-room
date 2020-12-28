# [ts-node] FAQ


`tsconfig.json`が反映されない
-----------------------------

`--files`フラグを付けないといけない.

```console
npx ts-node --files main.ts
```

環境変数`TS_NODE_FILES=true`を指定してもOK.

