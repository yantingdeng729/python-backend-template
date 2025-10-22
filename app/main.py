from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, ziwei

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],  # 可根据需要放开前端 dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
