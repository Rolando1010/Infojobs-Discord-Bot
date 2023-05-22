from discord import Interaction, app_commands
from jobs.offers import get_offers, search_offers
from jobs.categories import get_categories, get_offers_category
from jobs.skills import get_skills, get_offers_skill
from jobs.countries import get_countries, get_offers_country
from discord_bot.bot import bot
from discord_bot.views import get_offers_embed, Pagination, autocompletion

def get_all_offers_embed(page: int):
    offers, total_pages = get_offers(page)
    return get_offers_embed(offers, total_pages, page, "Todas las ofertas de trabajo disponibles")

def get_offers_category_embed(page: int, category: str):
    offers_category, total_pages = get_offers_category(category, page)
    return get_offers_embed(offers_category, total_pages, page, f"Ofertas de trabajo de la categorías {category}")

def get_offers_skill_embed(page: int, skill: str):
    offers_skill, total_pages = get_offers_skill(skill, page)
    return get_offers_embed(offers_skill, total_pages, page, f"Ofertas de trabajo de la habilidad {skill}")

def get_offers_country_embed(page: int, country: str):
    offers_country, total_pages = get_offers_country(country, page)
    return get_offers_embed(offers_country, total_pages, page, f"Ofertas de trabajo del país {country}")

def get_search_offers_embed(page: int, search: str):
    result_offers = search_offers(search, page)
    return get_offers_embed(result_offers[:10], "...", page, f"Ofertas de {search}")

class OfferCommandsGroup(app_commands.Group):
    @app_commands.command(name="todas", description="Muestra las ofertas de trabajo disponibles")
    async def all(self,interaction: Interaction):
        await interaction.response.send_message(embed=get_all_offers_embed(1), view=Pagination(get_all_offers_embed))
        
    @app_commands.command(name="categorias", description="Muestra las ofertas de trabajo disponibles de una categoría")
    @app_commands.autocomplete(categoria=autocompletion(get_categories))
    async def by_category(self, interaction: Interaction, categoria: str):
        await interaction.response.send_message(
            embed=get_offers_category_embed(1, categoria),
            view=Pagination(get_offers_category_embed, (categoria,))
        )

    @app_commands.command(name="habilidades", description="Muestra las ofertas de trabajo disponibles de una habilidad")
    @app_commands.autocomplete(habilidad=autocompletion(get_skills))
    async def by_skill(self, interaction: Interaction, habilidad: str):
        await interaction.response.send_message(
            embed=get_offers_skill_embed(1, habilidad),
            view=Pagination(get_offers_skill_embed, (habilidad,))
        )

    @app_commands.command(name="paises", description="Muestra las ofertas de trabajo disponibles de un país")
    @app_commands.autocomplete(pais=autocompletion(get_countries))
    async def by_country(self, interaction: Interaction, pais: str):
        await interaction.response.send_message(
            embed=get_offers_country_embed(1, pais),
            view=Pagination(get_offers_country_embed, (pais,))
        )
    
    @app_commands.command(name="buscar", description="Busca ofertas de trabajo por una palabra clave")
    @app_commands.describe(busqueda="Ingresa una palabra clave, ejemplo: Javascript")
    async def by_search(self, interaction: Interaction, busqueda: str):
        await interaction.response.send_message(
            embed=get_search_offers_embed(1, busqueda),
            view=Pagination(get_search_offers_embed, (busqueda,))
        )

offer_commands_group = OfferCommandsGroup(name="ofertas", description="Muestra las ofertas de trabajo disponibles")
bot.tree.add_command(offer_commands_group)