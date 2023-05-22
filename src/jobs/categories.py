from .db import Database, get_entity_offers_key, get_total_pages_key, get_category_skills_key
from .offers import Offer

def get_categories() -> list[str]:
    database = Database()
    categories = database.get_list("category")
    database.close()
    return categories

def get_offers_category(category: str, page: int) -> tuple[list[Offer], int]:
    database = Database()
    offers_category = database.get_list(get_entity_offers_key(category, page, "category"))
    total_page = database.get_int(get_total_pages_key(category, "category"))
    database.close()
    return list(map(Offer, offers_category)), total_page

def get_category_skills(category: str) -> list[str]:
    database = Database()
    skills = database.get_list(get_category_skills_key(category))
    database.close()
    return skills