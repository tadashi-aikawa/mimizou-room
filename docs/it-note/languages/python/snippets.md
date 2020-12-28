# [Python] Snippets


1ファイルツール
---------------

### GETとPOSTを受けつけるSimpleHTTPServer

単なるSimpleHTTPServerならファイルは不要だけど、コードから呼び出したりそうでない場合は...

`server.py`
```python
#!/usr/bin/env python

import json
import socketserver
import urllib
from http.server import SimpleHTTPRequestHandler
from typing import Optional


class MyServerHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        print("Log you want to output")
        SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        print("Log you want to output")
        # GETと同じ挙動ならこれだけ
        # SimpleHTTPRequestHandler.do_GET(self)

        # x-www-form-urlencoded対応
        content_type = self.headers.get_content_type()
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(
            json.dumps(
                {
                    "x-www-form-urlencoded": urllib.parse.parse_qs(
                        self.rfile.read(int(self.headers.get("content-length"))).decode("utf-8"),
                        keep_blank_values=1,
                    )
                    if content_type == "application/x-www-form-urlencoded"
                    else None
                },
                ensure_ascii=False,
            ).encode("utf-8")
        )


class ReuseAddressTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def handle(port: Optional[int]):
    with ReuseAddressTCPServer(("", port), MyServerHandler) as httpd:
        print(f"Serving HTTP on 0.0.0.0 port {port} (http://0.0.0.0:{port}/)")
        httpd.serve_forever()
```

必要があれば`port`にポート番号して呼び出せばOK

```python
server.handle(port)
```
