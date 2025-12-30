import requests
from config import API_DESTINO


def forward(endpoint: str, data: dict, emisor: str, token: str | None = None):
    headers = {
        "Emisor": emisor
    }

    if token:
        headers["token"] = token

    return requests.post(
        f"{API_DESTINO}{endpoint}",
        json=data,
        headers=headers,
        timeout=30
    )