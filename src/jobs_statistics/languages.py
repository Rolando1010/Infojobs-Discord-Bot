from api_requests.browser import browserify_request
from api_requests.urls import SEARCH_OFFERS_URL
from .charts import generate_chart
from .utils import attach_results_to_name

LANGUAGES = ["Java", "Javascript", "Python", "Csharp", "GO", "Cpp", "Typescript"," PHP", "Ruby"]

def generate_languages_chart():
    results_per_language: list[int] = []
    for language in LANGUAGES:
        response = browserify_request(f"{SEARCH_OFFERS_URL}?keyword={language}")
        results_per_language.append(response["overview"]["totalElements"])
    generate_chart(
        "Ofertas por lenguaje",
        "Cantidad de ofertas por lenguaje de programación",
        "offers_by_language",
        results_per_language,
        attach_results_to_name(LANGUAGES, results_per_language)
    )