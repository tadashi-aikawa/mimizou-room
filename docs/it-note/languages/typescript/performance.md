# [TypeScript] Performance


正確なパフォーマンス測定
------------------------

`performance.now()`で細かな精度の時間を取得できる。  
計測前と計測後に値をとって引き算した結果のミリ秒を見るのが一番単純。

`Date.now`は1ミリ秒の精度だが、`performance.now`は0.005ミリ秒の精度と高品質.

{{refer("https://sbfl.net/blog/2017/12/01/javascript-measure-time/")}}


### nodejsの場合

`perf_hooks`に`performance`があるのでそれを使う。

```ts
const pref = require('perf_hooks').performance;

const startTime = pref.now();

let sum = 0
for (let i = 0; i < 1000000; i++) {
    sum = sum + 1
}

const endTime = pref.now();
console.log(`100万回: ${Math.round(endTime - startTime)}ミリ秒`);
```

普通に`performance`ってやると問題あり

* `@types/node`があるとビルドでできるが、実際は`performance`がない
    * nodejsだと`perf_hooks.performance`だから
    * `lib.dom.d.ts`でperformanceが認識されてしまう
        * nodejsだとDOM使わないので無効にしたいけど分からなかった...
        * `tsconfig.json`の`lib`に`["dom"]`としてもダメだった


### ブラウザの場合

`window`に`performance`があるのでそれを使う。

