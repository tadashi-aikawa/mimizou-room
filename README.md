Mimizou Room
============

[![Netlify Status](https://api.netlify.com/api/v1/badges/c79dd463-28d2-44fd-9fa7-8621bf03f1b5/deploy-status)](https://app.netlify.com/sites/mimizou-room/deploys)

Mimizou Roomは https://mimizou.mamansoft.net にホスティングされています。


💻 For developers
-------------------

### Install dependencies

```
poetry install
```

### Run

```
make
```

### Create requirements.txt

Netlifyでデプロイするときは`requirements.txt`を使うため作成します。

```
make create-requirements
```

経緯: https://blog.mamansoft.net/2020/07/05/2020-07-1w-weekly-report/#netlifypoetry%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%83%93%E3%83%AB%E3%83%89%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E3%81%99%E3%82%8B%E3%81%A8%E6%99%82%E9%96%93%E3%81%8C%E3%81%8B%E3%81%8B%E3%82%8B

