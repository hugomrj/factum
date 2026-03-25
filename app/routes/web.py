from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.auth import authenticate_user
from app.core.security import crear_token_acceso

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
    usuario = authenticate_user(db, username, password)
    
    if not usuario:
        return templates.TemplateResponse(
            "login.html", 
            {"request": request, "error": "Usuario o contraseña incorrectos"}
        )
    
    # 1. Creamos el Token con la identidad del usuario
    token = crear_token_acceso(data={"sub": usuario.username})
    
    # 2. Preparamos la redirección
    response = RedirectResponse(url="/dashboard", status_code=303)
    
    # 3. Guardamos el token en una Cookie segura
    # httponly=True impide que JavaScript acceda al token (evita XSS)
    response.set_cookie(
        key="access_token", 
        value=f"Bearer {token}", 
        httponly=True, 
        max_age=86400, # 1 día en segundos
        samesite="lax"
    )
    
    return response



@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})