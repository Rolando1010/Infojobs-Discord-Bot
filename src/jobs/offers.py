from .requests import authenticated_get_request, browserified_request
from .constants import OFFERS_URL

class OfferAuthor():
    def __init__(self, name: str, link: str) -> None:
        self.name = name
        self.link = link
    
    def serialize(self):
        return {
            "name": self.name,
            "link": self.link
        }

class Offer():
    def __init__(self, offer: dict) -> None:
        self.id: str = offer.get("id", offer.get("code", ""))
        self.title: str = offer.get("title", "")
        self.city: str = offer.get("city", "")
        link = offer.get("link", "")
        self.link: str = "https:" + link if link[0] == "/" else link
        self.category: str = offer.get("category", "")
        self.subcategory: str = offer.get("subcategory", "")
        self.salary_min: int = offer.get("salary_min", 0)
        self.salary_max: int = offer.get("salary_max", 0)
        self.experience: str = offer.get("experience", "")
        self.work_day: str = offer.get("work_day", "")
        self.updated: str = offer.get("updated", "")
        author = offer.get("author", {})
        self.author = OfferAuthor(
            author.get("name", "") or offer.get("companyName", ""),
            author.get("uri", author.get("link", "")) or offer.get("companyLink", "")
        )
        self.applications: int = offer.get("applications", 0)
    
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "link": self.link,
            "author": self.author.serialize(),
            "applications": self.applications,
            "salary_min": self.salary_min,
            "salary_max": self.salary_max
        }

def get_offers(page: int = 1) -> tuple[list[Offer], int]:
    response = authenticated_get_request(OFFERS_URL + "?page="+str(page))
    total_pages = response.get("totalPages", 0)
    offers = list(map(Offer, response.get("items", [])))
    return offers, total_pages

def search_offers(search: str, page: int) -> list[Offer]:
    response = browserified_request(f"https://www.infojobs.net/webapp/offers/search?keyword={search}&page={page}&onlyForeignCountry=false")
    offers = list(map(Offer, response.get("offers", [])))
    return offers