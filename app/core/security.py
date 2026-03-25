# app/core/security.py
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



SECRET_KEY = "tu_clave_secreta_super_segura" # Usa una variable de entorno en producción
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 # 1 día



def generar_hash(password: str) -> str:
    """Convierte texto plano en un hash seguro."""
    return pwd_context.hash(password)

def verificar_password(password_plana: str, password_hasheada: str) -> bool:
    """Compara la contraseña con el hash."""
    return pwd_context.verify(password_plana, password_hasheada)

def crear_token_acceso(data: dict):
    a_copiar = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    a_copiar.update({"exp": expire})
    encoded_jwt = jwt.encode(a_copiar, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt    