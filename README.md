## 環境設置
以下為本專案所使用的環境：

- [Docker]
- [Python] 版本 11
- [Poetry]
- [Flask]

## 後端設置

後端使用 Python 11 和 PostgreSQL 15.3（資料庫使用 Docker container）。

### 安裝相關 Library

```bash
pip install poetry
poetry install
```

### 啟動 PostgreSQL

首先，需要啟動一個 PostgreSQL 15.3 的 Docker container：

```bash
docker run --name gainmiles -e POSTGRES_USER=GainMiles -e POSTGRES_PASSWORD=GainMiles -e POSTGRES_DB=gain_miles -p 5433:5432 postgres
```

上述的指令會在本地的 5433 port 啟動一個 PostgreSQL 15.3 的 Docker container

### 啟動後端伺服器

首先進入後端所在的資料夾：

```bash
cd /{path_to_GainMilesTest}/
```

接著，執行下面的指令來啟動伺服器，並會在`localhost:3000`運作：

```bash
poetry shell
python app.py
```

