from jobs.offers import Offer
from .db import Database, get_total_pages_key, get_entity_offers_key

def get_skills() -> list[str]:
    database = Database()
    skills = database.get_list("skill")
    database.close()
    return skills

def get_offers_skill(skill: str, page: int) -> tuple[list[Offer], int]:
    database = Database()
    total_pages = database.get_int(get_total_pages_key(skill, "skill"))
    offers = list(map(Offer, database.get_list(get_entity_offers_key(skill, page, "skill"))))
    database.close()
    return offers, total_pages