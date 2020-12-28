# [Axios] FAQ

### Shift-Jisのデータを扱うことができない

`responseType: arraybuffer`を指定して`ArrayBuffer`で結果を受け取る。

```ts
  const sjisStr: ArrayBuffer = await Axios.get("http://localhost:8080/sjis.txt", {
    responseType: "arraybuffer",
  })
    .then((x) => x.data)
```

これを`Buffer.from(arrayBuffer)`で`Buffer`に変換し、`iconv`などのライブラリでdecodeする。

{{refer("https://blog.sakaki333.com/ui/post/detail/29")}}
