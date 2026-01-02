from fastapi import APIRouter
from app.services.proxy import forward

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok", "service": "factum", "alive": True}

@router.get("/{emisor}/health/sifen/{env}")
def health_sifen(emisor: str, env: str):
    resp = forward(
        "GET",
        f"/api/health/sifen/{env}",
        params={"emisor": emisor}
    )
    return resp.json()
