import requests
from config import API_DESTINO

def forward(endpoint: str, data: dict, emisor: str):
    return requests.post(
        f"{API_DESTINO}{endpoint}",
        json=data,
        headers={"Emisor": emisor},
        timeout=30
    )
