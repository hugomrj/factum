import requests
from requests import Response
from config import API_DESTINO


def forward(
    method: str,
    endpoint: str,
    *,
    params: dict | None = None,
    data: dict | None = None,
    headers: dict | None = None, 
    token: str | None = None
) -> Response:
    method = method.upper()

    # 1. Creamos los headers que SIEMPRE deben ir
    request_headers = {
        "Content-Type": "application/json"
    }

    # 2. Si recibimos headers los agregamos
    if headers:
        request_headers.update(headers)

    # 3. Si hay token, lo agregamos 
    if token and "token" not in request_headers:
        request_headers["token"] = token

    try:
        # 4. Enviamos 'request_headers', NO la variable 'headers' original
        return requests.request(
            method=method,
            url=f"{API_DESTINO}{endpoint}",
            params=params,
            json=data,
            headers=request_headers,
            timeout=30
        )

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error comunicando con API destino: {e}")