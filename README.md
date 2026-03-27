# Factum API

### Setup del Proyecto

1. **Crear Entorno Virtual:**
```bash
   python3 -m venv venv
   source venv/bin/activate
``

Instalar Dependencias:

```bash
pip install -r requirements.txt
```


### Variables de Entorno
Es obligatorio crear un archivo .env en la raíz del proyecto para la conexión a la base de datos y la seguridad del sistema.

Crea el archivo .env:

```bash
touch .env
```

Copia y pega este formato:


```Ini, TOML
# Configuración de PostgreSQL
DB_USER=mi_usuario
DB_PASSWORD=mi_contraseña
DB_HOST=localhost
DB_PORT=5432
DB_NAME=factum_database

# URL que usará SQLAlchemy (Se arma automáticamente en la app)
DATABASE_URL=postgresql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}

# Seguridad (Generar una clave fuerte)
# Comando sugerido: openssl rand -hex 32
SECRET_KEY=tu_clave_super_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
```



Ejecución
Para iniciar el servidor principal:

```bash
python run.py
```

O vía uvicorn directamente:

```bash
uvicorn app.main:app --reload --port 9000 --host 0.0.0.0
```


swagger

```bash
http://localhost:9000/docs
```
