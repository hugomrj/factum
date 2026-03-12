# app/core/security.py
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generar_hash(password: str) -> str:
    """Convierte texto plano en un hash seguro."""
    return pwd_context.hash(password)

def verificar_password(password_plana: str, password_hasheada: str) -> bool:
    """Compara la contraseña con el hash."""
    return pwd_context.verify(password_plana, password_hasheada)