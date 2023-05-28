from discord import Interaction, Color
from discord_bot.embeds.list import get_list_embed
from discord_bot.bot import bot
from jobs.categories import get_categories

@bot.tree.command(name="categorias", description="Listado de categorías de ofertas de trabajo")
async def show_categories(interaction: Interaction):
    categories = get_categories()
    await interaction.response.send_message(embed=get_list_embed("Categorías", "", Color.dark_green(), categories))