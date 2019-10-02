# [Poetry] Snippets

{{link("https://poetry.eustace.io/docs/cli/")}}


プロジェクトの作成
------------------

```bash
poetry new <project_name>
```

`pyproject.toml`を作成するだけなら`poetry init`.


packageのインストール/アンインストール
--------------------------------------

### 新しいpackageを指定してインストール

```bash
poetry add <package_name>
```

### packageを指定してアンインストール

```bash
poetry remove <package_name>
```

### 依存関係を全てインストール(devも含む)

```bash
poetry install [<packages>...]
```

* `poetry.lock`がある場合は記載されたバージョンをインストール
* `poetry.lock`がない場合は`pyproject.toml`から依存性グラフを作成した結果のバージョンをインストール + `poetry.lock`の作成

### 依存関係のアップデート

```bash
poetry update [<packages>...]
```

`pyproject.toml`の条件を満たすバージョン最新が、`poetry.lock`に記録されていなければファイルをアップデート + インストール


環境
----

### 各種バージョンや仮想環境

```bash
poetry debug:info
```

packageの依存関係
-----------------

### 一覧で表示

```bash
poetry show
```

### ツリー表示

```bash
poetry show --tree
```

### devは除いて表示

```bash
poetry show --no-dev
```

### 最新版と比較して表示

```bash
poetry show --latest
```

### 古いpackageのみ表示

```bash
poetry show --outdated
```


packageのビルド
---------------

### tarballとwheelを作成

```bash
poetry build
```

### wheelだけ作成

```bash
poetry build -f wheel
```


実行
----

### 仮想環境で実行

```bash
poetry run <commands>...
```
