from .offers import Offer
from .db import Database, get_total_pages_key, get_entity_offers_key

def get_countries() -> list[str]:
    database = Database()
    countries = database.get_list("country")
    database.close()
    return countries

def get_offers_country(country: str, page: int) -> tuple[list[Offer], int]:
    database = Database()
    total_pages = database.get_int(get_total_pages_key(country, "country"))
    offers = database.get_list(get_entity_offers_key(country, page, "country"))
    database.close()
    return list(map(Offer, offers)), total_pages