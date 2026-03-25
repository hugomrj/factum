# app/services/auth.py
from sqlalchemy.orm import Session
from app.db.models.usuario import Usuario  # El modelo puede seguir en ES
from app.core.security import verify_password

def authenticate_user(db: Session, username: str, password_plain: str):
    # 1. Search object in DB
    user = db.query(Usuario).filter(Usuario.username == username).first()
    
    if not user:
        return None
    
    # 2. Validate password
    if not verify_password(password_plain, user.password):
        return None
        
    return user