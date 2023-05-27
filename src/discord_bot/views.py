from discord import Embed, ButtonStyle, Interaction, app_commands
from discord.ui import View, button, Button
from typing import Callable, List
from .embeds.offers import get_offers_embed
from jobs.offers import search_offers

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