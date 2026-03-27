from fastapi import APIRouter, Request, Depends, Form, Response  # 1. Agregado Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.auth import authenticate_user
from app.core.security import create_access_token 

router = APIRouter(tags=["web"])
templates = Jinja2Templates(directory="web/templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
async def login(
    request: Request, 
    username: str = Form(...), 
    password: str = Form(...), 
    db: Session = Depends(get_db)
):
    # 1. Validamos con el servicio (Lógica de Negocio)
    user = authenticate_user(db, username, password)
    
    if not user:
        # 2. Si falla, enviamos solo el "pedacito" de HTML del error
        return templates.TemplateResponse(
            "partials/error_message.html", 
            {"request": request, "type": "error", "message": "Usuario o clave incorrectos"}
        )
    
    # 3. Si tiene éxito, generamos el token
    token = create_access_token(data={"sub": user.username})
    
    # 4. Creamos una respuesta vacía (204 No Content) pero con instrucciones para HTMX
    response = Response(status_code=204)
    response.headers["HX-Redirect"] = "/dashboard" # <--- HTMX lee esto y redirecciona
    
    # 5. Guardamos el token en una cookie segura
    response.set_cookie(
        key="access_token", 
        value=f"Bearer {token}", 
        httponly=True, 
        max_age=86400,
        samesite="lax"
    )
    
    return response


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})