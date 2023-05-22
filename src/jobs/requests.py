import requests
from config import INFOJOBS_TOKEN

def authenticated_get_request(url: str) -> dict:
    return requests.get(url, headers={
        "Authorization": f"Basic {INFOJOBS_TOKEN}"
    }).json()

def browserified_request(url: str) -> dict:
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }).json()