---
description: PoetryのFAQ
---

# [Poetry] FAQ

{{ page.meta.description }}


依存関係を追加するとAssertionError
----------------------------------

こういう感じになる場合。

```
~\tmp\rich ❯ poetry add rich                                                                                                                                                       09:35:00
Creating virtualenv rich-a9RZ6qXV-py3.8 in C:\Users\syoum\AppData\Local\pypoetry\Cache\virtualenvs
Using version ^2.0.1 for rich

Updating dependencies
Resolving dependencies...

[AssertionError]
```

プロジェクト名と依存関係のパッケージ名が同一だと起こるらしい。

{{refer("https://github.com/python-poetry/poetry/issues/1051")}}

『もう少し説明的なエラーにしたいね』とのコメントがある。
