# app/core/security.py
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "tu_clave_secreta_super_segura" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)



# --- CLASE PROFESIONAL DE MIDDLEWARE ---
class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        
        # 1. LISTA BLANCA: Rutas que NUNCA se bloquean
        # Si es un archivo de CSS/JS o la página de login, lo dejamos pasar directo
        if path.startswith("/static") or path == "/login":
            return await call_next(request)
        
        # 2. RUTAS PROTEGIDAS: Si la ruta empieza con estas, pedimos credenciales
        protected_prefixes = ["/dashboard", "/facturas", "/archivos", "/eventos", "/consultas"]
        
        if any(path.startswith(prefix) for prefix in protected_prefixes):
            token = request.cookies.get("access_token")
            
            # Si no hay cookie, al login
            if not token:
                return RedirectResponse(url="/login", status_code=302)
            
            try:
                # Quitamos el prefijo 'Bearer ' y validamos el JWT
                token_clean = token.replace("Bearer ", "")
                jwt.decode(token_clean, SECRET_KEY, algorithms=[ALGORITHM])
            except JWTError:
                # Si el token expiró o es falso, borramos la cookie y al login
                response = RedirectResponse(url="/login", status_code=302)
                response.delete_cookie("access_token")
                return response
        
        # 3. Si todo está OK, seguimos al controlador (API o View)
        return await call_next(request)