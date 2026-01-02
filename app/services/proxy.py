import requests
from requests import Response
from config import API_DESTINO


def forward(
    method: str,
    endpoint: str,
    *,
    params: dict | None = None,
    data: dict | None = None,
    token: str | None = None
) -> Response:
    method = method.upper()

    headers = {
        "Content-Type": "application/json"
    }

    if token:
        headers["token"] = token

    try:
        return requests.request(
            method=method,
            url=f"{API_DESTINO}{endpoint}",
            params=params,
            json=data,
            headers=headers,
            timeout=30
        )

    except requests.exceptions.RequestException as e:
        # log real iría acá
        raise RuntimeError(f"Error comunicando con API destino: {e}")
