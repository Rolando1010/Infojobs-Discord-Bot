from jobs.categories import get_categories, get_offers_category
from .charts import generate_chart
from .utils import attach_results_to_name

def generate_categories_chart():
    categories = get_categories()
    offers_categories_length: list[int] = []
    for category in categories:
        offers_categories_length.append(0)
        page = 1
        total_pages = 2
        while page <= total_pages:
            offers, total_pages = get_offers_category(category, page)
            offers_categories_length[-1] += len(offers)
            page += 1
    generate_chart(
        "Ofertas por categoría",
        "Cantidad de ofertas por categoría",
        "offers_by_categories",
        offers_categories_length,
        attach_results_to_name(categories, offers_categories_length)
    )