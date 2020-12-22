---
description: sedのFAQ
---

# [sed] FAQ

{{ page.meta.description }}


Windowsでsedを使ってファイルを上書きしたい
------------------------------------------

gitに同梱されているsedを使う。  
`-i`オプションはファイル名の手前に。

```
C:\Program Files\Git\usr\bin\sed -r 's/version: .+/version: $(version)/g' -i remote-config.yml
```



