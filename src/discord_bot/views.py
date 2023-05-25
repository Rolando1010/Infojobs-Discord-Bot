from discord import Embed, Color, Colour, ButtonStyle, Interaction, app_commands
from discord.ui import View, button, Button
from typing import Callable, List
from jobs.offers import Offer, search_offers
import numpy
def get_commands_embed():
    commands_embed = Embed(
        title="Lista de comandos",
        description="""
            Puedes acceder a los servicios de infojobs a través de este bot
            Utiliza el '/' para ejecutar cada comando
        """,
        color=Color.dark_red()
    )
    commands_embed.add_field(name="", value="-"*70)
    commands_embed.add_field(name="Comandos", value="""
        Muestra la lista de comandos que puedes ejecutar
        **Commando:** /comandos,
    """, inline=False)
    commands_embed.add_field(name="", value="-"*70)
    commands_embed.add_field(name="Ofertas de trabajo", value="""
        Muestra la lista ofertas de trabajo disponibles
        **Commando:** /ofertas,
    """, inline=False)
    return commands_embed

def get_offers_embed(offers: list[Offer], total_pages: int, page: int, description: str):
    offers_embed = Embed(
        title=f"Ofertas de trabajo ({page}/{total_pages})",
        description=description,
        color=Color.dark_blue()
    )
    for offer in offers:
        salary_message = f"Salario de {offer.salary_min} a {offer.salary_max}" if offer.salary_min or offer.salary_max else "Salario no disponible"
        offers_embed.add_field(name="", value=f"""
            ***[{offer.title}]({offer.link})***
            [{offer.author.name}]({offer.author.link})
            ***id***: {offer.id}
            {offer.applications} aplicaciones
            {offer.get_salary_message()}
        """, inline=False)
        offers_embed.add_field(name="", value="-"*70, inline=False)
    return offers_embed

def get_offer_embed(offer: Offer):
    offer_embed = Embed(
        title=offer.title,
        url=offer.link,
        description="",
        color=Color.dark_teal(),
    )
    offer_embed.set_thumbnail(url=offer.author.logo)
    offer_embed.add_field(name="", value=f"[{offer.author.name}]({offer.author.link})", inline=False)
    offer_embed.add_field(name="", value=offer.country)
    offer_embed.add_field(name="", value=offer.category)
    offer_embed.add_field(name="", value="", inline=False)
    offer_embed.add_field(name="", value=offer.get_salary_message())
    offer_embed.add_field(name="", value=f"{offer.applications} aplicaciones")
    offer_embed.add_field(name="", value="", inline=False)
    description = offer.description[:200] + "..." if len(offer.description) > 100 else offer.description
    offer_embed.add_field(name="", value=description, inline=False)
    return offer_embed

def get_list_embed(title: str, description: str, color: int | Colour, items: list[str], thumbnail: str=None):
    list_embed = Embed(title=title, description=description, color=color)
    if thumbnail: list_embed.set_thumbnail(url=thumbnail)
    for item in items:
        list_embed.add_field(name="", value=f"* {item}", inline=False)
    return list_embed

class Pagination(View):
    def __init__(self, get_embed: Callable[[int], Embed], args: tuple = ()):
        super().__init__()
        self.page = 1
        self.get_embed = get_embed
        self.args = args
    
    @button(label="Atrás", style=ButtonStyle.primary)
    async def previous_page(self, interaction: Interaction, button: Button):
        if self.page > 1:
            self.page -= 1
            await interaction.response.edit_message(embed=self.get_embed(self.page, *self.args), view=self)

    @button(label="Siguiente", style=ButtonStyle.primary)
    async def next_page(self, interaction: Interaction, button: Button):
        self.page += 1
        await interaction.response.edit_message(embed=self.get_embed(self.page, *self.args), view=self)

class LanguagesRecommendationOffers(View):
    def __init__(self, languages: str):
        super().__init__()
        for language in languages:
            button = Button(label=f"Recomendaciones de {language}", style=ButtonStyle.green)
            button.callback = self.recommend_languages_offers(language)
            self.add_item(button)
    
    def recommend_languages_offers(self, language: str):
        async def action(interaction: Interaction):
            recommendation_offers = search_offers(language, 1)
            await interaction.response.send_message(embed=get_offers_embed(
                recommendation_offers,
                len(recommendation_offers) and 1,
                len(recommendation_offers) and 1,
                f"Recomendaciones para {language}" if len(recommendation_offers) else f"No hay recomendaciones para {language}"
            ), view=self)
        return action

def autocompletion(get_options: Callable[[], list[str]]):
    async def get_similar_options(interaction: Interaction, current: str) -> List[app_commands.Choice[str]]:
        similar = []
        options = get_options()
        for option in options:
            if current.lower() in option.lower():
                similar.append(app_commands.Choice(name=option, value=option))
        return similar[:10]
    return get_similar_options