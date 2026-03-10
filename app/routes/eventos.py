from fastapi import APIRouter, Header
from app.services.proxy import forward
from app.schemas import CancelarRequest

router = APIRouter()

@router.post("/{emisor}/evento/cancelar")
def cancelar_evento(
    emisor: str,
    data: CancelarRequest,
    token: str | None = Header(None)
):
    headers = {
        "Emisor": emisor,
        "token": token
    }

    resp = forward(
        "POST",
        "/api/evento/cancelar",
        data=data.model_dump(),
        headers=headers  
    )

    return resp.json()