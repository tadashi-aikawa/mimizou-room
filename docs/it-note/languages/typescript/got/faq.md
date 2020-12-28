# [got] FAQ

### ステータスコード2xx以外の結果がErrorとしてcatchされてしまう

`throwHttpErrors: false`を指定します。

```typescript
got.put(url, { responseType: 'json', throwHttpErrors: false })
```

{{refer("https://github.com/sindresorhus/got#throwhttperrors")}}

