import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/archivos", tags=["Archivos P12"])

P12_DIR = "/opt/sifen/p12/"

@router.get("/descargar/{nombre_archivo}")
async def descargar_p12(nombre_archivo: str):
    # Sanitizamos el nombre para evitar saltos de carpeta
    nombre_seguro = os.path.basename(nombre_archivo)
    file_path = os.path.join(P12_DIR, nombre_seguro)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="El certificado no existe.")
    
    return FileResponse(
        path=file_path,
        filename=nombre_seguro,
        media_type="application/x-pkcs12"
    )



@router.get("/listar")
async def listar_p12():
    """Opcional: Para saber qué archivos hay disponibles"""
    try:
        archivos = os.listdir(P12_DIR)
        return {"archivos": [f for f in archivos if f.endswith('.p12')]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))