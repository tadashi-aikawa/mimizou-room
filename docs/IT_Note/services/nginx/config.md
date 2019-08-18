# [Nginx] Config


コンテナとのリバースプロキシとして使うconf
------------------------------------------

`your.host.net`でNginxサーバへ到達可能であり、その中で`3333 -> ?`というコンテナとのポートフォワーディングをしている場合。

```conf
server {
  listen 80;
  server_name <your_domain>;

  proxy_set_header Host $host;
  proxy_set_header Host $http_host;
  proxy_set_header X-Real-IP $remote_addr;
  proxy_set_header X-Forwarded-Proto https;
  proxy_set_header X-Forwarded-Host $host;
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

  location / {
    proxy_pass http://127.0.0.1:3333;
  }
}
```

`proxy_set_header`を忘れるとリバースプロキシのことが考慮されずに色々ハマル。  
301で127.0.01にリダイレクトされたりとか..。

HTTP(80)へのアクセスを恒久的リダイレクトとしてHTTPS(443)に渡す。  
443側ではsslを使って証明書情報を`ssl_certificate`オプションで渡す。

### HTTPSとして受けつける場合 (コンテナへはHTTP)

```conf
server {
  listen 80;
  server_name <your_domain>;
  return 301 https://$host$request_uri;
}

server {
  listen 443 ssl;
  server_name <your_domain>;

  ssl_certificate /etc/letsencrypt/live/<your_domain>/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/<your_domain>/privkey.pem;

  proxy_set_header Host $host;
  proxy_set_header Host $http_host;
  proxy_set_header X-Real-IP $remote_addr;
  proxy_set_header X-Forwarded-Proto https;
  proxy_set_header X-Forwarded-Host $host;
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

  location / {
    proxy_pass http://127.0.0.1:3333;
  }
}
```


Basic認証のconf
---------------

`server`セクションの中に以下2行を追加。

```conf
  auth_basic "Restricted";
  auth_basic_user_file /etc/nginx/.htpasswd;
```

`/etc/nginx/.htpasswd`には認証情報を記載すること。

```term
$pass=<password>
echo "<user>:$(openssl passwd -crypt $pass)" > /etc/nginx/.htpasswd
```

