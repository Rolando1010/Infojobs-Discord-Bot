from .db import Database, get_entity_offers_key, get_total_pages_key, get_category_skills_key
from .offers import get_offers, get_offer

MAX_OFFERS_PAGE_SIZE = 10

database = Database()

def add_entity_page(new_total_pages: int, total_pages_key: str, type: str, entity: str, offers: list[dict]):
    if not offers: return
    database.set(total_pages_key, new_total_pages)
    new_page_key = get_entity_offers_key(entity, new_total_pages, type)
    database.set(new_page_key, offers[:MAX_OFFERS_PAGE_SIZE])
    add_entity_page(new_total_pages + 1, total_pages_key, type, entity, offers[MAX_OFFERS_PAGE_SIZE:])

def save_entity(entities: dict[str, list], type: str):
    entity_names: list[str] = []
    for entity in entities:
        total_pages_key = get_total_pages_key(entity, type)
        total_pages = database.get_int(total_pages_key)
        if total_pages:
            key = get_entity_offers_key(entity, total_pages, type)
            saved_offers = database.get_list(key)
            limit = MAX_OFFERS_PAGE_SIZE - len(saved_offers)
            offers = entities[entity]
            database.set(key, saved_offers + offers[:limit])
            add_entity_page(total_pages + 1, total_pages_key, type, entity, offers[limit:])
        else:
            add_entity_page(1, total_pages_key, type, entity, entities[entity])
        entity_names.append(entity)
    database.set(type, entity_names)

def add_category_skills(category: str, skills: list[str]):
    key = get_category_skills_key(category)
    saved_category_skills = database.get_list(key)
    for skill in skills:
        if skill not in saved_category_skills:
            saved_category_skills.append(skill)
    database.set(key, saved_category_skills)

def extract_offers_data(begin_page: int, end_page: int, clear: bool = False):
    if clear: database.clear()
    page = begin_page
    while page <= end_page:
        offers, total_pages = get_offers(page)
        categories: dict[str, list] = {}
        countries: dict[str, list] = {}
        skills: dict[str, list] = {}
        for offer in offers:
            offer_detail = get_offer(offer.id)
            serialized_offer = offer.serialize()
            if offer_detail.category in categories: categories[offer_detail.category].append(serialized_offer)
            else: categories[offer_detail.category] = [serialized_offer]
            if offer_detail.country in countries: countries[offer_detail.country].append(serialized_offer)
            else: countries[offer_detail.country] = [serialized_offer]
            for skill in offer_detail.skills:
                if skill in skills: skills[skill].append(serialized_offer)
                else: skills[skill] = [serialized_offer]
            add_category_skills(offer_detail.category, offer_detail.skills)
            print("offer:", offer.title)
        save_entity(categories, "category")
        save_entity(countries, "country")
        save_entity(skills, "skill")
        print("page:", page)
        page += 1
    database.close()