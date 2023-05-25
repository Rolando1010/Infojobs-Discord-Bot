import requests
from config import GITHUB_TOKEN

def authenticated_github_request(url) -> dict:
    return requests.get(url, headers={
        "Authorization": f"Bearer {GITHUB_TOKEN}"
    }).json()