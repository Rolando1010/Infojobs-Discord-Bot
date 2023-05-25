import requests
from config import INFOJOBS_TOKEN

def authenticated_infojobs_request(url: str) -> dict:
    return requests.get(url, headers={
        "Authorization": f"Basic {INFOJOBS_TOKEN}"
    }).json()