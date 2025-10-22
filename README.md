# Pikpop Python 后端项目

本项目基于 **FastAPI** 与 **SQLModel** 构建，使用 **MySQL** 作为数据库，
并通过 **Alembic** 管理数据库迁移。依赖与虚拟环境由 [uv](https://github.com/astral-sh/uv) 管理，
适用于云函数（FC）或轻量级后端服务的开发与部署。

---

## 一、项目特性

- 使用 FastAPI 构建 RESTful 后端服务
- 采用 SQLModel 定义数据库模型（兼具 ORM 与 Pydantic 数据校验能力）
- 集成 Alembic 实现数据库结构的版本控制与迁移
- 通过 uv 管理依赖与 Python 环境

---

## 二、环境要求

| 依赖项 | 说明 |
| --- | --- |
| **Python** | 3.11 及以上版本 |
| **MySQL** | 8.0 及以上版本 |
| **uv** | Python 依赖与虚拟环境管理工具 |

---

## 三、初始化步骤

### 1. 创建环境变量配置

复制示例环境文件：

```bash
cp .env.example .env
```

在 `.env` 文件中填写数据库连接信息与必要参数，例如：

```dotenv
DATABASE_URL=mysql+pymysql://user:password@127.0.0.1:3306/pikpop
SECRET_KEY=your_secret_key
```

### 2. 安装依赖

使用 uv 同步依赖（自动创建虚拟环境）：

```bash
uv sync
```

### 3. 激活虚拟环境

uv 会默认在项目根目录创建 `.venv`。如需在交互式终端中使用虚拟环境，请手动激活：

```bash
source .venv/bin/activate  # macOS / Linux
```

```powershell
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
```

---

## 四、数据库迁移（Alembic）

1. **生成迁移脚本**

   当数据库模型（`app/db/models.py`）有更新时执行：

   ```bash
   uv run alembic revision --autogenerate -m "init tryon tables"
   ```

2. **应用迁移**

   ```bash
   uv run alembic upgrade head
   ```

3. **验证迁移结果**

   确认数据库中已创建或更新相应表结构。

---

## 五、启动后端服务

本地启动 FastAPI 服务进行开发调试：

```bash
uv run uvicorn app.main:app --reload --reload-dir app
```

访问 `http://127.0.0.1:8000/docs` 可查看自动生成的交互式接口文档。

## 六、项目结构说明

```text
app/
├── api/                 # 路由层（API 接口定义）
├── core/                # 全局配置与依赖注入
├── db/                  # 数据库模型与连接配置
├── repositories/        # 数据访问层
├── schemas/             # 数据结构定义（Pydantic 模型）
├── services/            # 业务逻辑层
└── main.py              # 应用入口（创建 FastAPI 实例）
```

## 七、依赖管理说明

本项目使用 uv 管理 Python 环境与依赖：

| 命令 | 说明 |
| --- | --- |
| `uv sync` | 安装项目依赖并创建虚拟环境 |
| `uv add <package>` | 添加新依赖 |
| `uv remove <package>` | 移除依赖 |
| `uv run <command>` | 在隔离环境中运行命令 |
| `uv lock` | 生成锁定文件 `uv.lock` |

---

## 九、许可证

本项目基于 MIT License 开源。