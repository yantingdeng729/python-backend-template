from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os
from pathlib import Path

# 加载 .env
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")

# 创建 Engine
engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)

# Session 工具方法
def get_session():
    with Session(engine) as session:
        yield session
