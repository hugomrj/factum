from fastapi import APIRouter, Header, Response, Request
from app.database import get_db
from app.schemas import CdcRequest, LoteRequest, RucRequest
from app.services.proxy import forward
from fastapi.responses import JSONResponse
from fastapi import Body


router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "ok",
        "service": "factum",
        "alive": True
    }


@router.post("/{emisor}/consulta/ruc")
def consulta_ruc(emisor: str, data: RucRequest):
    
    resp = forward(
        "/api/consulta/ruc",
        data.model_dump(),  
        emisor
    )

    return resp.json()



@router.post("/{emisor}/consulta/de/xml")
def consulta_xml(emisor: str, data: CdcRequest):

    resp = forward(
        "/api/consulta/de/xml",
        data.model_dump(),
        emisor
    )

    return Response(
        content=resp.text,
        status_code=resp.status_code,
        media_type="application/xml"
    )




@router.post("/{emisor}/consulta/lote")
def consulta_lote(
    emisor: str,
    data: LoteRequest
):

    resp = forward(
        "/api/consulta/lote",
        data.model_dump(),
        emisor
    )

    return resp.json()





@router.post("/{emisor}/factura/async")
async def factura_async(
    emisor: str,
    body: dict = Body(...),
    token: str | None = Header(default=None)
):
    
    resp = forward(
        "/api/factura/async/recibe",
        body,
        emisor
    )

    return JSONResponse(
        content=resp.json(),
        status_code=resp.status_code
    )