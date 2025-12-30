import os
from fastapi import FastAPI
from app.routes import router

ROOT_PATH = os.getenv("ROOT_PATH", "")

app = FastAPI(
    title="Factum",
    root_path=ROOT_PATH
)

app.include_router(router)

