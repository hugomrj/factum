import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles # <--- Importante
from app.router import router

ROOT_PATH = os.getenv("ROOT_PATH", "")

app = FastAPI(
    title="Factum",
    root_path=ROOT_PATH
)

# Montar la carpeta de estáticos
# Esto hace que lo que está en 'web/static' sea accesible vía '/static'
app.mount("/static", StaticFiles(directory="web/static"), name="static")

app.include_router(router)