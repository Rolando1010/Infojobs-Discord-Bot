import requests
from config import INFOJOBS_TOKEN

OFFERS_URL = "https://api.infojobs.net/api/4/offer"
SEARCH_OFFERS_URL = "https://www.infojobs.net/webapp/offers/search"

def authenticated_infojobs_request(url: str) -> dict:
    return requests.get(url, headers={
        "Authorization": f"Basic {INFOJOBS_TOKEN}"
    }).json()

def browserify_request(url: str) -> dict:
    return requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    }).json()