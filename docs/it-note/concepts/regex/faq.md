---
description: 正規表現のFAQ
---

# [正規表現] FAQ

{{ page.meta.description }}


名前付きキャプチャで文字列を抽出したい
--------------------------------------

=== "JavaScript"
    `match`でキャプチャのパターン手前に`?<名前>`を入れる。  
    `(?<名前>パターン)`のようにカッコの中なので注意。
    
    ```javascript
    "tadashi-aikawa".match(/(?<firstName>.+)-(?<lastname>.+)/).groups
    // -> {firstName: "tadashi", lastname: "aikawa"}
    ```

=== "python"
    `re`モジュールの`match`でキャプチャのパターン手前に`?P<名前>`を入れる。  
    JavaScriptとは異なり `?` のあとに `P` が入るので要注意。
    
    ```python
    import re
    
    re.match(r'(?P<firstName>.+)-(?P<lastname>.+)', 'tadashi-aikawa').groupdict()
    # -> {'firstName': 'tadashi', 'lastname': 'aikawa'}
    ```

