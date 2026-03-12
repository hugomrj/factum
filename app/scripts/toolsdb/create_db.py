import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv

load_dotenv()

def run():
    db_name = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    
    print(f"🔄 Iniciando ciclo de reset para: {db_name}")
    
    try:
        # Conexión a la base maestra para gestionar la otra
        conn = psycopg2.connect(
            dbname='postgres',
            user=user,
            password=password,
            host=host
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()

        # 1. Forzar cierre de conexiones (si tienes pgAdmin o VSCode abierto, esto lo soluciona)
        print("🔌 Cerrando conexiones activas...")
        cur.execute(f"""
            SELECT pg_terminate_backend(pg_stat_activity.pid)
            FROM pg_stat_activity
            WHERE pg_stat_activity.datname = '{db_name}'
              AND pid <> pg_backend_pid();
        """)

        # 2. Borrar si existe
        print(f"🗑  Borrando base de datos '{db_name}'...")
        cur.execute(f"DROP DATABASE IF EXISTS {db_name};")
        
        # 3. Crear de nuevo
        print(f"🏗  Creando base de datos '{db_name}' desde cero...")
        cur.execute(f"CREATE DATABASE {db_name};")
        
        print(f"✅ ¡Base de datos recreada exitosamente!")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error durante el proceso: {e}")

if __name__ == "__main__":
    run()
    

# python3 -m app.scripts.toolsdb.create_db