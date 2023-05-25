from jobs.countries import get_countries, get_offers_country
from .charts import generate_chart
from .utils import attach_results_to_name

def generate_countries_categories():
    countries = get_countries()
    countries_offers_length: list[int] = []
    for country in countries:
        total_pages = 2
        countries_offers_length.append(0)
        for page in range(total_pages):
            offers, total_pages = get_offers_country(country, page)
            countries_offers_length[-1] += len(offers)
    generate_chart(
        "Ofertas por país",
        "Cantidad de ofertas por país",
        "offers_by_country",
        countries_offers_length,
        attach_results_to_name(countries, countries_offers_length)
    )