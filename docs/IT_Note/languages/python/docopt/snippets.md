# [Docopt] Snippets


Usageの書き方
-------------

```
"""Naval Fate.

Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <x> <y>
  naval_fate.py mine (set|remove) <x> <y> [--moored | --drifting]
  naval_fate.py (-h | --help)
  naval_fate.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.

"""
```

### `node new tokyo osaka`

```json
{'--help': False,
 '--type': None,
 '--version': False,
 '--with-nodes': False,
 '-v': 0,
 '<lat>': None,
 '<lon>': None,
 '<name>': ['tokyo', 'osaka'],
 'info': False,
 'move': False,
 'name': False,
 'new': True,
 'node': True,
 'remove': False,
 'stop': False}
```

### `node move 35.00000 135.00000`

数値でも文字列として読み込まれる。

```json
{'--help': False,
 '--type': None,
 '--version': False,
 '--with-nodes': False,
 '-v': 0,
 '<lat>': '35.00000',
 '<lon>': '135.00000',
 '<name>': [],
 'info': False,
 'move': True,
 'name': False,
 'new': False,
 'node': True,
 'remove': False,
 'stop': False}
```

### `node remove --type station`

`--type`の代わりに`-t`でもOK.

```json
{'--help': False,
 '--type': 'station',
 '--version': False,
 '--with-nodes': False,
 '-v': 0,
 '<lat>': None,
 '<lon>': None,
 '<name>': [],
 'info': False,
 'move': False,
 'name': False,
 'new': False,
 'node': True,
 'remove': True,
 'stop': False}
```

### `stop new yaesu marunouchi -n`

`-n`の代わりに`--with-nodes`でもOK.

```json
{'--help': False,
 '--type': None,
 '--version': False,
 '--with-nodes': True,
 '-v': 0,
 '<lat>': None,
 '<lon>': None,
 '<name>': ['yaesu', 'marunouchi'],
 'info': False,
 'move': False,
 'new': True,
 'node': False,
 'remove': False,
 'stop': True}
```

### `info -vv`

`-vv`は`-v: 2`として扱われる。

```json
{'--help': False,
 '--type': None,
 '--version': False,
 '--with-nodes': False,
 '-v': 2,
 '<lat>': None,
 '<lon>': None,
 '<name>': [],
 'info': True,
 'move': False,
 'new': False,
 'node': False,
 'remove': False,
 'stop': False}
```


サブコマンドの実装例
--------------------

### argv=sys.argv[1:3]

何が引数になっても受け入れられるように必要

### option_first=True

main_argsのパースでヘルプ表示されないように必要
