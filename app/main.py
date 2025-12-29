from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Factum")

app.include_router(router)
