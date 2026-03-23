from fastapi import APIRouter

from app.routes.health import router as health_router
from app.routes.consultas import router as consultas_router
from app.routes.facturas import router as facturas_router
from app.routes.eventos import router as eventos_router

from app.routes.archivos import router as archivos_router
from app.routes.web import router as web_router

router = APIRouter()

router.include_router(health_router)
router.include_router(consultas_router)
router.include_router(facturas_router)
router.include_router(eventos_router)

router.include_router(archivos_router)

router.include_router(web_router)