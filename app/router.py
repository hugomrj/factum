from fastapi import APIRouter

from app.routes.health import router as health_router
from app.routes.consultas import router as consultas_router
from app.routes.facturas import router as facturas_router
from app.routes.eventos import router as eventos_router

router = APIRouter()

router.include_router(health_router)
router.include_router(consultas_router)
router.include_router(facturas_router)
router.include_router(eventos_router)
