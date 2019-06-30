# [Python] FAQ


URLを分解/解析/組み立てしたい
-----------------------------

`urllib.parse`の関数を使う。

{{link("https://docs.python.org/ja/3/library/urllib.parse.html#urllib.parse.urlsplit")}}


HTMLに記載できない文字をエスケープしたい
----------------------------------------

`xml.sax.saxutils`の`escape`を使う。

{{link("https://docs.python.org/ja/3/library/xml.sax.utils.html?highlight=xml%20sax%20saxutil#xml.sax.saxutils.escape")}}


[requests]や[requests-html]のリクエストをキャッシュしたい
---------------------------------------------------------

`requests-cache`を使う。

{{link("https://github.com/reclosedev/requests-cache")}}

Sessionをimportする前にimportする必要がある。

```python
import requests_cache

# Must install before importing HTMLSession
requests_cache.install_cache(
    cache_name="mimizou_room", backend="sqlite", expire_after=timedelta(hours=24)
)
from requests_html import HTMLSession
```

[requests]: https://github.com/kennethreitz/requests
[requests-html]: https://github.com/kennethreitz/requests-html