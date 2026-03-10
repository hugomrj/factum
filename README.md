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
