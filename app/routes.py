from fastapi import APIRouter, Header, Response
from app.database import get_db
from app.schemas import CdcRequest, RucRequest
from app.services.proxy import forward

router = APIRouter()


@router.post("/{emisor}/consulta/ruc")
def consulta_ruc(emisor: str, data: RucRequest):

    emisor = None 

    resp = forward(
        "/api/consulta/ruc",
        data.model_dump(),  
        emisor
    )

    return resp.json()





@router.post("/{emisor}/consulta/de/xml")
def consulta_xml(emisor: str, data: CdcRequest):


    emisor = None 


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