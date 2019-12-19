# [Docopt] FAQ


上手くパースされない系
----------------------

### boolじゃない引数がboolになる

以下のように`Usage`と`Options`の間に **空行が存在していない** かを確認する。  
空行がないと意図通り動作しない。

```
"""Initialize a project template for Jumeaux
Usage:
  {cli} (-h | --help)
  {cli} [<name>]
Options:
  <name>                              Initialize template name
  -h --help                           Show this screen.
"""
```

正しくは下記。

```
"""Initialize a project template for Jumeaux
Usage:
  {cli} (-h | --help)
  {cli} [<name>]

Options:
  <name>                              Initialize template name
  -h --help                           Show this screen.
"""
```
