from fastapi import APIRouter, Header
from app.schemas import RucRequest, CdcRequest, LoteRequest
from app.services.proxy import forward


router = APIRouter()





@router.post("/{emisor}/consulta/ruc")
def consulta_ruc(
    emisor: str,
    data: RucRequest,
    token: str | None = Header(None)
):
    headers = {
        "emisor": emisor,
        "token": token
    }

    resp = forward(
        "POST",
        "/api/consulta/ruc",
        data=data.model_dump(),
        headers=headers
    )
    
    return resp.json()



@router.post("/{emisor}/consulta/de/xml")
def consulta_xml(
    emisor: str,
    data: CdcRequest,
    token: str | None = Header(None)
):

    headers = {
        "Emisor": emisor,
        "token": token
    }

    resp = forward(
        "POST",
        "/api/consulta/de/xml",
        data=data.model_dump(),
        headers=headers  
    )

    return {
        "status": resp.status_code,
        "data": resp.text
    }



@router.post("/{emisor}/consulta/lote")
def consulta_lote(
    emisor: str,
    data: LoteRequest,
    token: str | None = Header(None)
):
    headers = {
        "Emisor": emisor,
        "token": token
    }

    resp = forward(
        "POST",
        "/api/consulta/lote",
        data=data.model_dump(),
        headers=headers  
    )

    return resp.json()