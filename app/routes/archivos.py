import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/archivos", tags=["Archivos P12"])

# Ruta base donde están tus certificados
P12_DIR = "/opt/sifen/p12/"

@router.get("/descargar/{nombre_archivo}")
async def descargar_p12(nombre_archivo: str):
    # Construir la ruta completa al archivo
    file_path = os.path.join(P12_DIR, nombre_archivo)
    
    # Validar que el archivo exista
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="El archivo solicitado no existe.")
    
    # Retornar el archivo para descarga
    return FileResponse(
        path=file_path,
        filename=nombre_archivo,
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