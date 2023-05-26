from .requests import authenticated_infojobs_request, browserify_request, OFFERS_URL, SEARCH_OFFERS_URL

class OfferAuthor():
    def __init__(self, name: str, link: str, logo: str) -> None:
        self.name = name
        self.link = link
        self.logo = logo
    
    def serialize(self):
        return {
            "name": self.name,
            "link": self.link
        }

class Offer():
    def __init__(self, offer: dict) -> None:
        self.id: str = offer.get("id", offer.get("code", ""))
        self.title: str = offer.get("title", "")
        self.description: str = offer.get("description", "")
        self.category: str = offer.get("category", {}).get("value", "")
        self.salary_min: int = offer.get("salary_min", 0)
        self.salary_max: int = offer.get("salary_max", 0)
        self.experience: str = offer.get("experience", "")
        self.country: str = offer.get("country", {}).get("value", "")
        self.applications: int = offer.get("applications", 0)
        link = offer.get("link", "")
        self.link: str = "https:" + link if link[0] == "/" else link
        author = offer.get("author", {})
        profile = offer.get("profile", {})
        self.author = OfferAuthor(
            author.get("name", "") or offer.get("companyName", "") or profile.get("name"),
            author.get("uri", "") or author.get("link", "") or offer.get("companyLink", "") or profile.get("url", ""),
            profile.get("logoUrl", "")
        )
        self.skills: list[str] = list(map(lambda s: s["skill"], offer.get("skillsList", [])))
    
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

    def get_salary_message(self):
        return f"Salario de {self.salary_min} a {self.salary_max}" if self.salary_min or self.salary_max else "Salario no disponible"

def get_offers(page: int = 1) -> tuple[list[Offer], int]:
    response = authenticated_infojobs_request(OFFERS_URL + "?page="+str(page))
    total_pages = response.get("totalPages", 0)
    offers = list(map(Offer, response.get("items", [])))
    return offers, total_pages

def search_offers(search: str, page: int) -> list[Offer]:
    response = browserify_request(f"{SEARCH_OFFERS_URL}?keyword={search}&page={page}")
    offers = list(map(Offer, response.get("offers", [])))
    return offers

def get_offer(id: str):
    response = authenticated_infojobs_request(f"{OFFERS_URL}/{id}")
    if "error" in response:
        raise Exception("offer not found")
    return Offer(response)