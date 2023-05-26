from jobs.requests import browserify_request, SEARCH_OFFERS_URL
from .charts import generate_chart
from .utils import attach_results_to_name

def generate_technologies_chart(title, description, image_name, technologies: list[str]):
    results_per_technology: list[int] = []
    for technology in technologies:
        response = browserify_request(f"{SEARCH_OFFERS_URL}?keyword={technology}")
        results_per_technology.append(response["overview"]["totalElements"])
    generate_chart(
        title,
        description,
        image_name,
        results_per_technology,
        attach_results_to_name(technologies, results_per_technology)
    )