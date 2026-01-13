from fastapi import APIRouter, Body, Header
from app.services.proxy import forward
from fastapi import Response

router = APIRouter()

@router.post("/{emisor}/factura/async")
def factura_async(emisor: str, body: dict = Body(...), token: str | None = Header(None)):
    resp = forward("POST", "/api/factura/async/recibe", data=body, token=token)
    return resp.json()






@router.post("/{emisor}/factura/xml/generar")
def generar_factura_xml(
    emisor: str,
    body: dict = Body(...),
):
    print("=== FACTURA XML GENERAR ===")
    print("Emisor (path):", emisor)

    resp = forward(
        "POST",
        "/api/factura/xml/generar",
        data=body,
        token=emisor  # ← se envía como header
    )

    return Response(
        content=resp.text,
        status_code=resp.status_code,
        media_type="application/json"
    )
