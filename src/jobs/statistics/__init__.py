from .categories import generate_categories_chart
from .countries import generate_countries_chart
from .technologies import generate_technologies_chart

generate_categories_chart()
generate_countries_chart()
generate_technologies_chart(
    "Ofertas por lenguaje",
    "Cantidad de ofertas por lenguaje de programación",
    "offers_by_languages",
    ["Java", "Javascript", "Python", "Csharp", "Go", "Cpp", "Typescript"," PHP", "Ruby"]
)
generate_technologies_chart(
    "Ofertas por tecnología frontend",
    "Cantidad de ofertas por tecnología frontend",
    "offers_by_frontend",
    ["React", "Angular", "Vue", "Jquery", "Astro", "Nextjs", "Svelte"," Qwick"]
)
generate_technologies_chart(
    "Ofertas por tecnología backend",
    "Cantidad de ofertas por tecnología backend",
    "offers_by_backend",
    ["Node", "Django", "Flask", ".NET", "SpringBoot", "Nextjs", "Deno"," Ruby on Rails", "Laravel"]
)