# app/main.py
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.router import router
from app.core.security import AuthMiddleware # <--- Importamos tu nuevo peaje

ROOT_PATH = os.getenv("ROOT_PATH", "")

app = FastAPI(
    title="Factum",
    root_path=ROOT_PATH
)

# 1. Registro del Middleware
# Debe ir ANTES de los routers para que intercepte cada petición.
app.add_middleware(AuthMiddleware)

# 2. Montar estáticos
# El Middleware por defecto no debería bloquear /static si no 
# incluiste ese prefijo en 'protected_prefixes' en security.py
app.mount("/static", StaticFiles(directory="web/static"), name="static")

# 3. Incluir las rutas
app.include_router(router)