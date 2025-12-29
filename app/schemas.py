from pydantic import BaseModel

class RucRequest(BaseModel):
    ruc: str




class CdcRequest(BaseModel):
    cdc: str
