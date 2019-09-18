# [Jest] Snippets


`jest.config.js`
----------------

```js
module.exports = {
  verbose: true,
  testPathIgnorePatterns: ["/node_modules/", "/dist/"],

  // src配下のtsファイルから測定していとき
  collectCoverageFrom: ["src/**/*.ts"],
  // collectCoverageFromだけではカバレッジ測定できない
  collectCoverage: true
};
```
