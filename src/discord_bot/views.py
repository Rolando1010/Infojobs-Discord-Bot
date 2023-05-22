from discord import Embed, Color, Colour, ButtonStyle, Interaction, app_commands
from discord.ui import View, button, Button
from typing import Callable, List
from jobs.offers import Offer

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
            {offer.applications} aplicaciones
            {salary_message}
        """, inline=False)
        offers_embed.add_field(name="", value="-"*70, inline=False)
    return offers_embed

def get_list_embed(title: str, description: str, color: int | Colour, items: list[str]):
    list_embed = Embed(title=title, description=description, color=color)
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
    
def autocompletion(get_options: Callable[[], list[str]]):
    async def get_similar_options(interaction: Interaction, current: str) -> List[app_commands.Choice[str]]:
        similar = []
        options = get_options()
        for option in options:
            if current.lower() in option.lower():
                similar.append(app_commands.Choice(name=option, value=option))
        return similar[:10]
    return get_similar_options