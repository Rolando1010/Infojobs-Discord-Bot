from redis import Redis
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD
import json

def get_entity_offers_key(entity: str, page: int, type: str):
    return {
        "type": type,
        "value": "offers",
        "key": entity,
        "page": page
    }

def get_total_pages_key(entity: str, type: str):
    return {
        "type": type,
        "value": "total_pages",
        "key": entity
    }

def get_category_skills_key(category: str):
    return {"type": "category", "value": "skills", "key": category}

class Database():
    def __init__(self) -> None:
        self.redis_database = Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

    def close(self):
        self.redis_database.close()
    
    def clear(self):
        self.redis_database.flushall()
    
    def adapt(self, value: dict | list | str) -> str:
        if type(value) == dict or type(value) == list:
            return json.dumps(value)
        return value
    
    def get_int(self, key: dict | str):
        response = self.redis_database.get(self.adapt(key))
        return int(response) if response != None else None
    
    def get_list(self, key: dict | str) -> list:
        response = self.redis_database.get(self.adapt(key))
        if not response: return []
        return json.loads(response.decode("utf-8"))
    
    def set(self, key: dict | str, value: dict | list | str | int):
        self.redis_database.set(self.adapt(key), self.adapt(value))