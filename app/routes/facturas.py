from fastapi import APIRouter, Body, Header
from app.services.proxy import forward


router = APIRouter()

@router.post("/{emisor}/factura/async")
def factura_async(emisor: str, body: dict = Body(...), token: str | None = Header(None)):
    resp = forward("POST", "/api/factura/async/recibe", data=body, token=token)
    return resp.json()
