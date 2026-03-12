import sys
from sqlalchemy.orm import Session
from app.db.models.usuario import Usuario
from app.db.session import Base, engine, SessionLocal



from app.core.security import generar_hash  # La utilidad de Bcrypt que creamos

def sembrar_admin_por_defecto(db: Session):
    """Inserta el usuario admin/admin con hash de seguridad."""
    # Buscamos si ya existe para evitar errores de duplicado
    existe = db.query(Usuario).filter(Usuario.username == "admin").first()
    
    if not existe:
        print("👤 Sembrando usuario administrador inicial...")
        
        # Encriptamos 'admin' antes de guardarlo
        password_segura = generar_hash("admin")
        
        nuevo_admin = Usuario(
            username="admin", 
            password=password_segura
        )
        
        db.add(nuevo_admin)
        db.commit()
        print("✅ Usuario 'admin' creado con éxito (Contraseña encriptada).")
    else:
        print("ℹ️  El usuario 'admin' ya existe, saltando siembra.")

def run():
    db = SessionLocal()
    try:
        # Si pasamos un nombre de tabla específico por consola
        if len(sys.argv) > 1:
            target = sys.argv[1]
            if target in Base.metadata.tables:
                print(f"🏗  Creando tabla específica: {target}...")
                Base.metadata.tables[target].create(bind=engine, checkfirst=True)
                
                # Si la tabla que creamos es 'usuarios', sembramos el admin
                if target == "usuarios":
                    sembrar_admin_por_defecto(db)
            else:
                print(f"❌ La tabla '{target}' no está definida en los modelos.")
        
        # Si no pasamos argumentos, crea TODO
        else:
            print("🏗  Creando todas las tablas definidas en los modelos...")
            Base.metadata.create_all(bind=engine)
            sembrar_admin_por_defecto(db)
            
    except Exception as e:
        print(f"❌ Error durante la creación: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    run()

# python3 -m app.scripts.toolsdb.create_tables usuarios    