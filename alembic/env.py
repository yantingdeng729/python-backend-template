import os
import sys
from logging.config import fileConfig
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlmodel import SQLModel
from alembic import context

# =========================================
# 1. 确保 Alembic 能导入 app 模块
# =========================================
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "app"))

# =========================================
# 2. 加载 .env 文件
# =========================================
load_dotenv(BASE_DIR / ".env")

DB_URL = os.getenv("DATABASE_URL")

# =========================================
# 3. Alembic 基础配置
# =========================================
config = context.config

# 如果 alembic.ini 没设置数据库连接，这里动态注入
if DB_URL:
    config.set_main_option("sqlalchemy.url", DB_URL)

# logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# =========================================
# 4. 导入模型 metadata
# =========================================
from app.db import models  # noqa: F401  # 确保 models 文件被导入
target_metadata = SQLModel.metadata

# =========================================
# 5. 跳过 auth schema（你原有逻辑保留）
# =========================================
def include_object(object, name, type_, reflected, compare_to):
    if type_ == "table" and object.schema == "auth":
        return False
    if type_ == "column" and object.table.schema == "auth":
        return False
    return True

# =========================================
# 6. 迁移逻辑
# =========================================
def run_migrations_offline() -> None:
    url = DB_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_object=include_object,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = create_engine(DB_URL, pool_pre_ping=True)
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
