# [Make] FAQ


CLIで指定した変数が反映されない
-------------------------------

makeコマンドの後に指定されているか確認する。

* 🆖 `VAR=hoge make run`
* 🆗 `make run VAR=hoge`


Windowsでshellが使われてしまう
------------------------------

Makefileの先頭に以下を記載する。

```
SHELL=cmd
```

GNU Makeは`sh`にパスが通っていると、SHELLにそちらを割り当てるから。
